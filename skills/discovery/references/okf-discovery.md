# OKF discovery bundle

Consumer record of meetings, use cases, and decisions. OKF **v0.2** compatible.
Markdown is SoT. `catalog.json` is an optional rebuildable cache.

## Layout

```text
docs/discovery/
  index.md                 # team list only (not a mega-bundle)
  <team>/                  # ONE OKF bundle root per team
    index.md               # okf_version: "0.2" only
    catalog.json           # optional cache
    log.md                 # optional
    <slug>.md              # UseCase | Decision (stable; update in place)
    YYYY-MM-DD-<slug>.md   # Session | Recap (dated snapshot)
```

No project-level OKF root. Optional frontmatter `project: <slug>` on concepts.
No required `sessions/` / `use-cases/` / `decisions/` subdirectories.

## Conformance

- Every concept `.md`: YAML frontmatter with required `type`.
- Bundle-root `index.md`: may carry only `okf_version: "0.2"`.
- Child indexes (if any): no frontmatter.
- Links: prefer bundle-relative `/concept.md`.
- Reserved names: `index.md`, `log.md` — not concepts.
- Preserve unknown frontmatter keys when round-tripping.
- Actor for generation: `discovery/skill` under `generated.by`.

## Types

| `type` | Filename habit | Role |
|--------|----------------|------|
| `Session` | `YYYY-MM-DD-<slug>.md` | One meeting map / pain finding / prioritization notes |
| `Recap` | `YYYY-MM-DD-<slug>.md` | Scored prioritization recap (reassess appends) |
| `UseCase` | `<slug>.md` | Durable opportunity; history across meetings |
| `Decision` | `<slug>.md` | Priority call, good-enough bar, constraint, or gate |

## Use case frontmatter (current scores)

```yaml
---
type: UseCase
title: <display name>
description: <one line>
project: <optional slug>
category: external | internal | unconfirmed
team: <team slug>
status: scored | blocked | deferred | needs-discovery | delivered | retired
p_level: P1 | P2 | P3 | P4 | none
n_score: <20-100 or none>
scores: { K: <1-5>, P: <1-5>, F: <1-5>, S: <1-5> }
confidence: H | M | L
generated:
  by: discovery/skill
  at: <ISO 8601 with offset>
---
```

Body: Stakeholder blank; process, pain, scale, value, potential, KPIs,
constraints; links to binding decisions and sessions; History lines.

## Decision frontmatter

```yaml
---
type: Decision
title: <display name>
description: <one line>
kind: priority | good-enough | constraint | gate
state: active | superseded | lifted
generated:
  by: discovery/skill
  at: <ISO 8601 with offset>
---
```

## Root team index

`docs/discovery/<team>/index.md`:

```markdown
---
okf_version: "0.2"
---

# <Team> discovery

## Use cases

* [Title](/slug.md) - short description

## Sessions and recaps

* [Label](/YYYY-MM-DD-slug.md) - short description

## Decisions

* [Title](/decision-slug.md) - short description
```

## Parent listing

`docs/discovery/index.md` — bullets to team folders only. No `okf_version`
(not a merged bundle).

## catalog.json (cache)

Rebuild after writes. Suggested shape (producer extension, not OKF-required):

```json
{
  "okf_version": "0.2",
  "team": "<team>",
  "concepts": [
    {
      "id": "slug",
      "path": "slug.md",
      "type": "UseCase",
      "title": "...",
      "project": null,
      "status": "scored",
      "p_level": "P1",
      "n_score": 88
    }
  ]
}
```

## First write

1. Ensure `docs/discovery/` and parent index.
2. Create `<team>/` with root `index.md` (`okf_version` only).
3. Write concepts; update indexes + catalog.
4. Never put durable discovery records under `.scratch/`.
