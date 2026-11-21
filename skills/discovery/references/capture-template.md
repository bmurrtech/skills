# Capture template

One file per meeting: `YYYY-MM-DD-<short-slug>.md` in the team bundle. Fill from
evidence only; leave unknown cells blank; delete unused bracket lines. Cite
transcripts and notes by path. Never paste them.

Add **Narrative** only when the user supplied prose or a meeting-summary path.

The **Use-case registry** stays empty until **brief** runs; brief patches it.

```markdown
---
type: Capture
title: <meeting title>
description: <one line: why this conversation happened>
date: <YYYY-MM-DD>
sources: [<paths>]
generated:
  by: discovery/skill
  at: <ISO 8601 with offset>
---

# <Meeting title>

## Roster

| Name | Email | Title | Role |
|---|---|---|---|
| | | | sponsor \| system owner \| contributor |

Roles: **sponsor** approves go/no-go · **system owner** holds admin access to a
needed system · **contributor** subject expert or informational. Evidence only;
never invent a person or an email.

## Signals

| Signal | Heard |
|---|---|
| Pain | |
| Who feels it / how often | |
| Want and sponsorship | |
| Measures that matter | |
| Systems, data, rules, access owner | |
| Minimum demo path (sample/static OK?) | |
| Must-never-touch | |
| Blockers | |
| External or internal | |

## Narrative

[Optional. Short paragraphs on pain, sentiment, feasibility. Not a charter.]

## Metric and fiscal claims

| Label or fiscal tier | What was said | Sized? (y/n/unknown) |
|---|---|---|
| | | |

## Candidate use cases

| Working title | External / internal | Pain in one line | Measure hint | Weakest feasibility area |
|---|---|---|---|---|
| | | | | |

## Use-case registry

| Use case | Brief | Priority | Overall | Status |
|---|---|---|---|---|
| | [/<slug>.md](/<slug>.md) | P0–P3 or none | — | scored \| needs-discovery |

## Open questions

[Open gap asks from linked briefs first, tagged [K] [P] [F] [S]; then anything else.]

1. …
```
