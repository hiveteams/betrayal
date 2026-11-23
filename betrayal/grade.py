"""Grading: read the model's final answer and decide whether it is right."""

from __future__ import annotations

import json
import re
from typing import Optional

from . import arena, obvious, sight
from .inverse import grade_script
from .questions import LETTERS, NOBODY_WORD

ANSWER_LINE = re.compile(r"ANSWER\s*:\s*(.*)", re.IGNORECASE)
LETTER = re.compile(r"[(\[]?([A-F])(?![A-Za-z])")
NOBODY = re.compile(r"\b(nobody|no one|no-one|none)\b", re.IGNORECASE)


def parse(item: dict, text: str) -> Optional[str]:
    """The model's answer, or None when the reply has no readable answer."""
    lines = ANSWER_LINE.findall(text)
    if not lines:
        return None
    raw = lines[-1].strip().strip("*_`").strip()
    if item["kind"] == "inform":
        others = [name for name in item["names"] if name != item["path"][0]]
        named = sorted(name for name in others if re.search(rf"\b{re.escape(name)}\b", raw, re.IGNORECASE))
        if named:
            return ", ".join(named)
        return NOBODY_WORD if NOBODY.search(raw) else None
    match = LETTER.match(raw)
    if match and LETTERS.index(match.group(1)) < len(item["options"]):
        return match.group(1)
    spelled = [LETTERS[i] for i, option in enumerate(item["options"]) if option.lower() in raw.lower()]
    return spelled[0] if len(spelled) == 1 else None


def grade(item: dict, text: str) -> tuple[Optional[str], bool, str]:
    """(the answer as read, whether it is right, a short note). The answer is None when none can be read."""
    if item["part"] == "sight":
        return sight.grade(item, text)
    if item["part"] == "obvious":
        lines = ANSWER_LINE.findall(text)
        answer, right = obvious.grade_answer(item, lines[-1]) if lines else (None, False)
        return answer, right, ""
    if item["kind"] in ("plan", "explain"):
        return grade_script(item, text)
    if item["kind"] == "arena":  # no right answer: the report scores the moves against the other models
        play = arena.read(item, text)
        return (None if play is None else json.dumps(play)), False, ""
    answer = parse(item, text)
    return answer, answer == item["gold"], ""
