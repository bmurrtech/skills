---
title: discovery
description: User-invoked discovery skill — prep/capture/brief/rank modes, team OKF bundles, KPFS scoring.
type: concept
tags: [skills, discovery, okf, business-analysis, prioritization]
---

# discovery

**discovery** helps solution creators turn stakeholder meetings, transcripts, or notes into use cases scored on one model and ranked P0–P3. A use case is ranked only once all four dimensions have evidence.

## Modes

| Mode | When | Writes |
|---|---|---|
| prep | Before or during a meeting | Chat checklist (optionally an empty capture) |
| capture | One meeting's notes | `YYYY-MM-DD-<slug>.md` (`Capture`) |
| brief | Per use case; new evidence or answers | `<slug>.md` (`UseCase`), updated in place |
| rank | Order every brief | `YYYY-MM-DD-ranking.md` (`Ranking`) |

## Bundle (OKF v0.2)

- Home: `docs/discovery/<team>/`, **one bundle root per team**
- Parent `docs/discovery/index.md` lists teams (not a mega-bundle)
- Optional `project:` on concepts; optional `catalog.json` cache; Markdown is SoT
- Rosters carry name/email/title/role from evidence only
- Track vs ignore: setup **Commit discovery records?** A ignore (default) / B track; B keeps the repo private. Library dogfoods A. Mirrors PRD A/B ([ADR 0013](../docs/adr/0013-ADR-prd-tracking-choice.md)); discovery skill does not warn on tracked writes

## Scoring (scripted)

KPFS bands 1–3 or unscored → BV/DR/Overall (40/60) → P0–P3. The LLM assigns bands, blockers, and gap asks; `scripts/priority_score.py` does the math. See the glossary entry **Discovery priority formula**.

## Does not own

PRD, ADR, tickets, intake, solution design. Point at those skills once briefs are ranked.

## Related

- Glossary: [CONTEXT.md](../CONTEXT.md)
- Scripts policy: [skill-scripts.md](skill-scripts.md)
- How-to: [`docs/how-to-discovery.md`](../docs/how-to-discovery.md)
- Skill: [`skills/discovery`](../skills/discovery/SKILL.md)
- Test map: [discovery-priority-score.md](discovery-priority-score.md)
- OKF shape reference: Google OKF v0.2 (bundle = directory; `type` required; root `index.md` may carry `okf_version`)
