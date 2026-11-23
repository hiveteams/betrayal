"""Dataset tests: the grader, the generator's contract with the skins, and the built items."""

import random

from betrayal.build import build
from betrayal.engine import beliefs
from betrayal.generate import GenConfig, generate
from betrayal.grade import parse
from betrayal.questions import LETTERS, pick

MCQ = {"kind": "belief", "options": ["the red box", "the blue drawer", "the wicker basket", "the green cupboard"]}
INFORM = {"kind": "inform", "options": [], "names": ["Amara", "Bruno", "Chidi", "Dalia"], "path": ["Amara"]}


def test_grader_reads_letters_in_common_shapes():
    for reply in ("ANSWER: C", "thinking...\n**ANSWER: C**", "ANSWER: (C)", "answer: C. the wicker basket", "ANSWER: A\nANSWER: C"):
        assert parse(MCQ, reply) == "C", reply
    assert parse(MCQ, "ANSWER: the wicker basket") == "C"


def test_grader_rejects_unreadable_replies():
    for reply in ("I think it is the basket.", "ANSWER: E", "ANSWER: either box or drawer", "ANSWER:", ""):
        assert parse(MCQ, reply) is None, reply


def test_grader_reads_name_sets():
    assert parse(INFORM, "ANSWER: Chidi, Bruno") == "Bruno, Chidi"
    assert parse(INFORM, "ANSWER: Bruno and Chidi.") == "Bruno, Chidi"
    assert parse(INFORM, "ANSWER: Amara sends notes to Dalia") == "Dalia"  # the sender's own name is not an answer
    assert parse(INFORM, "ANSWER: NOBODY") == "NOBODY"
    assert parse(INFORM, "ANSWER: nobody.") == "NOBODY"
    assert parse(INFORM, "ANSWER: everyone") is None


def test_generator_keeps_its_contract_with_the_skins():
    for seed in range(300):
        cfg = GenConfig(n_vars=1 + seed % 2, n_events=(8, 11, 14)[seed % 3])
        scenario = generate(seed, cfg)
        table = beliefs(cfg.n_agents, cfg.n_vars, [], cfg.max_order)
        told = set()
        assert len(scenario.steps) == cfg.n_events + 1
        for step in scenario.steps:
            event = step.event
            truth = table.reality(event.var)
            if event.channel == "room":
                assert event.overt | event.presumed == step.occupancy
                assert not event.covert & step.occupancy
            else:
                assert event.kind == "tell" and len(event.overt) == 2 and not event.presumed
                key = (event.actor, *(event.overt - {event.actor}), event.var)
                assert key not in told
                told.add(key)
            if event.kind == "see":
                assert event.value == truth
            if event.kind == "set":
                assert event.value != truth
                assert step.first == (truth is None)
            if event.kind == "tell":
                own = table.get((event.actor,), event.var)
                assert own is not None and (event.value == own) == event.sincere
                for hearer in (event.overt | event.covert) - {event.actor}:
                    # nobody who holds the true value is ever told a false one
                    assert event.value == truth or table.get((hearer,), event.var) != truth
            table.apply(event)


def test_built_items_are_well_formed_and_reproducible():
    items, _ = build(12, 3, {})
    again, _ = build(12, 3, {})
    assert items == again
    assert len({item["id"] for item in items}) == len(items)
    for item in items:
        assert item["prompt"].count("ANSWER:") == 1
        if item["kind"] == "inform":
            assert item["gold"] == "NOBODY" or set(item["gold"].split(", ")) <= set(item["names"]) - {item["path"][0]}
            assert item["gold"] != item["shortcuts"]["omniscient"]
        else:
            assert item["gold"] in LETTERS[: len(item["options"])]
            for index, option in enumerate(item["options"]):
                assert f"{LETTERS[index]}. {option}" in item["prompt"]
        if item["slot"].endswith("hard"):
            assert item["gold"] != item["shortcuts"]["reality"]
            if item["order"] > 1:
                assert item["gold"] != item["shortcuts"]["inner"]
        if item["slot"] == "know":
            assert item["options"][-1].endswith(("is", "in", "for", "supplier", "quote", "account")) and item["gold"] == LETTERS[len(item["options"]) - 1]
    for name in ("classic", "workplace"):
        assert sum(item["skin"] == name for item in items) > 60


def test_every_slot_is_filled_or_the_scenario_is_dropped():
    for seed in range(100):
        cfg = GenConfig(n_vars=1 + seed % 2)
        asks = pick(generate(seed, cfg), random.Random(seed))
        if asks is not None:
            slots = [ask.slot for ask in asks]
            assert len(slots) == len(set(slots)) == 12 + (cfg.n_vars == 2)
