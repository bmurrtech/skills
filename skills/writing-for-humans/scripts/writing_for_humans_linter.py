#!/usr/bin/env python3
"""Deterministic writing metrics for writing-for-humans (stdlib only).

Measures and reports. Does not rewrite. The LLM judges material vs cosmetic
and may spend at most the reported revision_budget.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

# Length thresholds — SoT for soft/hard signals (refs point here).
SOFT_LIMIT = 20
HARD_LIMIT = 30

FILLER_CONNECTORS = (
    "in order to",
    "due to the fact that",
    "at this point in time",
    "in the event that",
    "with regard to",
    "with respect to",
    "for the purpose of",
    "in the process of",
    "it is important to note that",
    "it is worth noting that",
)

INDIRECT_PATTERNS = (
    "should be performed",
    "is to be",
    "are to be",
    "needs to be",
    "has to be",
    "have to be",
    "must be performed",
    "will be performed",
)

# Crude passive-ish signal: be-form + past participle ending. Heuristic only.
PASSIVE_RE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+[A-Za-z]+(?:ed|en)\b",
    re.IGNORECASE,
)

FUNCTION_WORDS = frozenset(
    """
    a an the and or but if then else when while as at by for from in into of
    on onto to with without within over under about after before between
    during against among through until unless not no nor so yet than that
    this these those it its they them their we our you your he she his her
    can could may might must shall should will would do does did done
    is are was were be been being have has had
    """.split()
)

CODE_FENCE_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
URL_RE = re.compile(r"https?://[^\s<>\")\]]+|www\.[^\s<>\")\]]+", re.IGNORECASE)
PATH_RE = re.compile(r"(?:/?[\w.-]+)(?:/[\w.-]+)+")
SNAKE_RE = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b")
CAMEL_RE = re.compile(r"\b[A-Z][a-z0-9]+(?:[A-Z][a-z0-9]+)+\b")
DOTTED_RE = re.compile(r"\b[A-Za-z][\w]*(?:\.[A-Za-z][\w]*)+\b")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(\[])")
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?")

_TOP_MATERIAL_CAP = 8


@dataclass(frozen=True)
class Finding:
    severity: str  # info | advisory | review | critical
    kind: str
    message: str
    sentence_index: int | None = None
    text: str | None = None


def strip_non_prose(text: str) -> str:
    """Remove fences, inline code, URLs, paths, and identifier-like tokens."""
    cleaned = CODE_FENCE_RE.sub(" ", text)
    cleaned = INLINE_CODE_RE.sub(" ", cleaned)
    cleaned = URL_RE.sub(" ", cleaned)
    cleaned = PATH_RE.sub(" ", cleaned)
    cleaned = DOTTED_RE.sub(" ", cleaned)
    cleaned = SNAKE_RE.sub(" ", cleaned)
    cleaned = CAMEL_RE.sub(" ", cleaned)
    return cleaned


def split_sentences(text: str) -> list[str]:
    cleaned = strip_non_prose(text).strip()
    if not cleaned:
        return []
    flat = re.sub(r"\s+", " ", cleaned)
    parts = SENTENCE_SPLIT_RE.split(flat)
    return [p.strip() for p in parts if p.strip()]


def word_count(sentence: str) -> int:
    return len(WORD_RE.findall(sentence))


def _phrase_pattern(phrase: str) -> re.Pattern[str]:
    parts = [re.escape(w) for w in phrase.split()]
    return re.compile(r"\b" + r"\s+".join(parts) + r"\b", re.IGNORECASE)


def find_phrases(sentence: str, phrases: tuple[str, ...]) -> list[str]:
    hits: list[str] = []
    for phrase in phrases:
        if _phrase_pattern(phrase).search(sentence):
            hits.append(phrase)
    return hits


def phrase_match_spans(sentence: str, phrases: tuple[str, ...]) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for phrase in phrases:
        for m in _phrase_pattern(phrase).finditer(sentence):
            spans.append((m.start(), m.end()))
    return spans


def _overlaps(start: int, end: int, spans: list[tuple[int, int]]) -> bool:
    for a, b in spans:
        if start < b and end > a:
            return True
    return False


def noun_cluster_candidates(sentence: str) -> list[str]:
    """Flag 4+ consecutive content-word runs (heuristic, not POS-tagged)."""
    tokens = WORD_RE.findall(sentence)
    clusters: list[str] = []
    run: list[str] = []
    for tok in tokens:
        if tok.lower() in FUNCTION_WORDS or tok.isdigit():
            if len(run) >= 4:
                clusters.append(" ".join(run))
            run = []
            continue
        run.append(tok)
    if len(run) >= 4:
        clusters.append(" ".join(run))
    return clusters


def _count_by_severity(findings: list[Finding]) -> dict[str, int]:
    counts = {"info": 0, "advisory": 0, "review": 0, "critical": 0}
    for f in findings:
        counts[f.severity] = counts.get(f.severity, 0) + 1
    return counts


def _build_agent_summary(
    findings: list[Finding], *, revision_budget: int, material: bool
) -> dict:
    material_findings = [f for f in findings if f.severity in ("review", "critical")]
    advisory_findings = [f for f in findings if f.severity == "advisory"]
    top_material = [
        {"severity": f.severity, "kind": f.kind, "message": f.message}
        for f in material_findings[:_TOP_MATERIAL_CAP]
    ]
    return {
        "recommendation": "REVISE_ONCE" if revision_budget == 1 else "STOP",
        "revision_budget": revision_budget,
        "material_review_needed": material,
        "material_kinds": sorted({f.kind for f in material_findings}),
        "advisory_count": len(advisory_findings),
        "finding_counts": _count_by_severity(findings),
        "top_material": top_material,
    }


def analyze(text: str) -> dict:
    sentences_raw = split_sentences(text)
    sentence_rows: list[dict] = []
    findings: list[Finding] = []

    for i, sentence in enumerate(sentences_raw):
        words = word_count(sentence)
        over_soft = words > SOFT_LIMIT
        over_hard = words > HARD_LIMIT
        sentence_rows.append(
            {
                "index": i,
                "text": sentence,
                "words": words,
                "over_soft_limit": over_soft,
                "over_hard_limit": over_hard,
            }
        )
        if over_hard:
            findings.append(
                Finding(
                    severity="review",
                    kind="sentence_length",
                    message=f"Sentence has {words} words (hard review threshold {HARD_LIMIT}).",
                    sentence_index=i,
                    text=sentence,
                )
            )
        elif over_soft:
            findings.append(
                Finding(
                    severity="advisory",
                    kind="sentence_length",
                    message=f"Sentence has {words} words (soft threshold {SOFT_LIMIT}).",
                    sentence_index=i,
                    text=sentence,
                )
            )

        for phrase in find_phrases(sentence, FILLER_CONNECTORS):
            findings.append(
                Finding(
                    severity="advisory",
                    kind="filler_connector",
                    message=f"Filler connector matched: {phrase!r}.",
                    sentence_index=i,
                    text=sentence,
                )
            )

        indirect_hits = find_phrases(sentence, INDIRECT_PATTERNS)
        indirect_spans = phrase_match_spans(sentence, INDIRECT_PATTERNS)
        for phrase in indirect_hits:
            findings.append(
                Finding(
                    severity="advisory",
                    kind="indirect_instruction",
                    message=f"Indirect instruction pattern matched: {phrase!r}.",
                    sentence_index=i,
                    text=sentence,
                )
            )

        for m in PASSIVE_RE.finditer(sentence):
            if _overlaps(m.start(), m.end(), indirect_spans):
                continue
            findings.append(
                Finding(
                    severity="advisory",
                    kind="passive_heuristic",
                    message=f"Passive/indirect heuristic matched: {m.group(0)!r}.",
                    sentence_index=i,
                    text=sentence,
                )
            )

        for cluster in noun_cluster_candidates(sentence):
            findings.append(
                Finding(
                    severity="advisory",
                    kind="noun_cluster",
                    message=f"Noun-cluster candidate: {cluster!r}.",
                    sentence_index=i,
                    text=sentence,
                )
            )

    word_counts = [row["words"] for row in sentence_rows]
    avg = round(sum(word_counts) / len(word_counts), 1) if word_counts else 0.0
    max_words = max(word_counts) if word_counts else 0
    over_soft_n = sum(1 for row in sentence_rows if row["over_soft_limit"])
    over_hard_n = sum(1 for row in sentence_rows if row["over_hard_limit"])

    findings.append(
        Finding(
            severity="info",
            kind="aggregate",
            message=(
                f"average_sentence_words={avg}; max={max_words}; "
                f"over_soft={over_soft_n}; over_hard={over_hard_n}"
            ),
        )
    )

    severities = {f.severity for f in findings}
    material = "critical" in severities or "review" in severities
    revision_budget = 1 if material else 0
    agent_summary = _build_agent_summary(
        findings, revision_budget=revision_budget, material=material
    )

    summary = {
        "sentence_count": len(sentence_rows),
        "average_sentence_words": avg,
        "max_sentence_words": max_words,
        "sentences_over_soft_limit": over_soft_n,
        "sentences_over_hard_limit": over_hard_n,
        "soft_limit": SOFT_LIMIT,
        "hard_limit": HARD_LIMIT,
        "finding_counts": _count_by_severity(findings),
        "material_review_needed": material,
        "revision_budget": revision_budget,
    }

    return {
        "tool": "writing_for_humans_linter",
        "version": 2,
        "summary": summary,
        "agent_summary": agent_summary,
        "sentences": sentence_rows,
        "findings": [asdict(f) for f in findings],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Measure writing metrics for writing-for-humans (no rewrite)."
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="File to lint, or '-' for stdin. Omit path and pass --text.",
    )
    parser.add_argument(
        "--text",
        default=None,
        help="Inline text to lint (alternative to path/stdin).",
    )
    args = parser.parse_args(argv)

    if args.text is not None:
        text = args.text
    elif args.path in (None, "-"):
        text = sys.stdin.read()
    else:
        text = Path(args.path).read_text(encoding="utf-8")

    report = analyze(text)
    json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
