"""The Obvious part: everyday scenes whose answer any adult sees at once.

Twenty short situations, each in two versions that differ in one detail and so in their answer
(the person was out of the room, or watched through the window). No rules are stated: the reader
must know what people can see, hear and know in ordinary life. Picture items from `pictures.py`
ask the same kind of question about a drawing.

A wrong answer here needs no expert to judge it. The report prints every one in full.
"""

from __future__ import annotations

import json
import random
import re
from pathlib import Path
from typing import Callable

from . import pictures
from .questions import LETTERS
from .skins import NAMES

Scene = tuple[str, str, list[str]]  # story, question, options with the right one first

MOVED = [("car keys", "bowl by the door", "pocket of the blue coat", "kitchen drawer"),
         ("last bar of chocolate", "fridge", "top cupboard", "freezer"),
         ("passport", "desk drawer", "suitcase", "bookcase")]


def moved(n: list[str], v: int, twist: bool) -> Scene:
    thing, first, second, third = MOVED[v % 3]
    seen = f" {n[0]} has not gone far, and watches {n[1]} do this through the window." if twist else ""
    return (
        f"{n[0]} puts the {thing} in the {first} and goes out for a walk. While {n[0]} is out, {n[1]} moves the "
        f"{thing} to the {second}.{seen}",
        f"{n[0]} comes back and wants the {thing}. Where does {n[0]} look first?",
        [f"in the {second if twist else first}", f"in the {first if twist else second}", f"in the {third}"],
    )


def headphones(n: list[str], v: int, twist: bool) -> Scene:
    visitor, early, late = [("landlord", "two", "five"), ("plumber", "ten", "three"), ("piano tuner", "nine", "four")][v % 3]
    ears = (
        f"{n[0]} has just taken off a pair of headphones and listens" if twist
        else f"{n[0]} lies on the sofa with noise-cancelling headphones on, the music turned up loud and eyes shut, and does not stir"
    )
    return (
        f"{n[0]} and {n[1]} share a flat. Both know that the {visitor} will come at {early} o'clock. {n[1]}'s phone "
        f"rings, and {n[1]} takes the call in the living room. {ears}. After the call {n[1]} says out loud: \"That "
        f"was the {visitor}. The visit is at {late} o'clock now, not at {early}.\" Then {n[1]} leaves for work.",
        f"At what time does {n[0]} expect the {visitor}?",
        [f"at {late if twist else early} o'clock", f"at {early if twist else late} o'clock", f"{n[0]} does not expect the {visitor} at all"],
    )


def note(n: list[str], v: int, twist: bool) -> Scene:
    thing, place = [("charger", "hall cupboard"), ("bike lock", "garden shed"), ("library card", "desk drawer")][v % 3]
    fate = f"{n[0]} comes home and reads the note." if twist else f"A gust of wind blows the note under the fridge before {n[0]} comes home. {n[0]} never sees it."
    return (
        f"{n[1]} leaves a note for {n[0]} on the kitchen table: \"I put your {thing} in the {place}.\" {fate}",
        f"Does {n[0]} know where the {thing} is?",
        [f"Yes: in the {place}", f"No: {n[0]} does not know where it is", "Yes: under the fridge"] if twist
        else [f"No: {n[0]} does not know where it is", f"Yes: in the {place}", "Yes: under the fridge"],
    )


def secret_watcher(n: list[str], v: int, twist: bool) -> Scene:
    place = ["at the back of the wardrobe", "behind the paint tins in the garage", "under the spare bed"][v % 3]
    notice = f"{n[0]} looks up, their eyes meet, and they both laugh." if twist else f"{n[0]} is busy and does not notice {n[1]} at all."
    return (
        f"{n[0]} hides a birthday present for {n[1]} {place}. At that moment {n[1]} walks past the open door and sees "
        f"exactly where the present goes. {notice}",
        f"Does {n[0]} think that {n[1]} knows where the present is?",
        ["Yes", "No"] if twist else ["No", "Yes"],
    )


