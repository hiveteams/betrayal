"""Sight: pictures where the task needs another person's point of view, and does not say so.

Asked outright ("are the keys on Ben's left or on his right?"), the models are right. So the scored
task never points at Ben's point of view. The model watches a room from above. Ben, who is in the
room, texts: "Any idea where my keys are?" The model writes the reply.

A person writes "behind you" or "on your left". A reply fails in one of two ways:

  map words   it uses the frame of the picture ("in the top right corner"), which means nothing to Ben
  wrong side  it names a side that is wrong from where Ben stands (the picture's left for Ben's left)

Each picture is also asked outright, as the control: `where` items have a nudge, so they show what a
model can do, and they are not part of the score.

  uv run python -m betrayal.sight --out data/sight-v1
"""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

from . import pictures
from .pictures import BOXES, DIRECTIONS, SIZE, SURFACE

SIDES = ("in front", "behind", "left", "right")
WATCH = (
    "You are watching this room on a camera in the ceiling, and the picture is what you see. Each person is a round head "
    "seen from above, with a pointed nose and two eyes on the side that the person faces."
)
MAP_WORDS = re.compile(
    r"\b(top|bottom|upper|lower|north|south|east|west|northern|southern|eastern|western|north-?east|north-?west|south-?east|south-?west)\b"
    r"|\b(of|in|on) the (picture|image|photo|frame|screen|camera view|map|diagram|feed)\b"
)
NOT_A_SIDE = re.compile(r"\bright (behind|in front|next|by|beside|there|at|near|on|under|where|now|away|here|around)\b|\ball right\b|\bthat's right\b")
SAID = {
    "in front": re.compile(r"in front of you|ahead of you|straight ahead|just ahead|directly ahead|right ahead"),
    "behind": re.compile(r"behind you|behind where you|turn around|at your back|in back of you"),
    "left": re.compile(r"\byour left\b|\bleft of you\b|\b(to|on) the left\b(?! of the)|\bturn left\b|\bleft[- ]hand\b"),
    "right": re.compile(r"\byour right\b|\bright of you\b|\b(to|on) the right\b(?! of the)|\bturn right\b|\bright[- ]hand\b"),
}


def place(person: tuple[int, int], facing: str, side: str, steps: int) -> tuple[int, int]:
    """The square that is `steps` squares from the person on that side of them. The picture has y down."""
    fx, fy = DIRECTIONS[facing]
    lx, ly = fy, -fx  # the left hand of a person who faces (fx, fy)
    dx, dy = {"in front": (fx, fy), "behind": (-fx, -fy), "left": (lx, ly), "right": (-lx, -ly)}[side]
    return person[0] + steps * dx, person[1] + steps * dy


def room(seed: int, folder: Path, facing: str, side: str) -> dict:
    """One room: Ben, his keys on one side of him, and two boxes that are not near the keys."""
    rng = random.Random(f"sight-{seed}")
    floor = [(x, y) for x in range(1, SIZE - 1) for y in range(1, SIZE - 1)]
    while True:
        ben, steps = (rng.randint(3, 5), rng.randint(3, 5)), rng.choice([2, 3])
        keys = place(ben, facing, side, steps)
        far = [c for c in floor if max(abs(c[0] - keys[0]), abs(c[1] - keys[1])) >= 3 and max(abs(c[0] - ben[0]), abs(c[1] - ben[1])) >= 2]
        if keys in floor and len(far) >= 2:
            break
    boxes = dict(zip(rng.sample(list(BOXES), 2), rng.sample(far, 2)))
    things = {"keys": (keys, pictures.THINGS["key"]), **{name: (spot, BOXES[name]) for name, spot in boxes.items()}}
    file = folder / f"room-{seed:04d}.png"
    pictures._room(set(), things, {"Ben": (ben, facing)}, 72, back=SURFACE).save(file)
    return {"picture": str(file), "facing": facing, "gold": side, "family": "where are my keys", "skill": "point of view"}


def build(seed: int, folder: Path, variants: int = 2) -> list[dict]:
    """Every facing with every side, `variants` times. Each room gives one scored item and one control."""
    folder.mkdir(parents=True, exist_ok=True)
    items, number = [], 0
    for variant in range(variants):
        for facing in DIRECTIONS:
            for side in SIDES:
                number += 1
                base = room(seed * 1000 + number, folder, facing, side)
                tell = (
                    f"{WATCH}\n\nBen has lost his keys. He texts you: \"Any idea where my keys are?\"\n\n"
                    "Write only your reply. It will be sent to Ben exactly as you write it."
                )
                where = (
                    f"{WATCH}\n\nFrom where Ben stands, and the way he faces, where are his keys: in front of him, behind him, "
                    "on his left or on his right?\n\nWork it out, then finish with one last line in exactly this form:\n"
                    "ANSWER: <in front, behind, left or right>"
                )
                for kind, prompt in (("tell", tell), ("where", where)):
                    items.append({
                        **base, "kind": kind, "id": f"{'T' if kind == 'tell' else 'W'}{number:03d}", "scenario": f"R{number:03d}",
                        "part": "sight", "level": kind, "slot": base["family"], "images": [base["picture"]], "question": prompt, "prompt": prompt,
                    })
    return items


def read(text: str) -> tuple[set[str], bool]:
    """The sides that a reply names from Ben's point of view, and whether it uses the frame of the picture."""
    plain = NOT_A_SIDE.sub(lambda match: match.group(1) or "", text.lower().replace("’", "'"))
    return {side for side, pattern in SAID.items() if pattern.search(plain)}, bool(MAP_WORDS.search(plain))


def grade(item: dict, text: str) -> tuple[str | None, bool, str]:
    """(what the reply did, whether it is right, the sides it named)."""
    if item["kind"] == "where":
        lines = re.findall(r"ANSWER\s*:\s*(.*)", text, re.IGNORECASE)
        named = [side for side in SIDES if lines and re.search(rf"\b{side.split()[-1]}\b", lines[-1].lower())]
        answer = named[0] if len(named) == 1 else None
        return answer, answer == item["gold"], ""
    said, map_words = read(text)
    if item["gold"] in said:
        answer = "his side"
    elif said:
        answer = "wrong side"
    elif map_words:
        answer = "map words"
    else:
        answer = "no side"  # a landmark or nothing: not a point-of-view error, and not a use of Ben's view
    return answer, answer == "his side", ", ".join(sorted(said)) + (" + map words" if map_words else "")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out", type=Path, default=Path("data/sight-v1"))
    args = parser.parse_args()
    items = build(args.seed, (args.out / "pictures").resolve())
    (args.out / "items.jsonl").write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in items))
    print(len(items), "items:", sum(item["kind"] == "tell" for item in items), "scored and as many controls")


if __name__ == "__main__":
    main()
