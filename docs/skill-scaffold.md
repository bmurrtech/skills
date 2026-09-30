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
│   ├── diagrams/           # visual-explainer HTML (+ optional .md companions)
│   ├── adr-optics/         # to-adr at-a-glance catalog HTML
│   └── ideas/              # idea brain dumps (on demand; promote via roadmap)
├── AGENTS.md               # agent ops manual
├── CLAUDE.md               # body is exactly: AGENTS.md
├── CONTEXT.md              # glossary SoT (OKF root)
├── knowledge/
│   └── index.md            # OKF catalog stub → CONTEXT + concepts
└── docs/
    ├── adr/
    │   └── index.md        # empty ADR catalog (tracked decisions home)
    └── prd/                # to-prd home; ignore (A) or track (B) per setup
```

Skill folders land wherever your agent host installs them (often
`.agents/skills/` or similar) via **`npx skills`**, not via this setup skill.
Optional docx toolchain if you opt in during setup. PRD track vs ignore:
setup **Commit PRDs?** ([ADR 0013](adr/0013-ADR-prd-tracking-choice.md)).

## Artifacts (what)

| Path | What setup does |
|------|-----------------|
| `.gitignore` | Appends missing ignore lines for `/pm/`, agent dirs, `.scratch/`, etc. **`/docs/prd/`** only when PRD choice is **A** (default). Prefers append over rewrite. |
| `.scratch/` | Creates on disk (ignored). Exploratory dumps. Default handoffs stay in OS temp; **keep** → `.scratch/handoffs/` (created on demand by **`handoff`**). Ideas → `.scratch/ideas/` (created on demand by **`idea`**). |
| `.scratch/diagrams/` | Creates on disk. **visual-explainer** HTML (+ optional `.md` companions). |
| `.scratch/adr-optics/` | Creates on disk. **`to-adr`** at-a-glance catalog (`adr-at-a-glance.html`). |
| `AGENTS.md` | Lean ops manual stub (commands, boundaries, Test index stub). PRD bullets match setup A/B. |
| `CLAUDE.md` | Body exactly `AGENTS.md` (optional trailing newline). |
| `CONTEXT.md` | Root glossary stub (OKF). PRD locality matches A/B when stub/edit applies. |
| `knowledge/index.md` | Minimal OKF catalog pointing at `CONTEXT.md`. |
| `docs/adr/index.md` | Empty tracked ADR catalog table. |
| `docs/prd/` | Policy via setup **Commit PRDs?** — **A** ignore (default) / **B** track ([ADR 0013](adr/0013-ADR-prd-tracking-choice.md)). Files authored later with **`to-prd`**. |
| Optional docx | If you opt in: ensure **`docx`** skill path / toolchain. Default **no**. |

## Tracked vs local (after scaffold)

| Commit to the remote | Keep local (ignored) |
|----------------------|----------------------|
| `AGENTS.md`, `CLAUDE.md` | `.scratch/` |
| `CONTEXT.md`, `knowledge/**` (your glossary) | `pm/`, `.agents/`, `.claude/`, `.cursor/` |
| `docs/adr/**` | `.env`, secrets |
| Project source as usual | |
| `docs/prd/**` when setup **B** | `docs/prd/**` when setup **A** (default) |

`docs/prd/` is never both: setup chooses **A** or **B** ([ADR 0013](adr/0013-ADR-prd-tracking-choice.md)).


## Related

- [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md) — install → shape → ship
- [how-to-adr.md](how-to-adr.md) — ADR catalog under `.scratch/adr-optics/`
- [knowledge/skill-scaffold.md](../knowledge/skill-scaffold.md) — why this tree
- [knowledge/prd.md](../knowledge/prd.md) — why PRDs stay local
- Skill: [`setup-bmurrtech-skills`](../skills/setup-bmurrtech-skills/SKILL.md)
