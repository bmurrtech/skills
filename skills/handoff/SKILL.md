---
name: handoff
description: >
  Compact the conversation into a handoff doc for a fresh agent. Saves under the
  OS temp dir as bmurrtech-skills-handoff-*.md. Use when switching sessions,
  before muddy ADR/PRD authoring, or when the user asks for a handoff.
disable-model-invocation: true
---

# handoff

Write a handoff so another agent can continue without this chat.

## Output path

Save **outside the workspace** in the OS temp directory:

`{tmpdir}/bmurrtech-skills-handoff-{yyyyMMdd-HHmmss}.md`

Never write handoffs into the repo (not under `docs/`, `pm/`, or skills).

## Contents

- Goal / current position (short)
- Settled decisions (link ADRs/PRDs/CONTEXT — do not paste them)
- Open frontier / next questions
- Artifacts touched (paths only)
- **Suggested skills** to invoke next (names only)
- If the user passed a focus argument, tailor the next-session section to it

## Rules

- Do not duplicate specs, plans, ADRs, issues, commits, or diffs — **reference** by path/URL
- Redact secrets, tokens, passwords, and PII
- Tell the user the absolute path written

**Done when:** file exists at the temp path and the path was reported.
