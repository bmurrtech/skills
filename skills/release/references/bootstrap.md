# Release bootstrap

Read when step 2 applies (no release workflow).

## Confidence

| Level | Action |
|-------|--------|
| High | Explicit docs or package script; verify locally; scaffold thin `release.yml` that **calls the same command**; stop — no tag this run |
| Medium | Obvious ecosystem, unclear packaging; propose contract; no matrices/signing/registries |
| Low | Ambiguous/monorepo/signing/multi-system → concise gap report; stop |

## Thin workflow

Scaffold minimal tag-triggered workflow that:

- triggers on `v*` (or repo-equivalent)
- checks out, sets up toolchain as needed
- runs the **same** local release/package command
- creates GitHub Release / attaches artifacts as the repo already intends
- builds release notes via CHANGELOG extract (not a hardcoded stub)
- for SemVer pre-release versions (`X.Y.Z-<id>`, e.g. `-rcN`), pass
  `gh release create --prerelease --latest=false` so GitHub **Latest** stays on
  the newest stable release

Do not embed one-off language recipes that diverge from the local command.

## Release notes + CTA

1. Copy SoT [`../scripts/changelog_release_notes.py`](../scripts/changelog_release_notes.py)
   → consumer `scripts/changelog_release_notes.py` (one file; no library-ops twin).
2. In the workflow’s `gh release create` step, set notes from:

   ```bash
   NOTES="$(python3 scripts/changelog_release_notes.py \
     --version "$VERSION" \
     --repo-root . \
     --extra-note "<optional install / artifact blurb>")"
   ```

   (This library dogfoods `python3 skills/release/scripts/changelog_release_notes.py`
   instead of maintaining a second copy under repo `scripts/`.)

3. CTA footer is automatic when `.github/FUNDING.yml` (or CONTEXT URLs) exist —
   see [release-notes-template.md](release-notes-template.md). Do not invent
   donation links during bootstrap; that is **`setup-bmurrtech-skills`**
   Donation CTA opt-in.

## After scaffold

Hand workflow + any supporting files to **`commit`** (PR when policy requires).
Stop. Operator merges infrastructure, then invokes **`release`** again to tag.