def party(n: list[str], v: int, twist: bool) -> Scene:
    told = f" At lunch, {n[1]} tells {n[4]} all about it." if twist else ""
    planners = f"{n[1]}, {n[2]} and {n[3]}"
    return (
        f"{planners} are planning a surprise party for their colleague {n[0]} on Friday. They have told nobody "
        f"else. {n[4]} started work in the office today.{told}",
        "Who knows about the party?",
        [f"{planners}, and also {n[4]}", f"only {planners}", f"{planners}, and also {n[0]}"] if twist
        else [f"only {planners}", f"{planners}, and also {n[4]}", f"{planners}, and also {n[0]}"],
    )


def cake(n: list[str], v: int, twist: bool) -> Scene:
    food = ["last slice of cake", "last doughnut", "last piece of pie"][v % 3]
    where = f"{n[1]} was in the garden and saw {n[0]} eat it through the window" if twist else f"{n[1]} was at work all day"
    return (
        f"{n[0]} eats the {food} that {n[1]} was saving. {where}. In the evening {n[1]} asks who ate it, and {n[0]} "
        "says: \"The dog got it.\"",
        f"Does {n[1]} know who really ate the {food}?",
        [f"Yes: {n[1]} knows that {n[0]} ate it", f"No: {n[1]} does not know that {n[0]} ate it"] if twist
        else [f"No: {n[1]} does not know that {n[0]} ate it", f"Yes: {n[1]} knows that {n[0]} ate it"],
    )


def tin(n: list[str], v: int, twist: bool) -> Scene:
    box, shown, inside = [("biscuit tin", "biscuits", "sewing things"), ("cereal box", "cereal", "crayons"), ("egg carton", "eggs", "golf balls")][v % 3]
    past = f"Yesterday {n[0]} watched {n[1]} do this." if twist else f"{n[0]} was away when {n[1]} did this."
    return (
        f"On the table is a closed {box} with a picture of {shown} on it. {n[1]} has taken out all the {shown} and "
        f"filled it with {inside}. {past} Now {n[0]} comes into the room and sees the closed {box}.",
        f"Before {n[0]} opens it, what does {n[0]} think is inside?",
        [inside if twist else shown, shown if twist else inside, "nothing at all"],
    )


def envelope(n: list[str], v: int, twist: bool) -> Scene:
    treat, truth = [("tickets for your favourite band", "a dentist's bill"), ("a voucher for a weekend away", "a parking fine"), ("a letter that says you got the job", "an advert for double glazing")][v % 3]
    story = (
        f"{n[1]} hands {n[0]} a sealed envelope and says: \"Open it later. It is {treat}.\" This is a joke: the "
        f"envelope holds {truth}. {n[0]} believes {n[1]}."
    )
    if twist:
        return story, f"How does {n[0]} feel just after opening the envelope?", ["let down", "delighted", "proud"]
    return story, f"How does {n[0]} feel while carrying the unopened envelope home?", ["pleased and excited", "worried and upset", "bored"]


def plan(n: list[str], v: int, twist: bool) -> Scene:
    first, second = [("cinema", "bowling alley"), ("station café", "pizza place"), ("museum steps", "park gate")][v % 3]
    told = (
        f"{n[1]} sends {n[2]} a message about the change, and {n[2]} answers: \"OK, see you there.\"" if twist
        else f"Each of them thinks that the other will tell {n[2]}, so nobody does."
    )
    return (
        f"{n[0]}, {n[1]} and {n[2]} agree to meet at the {first} at eight. Later {n[0]} and {n[1]} talk on the phone "
        f"and decide to meet at the {second}. {told}",
        f"Where does {n[2]} go at eight?",
        [f"to the {second if twist else first}", f"to the {first if twist else second}", f"{n[2]} stays at home"],
    )


def announcement(n: list[str], v: int, twist: bool) -> Scene:
    news = ["Friday's meeting is cancelled", "the office will close early on Thursday", "the deadline has moved to next month"][v % 3]
    how = (
        f"In the morning meeting, with {n[0]} and {n[1]} both in the room, the manager tells the whole team that {news}." if twist
        else f"The manager meets {n[0]} in the corridor and says quietly that {news}. Later the manager sends {n[1]} a "
        f"private message with the same news. {n[0]} and {n[1]} have not spoken to each other today."
    )
    return how, f"Does {n[0]} know that {n[1]} has heard this news?", ["Yes", "No"] if twist else ["No", "Yes"]


