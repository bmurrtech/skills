---
title: Package skills
description: Seam map for filtered skills release tarball include/exclude contract.
type: test-map
tags: [tests, packaging, release]
---

# Package skills (test map)

## Seam

`scripts/package_skills.py` public contract: release members and tarball contain `skills/` + `LICENSE` only; library OKF/ops/docs excluded.

## Run

```bash
python3 -m unittest tests.test_package_skills -v
```

## Tests

- `tests/test_package_skills.py`

## Related

- Concept: [skills-release-artifact.md](skills-release-artifact.md)
- ADR: [0005-ADR-skills-release-artifact.md](../docs/adr/0005-ADR-skills-release-artifact.md)
