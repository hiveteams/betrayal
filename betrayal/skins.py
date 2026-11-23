"""Skins: turn an abstract scenario into a story and into question text.

Two surface forms share one engine:

  classic    objects in closed containers, people who come and go from a room
  workplace  facts about a team's work, set and passed on in calls and direct messages

Templates never use pronouns for people, so no name is given a gender.
"""

from __future__ import annotations

import random
from typing import Optional

from .engine import Path
from .generate import Scenario, Step

NAMES = [
    "Amara", "Bruno", "Chidi", "Dalia", "Emeka", "Farah", "Goran", "Hana", "Ines", "Jonas", "Keiko", "Luca",
    "Mirela", "Nadim", "Oksana", "Pablo", "Quinn", "Rania", "Soren", "Tariq", "Uma", "Viktor", "Wanjiru",
    "Xavier", "Yara", "Zoltan",
]
ROOMS = ["kitchen", "study", "garage", "attic", "workshop", "greenhouse", "pantry", "cellar", "boathouse", "sunroom"]
CONTAINERS = [
    "red box", "blue drawer", "wicker basket", "green cupboard", "leather bag", "wooden chest", "grey locker",
    "canvas sack", "white cabinet", "black trunk",
]
TINS = ["round tin", "square tin", "tall tin", "flat tin", "copper tin", "striped tin"]
OBJECTS = [
    "marble", "whistle", "compass", "medal", "thimble", "stopwatch", "harmonica", "magnet", "padlock", "token",
    "brooch", "torch",
]

# Workplace facts. `state` is a clause; `set` and `intro` are verb phrases; `head`/`tail` wrap a belief chain.
# Changes never name the old value: it is not needed, and it would invite guesses about who changed what.
FACTS = [
    {
        "values": ["Room Alder", "Room Birch", "Room Cedar", "Room Dogwood", "Room Elm", "Room Fir"],
        "state": "the client workshop is booked in {v}",
        "set": "moves the client workshop to {new}",
        "intro": "books the client workshop into {new}",
        "system": "booking system",
        "real": "which room is the client workshop really booked in",
        "head": "which room does",
        "tail": "the client workshop is booked in",
        "ask": "which room the client workshop is booked in",
    },
    {
        "values": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "state": "the product release is set for {v}",
        "set": "moves the product release to {new}",
        "intro": "sets the product release for {new}",
        "system": "release calendar",
        "real": "which day is the product release really set for",
        "head": "which day does",
        "tail": "the product release is set for",
        "ask": "which day the product release is set for",
    },
    {
        "values": ["Northwind", "Halcyon", "Brightwater", "Ironbridge", "Sablewood"],
        "state": "the packaging supplier is {v}",
        "set": "switches the packaging supplier to {new}",
        "intro": "picks {new} as the packaging supplier",
        "system": "supplier register",
        "real": "which company is really the packaging supplier",
        "head": "which company does",
        "tail": "is the packaging supplier",
        "ask": "which company is the packaging supplier",
    },
    {
        "values": ["Porto", "Ghent", "Leeds", "Turin", "Graz"],
        "state": "the team offsite is in {v}",
        "set": "moves the team offsite to {new}",
        "intro": "fixes {new} as the place for the team offsite",
        "system": "travel plan",
        "real": "which city is the team offsite really in",
        "head": "which city does",
        "tail": "the team offsite is in",
        "ask": "which city the team offsite is in",
    },
    {
        "values": ["5%", "10%", "15%", "20%", "25%"],
        "state": "the discount on the Fenwick quote is {v}",
        "set": "changes the discount on the Fenwick quote to {new}",
        "intro": "sets the discount on the Fenwick quote at {new}",
        "system": "quote record",
        "real": "what discount is really on the Fenwick quote",
        "head": "what discount does",
        "tail": "is on the Fenwick quote",
        "ask": "what discount is on the Fenwick quote",
    },
    {
        "values": ["the Lisbon office", "the Denver office", "the Osaka office", "the Nairobi office"],
        "state": "the Marlow account is with {v}",
        "set": "reassigns the Marlow account to {new}",
        "intro": "assigns the Marlow account to {new}",
        "system": "account list",
        "real": "which office really has the Marlow account",
        "head": "which office does",
        "tail": "has the Marlow account",
        "ask": "which office has the Marlow account",
    },
]