def across_table(n: list[str], v: int, twist: bool) -> Scene:
    thing = ["candle", "water jug", "bread basket"][v % 3]
    seats = (
        f"{n[0]} and {n[1]} sit side by side on a bench at a long table, with {n[1]} on {n[0]}'s right" if twist
        else f"{n[0]} and {n[1]} sit facing each other across a small table"
    )
    return (
        f"{seats}. A {thing} stands on the table, a little to {n[0]}'s left, where both can see it.",
        f"For {n[1]}, is the {thing} more to the left or more to the right?",
        ["more to the left", "more to the right"] if twist else ["more to the right", "more to the left"],
    )


def umbrella(n: list[str], v: int, twist: bool) -> Scene:
    thing = ["umbrella", "grey coat", "black rucksack"][v % 3]
    how = (
        f"{n[0]} has no {thing}. {n[0]} looks round, sees that {n[1]} is busy at the counter, takes {n[1]}'s {thing} and hurries out." if twist
        else f"{n[0]} and {n[1]} have {thing}s that look exactly the same, and both leave them by the café door. {n[0]} "
        f"leaves first, picks one up without a second look and goes home. It is {n[1]}'s."
    )
    return how, f"Did {n[0]} mean to take {n[1]}'s {thing}?", ["Yes, on purpose", "No, by mistake"] if twist else ["No, by mistake", "Yes, on purpose"]


def dry_cake(n: list[str], v: int, twist: bool) -> Scene:
    food, fault = [("lemon cake", "far too dry"), ("pot of soup", "much too salty"), ("loaf of bread", "as hard as a brick")][v % 3]
    how = (
        f"{n[0]} watches {n[1]} carry in a {food} and hears {n[1]} say: \"I made this last night.\" {n[0]} tastes it, "
        f"grins at {n[1]} and says: \"Yours is {fault}, as always.\"" if twist
        else f"{n[1]} has made a {food} for the office. {n[0]} arrives late, when it is already on the table with no "
        f"name on it. {n[0]} tastes it and says to {n[1]}: \"Who made this? It is {fault}.\""
    )
    return how, f"When {n[0]} said that, did {n[0]} know that {n[1]} had made it?", ["Yes", "No"] if twist else ["No", "Yes"]


def sofa(n: list[str], v: int, twist: bool) -> Scene:
    thing, place = [("remote control", "laundry basket"), ("biscuit jar", "piano stool"), ("car key", "flower pot")][v % 3]
    state = f"{n[0]} is fast asleep on the sofa and snores" if twist else f"{n[0]} lies on the sofa with eyes shut, wide awake, and listens"
    return (
        f"{state}. The two children think that {n[0]} is asleep. They whisper to each other that they have hidden "
        f"the {thing} in the {place}.",
        f"Does {n[0]} know where the {thing} is?",
        ["No", "Yes"] if twist else ["Yes", "No"],
    )


def sofa_children(n: list[str], v: int, twist: bool) -> Scene:
    story, asked, _ = sofa(n, v, False)
    if twist:
        story += f" Then {n[0]} sits up and says: \"I heard every word.\""
    return story, "At the end, do the children think that " + asked[5:], ["Yes", "No"] if twist else ["No", "Yes"]


def shoebox(n: list[str], v: int, twist: bool) -> Scene:
    second = f"Then {n[1]} lifts the lid and looks inside too." if twist else f"{n[1]} only picks the box up and shakes it. Something rattles."
    return (
        f"A closed shoebox is on the table. Neither {n[0]} nor {n[1]} has seen it before. {n[0]} lifts the lid, "
        f"looks inside and closes it again. {second}",
        "Who knows what is in the box?",
        [f"both {n[0]} and {n[1]}", f"only {n[0]}", f"only {n[1]}", "neither of them"] if twist
        else [f"only {n[0]}", f"both {n[0]} and {n[1]}", f"only {n[1]}", "neither of them"],
    )


