---
title: Skill
description: A modular Agent Skill folder under skills/ with SKILL.md, agents/openai.yaml, and optional bundled resources.
type: concept
tags: [skills]
---

# Skill

A **Skill** in this repository is a directory at `skills/<name>/` containing:

- `SKILL.md` (required) — frontmatter triggers + body instructions
- `agents/openai.yaml` (required) — host UI metadata + invocation policy
- `scripts/` (optional) — deterministic helpers the agent can run (see [skill-scripts.md](skill-scripts.md))
- `references/` (optional) — docs loaded on demand
- `assets/` (optional) — files for output, not for context stuffing

## Rules

- Create and edit skills only under [`skills/`](../skills/).
- `name` is kebab-case, ≤64 characters, matching the folder name.
- Put “when to use” only in `description` (always-loaded pointer).
- Keep the body lean; push branch-specific detail into `references/` with explicit when-to-read links.
- Before adding `scripts/`, apply [Skill scripts vs LLM](skill-scripts.md) — judgment stays in the model; scripts earn their keep via exactness, repetition, or compression.

## Related

- Glossary: [CONTEXT.md](../CONTEXT.md)
- Scripts policy: [skill-scripts.md](skill-scripts.md)
- Writing levers: [`skills/writing-for-agents`](../skills/writing-for-agents/SKILL.md)
