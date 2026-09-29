---
name: release
description: >
  Cut a versioned release: discover repo contract, version gate, prep via
  commit, build before tag, publication gate, push one annotated v* tag, verify
  GitHub Release. Use when the user asks to release, cut a version, tag a
  release, or bootstrap missing release CI.
disable-model-invocation: true
---

# release

Prove the canonical version builds, then deliberately publish it. Owns version
and channel intent, **version gate**, **publication gate**, local validation,
tagging, and verification — not routine commits/PRs (**`commit`**) or PR
integration (**`merge`**, only when prep must enter via PR). Does **not** mutate
CHANGELOG — that is **`upkeep`** (via **`commit`** with release context).

Invariant: **build before tag**. Session Unreleased hygiene and Unreleased →
dated promotion are **`upkeep`**; this skill authorizes the cut and tags.

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

### 3. Version gate

Authorize version **and** channel before prep. Rules and recommendation:
[references/version-gate.md](references/version-gate.md).

Build structured **release context** after authorization — field schema in
[references/version-gate.md](references/version-gate.md).

**Done when:** version + channel authorized; release context ready.

### 4. Prepare via commit

Pass release context into **`commit`** (prep). `commit` orchestrates
**`upkeep`** release-cut and conditional **`roadmap` status** — do not promote
CHANGELOG here. Invoke **`merge`** only when policy requires PR into the
release branch. Identify canonical release SHA after prep lands.

Compose release notes from the dated CHANGELOG section (after upkeep) +
[references/release-notes-template.md](references/release-notes-template.md).

**Done when:** release commit SHA known; CHANGELOG dated on that commit (or
hard-stop / waive recorded).

### 5. Validate locally

Run repo-required tests, then the release build command, then artifact checks
where applicable ([references/local-build.md](references/local-build.md)).
Docker only if the contract requires it.

On failure → **do not tag**. Fix via ordinary change flow; resume later.

**Done when:** local validation passed for this SHA.

### 6. Publication gate → tag → verify

Confirm exact tag + SHA + validation per
[references/publication-gate.md](references/publication-gate.md). Affirmative
enough after version was authorized.

Then create **annotated** tag `v…`; push **only that tag** (never
`git push --tags` as normal). Observe the release workflow; verify GitHub
Release + expected artifacts.

Pushed tags are **immutable** — never move/delete/recreate; cut a new version.

**Done when:** publication authorized; tag pushed; release verified (or workflow
failure reported without retagging).

## Boundaries

- Do not treat ordinary branch pushes as releases.
- Do not scaffold workflow and tag in the same first bootstrap operation.
- Do not invent registry publish (npm/PyPI/crates/Docker).
- Never force-move release tags; never embed secrets in workflows/scripts.
- Do not silently choose version or channel.
- Do not tag or push without publication-gate authorization.
- Do not promote Unreleased → dated CHANGELOG here — name **`upkeep`** via
  **`commit`**.
- Do not duplicate **`commit`** / **`upkeep`** / **`roadmap`** bodies.
