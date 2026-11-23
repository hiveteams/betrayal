"""Engine tests: hand-worked classics, then the two implementations against each other."""

import random

from betrayal.engine import Event, all_paths, belief_ref, beliefs, reality_ref

F = frozenset
A, B, C, D = 0, 1, 2, 3
BOX, DRAWER, BASKET = 0, 1, 2


def table(events, n=4, order=4):
    return beliefs(n, 1, events, order)


def test_sally_anne_first_order_false_belief():
    events = [
        Event("set", 0, BOX, F({A, B}), actor=A),  # Sally puts the ball in the box, Anne watches
        Event("set", 0, DRAWER, F({B}), actor=B),  # Sally is out; Anne moves it
    ]
    t = table(events)
    assert t.reality(0) == DRAWER
    assert t.get((A,), 0) == BOX
    assert t.get((B,), 0) == DRAWER
    assert t.get((B, A), 0) == BOX  # Anne knows Sally still thinks box
    assert t.get((A, B), 0) == BOX  # Sally thinks Anne thinks box


def test_second_order_false_belief_via_covert_witness():
    # Perner and Wimmer: John does not know that Mary saw the van move.
    events = [
        Event("set", 0, BOX, F({A, B}), actor=A),
        Event("set", 0, DRAWER, F({B}), covert=F({A}), actor=B),  # A watches unnoticed
    ]
    t = table(events)
    assert t.get((A,), 0) == DRAWER
    assert t.get((B, A), 0) == BOX  # B wrongly thinks A still believes box
    assert t.get((A, B, A), 0) == BOX  # and A knows that B thinks so
    assert t.get((A, B), 0) == DRAWER


def test_presumed_witness():
    events = [
        Event("set", 0, BOX, F({A, B, C}), actor=A),
        Event("set", 0, DRAWER, F({A, C}), presumed=F({B}), actor=A),  # B misses it, nobody notices
    ]
    t = table(events)
    assert t.get((B,), 0) == BOX
    assert t.get((A, B), 0) == DRAWER  # A wrongly thinks B saw
    assert t.get((C, A, B), 0) == DRAWER
    assert t.get((B, A), 0) == BOX
    assert t.get((A, B, A), 0) == DRAWER


def test_lie_and_overhearing():
    events = [
        Event("set", 0, BOX, F({A, B, C, D}), actor=A),
        Event("set", 0, DRAWER, F({A}), actor=A),  # A moves it alone
        Event("tell", 0, BASKET, F({A, B}), covert=F({C}), actor=A, sincere=False, channel="private"),
    ]
    t = table(events)
    assert t.get((A,), 0) == DRAWER  # the liar keeps the truth
    assert t.get((B,), 0) == BASKET  # the listener is fooled
    assert t.get((B, A), 0) == BASKET  # and takes the liar to believe it
    assert t.get((A, B), 0) == BASKET
    assert t.get((A, B, A), 0) == BASKET
    assert t.get((C,), 0) == BASKET  # the eavesdropper is fooled too
    assert t.get((C, B), 0) == BASKET
    assert t.get((A, C), 0) == BOX  # A does not know C overheard
    assert t.get((B, C), 0) == BOX
    assert t.get((D,), 0) == BOX
    assert t.get((D, A), 0) == BOX


def test_mistaken_honest_tell_spreads_a_false_belief():
    events = [
        Event("set", 0, BOX, F({A, B, C}), actor=A),
        Event("set", 0, DRAWER, F({C}), actor=C),
        Event("set", 0, BASKET, F({A}), actor=A),  # A finds it and moves it again, alone
        Event("tell", 0, DRAWER, F({C, B}), actor=C, channel="private"),  # C is out of date
    ]
    t = table(events)
    assert t.reality(0) == BASKET
    assert t.get((B,), 0) == DRAWER
    assert t.get((C,), 0) == DRAWER
    assert t.get((A, B), 0) == BOX  # A knows nothing of the message
    assert t.get((B, C, A), 0) == BOX


def test_ignorance_of_a_fact_introduced_to_a_partial_audience():
    events = [Event("set", 0, BOX, F({A, B}), covert=F({C}), actor=A)]
    t = table(events)
    assert t.get((D,), 0) is None
    assert t.get((A, D), 0) is None
    assert t.get((A, C), 0) is None  # A does not know C watched
    assert t.get((C, A), 0) == BOX


def random_event(rng: random.Random, n_agents: int, n_vars: int, n_values: int) -> Event:
    agents = list(range(n_agents))
    rng.shuffle(agents)
    n_overt = rng.randint(1, n_agents)
    overt = agents[:n_overt]
    rest = agents[n_overt:]
    covert = [a for a in rest if rng.random() < 0.3]
    presumed = [a for a in rest if a not in covert and rng.random() < 0.3]
    kind = rng.choice(["set", "see", "tell"])
    return Event(
        kind,
        rng.randrange(n_vars),
        rng.randrange(n_values),
        F(overt),
        F(covert),
        F(presumed),
        actor=rng.choice(overt),
        sincere=kind != "tell" or rng.random() < 0.6,
    )


def test_incremental_rule_matches_reference_on_random_stories():
    rng = random.Random(20261120)
    checked = 0
    for _ in range(600):
        n_agents, n_vars, max_order = rng.randint(2, 5), rng.randint(1, 2), 4
        events = [random_event(rng, n_agents, n_vars, 4) for _ in range(rng.randint(1, 14))]
        t = beliefs(n_agents, n_vars, events, max_order)
        for var in range(n_vars):
            assert t.reality(var) == reality_ref(events, var)
            for path in all_paths(n_agents, max_order):
                assert t.get(path, var) == belief_ref(path, events, var), (path, var, events)
                checked += 1
    assert checked > 100_000


def test_settled_beliefs_and_contested_ones():
    events = [
        Event("set", 0, BOX, F({A, B, C, D}), actor=A),
        Event("set", 0, DRAWER, F({A, B}), actor=A),  # C and D are out; A and B see that
    ]
    t = table(events)
    assert t.get((A, C), 0) == BOX and t.settled((A, C), 0)  # A saw the move and saw that C was not there
    t.apply(Event("tell", 0, BASKET, F({B, C}), actor=B, sincere=False, channel="private"))
    assert t.settled((C, B), 0) and t.get((C, B), 0) == BASKET  # C takes B to believe what B said
    assert t.get((C, D), 0) == BOX and not t.settled((C, D), 0)  # C now knows of a change, but not who else saw it
    assert t.settled((A, C), 0)  # A knows nothing of the message
    t.apply(Event("set", 0, BOX, F({C, D}), actor=D))  # C watches a move from a place C did not expect
    assert t.settled((C, D), 0) and not t.settled((C, A), 0)
