# Scoring (KPFS)

The only home for scoring rules. Templates link here; they do not restate it.
You assign bands from evidence; `scripts/priority_score.py` does all arithmetic.

## Dimensions

| Code | Dimension | Measure | Asks |
|---|---|---|---|
| **K** | Business impact | Business Value (BV) | What measurable change could this deliver? |
| **P** | Problem severity | Business Value (BV) | How much does today's problem cost, and whom? |
| **F** | Delivery feasibility | Delivery Readiness (DR) | How realistically can a solution ship? |
| **S** | Stakeholder sentiment | Delivery Readiness (DR) | Is it wanted, and will a sponsor back it? |

## Bands

| | **1** Low | **2** Medium | **3** High |
|---|---|---|---|
| **K** | Direction only, nothing measurable | Measure named, not sized | Sized claim (hours, cycle time, errors, cost) |
| **P** | Occasional or mild | Recurring, real cost to one group | Frequent, heavy, many people, or real risk |
| **F** | Weakest area is hard | Weakest area has a named, open blocker | Systems reachable, data approved, rules known, owner named |
| **S** | Little appetite | Want **or** sponsorship, not both | Want **and** a sponsor who will sign off / give time or data |

- **null** (shown `—`) when there is no usable signal. Never `0`; never a default `2`.
- A **3** needs evidence you can cite. Doubt between two bands → the lower one plus an ask.
- **F** = the weakest of tech · data · governance · delivery. Never the average. Name the weakest area.
- **S** cannot reach 3 without sponsorship.
- Fiscal claims count toward K only with a fiscal tier (`kpi-catalog.md`). Time saved is not money.

## Blockers

A **blocker** is a generic condition that stops delivery for any client. Record each
on the brief with the dimension it lowers. Blockers lower bands; they never hide a
use case or suppress its priority.

| Blocker | Lowers |
|---|---|
| No lawful or granted access to required data or systems | F |
| Unresolved security, privacy, legal, or compliance question | F |
| No owner to run or support it in production | F |
| No realistic integration path for the minimum viable version | F |
| No sponsor or decision maker willing to approve | S |
| No measurable outcome anyone will commit to | K |

Client-specific policies (procurement windows, change boards, …) go in timing notes.

## Minimum evidence and seed asks

Hone each seed into the stakeholder's words. Tag every ask `[K]` `[P]` `[F]` `[S]`.

| Dim | Enough for a band | Seed ask when thin |
|---|---|---|
| K | Any named measure (2); a number or baseline (3) | Which number should move, and what is it today? |
| P | Who + how often + consequence | When did this last go wrong: who, how often, what happened? |
| F | Weakest area identified | What single thing stops a first demo: access, data, rules, hosting? |
| S | Want stated; sponsor named and committed | Who signs off a pilot, and have they said yes? |

## Run the scorer

Build one JSON object per use case (`null` for unscored dims). Run from the skill folder:

```bash
python3 scripts/priority_score.py --stdin <<'EOF'
{"use_cases":[{"id":"intake-triage","K":3,"P":3,"F":2,"S":3},{"id":"report-pack","K":2,"P":null,"F":3,"S":2}]}
EOF
```

Copy `bv`, `dr`, `overall`, `priority`, `status`, `missing`, and `rank` from the
output into the brief or ranking verbatim. If the script exits non-zero, report its
message and stop. Do not compute a fallback.

What the script applies:

- BV = (K+P)/6×100 · DR = (F+S)/6×100 · **Overall = 0.4·BV + 0.6·DR**
  (effective weights K 20 · P 20 · F 30 · S 30)
- **P0** ≥ 80 · **P1** ≥ 65 · **P2** ≥ 50 · **P3** < 50
- Any null → priority **none**, status **needs-discovery**, `missing` lists dims
- Order: label, then Overall desc, then S desc, then id. Unscored come after, unranked.

## Unscored use cases

Status stays **needs-discovery** until every dim has a band from new evidence.
Unclear answers do not count: ask for clarification in chat and leave the dim null.

## Gap asks

List every ask needed to clear a null dim or defend a thin **1**. Put the most
blocking first ("top missing"). Asks are questions, not drafted messages.

## Notes outside the formula

- **Timing:** deadlines, dependencies, closed windows.
- **Reuse:** another team could adopt the pattern.

Both are written down and add no points.

## Judgment check

Readiness carries 60%, so a low-value use case can outrank a high-value one.
Always show BV beside Overall. When the room's pick disagrees with the ranking,
write one line naming the gap. Override neither side.
