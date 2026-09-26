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
│   └── adr-optics/         # to-adr at-a-glance catalog HTML
├── AGENTS.md               # agent ops manual
├── CLAUDE.md               # body is exactly: AGENTS.md
├── CONTEXT.md              # glossary SoT (OKF root)
├── knowledge/
│   └── index.md            # OKF catalog stub → CONTEXT + concepts
└── docs/
    ├── adr/
    │   └── index.md        # empty ADR catalog (tracked decisions home)
    └── prd/                # usually not created as files yet; path ignored
```

Skill folders land wherever your agent host installs them (often
`.agents/skills/` or similar) via **`npx skills`**, not via this setup skill.
Optional docx toolchain if you opt in during setup.

## Artifacts (what)

| Path | What setup does |
|------|-----------------|
| `.gitignore` | Appends missing ignore lines for `/pm/`, agent dirs, `/docs/prd/`, `.scratch/`, etc. Prefers append over rewrite. |
| `.scratch/` | Creates on disk (ignored). Exploratory dumps. Not for handoffs. |
| `.scratch/diagrams/` | Creates on disk. **visual-explainer** HTML (+ optional `.md` companions). |
| `.scratch/adr-optics/` | Creates on disk. **`to-adr`** at-a-glance catalog (`adr-at-a-glance.html`). |
| `AGENTS.md` | Lean ops manual stub (commands, boundaries, Test index stub). |
| `CLAUDE.md` | Body exactly `AGENTS.md` (optional trailing newline). |
| `CONTEXT.md` | Root glossary stub (OKF). |
| `knowledge/index.md` | Minimal OKF catalog pointing at `CONTEXT.md`. |
| `docs/adr/index.md` | Empty tracked ADR catalog table. |
| `docs/prd/` | Ensures **ignore** only; PRD files authored later with **`to-prd`**. |
| Optional docx | If you opt in: ensure **`docx`** skill path / toolchain. Default **no**. |

## Tracked vs local (after scaffold)

| Commit to the remote | Keep local (ignored) |
|----------------------|----------------------|
| `AGENTS.md`, `CLAUDE.md` | `.scratch/` |
| `CONTEXT.md`, `knowledge/**` (your glossary) | `docs/prd/**` |
| `docs/adr/**` | `pm/`, `.agents/`, `.claude/`, `.cursor/` |
| Project source as usual | `.env`, secrets |

## Related

- [how-to-bmurrtech-skills.md](how-to-bmurrtech-skills.md) — install → shape → ship
- [how-to-adr.md](how-to-adr.md) — ADR catalog under `.scratch/adr-optics/`
- [knowledge/skill-scaffold.md](../knowledge/skill-scaffold.md) — why this tree
- [knowledge/prd.md](../knowledge/prd.md) — why PRDs stay local
- Skill: [`setup-bmurrtech-skills`](../skills/setup-bmurrtech-skills/SKILL.md)
