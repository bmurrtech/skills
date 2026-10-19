"""Seams for doop ensure_doop identity + stop safety."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "skills" / "doop" / "scripts" / "ensure_doop.py"


def _load():
    spec = importlib.util.spec_from_file_location("ensure_doop", SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ensure_doop"] = mod
    spec.loader.exec_module(mod)
    return mod


ensure_doop = _load()


def _fake_doop_tree(root: Path) -> None:
    (root / "server").mkdir(parents=True)
    (root / "shared").mkdir(parents=True)
    (root / "package.json").write_text(
        json.dumps({"name": "doop", "private": True}), encoding="utf-8"
    )
    for rel in ensure_doop.DOOP_MARKER_FILES:
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("// marker\n", encoding="utf-8")


class CheckoutIdentityTests(unittest.TestCase):
    def test_accepts_doop_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _fake_doop_tree(root)
            ok, reason = ensure_doop.is_doop_checkout(root)
            self.assertTrue(ok, reason)

    def test_rejects_wrong_package_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _fake_doop_tree(root)
            (root / "package.json").write_text(json.dumps({"name": "other"}), encoding="utf-8")
            ok, reason = ensure_doop.is_doop_checkout(root)
            self.assertFalse(ok)
            self.assertIn("other", reason)

    def test_rejects_missing_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "package.json").write_text(json.dumps({"name": "doop"}), encoding="utf-8")
            ok, reason = ensure_doop.is_doop_checkout(root)
            self.assertFalse(ok)
            self.assertIn("missing", reason)


class LiveProbeTests(unittest.TestCase):
    def test_healthz_ok(self) -> None:
        self.assertTrue(ensure_doop.is_doop_healthz_body('{"ok": true}'))
        self.assertFalse(ensure_doop.is_doop_healthz_body("<html>ok</html>"))
        self.assertFalse(ensure_doop.is_doop_healthz_body('{"ok": false}'))

    def test_html_markers(self) -> None:
        self.assertTrue(
            ensure_doop.is_doop_html_body(
                '<script>localStorage.getItem("doop-theme")</script><title>Doop</title>'
            )
        )
        self.assertFalse(ensure_doop.is_doop_html_body("<title>Other App</title>"))

    def test_probe_live_via_api(self) -> None:
        def fake_fetch(url: str, timeout: float = 1.5):
            if url.endswith("/healthz") and "4400" in url:
                return 200, '{"ok": true}'
            return None, ""

        with mock.patch.object(ensure_doop, "fetch_text", side_effect=fake_fetch):
            with mock.patch.dict(
                "os.environ",
                {"DOOP_WEB": "http://127.0.0.1:4300", "DOOP_API": "http://127.0.0.1:4400"},
                clear=False,
            ):
                live = ensure_doop.probe_doop_live()
        self.assertTrue(live["live"])
        self.assertEqual(live["via"], "api_healthz")

    def test_probe_occupied_non_doop(self) -> None:
        def fake_fetch(url: str, timeout: float = 1.5):
            return 200, "<html><title>nginx</title></html>"

        with mock.patch.object(ensure_doop, "fetch_text", side_effect=fake_fetch):
            live = ensure_doop.probe_doop_live()
        self.assertFalse(live["live"])
        self.assertTrue(live["port_occupied"])


class StopSafetyTests(unittest.TestCase):
    def test_expected_bun_dev_cmdline_and_cwd(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            with mock.patch.object(ensure_doop.os, "kill", return_value=None):
                with mock.patch.object(
                    ensure_doop, "process_cmdline", return_value="bun run dev"
                ):
                    with mock.patch.object(ensure_doop, "process_cwd", return_value=root):
                        ok, reason = ensure_doop.is_expected_bun_dev(12345, root)
            self.assertTrue(ok, reason)

    def test_refuse_unrelated_pid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            with mock.patch.object(ensure_doop.os, "kill", return_value=None):
                with mock.patch.object(
                    ensure_doop, "process_cmdline", return_value="/usr/bin/python3 server.py"
                ):
                    with mock.patch.object(ensure_doop, "process_cwd", return_value=root):
                        ok, reason = ensure_doop.is_expected_bun_dev(99, root)
            self.assertFalse(ok)
            self.assertIn("bun", reason)


class EnsureGateTests(unittest.TestCase):
    def test_ensure_refuses_non_doop_home(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "package.json").write_text(json.dumps({"name": "nope"}), encoding="utf-8")
            with mock.patch.object(ensure_doop, "home", return_value=root):
                with mock.patch.object(
                    ensure_doop, "probe_doop_live", return_value={"live": False, "port_occupied": False}
                ):
                    with mock.patch.object(ensure_doop, "status_payload", return_value={"bun": True, "docker": False}):
                        code = ensure_doop.cmd_ensure(argparse_ns())
            self.assertEqual(code, 2)


def argparse_ns():
    return mock.Mock()


if __name__ == "__main__":
    unittest.main()
