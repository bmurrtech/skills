---
title: upkeep
description: Skill and practice for maintaining AGENTS.md and the CLAUDE.md pointer.
type: concept
tags: [agents, upkeep]
---

# upkeep

**upkeep** keeps the agent operating manual accurate.

## Owns

- [`AGENTS.md`](../AGENTS.md) — structure, commands, boundaries, verification
- [`CLAUDE.md`](../CLAUDE.md) — body must be exactly `AGENTS.md` (create if missing)

## Does not own

- [`CONTEXT.md`](../CONTEXT.md) or [`knowledge/`](index.md) — those belong to **context**

## When

Run after [`implement`](../skills/implement/SKILL.md) and [`code-review`](../skills/code-review/SKILL.md), and whenever repo layout, checks, or boundaries change.

## Related

- Skill: [`skills/upkeep`](../skills/upkeep/SKILL.md)
