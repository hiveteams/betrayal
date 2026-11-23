"""Picture items: what a person can see, drawn so that the answer is plain at a glance.

Three kinds, all rooms or tables seen from above:

  see    one room: which of these things can this person see?
  story  two or three panels: a ball is moved between closed boxes while a person looks on, looks away,
         stands behind a wall or is out of the room. Where will that person look for the ball?
  table  people sit round a table: from this seat, which block is on the left?

Geometry decides every answer, and only clear cases are used: a sight line counts as open or
blocked only if it stays so when both of its ends are moved by 0.4 of a square and the walls are
made a little bigger or smaller.
"""

from __future__ import annotations

import random
from pathlib import Path
from typing import Optional

from PIL import Image, ImageDraw, ImageFont

SIZE = 9  # squares per side, the outer wall included
DIRECTIONS = {"north": (0, -1), "east": (1, 0), "south": (0, 1), "west": (-1, 0)}
PEOPLE = {"Ana": "#2a78d6", "Ben": "#eb6834", "Cleo": "#1baf7a", "Dev": "#6250d6"}
THINGS = {"key": "#eda100", "mug": "#1baf7a", "pen": "#e34948", "jar": "#6250d6", "hat": "#e87ba4", "lamp": "#eb6834", "fan": "#008300", "shoe": "#2a78d6"}
BOXES = {"red box": "#e34948", "blue box": "#2a78d6", "green box": "#008300"}
BLOCKS = {"red block": "#e34948", "blue block": "#2a78d6", "yellow block": "#eda100", "green block": "#008300"}
SURFACE, WALL, INK = "#fcfcfb", "#2b2b2b", "#0b0b0b"
Cell = tuple[int, int]

LEGEND = (
    "The dark blocks are walls. Each person is a round head seen from above, with a pointed nose and two eyes on "
    "the side that the person faces. A person can see a thing when it is in front of them and no wall is between "
    "them. Things, boxes and other people do not block the view."
)


def _crosses(start: tuple[float, float], end: tuple[float, float], wall: Cell, grow: float) -> bool:
    """Does the line pass through the wall square, grown (or shrunk) by `grow` on every side?"""
    low, high = 0.0, 1.0
    for origin, target, centre in ((start[0], end[0], wall[0]), (start[1], end[1], wall[1])):
        near, far, step = centre - 0.5 - grow, centre + 0.5 + grow, target - origin
        if abs(step) < 1e-9:
            if not near < origin < far:
                return False
            continue
        first, second = sorted(((near - origin) / step, (far - origin) / step))
        low, high = max(low, first), min(high, second)
        if low >= high:
            return False
    return True


def sees(person: Cell, facing: str, target: Cell, walls: set[Cell]) -> Optional[bool]:
    """True or False when the answer is plain, None when a careful person could hesitate."""
    dx, dy = target[0] - person[0], target[1] - person[1]
    fx, fy = DIRECTIONS[facing]
    ahead, aside = dx * fx + dy * fy, abs(dx * fy - dy * fx)
    if ahead <= -1 and aside <= 2 * -ahead:
        return False  # plainly behind
    if ahead < 1 or aside > ahead:
        return None  # off to the side
    nudges = [(-0.4, -0.4), (-0.4, 0.4), (0.4, -0.4), (0.4, 0.4), (0.0, 0.0)]
    lines = [((person[0] + a, person[1] + b), (target[0] + c, target[1] + d)) for a, b in nudges for c, d in nudges]
    if all(any(_crosses(start, end, wall, -0.15) for wall in walls) for start, end in lines):
        return False
    if not any(_crosses(start, end, wall, 0.15) for wall in walls for start, end in lines):
        return True
    return None


def _diagonal(person: Cell, facing: str, target: Cell) -> bool:
    """Exactly 45 degrees off the line of sight: in view for a person, but a strict reader of "in front" could say no."""
    dx, dy = target[0] - person[0], target[1] - person[1]
    fx, fy = DIRECTIONS[facing]
    return abs(dx * fy - dy * fx) == dx * fx + dy * fy


