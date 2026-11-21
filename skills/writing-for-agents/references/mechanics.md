# Skill mechanics

Read when the document is a **skill** (`SKILL.md` + optional bundle). Covers
layout, frontmatter, invocation, routers, and a must-pass checklist. For shared
writing levers (any agent doc), see [levers.md](levers.md).

## File structure

```text
skills/<kebab-name>/
├── SKILL.md          # required — exact filename (case-sensitive)
├── agents/
│   └── openai.yaml   # required in this library
├── scripts/          # optional
├── references/       # optional
└── assets/           # optional
```

- Folder name: kebab-case only (no spaces, underscores, or capitals); matches
  frontmatter `name`
- `SKILL.md` only — not `skill.md`, `SKILL.MD`, or other variants
- No `README.md` inside the skill folder; put docs in `SKILL.md` or
  `references/`
- Omit `scripts/` / `references/` / `assets/` unless the skill needs them

## Frontmatter

Minimal:

```yaml
---
name: your-skill-name
description: What it does. Use when user asks to [specific phrases].
---
```

Required:

- `name` — kebab-case, ≤64 chars, matches folder
- `description` — what **and** when; ≤1024 chars; no `<` or `>`; include
  concrete task phrases (and file types when relevant); the always-loaded
  **context pointer** (see levers)

Optional host fields (`license`, `allowed-tools`, `metadata`, …): prefer omit
unknowns.

### Description field (first progressive-disclosure level)

Metadata alone should tell the host **when** to load the skill — without
pulling the body into context. Structure:

**[What it does] + [When to use it] + [Key capabilities]**

Pointer rules:

- Third person; front-load the **leading word**
- One trigger phrase per distinct **branch** (collapse synonyms)
- Specific and actionable; include user-said phrases and file types when
  relevant
- No identity fluff the body already states

Good:

```yaml
description: >
  Analyzes Figma design files and generates developer handoff documentation.
  Use when user uploads .fig files, asks for "design specs", "component
  documentation", or "design-to-code handoff".
```

```yaml
description: >
  Manages Linear project workflows including sprint planning, task creation,
  and status tracking. Use when user mentions "sprint", "Linear tasks",
  "project planning", or asks to "create tickets".
```

```yaml
description: >
  End-to-end customer onboarding workflow for PayFlow. Handles account
  creation, payment setup, and subscription management. Use when user says
  "onboard new customer", "set up subscription", or "create PayFlow account".
```

Bad:

```yaml
description: Helps with projects.   # too vague — no what/when/triggers
```

```yaml
description: >
  Creates sophisticated multi-page documentation systems.  # missing triggers
```

```yaml
description: >
  Implements the Project entity model with hierarchical relationships.
  # too technical — no user-facing triggers
```

## Writing the body

After frontmatter, write Markdown instructions the agent follows once the skill
loads. Prefer this shape (adapt; omit sections that do not earn their keep):

~~~~markdown
# your-skill-name

## Overview
[One or two sentences — optional if the first step is enough]

## Workflow

### 1. [First major step]

[What to do — specific commands, paths, checks.]

Example:
```bash
python scripts/fetch_data.py --project-id PROJECT_ID
```
Expected output: [what success looks like]

**Done when:** [checkable criterion]

### 2. [Next step]
…
**Done when:** …

## Examples
### Example 1: [common scenario]
User says: "…"
Actions: 1. … 2. …
Result: …

## Troubleshooting
### Error: [common message]
**Cause:** …
**Solution:** …
~~~~

Keep core steps in `SKILL.md`. Move long API tables, branch matrices, and deep
guides to `references/` with **when-to-read** links. End real avoid-behaviours
in **Boundaries** (see levers).

### Instruction best practices

**Be specific and actionable**

- Good: Run `python scripts/validate.py --input {filename}` to check data
  format. If validation fails: missing required fields; dates must be
  YYYY-MM-DD.
