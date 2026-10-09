---
title: discovery
description: User-invoked discovery skill — cycles, team OKF bundles, and priority formula for solution creators.
type: concept
tags: [skills, discovery, okf, business-analysis]
---

# discovery

**discovery** helps solution creators turn stakeholder meetings, transcripts, or notes into a small set of use cases worth building — value first, solution later.

## Cycles

| Cycle | When | Load |
|---|---|---|
| Initial (pain) | New / no pains yet | pain-point finder |
| Map | Same meeting, pains clear | discovery map |
| Prioritize | Follow-up / rank | prioritization |
| Requirements | Winners → POC/MVP | requirements gathering |
| Recap | After ranking / on demand | prioritization recap + formula |
| Reassess | New evidence on existing artifacts | same recap rules; append delta |

Route from trigger words + bundle evidence. Prefer zero-shot: user points at materials; ask only when a high-value field is unclear.

## Bundle (OKF v0.2)

- Home: `docs/discovery/<team>/` — **one bundle root per team**
- Parent: `docs/discovery/index.md` lists teams (not a mega-bundle)
- Concepts: stable `<slug>.md` (UseCase / Decision) + `YYYY-MM-DD-<slug>.md` (Session / Recap)
- Optional `project:` on concepts; no project-level OKF
- Optional `catalog.json` rebuildable cache; Markdown is SoT
- Stakeholder name line always blank for a human

## Priority (scripted)

LLM scores bands; `scripts/priority_score.py` computes P-level + N. See glossary **Discovery priority formula**.

## Does not own

PRD, ADR, tickets, roadmap — point at those skills after the record exists.

## Related

- Glossary: [CONTEXT.md](../CONTEXT.md)
- Scripts policy: [skill-scripts.md](skill-scripts.md)
- How-to: [`docs/how-to-discovery.md`](../docs/how-to-discovery.md)
- Skill: [`skills/discovery`](../skills/discovery/SKILL.md)
- Test map: [discovery-priority-score.md](discovery-priority-score.md)
- Idea scratch (pre-ship): `.scratch/ideas/universal-discovery-skill.md`
- OKF shape reference: Google OKF v0.2 (bundle = directory; `type` required; root `index.md` may carry `okf_version`)
