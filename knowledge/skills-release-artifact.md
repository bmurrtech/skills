---
title: Skills release artifact
description: Filtered install tarball of skills/ + LICENSE; library OKF stays in git only.
type: concept
tags: [skills, release, packaging]
---

# Skills release artifact

The **skills release artifact** is the versioned tarball installers download. It is built from a tagged commit but **filtered** — not a full-repo snapshot.

## Include

- `LICENSE`
- `skills/**` (skill folders and their bundles)

## Exclude (tracked in git, never shipped)

- `knowledge/`, `CONTEXT.md` — library OKF (ADR 0002)
- `AGENTS.md`, `CLAUDE.md` — library ops
- `docs/`, README, CHANGELOG, `scripts/`, `tests/`, integrations, local agent dirs

## Why not gitignore knowledge/

Consumer cleanliness is a **packaging** concern. Library maintainers still need the OKF in the source repo. See [ADR 0005](../docs/adr/0005-ADR-skills-release-artifact.md).

## Related

- Glossary: [CONTEXT.md](../CONTEXT.md)
- Packager: [`scripts/package_skills.py`](../scripts/package_skills.py)
- Test map: [package-skills.md](package-skills.md)
