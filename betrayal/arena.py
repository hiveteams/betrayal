"""Arena: one-shot strategy games where the best move depends on what the other models do.

There is no answer key. Every model plays every game several times. A model's payoff is worked
out against the moves that the *other* models made, so a high score needs a correct picture of
how those minds choose. Each reply also carries a forecast of the other players' moves, which is
scored on its own: that separates knowing what others will do from acting well on it.

Scores depend on the pool of players. The raw moves are stored, so a later model can be scored
against the same pool.
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass, field
from statistics import mean
from typing import Callable, Optional

INTRO = (
    "You are a player in a one-shot game. The other players are other AI language models: current leading models "
    "from several AI labs. {who} gets this same message, chooses alone, and cannot talk to the others. "
    "Play to get the highest payoff for yourself."
)
MIRROR_INTRO = (
    "You are a player in a one-shot game. The other players are copies of you: the same AI model as you. "
    "Every player gets this same message, chooses alone, and cannot talk to the others. "
    "Play to get the highest payoff for yourself."
)
OUTRO = "Think it through, then finish with exactly these two lines:\nCHOICE: {choice}\nFORECAST: {forecast}"
GROUP = "You are put in a group with six other players, drawn at random."
PAIR = "You are paired with one other player, drawn at random."
CHOICE = re.compile(r"CHOICE\s*:\s*(.*)", re.IGNORECASE)
FORECAST = re.compile(r"FORECAST\s*:\s*(.*)", re.IGNORECASE)
NUMBER = re.compile(r"-?\d+(?:\.\d+)?")

LISTS = {
    "numbers": ["17", "3", "42", "7", "100", "64", "23", "8"],
    "words": ["river", "anchor", "velvet", "thunder", "pencil", "orchid", "lantern", "gravel"],
    "cities": ["Lima", "Oslo", "Cairo", "Perth", "Hanoi", "Quito", "Tunis", "Dhaka"],
    "times": ["03:17", "12:00", "08:45", "17:30", "23:59", "06:00"],
    "colours": ["teal", "crimson", "amber", "slate", "ivory", "olive", "coral", "indigo"],
    "pairs": ["QZ", "MM", "AB", "XK", "LO", "TT"],
}


@dataclass(frozen=True)
class Game:
    key: str  # family and variant, e.g. "beauty/two-thirds"
    rules: str
    choice: str  # how to write the CHOICE line
    forecast: str  # what the FORECAST line means
    actions: Optional[list]  # every legal move, or None when there are too many to list
    payoff: Callable[[object, list], float]  # (my move, the other players' moves) -> points
    group: int = 1  # how many other players one round has
    versus: Optional[str] = None  # the game whose players are the opponents, for games with two roles
    numeric_forecast: Optional[Callable[[list], float]] = None  # truth for a number forecast, from one group
    span: float = 1.0  # scale for the error of a number forecast
    shuffle: bool = False  # show the options in a new random order to each player
    parts: Optional[tuple[int, int]] = None  # blotto only: (soldiers, battlefields)
    weights: tuple[float, ...] = field(default=())

    @property
    def family(self) -> str:
        return self.key.split("/")[0]


def _numbers(lo: int, hi: int) -> list[int]:
    return list(range(lo, hi + 1))


def beauty(name: str, lo: int, hi: int, factor: float, factor_text: str, plus: int = 0) -> Game:
    extra = f", plus {plus}" if plus else ""
    return Game(
        f"beauty/{name}",
        f"Each player picks a whole number from {lo} to {hi}. {GROUP} Your payoff is 100 minus the distance between "
        f"your number and the target. The target is {factor_text} the average of the six other players' numbers{extra}.",
        f"<a whole number from {lo} to {hi}>",
        "<the average number that you expect the other players to pick>",
        _numbers(lo, hi),
        lambda mine, others: 100 - abs(mine - (factor * mean(others) + plus)),
        group=6, numeric_forecast=mean, span=hi - lo,
    )


def requests(name: str, lo: int, hi: int, gap: int, bonus: int) -> Game:
    return Game(
        f"requests/{name}",
        f"Each player asks for a whole number of points from {lo} to {hi}. You get the points that you ask for. {PAIR} "
        f"If you asked for exactly {gap} less than that player, you also get {bonus} bonus points.",
        f"<a whole number from {lo} to {hi}>",
        "<the average number that you expect the other players to ask for>",
        _numbers(lo, hi),
        lambda mine, others: mine + (bonus if mine == others[0] - gap else 0),
        numeric_forecast=mean, span=hi - lo,
    )


def traveler(name: str, lo: int, hi: int, swing: int) -> Game:
    def payoff(mine: int, others: list) -> float:
        other = others[0]
        return min(mine, other) + (swing if mine < other else -swing if mine > other else 0)

    return Game(
        f"traveler/{name}",
        f"Each player claims a whole number from {lo} to {hi}. {PAIR} Both of you are paid the lower of the two "
        f"claims. If the claims differ, the player with the lower claim also gets {swing} extra, and the player "
        f"with the higher claim loses {swing}.",
        f"<a whole number from {lo} to {hi}>",
        "<the average number that you expect the other players to claim>",
        _numbers(lo, hi), payoff, numeric_forecast=mean, span=hi - lo,
    )


def pick_same(name: str, options: list[str], same: bool, mirror: bool = False) -> Game:
    goal = "the same item as you" if same else "a different item from you"
    family = ("mirror" if mirror else "coordinate") if same else "avoid"
    return Game(
        f"{family}/{name}",
        "Each player picks one item from this list: {options}. Each player sees the list in a different random "
        f"order. {GROUP} Your payoff is 100 times the share of those six players who pick {goal}.",
        "<one item from the list>",
        "<the item that you expect the most other players to pick>",
        options,
        lambda mine, others: 100 * mean((other == mine) == same for other in others),
        group=6, shuffle=True,
    )


def blotto(name: str, soldiers: int, fields: int, weighted: bool) -> Game:
    weights = tuple(float(k) for k in range(1, fields + 1)) if weighted else (1.0,) * fields
    worth = (
        f"Battlefield k is worth k points, so the battlefields are worth 1 to {fields} points. Your payoff is the "
        "total worth of the battlefields that you win."
        if weighted else "Your payoff is the number of battlefields that you win."
    )

    def payoff(mine: tuple, others: list) -> float:
        return sum(w * (1.0 if a > b else 0.5 if a == b else 0.0) for w, a, b in zip(weights, mine, others[0]))

    return Game(
        f"blotto/{name}",
        f"Each player places {soldiers} soldiers on {fields} battlefields, numbered 1 to {fields}. Each battlefield "
        f"gets a whole number of soldiers, zero or more, and all {soldiers} soldiers must be placed. {PAIR} On each "
        "battlefield, the player with more soldiers there wins it. If both have the same number there, each gets "
        f"half of it. {worth}",
        f"<{fields} whole numbers separated by commas, for battlefields 1 to {fields}>",
        "<the number of soldiers that you expect the other players to put on battlefield 1, on average>",
        None, payoff, numeric_forecast=lambda others: others[0][0], span=soldiers,
        parts=(soldiers, fields), weights=weights,
    )


def ultimatum(pie: int) -> list[Game]:
    deal = (
        f"The proposer has {pie} points to split and offers the responder a whole number of points from 0 to {pie}. "
        "Before seeing the offer, the responder writes down the smallest offer that the responder will accept. "
        "If the offer is at least that number, the responder gets the offer and the proposer keeps the rest. "
        "If the offer is lower, both get nothing."
    )
    return [
        Game(
            f"ultimatum/offer-{pie}",
            f"You are a proposer. You are paired with one responder, drawn at random from the other players. {deal}",
            f"<your offer, a whole number from 0 to {pie}>",
            "<the average smallest offer that you expect the responders to accept>",
            _numbers(0, pie), lambda mine, others: pie - mine if mine >= others[0] else 0,
            versus=f"ultimatum/accept-{pie}", numeric_forecast=mean, span=pie,
        ),
        Game(
            f"ultimatum/accept-{pie}",
            f"You are a responder. You are paired with one proposer, drawn at random from the other players. {deal}",
            f"<the smallest offer that you will accept, a whole number from 0 to {pie}>",
            "<the average offer that you expect the proposers to make>",
            _numbers(0, pie), lambda mine, others: others[0] if others[0] >= mine else 0,
            versus=f"ultimatum/offer-{pie}", numeric_forecast=mean, span=pie,
        ),
    ]


def hide_and_seek(name: str, labels: list[str]) -> list[Game]:
    row = f"There are four boxes in a row. From left to right they are labelled {', '.join(labels)}."
    return [
        Game(
            f"hide/{name}-hider",
            f"{row} You are a hider. You are paired with one seeker, drawn at random from the other players. You put "
            "a prize in one box. The seeker, who does not see your move, opens one box. Your payoff is 100 if the "
            "seeker opens a box without the prize, and 0 if the seeker finds the prize.",
            "<the position of your box, a number from 1 to 4 counted from the left>",
            "<the position that you expect the most seekers to open>",
            _numbers(1, 4), lambda mine, others: 100.0 * (mine != others[0]), versus=f"hide/{name}-seeker",
        ),
        Game(
            f"hide/{name}-seeker",
            f"{row} You are a seeker. You are paired with one hider, drawn at random from the other players. The "
            "hider puts a prize in one box. You do not see that move, and you open one box. Your payoff is 100 if "
            "you find the prize, and 0 if you open a box without it.",
            "<the position of the box that you open, a number from 1 to 4 counted from the left>",
            "<the position that you expect the most hiders to use>",
            _numbers(1, 4), lambda mine, others: 100.0 * (mine == others[0]), versus=f"hide/{name}-hider",
        ),
    ]


def pennies(name: str, first: str, second: str) -> list[Game]:
    deal = (
        f"Each of the two secretly picks {first} or {second}. If both pick the same word, the matcher gets 100 "
        "points and the avoider gets 0. If they pick different words, the avoider gets 100 points and the "
        "matcher gets 0."
    )
    return [
        Game(
            f"pennies/{name}-matcher",
            f"You are a matcher. You are paired with one avoider, drawn at random from the other players. {deal}",
            f"<{first} or {second}>", "<the word that you expect the most avoiders to pick>",
            [first, second], lambda mine, others: 100.0 * (mine == others[0]), versus=f"pennies/{name}-avoider",
        ),
        Game(
            f"pennies/{name}-avoider",
            f"You are an avoider. You are paired with one matcher, drawn at random from the other players. {deal}",
            f"<{first} or {second}>", "<the word that you expect the most matchers to pick>",
            [first, second], lambda mine, others: 100.0 * (mine != others[0]), versus=f"pennies/{name}-matcher",
        ),
    ]


def stag(name: str, safe: int, need: int) -> Game:
    return Game(
        f"stag/{name}",
        f"Each player chooses HUNT or SAFE. {GROUP} SAFE pays {safe} points whatever the others do. HUNT pays 100 "
        f"points if at least {need} of the six other players also choose HUNT, and 0 points if fewer do.",
        "<HUNT or SAFE>", "<how many of the six other players you expect to choose HUNT>",
        ["HUNT", "SAFE"],
        lambda mine, others: safe if mine == "SAFE" else 100.0 * (others.count("HUNT") >= need),
        group=6, numeric_forecast=lambda others: others.count("HUNT"), span=6,
    )


def entry(name: str, room: int) -> Game:
    return Game(
        f"entry/{name}",
        f"Each player chooses ENTER or STAY. {GROUP} STAY pays 50 points. ENTER pays 50 + 20 x ({room} - E) points, "
        "where E is the number of players in your group of seven who choose ENTER, yourself included.",
        "<ENTER or STAY>", "<how many of the six other players you expect to choose ENTER>",
        ["ENTER", "STAY"],
        lambda mine, others: 50.0 if mine == "STAY" else 50.0 + 20 * (room - 1 - others.count("ENTER")),
        group=6, numeric_forecast=lambda others: others.count("ENTER"), span=6,
    )


def lowest_unique(name: str, hi: int) -> Game:
    def payoff(mine: int, others: list) -> float:
        picks = [mine, *others]
        unique = [n for n in picks if picks.count(n) == 1]
        return 100.0 * (bool(unique) and min(unique) == mine)

    return Game(
        f"unique/{name}",
        f"Each player picks a whole number from 1 to {hi}. {GROUP} In your group of seven, the lowest number that "
        "exactly one player picked wins: that player gets 100 points and the others get 0. If no number is picked "
        "by exactly one player, nobody gets points.",
        f"<a whole number from 1 to {hi}>", "<the number that you expect the most other players to pick>",
        _numbers(1, hi), payoff, group=6,
    )


def auction() -> Game:
    def payoff(mine: int, others: list) -> float:
        top = max(others)
        if mine < top:
            return 0.0
        return (100 - mine) / (1 + others.count(mine)) if mine == top else 100.0 - mine

    return Game(
        "auction/first-price",
        f"Each player bids a whole number from 0 to 100 for a prize that is worth 100 points to every player. {GROUP} "
        "The highest bid in your group of seven wins the prize and pays that bid, so the winner's payoff is 100 "
        "minus the bid. Everyone else gets 0. If several players share the highest bid, one of them wins at random.",
        "<your bid, a whole number from 0 to 100>",
        "<the highest bid that you expect among the six other players>",
        _numbers(0, 100), payoff, group=6, numeric_forecast=max, span=100,
    )


GAMES: dict[str, Game] = {
    game.key: game
    for game in [
        beauty("two-thirds", 0, 100, 2 / 3, "two thirds of"),
        beauty("half", 0, 100, 1 / 2, "half of"),
        beauty("nine-tenths", 0, 100, 0.9, "nine tenths of"),
        beauty("half-plus-30", 0, 100, 1 / 2, "half of", plus=30),
        beauty("times-1.3", 0, 100, 1.3, "1.3 times"),
        requests("11-20", 11, 20, 1, 20),
        requests("11-20-big-bonus", 11, 20, 1, 40),
        requests("31-40-two-less", 31, 40, 2, 20),
        traveler("small-swing", 2, 100, 2),
        traveler("mid-swing", 2, 100, 20),
        traveler("high-range", 100, 200, 10),
        *[pick_same(name, options, same=True) for name, options in LISTS.items()],
        *[pick_same(name, LISTS[name], same=False) for name in ("numbers", "cities", "pairs")],
        *[pick_same(name, options, same=True, mirror=True) for name, options in LISTS.items()],
        blotto("5-fields", 100, 5, weighted=False),
        blotto("3-fields", 60, 3, weighted=False),
        blotto("4-weighted", 100, 4, weighted=True),
        *ultimatum(100),
        *hide_and_seek("abaa", ["A", "B", "A", "A"]),
        *hide_and_seek("numbers", ["1", "2", "3", "4"]),
        *pennies("coin", "HEADS", "TAILS"),
        *pennies("sides", "LEFT", "RIGHT"),
        stag("all-six", 40, 6),
        stag("four", 60, 4),
        stag("five-cheap", 30, 5),
        entry("room-2", 2),
        entry("room-4", 4),
        lowest_unique("1-10", 10),
        lowest_unique("1-5", 5),
        auction(),
    ]
}


def items(samples: int) -> list[dict]:
    """`samples` plays of every game. A play of a list game shows the list in its own seeded order."""
    out = []
    for game in GAMES.values():
        for sample in range(samples):
            rules = game.rules
            options = None
            if game.shuffle:
                options = list(game.actions)
                random.Random(f"{game.key}#{sample}").shuffle(options)
                rules = rules.format(options=", ".join(options))
            if game.family == "mirror":
                intro = MIRROR_INTRO
            else:
                intro = INTRO.format(who="Every player in your role" if game.versus else "Every player")
            prompt = f"{intro}\n\n{rules}\n\n" + OUTRO.format(choice=game.choice, forecast=game.forecast)
            out.append({
                "id": f"arena-{game.key}#{sample}", "scenario": f"arena-{game.key}", "part": "arena",
                "level": game.family, "skin": "arena", "kind": "arena", "slot": f"arena-{game.family}",
                "game": game.key, "sample": sample, "options": options, "prompt": prompt,
            })
    return out


def _last(pattern: re.Pattern, text: str) -> Optional[str]:
    found = pattern.findall(text)
    return found[-1].strip().strip("*_`<>").strip() if found else None


def _move(game: Game, raw: Optional[str]):
    """A legal move read from text, or None."""
    if raw is None:
        return None
    if game.parts:
        soldiers, fields = game.parts
        placed = tuple(int(n) for n in re.findall(r"\d+", raw))
        return placed if len(placed) == fields and sum(placed) == soldiers else None
    if isinstance(game.actions[0], int):
        found = NUMBER.search(raw)
        value = float(found.group()) if found else None
        return int(value) if value is not None and value in game.actions else None
    hits = [action for action in game.actions if re.search(rf"(?<![\w:]){re.escape(action)}(?![\w:])", raw, re.IGNORECASE)]
    return hits[0] if len(hits) == 1 else None


def read(item: dict, text: str) -> Optional[dict]:
    """The move and the forecast in a reply. None when there is no legal move."""
    game = GAMES[item["game"]]
    move = _move(game, _last(CHOICE, text))
    if move is None:
        return None
    raw = _last(FORECAST, text)
    if game.numeric_forecast:
        found = NUMBER.search(raw or "")
        forecast = float(found.group()) if found else None
    else:
        forecast = _move(game, raw)
    return {"move": list(move) if isinstance(move, tuple) else move, "forecast": forecast}


def _rounds(game: Game, pool: dict[str, list], rng: random.Random, count: int) -> list[tuple[list, float]]:
    """Opponent line-ups with weights. Every model in the pool counts the same, however many plays it has.

    A pair game uses every stored move once. A group game draws random groups of six.
    """
    if game.group == 1:
        return [([move], 1 / len(moves)) for moves in pool.values() for move in moves]
    names = list(pool)
    rounds = []
    for _ in range(count):
        seats = rng.sample(names, game.group) if len(names) >= game.group else rng.choices(names, k=game.group)
        rounds.append(([rng.choice(pool[name]) for name in seats], 1.0))
    return rounds


def _blotto_candidates(game: Game, pool: dict[str, list], rng: random.Random) -> tuple[list, list]:
    """(random placements, placements to try as a best reply)."""
    soldiers, fields = game.parts

    def placement() -> tuple:
        cuts = sorted(rng.randint(0, soldiers) for _ in range(fields - 1))
        return tuple(b - a for a, b in zip([0, *cuts], [*cuts, soldiers]))

    randoms = [placement() for _ in range(400)]
    return randoms, randoms + [move for moves in pool.values() for move in moves]


def _climb(game: Game, start: tuple, value: Callable[[tuple], float]) -> float:
    """Hill-climb a blotto placement by moving soldiers between two battlefields."""
    best, best_value = start, value(start)
    improved = True
    while improved:
        improved = False
        for give in range(len(best)):
            for take in range(len(best)):
                for size in (1, 3, 9):
                    if give == take or best[give] < size:
                        continue
                    trial = list(best)
                    trial[give] -= size
                    trial[take] += size
                    trial_value = value(tuple(trial))
                    if trial_value > best_value + 1e-9:
                        best, best_value, improved = tuple(trial), trial_value, True
    return best_value


def score(moves: dict[str, dict[str, list[dict]]], players: list[str], seed: int = 0) -> dict[str, dict[str, dict]]:
    """Per model and game: payoff, and the share of the best reply's gain over a random move that the model got.

    `moves[model][game]` holds the model's plays, each {"move", "forecast"}. `players` are the models that
    form the pool of opponents. A model never plays against its own moves, except in the mirror games.
    """
    results: dict[str, dict[str, dict]] = {name: {} for name in moves}
    for key, game in GAMES.items():
        facing = game.versus or key
        for name, plays_by_game in moves.items():
            plays = plays_by_game.get(key, [])
            if game.family == "mirror":
                same = [a["move"] == b["move"] for i, a in enumerate(plays) for b in plays[i + 1:]]
                if same:
                    results[name][key] = {"payoff": 100 * mean(same), "score": mean(same), "plays": len(plays)}
                continue
            pool = {
                other: [tuple(p["move"]) if game.parts else p["move"] for p in moves[other].get(facing, [])]
                for other in players if other != name
            }
            pool = {other: listed for other, listed in pool.items() if listed}
            if not plays or not pool:
                continue
            rng = random.Random(f"{seed}-{key}-{name}")
            rounds = _rounds(game, pool, rng, 600)
            total = sum(weight for _, weight in rounds)

            def value(move) -> float:
                return sum(weight * game.payoff(move, others) for others, weight in rounds) / total

            mine = [tuple(p["move"]) if game.parts else p["move"] for p in plays]
            earned = mean(value(move) for move in mine)
            if game.parts:
                randoms, candidates = _blotto_candidates(game, pool, rng)
                at_random = mean(value(move) for move in randoms)
                starts = sorted(candidates + mine, key=value, reverse=True)[:3]
                best = max(_climb(game, start, value) for start in starts)
            else:
                values = [value(action) for action in game.actions]
                at_random, best = mean(values), max(values)
            row = {"payoff": earned, "best": best, "random": at_random, "plays": len(plays)}
            if best - at_random > 1e-9:  # 1 = as good as the best reply, 0 = no better than a random move
                row["score"] = max(-1.0, (earned - at_random) / (best - at_random))
            forecasts = [p["forecast"] for p in plays if p["forecast"] is not None]
            if forecasts and game.numeric_forecast:
                truth = sum(weight * game.numeric_forecast(others) for others, weight in rounds) / total
                row["forecast"] = mean(max(0.0, 1 - abs(f - truth) / game.span) for f in forecasts)
            elif forecasts:
                shares = {action: 0.0 for action in game.actions}
                for others, weight in rounds:
                    for move in others:
                        shares[move] += weight
                row["forecast"] = mean(shares[f] for f in forecasts) / max(shares.values())
            results[name][key] = row
    return results
