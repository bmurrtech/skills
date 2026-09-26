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

- Spec discovery is ordered and optional (`docs/prd/` is one path, not the only one).
- Validation = target repo evidence (`AGENTS.md`, package scripts, CI).
- Skill validators (`quick_validate.py`) are optional and only when a `skills/` tree changed **and** a validator exists.
- `upkeep` / `context` run when installed **and** artifacts exist; otherwise one-line skip.

## Contrast

Library-specific skills (`skill-create`, `setup-bmurrtech-skills`, `to-prd`, `to-adr`, `upkeep`, `context`) may assume this repo’s layout. Do not copy those assumptions into universal sprint skills.

## Related

- Glossary: [CONTEXT.md](../CONTEXT.md)
- [Skill](skill.md)
