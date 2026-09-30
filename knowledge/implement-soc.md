---
title: Implement SoC
description: Seam map for implement skill review-exit and hard Git-ban content contract.
type: test-map
tags: [tests, implement, soc, review, git]
---

# Implement SoC (test map)

## Seam

`skills/implement/SKILL.md` public instruction contract: hard Git ban (never stage/commit/push/PR/force-align); review exit via subagent or code-review (`cd-rvw`) handoff with affirmative never same-agent inline; housekeeping before review; soft new-session grill re-open; points operators at `commit`. CI/AGENTS bulk unittest lists include `tests.test_implement_soc`.

## Run

```bash
python3 -m unittest tests.test_implement_soc -v
```

Also (frontmatter/layout):

```bash
python3 scripts/quick_validate.py skills/implement
```

## Tests

- `tests/test_implement_soc.py`

## Related

- Local PRD: `docs/prd/0002-PRD-implement-review-git-soc.md`
- ADR: [0012-ADR-handoff-hybrid-kinds.md](../docs/adr/0012-ADR-handoff-hybrid-kinds.md)
