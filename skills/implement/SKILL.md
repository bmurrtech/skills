---
name: implement
description: >
  Implement work from a spec or tickets: prefer tdd at agreed seams, run the
  target repo's checks, then code-review. Use when building features or fixing
  bugs after design clarity.
disable-model-invocation: true
---

# implement

Ship the requested change in the **current** (consumer) repo. Prefer **`tdd`** at pre-agreed seams when code applies.

## Workflow

### 1. Clarify inputs

Locate the acceptance target, in order:

1. Tickets / issue refs the user named
2. Path the user passed (PRD, design doc, paste, handoff)
3. Discovery if present: `docs/prd/`, `docs/`, `specs/`, `.scratch/`
4. User paste / this chat

If scope is still a design tree with open frontier, **suggest** **`grill-me`** (or **`to-prd`** when they want a written PRD) — do not hard-gate every ticket.

**Done when:** acceptance target is clear.

### 2. Seams + TDD

If code/tests apply: agree seams with the user, then follow **`tdd`** (red → green, vertical slices).

**Done when:** agreed checks pass for the slice set (or TDD skipped because no code seam applies).

### 3. Validate (target repo)

Run **this repo’s** real checks from evidence — `AGENTS.md`, package scripts, CI config — typecheck / unit / lint as applicable.

Optional: *if* the change touched Agent Skills under a `skills/` tree **and** a validator exists in this repo, run it. Never treat skill validation as the primary success path for ordinary app/lib work.

**Done when:** relevant target-repo checks exit 0 (or none apply, noted).

### 4. Housekeeping (if applicable)

If **`upkeep`** / **`context`** are installed **and** the target artifacts exist (`AGENTS.md`, `CONTEXT.md` / `knowledge/`, or the user follows those conventions): run **`upkeep`** then **`context`**.

Otherwise skip with a one-line note. Do not fail an implement because glossary/ops files are missing.

If an ADR-worthy decision appeared and **`to-adr`** is available, offer it (or note for later).

**Done when:** housekeeping applied or explicitly skipped.

### 5. Review

Run **`code-review`** on the change (ask for fixed point if missing).

**Done when:** review reported (or user skipped explicitly).

Commit only if the user asked.
