# Prioritization meeting recap

Use right after a ranking meeting, when the user asks for a recap or
post-meeting map, or on a **reassess** of an older recap. Score with
[priority-formula.md](priority-formula.md) via `scripts/priority_score.py`.
Order by P-level, then N descending. No High/Medium labels and no tiers.

Keep each table cell to one clause. Evidence = what was said or measured.
Sentiment records the room (including disagreement and who must still confirm —
role, not name). Stakeholder column stays blank.

Fold overlaps into the parent use case before scoring. Gated items list under
status, not P-level. Potential KPIs only when evidence supports them.

On a rerun: keep the original tables; add **Reassessment** at the bottom.

````markdown
# Prioritization recap — [team or program] — [meeting date]

> Stakeholder-sentiment map scored with the discovery priority formula. Ranks are evidence-weighted, not final commitments. Scores marked L confidence need the follow-up listed for them.

## Ranked use cases

| # | P | N | Use case | Category | Sentiment / consensus | Rationale / evidence | Next action | Stakeholder |
|---|---|---|---|---|---|---|---|---|
| 1 | P1 | [N] | [title] | [external / internal] | [picked first / strong / mixed / cool — who agreed, who must still confirm] | [what was said or measured, one clause] | [quantify / validate access / define good-enough / prototype / pilot] | |
| 2 | P1 | [N] | [title] | [category] | [sentiment] | [evidence] | [next] | |
| 3 | P2 | [N] | [title] | [category] | [sentiment] | [evidence] — **resolve:** [the dependency] | [next] | |

## Gated

| Use case | Status | Why | What would reopen it | Stakeholder |
|---|---|---|---|---|
| [title] | [Blocked / Deferred / Needs discovery] | [the gate, one clause] | [the change or evidence] | |

[Drop the section if nothing is gated.]

## Folded into another use case

- [absorbed item] → [parent use case] — [why it is the same work]

[Drop if none.]

## Categories

- **External** (served outside the sponsoring team): [#s, or "none surfaced"]
- **Internal** (sponsoring team's productivity or business process): [#s]

## Score sheet

| # | Use case | K | P | V | F | S | Confidence | Weakest feasibility area |
|---|---|---|---|---|---|---|---|---|
| 1 | [title] | [1–5] | [1–5] | [K+P] | [1–5] | [1–5] | [H / M / L, and which score is L] | [tech / data / governance / delivery] |

## Potential KPIs

| # | Use case | KPI it could move | Signal heard | What would size it |
|---|---|---|---|---|
| 1 | [title] | [hours saved / cycle time / throughput / quality / capacity redirected / hard savings / cost avoidance / reuse / active users / automation success rate] | [quote or paraphrase] | [volume × minutes, error rate, users, spend line] |

## Map

```text
                    FEASIBILITY
               low                 high
            +-------------------+-------------------+
 high value |  P2               |  P1               |
            |  [#] [title]      |  [#] [title]      |
            +-------------------+-------------------+
 low value  |  P4               |  P3               |
            |  [#] [title]      |  [#] [title]      |
            +-------------------+-------------------+
 Gated: [titles]
```

## Judgment check

- [Where the formula and the room disagree, one line each. Drop if they agree.]

## How the room got there

- **Frame that settled it:** [the re-ask that produced consensus]
- **Concerns answered:** [concern — response, one line each]
- **Still to confirm:** [decision and the role who owns it]

## Carry into the next meeting

### [#1 title]

Establish:
- [the single question that closes the biggest evidence gap]
- [the good-enough or constraint question, if F is still L]
- [drop extra lines; three is plenty]

## Decision principle

Meeting sentiment decides where discovery effort goes next. It does not declare
a solution. Final priority connects pain → scale → measurable value →
feasibility → risk and governance → ownership → adoption → production outcome.

## Reassessment — [date]

[Add only on a rerun. One block per rerun, newest last. Never edit the tables above.]

| # (was) | # (now) | Use case | P (was → now) | N (was → now) | Dimension moved | Evidence | Source |
|---|---|---|---|---|---|---|---|
| [3] | [5] | [title] | [P1 → P2] | [88 → 70] | [F 4 → 2] | [what was learned] | [session, test, delivery result] |

- **New order:** [#1 …, #2 …, #3 …]
- **Decision to file:** [if a constraint or bar changed, title it so use cases can link it]
````

## KPI hint table

| Signal | Possible KPI |
|--------|----------------|
| Repetitive, time-consuming | Hours saved |
| Too slow | Cycle time |
| High volume | Throughput |
| Many people affected | Capacity redirected, adoption |
| Errors, rework | Quality |
| Spend drops | Hard savings |
| Future spend avoided | Cost avoidance |
| Several teams can reuse it | Enterprise reuse |
| People keep using it | Active / repeat users |
| The automation holds up | Successful automation rate |
| Unsafe or not viable | Pause / defer |
