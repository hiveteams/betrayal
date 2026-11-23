"""Build a dataset: `uv run python -m betrayal.build --n 60 --seed 1 --out data/betrayal-v1.jsonl`.

Scenario i takes its skin, fact count and length from a fixed 12-cell cycle, so both skins
get the same mix. Seeds that cannot fill every question slot are skipped; the seed that was
used is stored on each item, so any item can be rebuilt.
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from . import arena, obvious
from .engine import beliefs
from .generate import GenConfig, Scenario, generate
from .inverse import EXPLAIN_LEVELS, PLAN_LEVELS, make_task, render_task
from .questions import Ask, pick, render
from .skins import SKINS

LENGTHS = (8, 11, 14)
SKIN_KEYS = ("classic", "workplace")


def cell(index: int) -> tuple[str, int, int]:
    return SKIN_KEYS[index % 2], 1 + (index // 2) % 2, LENGTHS[(index // 4) % 3]


HEAVY = {"n_agents": 8, "n_events": 40, "max_order": 6}


def build_scenario(index: int, base_seed: int, overrides: dict) -> tuple[Scenario, list[Ask], str]:
    skin_key, n_vars, n_events = cell(index)
    cfg = GenConfig(**{"n_vars": n_vars, "n_events": n_events, **overrides})
    for attempt in range(10_000):
        seed = base_seed * 1_000_000 + (300_000 if overrides else 0) + index * 1_000 + attempt
        scenario = generate(seed, cfg)
        asks = pick(scenario, random.Random(seed + 1))
        if asks is not None:
            return scenario, asks, skin_key
    raise RuntimeError(f"no usable scenario for index {index}")


def build(n: int, base_seed: int, overrides: dict, level: str = "standard") -> tuple[list[dict], list[str]]:
    """Tracking scenarios with their questions. Ids start with T (standard) or H (heavy)."""
    items, audit = [], []
    for index in range(n):
        scenario, asks, skin_key = build_scenario(index, base_seed, overrides)
        name = f"{level[0].upper()}{index:03d}"
        skin = SKINS[skin_key](scenario, random.Random(scenario.seed + 2))
        cfg = scenario.cfg
        table = beliefs(cfg.n_agents, cfg.n_vars, scenario.events, cfg.max_order)
        audit.append(f"\n## Scenario {name} ({skin_key}, {cfg.n_vars} fact(s), {cfg.n_events} events, seed {scenario.seed})\n")
        audit.append(skin.story() + "\n")
        for ask in asks:
            text = render(skin, ask, random.Random(f"{scenario.seed}-{ask.slot}"))
            item = {
                "id": f"{name}-{ask.slot}",
                "scenario": name,
                "seed": scenario.seed,
                "part": "track",
                "level": level,
                "skin": skin_key,
                "n_vars": cfg.n_vars,
                "n_events": cfg.n_events,
                "slot": ask.slot,
                "kind": ask.kind,
                "order": ask.order,
                "tier": ask.tier,
                "path": [skin.names[a] for a in ask.path],
                "contested": _contested(table, ask, cfg.n_agents),
                "names": sorted(skin.names),
                **text,
            }
            items.append(item)
            question = text["prompt"].split("Question: ")[1].split("\n")[0]
            options = " | ".join(f"{'ABCDEF'[i]}. {o}" for i, o in enumerate(text["options"]))
            trail = ""
            if ask.kind in ("belief", "action"):
                steps = [
                    f"{'>'.join(skin.names[a] for a in ask.path[:depth])}={_label(skin, ask.var, table.get(ask.path[:depth], ask.var))}"
                    for depth in range(1, len(ask.path) + 1)
                ]
                trail = f" [real={_label(skin, ask.var, table.reality(ask.var))}; " + "; ".join(steps) + "]"
            audit.append(f"- **{ask.slot}** (tier {ask.tier}) {question}\n  {options}\n  gold: **{text['gold']}**{trail}")
    return items, audit


def _label(skin, var: int, value) -> str:
    return "no idea" if value is None else skin.value_label(var, value)


def _contested(table, ask: Ask, n_agents: int) -> bool:
    """A careful reader could argue with the answer key (see `Beliefs.settled`). The report sets such items aside."""
    if ask.kind == "inform":
        return any(not table.settled((ask.path[0], other), ask.var) for other in range(n_agents) if other != ask.path[0])
    return bool(ask.path) and not table.settled(ask.path, ask.var)


def build_inverse(kind: str, per_level: int, base_seed: int) -> tuple[list[dict], list[str]]:
    """Plan or explain tasks: `per_level` at each level, alternating skins."""
    items, audit = [], []
    levels = PLAN_LEVELS if kind == "plan" else EXPLAIN_LEVELS
    for level in levels:
        seed = base_seed * 1_000_000 + (500_000 if kind == "plan" else 700_000) + level * 10_000
        for index in range(per_level):
            task = None
            while task is None:
                seed += 1
                task = make_task(kind, level, seed)
            skin_key = SKIN_KEYS[index % 2]
            skin = SKINS[skin_key](task["scenario"], random.Random(seed + 2))
            text = render_task(kind, task, skin)
            item = {
                "id": f"{kind}-L{level}-{index:03d}",
                "scenario": f"{kind}-L{level}-{index:03d}",
                "seed": seed,
                "part": kind,
                "level": f"L{level}",
                "skin": skin_key,
                "slot": f"{kind}-L{level}",
                "kind": kind,
                "order": task["max_order"],
                "n_targets": len(task["targets"]),
                "fits": task.get("fits"),
                **text,
            }
            items.append(item)
            audit.append(f"\n## {item['id']} ({skin_key}, seed {seed})\n\n{text['prompt']}\n\nreference: `{text['gold']}`")
    return items, audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=24, help="standard tracking scenarios")
    parser.add_argument("--heavy", type=int, default=0, help="heavy tracking scenarios: 8 people, 40 events, depth 6")
    parser.add_argument("--plan", type=int, default=0, help="plan tasks per level")
    parser.add_argument("--explain", type=int, default=0, help="explain tasks per level")
    parser.add_argument("--arena", type=int, default=0, help="plays of each arena game (an experiment, not scored)")
    parser.add_argument("--obvious", action="store_true", help="add the Obvious part, with its pictures and booklet")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out", type=Path, default=Path("data/betrayal-v1.jsonl"))
    parser.add_argument("--set", nargs="*", default=[], help="generator overrides, e.g. n_agents=6 p_lie=0.4")
    args = parser.parse_args()
    overrides = {key: json.loads(value) for key, value in (pair.split("=") for pair in args.set)}
    items, audit = build(args.n, args.seed, overrides)
    heavy_items, heavy_audit = build(args.heavy, args.seed, HEAVY, level="heavy")
    items += heavy_items
    audit += heavy_audit
    for kind, per_level in (("plan", args.plan), ("explain", args.explain)):
        more_items, more_audit = build_inverse(kind, per_level, args.seed)
        items += more_items
        audit += more_audit
    items += arena.items(args.arena)
    if args.obvious:
        folder = args.out.with_suffix("")
        plain = obvious.build(args.seed, (folder / "pictures").resolve())
        (folder / "booklet.md").write_text(obvious.booklet(plain))
        items = plain + items
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in items))
    args.out.with_suffix(".audit.md").write_text("\n".join(audit) + "\n")
    print(f"{len(items)} items -> {args.out}")


if __name__ == "__main__":
    main()
