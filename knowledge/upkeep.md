---
title: upkeep
description: Skill and practice for maintaining AGENTS.md, CLAUDE.md pointer, and CHANGELOG.md.
type: concept
tags: [agents, upkeep, changelog]
---

# upkeep

**upkeep** keeps the agent operating manual and release notes accurate.

## Owns

- [`AGENTS.md`](../AGENTS.md) — structure, commands, boundaries, verification
- [`CLAUDE.md`](../CLAUDE.md) — body must be exactly `AGENTS.md` (create if missing)
- [`CHANGELOG.md`](../CHANGELOG.md) — Keep a Changelog; ensure file exists; keep `## [Unreleased]` current after implement/code-review; **release-cut** promotes Unreleased → dated when `release_intent` + confirmed version

## Does not own

- [`CONTEXT.md`](../CONTEXT.md) or [`knowledge/`](index.md) — those belong to **context**
- Inventing a SemVer bump without release context — consume authorized version only

## When

Run after [`implement`](../skills/implement/SKILL.md) and [`code-review`](../skills/code-review/SKILL.md), when **`commit`** orchestrates maintenance, and whenever repo layout, checks, workflows, or boundaries change.

## Changelog rules

See skill [references/release-cut.md](../skills/upkeep/references/release-cut.md)
and [commit maintenance](../skills/commit/references/maintenance.md). Summary:
ordinary = Unreleased honesty; release-cut = promote only with authorized
version; missing CHANGELOG under `release_intent` hard-stops unless waived.

## Related

- Skill: [`skills/upkeep`](../skills/upkeep/SKILL.md)
- Glossary: [Release context](../CONTEXT.md), [Version gate](../CONTEXT.md)
