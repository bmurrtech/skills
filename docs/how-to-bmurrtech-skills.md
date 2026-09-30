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
| /setup-bmurrtech-skills [opt]   |
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
|   /grill-me                                          | |
|   |                                                  | |
|   + - - [lost?] - - > /wait-what                     | |
|   + - - [session muddy] - - > /handoff               | |
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
                 |      +--> /to-adr  (docs/adr/)
                 | [need local product spec?]
                 |      |
                 |      +--> /to-prd  (docs/prd/, gitignored)
                 |           cite ADRs; /ascii for structure
                 | [not this sprint / brain dump?]
                 |      |
                 |      +--> /idea  (.scratch/ideas/)
                 |           promote later via /roadmap → docs/ROADMAP.md
                 | [session switch / fresh agent?]
                 |      |
                 |      +--> /handoff  (hybrid brief; OS temp; keep → .scratch/handoffs/)
                 |           often before /code-review (fresh model)
                 v
+=================================+
| ship                            |
| /implement                      |
|   | prefer /tdd at agreed seams |
|   | target-repo checks          |
|   v                             |
| /upkeep → /context [if present] |
|   AGENTS / CHANGELOG / OKF      |
|   v                             |
| /code-review as subagent  OR    |
| /handoff → /code-review → stop  |
|   v                             |
| /commit (local | push+PR |      |
|          canonical — intent)    |
|   +--> /merge   [integrating]   |
|   +--> /release [cutting]       |
+=================================+
```

`idea` and `handoff` sit beside each other on the record spine: **`idea`** parks
thoughts that are not sprint work; **`handoff`** packs *current* work for a
fresh agent (review, continue, or muddy ADR/PRD authoring). Promote durable
intent with **`roadmap`**; do not treat scratch capture as a tracker ticket.

### Same idea later (edit loop)

```text
+------------------+
| /grill-me / edit |
| /to-prd / /to-adr|
+--------+---------+
         |
         v
+------------------+
| /implement       |
| (+ /tdd; checks) |
+--------+---------+
         |
         v
+------------------+
| /upkeep →        |
| /context         |
+--------+---------+
         |
         v
+------------------+
| /code-review as  |
| subagent  OR     |
| /handoff →       |
| /code-review     |
+--------+---------+
         |
         v
+------------------+
| /commit →        |
| [/merge] →       |
| [/release]       |
+------------------+
```

### Lost mid-explanation

```text
+-----------+
| /wait-what|
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

### Session switch / park a thought

```text
+---------------------------+
| mid-session fork          |
+-------------+-------------+
              |
     +--------+--------+
     |                 |
     v                 v
+---------+      +-----------+
| /handoff|      | /idea     |
+----+----+      +-----+-----+
     |                 |
     | continue work   | not this sprint
     | for fresh agent | preserve first
     v                 v
+------------------+  +------------------+
| OS temp (default)|  | .scratch/ideas/  |
| or keep →        |  |                  |
| .scratch/        |  | explicit promote  |
|   handoffs/      |  | → /roadmap       |
+--------+---------+  | → docs/ROADMAP.md|
         |            +--------+---------+
         v                     |
+------------------+           | optional
| fresh agent      |           v
| resume / review  |    +--------------+
+------------------+    | GitHub issue |
                        | / Fizzy card |
                        | (publish)    |
                        +--------------+
```

- **`handoff`** — hybrid portable brief for another agent (review bias break,
  muddy grill → ADR/PRD fork, session end). See [ADR 0012](adr/0012-ADR-handoff-hybrid-kinds.md).
- **`idea`** — local brain dump; never promotes or opens trackers by itself.
- **`roadmap`** — explicit promote into [ROADMAP.md](ROADMAP.md); publish is a
  separate explicit step.

## Branch map (when to reach for what)