SHARED_RULES = [
    "People say what they believe, unless the story says that they want to mislead.",
    "People believe what they see. They also believe what they are told and what they overhear. Nobody suspects "
    "a lie or a mistake. Newer information replaces what a person believed before.",
    "Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a "
    "person who hears that something has changed does not work out who changed it or who else knows.",
]


def join(names: list[str]) -> str:
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " and " + names[-1]


def cap(text: str) -> str:
    return text[0].upper() + text[1:]


class Skin:
    key = ""

    def __init__(self, scenario: Scenario, rng: random.Random) -> None:
        self.scenario = scenario
        self.names = rng.sample(NAMES, scenario.cfg.n_agents)

    def people(self, agents) -> str:
        return join([self.names[a] for a in sorted(agents)])

    def chain(self, path: Path) -> str:
        """'Amara think that Bruno thinks that Chidi thinks' (the caller supplies 'does')."""
        first, rest = path[0], path[1:]
        return self.names[first] + " think" + "".join(f" that {self.names[a]} thinks" for a in rest)

    def thinks(self, path: Path) -> str:
        """'Amara thinks that Bruno thinks'."""
        return " that ".join(f"{self.names[a]} thinks" for a in path)

    def story(self) -> str:
        return "\n".join(self.lines())

    def lines(self) -> list[str]:
        raise NotImplementedError

    def log(self, hidden: frozenset[int] = frozenset(), upto: Optional[int] = None) -> list[str]:
        """The story as numbered steps that each say who is there. Hidden steps show as gaps."""
        lines = [self.log_header()]
        for number, step in enumerate(self.scenario.steps[:upto], start=1):
            text = "[A step is missing here.]" if number - 1 in hidden else " ".join(self.log_step(step))
            lines.append(f"{number}. {text}")
        return lines


