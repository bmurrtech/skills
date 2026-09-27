#!/usr/bin/env python3
"""Probe for pinned docx-cli on PATH; print manual install hints on miss.

Public contract: https://github.com/kklimuk/docx-cli/releases
Pin + DIGESTS document the expected operator-installed version (manual verify).
Does not download, fetch release binaries, pipe remote scripts, or install via npx.
Does not install Word/LibreOffice — use ensure_office.py.
Human install: docs/how-to-docx-cli.md (library) / README pointer.
"""

from __future__ import annotations

import argparse
import platform
import shutil
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

PIN = "0.26.0"
TAG = f"v{PIN}"
REPO = "kklimuk/docx-cli"
DIGESTS_PATH = Path(__file__).resolve().with_name("DIGESTS")
HOW_TO = "docs/how-to-docx-cli.md"
HOW_TO_URL = (
    "https://github.com/bmurrtech/skills/blob/main/docs/how-to-docx-cli.md"
)

WhichFn = Callable[[str], str | None]


def asset_name(system: str, machine: str) -> str:
    system = system.lower()
    machine = machine.lower()
    arm = machine in {"arm64", "aarch64"}
    if system == "windows":
        if arm:
            raise ValueError(f"docx-cli {TAG} has no Windows ARM binary")
        return "docx-windows-x64.exe"
    if system == "darwin":
        return "docx-darwin-arm64" if arm else "docx-darwin-x64"
    if system == "linux":
        return "docx-linux-arm64" if arm else "docx-linux-x64"
    raise ValueError(f"unsupported platform {system}/{machine}")


def parse_sums(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        found[parts[-1].lstrip("*")] = parts[0].lower()
    return found


def load_digests(path: Path | None = None) -> dict[str, str]:
    target = path or DIGESTS_PATH
    return parse_sums(target.read_text(encoding="utf-8"))


def expected_digest(name: str, *, digests: dict[str, str] | None = None) -> str:
    table = digests if digests is not None else load_digests()
    digest = table.get(name)
    if not digest:
        raise RuntimeError(f"no committed digest for {name} in {DIGESTS_PATH.name}")
    return digest


def version_of(docx: str) -> str | None:
    try:
        completed = subprocess.run(
            [docx, "--version"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None
    if completed.returncode != 0:
        return None
    parts = completed.stdout.strip().split()
    return parts[-1] if parts else None


def manual_install_hint(
    *,
    system: str | None = None,
    machine: str | None = None,
) -> str:
    """Short OS hints for operators — never executed by this script."""
    lines = [
        f"Install docx-cli {PIN} yourself, then re-run this probe.",
        f"How-to: {HOW_TO} ({HOW_TO_URL})",
        "Quick paths (operator-run only):",
        "  bun add -g bun-docx   # needs Bun >= 1.3; then check docx --version",
        f"  # or standalone from https://github.com/{REPO}/releases/tag/{TAG}",
        f"  # set VERSION={PIN} when using that release's install.sh; verify SHA-256",
        f"  # against scripts/{DIGESTS_PATH.name} (or the release SHA256SUMS)",
    ]
    try:
        name = asset_name(system or platform.system(), machine or platform.machine())
        digest = expected_digest(name)
        lines.append(f"  # this platform asset: {name}  sha256:{digest}")
    except (RuntimeError, ValueError, OSError):
        pass
    return "\n".join(lines)


def ensure(*, which: WhichFn | None = None) -> str | None:
    lookup = which or shutil.which
    current = lookup("docx")
    if current and version_of(current) == PIN:
        print(f"docx {PIN} already on PATH ({current})")
        return None
    found = f" found {current}" if current else ""
    ver = version_of(current) if current else None
    if current and ver:
        found = f" found {current} ({ver})"
    return (
        f"docx {PIN} not ready{found}.\n"
        f"{manual_install_hint()}"
    )


def _load_script(name: str):
    import importlib.util

    mod_name = f"_docx_skill_{name}"
    if mod_name in sys.modules:
        return sys.modules[mod_name]
    path = Path(__file__).resolve().parent / f"{name}.py"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            f"Probe for docx-cli {TAG} on PATH (operator-installed; no download)."
        )
    )
    parser.parse_args(argv)

    err = ensure()
    if err:
        print(err, file=sys.stderr)

    try:
        ready_mod = _load_script("toolchain_ready")
        print(ready_mod.format_report(ready_mod.snapshot(pin=PIN)))
    except (OSError, ImportError, RuntimeError) as exc:
        print(f"toolchain ready report failed: {exc}", file=sys.stderr)

    return 1 if err else 0


if __name__ == "__main__":
    raise SystemExit(main())
