"""Seams for docx ensure scripts (platform plans + probe-only readiness)."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "skills" / "docx" / "scripts"


def _load(name: str):
    path = SCRIPTS / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ensure_docx = _load("ensure_docx")
ensure_office = _load("ensure_office")
toolchain_ready = _load("toolchain_ready")


class EnsureDocxAssetTests(unittest.TestCase):
    def test_darwin_arm(self) -> None:
        self.assertEqual(
            ensure_docx.asset_name("Darwin", "arm64"), "docx-darwin-arm64"
        )

    def test_linux_x64(self) -> None:
        self.assertEqual(ensure_docx.asset_name("Linux", "x86_64"), "docx-linux-x64")

    def test_windows_arm_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ensure_docx.asset_name("Windows", "arm64")


class LibreOfficeInstallPlanTests(unittest.TestCase):
    def test_macos_brew(self) -> None:
        plan = ensure_office.libreoffice_install_plan(
            "Darwin", which=lambda n: "/opt/homebrew/bin/brew" if n == "brew" else None
        )
        self.assertEqual(plan, [["/opt/homebrew/bin/brew", "install", "--cask", "libreoffice"]])

    def test_macos_without_brew(self) -> None:
        plan = ensure_office.libreoffice_install_plan("Darwin", which=lambda _n: None)
        self.assertIsInstance(plan, str)

    def test_windows_prefers_winget(self) -> None:
        def which(n: str) -> str | None:
            return {"winget": "winget", "choco": "choco"}.get(n)

        plan = ensure_office.libreoffice_install_plan("Windows", which=which)
        self.assertIsInstance(plan, list)
        self.assertEqual(plan[0][0], "winget")
        self.assertIn("TheDocumentFoundation.LibreOffice", plan[0])

    def test_debian_apt(self) -> None:
        plan = ensure_office.libreoffice_install_plan(
            "Linux", which=lambda n: "/usr/bin/apt-get" if n == "apt-get" else None
        )
        self.assertIsInstance(plan, list)
        self.assertEqual(len(plan), 2)
        self.assertIn("libreoffice", plan[1])


class ToolchainReadyTests(unittest.TestCase):
    def test_pin_match_and_office_ready(self) -> None:
        report = toolchain_ready.assess(
            pin=ensure_docx.PIN,
            docx_path="/bin/docx",
            docx_version=ensure_docx.PIN,
            soffice="/opt/homebrew/bin/soffice",
            word=False,
        )
        self.assertTrue(report.docx_pin_ok)
        self.assertTrue(report.office_ready)
        self.assertTrue(report.ready)
        self.assertEqual(report.errors, [])

    def test_pin_mismatch(self) -> None:
        report = toolchain_ready.assess(
            pin="0.26.0",
            docx_path="/bin/docx",
            docx_version="0.1.0",
            soffice="/opt/homebrew/bin/soffice",
            word=False,
        )
        self.assertFalse(report.docx_pin_ok)
        self.assertTrue(report.office_ready)
        self.assertFalse(report.ready)
        self.assertTrue(any("0.26.0" in e for e in report.errors))

    def test_docx_missing(self) -> None:
        report = toolchain_ready.assess(
            pin="0.26.0",
            docx_path=None,
            docx_version=None,
            soffice="/opt/homebrew/bin/soffice",
            word=False,
        )
        self.assertFalse(report.docx_pin_ok)
        self.assertFalse(report.ready)
        self.assertTrue(any("docx" in e.lower() for e in report.errors))

    def test_office_absent(self) -> None:
        report = toolchain_ready.assess(
            pin="0.26.0",
            docx_path="/bin/docx",
            docx_version="0.26.0",
            soffice=None,
            word=False,
        )
        self.assertTrue(report.docx_pin_ok)
        self.assertFalse(report.office_ready)
        self.assertFalse(report.ready)
        self.assertTrue(any("office" in e.lower() or "libreoffice" in e.lower() or "word" in e.lower() for e in report.errors))

    def test_word_alone_is_office_ready(self) -> None:
        report = toolchain_ready.assess(
            pin="0.26.0",
            docx_path="/bin/docx",
            docx_version="0.26.0",
            soffice=None,
            word=True,
        )
        self.assertTrue(report.office_ready)
        self.assertTrue(report.ready)


class EnsureDocxDigestTests(unittest.TestCase):
    def test_committed_digests_cover_supported_assets(self) -> None:
        digests = ensure_docx.load_digests()
        for system, machine in (
            ("Darwin", "arm64"),
            ("Darwin", "x86_64"),
            ("Linux", "x86_64"),
            ("Linux", "aarch64"),
            ("Windows", "AMD64"),
        ):
            name = ensure_docx.asset_name(system, machine)
            self.assertIn(name, digests)
            self.assertEqual(len(digests[name]), 64)

    def test_expected_digest_matches_digests_file(self) -> None:
        name = ensure_docx.asset_name("Darwin", "arm64")
        self.assertEqual(
            ensure_docx.expected_digest(name),
            "0050490bda31af2b0dc698aa95df583c13fbe210fd1effd5bc98291c634f0ccf",
        )


class EnsureDocxProbeTests(unittest.TestCase):
    def test_ensure_missing_points_at_how_to_not_install_flag(self) -> None:
        err = ensure_docx.ensure(which=lambda _n: None)
        self.assertIsNotNone(err)
        self.assertIn(ensure_docx.HOW_TO, err or "")
        self.assertIn(ensure_docx.PIN, err or "")
        self.assertNotIn("--install", err or "")
        self.assertNotIn("urllib", err or "")

    def test_manual_hint_includes_platform_asset(self) -> None:
        hint = ensure_docx.manual_install_hint(system="Darwin", machine="arm64")
        self.assertIn("docx-darwin-arm64", hint)
        self.assertIn(ensure_docx.HOW_TO, hint)
        self.assertIn("bun-docx", hint)

    def test_source_has_no_download_or_install_flag(self) -> None:
        source = (SCRIPTS / "ensure_docx.py").read_text(encoding="utf-8")
        self.assertNotIn("import urllib", source)
        self.assertNotIn("urlopen", source)
        self.assertNotIn("--install", source)
        self.assertNotIn("def download", source)
        self.assertNotIn("def install_binary", source)
        facade = (SCRIPTS / "ensure_toolchain.py").read_text(encoding="utf-8")
        self.assertNotIn("--install", facade)


class EnsureOfficeInstallAdapterTests(unittest.TestCase):
    def test_manual_hint_includes_plan_commands(self) -> None:
        hint = ensure_office.manual_install_hint(
            "Darwin",
            which=lambda n: "/opt/homebrew/bin/brew" if n == "brew" else None,
        )
        self.assertIn("brew", hint)
        self.assertIn("libreoffice", hint)
        self.assertNotIn("sudo", hint)

    def test_debian_plan_documents_sudo_but_ensure_never_runs(self) -> None:
        plan = ensure_office.libreoffice_install_plan(
            "Linux", which=lambda n: "/usr/bin/apt-get" if n == "apt-get" else None
        )
        self.assertIsInstance(plan, list)
        self.assertEqual(plan[0][0], "sudo")
        recorded: list[list[str]] = []

        def fake_run(cmd: list[str], *, check: bool = False):
            recorded.append(cmd)
            return subprocess.CompletedProcess(cmd, 0)

        code = ensure_office.ensure(
            probe=lambda: {"soffice": None, "word": False, "ready": False},
            run=fake_run,
            system="Linux",
            which=lambda n: "/usr/bin/apt-get" if n == "apt-get" else None,
        )
        self.assertEqual(code, 1)
        self.assertEqual(recorded, [])

    def test_ensure_probe_exit_0_when_ready(self) -> None:
        code = ensure_office.ensure(
            probe=lambda: {"soffice": "/opt/homebrew/bin/soffice", "word": False, "ready": True},
        )
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