- Bad: Validate the data before proceeding.

**Include error handling** when failures are common — short **Troubleshooting**
(or per-step recovery) with cause + fix, not a shrug.

**Reference bundled resources clearly**

- Good: Before writing queries, consult `references/api-patterns.md` for rate
  limits, pagination, and error codes.
- Name the path and what to take from it.

**Use progressive disclosure** — lean body; disclose branch-only detail under
`references/` (see levers).

## Invocation choice

Decide whether the host may model-trigger the skill:

| Intent | Frontmatter / policy |
|--------|----------------------|
| User-only / explicit invoke | `disable-model-invocation: true` and `policy.allow_implicit_invocation: false` |
| Model may auto-route | omit disable; `policy.allow_implicit_invocation: true` |

Keep description human/routing-facing either way. Align yaml policy with whether
the skill may model-trigger — mismatch is a variance bug.

**Split by invocation** when one folder tries to serve both a rare explicit
procedure and a high-frequency auto-route: two skills (or a thin router +
bodies), not one overloaded description.

## Router skills

A **router** skill's job is to choose or dispatch other skills — not to inline
their workflows.

- Description lists genuinely distinct branches (one trigger each)
- Body: short chooser + links/names of target skills
- Never paste a second skill's full steps; name it and stop
- Disclose long branch matrices under `references/` with when-to-read

## Must-pass checklist

Score before ship. Waive only with reason.

### Description (trigger pointer)

- [ ] Third person; **what + when + key capabilities**; front-load the leading word
- [ ] Concrete user trigger phrases (and file types when relevant)
- [ ] One trigger per distinct branch
- [ ] ≤1024 chars; no `<`/`>`; no identity the body already carries
- [ ] Not vague, not trigger-less, not internals-only jargon
- [ ] If user-only, description stays routing-facing; policy matches

### Body shape

- [ ] Imperative steps in order; each ends with checkable **Done when**
      (clarity + demand — see levers)
- [ ] Commands/paths concrete; expected success called out when useful
- [ ] Common failures have cause + fix (inline or Troubleshooting)
- [ ] Bundled `references/` / `scripts/` named with when-to-read / how-to-run
- [ ] **Boundaries** (or equivalent) holds negative-imperative guardrails for
      real avoid-behaviours; omit only if none; no soft “prefer not” hedges
- [ ] Degrees of freedom match fragility (high prose / medium templates / low scripts)
- [ ] Repo-relative POSIX paths only

### Layout

- [ ] Folder + `name` kebab-case and matching
- [ ] Entry file is exactly `SKILL.md` (case-sensitive)
- [ ] No `README.md` (or other skill-folder readme) under the skill tree
- [ ] Optional dirs only when used (`scripts/` / `references/` / `assets/`)

### Progressive disclosure

- [ ] Always-needed rules stay inline
- [ ] Branch-only / long lists in `references/` with when-to-read links
- [ ] Refs one level deep from `SKILL.md`
- [ ] Scripts are run (or “read as reference”), not pasted wholesale

### Anti-bloat

- [ ] No restating always-loaded host/ops/glossary material the environment already provides
- [ ] No host-only orchestration unless this skill's product is that host
- [ ] No second skill's full workflow inlined — link the skill name
- [ ] Output templates only when format is part of the contract
- [ ] No **no-ops** / **sediment** (see levers pruning)

### `agents/openai.yaml`

- [ ] `display_name`, `short_description` (25–64 chars)
- [ ] `policy.allow_implicit_invocation` matches model-trigger intent

## Further reading

- Workflow patterns (sequential, multi-MCP, iterative, …): [patterns.md](patterns.md)
- Packaging / trigger / MCP troubleshooting: [troubleshooting.md](troubleshooting.md)
- Skill triggering + functional + baseline TDD: **`tdd`**
  [`references/skill-testing.md`](../../tdd/references/skill-testing.md)