class Classic(Skin):
    key = "classic"

    def __init__(self, scenario: Scenario, rng: random.Random) -> None:
        super().__init__(scenario, rng)
        cfg = scenario.cfg
        self.room = rng.choice(ROOMS)
        self.objects = rng.sample(OBJECTS, cfg.n_vars)
        self.places = [rng.sample(CONTAINERS, cfg.n_values)]
        if cfg.n_vars == 2:
            self.places.append(rng.sample(TINS, cfg.n_values))

    def rules(self) -> list[str]:
        room = self.room
        return [
            "Nobody can see into a closed container. A person learns where a thing is only by watching it being "
            "put there, by seeing inside the containers, or by being told.",
            f"People in the {room} see and hear everything that happens there, unless the story says that a person "
            f"missed it. People outside the {room} see and hear nothing of it, unless the story says so.",
            f"Everyone in the {room} can see who else is in the {room}.",
            "Text messages are private. The person who gets one reads it at once, and the sender knows this.",
            *SHARED_RULES,
        ]

    def value_label(self, var: int, value: int) -> str:
        return f"the {self.places[var][value]}"

    def _every(self, var: int) -> str:
        if self.scenario.cfg.n_vars == 1:
            return "every container"
        return "every tin on the shelf" if var else "every container on the floor"

    def _setting(self) -> str:
        room = self.room
        floor = join([f"the {c}" for c in self.places[0]])
        if self.scenario.cfg.n_vars == 1:
            return f"The {room} has four closed containers that nobody can see into: {floor}."
        shelf = join([f"the {c}" for c in self.places[1]])
        return (
            f"On the floor of the {room} there are four closed containers that nobody can see into: {floor}. "
            f"On a shelf there are four closed tins that nobody can see into: {shelf}. The tins are empty at "
            f"the start, and the {self.objects[0]} is only ever kept in the containers on the floor."
        )

    def log_header(self) -> str:
        everyone = self.people(range(self.scenario.cfg.n_agents))
        return f"{everyone} share a house. {self._setting()} This is what happened, in order."

    def log_step(self, step: Step) -> list[str]:
        event = step.event
        if event.channel == "private":
            return self._event(step)
        if step.occupancy == {event.actor}:
            presence = f"{self.names[event.actor]} is alone in the {self.room}."
        else:
            presence = f"{self.people(step.occupancy)} are in the {self.room}."
        return [presence, *self._event(step)]

    def claim(self, path: Path, value: int) -> str:
        place = self.value_label(0, value)
        if not path:
            return f"The {self.objects[0]} is really in {place}."
        return f"{self.thinks(path)} the {self.objects[0]} is in {place}."

    def value_names(self) -> list[str]:
        return list(self.places[0])

    def step_help(self) -> list[str]:
        room, thing = self.room, self.objects[0]
        return [
            '{"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], '
            f'"secret_witnesses": [NAMES]}}\n  NAME moves the {thing} to PLACE, which must not be the place where it '
            "already is.",
            '{"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}\n'
            f"  NAME opens every container in full view of the {room}, which shows where the {thing} really is.",
            '{"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], '
            f'"secret_witnesses": [NAMES]}}\n  NAME says out loud to everyone in the {room} that the {thing} is in '
            "PLACE. At least one other person must be present.",
            '{"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}\n'
            f"  One person sends another a private text message that says the {thing} is in PLACE.",
            f'"present" lists everyone who is in the {room} at that step, NAME included. "missed_by" lists people in '
            f'the {room} who do not notice the step, while nobody realises that they missed it. "secret_witnesses" '
            f"lists people outside the {room} who watch and hear the step through the window, while nobody knows "
            'that they do. "secret_readers" lists people who read a message on the receiver\'s phone, while the '
            "sender and the receiver never know.",
            f"Between steps, people go in and out of the {room} freely. That is not a step and nobody learns "
            "anything from it.",
        ]

    def lines(self) -> list[str]:
        scenario, room = self.scenario, self.room
        everyone = self.people(range(scenario.cfg.n_agents))
        setting = self._setting()
        opening = scenario.steps[0].event
        lines = [
            f"{everyone} are in the {room}. {setting}",
            f"While everyone watches, {self.names[opening.actor]} puts a {self.objects[0]} in "
            f"{self.value_label(0, opening.value)}.",
        ]
        present = scenario.steps[0].occupancy
        for step in scenario.steps[1:]:
            parts = []
            leavers, enterers = present - step.occupancy, step.occupancy - present
            if leavers:
                parts.append(f"{self.people(leavers)} {'leaves' if len(leavers) == 1 else 'leave'} the {room}.")
            if enterers:
                parts.append(
                    f"{self.people(enterers)} {'comes' if len(enterers) == 1 else 'come'} back into the {room}."
                )
            present = step.occupancy
            parts.extend(self._event(step))
            lines.append(" ".join(parts))
        return lines

    def _event(self, step: Step) -> list[str]:
        event, room = step.event, self.room
        actor, thing = self.names[event.actor], self.objects[event.var]
        place = self.value_label(event.var, event.value)
        if event.kind == "tell":
            said = f"“The {thing} is in {place}.”"
            if event.channel == "private":
                listener = self.names[next(iter(event.overt - {event.actor}))]
                lead = f"{actor} wants to mislead {listener}, so {actor} sends" if not event.sincere else f"{actor} sends"
                parts = [f"{lead} {listener} a private text message: {said}"]
                for reader in sorted(event.covert):
                    parts.append(
                        f"{self.names[reader]} secretly reads this message on {listener}'s phone. Neither {actor} "
                        f"nor {listener} ever knows that {self.names[reader]} read it."
                    )
                return parts
            parts = [f"{actor} says out loud to everyone in the {room}: {said}"]
            missed = f"is in the {room} but is wearing earphones and does not hear this"
            spying = "is outside but watches and hears all of this through the open window"
            spy_verb = "listening"
        else:
            if event.kind == "see":
                where = self._every(event.var)
                if event.overt == {event.actor}:
                    parts = [f"{actor} opens {where} and sees that the {thing} is in {place}."]
                else:
                    parts = [f"{actor} opens {where} in full view of the {room}, showing that the {thing} is in {place}."]
            elif step.first:
                parts = [f"{actor} takes a {thing} out of a pocket and puts it in {place}."]
            else:
                parts = [f"{actor} moves the {thing} to {place}."]
            missed = f"is in the {room} but is absorbed in a phone and does not notice this"
            spying = "is outside but watches all of this through the window"
            spy_verb = "watching"
        for agent in sorted(event.presumed):
            name = self.names[agent]
            parts.append(f"{name} {missed}. Nobody realises that {name} missed it.")
        for agent in sorted(event.covert):
            name = self.names[agent]
            parts.append(f"{name} {spying}. Nobody knows that {name} is {spy_verb}.")
        return parts

    def q_reality(self, var: int) -> str:
        return f"At the end of the story, where is the {self.objects[var]} really?"

    def q_belief(self, path: Path, var: int) -> str:
        return f"At the end of the story, where does {self.chain(path)} the {self.objects[var]} is?"

    def q_action(self, path: Path, var: int) -> str:
        thing = self.objects[var]
        if len(path) == 1:
            name = self.names[path[0]]
            return (
                f"At the end of the story, {name} needs the {thing} and goes to fetch it. "
                f"Which container does {name} open first?"
            )
        waiter, fetcher = self.names[path[0]], self.names[path[1]]
        return (
            f"At the end of the story, {fetcher} is about to fetch the {thing}. {waiter} wants to be waiting beside "
            f"the container that {fetcher} will open first, and must pick the spot before {fetcher} moves. "
            f"Beside which container does {waiter} wait?"
        )

    def q_inform(self, agent: int, var: int) -> str:
        name = self.names[agent]
        return (
            f"At the end of the story, {name} wants everybody else to share {name}'s own view of where the "
            f"{self.objects[var]} is. {name} sends a private note to every person who, as far as {name} can tell, "
            f"thinks something different or has no idea at all, and to nobody else. Who gets a note from {name}?"
        )

    def no_idea(self, path: Path, var: int) -> str:
        thing = self.objects[var]
        if len(path) == 1:
            return f"{self.names[path[0]]} has no idea where the {thing} is"
        return f"{self.names[path[0]]} thinks that {self.names[path[1]]} has no idea where the {thing} is"