def calendar(n: list[str], v: int, twist: bool) -> Scene:
    event, early, late = [("review", "2 pm", "4 pm"), ("client call", "11 am", "1 pm"), ("team lunch", "noon", "1.30 pm")][v % 3]
    seen = (
        f"{n[1]}'s phone shows the change at once, and {n[1]} replies: \"Thanks, {late} works.\"" if twist
        else f"{n[1]} is on a train with no signal all day and does not see the change."
    )
    return (
        f"At nine, {n[1]} looks at the shared calendar: the {event} is at {early}. At ten, {n[0]} moves the {event} to "
        f"{late} in the calendar. {seen}",
        f"At what time does {n[1]} expect the {event} to start?",
        [f"at {late if twist else early}", f"at {early if twist else late}", f"{n[1]} does not expect it at all"],
    )


def risotto(n: list[str], v: int, twist: bool) -> Scene:
    food, dish = [("mushrooms", "mushroom risotto"), ("fish", "fish pie"), ("coconut", "coconut curry")][v % 3]
    if twist:
        return (
            f"{n[0]} cannot stand {food}, and told {n[1]} so last week. Today {n[1]} is cross with {n[0]} and cooks "
            f"a big {dish} for dinner anyway.",
            f"Does {n[1]} expect {n[0]} to enjoy the dinner?", ["No", "Yes"],
        )
    return (
        f"{n[0]} cannot stand {food}, but has never told {n[1]}. {n[1]} wants to give {n[0]} a treat and cooks a big "
        f"{dish} for dinner.",
        f"Does {n[1]} expect {n[0]} to enjoy the dinner?", ["Yes", "No"],
    )


def scarf(n: list[str], v: int, twist: bool) -> Scene:
    gift = ["scarf", "painting", "hat"][v % 3]
    story = (
        f"{n[0]} spent a month making a {gift} for {n[1]}. {n[1]} thinks it is ugly, but smiles warmly and says: "
        f"\"I love it. Thank you!\" {n[0]} goes home happy."
    )
    if twist:
        return story, f"Does {n[1]} really like the {gift}?", ["No", "Yes"]
    return story, f"Does {n[0]} think that {n[1]} likes the {gift}?", ["Yes", "No"]


def newcomer(n: list[str], v: int, twist: bool) -> Scene:
    thing, place = [("spare key", "under the green flower pot"), ("door code", "written inside the cupboard door"), ("first-aid box", "on top of the fridge")][v % 3]
    arrival = (
        f"{n[2]} arrives an hour later, and {n[0]} tells {n[2]} the same thing." if twist
        else f"{n[2]} arrives an hour later. Nobody says anything to {n[2]} about it."
    )
    return (
        f"On the first day in the holiday house, {n[0]} tells {n[1]} where the {thing} is: {place}. {arrival}",
        f"Does {n[2]} know where the {thing} is?",
        ["Yes", f"No: {n[2]} has no idea"] if twist else [f"No: {n[2]} has no idea", "Yes"],
    )


FAMILIES: dict[str, tuple[Callable[[list[str], int, bool], Scene], str]] = {
    "moved while out": (moved, "false belief"),
    "headphones": (headphones, "false belief"),
    "lost note": (note, "knowledge"),
    "secret watcher": (secret_watcher, "belief about a belief"),
    "surprise party": (party, "knowledge"),
    "who ate it": (cake, "knowledge"),
    "wrong contents": (tin, "false belief"),
    "joke envelope": (envelope, "feeling"),
    "changed plan": (plan, "false belief"),
    "told in public": (announcement, "belief about a belief"),
    "across the table": (across_table, "point of view"),
    "wrong umbrella": (umbrella, "intention"),
    "dry cake": (dry_cake, "knowledge"),
    "awake on the sofa": (sofa, "knowledge"),
    "what the children think": (sofa_children, "belief about a belief"),
    "looked in the box": (shoebox, "knowledge"),
    "shared calendar": (calendar, "false belief"),
    "wrong dinner": (risotto, "belief about a wish"),
    "kind lie": (scarf, "belief about a feeling"),
    "newcomer": (newcomer, "knowledge"),
}
STORY_MIX = [(True, ""), (False, "away"), (True, ""), (False, "wall"), (True, ""), (False, "out")]


