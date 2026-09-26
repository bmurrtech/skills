---
title: Docx ensure
description: Test map for ToolchainReady, docx asset names, LibreOffice plans, and install adapters.
type: test-map
tags: [tests, docx, tdd]
---

# Docx ensure

**Seam:** `toolchain_ready.assess` (pin + office ready); `ensure_docx.asset_name` /
`install_binary(download=…)`; `ensure_office.libreoffice_install_plan` /
`install_libreoffice(run=…)` / `ensure(probe=…)`.

**Run:**

```bash
python3 -m unittest tests.test_docx_ensure -v
```

**Tracked tests:** `tests/test_docx_ensure.py`

Scratch smokes (not tracked): `.scratch/docx-smoke/` after `ensure_docx.py`.
