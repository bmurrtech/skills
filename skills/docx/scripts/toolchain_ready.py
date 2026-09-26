"""Typed toolchain readiness for docx skill (docx pin + office host).

Pure assess() is the test surface. snapshot() gathers live PATH / host state.
"""

from __future__ import annotations

import importlib.util
import shutil
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

WhichFn = Callable[[str], str | None]
VersionFn = Callable[[str], str | None]
SofficeFn = Callable[[], str | None]
WordFn = Callable[[], bool]

_SCRIPTS = Path(__file__).resolve().parent


def _load_sibling(name: str):
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


@dataclass(frozen=True)
class ToolchainReady:
    docx_path: str | None
    docx_version: str | None
    docx_pin_ok: bool
    soffice: str | None
    word: bool
    office_ready: bool
    ready: bool
    errors: list[str] = field(default_factory=list)


def assess(
    *,
    pin: str,
    docx_path: str | None,
    docx_version: str | None,
    soffice: str | None,
    word: bool,
) -> ToolchainReady:
    errors: list[str] = []
    docx_pin_ok = bool(docx_path) and docx_version == pin
    if not docx_path:
        errors.append("docx not found on PATH")
    elif docx_version != pin:
        errors.append(
            f"docx on PATH is {docx_version or 'unknown'} ({docx_path}), want {pin}"
        )

    office_ready = bool(soffice) or word
    if not office_ready:
        errors.append("neither Word nor LibreOffice found")

    return ToolchainReady(
        docx_path=docx_path,
        docx_version=docx_version,
        docx_pin_ok=docx_pin_ok,
        soffice=soffice,
        word=word,
        office_ready=office_ready,
        ready=docx_pin_ok and office_ready,
        errors=errors,
    )


def snapshot(
    *,
    pin: str,
    which: WhichFn | None = None,
    version_of: VersionFn | None = None,
    resolve_soffice: SofficeFn | None = None,
    word_present: WordFn | None = None,
) -> ToolchainReady:
    """Gather live state and return ToolchainReady. Adapters injectable for tests."""
    lookup = which or shutil.which
    docx_path = lookup("docx")
    ver_fn = version_of
    if ver_fn is None:
        ver_fn = _load_sibling("ensure_docx").version_of
    docx_version = ver_fn(docx_path) if docx_path else None

    soffice_fn = resolve_soffice
    word_fn = word_present
    if soffice_fn is None or word_fn is None:
        office = _load_sibling("ensure_office")
        soffice_fn = soffice_fn or office.resolve_soffice
        word_fn = word_fn or office.word_present

    return assess(
        pin=pin,
        docx_path=docx_path,
        docx_version=docx_version,
        soffice=soffice_fn(),
        word=word_fn(),
    )


def format_report(report: ToolchainReady) -> str:
    lines = [
        f"docx: {report.docx_path or 'not found'}"
        + (f" ({report.docx_version})" if report.docx_version else ""),
        f"docx pin ok: {report.docx_pin_ok}",
        f"Word present: {report.word}",
        f"soffice: {report.soffice or 'not found'}",
        f"office ready: {report.office_ready}",
        f"toolchain ready: {report.ready}",
    ]
    for err in report.errors:
        lines.append(f"error: {err}")
    return "\n".join(lines)
