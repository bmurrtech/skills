---
title: Changelog release notes
description: Seam map for CHANGELOG extract + Donation CTA footer used by release CI.
type: test-map
tags: [tests, release, changelog, funding]
---

# Changelog release notes (test map)

## Seam

`skills/release/scripts/changelog_release_notes.py` — extract dated CHANGELOG
section; append optional artifact blurb; CTA footer from `.github/FUNDING.yml`
or CONTEXT URL fallback. Single SoT (no repo-`scripts/` twin).

## Run

```bash
python3 -m unittest tests.test_changelog_release_notes -v
```

## Tests

- `tests/test_changelog_release_notes.py`

## Related

- ADR: [0015-ADR-donation-cta-changelog-release-notes.md](../docs/adr/0015-ADR-donation-cta-changelog-release-notes.md)
- Glossary: Donation CTA / FUNDING.yml / Release notes (CHANGELOG extract)
