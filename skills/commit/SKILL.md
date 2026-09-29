---
name: commit
description: >
  Local-first Git commit; on push intent, review branch + PR; on explicit
  canonical intent, direct push. Use when the user asks to commit, checkpoint,
  push, publish, or open/update a PR.
disable-model-invocation: true
---

# commit

Make work durable locally. Publish only when intent is explicit. Owns staging,
commit message, branch naming/reuse, push, and PR create/update — not merge or
release (invoke **`merge`** / **`release`** when those are the ask).

## Intent

| Signal | Mode |
|--------|------|
| commit / checkpoint / save to git (no push words) | **Local only** |
| push / publish / raise a PR / send this up / commit and push | **Review publish** |
| push to main / directly to master / straight to \<canonical\> | **Canonical override** |

Honor explicit overrides when stated: target base, branch name, or PR number to
update. Ask once if mode or overrides are ambiguous.

**Done when:** mode (+ any overrides) chosen from user words.

## Workflow

### 1. Inspect

Read `git status`, `git diff`, `git branch -vv`, and recent `git log`. Identify
canonical base (usually `main`/`master`). If secrets/credentials/`.env` appear
in the intended diff, or the stage set is ambiguous / mixes unrelated work →
**stop**; preserve state; report. Do not commit.

**Done when:** intended paths are clear and safe, or stopped with reason.

### 2. Branch (review publish only)

If mode is **review publish** and HEAD is canonical (or otherwise needs a
workstream branch), create or reuse a short `type/slug` branch per
[references/branch-policy.md](references/branch-policy.md). Skip for **local
only** and for **canonical override**.

**Done when:** on the correct branch for the mode, or skipped.

### 3. Stage and commit

Stage only relevant paths. Message: conventional
`<type>[optional scope][optional !]: <short description>` — see
[references/commit-conventions.md](references/commit-conventions.md). Commit on
the current branch.

**Done when:** commit exists; working tree clean for intended paths (or leftover
unrelated paths reported and left unstaged).

### 4. Publish (skip if local only)

**Review publish:** Push the branch. Create or update **one** PR for that head
(never a duplicate; honor explicit PR number when given). PR body: what / why /
validation / risks.

**Canonical override:** Push the requested branch. If protection rejects:
report; do not bypass; fall back to review-publish (step 2 onward).

**Done when:** local-only stopped after step 3; else remote branch + PR URL (or
successful canonical push) reported.

## Boundaries

- Do not push, create a branch, or open a PR without matching intent.
- Do not create a branch solely because HEAD is canonical when mode is local only.
- Do not commit when secrets are in the intended diff or staging is ambiguous.
- Never `git push --force`, `git reset --hard`, or `git clean -fd` as routine.
- Never commit secrets or ignored credential files.
- Do not implement merge or release flows here — name **`merge`** / **`release`**.
