---
title: Test map
description: OKF concept that maps a seam to the smallest tracked test run for session-scoped TDD.
type: concept
tags: [tests, okf, tdd]
---

# Test map

A **test map** is an OKF concept under `knowledge/` (prefer frontmatter `type: test-map`) that names:

1. The **seam** / capability under test
2. The **smallest run command** for that slice
3. The **tracked** test file paths (usually under `tests/`)

## Why

Full suites grow (hundreds of tests). Agents should not load or narrate the entire tree mid-session. Instead:

1. `AGENTS.md` → Testing → **Test index** holds one-liners
2. Each line points at a test-map OKF file
3. **`tdd`** opens only maps for the agreed seams, runs those commands, full suite once at the end

## Ownership

- OKF body: **`context`** / **`tdd`**
- AGENTS one-liner: **`tdd`** / **`upkeep`**
- Test source files: tracked in VCS (regressions). Throwaway dumps: `.scratch/`, not `tests/`.

## Related

- Glossary: [CONTEXT.md](../CONTEXT.md)
- Skill: [`skills/tdd`](../skills/tdd/SKILL.md)
