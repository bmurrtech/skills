---
title: Check slides
description: Test map for visual-explainer slide deck structural checker.
type: test-map
tags: [tests, visual-explainer, slides]
---

# Check slides (test map)

## Seam

`skills/visual-explainer/scripts/check_slides.py` public contract: fail closed on
missing shell marker, missing `data-screen-label`, empty action titles, missing
type-floor CSS tokens, and unresolved overflow markers.

## Run

```bash
python3 -m unittest tests.test_check_slides -v
```

## Tests

- `tests/test_check_slides.py`

## Related

- Glossary: [Deck shell](../CONTEXT.md), [Action-title outline](../CONTEXT.md)
- Skill: `skills/visual-explainer/`