def build(seed: int, folder: Path, variants: int = 2, n_see: int = 12, n_story: int = 18, n_table: int = 10) -> list[dict]:
    """All items of the Obvious part. Pictures are written to `folder`."""
    folder.mkdir(parents=True, exist_ok=True)
    items = []
    for family, (make, skill) in FAMILIES.items():
        for variant in range(variants):
            for twist in (False, True):
                rng = random.Random(f"{seed}-{family}-{variant}-{twist}")
                story, question, options = make(rng.sample(NAMES, 5), variant + seed, twist)
                gold = options[0]
                rng.shuffle(options)
                listing = "\n".join(f"{LETTERS[i]}. {option}" for i, option in enumerate(options))
                items.append({
                    "kind": "everyday", "family": family, "skill": skill, "picture": None,
                    "question": f"{story}\n\n{question}\n\n{listing}", "answer_form": "one letter",
                    "choices": options, "gold": LETTERS[options.index(gold)],
                })
    picture_seed = seed * 1000
    items += [{**pictures.see_item(picture_seed + i, folder), "family": "who can see what", "skill": "point of view"} for i in range(n_see)]
    items += [
        {**pictures.story_item(picture_seed + i, folder, *STORY_MIX[i % len(STORY_MIX)]), "family": "picture story", "skill": "false belief"}
        for i in range(n_story)
    ]
    items += [{**pictures.table_item(picture_seed + i, folder), "family": "left and right at a table", "skill": "point of view"} for i in range(n_table)]
    random.Random(f"{seed}-order").shuffle(items)
    for number, item in enumerate(items, start=1):
        item.update({
            "id": f"Q{number:03d}", "scenario": f"Q{number:03d}", "part": "obvious", "level": item["kind"], "slot": item["family"],
            "images": [item["picture"]] if item["picture"] else [],
            "prompt": item["question"] + f"\n\nWork it out, then finish with one last line in exactly this form:\nANSWER: <{item['answer_form']}>",
        })
    return items


def grade_answer(item: dict, answer: str) -> tuple[str | None, bool]:
    """(the answer in the gold's form, whether it is right). None when the answer cannot be read."""
    raw = answer.strip().strip("*_`.").strip()
    if item["kind"] == "everyday":
        match = re.match(r"[(\[]?([A-F])(?![A-Za-z])", raw)
        read = match.group(1) if match and LETTERS.index(match.group(1)) < len(item["choices"]) else None
        if read is None:
            spelled = [LETTERS[i] for i, choice in enumerate(item["choices"]) if choice.lower() == raw.lower()]
            read = spelled[0] if spelled else None
    else:
        # a box or block may be named by its colour alone
        short = item["kind"] != "see"
        named = [c for c in item["choices"] if re.search(rf"\b{re.escape(c.split()[0] if short else c)}\b", raw, re.IGNORECASE)]
        if item["kind"] == "see":
            read = ", ".join(named) if named else ("NOTHING" if re.search(r"\b(nothing|none)\b", raw, re.IGNORECASE) else None)
        else:
            read = named[0] if len(named) == 1 else None
    return read, read == item["gold"]


def booklet(items: list[dict]) -> str:
    """The same questions as one document, for a model that works through them in one sitting."""
    parts = [
        "# BetrayalBench: the Obvious booklet\n",
        f"There are {len(items)} questions. Answer every one. Some questions name a picture file: open the picture "
        "and look at it. Each question says what form its answer takes.\n",
    ]
    for item in items:
        parts.append(f"## {item['id']}\n")
        if item["picture"]:
            parts.append(f"Picture file: {item['picture']}\n")
        parts.append(item["question"] + "\n")
        parts.append(f"Answer with: {item['answer_form']}.\n")
    return "\n".join(parts)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Build the Obvious part: items, pictures and the booklet.")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out", type=Path, default=Path("data/obvious-v1"))
    args = parser.parse_args()
    items = build(args.seed, (args.out / "pictures").resolve())
    (args.out / "items.jsonl").write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in items))
    (args.out / "booklet.md").write_text(booklet(items))
    print(f"{len(items)} items -> {args.out}")


if __name__ == "__main__":
    main()
