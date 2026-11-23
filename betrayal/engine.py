"""Epistemic engine: who believes what, to any depth.

A scenario is a list of events. Each event shows one value of one fact to a
witness structure:

  overt     O  witness it, and each of them takes everyone in O and P to witness it
  covert    C  witness it, and nobody else knows that they do
  presumed  P  do not witness it, but every witness takes them to witness it

A nested perspective is a tuple of agents (a1, a2, ..., ak), read as
"a1 thinks that a2 thinks that ... ak thinks". An event updates that perspective
when a1 really witnessed it and a1 takes every later agent in the chain to have
witnessed it too.

Two independent implementations live here. `beliefs` applies that rule directly.
`belief_ref` rebuilds each agent's subjective story and recurses into it. The test
suite checks that they agree on random event sequences.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Iterable, Optional

Path = tuple[int, ...]
NOBODY: frozenset[int] = frozenset()


@dataclass(frozen=True)
class Event:
    kind: str  # "set": the fact changes | "see": the current value is inspected | "tell": a value is claimed
    var: int
    value: int
    overt: frozenset[int]
    covert: frozenset[int] = NOBODY
    presumed: frozenset[int] = NOBODY
    actor: Optional[int] = None  # mover, inspector or speaker
    sincere: bool = True  # "tell" only; False means the speaker is lying
    channel: str = "room"  # "room": the shared space | "private": a message between two people

    def __post_init__(self) -> None:
        assert self.kind in ("set", "see", "tell"), self.kind
        assert not (self.overt & self.covert) and not (self.overt & self.presumed) and not (self.covert & self.presumed)
        assert self.actor is None or self.actor in self.overt
        assert self.sincere or self.kind == "tell"


def all_paths(n_agents: int, max_order: int) -> list[Path]:
    """Every chain of agents up to max_order long, with no agent directly repeated."""
    out: list[Path] = []

    def grow(path: Path) -> None:
        if path:
            out.append(path)
        if len(path) < max_order:
            for agent in range(n_agents):
                if not path or path[-1] != agent:
                    grow(path + (agent,))

    grow(())
    return out


class Beliefs:
    """Belief table for every perspective, updated one event at a time."""

    def __init__(self, n_agents: int, n_vars: int, max_order: int, only: Optional[Iterable[Path]] = None) -> None:
        """`only` limits the table to the given perspectives, for searches that replay many stories."""
        paths = all_paths(n_agents, max_order) if only is None else [path for path in only if path]
        self.table: dict[Path, list[Optional[int]]] = {path: [None] * n_vars for path in [(), *paths]}
        self.clock = 0  # number of events applied
        self.set_at = {path: [0] * n_vars for path in self.table}  # event that last set each belief
        self.jolted_at = {path: [0] * n_vars for path in self.table}  # event that last showed this view it was out of date

    def copy(self) -> "Beliefs":
        twin = Beliefs.__new__(Beliefs)
        twin.clock = self.clock
        for name in ("table", "set_at", "jolted_at"):
            setattr(twin, name, {path: list(values) for path, values in getattr(self, name).items()})
        return twin

    def apply(self, event: Event) -> None:
        self.clock += 1
        before = self.table[()][event.var]
        shown = before if event.kind == "set" else event.value  # a move shows where the thing was until now
        if event.kind == "set":
            self.table[()][event.var] = event.value
        witnesses = event.overt | event.covert
        taken_as_witnesses = event.overt | event.presumed
        for path, values in self.table.items():
            if not path or path[0] not in witnesses:
                continue
            if any(agent not in taken_as_witnesses for agent in path[1:]):
                continue
            if event.kind == "tell" and not event.sincere and path == (event.actor,):
                continue  # a liar keeps their own belief
            if before is not None and values[event.var] != shown:
                self.jolted_at[path][event.var] = self.clock
            values[event.var] = event.value
            self.set_at[path][event.var] = self.clock

    def get(self, path: Path, var: int) -> Optional[int]:
        return self.table[path][var]

    def settled(self, path: Path, var: int) -> bool:
        """False when a careful reader could contest the belief at `path`.

        The engine keeps a belief about another person until an event replaces it. That is safe while the
        holder saw each change and saw who else was there. It is open to doubt once the holder (or a person
        earlier in the chain) has learned of a change without seeing it happen, because then the holder
        cannot tell who else saw it.
        """
        since = self.set_at[path][var]
        return all(self.jolted_at[path[:depth]][var] <= since for depth in range(1, len(path)))

    def reality(self, var: int) -> Optional[int]:
        return self.table[()][var]


def beliefs(n_agents: int, n_vars: int, events: list[Event], max_order: int) -> Beliefs:
    table = Beliefs(n_agents, n_vars, max_order)
    for event in events:
        table.apply(event)
    return table


def _perceive(event: Event, agent: int) -> Optional[Event]:
    """The event as `agent` experiences it, or None when the agent misses it."""
    if agent in event.overt:
        covert = NOBODY
    elif agent in event.covert:
        covert = frozenset({agent})
    else:
        return None
    return replace(
        event,
        overt=event.overt | event.presumed,
        covert=covert,
        presumed=NOBODY,
        sincere=event.sincere if agent == event.actor else True,
    )


def belief_ref(path: Path, events: list[Event], var: int) -> Optional[int]:
    """Reference implementation: the belief at `path`, from nested subjective stories."""
    agent, rest = path[0], path[1:]
    story = [seen for event in events if (seen := _perceive(event, agent)) is not None]
    if rest:
        return belief_ref(rest, story, var)
    value: Optional[int] = None
    for event in story:
        if event.var != var:
            continue
        if event.kind == "tell" and event.actor == agent and not event.sincere:
            continue
        value = event.value
    return value


def reality_ref(events: list[Event], var: int) -> Optional[int]:
    value: Optional[int] = None
    for event in events:
        if event.var == var and event.kind == "set":
            value = event.value
    return value
