"""Inverse-task tests: the step language, the replay checks, and the simulation grader."""

import json

import pytest

from betrayal.build import build_inverse
from betrayal.engine import Event
from betrayal.inverse import ScriptError, all_steps, grade_script, parse_script, replay, to_event, to_step

F = frozenset
CAST = ["Amara", "Bruno", "Chidi", "Dalia"]
VALUES = ["red box", "blue drawer", "wicker basket", "green cupboard"]
OPENING = Event("set", 0, 0, F({0, 1, 2, 3}), actor=0)


def test_script_is_read_from_the_last_marker():
    assert parse_script('thinking [1]\nSCRIPT: [{"step": "check"}]') == [{"step": "check"}]
    assert parse_script('SCRIPT: [1]\nfixed:\nSCRIPT:\n```json\n[{"step": "say"}]\n```') == [{"step": "say"}]
    assert parse_script("no marker [1, 2]") is None
    assert parse_script("SCRIPT: not json") is None
    assert parse_script('SCRIPT: {"step": "check"}') is None


def test_steps_round_trip_through_the_step_language():
    for event in all_steps(4, 4):
        again = to_event(to_step(event, CAST, VALUES), CAST, VALUES)
        expected = event if event.kind != "see" else again  # a check carries no value of its own
        assert again == expected and again.overt == event.overt and again.covert == event.covert


@pytest.mark.parametrize(
    "step",
    [
        {"step": "dance", "who": "Amara", "present": ["Amara"]},
        {"step": "change", "who": "Amara", "value": "red box", "present": ["Bruno"]},
        {"step": "change", "who": "Zed", "value": "red box", "present": ["Zed"]},
        {"step": "change", "who": "Amara", "value": "shoe", "present": ["Amara"]},
        {"step": "check", "who": "Amara", "present": ["Amara", "Bruno"], "missed_by": ["Amara"]},
        {"step": "check", "who": "Amara", "present": ["Amara", "Bruno"], "secret_witnesses": ["Bruno"]},
        {"step": "say", "who": "Amara", "value": "red box", "present": ["Amara"]},
        {"step": "message", "from": "Amara", "to": "Amara", "value": "red box"},
        {"step": "message", "from": "Amara", "to": "Bruno", "value": "red box", "secret_readers": ["Bruno"]},
        "move the marble",
    ],
)
def test_malformed_steps_are_rejected(step):
    with pytest.raises(ScriptError):
        to_event(step, CAST, VALUES)


def test_labels_are_matched_loosely():
    event = to_event({"step": "change", "who": "amara", "value": "The Blue Drawer", "present": ["Amara"]}, CAST, VALUES)
    assert (event.actor, event.value) == (0, 1)


def test_replay_settles_written_steps_and_checks_given_ones():
    lie = Event("tell", 0, 2, F({0, 1}), actor=0, channel="private")
    table = replay(4, [OPENING, lie], F({1}), 2)
    assert table.get((0,), 0) == 0 and table.get((1,), 0) == 2  # written: taken as a lie, the speaker keeps the truth
    with pytest.raises(ScriptError):
        replay(4, [OPENING, lie], F(), 2)  # given as sincere, but the speaker believes something else
    with pytest.raises(ScriptError):
        replay(4, [OPENING, Event("set", 0, 0, F({0}), actor=0)], F({1}), 2)  # a move to the same place
    with pytest.raises(ScriptError):
        replay(4, [OPENING, Event("see", 0, 3, F({0}), actor=0)], F(), 2)  # a given check that shows a false value
    assert replay(4, [OPENING, Event("see", 0, 3, F({0}), actor=0)], F({1}), 2).get((0,), 0) == 0


def test_grader_accepts_any_script_that_works_and_only_those():
    items, _ = build_inverse("plan", 2, 9)
    items += build_inverse("explain", 2, 9)[0]
    for item in items:
        assert grade_script(item, f"SCRIPT: {item['gold']}")[1], item["id"]
        assert not grade_script(item, "SCRIPT: []")[1]
        assert grade_script(item, "I give up")[0] is None
        too_long = json.dumps(json.loads(item["gold"]) * 9)
        assert not grade_script(item, f"SCRIPT: {too_long}")[1]
    plan = next(item for item in items if item["kind"] == "plan")
    wrong = json.loads(plan["gold"])[:-1]  # the reference without its last step misses a target
    answer, works, note = grade_script(plan, f"SCRIPT: {json.dumps(wrong)}")
    assert answer is not None and not works and note.endswith("targets")
