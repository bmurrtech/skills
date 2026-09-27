---
name: handoff
description: >
  Throwaway handoff: compact the conversation for a fresh agent under the OS
  temp dir; when the user says keep (or clear persist intent), write under
  .scratch/handoffs/ with a date-prefixed filename. Use when switching
  sessions, before muddy ADR/PRD authoring, or when the user asks for a
  handoff.
disable-model-invocation: true
---

# handoff

Write a **throwaway** handoff so another agent can continue without this chat.
Default destination is the OS temp dir (not the workspace). Persist only on an
explicit **keep** signal.

## Boundaries

- Do **not** write a transitory handoff into the repo (`docs/`, `pm/`, `skills/`,
  or `.scratch/`).
- Do **not** write a **keep** handoff anywhere except
  `.scratch/handoffs/{yyyyMMdd-HHmmss}-handoff.md`.
- Do **not** paste specs, plans, ADRs, issues, commits, or diffs — **reference**
  by path/URL.
- Do **not** include secrets, tokens, passwords, or PII.

## Workflow

### 1. Classify destination

**keep** when the invoke prompt says *keep* or clearly asks to persist /
retain (not throwaway). Otherwise temp.

| Signal | Destination |
|--------|-------------|
| Absent (default) | `{tmpdir}/bmurrtech-skills-handoff-{yyyyMMdd-HHmmss}.md` |
| **keep** | `.scratch/handoffs/{yyyyMMdd-HHmmss}-handoff.md` (create dirs if missing) |

If ambiguous → ask once; default remains temp.

**Done when:** destination path chosen.

### 2. Draft contents

Include:

- Goal / current position (short)
- Settled decisions (link ADRs/PRDs/CONTEXT)
- Open frontier / next questions
- Artifacts touched (paths only)
- **Suggested skills** to invoke next (names only)
- If the user passed a focus argument, tailor the next-session section to it

**Done when:** draft covers every bullet above (or N/A noted).

### 3. Write + report

Write the file to the path from step 1. Tell the user the absolute path and
whether it was **throwaway** (temp) or **kept** (`.scratch/handoffs/`).

**Done when:** file exists at that path and the path was reported.
