"""Run models on a dataset.

  uv run python -m betrayal.run --data data/betrayal-v1.jsonl --models gpt-6-luna claude-haiku-5-5

Each model writes to results/<run>/<model>@<effort>/:

  results.jsonl  one row per item that produced a reply (the run resumes from this file)
  errors.jsonl   attempts with no scorable reply: API errors, timeouts, a different served model

A row's status is `ok` (an answer was read), `no_answer` (a full reply with no readable answer),
`truncated` (cut off at the token limit) or `refused`. Only `ok` rows can be correct. Truncated
rows are reported and kept out of the accuracy figures, because they measure the limit, not the model.

Names that start with `baseline:` are lazy strategies run through the same grader:
oracle, random, reality, inner, outer, first.
"""

from __future__ import annotations

import argparse
import json
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import arena
from .grade import grade
from .providers import MODELS, Model, Reply, call
from .questions import LETTERS, NOBODY_WORD

BASELINES = ("oracle", "random", "reality", "inner", "outer", "first")


def baseline_reply(strategy: str, item: dict) -> Reply:
    rng = random.Random(f"{strategy}-{item['id']}")
    if item["kind"] == "arena":  # a uniformly random legal move, whatever the strategy
        game = arena.GAMES[item["game"]]
        if game.parts:
            soldiers, fields = game.parts
            cuts = sorted(rng.randint(0, soldiers) for _ in range(fields - 1))
            move = ", ".join(str(b - a) for a, b in zip([0, *cuts], [*cuts, soldiers]))
        else:
            move = rng.choice(game.actions)
        return Reply(f"CHOICE: {move}\nFORECAST: none", "end", f"baseline:{strategy}", 0, 0, 0, 0.0)
    if item["part"] == "obvious":  # the right answer, or a random one of the listed choices
        answer = item["gold"] if strategy == "oracle" else rng.choice(LETTERS[: len(item["choices"])] if item["kind"] == "everyday" else item["choices"])
        return Reply(f"ANSWER: {answer}", "end", f"baseline:{strategy}", 0, 0, 0, 0.0)
    if item["kind"] in ("plan", "explain"):  # the reference script, or an empty one
        return Reply(f"SCRIPT: {item['gold'] if strategy == 'oracle' else '[]'}", "end", f"baseline:{strategy}", 0, 0, 0, 0.0)
    if strategy == "oracle":
        answer = item["gold"]
    elif item["kind"] == "inform":
        others = [name for name in item["names"] if name != item["path"][0]]
        picked = sorted(name for name in others if rng.random() < 0.5)
        answer = (", ".join(picked) or NOBODY_WORD) if strategy == "random" else item["shortcuts"]["omniscient"]
    elif strategy == "random" or strategy not in item["shortcuts"]:
        answer = rng.choice(LETTERS[: len(item["options"])])
    else:
        answer = item["shortcuts"][strategy]
    return Reply(f"ANSWER: {answer}", "end", f"baseline:{strategy}", 0, 0, 0, 0.0)


def answer_item(model: Model | None, name: str, item: dict, effort: str, max_tokens: int, tries: int) -> dict:
    """One results row, or one errors row (it has an `error` key)."""
    for attempt in range(1, tries + 1):
        try:
            if model is None:
                reply = baseline_reply(name.split(":")[1], item)
            else:
                reply = call(model, item["prompt"], effort, max_tokens, item.get("images", ()))
                if model.name not in reply.served_model:
                    raise RuntimeError(f"asked for {model.name}, served by {reply.served_model}")
            break
        except Exception as error:  # every provider failure is recorded, never scored
            failure = f"{type(error).__name__}: {error}"[:500]
            if attempt == tries or getattr(error, "status_code", None) in (400, 401, 403, 404):  # no use in retrying
                return {"id": item["id"], "model": name, "effort": effort, "error": failure, "attempts": attempt}
            time.sleep(min(60, 2**attempt) * (0.5 + random.random()))
    answer, correct, note = grade(item, reply.text)
    if reply.stop == "refusal":
        status = "refused"
    elif answer is not None:
        status = "ok"
    elif reply.stop == "max_tokens":
        status = "truncated"
    else:
        status = "no_answer"
    return {
        "id": item["id"],
        "model": name,
        "effort": effort,
        "status": status,
        "answer": answer,
        "correct": None if item["kind"] == "arena" else status == "ok" and correct,
        "note": note,
        "stop": reply.stop,
        "served_model": reply.served_model,
        "input_tokens": reply.input_tokens,
        "output_tokens": reply.output_tokens,
        "reasoning_tokens": reply.reasoning_tokens,
        "seconds": round(reply.seconds, 2),
        "cost_usd": round(reply.cost(model), 6) if model else 0.0,
        "attempts": attempt,
        "text": reply.text,
    }


def run_model(name: str, items: list[dict], out_dir: Path, args: argparse.Namespace) -> None:
    model = None if name.startswith("baseline:") else MODELS[name]
    folder = out_dir / (name.replace(":", "-") if model is None else f"{name}@{args.effort}")
    folder.mkdir(parents=True, exist_ok=True)
    results_path, errors_path = folder / "results.jsonl", folder / "errors.jsonl"
    done = {}
    if results_path.exists():
        done = {row["id"]: row for row in map(json.loads, results_path.read_text().splitlines())}
    todo = [item for item in items if item["id"] not in done]
    spent = sum(row["cost_usd"] for row in done.values())
    lock = threading.Lock()
    counts = {"rows": 0, "correct": 0, "errors": 0}

    def work(item: dict) -> None:
        nonlocal spent
        with lock:
            if spent >= args.max_cost:
                return
        row = answer_item(model, name, item, args.effort, args.max_tokens, args.tries)
        with lock:
            if "error" in row:
                counts["errors"] += 1
                with errors_path.open("a") as handle:
                    handle.write(json.dumps(row) + "\n")
                return
            spent += row["cost_usd"]
            counts["rows"] += 1
            counts["correct"] += bool(row["correct"])
            with results_path.open("a") as handle:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            if counts["rows"] % 50 == 0:
                print(f"  {name}: {counts['rows']}/{len(todo)} done, {counts['correct'] / counts['rows']:.0%} right, ${spent:.2f}", flush=True)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(work, todo))
    stopped = " (stopped at the cost cap)" if spent >= args.max_cost else ""
    print(f"{name}: {counts['rows']} new rows, {counts['errors']} errors, {len(done)} already done, ${spent:.2f} total{stopped}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--models", nargs="+", required=True)
    parser.add_argument("--run", default="main", help="results/<run>/")
    parser.add_argument("--effort", default="high")
    parser.add_argument("--max-tokens", type=int, default=32000)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--tries", type=int, default=3)
    parser.add_argument("--max-cost", type=float, default=float("inf"), help="USD cap per model")
    parser.add_argument("--only", nargs="*", default=None, help="keep items whose id starts with one of these")
    args = parser.parse_args()
    items = [json.loads(line) for line in args.data.read_text().splitlines()]
    if args.only:
        items = [item for item in items if item["id"].startswith(tuple(args.only))]
    names = [f"baseline:{b}" for b in BASELINES] if args.models == ["baselines"] else args.models
    out_dir = Path("results") / args.run
    threads = [threading.Thread(target=run_model, args=(name, items, out_dir, args)) for name in names]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
