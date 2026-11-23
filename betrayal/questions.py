"""Questions: choose what to ask about a scenario, compute the gold answers, build the prompts.

Each scenario gets the same slots, so every model answers a matched mix:

  reality            where the fact really stands (not a theory-of-mind question)
  k1..k4 hard        a belief chain of depth 1-4 that shortcuts get wrong
  k1..k4 control     a chain of the same depth that is true, or that a shortcut gets right
  act1, act2         the hard depth-1 and depth-2 chains again, asked as "what will this person do"
  inform             who a person would correct, which needs that person's view of everyone else
  know               two-fact scenarios only: a person who has no idea about the second fact

Tier says how many lazy strategies a belief question defeats:

  0  the answer is the true state
  1  false belief, but the innermost person's real belief gives the answer
  2  false belief, and only dropping one end of the chain gives the answer (or depth 1)
  3  false belief, and no shorter chain gives the answer
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional, Union

from .engine import Beliefs, Path, all_paths, beliefs
from .generate import Scenario
from .skins import Skin

LETTERS = "ABCDEF"
NOBODY_WORD = "NOBODY"
Gold = Union[int, None, frozenset]


@dataclass(frozen=True)
class Ask:
    slot: str
    kind: str  # reality | belief | action | inform
    var: int
    path: Path  # () for reality, (agent,) for inform
    order: int  # depth of belief the question needs; 0 for reality, 2 for inform
    tier: Optional[int]
    gold: Gold  # a value, None for "has no idea", or the set of people for inform


def tier_of(table: Beliefs, path: Path, var: int) -> int:
    answer, truth = table.get(path, var), table.reality(var)
    if answer == truth:
        return 0
    if len(path) == 1:
        return 2
    if answer == table.get(path[-1:], var):
        return 1
    if answer in (table.get(path[1:], var), table.get(path[:-1], var)):
        return 2
    return 3


def inform_set(table: Beliefs, agent: int, var: int, n_agents: int) -> frozenset[int]:
    own = table.get((agent,), var)
    return frozenset(x for x in range(n_agents) if x != agent and table.get((agent, x), var) != own)


def wrong_set(table: Beliefs, agent: int, var: int, n_agents: int) -> frozenset[int]:
    """Who really differs from the true state: the answer of a reader who ignores the agent's view."""
    truth = table.reality(var)
    return frozenset(x for x in range(n_agents) if x != agent and table.get((x,), var) != truth)


def pick(scenario: Scenario, rng: random.Random) -> Optional[list[Ask]]:
    """The questions for a scenario, or None when the scenario cannot fill every slot."""
    cfg = scenario.cfg
    table = beliefs(cfg.n_agents, cfg.n_vars, scenario.events, cfg.max_order)
    pools: dict[int, list[tuple[int, Path, int]]] = {k: [] for k in range(1, cfg.max_order + 1)}
    for path in all_paths(cfg.n_agents, cfg.max_order):
        for var in range(cfg.n_vars):
            if table.get(path, var) is not None:
                pools[len(path)].append((tier_of(table, path, var), path, var))

    reality_var = rng.randrange(cfg.n_vars)
    asks = [Ask("reality", "reality", reality_var, (), 0, None, table.reality(reality_var))]
    for order, pool in pools.items():
        hard_tier = max((t for t, _, _ in pool), default=0)
        controls = [c for c in pool if c[0] == 0] if order == 1 else [c for c in pool if c[0] <= 1]
        if hard_tier < 2 or not controls:
            return None
        if order > 1:  # even out true-belief controls and shortcut-solvable false beliefs
            wanted = rng.choice([0, 1])
            controls = [c for c in controls if c[0] == wanted] or controls
        for label, (tier, path, var) in (
            ("hard", rng.choice([c for c in pool if c[0] == hard_tier])),
            ("control", rng.choice(controls)),
        ):
            asks.append(Ask(f"k{order}-{label}", "belief", var, path, order, tier, table.get(path, var)))
            if label == "hard" and order <= 2:
                asks.append(Ask(f"act{order}", "action", var, path, order, tier, table.get(path, var)))

    informers = [
        (agent, var)
        for agent in range(cfg.n_agents)
        for var in range(cfg.n_vars)
        if table.get((agent,), var) is not None
        and inform_set(table, agent, var, cfg.n_agents) != wrong_set(table, agent, var, cfg.n_agents)
    ]
    if not informers:
        return None
    partial = [c for c in informers if 0 < len(inform_set(table, *c, cfg.n_agents)) < cfg.n_agents - 1]
    agent, var = rng.choice(partial or informers)
    asks.append(Ask("inform", "inform", var, (agent,), 2, None, inform_set(table, agent, var, cfg.n_agents)))

    if cfg.n_vars == 2:
        unaware = [(a,) for a in range(cfg.n_agents) if table.get((a,), 1) is None]
        thought_unaware = [
            (a, b)
            for a in range(cfg.n_agents)
            for b in range(cfg.n_agents)
            if a != b and table.get((a,), 1) is not None and table.get((a, b), 1) is None
        ]
        choices = [pool for pool in (unaware, thought_unaware) if pool]
        if not choices:
            return None
        path = rng.choice(rng.choice(choices))
        asks.append(Ask("know", "belief", 1, path, len(path), None, None))
    return asks


