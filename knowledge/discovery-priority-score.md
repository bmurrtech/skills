---
title: Discovery priority score
description: Test map for discovery priority_score.py (V, P-level, N, rank).
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

- Input: JSON `{ "candidates": [ { id, K, P, F, S, confidence?, gate? } ] }`
- Scored: `V = K+P`; P1–P4 from V≥7 / F≥4 quadrant; `N = 5K+5P+6F+4S`
- Gated candidates get status, no P-level
- Rank: P-level then N; near-tie when |ΔN| ≤ 5 within a P-level

## Related

- [discovery](discovery.md)
- [Skill scripts vs LLM](skill-scripts.md)
