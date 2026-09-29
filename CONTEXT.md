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
Tracked decision under `docs/adr/NNNN-ADR-<slug>.md`, indexed by `docs/adr/index.md`. Accepted = immutable; change via supersede. Authoring SoT ships in **`to-adr`** (`references/mechanics.md`); library OKF only summarizes.

**How-to doc**:
Library consumer guide under `docs/how-to-<topic>.md` (e.g. `how-to-bmurrtech-skills`, `how-to-adr`, `how-to-visual-explainer`). Install/scaffold lives in the main skills how-to; topic how-tos are prompts + scope only.
_Avoid_: `how-to-use-…` naming; duplicating setup into every topic how-to; scaffolding library how-tos into consumers


**.scratch/**:
Gitignored local scratch pad for exploratory, pre-PRD, and other agent artifact dumps related to these skills. Includes `.scratch/diagrams/` for **visual-explainer** HTML (optional Markdown companions), `.scratch/adr-optics/` for **`to-adr`** at-a-glance catalog HTML, `.scratch/handoffs/` for **kept** (non-transitory) **`handoff`** docs, and `.scratch/ideas/` for **`idea`** brain dumps (promote only via **`roadmap`**). Default handoffs are throwaway under the OS temp dir; only an explicit keep signal lands under `.scratch/handoffs/`.
_Avoid_: committing scratch; using tracked `docs/` for throwaways; `/pm/diagrams` or harness skill dirs as diagram SoT; writing default handoffs into the repo; treating scratch ideas as roadmap or tracker commitments

**ROADMAP.md**:
Tracked durable idea ledger under `docs/ROADMAP.md`. Unordered and undated; inclusion ≠ priority or sprint commitment. Owned by **`roadmap`** (promote / publish). Raw thoughts stay in `.scratch/ideas/` via **`idea`** until explicitly promoted.
_Avoid_: dates/estimates/sprint assignments in the ledger; implicit promote or publish; using ROADMAP as the issue tracker

**idea** / **roadmap** (skills):
Capture-local vs durable-intent vs tracked-work commitment levels — **`idea`** preserves first under `.scratch/ideas/`; **`roadmap`** promotes into `docs/ROADMAP.md` and publishes to GitHub/Fizzy only on separate explicit intent.
_Avoid_: collapsing capture/promote/publish into one step; inventing roadmap fields to fill the template

**Test map**:
OKF concept (`type: test-map`) under `knowledge/` naming a seam, the smallest run command, and tracked test paths. Indexed by a one-liner in `AGENTS.md` so agents load only session-relevant tests.
_Avoid_: dumping the whole `tests/` tree into context each session

**grill-me**:
Design-tree interview in frontier rounds; updates glossary via `context`; warrants ADRs via `to-adr`.

**upkeep** / **context** (skills):
Ops manual vs glossary/OKF ownership — never cross-edit.

**writing-for-agents**:
Standalone guidance for writing skills and other agent instructions so behaviour is repeatable across LLMs. Owns levers: context pointers, two loads, information hierarchy, completion criteria, leading words, negative-imperative guardrails, pruning. Soft-skips skill validators when absent. Does not own ops-manual create/maintain.
_Avoid_: flattening levers into unnamed checklist vibes; treating this as upkeep for ops manuals; soft bans where a hard Boundaries line is required

**Context pointer**:
Always-loaded reference that names out-of-context material and encodes when to reach it (skill `description`, always-on instruction line). Wording decides reach reliability; weak wording on a must-have target is a variance bug.
_Avoid_: treating the target path as the trigger; stuffing identity the body already carries

**Leading word**:
Compact pretrained token the agent thinks with while running a document (*tight*, *red*). Recruits priors; repeats as a token, not a sentence. Anchors execution in the body and invocation in pointers.
_Avoid_: coining words with no prior; restating the same idea as a phrase in three places

**setup-bmurrtech-skills**:
Idempotent provision of gitignore (incl. `.scratch/`), `.scratch/` + `.scratch/diagrams/` + `.scratch/adr-optics/`, AGENTS/CLAUDE/CONTEXT, knowledge stub, docs/adr index, docs/prd ignore; optional **`docx`** (docx-cli + office host). Does not install skill folders into harnesses (that is `npx skills`) and does not copy library how-tos / explainers into the consumer. Does not pre-create `.scratch/handoffs/` — **`handoff`** creates it on **keep**. Tree: [docs/skill-scaffold.md](docs/skill-scaffold.md); why: [knowledge/skill-scaffold.md](knowledge/skill-scaffold.md).

**visual-explainer**:
Lean Agent Skill that turns architectures, diffs, plans, tables, and related intent into self-contained HTML under `.scratch/diagrams/`. Single entry with intent routing to modes (diagram, visual-plan, slides, diff-review, plan-review, project-recap, fact-check); modes also callable manually. Optional AI-readable Markdown companion (same basename) only when requested; ask before replace. Inspired by [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) (MIT); no Pi/MCP/PPTX bundle in this remake.
_Avoid_: ASCII/box-drawing as the primary artifact when this skill is loaded; writing diagrams under `/pm/` or agent install dirs; treating the `.md` companion as HTML source

**docx**:
Word `.docx` via pinned **docx-cli** on PATH (operator-installed; pin **0.26.0**). Skill probes version/pin and prints OS-specific **manual** prereq commands on failure — does not download or auto-install CLI/office. Install how-to: [docs/how-to-docx-cli.md](docs/how-to-docx-cli.md). Word or LibreOffice required for render/import. Prefer **`ensure_toolchain`** façade; cores remain `ensure_docx` / `ensure_office`. **ToolchainReady** is the typed evidence report (pin ok ∧ office ready). DIGESTS = operator verify for the pin only. Posture: [ADR 0011](docs/adr/0011-ADR-skill-scanner-posture-prereqs.md).
_Avoid_: agent binary download; `--install` in skill scripts; auto sudo / package-manager install; npx upstream skill install; attack-demo phrases in SKILL.md

**Universal sprint skill**:
Portable skill for any consumer repo: **`implement`**, **`code-review`**, **`tdd`**, plus soft-coupled **`grill-me`** / **`wait-what`** / **`handoff`**. Validation means the *target* repo’s checks; `upkeep`/`context` run only when installed and those artifacts exist. **`code-review`** Spec defaults to local diff + local Spec paths (no default tracker/`gh` fetch — [ADR 0011](docs/adr/0011-ADR-skill-scanner-posture-prereqs.md)).
_Avoid_: requiring `quick_validate.py` for ordinary app/lib work; assuming every consumer is a skills monorepo; default issue-body fetch in code-review

**Library-specific skill**:
Opinionated for this library (or repos that opted into the convention): **`writing-for-agents`**, **`setup-bmurrtech-skills`**, **`docx`**, **`visual-explainer`**, **`to-prd`** / **`to-adr`** homes, **`upkeep`** / **`context`** as glossary/ops maintainers.
_Avoid_: shipping library layout rules inside universal sprint skills

**Skills release artifact**:
Versioned install tarball of `skills/` + `LICENSE` only. Library `knowledge/` / `CONTEXT.md` / ops / docs stay **tracked** in git but are **excluded** by packaging (`scripts/package_skills.py`). Do not gitignore library OKF to keep consumer installs clean.
_Avoid_: shipping full-repo trees as the install artifact; overlaying library OKF onto consumer roots

**Git lifecycle**:
Composable skills **`commit`** / **`merge`** / **`release`** (catalog group in `skills.sh.json`, README, how-to): durable local change + optional review-branch/PR; integrate a chosen PR under GitHub-enforced gates; prove repo-native build contract then deliberate `v*` tag (existing contract > ecosystem defaults; this library dogfoods ADR 0005). Stages do not duplicate each other’s ops.
_Avoid_: one mega-git skill; default push without intent; inventing merge gates beyond GitHub policy; naming **`code-review`** inside **`merge`**; tagging in the same run as first release-workflow bootstrap; alternate packaging when `package_skills.py` + tag workflow exist

## Hard rules

1. **Tracked/published skills live only in `skills/`.** Library-local skills may sit under ignored `.agents/skills/` (host-readable; not product; not OKF; not release).
2. **No glossary/ops duplication.**
3. **`docs/prd/` is local-only** (gitignored); ADRs stay tracked.
4. **Release artifacts exclude library OKF/ops/docs** — filter at package time; keep `knowledge/` tracked.

Post-`implement`/`code-review` housekeeping lives in [`AGENTS.md`](AGENTS.md) Boundaries — not restated here.

## See also

- [knowledge/index.md](knowledge/index.md)
- [docs/adr/index.md](docs/adr/index.md)
- [docs/ROADMAP.md](docs/ROADMAP.md)
- [docs/how-to-bmurrtech-skills.md](docs/how-to-bmurrtech-skills.md)
- [AGENTS.md](AGENTS.md)