def _walls(rng: random.Random, pieces: int) -> set[Cell]:
    walls: set[Cell] = set()
    for _ in range(pieces):
        along_x, length = rng.random() < 0.5, rng.randint(2, 4)
        x, y = rng.randint(2, SIZE - 3), rng.randint(2, SIZE - 3)
        for step in range(length):
            cell = (x + step, y) if along_x else (x, y + step)
            if 1 <= cell[0] <= SIZE - 2 and 1 <= cell[1] <= SIZE - 2:
                walls.add(cell)
    return walls


def _floor(walls: set[Cell]) -> list[Cell]:
    return [(x, y) for x in range(1, SIZE - 1) for y in range(1, SIZE - 1) if (x, y) not in walls]


def _font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in ("/System/Library/Fonts/Helvetica.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _label(draw: ImageDraw.ImageDraw, centre: float, top: float, text: str, size: int, back: Optional[str] = None) -> None:
    """Centred text. `back` puts a patch of that colour behind it, so a name stays readable on a wall."""
    font = _font(size)
    left = centre - draw.textlength(text, font=font) / 2
    if back:
        box = draw.textbbox((left, top), text, font=font)
        draw.rounded_rectangle([box[0] - 3, box[1] - 2, box[2] + 3, box[3] + 2], radius=4, fill=back)
    draw.text((left, top), text, fill=INK, font=font)


def _room(walls: set[Cell], things: dict[str, tuple[Cell, str]], people: dict[str, tuple[Cell, str]], cell: int, back: Optional[str] = None) -> Image.Image:
    """One room. `things` maps a label to (square, colour); `people` maps a name to (square, facing)."""
    image = Image.new("RGB", (SIZE * cell, SIZE * cell), SURFACE)
    draw = ImageDraw.Draw(image)
    for x in range(SIZE):
        for y in range(SIZE):
            if x in (0, SIZE - 1) or y in (0, SIZE - 1) or (x, y) in walls:
                draw.rectangle([x * cell, y * cell, (x + 1) * cell, (y + 1) * cell], fill=WALL)
    unit = cell / 72
    labels: list[tuple[float, float, str]] = []
    for label, ((x, y), colour) in things.items():
        cx, cy = (x + 0.5) * cell, (y + 0.5) * cell
        draw.rounded_rectangle([cx - 18 * unit, cy - 24 * unit, cx + 18 * unit, cy + 6 * unit], radius=6 * unit, fill=colour)
        _label(draw, cx, cy + 8 * unit, label, round(16 * unit))
    for name, ((x, y), facing) in people.items():
        cx, cy = (x + 0.5) * cell, (y + 0.5) * cell - 6 * unit
        fx, fy = DIRECTIONS[facing]
        radius = 20 * unit
        nose = [
            (cx + fx * (radius + 16 * unit), cy + fy * (radius + 16 * unit)),
            (cx + fx * (radius - 4 * unit) - fy * 10 * unit, cy + fy * (radius - 4 * unit) + fx * 10 * unit),
            (cx + fx * (radius - 4 * unit) + fy * 10 * unit, cy + fy * (radius - 4 * unit) - fx * 10 * unit),
        ]
        draw.polygon(nose, fill=PEOPLE[name])
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=PEOPLE[name], outline=INK, width=2)
        for side in (-1, 1):
            ex, ey = cx + fx * 9 * unit - fy * 8 * unit * side, cy + fy * 9 * unit + fx * 8 * unit * side
            draw.ellipse([ex - 3.5 * unit, ey - 3.5 * unit, ex + 3.5 * unit, ey + 3.5 * unit], fill="#ffffff")
        labels.append((cx, cy - radius - 24 * unit if facing == "south" else cy + radius + 2 * unit, name))
    for cx, top, name in labels:  # names go on last, over heads and walls
        _label(draw, cx, top, name, round(19 * unit), back)
    return image


