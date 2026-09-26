---
name: to-adr
description: >
  Author or supersede Markdown Architectural Decision Records under docs/adr/
  with MADR headings and update docs/adr/index.md. Use when a decision is costly
  to reverse, alternatives were real, or someone will ask why months later; or
  when the user asks for an ADR.
---

# to-adr

Record one significant decision per file under `docs/adr/`.

## Warrant (before a new file)

Create only if at least one is true:

- costly to reverse
- reasonable people could have chosen differently
- someone will ask “why this way?” later

If none apply, point at an existing ADR or a doc section to edit instead. User insistence after a failed warrant → ask once; default remains no file.

## Workflow

### 1. Resolve intent

New vs edit: Accepted ADRs are immutable — “change” means a new ADR that supersedes the old path. Ambiguous → ask.

**Done when:** create vs supersede is clear.

### 2. Number and path

- Home: `docs/adr/`
- Name: `NNNN-ADR-<slug>.md` (four digits, no project-key prefix)
- Next `NNNN`: max existing index + 1 (first is `0001`)

**Done when:** path does not collide.

### 3. Write MADR body

Use headings from [references/madr.md](references/madr.md). Status values: Proposed | Accepted | Deprecated | Superseded. Link supersedes / superseded-by / related docs with Markdown paths.

**Done when:** required headings present; decision outcome is assertive.

### 4. Update index

Add or revise the row in `docs/adr/index.md`.

**Done when:** index row matches the file.

## See also

- [knowledge/adr.md](../../knowledge/adr.md)
