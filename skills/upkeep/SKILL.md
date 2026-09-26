---
name: upkeep
description: >
  Maintain AGENTS.md as the agent ops manual; create or repair CLAUDE.md so its
  entire body is exactly AGENTS.md; ensure CHANGELOG.md exists and Unreleased
  notes cover the session. Use when auditing or rewriting AGENTS.md, after
  implement or code-review, when layout/commands/boundaries change, when
  CLAUDE.md is missing or drifts, or when CHANGELOG.md is missing/stale.
---

# upkeep

Keep `AGENTS.md` accurate and executable. Keep `CHANGELOG.md` current for human/release notes. Do not edit `CONTEXT.md` or `knowledge/` here — that is the `context` skill.

## Completion bar

Done when:

- `AGENTS.md` matches repo evidence
- `CLAUDE.md` exists and its full body is exactly the six characters `AGENTS.md` plus optional trailing newline
- `CHANGELOG.md` exists (Keep a Changelog shape) with session-notable items under `## [Unreleased]` when this run follows implement/code-review work
- no glossary definitions were copied into `AGENTS.md`

## Workflow

### 1. Discover

Read existing `AGENTS.md` (if any), `README.md`, `CHANGELOG.md` (if any), `CONTEXT.md` (for links only), manifests, scripts, and CI. Build a fact sheet from evidence — never invent commands.

**Done when:** facts are listed or explicitly marked unknown.

### 2. Ensure CLAUDE.md pointer

If `CLAUDE.md` is missing, or its content is anything other than `AGENTS.md` (optional final newline allowed), write:

```text
AGENTS.md
```

**Done when:** pointer contract holds.

### 3. Ensure CHANGELOG.md

If `CHANGELOG.md` is **missing**, create a Keep a Changelog stub with `## [Unreleased]` (Added/Changed/Fixed as needed) and a one-line pointer that the project uses SemVer.

If it **exists** and this upkeep follows **`implement`** / **`code-review`** (or the user asked for changelog hygiene):

1. Ensure a `## [Unreleased]` section exists (create near the top, above dated releases, if absent).
2. Add concise bullets for **user-facing or operator-facing** changes from the session that are not already listed — packaging/CI/workflow, skills behavior, install contract, ADRs. Skip pure typo/noise.
3. Do **not** invent a version bump or move Unreleased → versioned unless the user is cutting a release.

**Done when:** changelog exists; Unreleased reflects the session (or was already complete).

### 4. Draft or patch AGENTS.md

Prefer operational sections: overview, structure, setup, validation, style, git/PR, boundaries, security, references.

Link to `CONTEXT.md` and `docs/adr/` instead of restating glossary or ADR bodies.

Preserve any **Test index (OKF)** one-liners under Testing — `tdd` owns appending them; `upkeep` keeps them accurate and linked. Do not expand them into suite dumps.

Mention `.scratch/` in structure/boundaries when the repo uses that pad (ignored; agent dumps only).

Mention `CHANGELOG.md` in references (and structure if useful) when the file exists.

Cite evidence-backed CI/workflow commands (e.g. `.github/workflows/`) when present.

**Done when:** every command cited is evidence-backed; boundaries include “skills only under `skills/`” and the post-`implement`/`code-review` hook to run `upkeep` then `context`; Test index preserved when present.

### 5. Validate

Check paths exist; root vs nested instructions do not conflict; no secret material.

**Done when:** file is safe to commit from an ops perspective.

## Template

Use [references/AGENTS.template.md](references/AGENTS.template.md) as a starting shape; delete irrelevant sections.
