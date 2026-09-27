#!/usr/bin/env python3
"""Probe for Word/LibreOffice; print manual install hints when missing.

Does not pipe remote scripts. Does not run package managers or sudo.
Does not claim success without a working host.
"""

from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

WhichFn = Callable[[str], str | None]
RunFn = Callable[..., subprocess.CompletedProcess[str]]
ProbeFn = Callable[[], dict[str, str | bool | None]]


def which_any(*names: str, which: WhichFn | None = None) -> str | None:
    lookup = which or shutil.which
    for name in names:
        found = lookup(name)
        if found:
            return found
    return None


def mac_app_soffice() -> Path | None:
    candidates = [
        Path("/Applications/LibreOffice.app/Contents/MacOS/soffice"),
        Path.home() / "Applications/LibreOffice.app/Contents/MacOS/soffice",
    ]
    for path in candidates:
        if path.is_file():
            return path
    return None


def mac_word_present() -> bool:
    return Path("/Applications/Microsoft Word.app").is_dir()


def windows_word_present() -> bool:
    program_files = [
        os.environ.get("ProgramFiles"),
        os.environ.get("ProgramFiles(x86)"),
        os.environ.get("LOCALAPPDATA"),
    ]
    for root in program_files:
        if not root:
            continue
        base = Path(root)
        for pattern in (
            "Microsoft Office*/root/Office*/WINWORD.EXE",
            "Microsoft Office/Office*/WINWORD.EXE",
        ):
            if any(base.glob(pattern)):
                return True
    return which_any("WINWORD.EXE", "winword") is not None


def resolve_soffice() -> str | None:
    found = which_any("soffice", "libreoffice")
    if found:
        return found
    if sys.platform == "darwin":
        app = mac_app_soffice()
        if app:
            return str(app)
    return None


def word_present() -> bool:
    system = platform.system().lower()
    if system == "darwin":
        return mac_word_present()
    if system == "windows":
        return windows_word_present()
    return False


def probe() -> dict[str, str | bool | None]:
    soffice = resolve_soffice()
    return {
        "soffice": soffice,
        "word": word_present(),
        "ready": bool(soffice) or word_present(),
    }


def libreoffice_install_plan(
    system: str,
    *,
    which: WhichFn | None = None,
) -> list[list[str]] | str:
    """Return argv lists the operator may run manually, or an error string."""
    lookup = which or shutil.which
    system = system.lower()
    if system == "darwin":
        brew = which_any("brew", which=lookup)
        if not brew:
            return "Homebrew not found; install brew then: brew install --cask libreoffice"
        return [[brew, "install", "--cask", "libreoffice"]]
    if system == "windows":
        winget = which_any("winget", which=lookup)
        if winget:
            return [
                [
                    winget,
                    "install",
                    "--id",
                    "TheDocumentFoundation.LibreOffice",
                    "-e",
                    "--accept-package-agreements",
                    "--accept-source-agreements",
                ]
            ]
        choco = which_any("choco", which=lookup)
        if choco:
            return [[choco, "install", "libreoffice-fresh", "-y"]]
        return "neither winget nor choco found; install LibreOffice manually"
    if system == "linux":
        if which_any("apt-get", which=lookup):
            return [
                ["sudo", "apt-get", "update"],
                ["sudo", "apt-get", "install", "-y", "libreoffice"],
            ]
        if which_any("dnf", which=lookup):
            return [["sudo", "dnf", "install", "-y", "libreoffice"]]
        if which_any("pacman", which=lookup):
            return [["sudo", "pacman", "-S", "--noconfirm", "libreoffice-fresh"]]
        return "no supported package manager (apt/dnf/pacman)"
    return f"unsupported platform: {system}"


def manual_install_hint(
    system: str | None = None,
    *,
    which: WhichFn | None = None,
) -> str:
    """Human-readable LibreOffice install steps (never executed by this script)."""
    plan = libreoffice_install_plan(system or platform.system(), which=which)
    if isinstance(plan, str):
        return plan
    lines = ["Install LibreOffice manually (this skill will not run package managers):"]
    for cmd in plan:
        lines.append("  " + " ".join(cmd))
    return "\n".join(lines)


def ensure(
    *,
    probe: ProbeFn | None = None,
    run: RunFn | None = None,
    system: str | None = None,
    which: WhichFn | None = None,
) -> int:
    """Probe only. `run` is accepted for tests to prove no install commands execute."""
    _ = run  # intentional: never invoke package managers from this skill
    probe_fn = probe or globals()["probe"]
    state = probe_fn()
    print(f"Word present: {state['word']}")
    print(f"soffice: {state['soffice'] or 'not found'}")
    if state["ready"]:
        print("office host ready")
        return 0
    print(
        "neither Word nor LibreOffice found; install a host yourself, then re-probe",
        file=sys.stderr,
    )
    print(manual_install_hint(system, which=which), file=sys.stderr)
    return 1


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
        description="Probe Word/LibreOffice; print manual install hints (no auto-install)."
    )
    parser.parse_args(argv)
    code = ensure()
    try:
        ready_mod = _load_script("toolchain_ready")
        pin = _load_script("ensure_docx").PIN
        print(ready_mod.format_report(ready_mod.snapshot(pin=pin)))
    except (OSError, ImportError, RuntimeError) as exc:
        print(f"toolchain ready report failed: {exc}", file=sys.stderr)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
