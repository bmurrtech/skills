#!/usr/bin/env python3
"""Probe for Word/LibreOffice; install LibreOffice via OS package manager if missing.

Does not pipe remote scripts. Does not claim success without a working host.
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
    """Return argv lists to run, or an error string if install cannot proceed."""
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


def run(cmd: list[str], *, check: bool = False) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(cmd), flush=True)
    return subprocess.run(cmd, check=check, text=True)


def install_libreoffice(
    *,
    system: str | None = None,
    which: WhichFn | None = None,
    run: RunFn | None = None,
) -> str | None:
    runner = run or globals()["run"]
    plan = libreoffice_install_plan(system or platform.system(), which=which)
    if isinstance(plan, str):
        return plan
    try:
        for cmd in plan:
            runner(cmd, check=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        return f"LibreOffice install failed: {exc}"
    return None


def ensure(
    *,
    install: bool,
    assume_yes: bool,
    probe: ProbeFn | None = None,
    install_libreoffice: Callable[..., str | None] | None = None,
) -> int:
    probe_fn = probe or globals()["probe"]
    install_fn = install_libreoffice or globals()["install_libreoffice"]
    state = probe_fn()
    print(f"Word present: {state['word']}")
    print(f"soffice: {state['soffice'] or 'not found'}")
    if state["ready"]:
        print("office host ready")
        return 0
    if not install:
        print(
            "neither Word nor LibreOffice found; re-run with --install",
            file=sys.stderr,
        )
        return 1
    if not assume_yes:
        print(
            "refusing install without --yes (or confirm via setup-bmurrtech-skills)",
            file=sys.stderr,
        )
        return 1
    err = install_fn()
    if err:
        print(err, file=sys.stderr)
        return 1
    state = probe_fn()
    print(f"soffice after install: {state['soffice'] or 'not found'}")
    if not state["soffice"] and not state["word"]:
        print(
            "install finished but soffice still not on PATH; open a new shell or add LibreOffice to PATH",
            file=sys.stderr,
        )
        return 1
    print("office host ready")
    return 0


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
        description="Probe Word/LibreOffice; optionally install LibreOffice."
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="if neither host is present, install LibreOffice via brew/winget/apt/dnf/pacman",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="required with --install (non-interactive confirm)",
    )
    args = parser.parse_args(argv)
    code = ensure(install=args.install, assume_yes=args.yes)
    try:
        ready_mod = _load_script("toolchain_ready")
        pin = _load_script("ensure_docx").PIN
        print(ready_mod.format_report(ready_mod.snapshot(pin=pin)))
    except (OSError, ImportError, RuntimeError) as exc:
        print(f"toolchain ready report failed: {exc}", file=sys.stderr)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
