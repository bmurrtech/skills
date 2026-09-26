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
- [`CHANGELOG.md`](../CHANGELOG.md) — Keep a Changelog; ensure file exists; keep `## [Unreleased]` current after implement/code-review

## Does not own

- [`CONTEXT.md`](../CONTEXT.md) or [`knowledge/`](index.md) — those belong to **context**
- Version bumps / moving Unreleased into a dated release — only when the user is cutting a release

## When

Run after [`implement`](../skills/implement/SKILL.md) and [`code-review`](../skills/code-review/SKILL.md), and whenever repo layout, checks, workflows, or boundaries change.

## Changelog rules

1. Missing `CHANGELOG.md` → create stub with Unreleased.
2. After implement/review → add missing Unreleased bullets for notable session changes.
3. Do not invent SemVer tags in the changelog unless releasing.

## Related

- Skill: [`skills/upkeep`](../skills/upkeep/SKILL.md)
