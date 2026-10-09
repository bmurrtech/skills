# Discovery priority formula

Read on **recap** or **reassess**. LLM assigns bands and gates from evidence.
Run `scripts/priority_score.py` for V, P-level, N, and sort order.

## Step 1. Gates

Any open gate → status, not a P-level:

| Status | Meaning |
|--------|---------|
| **Blocked** | Stop with no path (no lawful access, legal no, no production owner) |
| **Deferred** | Viable later; name why it waits |
| **Needs discovery** | Not enough evidence to score Value or Feasibility |

Gates include: no business owner; no legitimate data/system access; unresolved
security/privacy/legal/records/compliance; human judgment with no review model;
no measurable outcome; no production support; no realistic integration path.
Never invent an assumption to clear a gate.

## Step 2. Score four dimensions (1–5)

Round to a whole band. Mark each score **H / M / L** confidence. Unknown →
**2** with **L**, never a guess at 4.

| Dimension | 1 | 3 | 5 |
|-----------|---|---|---|
| **KPI benefit (K)** | No measurable change named | Real measure, not sized | Sized number they gave |
| **Pain reduction (P)** | "Would be nice" | Recurring, one team | Frequent, heavy, many people/teams, or risk if it slips |
| **Feasibility (F)** | Weakest of tech/data/governance/delivery is hard | Path exists; one area unproven | Systems readable, data authorized, rules known, owner/testers named |
| **Sentiment (S)** | Not now / no appetite | Interest + recognized pain | Picked first in re-ask; someone offered time/data/testing |

Score **F** at the **weakest** of tech / data / governance / delivery — not the average.
Do not upgrade time saved into money.

## Step 3. P-level (quadrant)

- **Value (V) = K + P** (range 2–10). High when **V ≥ 7**.
- **Feasibility** high when **F ≥ 4**.

```text
                    FEASIBILITY
               low (F ≤ 3)        high (F ≥ 4)
            +------------------+------------------+
 high       |  P2              |  P1              |
 (V ≥ 7)    |  Resolve first   |  Do first        |
            +------------------+------------------+
 low        |  P4              |  P3              |
 (V ≤ 6)    |  Defer / avoid   |  Quick win       |
            +------------------+------------------+
```

Sentiment never moves the quadrant — only orders inside a P-level.

## Step 4. N-score (within P-level only)

```text
N = 5K + 5P + 6F + 4S        (range 20–100)
```

Weights: value 40, feasibility 30, sentiment 20. Never compare N across P-levels.

## Step 5. Rank

1. Sort P1 → P2 → P3 → P4; gated after under their status.
2. Within a P-level, sort by N descending.
3. **Near-tie** when N differs by ≤ 5: higher confidence, then higher S; still tied → report tied.
4. Number 1..n down the whole page.

## Step 6. Judgment check

If the formula contradicts a clear room choice, name the gap in one line and
let humans decide. Do not silently override either side.

## Reassess

Re-score only dimensions new evidence touches. Recompute V, P-level, N via the
script. Keep old P/N next to new with the reason. Append a Reassessment section;
do not rewrite the original recap tables.
