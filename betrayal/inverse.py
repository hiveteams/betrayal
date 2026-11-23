"""Inverse tasks: instead of reading beliefs off a story, write the events that produce them.

  plan     an opening scene and a list of target beliefs: write a script that makes them all true
  explain  a story with one step missing and facts about how it ends: write the missing step

Both are graded by simulation. The engine replays the story with the model's steps in place and
checks every target, so any script that works is accepted and no answer key can be wrong.
"""

from __future__ import annotations

import json
import random
import re
from dataclasses import replace
from itertools import product
from typing import Iterator, Optional

from .engine import NOBODY, Beliefs, Event, Path, all_paths, beliefs
from .generate import GenConfig, generate
from .questions import tier_of

Target = tuple[Path, int]
SCRIPT = re.compile(r"SCRIPT\s*:", re.IGNORECASE)
ROOM_STEPS = {"change": "set", "check": "see", "say": "tell"}


class ScriptError(Exception):
    """A script that cannot be read, or a story that cannot happen as told."""


def parse_script(text: str) -> Optional[list]:
    """The JSON array after the last SCRIPT: marker, or None."""
    marks = list(SCRIPT.finditer(text))
    if not marks:
        return None
    tail = text[marks[-1].end():]
    start, end = tail.find("["), tail.rfind("]")
    if start < 0 or end < start:
        return None
    try:
        steps = json.loads(tail[start:end + 1])
    except json.JSONDecodeError:
        return None
    return steps if isinstance(steps, list) else None


def _index(label: object, pool: list[str], what: str) -> int:
    wanted = str(label).strip().lower().removeprefix("the ")
    for index, known in enumerate(pool):
        if known.lower().removeprefix("the ") == wanted:
            return index
    raise ScriptError(f"unknown {what}: {label!r}")


def _people(step: dict, key: str, cast: list[str]) -> frozenset[int]:
    listed = step.get(key) or []
    if not isinstance(listed, list):
        raise ScriptError(f'"{key}" must be a list')
    return frozenset(_index(name, cast, "person") for name in listed)


def to_event(step: object, cast: list[str], values: list[str]) -> Event:
    """One written step as an engine event. A check's value and a claim's sincerity are settled at replay."""
    if not isinstance(step, dict):
        raise ScriptError("a step must be a JSON object")
    kind = step.get("step")
    if kind == "message":
        sender, receiver = _index(step.get("from"), cast, "person"), _index(step.get("to"), cast, "person")
        readers = _people(step, "secret_readers", cast)
        if sender == receiver or readers & {sender, receiver}:
            raise ScriptError("a message needs two different people, and its secret readers must be other people")
        value = _index(step.get("value"), values, "value")
        return Event("tell", 0, value, frozenset({sender, receiver}), readers, actor=sender, channel="private")
    if kind not in ROOM_STEPS:
        raise ScriptError(f"unknown step type: {kind!r}")
    actor = _index(step.get("who"), cast, "person")
    present, missed = _people(step, "present", cast), _people(step, "missed_by", cast)
    secret = _people(step, "secret_witnesses", cast)
    if actor not in present:
        raise ScriptError('"who" must be in "present"')
    if not missed <= present - {actor}:
        raise ScriptError('"missed_by" must name people in "present" other than "who"')
    if secret & present:
        raise ScriptError('"secret_witnesses" must not be in "present"')
    if kind == "say" and len(present) < 2:
        raise ScriptError('a "say" step needs at least one other person present')
    value = 0 if kind == "check" else _index(step.get("value"), values, "value")
    return Event(ROOM_STEPS[kind], 0, value, present - missed, secret, missed, actor=actor)


def to_step(event: Event, cast: list[str], values: list[str]) -> dict:
    """An engine event in the step language, for reference answers."""
    names = lambda agents: sorted(cast[a] for a in agents)  # noqa: E731
    if event.channel == "private":
        receiver = next(iter(event.overt - {event.actor}))
        return {
            "step": "message", "from": cast[event.actor], "to": cast[receiver],
            "value": values[event.value], "secret_readers": names(event.covert),
        }
    kind = next(name for name, engine_kind in ROOM_STEPS.items() if engine_kind == event.kind)
    step = {"step": kind, "who": cast[event.actor]}
    if kind != "check":
        step["value"] = values[event.value]
    return {
        **step, "present": names(event.overt | event.presumed),
        "missed_by": names(event.presumed), "secret_witnesses": names(event.covert),
    }


