# Brief template

One durable file per use case: `<slug>.md` in the team bundle. Update in place;
append history. Reuse an existing brief when the title is clearly the same work.
Bands, blockers, asks, and scorer use: [scoring.md](scoring.md).

Drop optional blocks the evidence does not support. This brief seeds a later
intake or PRD. It is not one.

```markdown
---
type: UseCase
title: <display name>
description: <one line>
project: <optional slug>
category: external | internal | unconfirmed
status: scored | needs-discovery
priority: P0 | P1 | P2 | P3 | none
overall: <number or null>
bv: <number or null>
dr: <number or null>
scores: { K: <1-3|null>, P: <1-3|null>, F: <1-3|null>, S: <1-3|null> }
sources: [<capture paths, notes>]
generated:
  by: discovery/skill
  at: <ISO 8601 with offset>
---

# <Use case title>

## Purpose

[The need and the kind of solution that would meet it.]

## Outcomes

Checkable at go-live: *<group> can <do what>, <how well or by when>*.

1. …

## Stakeholders

Rows from the capture roster that apply to this use case.

| Name | Email | Title | Role |
|---|---|---|---|
| | | | sponsor \| system owner \| contributor |

## Background

- **Problem:** [who is affected, how often, what happens if nothing changes]
- **Current state:** [who does it today, the steps, where it breaks]
- **Alternatives:** [tool considered → gap that rules it out, or "none considered"]

## Priority

| K | P | F | S | BV | DR | Overall | Priority |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

- **Weakest F area:** tech | data | governance | delivery | n/a
- **Blockers:** [blocker → dimension it lowers, or "none heard"]
- **Timing:** [deadline / dependency / window, or drop]
- **Reuse:** [who else could adopt it, or drop]
- **Judgment check:** [one line if the room disagrees with the score, or drop]

### Gaps

| Dim | Band | Missing | Ask |
|---|---|---|---|
| K | | | |
| P | | | |
| F | | | |
| S | | | |

**Top missing:** [one clause, or "none"]

**Asks:**
1. [K|P|F|S] …

## Delivery notes

[Optional; only when heard. Names, not designs.]

- **Workflow:** …
- **Systems / integrations:** …
- **Data sensitivity:** public | internal | confidential | personal | unknown
- **Minimum demo path:** sample/static OK? yes/no/unknown; live integration required? yes/no/unknown
- **Good enough:** [their bar and the miss they won't accept]

## Intake gaps

[Fields a human still needs before intake or PRD, or "none".]

## History

| Date | Change | Source |
|---|---|---|
| <YYYY-MM-DD> | created · K 1→2 · none→P1 | <path> |
```
