---
title: Writing for humans linter
description: Test map for writing-for-humans measure-only linter (script measures; LLM judges).
type: test-map
tags: [writing-for-humans, test-map]
---

# Writing for humans linter

**Seam:** `skills/writing-for-humans/scripts/writing_for_humans_linter.py`

**Smallest run:**

```bash
python3 -m unittest tests.test_writing_for_humans_linter -v
```

**Tracked tests:** `tests/test_writing_for_humans_linter.py`

Measures sentence length, fillers, indirect patterns, passive heuristics, and
noun-cluster candidates. Emits compact `agent_summary` (`STOP` /
`REVISE_ONCE`) plus `revision_budget`; excludes fences/inline/URLs/ids; does
not rewrite.
