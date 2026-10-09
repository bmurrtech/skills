---
title: Universal sprint skill
description: Portable implement/code-review/tdd (and soft-coupled siblings) for any consumer repo.
type: concept
tags: [skills, sprint]
---

# Universal sprint skill

Skills meant to improve sprints in **any** repo that installs them — not only this library.

## Set

- Core: `implement`, `code-review`, `tdd`
- Soft-coupled: `grill-me`, `wait-what`, `handoff` (CONTEXT / glossary “if present”)

## Rules of thumb

- Spec discovery is ordered and optional (`docs/prd/` / `.scratch/` are paths, not the only ones).
- Validation = target repo evidence (`AGENTS.md`, package scripts, CI).
- Skill validators (`quick_validate.py`) are optional and only when a `skills/` tree changed **and** a validator exists.
- `upkeep` / `context` run when installed **and** artifacts exist; otherwise one-line skip.
- **`implement`**: review exit = subagent `code-review` or `handoff` for code-review (`cd-rvw`); never stage/commit/push — Git via `commit` / `merge` / `release`. When editing agent skills/instructions/scripts, apply `writing-for-agents` + skill-scripts judgment if present (soft-skip otherwise).
- **`code-review`**: judge only — never call `implement`. Gated `tdd` load + adversarial test bar + smallest evidence-run (AGENTS Test index → OKF maps). Path-gated `references/agent-artifacts.md` for skill/agent diffs; skip that lens otherwise.
- **`tdd`**: session-scoped runs via AGENTS Test index → OKF test-maps when those conventions exist.

## Contrast

Library-specific skills (`writing-for-agents`, `writing-for-humans`, `setup-bmurrtech-skills`, `docx`, `visual-explainer`, `to-prd`, `to-adr`, `upkeep`, `context`) may assume this repo’s layout. Do not copy those assumptions into universal sprint skills.

## Related

- Glossary: [CONTEXT.md](../CONTEXT.md)
- [Skill](agent-skill.md)
