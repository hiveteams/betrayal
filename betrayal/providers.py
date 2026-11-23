"""Model clients: one function per provider turns a prompt into a Reply.

Every model gets the same single user message (with its pictures, if any) and the same named reasoning effort.
No system prompt, no tools, no sampling settings. Refusal fallbacks are left off on
purpose: a benchmark must score the model it names, not a stand-in.

Two routes reach a model. With an API key in the environment, the call goes to the provider's
API. Without one, Claude, Gemini and Muse models run through the command-line tool of a signed-in
subscription (`claude`, `agy`, `muse`), one fresh session per prompt, in a folder that holds
nothing but that prompt's own pictures.

The routes are not equal, and the report says which one each row used. The API sends the prompt
alone. `claude` runs with a one-line system prompt and no tools or connectors, and adds about 850
tokens of notes on the folder, the date and the model. `agy` is Google's coding agent: it adds
about 25,000 tokens of its own instructions, tools and the user's global notes, and no flag
turns them off. The model `agy-claude-opus-5-5` is a control for that: a Claude model inside `agy`.
"""

from __future__ import annotations

import base64
import json
import os
import shutil
import subprocess
import time
from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Optional, Sequence


@dataclass(frozen=True)
class Model:
    name: str
    provider: str
    price_in: float  # USD per million input tokens
    price_out: float  # USD per million output tokens; reasoning tokens are billed as output
    label: str
    lab: str


MODELS = {
    model.name: model
    for model in [
        Model("claude-fable-5-2", "anthropic", 8.00, 40.00, "Claude Fable 5.2", "Anthropic"),
        Model("claude-opus-5-5", "anthropic", 4.00, 20.00, "Claude Opus 5.5", "Anthropic"),
        Model("claude-sonnet-5-5", "anthropic", 2.00, 10.00, "Claude Sonnet 5.5", "Anthropic"),
        Model("claude-haiku-5-5", "anthropic", 0.10, 0.50, "Claude Haiku 5.5", "Anthropic"),
        Model("gpt-6.2-astra", "openai", 8.00, 40.00, "GPT-6.2 Astra", "OpenAI"),
        Model("gpt-6.2-sol", "openai", 2.00, 10.00, "GPT-6.2 Sol", "OpenAI"),
        Model("gpt-6.1-terra", "openai", 1.00, 5.00, "GPT-6.1 Terra", "OpenAI"),
        Model("gpt-6-luna", "openai", 0.10, 0.50, "GPT-6 Luna", "OpenAI"),
        # reached through a subscription tool, so no API prices
        Model("gemini-4-carbon", "agy", 0, 0, "Gemini 4 Carbon", "Google"),
        Model("gemini-4-argon", "agy", 0, 0, "Gemini 4 Argon", "Google"),
        Model("gemini-4-neon", "agy", 0, 0, "Gemini 4 Neon", "Google"),
        Model("gemini-4-hydrogen", "agy", 0, 0, "Gemini 4 Hydrogen", "Google"),
        # route controls: Anthropic models inside Google's agent tool, isolating the 25k-token harness effect
        Model("agy-claude-opus-5-5", "agy", 0, 0, "Claude Opus 5.5 in Google's agent", "Anthropic"),
        Model("agy-claude-sonnet-5-5", "agy", 0, 0, "Claude Sonnet 5.5 in Google's agent", "Anthropic"),
        Model("muse-wonder-1.0", "muse", 0, 0, "Muse Wonder 1.0", "Meta"),
        Model("muse-spark-1.3", "muse", 0, 0, "Muse Spark 1.3", "Meta"),
        Model("muse-ember-1.0", "muse", 0, 0, "Muse Ember 1.0", "Meta"),
    ]
}


@dataclass(frozen=True)
class Reply:
    text: str
    stop: str  # "end" | "max_tokens" | "refusal" | another provider value
    served_model: str
    input_tokens: int
    output_tokens: int  # includes reasoning tokens
    reasoning_tokens: Optional[int]
    seconds: float

    def cost(self, model: Model) -> float:
        return (self.input_tokens * model.price_in + self.output_tokens * model.price_out) / 1e6


