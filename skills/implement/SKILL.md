---
name: implement
description: >
  Implement work from a spec or tickets: prefer tdd at agreed seams, run the
  target repo's checks, soft housekeeping, then exit via fresh-context review
  (subagent code-review or handoff for code-review). Never owns Git — use commit.
  Use when building features or fixing bugs after design clarity.
disable-model-invocation: true
---

# implement

Ship the requested change in the **current** (consumer) repo. Prefer **`tdd`** at
pre-agreed seams when code applies. Own build + soft housekeeping only — review
is a **fresh-context exit**; Git publish belongs to **`commit`** / **`merge`** /
**`release`**.

## Workflow

### 1. Clarify inputs

Locate the acceptance target, in order:

1. Tickets / issue refs the user named
2. Path the user passed (PRD, design doc, paste, handoff)
3. Discovery if present: `docs/prd/`, `docs/`, `specs/`, `.scratch/`
4. User paste / this chat

If scope is still a design tree with open frontier, **suggest** **`grill-me`**
(or **`to-prd`** when they want a written PRD) — do not hard-gate every ticket.

If design cracks mid-build, **soft-suggest** a **new-session** **`grill-me`** or
**`handoff`** (operator brings prior context manually). Do **not** auto-run
**`grill-me`** in this chat. If unclear whether to stop vs continue the current
slice, ask once; default continue only when acceptance for that slice stays clear.

**Done when:** acceptance target is clear.

### 2. Seams + TDD

If code/tests apply: agree seams with the user, then follow **`tdd`** (red →
green, vertical slices).

**Done when:** agreed checks pass for the slice set (or TDD skipped because no
code seam applies).

### 3. Validate (target repo)

Run **this repo’s** real checks from evidence — `AGENTS.md`, package scripts, CI
config — typecheck / unit / lint as applicable.

Optional: *if* the change touched Agent Skills under a `skills/` tree **and** a
validator exists in this repo, run it. Never treat skill validation as the
primary success path for ordinary app/lib work.

**Done when:** relevant target-repo checks exit 0 (or none apply, noted).

### 4. Housekeeping (if applicable)

If **`upkeep`** / **`context`** are installed **and** the target artifacts exist
(`AGENTS.md`, `CONTEXT.md` / `knowledge/`, or the user follows those
conventions): run **`upkeep`** then **`context`**.

Otherwise skip with a one-line note. Do not fail an implement because
glossary/ops files are missing.

If an ADR-worthy decision appeared and **`to-adr`** is available, offer it (or
note for later).

**Done when:** housekeeping applied or explicitly skipped.

### 5. Review exit (context boundary)

Prefer a real context boundary — never same-agent inline **`code-review`**.

1. If the harness can spawn subagents → run **`code-review`** as a **subagent**;
   report the verdict; do **not** also write a handoff unless the user asks.
2. Else → invoke **`handoff`** with aim **code-review** / kind **`cd-rvw`**
   (no aim-ask beat), write + glance, **stop** for a fresh agent.

Ask for a fixed point when missing (subagent path), or record `none` + working-tree
scope in the **code-review (`cd-rvw`)** kind block.

**Done when:** subagent review reported, or code-review (`cd-rvw`) handoff written
and session stopped for review.

### 6. Git ban (hard)

Never stage, never commit, never push, never open/update a PR, never
force-align branches — even if the prompt says “and push to main.”

Name **`commit`** (and the how-to git lifecycle) for later user intent. Local /
push+PR / canonical publish are **`commit`** modes only.

**Done when:** no Git publish actions taken; operator knows to run **`commit`**
when ready.
