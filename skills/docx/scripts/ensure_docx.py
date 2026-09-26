#!/usr/bin/env python3
"""Ensure a pinned docx-cli release binary is on PATH (SHA-256 verified).

Public contract: https://github.com/kklimuk/docx-cli/releases
Does not install Word/LibreOffice — use ensure_office.py.
Does not pipe remote scripts.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from collections.abc import Callable
from pathlib import Path

PIN = "0.26.0"
TAG = f"v{PIN}"
REPO = "kklimuk/docx-cli"

DownloadFn = Callable[[str, Path], None]


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


def install_dir() -> Path:
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(base) / "docx-cli"
    return Path.home() / ".local" / "bin"


def binary_name() -> str:
    return "docx.exe" if os.name == "nt" else "docx"


def parse_sums(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for line in text.splitlines():
        parts = line.split()
        if len(parts) < 2:
            continue
        found[parts[-1].lstrip("*")] = parts[0].lower()
    return found


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


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


def download(url: str, dest: Path) -> None:
    with urllib.request.urlopen(url, timeout=120) as response:
        dest.write_bytes(response.read())


def install_binary(
    *,
    system: str | None = None,
    machine: str | None = None,
    dest_dir: Path | None = None,
    download: DownloadFn | None = None,
) -> Path:
    fetch = download or globals()["download"]
    name = asset_name(system or platform.system(), machine or platform.machine())
    base = f"https://github.com/{REPO}/releases/download/{TAG}"
    out_dir = dest_dir or install_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / binary_name()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        sums_path = root / "SHA256SUMS"
        blob = root / name
        fetch(f"{base}/SHA256SUMS", sums_path)
        fetch(f"{base}/{name}", blob)
        expected = parse_sums(sums_path.read_text(encoding="utf-8")).get(name)
        actual = sha256_file(blob)
        if not expected or actual != expected:
            raise RuntimeError(f"SHA-256 mismatch for {name}")
        shutil.copyfile(blob, dest)
    if os.name != "nt":
        dest.chmod(dest.stat().st_mode | 0o111)
    return dest


def dir_on_path(directory: Path) -> bool:
    want = str(directory.resolve()).lower()
    for entry in os.environ.get("PATH", "").split(os.pathsep):
        if not entry:
            continue
        try:
            if str(Path(entry).resolve()).lower() == want:
                return True
        except OSError:
            continue
    return False


def path_ok(dest: Path) -> str | None:
    resolved = shutil.which("docx")
    if not dir_on_path(dest.parent) or resolved is None:
        return f"add to PATH: {dest.parent}"
    try:
        same = Path(resolved).resolve() == dest.resolve()
    except OSError:
        same = False
    ver = version_of(resolved)
    if not same or ver != PIN:
        return f"docx on PATH is {ver or 'unknown'} ({resolved}), want {PIN} at {dest}"
    return None


def ensure() -> str | None:
    current = shutil.which("docx")
    if current and version_of(current) == PIN:
        print(f"docx {PIN} already on PATH ({current})")
        return None
    try:
        dest = install_binary()
    except (OSError, RuntimeError, ValueError) as exc:
        return f"docx binary install failed: {exc}"
    err = path_ok(dest)
    if err:
        print(f"installed {dest}", file=sys.stderr)
        return err
    print(f"installed {dest}")
    return None


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
        description=f"Ensure docx-cli {TAG} binary (SHA-256 verified)."
    )
    parser.add_argument(
        "--with-upstream-skill",
        action="store_true",
        help="also npx skills add kklimuk/docx-cli at the pin (global)",
    )
    args = parser.parse_args(argv)

    err = ensure()
    if err:
        print(err, file=sys.stderr)

    try:
        ready_mod = _load_script("toolchain_ready")
        print(ready_mod.format_report(ready_mod.snapshot(pin=PIN)))
    except (OSError, ImportError, RuntimeError) as exc:
        print(f"toolchain ready report failed: {exc}", file=sys.stderr)

    if args.with_upstream_skill:
        npx = shutil.which("npx")
        if not npx:
            print("npx not found; upstream skill not installed", file=sys.stderr)
            return 1
        completed = subprocess.run(
            [
                npx,
                "--yes",
                "skills",
                "add",
                f"{REPO}#{TAG}",
                "-g",
                "-y",
                "--skill",
                "docx-cli",
            ],
            check=False,
        )
        if err:
            return 1
        return completed.returncode

    return 1 if err else 0


if __name__ == "__main__":
    raise SystemExit(main())
