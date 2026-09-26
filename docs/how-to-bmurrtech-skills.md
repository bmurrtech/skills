# How to use bmurrtech skills

Install once, then pick an entry that matches what you already have. Skills are
agent procedures — invoke them by name in your coding agent after `npx skills`
install.

Dashed edges in the diagrams are optional. Skill names match folders under
[`skills/`](../skills/).

## Install (once per machine or repo)

```bash
npx skills@latest add bmurrtech/skills
```

Useful variants:

```bash
npx skills@latest add bmurrtech/skills --list
npx skills@latest add bmurrtech/skills --skill grill-me
npx skills@latest add bmurrtech/skills --skill docx
```

This clones the GitHub source and installs skill folders into your agent skill
paths. It does **not** scaffold `AGENTS.md` / glossary / ADR home — that is
**`setup-bmurrtech-skills`**. Tree of what setup creates:
[skill-scaffold.md](skill-scaffold.md). Whys live in
[knowledge/skill-scaffold.md](../knowledge/skill-scaffold.md).

Release tarballs (`skills/` + `LICENSE` only) are for future adapters; see
[ADR 0005](adr/0005-ADR-skills-release-artifact.md) and
[ADR 0006](adr/0006-ADR-npx-skills-install-only.md).

## Main flow

Spine from install through ship. Three shape entries; take one.

```text
+=================================+
| once                            |
| npx skills@latest add           |
|   bmurrtech/skills              |
|                                 |
| setup-bmurrtech-skills [opt]    |
|   .scratch/ (+ diagrams,          |
|   adr-optics), AGENTS, CLAUDE,    |
|   CONTEXT, knowledge/, docs/adr   |
|   docs/prd ignore; optional docx  |
+================+================+
                 |
                 v
+================+=======================================+
| shape: one entry                                       |
|                                                        |
| unclear design / open frontier ----------------------+ |
|   grill-me                                           | |
|   |                                                  | |
|   + - - [lost?] - - > wait-what                      | |
|   + - - [session muddy] - - > handoff                | |
|                                                      | |
| written target exists --------------------------------+ |
|   PRD / tickets / paste / handoff doc                | |
|                                                      | |
| greenfield conventions only --------------------------+ |
|   (scaffold done; no feature yet)                    | |
|            |                                         | |
|            +-----------------------------------------+ |
+================+=======================================+
                 |
                 | [need durable decision?]
                 |      |
                 |      +--> to-adr  (docs/adr/)
                 | [need local product spec?]
                 |      |
                 |      +--> to-prd  (docs/prd/, gitignored)
                 |           cite ADRs; ascii for structure
                 v
+=================================+
| ship                            |
| implement                       |
|   | prefer tdd at agreed seams  |
|   | target-repo checks          |
|   v                             |
| code-review                     |
|   | Standards || Spec           |
|   | severity + ship call        |
|   v                             |
| upkeep then context [if present]|
|   AGENTS / CHANGELOG / OKF      |
+=================================+
```

### Same idea later (edit loop)

```text
+------------------+
| grill-me / edit  |
| to-prd / to-adr  |
+--------+---------+
         |
         v
+------------------+
| implement        |
+--------+---------+
         |
         v
+------------------+
| code-review      |
+--------+---------+
         |
         v
+------------------+
| upkeep → context |
+------------------+
```

### Lost mid-explanation

```text
+-----------+
| wait-what |
+-----+-----+
      |
      | re-pitch in STE
      | (glossary if present)
      v
+-----------+
| continue  |
| prior skill
+-----------+
```

### Session switch

```text
+---------+
| handoff |
+----+----+
     |
     | OS temp:
     | bmurrtech-skills-handoff-*.md
     v
+------------------+
| fresh agent      |
| resume from file |
+------------------+
```

## Branch map (when to reach for what)

