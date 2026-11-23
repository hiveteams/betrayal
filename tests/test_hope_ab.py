import re

from betrayal import briefs, hope_ab, ladder


def test_every_case_has_unique_swap_preserving_limit_and_defects():
    assert set(hope_ab.SWAPS) == set(briefs.CASES)
    for case, facts in briefs.CASES.items():
        base = facts["notes"]
        flipped = hope_ab.flipped_notes(case)
        assert flipped != base
        assert re.search(facts["limit"][0], flipped), f"{case}: limit figure missing after flip"
        if "defect" in facts:
            assert briefs.named_defect(case, flipped), f"{case}: defect missing after flip"
        prompt = hope_ab.flipped_prompt(case)
        assert ladder.LOW[case][1] in prompt
        assert briefs.LEAD in prompt