def advance(table: Beliefs, event: Event, written: bool, number: int) -> None:
    """Apply one event. Written steps take their open details from the state; given steps must fit it."""
    truth = table.reality(0)
    if event.kind == "set" and event.value == truth:
        raise ScriptError(f"step {number} moves the thing to where it already is")
    if event.kind == "see":
        if written:
            event = replace(event, value=truth)
        elif event.value != truth:
            raise ScriptError(f"step {number} shows a value that is not the true one at that point")
    if event.kind == "tell":
        honest = table.get((event.actor,), 0) == event.value
        if written:
            event = replace(event, sincere=honest)
        elif honest != event.sincere:
            raise ScriptError(f"step {number} has a speaker who says something else than the story lets them believe")
    table.apply(event)


def replay(
    n_agents: int, events: list[Event], written: frozenset[int], max_order: int, only: Optional[list[Path]] = None
) -> Beliefs:
    table = Beliefs(n_agents, 1, max_order, only)
    for index, event in enumerate(events):
        advance(table, event, index in written, index + 1)
    return table


def met(table: Beliefs, targets: list[Target]) -> list[bool]:
    return [table.get(path, 0) == value for path, value in targets]


def dump_event(event: Event) -> dict:
    return {
        "kind": event.kind, "value": event.value, "overt": sorted(event.overt), "covert": sorted(event.covert),
        "presumed": sorted(event.presumed), "actor": event.actor, "sincere": event.sincere, "channel": event.channel,
    }


def load_event(data: dict) -> Event:
    return Event(
        data["kind"], 0, data["value"], frozenset(data["overt"]), frozenset(data["covert"]),
        frozenset(data["presumed"]), actor=data["actor"], sincere=data["sincere"], channel=data["channel"],
    )


def grade_script(item: dict, text: str) -> tuple[Optional[str], bool, str]:
    """(the script as text, whether it works, a short reason)."""
    steps = parse_script(text)
    if steps is None:
        return None, False, "no script"
    answer = json.dumps(steps, ensure_ascii=False)
    if not 1 <= len(steps) <= item["budget"]:
        return answer, False, f"{len(steps)} steps, allowed 1 to {item['budget']}"
    given, hole = [load_event(e) for e in item["given"]], item["hole"]
    targets = [(tuple(path), value) for path, value in item["targets"]]
    try:
        mine = [to_event(step, item["cast"], item["values"]) for step in steps]
        events = given[:hole] + mine + given[hole:]
        table = replay(len(item["cast"]), events, frozenset(range(hole, hole + len(mine))), item["max_order"])
    except ScriptError as error:
        return answer, False, str(error)
    hits = met(table, targets)
    return answer, all(hits), f"{sum(hits)}/{len(hits)} targets"


def choose_chains(table: Beliefs, rng: random.Random, n_agents: int, depth: int, n_chains: int) -> Optional[list[Path]]:
    """Belief chains of the given depth that no shorter chain explains, each led by a different person."""
    pool = [path for path in all_paths(n_agents, depth) if len(path) == depth and tier_of(table, path, 0) == 3]
    rng.shuffle(pool)
    chains: list[Path] = []
    for path in pool:
        if all(path[0] != chain[0] for chain in chains):
            chains.append(path)
        if len(chains) == n_chains:
            return chains
    return None


def targets_for(table: Beliefs, chains: list[Path], n_agents: int) -> list[Target]:
    """The true state, what each person thinks, and every level of each chain."""
    paths: list[Path] = [(), *[(agent,) for agent in range(n_agents)]]
    for chain in chains:
        paths.extend(chain[:length] for length in range(2, len(chain) + 1))
    return [(path, table.get(path, 0)) for path in dict.fromkeys(paths)]


