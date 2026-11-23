"""Scenario generator: a seeded random walk over who is present, what changes and who tells whom.

The generator works on abstract agents, facts and values. `skins.py` turns a scenario
into text. Every constraint below exists to keep the gold answers free of judgement calls:
a listener is never told something they are in a position to know is false, and a speaker
never tells a listener something the speaker takes them to know already.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional

from .engine import NOBODY, Beliefs, Event


@dataclass(frozen=True)
class GenConfig:
    n_agents: int = 5
    n_values: int = 4
    n_vars: int = 1  # 2 adds a second fact that first appears while some people are away
    n_events: int = 10  # events after the opening one
    max_order: int = 4
    p_churn: float = 0.6  # chance that people come or go before a shared-space event
    p_covert: float = 0.25
    p_presumed: float = 0.2
    p_lie: float = 0.3  # share of private messages that are lies
    w_set: float = 0.30
    w_see: float = 0.15
    w_tell_private: float = 0.35
    w_tell_public: float = 0.20


@dataclass(frozen=True)
class Step:
    occupancy: frozenset[int]  # who is in the shared space when the event happens
    event: Event
    first: bool  # the event brings its fact into the story


@dataclass(frozen=True)
class Scenario:
    seed: int
    cfg: GenConfig
    steps: tuple[Step, ...]

    @property
    def events(self) -> list[Event]:
        return [step.event for step in self.steps]


def generate(seed: int, cfg: GenConfig) -> Scenario:
    rng = random.Random(seed)
    agents = list(range(cfg.n_agents))
    occupancy = set(agents)
    table = Beliefs(cfg.n_agents, cfg.n_vars, cfg.max_order)
    steps: list[Step] = []
    introduced = [0]
    messaged: set[tuple[int, int, int]] = set()  # (speaker, listener, fact): nobody repeats or retracts a message

    def commit(event: Event, present: set[int]) -> None:
        nonlocal occupancy
        first = table.reality(event.var) is None
        table.apply(event)
        steps.append(Step(frozenset(present), event, first))
        occupancy = set(present)

    def churn() -> set[int]:
        present = set(occupancy)
        if rng.random() < cfg.p_churn:
            for _ in range(1 if rng.random() < 0.7 else 2):
                agent = rng.choice(agents)
                if agent in present and len(present) > 1:
                    present.discard(agent)
                else:
                    present.add(agent)
        return present

    def room_witnesses(present: set[int], actor: int) -> tuple[frozenset[int], frozenset[int], frozenset[int]]:
        presumed = NOBODY
        others = sorted(present - {actor})
        if others and rng.random() < cfg.p_presumed:
            presumed = frozenset({rng.choice(others)})
        covert = NOBODY
        outside = sorted(set(agents) - present)
        if outside and rng.random() < cfg.p_covert:
            covert = frozenset({rng.choice(outside)})
        return frozenset(present) - presumed, covert, presumed

    def knows_better(agent: int, var: int, value: int) -> bool:
        """The claim is false and this listener holds the true value, so acceptance would be a judgement call."""
        truth = table.reality(var)
        return value != truth and table.get((agent,), var) == truth

    def make_set() -> Optional[tuple[Event, set[int]]]:
        present = churn()
        actor = rng.choice(sorted(present))
        var = rng.choice(introduced)
        value = rng.choice([v for v in range(cfg.n_values) if v != table.reality(var)])
        overt, covert, presumed = room_witnesses(present, actor)
        return Event("set", var, value, overt, covert, presumed, actor=actor), present

    def make_intro() -> tuple[Event, set[int]]:
        """Fact 1 first appears with at least one person away, so someone has no idea about it."""
        size = rng.randint(2, cfg.n_agents - 1)
        present = set(rng.sample(agents, size))
        actor = rng.choice(sorted(present))
        overt, covert, presumed = room_witnesses(present, actor)
        return Event("set", 1, rng.randrange(cfg.n_values), overt, covert, presumed, actor=actor), present

    def make_see() -> Optional[tuple[Event, set[int]]]:
        present = churn()
        actor = rng.choice(sorted(present))
        var = rng.choice(introduced)
        truth = table.reality(var)
        overt, covert, presumed = room_witnesses(present, actor)
        if all(table.get((agent,), var) == truth for agent in overt | covert):
            return None  # nobody would learn anything
        return Event("see", var, truth, overt, covert, presumed, actor=actor), present

    def make_tell_private() -> Optional[tuple[Event, set[int]]]:
        var = rng.choice(introduced)
        speakers = [a for a in agents if table.get((a,), var) is not None]
        rng.shuffle(speakers)
        for speaker in speakers:
            own = table.get((speaker,), var)
            listeners = [a for a in agents if a != speaker]
            rng.shuffle(listeners)
            for listener in listeners:
                assumed = table.get((speaker, listener), var)
                if assumed == own or (speaker, listener, var) in messaged:
                    continue  # as far as the speaker knows, the listener has it already
                lie = rng.random() < cfg.p_lie
                value = rng.choice([v for v in range(cfg.n_values) if v not in (own, assumed)]) if lie else own
                if knows_better(listener, var, value):
                    continue
                covert = NOBODY
                if rng.random() < cfg.p_covert:
                    readers = [a for a in agents if a not in (speaker, listener) and not knows_better(a, var, value)]
                    if readers:
                        covert = frozenset({rng.choice(readers)})
                event = Event(
                    "tell", var, value, frozenset({speaker, listener}), covert,
                    actor=speaker, sincere=not lie, channel="private",
                )
                messaged.add((speaker, listener, var))
                return event, set(occupancy)
        return None

    def make_tell_public() -> Optional[tuple[Event, set[int]]]:
        present = churn()
        if len(present) < 3:
            return None
        var = rng.choice(introduced)
        speakers = [a for a in sorted(present) if table.get((a,), var) is not None]
        if not speakers:
            return None
        speaker = rng.choice(speakers)
        value = table.get((speaker,), var)
        overt, covert, presumed = room_witnesses(present, speaker)
        hearers = overt - {speaker}
        if not hearers or any(knows_better(a, var, value) for a in hearers | covert):
            return None
        if all(table.get((speaker, hearer), var) == value for hearer in hearers):
            return None  # as far as the speaker knows, everyone here has it already
        return Event("tell", var, value, overt, covert, presumed, actor=speaker), present

    makers = [make_set, make_see, make_tell_private, make_tell_public]
    weights = [cfg.w_set, cfg.w_see, cfg.w_tell_private, cfg.w_tell_public]

    opening = Event("set", 0, rng.randrange(cfg.n_values), frozenset(agents), actor=rng.choice(agents))
    commit(opening, set(agents))
    intro_at = rng.randint(2, max(2, cfg.n_events // 2)) if cfg.n_vars == 2 else None

    while len(steps) < cfg.n_events + 1:
        if len(steps) == intro_at:
            commit(*make_intro())
            introduced.append(1)
            continue
        made = rng.choices(makers, weights)[0]()
        if made is not None:
            commit(*made)

    return Scenario(seed, cfg, tuple(steps))
