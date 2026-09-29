# Release bootstrap

Read when step 2 applies (no release workflow).

## Confidence

| Level | Action |
|-------|--------|
| High | Explicit docs or package script; verify locally; scaffold thin `release.yml` that **calls the same command**; stop — no tag this run |
| Medium | Obvious ecosystem, unclear packaging; propose contract; no matrices/signing/registries |
| Low | Ambiguous/monorepo/signing/multi-system → concise gap report; stop |

## Thin workflow

Scaffold minimal tag-triggered workflow that:

- triggers on `v*` (or repo-equivalent)
- checks out, sets up toolchain as needed
- runs the **same** local release/package command
- creates GitHub Release / attaches artifacts as the repo already intends

Do not embed one-off language recipes that diverge from the local command.

## After scaffold

Hand workflow + any supporting files to **`commit`** (PR when policy requires).
Stop. Operator merges infrastructure, then invokes **`release`** again to tag.
