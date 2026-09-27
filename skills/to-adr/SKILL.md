---
name: to-adr
description: >
  Author or supersede Architectural Decision Records under docs/adr/ with
  shipped mechanics headings; classify cited prior ADRs as supersede vs relate;
  update docs/adr/index.md; rebuild at-a-glance HTML catalog. Use when a
  decision is costly to reverse, alternatives were real, someone will ask why
  months later, a new ADR replaces an Accepted one, or when visualizing the
  decision log.
disable-model-invocation: true
---

# to-adr

Record **one** significant decision per file under `docs/adr/`. Markdown is
authoritative; the HTML catalog is a generated view.

This skill is **self-contained** (ships in the skills release artifact). Do not
require this library’s `knowledge/` to author ADRs in a consumer repo.

When **`writing-for-agents`** is installed, apply its levers to ADR prose
(hierarchy, completion criteria, pruning). Soft-skip when absent.

## Boundaries

- Do **not** put feature scope, journeys, MVP phases, or sprint plans in an ADR
  — those belong in a PRD (via **`to-prd`** when present).
- Do **not** paste standing ops or glossary text into an ADR — link consumer
  `AGENTS.md` / `CONTEXT.md` / `knowledge/` (when they exist) or another ADR.
- Do **not** edit an **Accepted** ADR in place — supersede with a new file.
- Do **not** invent Implementation Notes checklists (security/CI/ops) unless
  that topic *is* the decision — see [references/mechanics.md](references/mechanics.md).

## Warrant (before a new file)

Create only if at least one is true:

- costly to reverse
- reasonable people could have chosen differently
- someone will ask “why this way?” later

If none apply, point at an existing ADR or a doc section to edit instead. User
insistence after a failed warrant → ask once; default remains no file.

## Workflow

### 1. Resolve intent

New vs edit: Accepted ADRs are immutable — “change” means a new ADR that
**supersedes** the old path. Ambiguous → ask.

**Done when:** create vs supersede is clear.

### 2. Classify cited prior ADRs

For every older ADR this decision mentions, pick exactly one:

| Class | Meaning | Status links |
|-------|---------|--------------|
| **supersede** | New **outcome replaces** the old decision | New: `Supersedes` → old. Old: Status → `Superseded`, `Superseded by` → new. Index both rows. |
| **relate** | New decision **preserves or extends** the old one | Status `Supersedes` / `Superseded by` stay `—`. Index **Related** column (and optional Status **Related ADRs**). |
| **reject-option-cost** | Old ADR is a reason an **option fails** (pros/cons), not a replaced decision | Same as **relate** — never write `Superseded by` on the old ADR. |

Citing “breaks ADR NNNN” under a rejected option is **reject-option-cost** /
**relate**, not **supersede**.

**Done when:** every cited prior ADR has one class; supersede pairs get
bidirectional Status updates in the same run.

### 3. Number and path

- Home: `docs/adr/` (create if missing)
- Name: `NNNN-ADR-<slug>.md` (four digits, no project-key prefix)
- Next `NNNN`: max existing index + 1 (first is `0001`)

**Done when:** path does not collide.

### 4. Write body

Load [references/mechanics.md](references/mechanics.md) for headings, placement,
and anti-bloat rules. Status values: Proposed | Accepted | Deprecated |
Superseded. Link supersedes / superseded-by / related with Markdown paths.
Prefer cite under **References** over paste.

**Done when:** required headings present; decision outcome is assertive; Status
links match the class from step 2; Implementation Notes (if any) are
outcome-entailed only.

### 5. Update index

Add or revise the row in `docs/adr/index.md`. Put **relate** /
**reject-option-cost** targets in the Related column; for **supersede**, set
Status on both rows.

**Done when:** index row matches the file(s).

### 6. Visualize (at-a-glance)

After create/supersede (or when the user asks for the decision log / catalog):

1. If **`.scratch/adr-optics/`** is missing, run **`setup-bmurrtech-skills`**
   (creates `.scratch/`, `.scratch/diagrams/`, `.scratch/adr-optics/`, and the
   rest of the scaffold) — then continue.
2. Rebuild and **open** the catalog with this skill’s **repo-local** helper
   (ships beside this `SKILL.md`; no remote install):

| | |
|--|--|
| **Script** | `scripts/build_catalog.py` under this skill directory (library path: `skills/to-adr/scripts/build_catalog.py`; harness installs: same relative path on the installed skill) |
| **Reads** | Markdown ADRs under `--home` (default intent: `docs/adr/`); template `scripts/visualizer_template.html` |
| **Writes** | Optional refresh of `docs/adr/index.md`; with `--visualize`: `.scratch/adr-optics/adr-catalog.json` + `adr-at-a-glance.html` |
| **Side effects** | `--open` may launch the default browser on a `file://` URI; no network font/CDN loads (system fonts only) |

```bash
python3 skills/to-adr/scripts/build_catalog.py --home docs/adr --visualize --open
```

If this skill lives outside `skills/to-adr/` (harness install path), point at
this skill’s `scripts/build_catalog.py` instead.

`--open` launches the default browser (`file://`). If the harness cannot open a
browser, report the absolute path and the `file://` URI from the script JSON.

Markdown under `docs/adr/` remains SoT; HTML is a generated view (not tracked).

**Done when:** script exits 0; browser opened or `file://` path reported; soft-skip
only if Python unavailable (still leave Markdown + index correct).