class Workplace(Skin):
    key = "workplace"

    def __init__(self, scenario: Scenario, rng: random.Random) -> None:
        super().__init__(scenario, rng)
        cfg = scenario.cfg
        self.facts = rng.sample(FACTS, cfg.n_vars)
        self.values = [rng.sample(fact["values"], cfg.n_values) for fact in self.facts]

    def rules(self) -> list[str]:
        return [
            "A person learns a fact only by being on a call where it is set, read out or said, by checking a "
            "system, or by being told.",
            "People on a call hear everything that happens on it, unless the story says that a person missed it. "
            "People who are not on a call learn nothing about it, unless the story says so.",
            "Everyone on a call can see who else is on it.",
            "Direct messages are private. The person who gets one reads it at once, and the sender knows this.",
            *SHARED_RULES,
        ]

    def value_label(self, var: int, value: int) -> str:
        return self.values[var][value]

    def _state(self, var: int, value: int) -> str:
        return self.facts[var]["state"].format(v=self.value_label(var, value))

    def lines(self) -> list[str]:
        return self.log()

    def log_header(self) -> str:
        everyone = self.people(range(self.scenario.cfg.n_agents))
        return f"{everyone} work on the same team. This is what happened, in order."

    def log_step(self, step: Step) -> list[str]:
        return self._event(step)

    def claim(self, path: Path, value: int) -> str:
        state = self._state(0, value)
        if not path:
            return cap(state.replace(" is ", " is really ", 1)) + "."
        return f"{self.thinks(path)} {state}."

    def value_names(self) -> list[str]:
        return list(self.values[0])

    def step_help(self) -> list[str]:
        fact = self.facts[0]
        state = fact["state"].format(v="VALUE")
        return [
            '{"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], '
            f'"secret_witnesses": [NAMES]}}\n  NAME {fact["set"].format(new="VALUE")}, which must not be the value '
            "it already has.",
            '{"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}\n'
            f"  NAME opens the {fact['system']} and reads it out, which shows the true value.",
            '{"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], '
            f'"secret_witnesses": [NAMES]}}\n  NAME says on a call that {state}. At least one other person must be '
            "present.",
            '{"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}\n'
            f"  One person sends another a direct message that says {state}.",
            '"present" lists everyone on the call at that step, NAME included. A "present" list with only NAME '
            'means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the '
            'step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who '
            "secretly listen in and can see who is on it (or who secretly watch the screen of a person who works "
            'alone), while nobody knows that they do. "secret_readers" lists people who read a message on the '
            "receiver's screen, while the sender and the receiver never know.",
            "Every call is a new call with its own list of people.",
        ]

    def _event(self, step: Step) -> list[str]:
        event = step.event
        actor, fact = self.names[event.actor], self.facts[event.var]
        new = self.value_label(event.var, event.value)
        said = f"“{cap(self._state(event.var, event.value))}.”"
        if event.channel == "private":
            listener = self.names[next(iter(event.overt - {event.actor}))]
            lead = f"{actor} wants to mislead {listener}, so {actor} sends" if not event.sincere else f"{actor} sends"
            parts = [f"{lead} {listener} a direct message: {said}"]
            for reader in sorted(event.covert):
                parts.append(
                    f"{self.names[reader]} secretly reads this message on {listener}'s screen. Neither {actor} nor "
                    f"{listener} ever knows that {self.names[reader]} read it."
                )
            return parts
        alone = step.occupancy == {event.actor}
        if event.kind == "tell":
            action, alone_action = f"says: {said}", ""
        elif event.kind == "see":
            action = f"opens the {fact['system']} and reads it out: {said}"
            alone_action = f"checks the {fact['system']} and sees that {self._state(event.var, event.value)}"
        else:
            action = (fact["intro"] if step.first else fact["set"]).format(new=new)
            alone_action = action + " and tells nobody"
        if alone:
            parts = [f"{actor}, working alone, {alone_action}."]
        else:
            ending = "" if action.endswith("”") else "."
            parts = [f"Call with {self.people(step.occupancy)}: {actor} {action}{ending}"]
        for agent in sorted(event.presumed):
            name = self.names[agent]
            parts.append(
                f"{name} is on the call but has stepped away from the desk and misses this. "
                f"Nobody realises that {name} missed it."
            )
        for agent in sorted(event.covert):
            name = self.names[agent]
            if alone:
                parts.append(
                    f"{name} secretly watches {actor}'s screen as this happens. Nobody knows that {name} is watching."
                )
            else:
                parts.append(
                    f"{name} is not on the call but secretly listens in, and can see who is on it. "
                    f"Nobody knows that {name} is listening."
                )
        return parts

    def q_reality(self, var: int) -> str:
        return f"At the end of the story, {self.facts[var]['real']}?"

    def q_belief(self, path: Path, var: int) -> str:
        fact = self.facts[var]
        return f"At the end of the story, {fact['head']} {self.chain(path)} {fact['tail']}?"

    def q_action(self, path: Path, var: int) -> str:
        ask = self.facts[var]["ask"]
        if len(path) == 1:
            name = self.names[path[0]]
            return (
                f"At the end of the story, a new client asks {name} {ask}. {name} answers honestly. "
                f"What does {name} say?"
            )
        writer, speaker = self.names[path[0]], self.names[path[1]]
        return (
            f"At the end of the story, a new client is about to ask {speaker} {ask}, and {speaker} will answer "
            f"honestly. Before {speaker} answers, {writer} writes down what {writer} expects {speaker} to say. "
            f"What does {writer} write?"
        )

    def q_inform(self, agent: int, var: int) -> str:
        name = self.names[agent]
        return (
            f"At the end of the story, {name} wants everybody else on the team to share {name}'s own view of "
            f"{self.facts[var]['ask']}. {name} sends a direct message to every person who, as far as {name} can "
            f"tell, thinks something different or has no idea at all, and to nobody else. "
            f"Who gets a message from {name}?"
        )

    def no_idea(self, path: Path, var: int) -> str:
        ask = self.facts[var]["ask"]
        if len(path) == 1:
            return f"{self.names[path[0]]} has no idea {ask}"
        return f"{self.names[path[0]]} thinks that {self.names[path[1]]} has no idea {ask}"


SKINS = {Classic.key: Classic, Workplace.key: Workplace}
