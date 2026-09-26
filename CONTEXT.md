---
title: bmurrtech/skills
description: Domain language and entry point for the skills library knowledge bundle.
type: glossary
okf_version: "0.2"
tags: [skills, agents, glossary]
---

# bmurrtech/skills

Opinionated library of Agent Skills for agentic coding. This file is the glossary SoT. Progressive disclosure lives under [`knowledge/`](knowledge/index.md). Ops instructions for agents live in [`AGENTS.md`](AGENTS.md) — do not duplicate them here.

## Language

**Skill**:
A tracked folder under `skills/<name>/` with required `SKILL.md` and `agents/openai.yaml`, plus optional `scripts/`, `references/`, and `assets/`. The only place new skills are created in this repository.
_Avoid_: prompt pack, `.agents/skills` as SoT

**SKILL.md**:
The skill entry document: YAML frontmatter (`name`, `description`) plus Markdown body loaded after the skill triggers.

**agents/openai.yaml**:
Host UI metadata (`interface`) and `policy.allow_implicit_invocation` for a skill.

**OKF bundle**:
A directory of Markdown concept files with YAML frontmatter, linked for progressive disclosure. Root glossary is this file; concepts live under `knowledge/`. Local PRDs are OKF concepts under gitignored `docs/prd/`.

**CONTEXT.md**:
This glossary. Owned by the `context` skill. Not an ops manual.

**AGENTS.md**:
Agent operating manual. Owned by `upkeep`. May link here; must not restate glossary definitions.

**CLAUDE.md**:
Repo file whose entire body is exactly `AGENTS.md`.

**ADR**:
Tracked decision under `docs/adr/NNNN-ADR-<slug>.md`, indexed by `docs/adr/index.md`. Accepted = immutable; change via supersede.

**PRD**:
Local OKF product requirement under `docs/prd/NNNN-PRD-<slug>.md` (gitignored). See `docs/about-prd.md`.

**grill-me**:
Design-tree interview in frontier rounds; updates glossary via `context`; warrants ADRs via `to-adr`.

**upkeep** / **context** (skills):
Ops manual vs glossary/OKF ownership — never cross-edit.

**skill-create**:
Scaffolds skills under `skills/` including `agents/openai.yaml`.

**setup-bmurrtech-skills**:
Idempotent provision of gitignore, AGENTS/CLAUDE/CONTEXT, knowledge stub, docs/adr, about-prd.

**Universal sprint skill**:
Portable skill for any consumer repo: **`implement`**, **`code-review`**, **`tdd`**, plus soft-coupled **`grill-me`** / **`wait-what`** / **`handoff`**. Validation means the *target* repo’s checks; `upkeep`/`context` run only when installed and those artifacts exist.
_Avoid_: requiring `quick_validate.py` for ordinary app/lib work; assuming every consumer is a skills monorepo

**Library-specific skill**:
Opinionated for this library (or repos that opted into the convention): **`skill-create`**, **`setup-bmurrtech-skills`**, **`to-prd`** / **`to-adr`** homes, **`upkeep`** / **`context`** as glossary/ops maintainers.
_Avoid_: shipping library layout rules inside universal sprint skills

## Hard rules

1. **All skills live in `skills/`.**
2. **No glossary/ops duplication.**
3. **`docs/prd/` is local-only** (gitignored); ADRs stay tracked.

Post-`implement`/`code-review` housekeeping lives in [`AGENTS.md`](AGENTS.md) Boundaries — not restated here.

## See also

- [knowledge/index.md](knowledge/index.md)
- [docs/adr/index.md](docs/adr/index.md)
- [docs/about-prd.md](docs/about-prd.md)
- [AGENTS.md](AGENTS.md)
