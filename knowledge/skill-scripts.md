---
title: Skill scripts vs LLM
description: When a skill should use a deterministic script versus the LLM — judgment, cost, compression, and error prevention.
type: concept
tags: [skills, scripts, llm, tokenomics]
---

# Skill scripts vs LLM

**Principle:** LLM for judgment. Scripts for cheap, deterministic work that would otherwise burn meaningful tokens or introduce calculation risk.

A script is justified only when its **total** cost — tool call, context, maintenance, failure modes, and output tokens — is lower than letting the LLM do the work, **or** when exactness/reproducibility matters enough to prevent arithmetic hallucination.

“Can a script do this?” is the wrong question. Almost everything can be scripted eventually. Prefer: **Would scripting this reduce total system cost or improve reliability enough to justify the complexity?**

## Prefer LLM

| Task | Why |
|---|---|
| Interpretation | Needs context and judgment |
| Classification (semantic) | Usually contextual |
| Prioritization / tradeoffs | Reasoning across variables |
| Strategy | Cross-cutting reasoning |
| Ambiguous decisions | Scripts cannot reliably resolve ambiguity |

**Judgment class (A):** What does this mean? Is it important? What should we recommend? Which option is better? What does the customer care about?

Do **not** build “smart scripts” that pretend to do semantics (sentiment from regex, “is this valuable?”, “is this requirement ambiguous?”). Those become brittle pseudo-LLMs.

## Prefer script

| Task | Why |
|---|---|
| Non-trivial calculations | Deterministic, exact |
| Counting / aggregates | No reason to spend tokens |
| Sorting/ranking numeric data | Exact and reproducible |
| Threshold / formula application | Prevents arithmetic errors |
| Schema / regex / string validation | Mechanical |
| File transformation | Often cheaper at scale |
| Repeated bulk operations | Better than repeated LLM calls |
| Compression of large inputs | Small evidence set for the LLM |

**Deterministic class (B):** count, sum, average, sort, filter, calculate, validate, parse, convert, compare, format — script when the operation is **non-trivial or repeated**.

**Hybrid class (D):** LLM assigns semantic inputs (bands, labels); script applies the formula / sorts / thresholds; LLM interprets the small result. Example: score 1–5 dimensions → script returns P-level + N + rank → LLM explains judgment gaps.

## Do not script (trivial deterministic)

If the model can do it in one cheap step (`8 + 7`, sort three scores), a tool round-trip can cost more than the work. Not every deterministic op deserves a script.

## Tests before adding a script

1. **Mistake test** — Would the LLM actually err (weighted scores, money × rate, multi-step formula)? Exactness alone can justify a tiny script.
2. **Tokenomics test** — Sum tool invocation + args + returned output + context + orchestration + maintenance + failure handling. Simple + model-known → don’t script.
3. **Compression test** — Strong win when raw bulk (hundreds of rows/responses) becomes a small JSON evidence set the model reasons over once.
4. **Output size** — Prefer small results (`n`, means, flags, ranked ids). Avoid dumping every intermediate row unless needed for audit/debug.
5. **Four characteristics** — Strong candidates are deterministic, simple, robust on ordinary edges, and compressing.

## Architecture pattern

```text
raw / semantic inputs
        ↓
   LLM (judgment: bands, meaning)
        ↓
   script (mechanics: formula, sort, validate)
        ↓
   small deterministic evidence
        ↓
   LLM (interpret, write artifacts, next ask)
```

## Related

- Glossary: [Skill](../CONTEXT.md), [Skill scripts vs LLM](../CONTEXT.md)
- Skill bundle note: [agent-skill.md](agent-skill.md)
- Ops pointer: [`skills/upkeep`](../skills/upkeep/SKILL.md) (when Code style / skill `scripts/` change)
- Example hybrid: [writing-for-humans linter](writing-for-humans-linter.md) — script measures; LLM judges
