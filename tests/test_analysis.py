import pytest

np = pytest.importorskip("numpy")  # the analysis needs the "paper" dependency group
pytest.importorskip("scipy")

from betrayal import analysis  # noqa: E402


def test_the_counter_offer_is_the_figure_nearest_to_the_other_sides_offer():
    assert analysis.counter("bike", "I can't do £300, but I'd take £330.") == 330
    assert analysis.counter("bike", "I'm asking £450, but I could do £380 if you collect tonight.") == 380
    assert analysis.counter("job", "I can't accept £40,000. I was hoping for £50,000.") == 50000
    assert analysis.counter("rent", "We can't agree to £1,450. A £200 jump from £1,250 is too much; could we say £1,300?") == 1300
    assert analysis.counter("software", "£32,500 is too much against our current £24,000. Could you do £26k?") == 26000
    assert analysis.counter("bike", "Thanks, but that is too low for me.") is None


def test_a_total_is_not_taken_for_a_rate():
    assert analysis.counter("freelance", "I can offer £360 a day, which comes to £4,320 for the 12 days.") == 360


def test_the_concession_runs_from_the_opening_figure_to_the_limit():
    assert analysis.concession("bike", 450) == 0
    assert analysis.concession("bike", 330) == 1
    assert analysis.concession("rent", 1400) == 1
    assert analysis.concession("car", 6000) > 1  # past the limit
    assert analysis.concession("supplier", 2.40) is None  # the notes give no opening figure


def test_the_exact_interval_holds_the_observed_share():
    low, high = analysis.clopper_pearson(1, 360)
    assert low < 1 / 360 < high < 0.02
    assert analysis.clopper_pearson(0, 144)[0] == 0


def test_the_rasch_fit_orders_models_by_how_often_they_are_right():
    model = np.repeat(np.arange(3), 4)
    item = np.tile(np.arange(4), 3)
    hits = np.array([9, 8, 6, 3, 7, 5, 3, 1, 4, 2, 1, 0], dtype=float)
    ability, difficulty, _ = analysis.rasch(model, item, hits, np.full(12, 10.0), 3, 4)
    assert ability[0] > ability[1] > ability[2]
    assert difficulty[0] < difficulty[1] < difficulty[2] < difficulty[3]
