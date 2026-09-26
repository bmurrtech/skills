---
name: setup-bmurrtech-skills
description: >
  Idempotent greenfield provision for bmurrtech skills conventions: gitignore,
  AGENTS.md, CLAUDE.md pointer, CONTEXT.md, knowledge OKF stub, docs/adr,
  docs/about-prd, docs/prd ignore. Use when bootstrapping a repo or repairing
  missing scaffold — never silent overwrite of user content.
disable-model-invocation: true
---

# setup-bmurrtech-skills

Provision this repo’s agent conventions. **Explore → present → confirm → write.** Idempotent: create only what is missing; ask before replacing non-empty files.

This does **not** install skill folders into the consumer (use `npx skills add bmurrtech/skills` for that).

## 1. Explore

Inspect:

- `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `knowledge/`, `docs/adr/`, `docs/about-prd.md`, `docs/about-license.md`, `LICENSE`
- Whether `docs/prd/` is ignored
- Remotes / GitHub (informational only — no issue-tracker setup unless asked later)

**Done when:** present/missing map is ready.

## 2. Present and confirm

Show what you will create vs leave alone. Recommended defaults:

| Artifact | Action if missing |
|----------|-------------------|
| `.gitignore` entries | Ensure `/pm/`, `.agents/`, `.claude/`, `.cursor/`, `/docs/prd/` |
| `AGENTS.md` | Create lean ops manual (link glossary; skills only under `skills/` if that dir exists) |
| `CLAUDE.md` | Body exactly `AGENTS.md` |
| `CONTEXT.md` | OKF-shaped glossary stub |
| `knowledge/index.md` | Minimal index linking CONTEXT |
| `docs/adr/index.md` | Empty catalog table |
| `docs/about-prd.md` | Explains local OKF PRDs |

Wait for confirmation before writing.

## 3. Write

Apply confirmed creates/patches only. Prefer append for `.gitignore` missing lines over rewriting the whole file.

**Done when:** confirmed artifacts exist; `CLAUDE.md` pointer holds; user told what changed.

## 4. Point next

Suggest: `npx skills add bmurrtech/skills` (if skills not present), then `grill-me` / `to-prd` / `to-adr` as needed.