@cache
def _anthropic_client():
    import anthropic

    return anthropic.Anthropic(timeout=900.0, max_retries=3)


@cache
def _openai_client(base_url: Optional[str] = None, key_var: str = "OPENAI_API_KEY"):
    import openai

    return openai.OpenAI(api_key=os.environ[key_var], base_url=base_url, timeout=900.0, max_retries=3)


@cache
def _google_client():
    from google import genai

    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def _png(path: str) -> str:
    return base64.standard_b64encode(Path(path).read_bytes()).decode()


def _anthropic(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str]) -> Reply:
    pictures = [{"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": _png(p)}} for p in images]
    start = time.monotonic()
    message = _anthropic_client().messages.create(
        model=model.name,
        max_tokens=max_tokens,
        output_config={"effort": effort},
        messages=[{"role": "user", "content": [*pictures, {"type": "text", "text": prompt}]}],
    )
    seconds = time.monotonic() - start
    text = "".join(block.text for block in message.content if block.type == "text")
    stop = "end" if message.stop_reason == "end_turn" else message.stop_reason
    return Reply(text, stop, message.model, message.usage.input_tokens, message.usage.output_tokens, None, seconds)


def _openai(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str]) -> Reply:
    pictures = [{"type": "input_image", "image_url": f"data:image/png;base64,{_png(p)}"} for p in images]
    start = time.monotonic()
    response = _openai_client().responses.create(
        model=model.name,
        input=[{"role": "user", "content": [{"type": "input_text", "text": prompt}, *pictures]}],
        reasoning={"effort": effort},
        max_output_tokens=max_tokens,
        store=False,
    )
    seconds = time.monotonic() - start
    stop = "end"
    if response.status == "incomplete":
        reason = response.incomplete_details.reason
        stop = "max_tokens" if reason == "max_output_tokens" else reason
    elif any(part.type == "refusal" for out in response.output if out.type == "message" for part in out.content):
        stop = "refusal"
    usage = response.usage
    return Reply(
        response.output_text, stop, response.model, usage.input_tokens, usage.output_tokens,
        usage.output_tokens_details.reasoning_tokens, seconds,
    )


def _google(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str]) -> Reply:
    from google.genai import types

    pictures = [types.Part.from_bytes(data=Path(p).read_bytes(), mime_type="image/png") for p in images]
    start = time.monotonic()
    response = _google_client().models.generate_content(
        model=model.name,
        contents=[*pictures, prompt],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level=effort),
            max_output_tokens=max_tokens,
        ),
    )
    seconds = time.monotonic() - start
    usage = response.usage_metadata
    thoughts = usage.thoughts_token_count or 0
    finish = response.candidates[0].finish_reason.name if response.candidates else "NO_CANDIDATE"
    stop = {"STOP": "end", "MAX_TOKENS": "max_tokens", "SAFETY": "refusal"}.get(finish, finish)
    return Reply(
        response.text or "", stop, response.model_version or model.name, usage.prompt_token_count or 0,
        (usage.candidates_token_count or 0) + thoughts, thoughts, seconds,
    )


COMPATIBLE = {  # providers that speak the OpenAI chat API: base URL and the variable that holds the key
    "xai": ("https://api.x.ai/v1", "XAI_API_KEY"),
    "openrouter": ("https://openrouter.ai/api/v1", "OPENROUTER_API_KEY"),
}


def _compatible(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str]) -> Reply:
    pictures = [{"type": "image_url", "image_url": {"url": f"data:image/png;base64,{_png(p)}"}} for p in images]
    start = time.monotonic()
    completion = _openai_client(*COMPATIBLE[model.provider]).chat.completions.create(
        model=model.name,
        messages=[{"role": "user", "content": [{"type": "text", "text": prompt}, *pictures]}],
        reasoning_effort=effort,
        max_completion_tokens=max_tokens,
    )
    seconds = time.monotonic() - start
    choice, usage = completion.choices[0], completion.usage
    stop = {"stop": "end", "length": "max_tokens", "content_filter": "refusal"}.get(choice.finish_reason, choice.finish_reason)
    details = usage.completion_tokens_details
    return Reply(
        choice.message.content or "", stop, completion.model, usage.prompt_tokens,
        usage.total_tokens - usage.prompt_tokens, details.reasoning_tokens if details else None, seconds,
    )