| Situation | Skill(s) |
|-----------|----------|
| Skills not installed | `npx skills@latest add bmurrtech/skills` |
| Repo lacks AGENTS / CONTEXT / ADR / `.scratch` conventions | **`setup-bmurrtech-skills`** ([tree](skill-scaffold.md)) |
| Design ambiguous; need shared understanding | **`grill-me`** |
| Need a local PRD / focused sprint spec | **`to-prd`** (see [Local PRDs](#local-prds-docsprd) below) |
| Costly-to-reverse decision | **`to-adr`** ([how-to](how-to-adr.md)) |
| Park a thought for later (not this sprint) | **`idea`** → `.scratch/ideas/` |
| Promote durable idea to public ledger | **`roadmap`** → [ROADMAP.md](ROADMAP.md) |
| Publish idea to GitHub / Fizzy | **`roadmap`** publish (explicit; not from capture alone) |
| Structure clearer as a diagram | **`ascii`** (terminal) or **`visual-explainer`** (HTML under `.scratch/diagrams/`) |
| Build from a clear acceptance target | **`implement`** (prefer **`tdd`**; then subagent **`code-review`** or **`handoff` → `code-review`**; Git via **`commit`**) |
| Review only (branch / PR / local diff) | **`code-review`** (prefer after **`handoff`** to a fresh agent) |
| Red-green at agreed seams | **`tdd`** |
| Local commit / checkpoint (default: no push) | **`commit`** |
| Commit and open/update a PR | **`commit`** with push intent |
| Push directly to main (override) | **`commit`** with canonical intent |
| Merge a reviewed PR | **`merge`** |
| Cut a versioned GitHub Release | **`release`** |
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

## Skill registry

Details live here (README keeps a short index only).

### Bootstrap

| Skill | Role |
|-------|------|
| **`setup-bmurrtech-skills`** | Idempotent scaffold: gitignore, `.scratch/` (+ `diagrams/`, `adr-optics/`), AGENTS/CLAUDE/CONTEXT, knowledge stub, `docs/adr/`, `docs/prd` ignore. Optional **`docx`**. Never silent overwrite. Tree: [skill-scaffold.md](skill-scaffold.md). |
| **`docx`** | Word `.docx` via pinned docx-cli (operator install — [how-to-docx-cli.md](how-to-docx-cli.md)); LibreOffice/Word probe. Opt in at setup or `--skill docx`. |

### Shape and record

| Skill | Role |
|-------|------|
| **`grill-me`** | Design-tree interview until shared understanding; updates glossary/OKF when present; may warrant **`to-adr`**. |
| **`to-prd`** | Local OKF PRDs under gitignored `docs/prd/` for a focused sprint. Cite ADRs; use **`ascii`** for structure. |
| **`to-adr`** | Tracked ADRs under `docs/adr/`; optional at-a-glance under `.scratch/adr-optics/`. [how-to-adr.md](how-to-adr.md). |
| **`ascii`** | Plain-text structure diagrams in-terminal. |
| **`visual-explainer`** | Intent-routed HTML under `.scratch/diagrams/`. [how-to-visual-explainer.md](how-to-visual-explainer.md). |
| **`writing-for-agents`** | Levers for skills and other agent-facing instructions (pointers, hierarchy, Boundaries, pruning). |

### Ship

| Skill | Role |
|-------|------|
| **`tdd`** | Red-green at agreed seams; OKF test-maps + AGENTS Test index when conventions exist. |
| **`implement`** | Spec/tickets → prefer TDD → target-repo checks → soft **`upkeep`** / **`context`** → **`code-review`** as subagent or **`handoff` → `code-review`**. Never stage/commit/push — **`commit`** owns Git. |
| **`code-review`** | Standards ‖ Spec; severity; APPROVE / REQUEST CHANGES / COMMENT. Prefer a **`handoff`** to a fresh agent first. |

### Git lifecycle

Safe Git/GitHub publish → integrate → cut. Defaults favor local durability and review; overrides are explicit in the prompt.

| Skill | Role |
|-------|------|
| **`commit`** | Local-first commit; orchestrates **`upkeep`** (+ **`roadmap` status** on ledger impact); on push intent → short branch + PR; on “push to main” → canonical push when allowed. Canonical push never skips maintenance. |
| **`merge`** | Choose PR; hard-stop on GitHub-enforced gates **or** missing maintenance on the reviewed head (route back to **`commit`**); surface advisory findings; expected-head merge/queue; safe cleanup. |
| **`release`** | Discover contract (existing > ecosystem defaults); **version gate** → prep via **`commit`** (release context) → local validate → **publication gate** → annotated `v*` tag; bootstrap thin workflow only when earned (no tag same run). Does not mutate CHANGELOG. |

**Defaults vs overrides (`commit`):** Intent→Mode matrix lives in
[`skills/commit/SKILL.md`](../skills/commit/SKILL.md#intent) (SoT). Prompt
examples:

| Prompt example | Behavior |
|----------------|----------|
| `Commit this` / `Checkpoint this` | Local commit only (still runs upkeep when applicable) |
| `Commit and push` / `Raise a PR` / `Publish this` | Review branch + push + one PR |
| `Push this directly to main` | Canonical push if allowed; else fall back to PR — maintenance still runs |

**Release gates (defaults):**

| Prompt example | Behavior |
|----------------|----------|
| `Release` (no version) | Version gate recommends; user authorizes version **and** channel; then prep |
| `Release 0.2.1-rc1` | Version + prerelease channel already stated — skip re-ask; still run publication gate before tag push |
| Affirmative after validate | Publication gate: yes/proceed/LGTM binds exact tag + SHA |

More examples:

- `Merge PR #42` — resolve that PR; respect required checks/reviews; hard-stop if maintenance missing → **`commit`** first
- `Merge this` — only if one unambiguous PR; else ask
- Dogfood here: `python3 scripts/package_skills.py` + existing `release.yml` (ADR 0005) — do not invent a second publication path

### Session hygiene / ideas

| Skill | Role |
|-------|------|
| **`handoff`** | Hybrid portable brief for a fresh agent ([ADR 0012](adr/0012-ADR-handoff-hybrid-kinds.md)). Default: OS temp. **keep** → `.scratch/handoffs/`. Base + kind overlays; kinds labeled in the file as full name `(slug)` (e.g. code-review (`cd-rvw`)); post-write glance. |
| **`idea`** | Preserve-first brain dump under `.scratch/ideas/`. No promote, no trackers, no implement. |
| **`roadmap`** | Ensure/promote/status into public [ROADMAP.md](ROADMAP.md); GitHub/Fizzy publish only on separate explicit intent. Templates: `skills/roadmap/references/`. |
| **`wait-what`** | STE re-pitch when an explanation did not land. |
| **`upkeep`** | `AGENTS.md`, `CLAUDE.md` pointer, `CHANGELOG.md` Unreleased; **release-cut** promotes Unreleased → dated when `release_intent` + confirmed version. |
| **`context`** | `CONTEXT.md` + `knowledge/` OKF — no ops-manual edits. |

Future orchestration (`ultrawork` / `ralph` OMX integration): [ROADMAP.md](ROADMAP.md) — not minted yet.

## Library maintainers (this repo)

When changing skills in **bmurrtech/skills** itself:

1. **`writing-for-agents`** for new/edited skills
2. `python3 scripts/init_skill.py <name>` when scaffolding a new skill folder
3. `python3 scripts/quick_validate.py skills/<name>`
4. Session tests via AGENTS Test index → OKF test-maps (`**tdd**`)
5. After implement: **`upkeep`** → **`context`**, then **`code-review`** as subagent or **`handoff` → `code-review`**; publish only via **`commit`**
6. Package smoke: `python3 scripts/package_skills.py --version <semver> --out dist/`

Consumer repos without `CONTEXT.md` / `AGENTS.md`: portable skills (**`implement`**,
**`code-review`**, **`tdd`**, **`grill-me`**, **`wait-what`**) soft-skip
glossary/ops housekeeping.

## Related

- [README.md](../README.md) — quick start + skill index
- [ROADMAP.md](ROADMAP.md) — durable idea ledger (`idea` → promote → publish)
- [skill-scaffold.md](skill-scaffold.md) — folders/files setup creates
- [how-to-adr.md](how-to-adr.md) — ADR authoring + at-a-glance
- [how-to-visual-explainer.md](how-to-visual-explainer.md) — visual-explainer prompts
- [about-license.md](about-license.md) — Apache-2.0
- [adr/index.md](adr/index.md) — decisions
- [CONTEXT.md](../CONTEXT.md) — glossary (library SoT; not shipped in release artifact)
- [Skill registry](#skill-registry) — this doc
