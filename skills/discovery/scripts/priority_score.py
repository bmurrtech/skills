#!/usr/bin/env python3
"""Deterministic discovery priority: K/P/F/S bands -> BV, DR, Overall, P0-P3, rank.

LLM assigns bands (1-3, or null when unscored); this script applies the math only.
See skills/discovery/references/scoring.md.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from typing import Any

DIMENSIONS = ("K", "P", "F", "S")
BV_WEIGHT = Fraction(2, 5)
DR_WEIGHT = Fraction(3, 5)
THRESHOLDS = ((80, "P0"), (65, "P1"), (50, "P2"))
LABEL_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


def _band(name: str, value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 3:
        raise ValueError(f"{name} must be an integer 1-3 or null, got {value!r}")
    return value


def _label(overall: Fraction) -> str:
    for floor, label in THRESHOLDS:
        if overall >= floor:
            return label
    return "P3"


def _one_decimal(value: Fraction) -> float:
    return float(round(value, 1))


def score_one(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError(f"each use case must be an object, got {raw!r}")
    uid = str(raw.get("id", "")).strip()
    if not uid:
        raise ValueError("each use case needs a non-empty id")

    bands = {d: _band(f"{uid}.{d}", raw.get(d)) for d in DIMENSIONS}
    row = dict(raw)
    row.update(bands)
    row["id"] = uid

    missing = [d for d in DIMENSIONS if bands[d] is None]
    if missing:
        row.update(
            status="needs-discovery",
            priority="none",
            missing=missing,
            bv=None,
            dr=None,
            overall=None,
        )
        return row

    bv = Fraction(bands["K"] + bands["P"], 6) * 100
    dr = Fraction(bands["F"] + bands["S"], 6) * 100
    overall = bv * BV_WEIGHT + dr * DR_WEIGHT
    row.update(
        status="scored",
        priority=_label(overall),
        missing=[],
        bv=_one_decimal(bv),
        dr=_one_decimal(dr),
        overall=_one_decimal(overall),
        _exact=overall,
    )
    return row


def rank(use_cases: list[Any]) -> dict[str, list[dict[str, Any]]]:
    seen: set[str] = set()
    scored: list[dict[str, Any]] = []
    unscored: list[dict[str, Any]] = []
    for raw in use_cases:
        row = score_one(raw)
        if row["id"] in seen:
            raise ValueError(f"duplicate id {row['id']!r}")
        seen.add(row["id"])
        (scored if row["status"] == "scored" else unscored).append(row)

    scored.sort(
        key=lambda r: (LABEL_ORDER[r["priority"]], -r["_exact"], -r["S"], r["id"])
    )
    for i, row in enumerate(scored, start=1):
        del row["_exact"]
        row["rank"] = i
    return {"scored": scored, "unscored": unscored}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score discovery use cases (K/P/F/S -> BV, DR, Overall, P0-P3)."
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help='read JSON from stdin: {"use_cases":[{"id","K","P","F","S"}]}',
    )
    parser.add_argument("path", nargs="?", help='JSON file with {"use_cases":[...]}')
    args = parser.parse_args(argv)

    try:
        if args.stdin:
            payload = json.load(sys.stdin)
        elif args.path:
            with open(args.path, encoding="utf-8") as fh:
                payload = json.load(fh)
        else:
            parser.error("provide a JSON path or --stdin")
        if not isinstance(payload, dict) or not isinstance(
            payload.get("use_cases"), list
        ):
            raise ValueError('JSON must be an object with a "use_cases" array')
        result = rank(payload["use_cases"])
    except (OSError, ValueError) as exc:
        sys.stderr.write(f"priority_score: {exc}\n")
        return 1

    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
