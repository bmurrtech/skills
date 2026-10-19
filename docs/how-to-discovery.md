# How to use `discovery`

Turn stakeholder meetings, transcripts, or notes into a short list of use
cases worth building. Built for **solution creators** doing business analysis
in any domain — not a department-specific playbook.

Install skills with [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md).
This page covers cycles, the team OKF bundle, and the priority formula.

## When to use it

Use **`/discovery`** when you need to:

- Find pains in an initial conversation (not design a solution yet)
- Map pains to rough use cases
- Rank what to do first with the room
- Capture good-enough requirements for a POC or MVP
- Produce a scored recap, or re-score when evidence changed

Do **not** use it to write a PRD, ADR, ticket, or roadmap entry. Point at
**`create-prd`**, **`create-adr`**, or **`roadmap`** after the discovery record
exists.

## Flow

```text
materials / "new" / team cue
            |
            v
     +-------------+
     | /discovery  |  infer cycle from words + bundle
     +------+------+
            |
    +-------+-------+--------+----------+----------+
    v       v       v        v          v          v
  pain    map   prioritize  reqs      recap    reassess
    |       |       |        |          |          |
    +-------+-------+--------+----------+----------+
                        |
                        v
           docs/discovery/<team>/   OKF bundle
           (index.md + optional catalog.json)
```

## Quick start

1. Point the agent at notes, a transcript, or say you are in a live meeting.
2. Invoke `/discovery` and name the cycle if you know it (`new`, `prioritize`,
   `recap`, `rerank`, …).
3. If this is a **new** team and you did not name one, answer the one ask for
   a team/client/company label.
4. Review the written files under `docs/discovery/<team>/`.
5. Leave **Stakeholder:** blank for a human to fill.

### Example prompts

- ` /discovery new — notes at path/to/kickoff.md for client Acme `
- ` /discovery prioritize using docs/discovery/acme/ and today's transcript `
- ` /discovery recap the ranking from yesterday `
- ` /discovery re-score status-self-serve — feasibility spike failed `

## Cycles

| Cycle | Trigger cues | What you get |
|-------|--------------|--------------|
| Initial (pain) | `new`, initial, pain, kickoff | Three questions; pain list; no solution design |
| Map | map the pains, use cases from this meeting | Short read-back map |
| Prioritize | follow up, prioritize, which first | Category check + re-asked priority frames |
| Requirements | requirements, good enough, POC, MVP | Seven short asks for winners only |
| Recap | recap, score, rank them | Scored table (P-level then N) |
| Reassess | rerank, things changed, didn't deliver | Old vs new scores; history kept |

On prioritize, the skill re-asks priority in different words on purpose until
the room converges. Record the frame that settled it.

## Bundle layout (OKF v0.2)

One OKF bundle **per team**. Project is an optional field, not a nested bundle.

```text
docs/discovery/
  index.md                      # lists teams only
  <team>/                       # bundle root
    index.md                    # okf_version: "0.2"
    catalog.json                # rebuildable cache (optional)
    <slug>.md                   # UseCase or Decision
    YYYY-MM-DD-<slug>.md        # Session or Recap
```

```text
Purpose: what is inside one team bundle

+===========================+
| docs/discovery/<team>/    |
|  index.md  (okf_version)  |
|  catalog.json [Optional]  |
|                           |
|  status-self-serve.md ----+--> type: UseCase (stable)
|  rank-first-slice.md -----+--> type: Decision
|  2026-10-09-pain.md ------+--> type: Session
|  2026-10-09-recap.md -----+--> type: Recap
+===========================+
```

Rules that keep the bundle compatible with OKF:

- Every concept file has YAML frontmatter with a `type`.
- Only the team root `index.md` may carry `okf_version`.
- Links use bundle-relative paths like `/status-self-serve.md`.
- `catalog.json` is a cache — regenerate it; do not treat it as source of truth.
- Do not commit raw transcripts into the bundle; cite a local path instead.

## Priority formula

The model assigns evidence bands. A small script applies the math so ranking
stays reproducible.

```text
Purpose: judgment vs mechanics

  evidence / transcript
           |
           v
     LLM: bands K,P,F,S + gates
           |
           v
  priority_score.py  -->  P-level + N + order
           |
           v
     LLM: write recap, name judgment gaps
```

### Gates (before scoring)

| Status | Meaning |
|--------|---------|
| Blocked | No path forward |
| Deferred | Wait for a named reason |
| Needs discovery | Not enough evidence to score |

### Bands (1–5)

| Code | Meaning |
|------|---------|
| **K** | KPI benefit (measurable change) |
| **P** | Pain reduction |
| **F** | Feasibility (weakest of tech / data / governance / delivery) |
| **S** | Sentiment (orders inside a P-level only) |

Unknown → score **2** with low confidence. Do not guess a 4.

### Quadrant → P-level

- **V = K + P**. High when V ≥ 7. High feasibility when F ≥ 4.

```text
                    FEASIBILITY
               low (F ≤ 3)        high (F ≥ 4)
            +------------------+------------------+
 high       |  P2 Resolve      |  P1 Do first     |
 (V ≥ 7)    |                  |                  |
            +------------------+------------------+
 low        |  P4 Defer        |  P3 Quick win    |
 (V ≤ 6)    |                  |                  |
            +------------------+------------------+
```

### N-score (within a P-level only)

```text
N = 5K + 5P + 6F + 4S     (20–100)
```

Value 40 · feasibility 30 · sentiment 20. Never compare N across P-levels.
Near-tie when N differs by 5 or less — break on confidence, then S.

### Run the script

From the skills library checkout:

```bash
python3 skills/discovery/scripts/priority_score.py --stdin <<'EOF'
{
  "candidates": [
    {"id": "status-self-serve", "K": 4, "P": 5, "F": 4, "S": 5, "confidence": "H"},
    {"id": "internal-compare", "K": 5, "P": 5, "F": 2, "S": 4, "confidence": "M", "gate": null}
  ]
}
EOF
```

Or pass a JSON file path as the only argument. Gated example:
`{"id": "x", "gate": "deferred"}`.

### Reassess

When feasibility, value, sentiment, or a gate changes: re-score only the
touched dimensions, keep old P/N visible, and append a Reassessment section.
Do not rewrite the original recap tables in place.

## Verify

- Team folder exists under `docs/discovery/<team>/` with `index.md`.
- Use cases and decisions use stable slugs; sessions/recaps use `YYYY-MM-DD-`.
- Stakeholder lines are blank.
- Recap order matches script output (P-level, then N).
- Optional: `python3 -m unittest tests.test_discovery_priority_score -v`
  (library maintainers).

## Related

- Skill: [`skills/discovery`](../skills/discovery/SKILL.md)
- Formula detail: [`references/priority-formula.md`](../skills/discovery/references/priority-formula.md)
- Bundle rules: [`references/okf-discovery.md`](../skills/discovery/references/okf-discovery.md)
- Glossary: [discovery](../knowledge/discovery.md) · [Skill scripts vs LLM](../knowledge/skill-scripts.md)
