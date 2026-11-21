# Ranking template

One dated snapshot per **rank** run: `YYYY-MM-DD-ranking.md` in the team bundle.
Order and numbers come straight from the scorer output ([scoring.md](scoring.md)).
Do not reorder by hand. Earlier rankings stay as they were.

If a brief's stored priority differs from the scorer, the scorer wins: list that
brief under **Re-brief**.

```markdown
---
type: Ranking
title: <team> ranking <YYYY-MM-DD>
description: <n> scored, <m> needs-discovery
date: <YYYY-MM-DD>
generated:
  by: discovery/skill
  at: <ISO 8601 with offset>
---

# <Team> ranking: <YYYY-MM-DD>

## Ranked

| # | Priority | Overall | BV | DR | K | P | F | S | Use case | Top gap |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P0 | 90.0 | 100.0 | 83.3 | 3 | 3 | 2 | 3 | [title](/<slug>.md) | [one clause or —] |

## Needs discovery

| Use case | Missing | Top ask |
|---|---|---|
| [title](/<slug>.md) | P, S | [S] … |

## Judgment check

- [Room's pick vs ranking, one line each. Drop if they agree.]

## Re-brief

- [Brief whose stored priority is stale. Drop if none.]

## Changed since last ranking

- [title]: P2 → P1 (F 1→2, <source>). Drop on the first ranking.
```
