#!/usr/bin/env python3
"""Façade: probe pinned docx-cli then Word/LibreOffice host.

Delegates to ensure_docx + ensure_office (does not fuse their implementations).
Prints ToolchainReady evidence; exit 0 only when ready.
Never downloads docx-cli or auto-installs an office host — operators install
via docs/how-to-docx-cli.md, then re-run.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent


def _load(name: str):
    mod_name = f"_docx_skill_{name}"
    if mod_name in sys.modules:
        return sys.modules[mod_name]
    path = _SCRIPTS / f"{name}.py"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Probe docx-cli pin + office host (façade over ensure_docx / ensure_office)."
    )
    parser.parse_args(argv)

    ensure_docx = _load("ensure_docx")
    ensure_office = _load("ensure_office")
    ready_mod = _load("toolchain_ready")

    docx_err = ensure_docx.ensure()
    if docx_err:
        print(docx_err, file=sys.stderr)
    docx_rc = 1 if docx_err else 0

    office_rc = ensure_office.ensure()

    report = ready_mod.snapshot(pin=ensure_docx.PIN)
    print(ready_mod.format_report(report))
    if not report.ready:
        for err in report.errors:
            print(err, file=sys.stderr)
        return 1
    if docx_rc != 0 or office_rc != 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