| Situation | Skill(s) |
|-----------|----------|
| Skills not installed | `npx skills@latest add bmurrtech/skills` |
| Repo lacks AGENTS / CONTEXT / ADR / `.scratch` conventions | **`setup-bmurrtech-skills`** ([tree](skill-scaffold.md)) |
| Design ambiguous; need shared understanding | **`grill-me`** |
| Need a local PRD | **`to-prd`** (see [Local PRDs](#local-prds-docsprd) below) |
| Costly-to-reverse decision | **`to-adr`** ([how-to](how-to-adr.md)) |
| Structure clearer as a diagram | **`ascii`** (terminal) or **`visual-explainer`** (HTML under `.scratch/diagrams/`) |
| Build from a clear acceptance target | **`implement`** (pulls **`tdd`**, then **`code-review`**) |
| Review only (branch / PR / local diff) | **`code-review`** |
| Red-green at agreed seams | **`tdd`** |
| Author or tighten a skill / agent instructions | **`writing-for-agents`** |
| Word `.docx` edit path | **`docx`** (+ ensure scripts) |
| HTML diagrams / slides / visual reviews | **`visual-explainer`** ([how-to](how-to-visual-explainer.md)) |
| Explanation did not land | **`wait-what`** |
| Compact for a fresh agent | **`handoff`** |
| Ops manual / Unreleased changelog drift | **`upkeep`** |
| Glossary / OKF drift | **`context`** |

## Local PRDs (`docs/prd/`)

Human how-to (layout + flows): [how-to-bmurrtech-skills.md — Local PRDs](how-to-bmurrtech-skills.md#local-prds-docsprd).
Why → [knowledge/prd.md](../knowledge/prd.md). Thin library pointer also at [about-prd.md](about-prd.md) (ADR 0007).

```text
+------------------+     +------------------+
| Tracked          |     | Local (ignored)  |
| docs/adr/        |     | docs/prd/        |
| CONTEXT.md       |     | docs/prd/index.md|
| knowledge/       |     | PRD bodies       |
+------------------+     +------------------+
         ^                        |
         | cite                   | author with to-prd
         +------------------------+
```

- Path: `docs/prd/NNNN-PRD-<slug>.md` (four-digit sequence, no project-key prefix)
- Each file is an OKF concept (YAML frontmatter + Markdown body)
- Local catalog: `docs/prd/index.md` (also gitignored)
- Author with **`to-prd`**; cite ADRs under tracked `docs/adr/` via **`to-adr`**

## Skill clusters

### Bootstrap

- **`setup-bmurrtech-skills`** — idempotent scaffold; never silent overwrite
- **`docx`** — optional; asked during setup or install with `--skill docx`

### Shape and record

- **`grill-me`** — design-tree interview; updates glossary/OKF when present
- **`to-prd`** — local OKF PRDs under `docs/prd/` (ignored)
- **`to-adr`** — ADRs under tracked `docs/adr/` ([how-to](how-to-adr.md))
- **`ascii`** — plain-text structure diagrams
- **`visual-explainer`** — intent-routed HTML under `.scratch/diagrams/` ([how-to](how-to-visual-explainer.md))
- **`writing-for-agents`** — levers for skills and repeatable agent instructions

### Ship

- **`tdd`** — seams first; OKF test-maps + AGENTS Test index when conventions exist
- **`implement`** — TDD → target checks → code-review; soft-gates upkeep/context
- **`code-review`** — Standards ‖ Spec; severity; APPROVE / REQUEST CHANGES / COMMENT

### Session hygiene

- **`upkeep`** — `AGENTS.md`, `CLAUDE.md` pointer, `CHANGELOG.md` Unreleased
- **`context`** — `CONTEXT.md` + `knowledge/`
- **`wait-what`** — STE re-pitch
- **`handoff`** — temp handoff outside the repo

## Library maintainers (this repo)

When changing skills in **bmurrtech/skills** itself:

1. **`writing-for-agents`** for new/edited skills
2. `python3 scripts/init_skill.py <name>` when scaffolding a new skill folder
3. `python3 scripts/quick_validate.py skills/<name>`
4. Session tests via AGENTS Test index → OKF test-maps (`**tdd**`)
5. **`code-review`** → **`upkeep`** → **`context`**
6. Package smoke: `python3 scripts/package_skills.py --version <semver> --out dist/`

Consumer repos without `CONTEXT.md` / `AGENTS.md`: portable skills (**`implement`**,
**`code-review`**, **`tdd`**, **`grill-me`**, **`wait-what`**) soft-skip
glossary/ops housekeeping.

## Related

- [README.md](../README.md) — quick start + compact map
- [skill-scaffold.md](skill-scaffold.md) — folders/files setup creates
- [how-to-adr.md](how-to-adr.md) — ADR authoring + at-a-glance
- [how-to-visual-explainer.md](how-to-visual-explainer.md) — visual-explainer prompts
- [about-license.md](about-license.md) — Apache-2.0
- [adr/index.md](adr/index.md) — decisions
- [CONTEXT.md](../CONTEXT.md) — glossary (library SoT; not shipped in release artifact)
