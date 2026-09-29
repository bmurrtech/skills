# Branch policy

Read when mode is **review publish** (step 2).

## Naming

```text
<type>/<short-slug>
```

Short, scannable, two–three meaningful terms. Avoid sentence-length names.

Examples: `fix/tag-check` `docs/release` `feat/merge-flow`.

## Reuse

Reuse an existing branch only when all hold:

- same base
- same logical workstream
- open PR still applicable (when one exists)
- new work does not materially broaden the PR
- branch not already merged/closed

Otherwise create a new short-lived branch. Prefer cleanup after **`merge`** over
catch-all long-lived branches.