def shortcuts(table: Beliefs, scenario: Scenario, ask: Ask) -> dict[str, Gold]:
    """What each lazy strategy would answer, for error analysis."""
    if ask.kind == "inform":
        return {"omniscient": wrong_set(table, ask.path[0], ask.var, scenario.cfg.n_agents)}
    if not ask.path:
        return {"reality": table.reality(ask.var)}
    first = next(event.value for event in scenario.events if event.var == ask.var)
    return {
        "reality": table.reality(ask.var),
        "inner": table.get(ask.path[-1:], ask.var),
        "outer": table.get(ask.path[:1], ask.var),
        "first": first,
    }


def render(skin: Skin, ask: Ask, rng: random.Random) -> dict:
    """Prompt, options and gold answer text for one question."""
    scenario = skin.scenario
    cfg = scenario.cfg
    table = beliefs(cfg.n_agents, cfg.n_vars, scenario.events, cfg.max_order)
    if ask.kind == "reality":
        question = skin.q_reality(ask.var)
    elif ask.kind == "belief":
        question = skin.q_belief(ask.path, ask.var)
    elif ask.kind == "action":
        question = skin.q_action(ask.path, ask.var)
    else:
        question = skin.q_inform(ask.path[0], ask.var)

    head = (
        "You will read a short story and then answer one question about it.\n\n"
        "Rules of the story world:\n" + "\n".join(f"- {rule}" for rule in skin.rules()) + "\n\n"
        "Story:\n" + skin.story() + "\n\n"
        f"Question: {question}\n\n"
    )

    def people(agents: frozenset) -> str:
        return ", ".join(sorted(skin.names[a] for a in agents)) or NOBODY_WORD

    if ask.kind == "inform":
        prompt = head + (
            "Work it out, then finish with one last line in exactly this form. Name every person who gets one, "
            f"or write {NOBODY_WORD}:\nANSWER: <names separated by commas>"
        )
        lazy = {name: people(value) for name, value in shortcuts(table, scenario, ask).items()}
        return {"prompt": prompt, "options": [], "gold": people(ask.gold), "shortcuts": lazy}

    order = list(range(cfg.n_values))
    rng.shuffle(order)
    options = [skin.value_label(ask.var, value) for value in order]
    letter_of: dict[Gold, str] = {value: LETTERS[i] for i, value in enumerate(order)}
    if ask.kind == "belief" and ask.var == 1 and ask.order <= 2:
        options.append(skin.no_idea(ask.path, ask.var))
        letter_of[None] = LETTERS[len(order)]
    listing = "\n".join(f"{LETTERS[i]}. {option}" for i, option in enumerate(options))
    prompt = head + (
        f"Options:\n{listing}\n\n"
        "Work it out, then finish with one last line in exactly this form:\nANSWER: <letter>"
    )
    lazy = {name: letter_of.get(value, "-") for name, value in shortcuts(table, scenario, ask).items()}
    return {"prompt": prompt, "options": options, "gold": letter_of[ask.gold], "shortcuts": lazy}
