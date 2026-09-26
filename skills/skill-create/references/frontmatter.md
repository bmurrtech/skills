# Frontmatter

## Required fields

- `name` — kebab-case `[a-z0-9-]+`, ≤64 chars, no leading/trailing/double hyphens, should match folder name
- `description` — what the skill does **and** when to use it; ≤1024 chars; no `<` or `>`

The host uses `name` + `description` to decide triggering. The body loads only after trigger.

## Description as pointer

- Front-load the leading word (the concept the agent should latch onto)
- One trigger phrase per distinct branch (collapse synonyms)
- Do not spend description tokens on identity the body already states

## Optional fields (interop)

Hosts may honor: `license`, `allowed-tools`, `metadata`, `compatibility`. Prefer omitting unknowns.

## User-only skills

If a skill must never model-trigger, set `disable-model-invocation: true` and keep `description` human-facing. Note: some validators may flag unknown keys — prefer host docs when enabling this.
