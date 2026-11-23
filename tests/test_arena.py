"""Arena tests: reading moves, and scoring against a known pool."""

from betrayal import arena
from betrayal.arena import GAMES, read, score


def item(key: str) -> dict:
    return next(i for i in arena.items(1) if i["game"] == key)


def play(move, forecast=None, n=5):
    return [{"move": move, "forecast": forecast}] * n


def test_every_game_has_a_prompt_and_two_answer_lines():
    listed = arena.items(2)
    assert len(listed) == 2 * len(GAMES)
    for entry in listed:
        assert "CHOICE:" in entry["prompt"] and "FORECAST:" in entry["prompt"] and "{" not in entry["prompt"]
    shuffled = [e["options"] for e in listed if e["game"] == "coordinate/words"]
    assert shuffled[0] != shuffled[1] and sorted(shuffled[0]) == sorted(shuffled[1])


def test_moves_are_read_and_illegal_ones_are_dropped():
    assert read(item("beauty/two-thirds"), "CHOICE: 22\nFORECAST: 33.5") == {"move": 22, "forecast": 33.5}
    assert read(item("beauty/two-thirds"), "CHOICE: 101\nFORECAST: 3") is None
    assert read(item("beauty/two-thirds"), "FORECAST: 3") is None
    assert read(item("coordinate/numbers"), "**CHOICE: 42**\nFORECAST: 7") == {"move": "42", "forecast": "7"}
    assert read(item("coordinate/times"), "CHOICE: 12:00\nFORECAST: 12:00")["move"] == "12:00"
    assert read(item("coordinate/numbers"), "CHOICE: 5\nFORECAST: 7") is None
    assert read(item("blotto/5-fields"), "CHOICE: 30, 30, 30, 10, 0\nFORECAST: 20") == {"move": [30, 30, 30, 10, 0], "forecast": 20.0}
    assert read(item("blotto/5-fields"), "CHOICE: 30, 30, 30, 10, 5\nFORECAST: 20") is None
    assert read(item("stag/all-six"), "CHOICE: hunt\nFORECAST: 6") == {"move": "HUNT", "forecast": 6.0}
    assert read(item("hide/abaa-hider"), "CHOICE: 3\nFORECAST: 2") == {"move": 3, "forecast": 2}


def test_scores_reward_the_best_reply_to_the_pool():
    pool = {f"m{i}": {
        "beauty/two-thirds": play(30), "coordinate/numbers": play("42"), "avoid/numbers": play("42"),
        "requests/11-20": play(20), "hide/abaa-seeker": play(2), "hide/abaa-hider": play(3),
        "blotto/3-fields": play([20, 20, 20]), "stag/all-six": play("HUNT"), "mirror/words": play("river"),
    } for i in range(7)}
    sharp = {
        "beauty/two-thirds": play(20, 30.0), "coordinate/numbers": play("42", "42"), "avoid/numbers": play("7", "42"),
        "requests/11-20": play(19, 20.0), "hide/abaa-hider": play(1, 2), "hide/abaa-seeker": play(3, 3),
        "blotto/3-fields": play([21, 21, 18], 20.0), "stag/all-six": play("HUNT", 6.0), "mirror/words": play("anchor"),
    }
    dull = {
        "beauty/two-thirds": play(90, 90.0), "coordinate/numbers": play("8", "8"), "avoid/numbers": play("42", "8"),
        "requests/11-20": play(11, 11.0), "hide/abaa-hider": play(2, 1), "hide/abaa-seeker": play(1, 1),
        "blotto/3-fields": play([60, 0, 0], 60.0), "stag/all-six": play("SAFE", 0.0),
        "mirror/words": [{"move": w, "forecast": None} for w in ("river", "anchor", "velvet", "thunder", "pencil")],
    }
    result = score({**pool, "sharp": sharp, "dull": dull}, players=list(pool))
    for key in sharp:
        if key.startswith("mirror"):
            assert result["sharp"][key]["score"] == 1 and result["dull"][key]["score"] == 0
            continue
        assert result["sharp"][key]["score"] > 0.95, (key, result["sharp"][key])
        assert result["dull"][key]["score"] < 0.2, (key, result["dull"][key])
        assert result["sharp"][key]["forecast"] > 0.99, (key, result["sharp"][key])
        assert result["dull"][key]["forecast"] < 0.5, (key, result["dull"][key])
    assert result["m0"]["coordinate/numbers"]["score"] == 1  # pool members are scored against the other members
