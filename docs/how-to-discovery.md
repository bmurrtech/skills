# How to use `discovery`

Turn stakeholder meetings, transcripts, or notes into use cases scored on the
same four dimensions and ranked P0–P3. Built for **solution creators** doing
business analysis in any domain.

Install skills with [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md).
This page covers modes, the team bundle, and the scoring model.

## When to use it

Use **`/discovery`** to:

- Prep what to listen for and ask in a stakeholder meeting
- Capture one meeting into a structured record
- Brief each use case: scores, blockers, gaps, follow-up asks
- Rank every use case in a team bundle

Do **not** use it to write a PRD, ADR, ticket, or intake document. After a use
case is ranked, point at **`create-prd`** or your intake process.

## Flow

```text
 "prep for X" / notes / transcript
             |
             v
      +--------------+
      |  /discovery  |   mode from your words + bundle state
      +------+-------+
             |
   +---------+---------+----------+
   v         v         v          v
  prep    capture    brief       rank
   |         |         |          |
   |         |   K P F S bands    |
   |         |   + scorer script  |
   +---------+----+----+----------+
                  v
       docs/discovery/<team>/   (OKF bundle)
                  |
                  v
   gaps open?  -> tagged follow-up asks -> answer -> brief again
   all scored  -> create-prd / intake
```

## Quick start

1. Run `/discovery prep for <meeting>` and take the need-to-know list into the room.
2. After the meeting: `/discovery capture notes at path/to/notes.md`.
3. `/discovery brief`: one brief per use case, scored or marked needs-discovery.
4. Answer the follow-up asks (paste them in chat), then rerun brief on that file.
5. `/discovery rank` once the use cases you care about are scored.

### Example prompts

- ` /discovery prep for the Acme billing kickoff `
- ` /discovery capture notes at notes/2026-11-20-acme.md for client Acme `
- ` /discovery brief from today's capture `
- ` /discovery brief intake-triage — sponsor confirmed, pilot data approved `
- ` /discovery rank acme `

## Modes

| Mode | You get |
|---|---|
| **prep** | Need-to-know checklist + honed questions, each tagged K/P/F/S; open gaps from existing briefs first |
| **capture** | Dated meeting record: roster, signals, metric claims, candidate use cases, registry, open questions |
| **brief** | One durable file per use case: purpose, outcomes, stakeholders, background, scores, blockers, gaps, history |
| **rank** | Dated ranking from the scorer: P0→P3, BV beside Overall, unscored listed separately |

## Scoring model

Four dimensions, each scored **1** Low · **2** Medium · **3** High from evidence,
or left **unscored** when there is no usable signal.

| Code | Dimension | Measure |
|---|---|---|
| **K** | Business impact | Business Value |
| **P** | Problem severity | Business Value |
| **F** | Delivery feasibility (weakest of tech/data/governance/delivery) | Delivery Readiness |
| **S** | Stakeholder sentiment (want **and** sponsorship for a 3) | Delivery Readiness |

```text
BV      = ((K + P) / 6) × 100
DR      = ((F + S) / 6) × 100
Overall = (BV × 0.40) + (DR × 0.60)      → K 20% · P 20% · F 30% · S 30%
```

| Priority | Overall |
|---|---|
| **P0** | ≥ 80 |
| **P1** | ≥ 65 |
| **P2** | ≥ 50 |
| **P3** | < 50 |
| **none** | any dimension unscored → status needs-discovery |

Example: K=3, P=3, F=2, S=3 → BV 100 · DR 83.3 · **Overall 90.0 · P0**.

Delivery readiness carries 60%, so a well-supported, easy use case can outrank a
high-value hard one. Rankings always show BV next to Overall so you can see this.

**Blockers** (no data access, unresolved compliance, no production owner, no
integration path, no sponsor, no committed measure) lower the dimension they
affect. They don't hide a use case. Timing and reuse are notes only; they add no points.

### Judgment vs mechanics

```text
 evidence --> agent: bands + blockers + gap asks
                 |
                 v
      priority_score.py --> BV, DR, Overall, P0–P3, order
                 |
                 v
          agent: writes brief / ranking
```

Run the scorer yourself from the library checkout:

```bash
python3 skills/discovery/scripts/priority_score.py --stdin <<'EOF'
{"use_cases":[
  {"id":"intake-triage","K":3,"P":3,"F":2,"S":3},
  {"id":"report-pack","K":2,"P":null,"F":3,"S":2}
]}
EOF
```

Or pass a JSON file path. `null` (or omitted) dimensions put the use case under
`unscored` with the missing dimensions listed.

## Bundle layout (OKF v0.2)

```text
docs/discovery/
  index.md                     # lists teams only
  <team>/                      # bundle root
    index.md                   # okf_version: "0.2"
    catalog.json               # rebuildable cache (optional)
    <slug>.md                  # UseCase brief (stable, updated in place)
    YYYY-MM-DD-<slug>.md       # Capture (one per meeting)
    YYYY-MM-DD-ranking.md      # Ranking (one per rank run)
```

- Every concept file has YAML frontmatter with a `type`.
- Only the team root `index.md` carries `okf_version`.
- Links are bundle-relative (`/intake-triage.md`).
- Transcripts are cited by path, never copied in.

**Personal data:** rosters and captures may record names, emails, titles/roles,
client business details, pain points, stakeholder sentiment, tech stack/systems,
and other client-confidential fields when the evidence names them.
**`setup-bmurrtech-skills`** default-ignores `docs/discovery/` (**Commit discovery
records?** **A**). Override with setup **B** only on an explicit choice — keep
that repo **private** (never public). Details:
[how-to-bmurrtech-skills.md — Discovery records](how-to-bmurrtech-skills.md#discovery-records-docsdiscovery).

## Verify

- Team folder exists under `docs/discovery/<team>/` with `index.md`.
- Every scored brief's priority matches the scorer; unscored briefs say needs-discovery.
- Rankings list every brief once.
- Library maintainers: `python3 -m unittest tests.test_discovery_priority_score -v`.

## Related

- Skill: [`skills/discovery`](../skills/discovery/SKILL.md)
- Scoring rules: [`references/scoring.md`](../skills/discovery/references/scoring.md)
- Bundle rules: [`references/okf-discovery.md`](../skills/discovery/references/okf-discovery.md)
- Glossary: [discovery](../knowledge/discovery.md) · [Skill scripts vs LLM](../knowledge/skill-scripts.md)
