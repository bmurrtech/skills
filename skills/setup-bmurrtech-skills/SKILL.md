---
name: setup-bmurrtech-skills
description: >
  Idempotent greenfield provision for bmurrtech skills conventions: gitignore
  (incl. .scratch/), .scratch/diagrams/ + .scratch/adr-optics/, AGENTS.md,
  CLAUDE.md pointer, CONTEXT.md, knowledge OKF stub, docs/adr index; PRD track
  vs ignore choice (default ignore); optional docx (docx-cli + office host). Use
  when bootstrapping a repo or repairing missing scaffold — never silent
  overwrite of user content; re-runs re-ask optional choices.
disable-model-invocation: true
---

# setup-bmurrtech-skills

Provision this repo’s agent conventions. **Explore → present → confirm → write.** Idempotent: create only what is missing; ask before replacing non-empty files; **re-ask** optional choices on every run so policy can flip.

This does **not** install skill folders into the consumer (use `npx skills add bmurrtech/skills` for that).

## 1. Explore

Inspect:

- `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `knowledge/`, `docs/adr/`
- **PRD policy class** for `docs/prd/` (`conflict` | `ignored` | `tracked` | `unset`) — see [references/prd-tracking.md](references/prd-tracking.md)
- Whether `.scratch/` is ignored
- Whether `.scratch/`, `.scratch/diagrams/`, and `.scratch/adr-optics/` exist as local folders
- Remotes / GitHub (informational only — no issue-tracker setup unless asked later)
- Optional: `docx` on PATH, Word / LibreOffice if offering docx tooling

**Done when:** present/missing map + PRD policy class ready.

## 2. Present and confirm

Show what you will create vs leave alone. Recommended defaults:

| Artifact | Action if missing |
|----------|-------------------|
| `.gitignore` entries | Ensure `/pm/`, `.agents/`, `.claude/`, `.cursor/`, `.scratch/` (and `/docs/prd/` **only** when PRD choice is **A**) |
| `.scratch/` | Create directory (untracked scratch pad — see below) |
| `.scratch/diagrams/` | Create directory (HTML output for **visual-explainer**) |
| `.scratch/adr-optics/` | Create directory (at-a-glance HTML for **`to-adr`**) |
| `AGENTS.md` | Create lean ops manual (link glossary; skills only under `skills/` if that dir exists; include Test index stub under Testing; PRD bullets match A/B choice) |
| `CLAUDE.md` | Body exactly `AGENTS.md` |
| `CONTEXT.md` | OKF-shaped glossary stub (PRD locality matches A/B) |
| `knowledge/index.md` | Minimal index linking CONTEXT |
| `docs/adr/index.md` | Empty catalog table |

Do **not** create library how-tos or explainers (`docs/how-to-*.md`, `docs/skill-scaffold.md`, `docs/about-prd.md`, `docs/about-license.md`, …) in the consumer — those live in the skills library ([ADR 0013](https://github.com/bmurrtech/skills/blob/main/docs/adr/0013-ADR-prd-tracking-choice.md)).

### Optional: Commit PRDs?

**Always re-ask** (even on repair/re-run). Setup **policy** A/B (not grill-me next-step A/B/C). Full prompt, detect classes, write matrix, and AGENTS templates: [references/prd-tracking.md](references/prd-tracking.md).

➡️ **A** (ignored / gitignored). No reply, LGTM, or bare affirmatives → **A**.

Target files for this choice only: `.gitignore`, `AGENTS.md`, `CONTEXT.md` (stub or confirmed edit), `CLAUDE.md` if AGENTS changed.

### Optional: Want AI to edit your `.docx` files?

Offer **once per run** (default **no** unless the user asked for Word/docx work):

> Want AI to edit your `.docx` files?

If yes: install **`docx`** skill if missing, point the operator at library
[docs/how-to-docx-cli.md](https://github.com/bmurrtech/skills/blob/main/docs/how-to-docx-cli.md)
(pin **0.26.0**), then run that skill’s **Ensure toolchain** probe
(`ensure_toolchain.py`). Do not download the CLI or run `--install`. Office
hosts stay manual. Do not restate install matrices here.

### `.scratch/` purpose

Untracked scratch pad for exploratory, pre-PRD, and other **agent artifact dumps** tied to these skills (draft notes, session dumps). **`.scratch/diagrams/`** is the default home for **visual-explainer** HTML (and optional Markdown companions). **`.scratch/adr-optics/`** holds **`to-adr`** at-a-glance catalog HTML. **`.scratch/handoffs/`** holds **kept** (non-transitory) **`handoff`** docs only — default handoffs stay in OS temp. **`.scratch/ideas/`** holds **`idea`** brain dumps (created on demand; promote only via **`roadmap`**). Never commit it. Prefer it over polluting `docs/`, `pm/`, or tracked trees. Harness skill install dirs remain **`npx skills`** — setup does not create Cursor/Claude/Pi/OpenClaw skill trees.

Wait for confirmation before writing (scaffold table + PRD A/B + docx).

**Done when:** user confirmed creates/patches and A/B (or defaulted to A); docx yes/no settled.

## 3. Write

Apply confirmed creates/patches only. Prefer append for `.gitignore` missing lines over rewriting the whole file.

Ensure `.gitignore` contains a distinct `.scratch/` (or `/.scratch/`) entry. Create `.scratch/`, `.scratch/diagrams/`, and `.scratch/adr-optics/` on disk if missing.

Apply the chosen PRD policy per [references/prd-tracking.md](references/prd-tracking.md) (A or B). Do **not** add `/docs/prd/` when the choice is **B**.

If the user confirmed docx: run **`docx`** ensure steps. Report versions / probe results — never claim ready without evidence.

**Done when:** confirmed artifacts exist; PRD policy surfaces match A or B; `CLAUDE.md` pointer holds; `.scratch/`, `.scratch/diagrams/`, and `.scratch/adr-optics/` ignored + present locally; optional docx result reported if chosen; user told what changed (including already-A/B no-ops).

## 4. Point next

Suggest: `npx skills add bmurrtech/skills` (if skills not present), then `grill-me` / `to-prd` / `to-adr` as needed. If docx was opted in, mention **`docx`**. If PRD policy is **B**, note that **`commit`** can track `docs/prd/` when ready.

For scaffold inventory, point humans at library **`docs/skill-scaffold.md`** (tree) and **`knowledge/skill-scaffold.md`** (why) on [bmurrtech/skills](https://github.com/bmurrtech/skills) — not copied into the consumer by setup. Flows: **`docs/how-to-bmurrtech-skills.md`**.

## Boundaries

- Never silent-overwrite non-empty AGENTS/CONTEXT/CLAUDE — ask, or surgically patch setup-owned policy lines only.
- PRD choice guardrails (default A, no `about-prd.md`, no unprompted `git rm --cached`): [references/prd-tracking.md](references/prd-tracking.md).
- Do not install harness skill trees; do not invent a PRD policy marker file.
