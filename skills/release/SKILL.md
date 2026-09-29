---
name: release
description: >
  Cut a versioned release: discover repo contract, build before tag, push one
  annotated v* tag, verify GitHub Release. Use when the user asks to release,
  cut a version, tag a release, or bootstrap missing release CI.
disable-model-invocation: true
---

# release

Prove the canonical version builds, then deliberately publish it. Owns version
choice, CHANGELOG promotion for the cut, local validation, tagging, and
verification — not routine commits/PRs (**`commit`**) or PR integration
(**`merge`**, only when prep must enter via PR).

Invariant: **build before tag**. Session Unreleased hygiene is **`upkeep`**;
this skill only promotes Unreleased → dated version for the cut.

## Workflow

### 1. Discover contract

Progressive disclosure — do **not** recursively ingest the repo up front.
**Existing repository release contracts outrank ecosystem defaults.** Follow
[references/discovery.md](references/discovery.md) (ladder, dogfood fixtures,
decision tree). Manifests are hints, not recipes.

**Done when:** contract path classified: *existing workflow* | *bootstrap* |
*gap report*.

### 2. Bootstrap path (only if workflow missing)

States: `DISCOVER` → `BOOTSTRAP_REQUIRED` → `LOCAL_CONTRACT_VERIFIED` →
`WORKFLOW_SCAFFOLDED` → **`commit`**/PR → (later) release again.

Confidence gates and thin-workflow rules:
[references/bootstrap.md](references/bootstrap.md).

**Done when:** scaffolded+handed to **`commit`**, or stopped with plan/gaps.

### 3. Prepare version + CHANGELOG

Determine version (`vMAJOR.MINOR.PATCH` or prerelease). Promote Unreleased →
dated `## [X.Y.Z…]`; leave empty Unreleased. Compose notes from that section +
[references/release-notes-template.md](references/release-notes-template.md).

If prep creates source changes → invoke **`commit`** (and **`merge`** only when
policy requires PR into the release branch). Identify canonical release SHA.

**Done when:** version + release commit SHA known; CHANGELOG promoted on that
commit (or no CHANGELOG and noted).

### 4. Validate locally

Run repo-required tests, then the release build command, then artifact checks
where applicable ([references/local-build.md](references/local-build.md)).
Docker only if the contract requires it.

On failure → **do not tag**. Fix via ordinary change flow; resume later.

**Done when:** local validation passed for this SHA.

### 5. Tag, push, verify

Confirm version, tag, SHA, branch, validation. Create **annotated** tag
`v…`; push **only that tag** (never `git push --tags` as normal). Observe the
release workflow; verify GitHub Release + expected artifacts.

Pushed tags are **immutable** — never move/delete/recreate; cut a new version.

**Done when:** tag pushed; release verified (or workflow failure reported without
retagging).

## Boundaries

- Do not treat ordinary branch pushes as releases.
- Do not scaffold workflow and tag in the same first bootstrap operation.
- Do not invent registry publish (npm/PyPI/crates/Docker).
- Never force-move release tags; never embed secrets in workflows/scripts.
- Do not reimplement **`upkeep`** session Unreleased editing outside the cut.
