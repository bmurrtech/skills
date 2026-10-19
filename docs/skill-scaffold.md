# Skill scaffold (`setup-bmurrtech-skills`)

Folders and files a **consumer repo** gets after running **`setup-bmurrtech-skills`**.
Not the layout of the `bmurrtech/skills` library itself. Does **not** install
skill folders — use `npx skills add bmurrtech/skills` for that.

Install → shape → ship flows: [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md).
**Why** each path exists: [knowledge/skill-scaffold.md](../knowledge/skill-scaffold.md).

The skill is **idempotent**: explore → present → confirm → write. Creates only
missing pieces; asks before replacing non-empty files.

## Expected tree (after confirm)

```text
.
├── .gitignore              # patched: ignore local-only paths below
├── .scratch/               # created on disk; gitignored
│   ├── visuals/            # default visual-explainer HTML (+ optional .md)
│   ├── adr-optics/         # create-adr at-a-glance HTML + fat adr-catalog.json
│   ├── doop/               # doop session sidecars (canvas URL/id + notes)
│   └── ideas/              # idea brain dumps (on demand; promote via roadmap)
├── AGENTS.md               # agent ops manual
├── CLAUDE.md               # body is exactly: AGENTS.md
├── CONTEXT.md              # glossary SoT (OKF root)
├── knowledge/
│   └── index.md            # OKF catalog stub → CONTEXT + concepts
└── docs/
    ├── adr/
    │   └── index.md        # empty ADR catalog (tracked decisions home)
    ├── visuals/            # tracked visual-explainer HTML (team/commit cues)
    └── prd/                # create-prd home; ignore (A) or track (B) per setup
```

Skill folders land wherever your agent host installs them (often
`.agents/skills/` or similar) via **`npx skills`**, not via this setup skill.
Optional docx toolchain and optional Donation CTA (FUNDING.yml + README
**Support this Repo**) if you opt in during setup. PRD track vs ignore:
setup **Commit PRDs?** ([ADR 0013](adr/0013-ADR-prd-tracking-choice.md)).

## Artifacts (what)

| Path | What setup does |
|------|-----------------|
| `.gitignore` | Appends missing ignore lines for `/pm/`, agent dirs, `.scratch/`, etc. **`/docs/prd/`** only when PRD choice is **A** (default). Prefers append over rewrite. |
| `.scratch/` | Creates on disk (ignored). Exploratory dumps. Default handoffs stay in OS temp; **keep** → `.scratch/handoffs/` (created on demand by **`handoff`**). Ideas → `.scratch/ideas/` (created on demand by **`idea`**). |
| `.scratch/visuals/` | Creates on disk (renames legacy `.scratch/diagrams/` → `visuals/` when safe). Default **visual-explainer** HTML (+ optional `.md` companions). |
| `.scratch/adr-optics/` | Creates on disk. **`create-adr`** glance (`adr-at-a-glance.html` + fat JSON); slim tracked catalog is `docs/adr/catalog.json`. |
| `.scratch/doop/` | Creates on disk. **`doop`** session sidecars (canvas URL/id + meeting notes). Doop DB stays in the Doop install. |
| `AGENTS.md` | Lean ops manual stub (commands, boundaries, Test index stub). PRD bullets match setup A/B. |
| `CLAUDE.md` | Body exactly `AGENTS.md` (optional trailing newline). |
| `CONTEXT.md` | Root glossary stub (OKF). PRD locality matches A/B when stub/edit applies. |
| `knowledge/index.md` | Minimal OKF catalog pointing at `CONTEXT.md`. |
| `docs/adr/index.md` | Empty tracked ADR catalog table. |
| `docs/visuals/` | Creates on disk. Tracked **visual-explainer** home for team/commit/docs cues ([ADR 0014](adr/0014-ADR-visual-explainer-homes.md)). |
| `docs/prd/` | Policy via setup **Commit PRDs?** — **A** ignore (default) / **B** track ([ADR 0013](adr/0013-ADR-prd-tracking-choice.md)). Files authored later with **`create-prd`**. |
| Optional docx | If you opt in: ensure **`docx`** skill path / toolchain. Default **no**. |
| Optional Donation CTA | If you opt in + supply URLs: `.github/FUNDING.yml`, README **Support this Repo**, CONTEXT glossary entries. Default **no**. |

## Tracked vs local (after scaffold)

| Commit to the remote | Keep local (ignored) |
|----------------------|----------------------|
| `AGENTS.md`, `CLAUDE.md` | `.scratch/` |
| `CONTEXT.md`, `knowledge/**` (your glossary) | `pm/`, `.agents/`, `.claude/`, `.cursor/` |
| `docs/adr/**`, `docs/visuals/**` | `.env`, secrets |
| `.github/FUNDING.yml` when Donation CTA opted in | |
| README **Support this Repo** when Donation CTA opted in | |
| Project source as usual | |
| `docs/prd/**` when setup **B** | `docs/prd/**` when setup **A** (default) |

`docs/prd/` is never both: setup chooses **A** or **B** ([ADR 0013](adr/0013-ADR-prd-tracking-choice.md)).


## Related

- [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md) — install → shape → ship
- [how-to-adr.md](how-to-adr.md) — ADR catalog + glance under `.scratch/adr-optics/`
- [knowledge/skill-scaffold.md](../knowledge/skill-scaffold.md) — why this tree
- [knowledge/prd.md](../knowledge/prd.md) — why PRDs stay local
- Skill: [`setup-bmurrtech-skills`](../skills/setup-bmurrtech-skills/SKILL.md)