def see_item(seed: int, folder: Path) -> dict:
    """Which of three listed things can one person see? At least one is hidden by a wall."""
    rng = random.Random(f"see-{seed}")
    while True:
        walls = _walls(rng, rng.randint(2, 3))
        spots = rng.sample(_floor(walls), 6)
        people = {name: (spots[i], rng.choice(list(DIRECTIONS))) for i, name in enumerate(rng.sample(list(PEOPLE), 2))}
        things = {name: spots[2 + i] for i, name in enumerate(rng.sample(list(THINGS), 4))}
        asked = rng.choice(list(people))
        place, facing = people[asked]
        plain = {name: sees(place, facing, spot, walls) for name, spot in things.items()}
        fx, fy = DIRECTIONS[facing]
        walled = [n for n, seen in plain.items() if seen is False and (things[n][0] - place[0]) * fx + (things[n][1] - place[1]) * fy >= 1]
        seen = [n for n, visible in plain.items() if visible]
        rest = [n for n, visible in plain.items() if visible is not None and n not in (walled[:1] + seen[:1])]
        if walled and seen and rest:
            break
    listed = sorted([walled[0], seen[0], rest[0]])
    file = folder / f"see-{seed:03d}.png"
    _room(walls, {name: (spot, THINGS[name]) for name, spot in things.items()}, people, 72).save(file)
    return {
        "kind": "see",
        "picture": str(file),
        "question": f"The picture shows a room from above. {LEGEND}\n\nWhich of these can {asked} see: the {', the '.join(listed)}?",
        "answer_form": "the names of the things, separated by commas, or NOTHING",
        "choices": listed,
        "gold": ", ".join(name for name in listed if plain[name]) or "NOTHING",
        "contested": any(plain[name] and _diagonal(place, facing, things[name]) for name in listed),
    }


def story_item(seed: int, folder: Path, watcher_sees_last: bool, reason: str) -> dict:
    """A ball moves between closed boxes over two or three panels. Where will the watcher look?

    `reason` says why the watcher misses the last move when `watcher_sees_last` is False:
    "away" (faces the other way), "wall" (a wall is in between) or "out" (not in the room).
    """
    rng = random.Random(f"story-{seed}")
    mover, watcher = rng.sample(list(PEOPLE), 2)
    n_moves = rng.choice([1, 2])
    while True:
        walls = _walls(rng, 2)
        floor = _floor(walls)
        boxes = dict(zip(rng.sample(list(BOXES), 3), rng.sample(floor, 3)))
        order = rng.sample(list(boxes), 1 + n_moves)  # where the ball is put, then each move
        panels, ok, doubt = [], True, False
        for step in range(1 + n_moves):
            last, first = step == n_moves, step == 0
            watching = True if first or not last else watcher_sees_last
            if not first and not last:
                watching = rng.random() < 0.5
            here = [boxes[order[step]]] + ([boxes[order[step - 1]]] if step else [])
            free = [c for c in floor if c not in boxes.values()]
            mover_spot = rng.choice([c for c in free if abs(c[0] - here[0][0]) + abs(c[1] - here[0][1]) == 1] or [None])
            if mover_spot is None:
                ok = False
                break
            mover_face = next(d for d, (fx, fy) in DIRECTIONS.items() if (mover_spot[0] + fx, mover_spot[1] + fy) == here[0])
            people = {mover: (mover_spot, mover_face)}
            if watching or reason != "out":
                wanted = True if watching else False
                found = [
                    (c, d) for c in free if c != mover_spot for d in DIRECTIONS
                    if all(sees(c, d, box, walls) is wanted for box in here)
                    and (watching or reason != "wall" or all((b[0] - c[0]) * DIRECTIONS[d][0] + (b[1] - c[1]) * DIRECTIONS[d][1] >= 1 for b in here))
                    and (watching or reason != "away" or all((b[0] - c[0]) * DIRECTIONS[d][0] + (b[1] - c[1]) * DIRECTIONS[d][1] <= -1 for b in here))
                ]
                if not found:
                    ok = False
                    break
                people[watcher] = rng.choice(found)
            if watching:  # the watcher must see where the ball goes: that box must be plainly in view
                doubt = doubt or _diagonal(*people[watcher], here[0])
            panels.append((people, watching))
        if ok:
            break
    seen = [order[step] for step, (_, watching) in enumerate(panels) if watching]
    cell, gap = 48, 24
    sheet = Image.new("RGB", (len(panels) * SIZE * cell + (len(panels) - 1) * gap, SIZE * cell + 40), SURFACE)
    draw = ImageDraw.Draw(sheet)
    for index, (people, _) in enumerate(panels):
        left = index * (SIZE * cell + gap)
        _label(draw, left + SIZE * cell / 2, 6, f"Picture {index + 1}", 22)
        sheet.paste(_room(walls, {name: (spot, BOXES[name]) for name, spot in boxes.items()}, people, cell), (left, 40))
    file = folder / f"story-{seed:03d}.png"
    sheet.save(file)
    lines = [f"Picture 1: {mover} puts a ball in the {order[0]}."]
    lines += [f"Picture {step + 1}: {mover} moves the ball to the {order[step]}." for step in range(1, 1 + n_moves)]
    return {
        "kind": "story",
        "picture": str(file),
        "question": (
            f"The pictures show one room from above at {len(panels)} moments, in order. {LEGEND} The boxes are closed, "
            "so nobody can see what is inside a box. A person who is not in a picture is out of the room at that "
            "moment and sees nothing.\n\n" + "\n".join(lines)
            + f"\n\nAfter the last picture, {watcher} wants the ball. Which box does {watcher} open first?"
        ),
        "answer_form": "the name of one box",
        "choices": sorted(boxes),
        "gold": seen[-1],
        "note": f"{'sees' if watcher_sees_last else 'misses'} the last move" + ("" if watcher_sees_last else f" ({reason})"),
        "contested": doubt,  # a sight line that the answer needs is not plain
    }


