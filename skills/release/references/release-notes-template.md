# Release notes template

Read when composing GitHub Release notes (after CHANGELOG verify) or when
scaffolding a tag-triggered workflow that owns `gh release create`.

## Preferred path (deterministic)

Prefer the extractor over hand-written stubs:

```bash
python3 scripts/changelog_release_notes.py \
  --version <semver> \
  --repo-root . \
  --extra-note "<optional install / artifact blurb>"
```

**SoT:** [`../scripts/changelog_release_notes.py`](../scripts/changelog_release_notes.py)
(shipped with **`release`**). This library’s dogfood workflow calls that path
under `skills/release/scripts/` directly.

**Bootstrap:** copy the skill script → consumer `scripts/changelog_release_notes.py`,
then wire `gh release create` with `--notes "$(…)"` as above.

**CTA footer:** script reads `.github/FUNDING.yml` first; if empty/missing, falls
back to Ko-fi / Buy Me a Coffee URLs in `CONTEXT.md`; otherwise omits the
footer. Use `--no-cta` only when the operator explicitly wants a bare body.

Dogfood: `.github/workflows/release.yml` (ADR 0005 artifact blurb via
`--extra-note`). Path decision: [ADR 0015](../../../docs/adr/0015-ADR-donation-cta-changelog-release-notes.md).

## Manual shape (fallback)

When the extractor is unavailable, approximate:

```markdown
## [<version>] - YYYY-MM-DD

(paste the matching CHANGELOG section body)

## Install / artifacts
- …

## Support
- (omit if no Donation CTA / FUNDING.yml)
```

Prefer CHANGELOG section as SoT; template adds install/artifact pointers and
Donation CTA when funding context exists.
_Avoid_: hardcoded stub bodies that ignore CHANGELOG.
