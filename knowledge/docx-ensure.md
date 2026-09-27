---
title: Docx ensure
description: Test map for ToolchainReady, docx asset names, committed digests, LibreOffice hints, and probe-only ensure.
type: test-map
tags: [tests, docx, tdd]
---

# Docx ensure

**Seam:** `toolchain_ready.assess` (pin + office ready); `ensure_docx.load_digests` /
`expected_digest` / `asset_name` / `ensure(which=…)` / `manual_install_hint`;
`ensure_office.libreoffice_install_plan` / `manual_install_hint` / `ensure(probe=…, run=…)`.

**Run:**

```bash
python3 -m unittest tests.test_docx_ensure -v
```

**Tracked tests:** `tests/test_docx_ensure.py`

Operator install (not agent): [docs/how-to-docx-cli.md](../docs/how-to-docx-cli.md).
Scratch smokes after manual CLI install: `.scratch/docx-smoke/`.