def table_item(seed: int, folder: Path) -> dict:
    """From one seat at a table, which of two blocks is on the left?"""
    rng = random.Random(f"table-{seed}")
    size, margin = 560, 150
    sides = rng.sample(list(DIRECTIONS), rng.choice([2, 3]))  # the side of the table each person sits on
    seats = dict(zip(rng.sample(list(PEOPLE), len(sides)), sides))
    asked = rng.choice(list(seats))
    side = seats[asked]
    first, second = rng.sample(list(BLOCKS), 2)
    centre = size / 2
    spread, depth = rng.choice([-1, 1]) * rng.uniform(70, 100), rng.uniform(-25, 25)
    # the two blocks sit apart along the line that runs across the asked person's view
    if side in ("north", "south"):
        spots = {first: (centre - spread, centre + depth), second: (centre + spread, centre - depth)}
    else:
        spots = {first: (centre + depth, centre - spread), second: (centre - depth, centre + spread)}
    # for a person who looks at the table: which map direction is on the left hand
    left_is = {"south": lambda p: -p[0], "north": lambda p: p[0], "west": lambda p: -p[1], "east": lambda p: p[1]}[side]
    gold = max(spots, key=lambda name: left_is(spots[name]))
    image = Image.new("RGB", (size, size), SURFACE)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle([margin, margin, size - margin, size - margin], radius=18, fill="#e9dcc3", outline=INK, width=2)
    for name, (x, y) in spots.items():
        draw.rounded_rectangle([x - 20, y - 20, x + 20, y + 20], radius=5, fill=BLOCKS[name], outline=INK, width=2)
    for name, seat in seats.items():
        fx, fy = DIRECTIONS[seat]
        cx, cy = centre + fx * (centre - 70), centre + fy * (centre - 70)
        nx, ny = -fx, -fy  # the person faces the table
        draw.polygon([(cx + nx * 38, cy + ny * 38), (cx + nx * 16 - ny * 11, cy + ny * 16 + nx * 11), (cx + nx * 16 + ny * 11, cy + ny * 16 - nx * 11)], fill=PEOPLE[name])
        draw.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=PEOPLE[name], outline=INK, width=2)
        for hand in (-1, 1):
            ex, ey = cx + nx * 10 - ny * 9 * hand, cy + ny * 10 + nx * 9 * hand
            draw.ellipse([ex - 4, ey - 4, ex + 4, ey + 4], fill="#ffffff")
        _label(draw, cx - fy * 0, cy + (26 if seat != "south" else -50), name, 20)
    file = folder / f"table-{seed:03d}.png"
    image.save(file)
    return {
        "kind": "table",
        "picture": str(file),
        "question": (
            "The picture shows a table from above, with people who sit round it. Each person is a round head seen from "
            "above, with a pointed nose and two eyes on the side that the person faces. Everybody faces the table. "
            f"Two coloured blocks are on the table: a {first} and a {second}.\n\n"
            f"From where {asked} sits, which block is on the left?"
        ),
        "answer_form": "the name of one block",
        "choices": sorted([first, second]),
        "gold": gold,
    }
