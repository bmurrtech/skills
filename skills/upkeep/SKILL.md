---
name: upkeep
description: >
  Maintain AGENTS.md as the agent ops manual; create or repair CLAUDE.md so its
  entire body is exactly AGENTS.md. Use when auditing or rewriting AGENTS.md,
  after implement or code-review, when layout/commands/boundaries change, or when
  CLAUDE.md is missing or drifts from the pointer contract.
---

# upkeep

Keep `AGENTS.md` accurate and executable. Do not edit `CONTEXT.md` or `knowledge/` here — that is the `context` skill.

## Completion bar

Done when: `AGENTS.md` matches repo evidence; `CLAUDE.md` exists and its full body is exactly the six characters `AGENTS.md` plus optional trailing newline; no glossary definitions were copied into `AGENTS.md`.

## Workflow

### 1. Discover

Read existing `AGENTS.md` (if any), `README.md`, `CONTEXT.md` (for links only), manifests, scripts, and CI. Build a fact sheet from evidence — never invent commands.

**Done when:** facts are listed or explicitly marked unknown.

### 2. Ensure CLAUDE.md pointer

If `CLAUDE.md` is missing, or its content is anything other than `AGENTS.md` (optional final newline allowed), write:

```text
AGENTS.md
```

**Done when:** pointer contract holds.

### 3. Draft or patch AGENTS.md

Prefer operational sections: overview, structure, setup, validation, style, git/PR, boundaries, security, references.

Link to `CONTEXT.md` and `docs/adr/` instead of restating glossary or ADR bodies.

**Done when:** every command cited is evidence-backed; boundaries include “skills only under `skills/`” and the post-`implement`/`code-review` hook to run `upkeep` then `context`.

### 4. Validate

Check paths exist; root vs nested instructions do not conflict; no secret material.

**Done when:** file is safe to commit from an ops perspective.

## Template

Use [references/AGENTS.template.md](references/AGENTS.template.md) as a starting shape; delete irrelevant sections.
