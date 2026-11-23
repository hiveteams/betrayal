"""Booklet runs: for models that are reached through a subscription agent, not an API.

  exam     make one folder per model with the booklet and its pictures, and nothing else (no answer key)
  collect  score the answer file that a model wrote, into the same result rows that `run.py` writes

  uv run python -m betrayal.booklet exam --data data/betrayal-v2.jsonl --root ~/betrayal-exam --models gemini-4-carbon
  uv run python -m betrayal.booklet collect --data data/betrayal-v2.jsonl --root ~/betrayal-exam --models gemini-4-carbon

A booklet run is less strict than an API run: the model sees all questions in one context and
works inside an agent's own instructions. The report shows which method each row used.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from . import obvious
from .grade import grade


def exam(data: Path, root: Path, models: list[str]) -> None:
    """Give each model its own folder: the Obvious booklet, the pictures it names, and room for answers."""
    items = [item for item in map(json.loads, data.read_text().splitlines()) if item["part"] == "obvious"]
    for model in models:
        folder = root / model
        (folder / "pictures").mkdir(parents=True, exist_ok=True)
        copies = []
        for item in items:
            picture = item["picture"]
            if picture:
                shutil.copy(picture, folder / "pictures" / Path(picture).name)
                picture = str(folder / "pictures" / Path(picture).name)
            copies.append({**item, "picture": picture})
        (folder / "booklet.md").write_text(obvious.booklet(copies))


def collect(data: Path, answers: Path, model: str, run: str) -> tuple[int, int]:
    """Write result rows for every answered question. Returns (right, answered)."""
    items = {item["id"]: item for item in map(json.loads, data.read_text().splitlines())}
    given = json.loads(answers.read_text())
    rows = []
    for key, raw in given.items():
        if key not in items:
            continue
        item = items[key]
        marker = "SCRIPT" if item["kind"] in ("plan", "explain") else "ANSWER"
        text = f"{marker}: {raw if isinstance(raw, str) else json.dumps(raw)}"
        answer, correct, note = grade(item, text)
        rows.append({
            "id": key, "model": model, "effort": "booklet", "status": "ok" if answer is not None else "no_answer",
            "answer": answer, "correct": answer is not None and correct, "note": note, "stop": "end",
            "served_model": model, "input_tokens": 0, "output_tokens": 0, "reasoning_tokens": None,
            "seconds": 0.0, "cost_usd": 0.0, "attempts": 1, "text": text,
        })
    folder = Path("results") / run / f"{model}@booklet"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "results.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    return sum(row["correct"] for row in rows), len(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("step", choices=["exam", "collect"])
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True, help="the folder that holds one folder per model")
    parser.add_argument("--models", nargs="+", required=True)
    parser.add_argument("--run", default="main")
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    if args.step == "exam":
        exam(args.data, root, args.models)
        print(f"booklets for {len(args.models)} models in {root}")
        return
    for model in args.models:
        answers = root / model / "answers.json"
        if answers.exists():
            right, answered = collect(args.data, answers, model, args.run)
            print(f"{model}: {right}/{answered} right")
        else:
            print(f"{model}: no answer file yet")


if __name__ == "__main__":
    main()