def shortest_known(n_agents: int, events: list[Event], targets: list[Target], depth: int) -> list[Event]:
    """Drop every event the targets do not need. The result sets the step budget for a plan task."""
    kept = list(events)
    needed = [path for path, _ in targets] + [(agent,) for agent in range(n_agents)]
    for index in range(len(kept) - 1, 0, -1):
        trial = kept[:index] + kept[index + 1:]
        try:
            table = replay(n_agents, trial, frozenset(range(1, len(trial))), depth, needed)
        except ScriptError:
            continue
        if all(met(table, targets)):
            kept = trial
    return kept


def plan_task(seed: int, n_agents: int, n_events: int, depth: int, n_chains: int) -> Optional[dict]:
    cfg = GenConfig(n_agents=n_agents, n_events=n_events, max_order=depth)
    scenario = generate(seed, cfg)
    table = beliefs(n_agents, 1, scenario.events, depth)
    chains = choose_chains(table, random.Random(seed + 1), n_agents, depth, n_chains)
    if chains is None:
        return None
    targets = targets_for(table, chains, n_agents)
    reference = shortest_known(n_agents, scenario.events, targets, depth)
    return {
        "scenario": scenario, "given": reference[:1], "hole": 1, "reference": reference[1:],
        "targets": targets, "budget": len(reference) - 1, "max_order": depth,
    }


def all_steps(n_agents: int, n_values: int) -> Iterator[Event]:
    """Every step a script can hold, for counting how many would fill a gap."""
    agents = range(n_agents)
    for actor in agents:
        others = [a for a in agents if a != actor]
        for roles in product("omc-", repeat=len(others)):  # open witness, missed it, covert witness, away
            overt = frozenset({actor, *(a for a, role in zip(others, roles) if role == "o")})
            missed = frozenset(a for a, role in zip(others, roles) if role == "m")
            covert = frozenset(a for a, role in zip(others, roles) if role == "c")
            yield Event("see", 0, 0, overt, covert, missed, actor=actor)
            for value in range(n_values):
                yield Event("set", 0, value, overt, covert, missed, actor=actor)
                if len(overt | missed) > 1:
                    yield Event("tell", 0, value, overt, covert, missed, actor=actor)
        for receiver in others:
            rest = [a for a in others if a != receiver]
            for picks in product((False, True), repeat=len(rest)):
                readers = frozenset(a for a, picked in zip(rest, picks) if picked)
                for value in range(n_values):
                    yield Event("tell", 0, value, frozenset({actor, receiver}), readers, actor=actor, channel="private")


def fills(n_agents: int, n_values: int, events: list[Event], hole: int, watch: list[Path]) -> list[list]:
    """For every step that can sit in the gap without breaking the later steps: the beliefs it leads to on `watch`."""
    needed = watch + [(agent,) for agent in range(n_agents)]  # any speaker's own belief
    before = replay(n_agents, events[:hole], frozenset(), 0, needed)
    outcomes = []
    for candidate in all_steps(n_agents, n_values):
        table = before.copy()
        try:
            advance(table, candidate, True, hole + 1)
            for offset, event in enumerate(events[hole + 1:]):
                advance(table, event, False, hole + 2 + offset)
        except ScriptError:
            continue
        outcomes.append([table.get(path, 0) for path in watch])
    return outcomes


def explain_task(seed: int, n_agents: int, n_events: int, depth: int, n_facts: int, max_fits: int) -> Optional[dict]:
    """Hide one step, then state the end-of-story facts that leave the fewest steps able to fill the gap.

    The facts are picked greedily: each one rules out as many of the still-possible steps as it can.
    So they say who did not witness the hidden step as well as who did.
    """
    cfg = GenConfig(n_agents=n_agents, n_events=n_events, max_order=depth)
    scenario = generate(seed, cfg)
    events = scenario.events
    rng = random.Random(seed + 1)
    full = beliefs(n_agents, 1, events, depth)
    paths = all_paths(n_agents, depth)
    shallow = [path for path in paths if len(path) <= 2]
    deeper = [path for path in paths if len(path) > 2]
    watch: list[Path] = [(), *shallow, *rng.sample(deeper, min(len(deeper), 60))]
    truth = [full.get(path, 0) for path in watch]
    holes = list(range(1, len(events) - 1))  # never the last step: later steps must lean on the hidden one
    rng.shuffle(holes)
    for hole in holes:
        left = [outcome for outcome in fills(n_agents, cfg.n_values, events, hole, watch) if outcome[0] == truth[0]]
        chosen = [0]
        while len(chosen) < n_facts and len(left) > 1:
            gains = [sum(outcome[i] != truth[i] for outcome in left) for i in range(len(watch))]
            best = max(range(len(watch)), key=lambda i: (gains[i], rng.random()))
            if gains[best] == 0:
                break
            chosen.append(best)
            left = [outcome for outcome in left if outcome[best] == truth[best]]
        if len(left) <= max_fits and len(chosen) == n_facts:
            return {
                "scenario": scenario, "given": events[:hole] + events[hole + 1:], "hole": hole,
                "reference": [events[hole]], "targets": [(watch[i], truth[i]) for i in chosen],
                "budget": 1, "max_order": depth, "fits": len(left),
            }
    return None


