---
title: context
description: Skill and practice for maintaining CONTEXT.md and the knowledge OKF bundle.
type: concept
tags: [glossary, okf, context]
---

# context

**context** (the skill) maintains domain language and the OKF bundle.

## Owns

- [`CONTEXT.md`](../CONTEXT.md) — glossary only
- [`knowledge/`](index.md) — concept files and index

## Does not own

- [`AGENTS.md`](../AGENTS.md) — that belongs to **upkeep**

## Discipline

- When a term resolves, update the glossary immediately.
- Prefer precise canonical terms; list aliases under `_Avoid_`.
- No implementation detail in the glossary — link to ADRs or skills instead.
- Keep OKF concepts linked from `knowledge/index.md` with short descriptions.

## When

Run after [`implement`](../skills/implement/SKILL.md) and [`code-review`](../skills/code-review/SKILL.md), and whenever domain terms change.

## Related

- Skill: [`skills/context`](../skills/context/SKILL.md)
