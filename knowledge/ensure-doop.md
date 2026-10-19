---
title: Ensure doop
description: Test map for doop checkout identity, live /healthz HTML probes, and stop cmdline safety.
type: test-map
tags: [tests, doop, tdd]
---

# Ensure doop

**Seam:** `is_doop_checkout`, `is_doop_healthz_body` / `is_doop_html_body` /
`probe_doop_live`, `is_expected_bun_dev`, `cmd_ensure` refusal when checkout is not Doop.

**Run:**

```bash
python3 -m unittest tests.test_ensure_doop -v
```

**Tracked tests:** `tests/test_ensure_doop.py`

Skill script: `skills/doop/scripts/ensure_doop.py`. Residual posture: [docs/accepted-risk.md](../docs/accepted-risk.md) / [ADR 0011](../docs/adr/0011-ADR-skill-scanner-posture-prereqs.md).