PLAN_LEVELS = {  # n_agents, n_events, depth, n_chains
    1: (4, 5, 2, 1),
    2: (5, 7, 3, 2),
    3: (6, 12, 4, 3),
    4: (8, 22, 6, 5),
}
PLAN_MIN_STEPS = {1: 2, 2: 3, 3: 5, 4: 7}
EXPLAIN_LEVELS = {  # n_agents, n_events, depth, n_facts, most steps that may still fill the gap
    1: (4, 6, 2, 4, 40),
    2: (5, 8, 3, 6, 12),
    3: (5, 10, 4, 8, 6),
}


def make_task(kind: str, level: int, seed: int) -> Optional[dict]:
    if kind == "plan":
        task = plan_task(seed, *PLAN_LEVELS[level])
        return task if task and task["budget"] >= PLAN_MIN_STEPS[level] else None
    return explain_task(seed, *EXPLAIN_LEVELS[level])


def render_task(kind: str, task: dict, skin) -> dict:
    """Prompt and grading data for one plan or explain task."""
    cast, values = list(skin.names), skin.value_names()
    rules = "\n".join(f"- {rule}" for rule in skin.rules())
    help_lines = skin.step_help()
    steps = "\n".join(f"- {line}" for line in help_lines[:4])
    notes = "\n".join(
        f"- {line}"
        for line in [
            *help_lines[4:],
            'A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. '
            "The people who hear or read it believe it all the same.",
            f"The values are: {json.dumps(values, ensure_ascii=False)}. The names are: {json.dumps(sorted(cast))}.",
        ]
    )
    facts = "\n".join(f"{n}. {skin.claim(path, value)}" for n, (path, value) in enumerate(task["targets"], start=1))
    if kind == "plan":
        prompt = (
            "You direct a short scene. Write the steps that make a list of target beliefs come true.\n\n"
            "Scene so far:\n" + "\n".join(skin.log(upto=1)) + "\n\n"
            f"Rules of the scene:\n{rules}\n\n"
            f"Steps you can write, each as one JSON object:\n{steps}\n\nNotes on the steps:\n{notes}\n\n"
            f"Targets. After your last step, all of these must be true:\n{facts}\n\n"
            f"Write at least 1 and at most {task['budget']} steps. Any script that makes every target true is "
            "accepted.\n\n"
            "Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps."
        )
    else:
        prompt = (
            "One step of this story is missing. Work out a step that fits the gap.\n\n"
            f"Rules of the story world:\n{rules}\n\n"
            "Story:\n" + "\n".join(skin.log(hidden=frozenset({task["hole"]}))) + "\n\n"
            f"Facts at the end of the story:\n{facts}\n\n"
            f"The missing step is one of these types, each written as one JSON object:\n{steps}\n\n"
            f"Notes on the steps:\n{notes}\n\n"
            "Your step is accepted if, with it in the gap, every step of the story can happen as told under the "
            "rules and every fact above is true. For example, a person who tells something without wanting to "
            "mislead must believe it at that moment.\n\n"
            "Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one "
            "missing step."
        )
    return {
        "prompt": prompt,
        "cast": cast,
        "values": values,
        "given": [dump_event(event) for event in task["given"]],
        "hole": task["hole"],
        "targets": [[list(path), value] for path, value in task["targets"]],
        "budget": task["budget"],
        "max_order": task["max_order"],
        "gold": json.dumps([to_step(event, cast, values) for event in task["reference"]], ensure_ascii=False),
    }
