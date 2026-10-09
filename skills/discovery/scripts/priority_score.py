#!/usr/bin/env python3
"""Deterministic discovery priority: V, P-level, N, rank from K/P/F/S bands.

LLM assigns bands and gates; this script applies the formula only.
See skills/discovery/references/priority-formula.md.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

CONFIDENCE_RANK = {"H": 3, "M": 2, "L": 1}
GATE_STATUSES = frozenset({"blocked", "deferred", "needs-discovery"})
P_ORDER = {"P1": 0, "P2": 1, "P3": 2, "P4": 3}


def validate_band(name: str, value: Any) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1 or value > 5:
        raise ValueError(f"{name} must be an integer 1–5, got {value!r}")
    return value


def score_one(raw: dict[str, Any]) -> dict[str, Any]:
    if "id" not in raw or not str(raw["id"]).strip():
        raise ValueError("each candidate needs a non-empty id")
    cid = str(raw["id"]).strip()
    gate = raw.get("gate")
    if gate is not None:
        gate_norm = str(gate).strip().lower().replace(" ", "-")
        if gate_norm not in GATE_STATUSES:
            raise ValueError(
                f"gate must be one of {sorted(GATE_STATUSES)} or null, got {gate!r}"
            )
        conf = str(raw.get("confidence", "L")).upper()
        if conf not in CONFIDENCE_RANK:
            raise ValueError(f"confidence must be H, M, or L, got {conf!r}")
        return {
            "id": cid,
            "status": gate_norm,
            "p_level": None,
            "V": None,
            "N": None,
            "K": raw.get("K"),
            "P": raw.get("P"),
            "F": raw.get("F"),
            "S": raw.get("S"),
            "confidence": conf,
        }

    k = validate_band("K", raw["K"])
    p = validate_band("P", raw["P"])
    f = validate_band("F", raw["F"])
    s = validate_band("S", raw["S"])
    conf = str(raw.get("confidence", "L")).upper()
    if conf not in CONFIDENCE_RANK:
        raise ValueError(f"confidence must be H, M, or L, got {conf!r}")

    v = k + p
    p_level = (
        "P1"
        if v >= 7 and f >= 4
        else "P2"
        if v >= 7 and f <= 3
        else "P3"
        if v <= 6 and f >= 4
        else "P4"
    )
    n = 5 * k + 5 * p + 6 * f + 4 * s
    return {
        "id": cid,
        "status": "scored",
        "p_level": p_level,
        "V": v,
        "N": n,
        "K": k,
        "P": p,
        "F": f,
        "S": s,
        "confidence": conf,
    }


def _sort_key(item: dict[str, Any]) -> tuple:
    return (
        P_ORDER[item["p_level"]],
        -item["N"],
        -CONFIDENCE_RANK[item["confidence"]],
        -item["S"],
        item["id"],
    )


def rank(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    scored: list[dict[str, Any]] = []
    gated: list[dict[str, Any]] = []
    for raw in candidates:
        row = score_one(raw)
        if row["status"] == "scored":
            scored.append(row)
        else:
            gated.append(row)

    scored.sort(key=_sort_key)

    ranked: list[dict[str, Any]] = []
    for i, item in enumerate(scored):
        near: list[str] = []
        for j, other in enumerate(scored):
            if i == j or item["p_level"] != other["p_level"]:
                continue
            if abs(item["N"] - other["N"]) <= 5:
                near.append(other["id"])
        out = dict(item)
        out["rank"] = i + 1
        out["near_tie_with"] = near
        ranked.append(out)

    return {"ranked": ranked, "gated": gated}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Score discovery candidates (K/P/F/S → P-level + N + rank)."
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="read JSON from stdin: {\"candidates\":[...]}",
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="JSON file with {\"candidates\":[...]}",
    )
    args = parser.parse_args(argv)

    if args.stdin:
        payload = json.load(sys.stdin)
    elif args.path:
        with open(args.path, encoding="utf-8") as fh:
            payload = json.load(fh)
    else:
        parser.error("provide a JSON path or --stdin")

    if not isinstance(payload, dict) or "candidates" not in payload:
        raise SystemExit('JSON must be an object with a "candidates" array')
    if not isinstance(payload["candidates"], list):
        raise SystemExit('"candidates" must be an array')

    result = rank(payload["candidates"])
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
