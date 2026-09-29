# Roadmap status grammar

Read when classifying or updating an existing `docs/ROADMAP.md` entry.

## Status values

| Value | Meaning |
|-------|---------|
| **Done** | Intent absorbed or shipped; no further ledger work expected |
| **Advanced** | Material progress without full close (spike done, partial ship) |
| **Superseded** | Replaced by another entry, ADR, or skill — point to the successor |

Omit **Status** on open ideas (absence = still open).

## Optional shipped-in-version

When Status is Done (or Advanced with a shipped slice), add a short note:

```markdown
**Status:** Done — absorbed into **`release`**; suite shipped in **0.2.0**.
```

or a separate line only if clearer:

```markdown
**Status:** Done

**Shipped in:** `0.2.0`
```

Prefer one compact **Status** line. No dates, estimates, or sprint labels.

## Placement

Put **Status** immediately under the entry `##` title (before **Domain**), matching
existing Done entries in this repo.
