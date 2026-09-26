---
name: tdd
description: >
  Red-green TDD at pre-agreed seams: behavior through public interfaces, vertical
  slices, no implementation-coupled or tautological tests. Use when implementing
  with tests first, agreeing seams, or checking test quality.
disable-model-invocation: true
---

# tdd

Red → green loop that keeps tests worth keeping. If `CONTEXT.md` is present, read it so names match domain language; respect ADRs in the area you touch when those exist.

## Seams first

A **seam** is the public boundary you test at. **No test at an unconfirmed seam.**

Before any test, list the seams and confirm with the user.

**Done when:** seam list is agreed (or user confirms no code seam applies).

## What a good test is

- Verifies **behavior** through public interfaces, not internals
- Reads like a specification (“user can checkout with valid cart”)
- Survives refactors of private structure
- Expected values from an independent source of truth (literals, worked examples, spec) — never recomputed the same way as the code

## Anti-patterns

- **Implementation-coupled** — mocks internals, private methods, or side-channel DB peeks
- **Tautological** — assertion rebuilds the implementation’s formula
- **Horizontal slicing** — all tests then all code; prefer **vertical slices** (one test → one minimal implementation → repeat)

## Loop rules

1. **Red before green** — failing test first; only enough code to pass
2. **One slice at a time** — one seam, one test, one minimal fix
3. **Refactor out of band** — belongs to review (`code-review`), not the red→green cycle

## After implement

When used under **`implement`**, keep running the smallest relevant checks from the **target** repo; full suite once at the end of the change set.
