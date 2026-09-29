---
title: Roadmap
description: Unordered durable idea ledger under docs/ROADMAP.md with promote vs publish commitment levels.
type: concept
tags: [roadmap, ideas, scratch, fizzy]
---

# Roadmap

`docs/ROADMAP.md` is the library’s **durable idea ledger**. Inclusion means an
idea is worth retaining — not that it is prioritized, scheduled, or ready to
implement. Order does not imply priority; no dates or sprint assignments.
Public conventions are reader-facing only; author/agent process lives in the
**`roadmap`** skill and `references/promotion.md`.

## Commitment levels

1. **Thought** — `.scratch/ideas/` via **`idea`** (default when ambiguous)
2. **Durable intent** — `docs/ROADMAP.md` via **`roadmap`** promote (explicit)
3. **Status** — Done / Advanced / Superseded (+ optional shipped-in-version) on an existing entry
4. **Tracked work** — GitHub Issues or Fizzy cards via **`roadmap`** publish
   (separate explicit intent; never inferred)

## Related skills

- **`idea`** — preserve-first scratch capture
- **`roadmap`** — ensure header, promote (classification), status, publish stubs
- **`commit`** — may invoke status on ledger impact / release context

Deterministic helpers: `skills/roadmap/scripts/ensure_header.py`,
`append_entry.py`, `mark_promoted.py`.

## Related

- [docs/ROADMAP.md](../docs/ROADMAP.md)
- Skill: [`roadmap`](../skills/roadmap/SKILL.md), [`idea`](../skills/idea/SKILL.md)
- Status grammar: [`skills/roadmap/references/status.md`](../skills/roadmap/references/status.md)
