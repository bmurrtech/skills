"""Estimate transcript size and hint direct vs map-reduce strategy."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Rough: 1 token ≈ 0.75 words → tokens ≈ words * 4/3
WORDS_PER_TOKEN = 0.75
# Advisory bar: above this, hint map-reduce (agent still judges fit).
# Aligned with default chunk size so long inputs prefer map-reduce.
MAP_REDUCE_WORD_HINT = 4000


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8-sig")


def word_count(text: str) -> int:
    return len(text.split())


def token_estimate(words: int) -> int:
    return int(words / WORDS_PER_TOKEN) if words else 0


def strategy_hint(words: int) -> str:
    return "map-reduce" if words >= MAP_REDUCE_WORD_HINT else "direct"


def assess(text: str) -> dict[str, int | str]:
    words = word_count(text)
    return {
        "words": words,
        "tokens_approx": token_estimate(words),
        "strategy_hint": strategy_hint(words),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Estimate transcript size; hint direct vs map-reduce."
    )
    parser.add_argument(
        "path",
        help="Transcript file path, or - for stdin",
    )
    args = parser.parse_args(argv)
    text = read_text(args.path)
    result = assess(text)
    print(f"words: {result['words']}")
    print(f"tokens_approx: {result['tokens_approx']}")
    print(f"strategy_hint: {result['strategy_hint']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