# The command-line tools start in a folder, and an agent can look round it. So a text prompt runs in a folder
# that stays empty, and a picture prompt runs in a folder that holds its own pictures and nothing else. The
# names say nothing about a test: an agent once took a folder called "room" for the room in the story.
DESK = Path.home() / "desk"


def _tool(command: list[str], images: Sequence[str]) -> tuple[str, float]:
    """Run a subscription tool on one prompt. Returns (what it printed, seconds)."""
    folder = DESK / (Path(images[0]).stem if images else "empty")
    folder.mkdir(parents=True, exist_ok=True)
    for image in images:
        shutil.copy(image, folder / Path(image).name)
    start = time.monotonic()
    done = subprocess.run(command, cwd=folder, capture_output=True, text=True, timeout=1800, stdin=subprocess.DEVNULL)
    if done.returncode != 0:
        raise RuntimeError(f"{command[0]} exited {done.returncode}: {done.stdout[-200:]} {done.stderr[-200:]}")
    return done.stdout, time.monotonic() - start


def _with_pictures(prompt: str, images: Sequence[str]) -> str:
    """The tools take pictures as files that the model opens itself."""
    if not images:
        return prompt
    return "Picture file to open and look at: " + ", ".join(Path(image).name for image in images) + "\n\n" + prompt


def _claude_tool(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str]) -> Reply:
    printed, seconds = _tool([
        "claude", "-p", _with_pictures(prompt, images), "--model", model.name, "--effort", effort,
        "--tools", "Read" if images else "", "--system-prompt", "You are a helpful assistant.",
        "--setting-sources", "", "--output-format", "json", "--no-session-persistence",
        # without these the tool sends the definitions of every connected service with each prompt
        "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}', "--disable-slash-commands",
    ], images)
    result = json.loads(printed)
    if result.get("is_error"):
        raise RuntimeError(f"claude: {str(result.get('result'))[:300]}")
    usage = result.get("usage", {})
    read = usage.get("input_tokens", 0) + usage.get("cache_creation_input_tokens", 0) + usage.get("cache_read_input_tokens", 0)
    thinking = usage.get("output_tokens_details", {}).get("thinking_tokens")
    served = ", ".join(result.get("modelUsage", {})) or model.name
    return Reply(result["result"], "end", served, read, usage.get("output_tokens", 0), thinking, seconds)


def _agy_tool(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str]) -> Reply:
    printed, seconds = _tool([
        "agy", "-p", _with_pictures(prompt, images), "--model", f"{model.name.removeprefix('agy-')}-{effort}", "--output-format", "json",
        *(["--dangerously-skip-permissions"] if images else []),
    ], images)
    result = json.loads(printed)
    if result.get("status") != "SUCCESS":
        raise RuntimeError(f"agy: {str(result)[:300]}")
    usage = result.get("usage", {})
    return Reply(
        result["response"], "end", f"{model.name}-{effort}", usage.get("input_tokens", 0),
        usage.get("output_tokens", 0), usage.get("thinking_tokens"), seconds,
    )


def _muse_tool(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str]) -> Reply:
    printed, seconds = _tool(["muse", "exec", "--model", model.name, "--reasoning-effort", effort, _with_pictures(prompt, images)], images)
    return Reply(printed.strip(), "end", model.name, 0, 0, None, seconds)


def _claude(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str]) -> Reply:
    route = _anthropic if os.environ.get("ANTHROPIC_API_KEY") else _claude_tool
    return route(model, prompt, effort, max_tokens, images)


CALLERS = {
    "anthropic": _claude, "openai": _openai, "google": _google, "xai": _compatible, "openrouter": _compatible,
    "agy": _agy_tool, "muse": _muse_tool,
}


def call(model: Model, prompt: str, effort: str, max_tokens: int, images: Sequence[str] = ()) -> Reply:
    return CALLERS[model.provider](model, prompt, effort, max_tokens, images)
