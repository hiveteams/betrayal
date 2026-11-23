"""Repeat chosen questions: does a model give the same answer every time?

  uv run python -m betrayal.repeat --data data/betrayal-v2.jsonl --ids Q027 Q088 Q089 --models gemini-4-carbon --times 5

One wrong answer can be chance. This asks the same question several times, each in a fresh
session, and writes results/<run>/repeats/<model>.jsonl. The report shows how many were right.
"""

from __future__ import annotations

import argparse
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .grade import grade
from .providers import MODELS, call


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--ids", nargs="+", required=True)
    parser.add_argument("--models", nargs="+", required=True)
    parser.add_argument("--times", type=int, default=5)
    parser.add_argument("--run", default="main")
    parser.add_argument("--effort", default="high")
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    items = {item["id"]: item for item in map(json.loads, args.data.read_text().splitlines())}
    out = Path("results") / args.run / "repeats"
    out.mkdir(parents=True, exist_ok=True)
    lock = threading.Lock()
    jobs = []
    for name in args.models:
        path = out / f"{name}.jsonl"
        done = {(row["id"], row["repeat"]) for row in map(json.loads, path.read_text().splitlines())} if path.exists() else set()
        jobs += [(name, key, repeat) for key in args.ids for repeat in range(args.times) if (key, repeat) not in done]

    def work(job: tuple[str, str, int]) -> None:
        name, key, repeat = job
        item = items[key]
        try:
            reply = call(MODELS[name], item["prompt"], args.effort, 32000, item.get("images", ()))
        except Exception as error:  # a failed call is left for the next run, never scored
            print(f"  {name} {key}: {type(error).__name__}: {str(error)[:120]}", flush=True)
            return
        answer, correct, _ = grade(item, reply.text)
        row = {"id": key, "model": name, "repeat": repeat, "answer": answer, "correct": bool(answer is not None and correct), "text": reply.text}
        with lock, (out / f"{name}.jsonl").open("a") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(work, jobs))
    for name in args.models:
        rows = [json.loads(line) for line in (out / f"{name}.jsonl").read_text().splitlines()] if (out / f"{name}.jsonl").exists() else []
        for key in args.ids:
            mine = [row for row in rows if row["id"] == key]
            print(f"{name} {key}: {sum(row['correct'] for row in mine)} of {len(mine)} right")


if __name__ == "__main__":
    main()
