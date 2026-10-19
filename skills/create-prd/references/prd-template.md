# PRD template (OKF concept)

```markdown
---
title: {short title}
description: {one-sentence what this MVP enables}
type: prd
tags: [prd, mvp]
---

# {Short title}

<!-- File: docs/prd/NNNN-PRD-<slug>.md -->

## 0) Summary
- **One-liner:** …
- **MVP User Journey:** …
- **ADR References:**
  - [docs/adr/NNNN-ADR-….md](../../adr/NNNN-ADR-….md) — …

## 1) Goal
…

## 2) System Diagrams
(At least one fenced diagram via ascii)

## 3) Scope
### 3.1 In Scope (MVP only)
### 3.2 Out of Scope
### 3.3 Non-goals

## 4) User Journey (MVP)
### UJ-1: …
### Critical failure handling

## 5) Functional Requirements (MVP)
Behavioral only; each FR supports UJ-1; implementation-agnostic.

### FR-1: …
**Behavior** / **Edge handling** / **Dependencies** / **Status:** Planned | Implemented | Dropped (see NNN-BUG-slug)

## 6) Phases (order only, no dates)
### Phase A / B / C

## 7) Definition of Done (DoD)
3–6 ship-focused bullets for the master PRD.

## 8) Implementation Standards (binding, lightweight)
KISS, YAGNI, DRY, SoC, fail fast, SoT, explicit over implicit.
Security: no hardcoded secrets; respect .gitignore; never log secrets.
Deviations need Why / Impact / Mitigation.

## 9) Bug Appendix
### 001-BUG-short-title
Status / Symptoms / Repro / Hypothesis / Fix (when Resolved)

## 10) References
Key files, symbols, docs — paths only.
```
