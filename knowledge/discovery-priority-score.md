---
title: Discovery priority score
description: Test map for discovery priority_score.py (KPFS → BV, DR, Overall, P0–P3, rank).
type: test-map
tags: [tests, discovery, tdd]
---

# Discovery priority score

**Seam:** `skills/discovery/scripts/priority_score.py`

## Run

```bash
python3 -m unittest tests.test_discovery_priority_score -v
```

## Contract

- Input: JSON `{ "use_cases": [ { id, K, P, F, S, ...extra } ] }`; bands int 1–3 or `null` (absent = `null`)
- Scored: `BV = (K+P)/6×100`, `DR = (F+S)/6×100`, `Overall = 0.4·BV + 0.6·DR` (exact rationals; one-decimal output)
- Labels: P0 ≥ 80 · P1 ≥ 65 · P2 ≥ 50 · P3 < 50
- Any `null` → `unscored`: priority `none`, status `needs-discovery`, `missing` dims
- Sort: label → Overall desc → S desc → id; `rank` 1..n on scored only
- Invalid band / id / duplicate id / envelope → exit 1, message on stderr
- Coverage: all 81 band combos vs an independent exact model; reference K3 P3 F2 S3 → 90.0 P0

## Related

- [discovery](discovery.md)
- [Skill scripts vs LLM](skill-scripts.md)
