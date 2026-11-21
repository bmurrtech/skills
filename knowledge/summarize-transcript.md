---
title: Summarize transcript
description: Test map for summarize-transcript assess_size / chunk_transcript seams and e2e fixture pipeline.
type: test-map
tags: [tests, summarize-transcript, tdd]
---

# Summarize transcript

**Seam:** `assess_size.assess` / `strategy_hint` / CLI; `chunk_transcript.split_units` /
`chunk_units` / `split_oversized_unit` / CLI; e2e assess→chunk on
`tests/fixtures/summarize_transcript/game_idea_research.txt`.

**Run:**

```bash
python3 -m unittest tests.test_summarize_transcript -v
```

**Tracked tests:** `tests/test_summarize_transcript.py`  
**Fixture:** `tests/fixtures/summarize_transcript/game_idea_research.txt`

Dry-run scratch (ignored): `.scratch/summarize-transcript/<run-id>/`.
