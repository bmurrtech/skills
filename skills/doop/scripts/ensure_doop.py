#!/usr/bin/env python3
"""Probe / start / stop a local Doop install for the doop skill.

Start/stop only after Doop identity checks (checkout + live probe).
Does not download Doop; operator clones to DOOP_HOME (default ~/.doop).

Env:
  DOOP_HOME   checkout path (default: ~/.doop)
  DOOP_WEB    default http://127.0.0.1:4300
  DOOP_API    default http://127.0.0.1:4400
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_HOME = Path.home() / ".doop"
CACHE = Path.home() / ".cache" / "bmurrtech-doop"
PID_FILE = CACHE / "doop-dev.pid"
MODE_FILE = CACHE / "doop-runtime.mode"  # bun | docker

# Markers that a directory is upstream Doop (kgoedecke/doop), not an arbitrary app.
DOOP_PACKAGE_NAME = "doop"
DOOP_MARKER_FILES = (
    "server/mcp.ts",
    "server/index.ts",
    "shared/agents.ts",
)


def home() -> Path:
    return Path(os.environ.get("DOOP_HOME", DEFAULT_HOME)).expanduser()


def web_base() -> str:
    return os.environ.get("DOOP_WEB", "http://127.0.0.1:4300").rstrip("/")


def api_base() -> str:
    return os.environ.get("DOOP_API", "http://127.0.0.1:4400").rstrip("/")


def fetch_text(url: str, timeout: float = 1.5) -> tuple[int | None, str]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            status = getattr(resp, "status", 200)
            body = resp.read(65536).decode("utf-8", errors="replace")
            return status, body
    except (urllib.error.URLError, TimeoutError, OSError):
        return None, ""


def is_doop_checkout(h: Path) -> tuple[bool, str]:
    """Return (ok, reason). Requires package.json name == doop + marker files."""
    pkg_path = h / "package.json"
    if not pkg_path.is_file():
        return False, "missing package.json"
    try:
        data = json.loads(pkg_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return False, f"unreadable package.json: {exc}"
    if data.get("name") != DOOP_PACKAGE_NAME:
        return False, f'package.json name is {data.get("name")!r}, want {DOOP_PACKAGE_NAME!r}'
    missing = [rel for rel in DOOP_MARKER_FILES if not (h / rel).is_file()]
    if missing:
        return False, f"missing Doop markers: {', '.join(missing)}"
    return True, "ok"


def is_doop_healthz_body(body: str) -> bool:
    body = body.strip()
    if not body.startswith("{"):
        return False
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return False
    return data.get("ok") is True


def is_doop_html_body(body: str) -> bool:
    # Vite serves index.html on :4300; /healthz is API-only (not proxied).
    return "doop-theme" in body and "Doop" in body


def probe_doop_live() -> dict:
    """Identify a live Doop via /healthz JSON or web HTML markers — not bare HTTP <500."""
    api = api_base()
    web = web_base()
    status_api, body_api = fetch_text(api + "/healthz")
    if status_api == 200 and is_doop_healthz_body(body_api):
        return {"live": True, "via": "api_healthz", "base": api}
    status_web_hz, body_web_hz = fetch_text(web + "/healthz")
    if status_web_hz == 200 and is_doop_healthz_body(body_web_hz):
        return {"live": True, "via": "web_healthz", "base": web}
    status_web, body_web = fetch_text(web + "/")
    if status_web == 200 and is_doop_html_body(body_web):
        return {"live": True, "via": "web_html", "base": web}
    occupied = any(s is not None for s in (status_api, status_web_hz, status_web))
    return {"live": False, "via": None, "base": None, "port_occupied": occupied}


def process_cmdline(pid: int) -> str | None:
    proc_cmd = Path(f"/proc/{pid}/cmdline")
    if proc_cmd.is_file():
        raw = proc_cmd.read_bytes().replace(b"\x00", b" ").decode("utf-8", errors="replace").strip()
        return raw or None
    try:
        out = subprocess.run(
            ["ps", "-p", str(pid), "-ww", "-o", "command="],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if out.returncode != 0:
        return None
    line = out.stdout.strip()
    return line or None


def process_cwd(pid: int) -> Path | None:
    proc_cwd = Path(f"/proc/{pid}/cwd")
    if proc_cwd.is_symlink() or proc_cwd.exists():
        try:
            return proc_cwd.resolve()
        except OSError:
            pass
    try:
        out = subprocess.run(
            ["lsof", "-a", "-p", str(pid), "-d", "cwd", "-Fn"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if out.returncode != 0:
        return None
    for line in out.stdout.splitlines():
        if line.startswith("n"):
            return Path(line[1:]).resolve()
    return None


def is_expected_bun_dev(pid: int, h: Path) -> tuple[bool, str]:
    """Refuse kill unless cmdline looks like bun … dev and cwd/home matches DOOP_HOME."""
    try:
        os.kill(pid, 0)
    except OSError:
        return False, "pid not running"
    cmd = process_cmdline(pid)
    if not cmd:
        return False, "cannot read cmdline"
    lower = cmd.lower()
    if "bun" not in lower:
        return False, f"cmdline has no bun: {cmd!r}"
    if "dev" not in lower:
        return False, f"cmdline has no dev: {cmd!r}"
    home_res = h.resolve()
    if str(home_res) in cmd:
        return True, "cmdline contains DOOP_HOME"
    cwd = process_cwd(pid)
    if cwd is not None and cwd == home_res:
        return True, "cwd matches DOOP_HOME"
    return False, f"process not bound to DOOP_HOME={home_res} (cmdline={cmd!r}, cwd={cwd})"


def status_payload() -> dict:
    h = home()
    checkout_ok, checkout_reason = is_doop_checkout(h)
    live = probe_doop_live()
    return {
        "doop_home": str(h),
        "home_exists": h.is_dir(),
        "is_doop_checkout": checkout_ok,
        "checkout_reason": checkout_reason,
        "web": web_base(),
        "api": api_base(),
        "doop_live": live.get("live", False),
        "live_via": live.get("via"),
        "port_occupied_non_doop": bool(live.get("port_occupied")) and not live.get("live"),
        "bun": shutil.which("bun") is not None,
        "docker": shutil.which("docker") is not None,
        "pid_file": str(PID_FILE),
        "pid_running": _pid_file_alive(),
    }


def _pid_file_alive() -> bool:
    if not PID_FILE.is_file():
        return False
    try:
        pid = int(PID_FILE.read_text().strip())
    except ValueError:
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def cmd_status(_: argparse.Namespace) -> int:
    print(json.dumps(status_payload(), indent=2))
    return 0


def cmd_ensure(_: argparse.Namespace) -> int:
    st = status_payload()
    live = probe_doop_live()
    if live.get("live"):
        print(json.dumps({"ok": True, "action": "already_up", **st, "live": live}, indent=2))
        return 0
    if live.get("port_occupied"):
        print(
            json.dumps(
                {
                    "ok": False,
                    "action": "port_busy_non_doop",
                    "hint": "Something answers on DOOP_WEB/DOOP_API but failed Doop identity (/healthz or HTML markers). Free the port or fix DOOP_* URLs.",
                    **st,
                },
                indent=2,
            ),
            file=sys.stderr,
        )
        return 8

    h = home()
    ok, reason = is_doop_checkout(h)
    if not ok:
        print(
            json.dumps(
                {
                    "ok": False,
                    "action": "not_doop_checkout",
                    "hint": f"Clone https://github.com/kgoedecke/doop into {h} (or set DOOP_HOME). Refusing start: {reason}",
                    **st,
                },
                indent=2,
            ),
            file=sys.stderr,
        )
        return 2

    if st["bun"]:
        return _start_bun(h)
    if st["docker"]:
        return _start_docker(h)

    print(
        json.dumps(
            {
                "ok": False,
                "action": "missing_runtime",
                "hint": "Install bun (preferred) or docker, then retry",
                **st,
            },
            indent=2,
        ),
        file=sys.stderr,
    )
    return 3


def _start_bun(h: Path) -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    log = PID_FILE.with_suffix(".log")
    if not (h / "node_modules").is_dir():
        install = subprocess.run(["bun", "install"], cwd=h, capture_output=True, text=True)
        if install.returncode != 0:
            print(install.stdout)
            print(install.stderr, file=sys.stderr)
            return install.returncode or 4

    with log.open("ab") as lf:
        proc = subprocess.Popen(
            ["bun", "run", "dev"],
            cwd=h,
            stdout=lf,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    PID_FILE.write_text(str(proc.pid))
    MODE_FILE.write_text("bun")

    deadline = time.time() + 90
    while time.time() < deadline:
        if probe_doop_live().get("live"):
            print(
                json.dumps(
                    {
                        "ok": True,
                        "action": "started_bun",
                        "pid": proc.pid,
                        "log": str(log),
                        **status_payload(),
                    },
                    indent=2,
                )
            )
            return 0
        time.sleep(1)

    print(
        json.dumps(
            {
                "ok": False,
                "action": "start_timeout",
                "pid": proc.pid,
                "log": str(log),
                **status_payload(),
            },
            indent=2,
        ),
        file=sys.stderr,
    )
    return 5


def _start_docker(h: Path) -> int:
    env = os.environ.copy()
    if not env.get("BETTER_AUTH_SECRET"):
        env["BETTER_AUTH_SECRET"] = "dev-only-" + os.urandom(8).hex()
    proc = subprocess.run(
        ["docker", "compose", "up", "-d", "--build"],
        cwd=h,
        env=env,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        return proc.returncode or 6

    deadline = time.time() + 120
    while time.time() < deadline:
        # Compose serves the app on DOOP_API (default :4400)
        if probe_doop_live().get("live"):
            CACHE.mkdir(parents=True, exist_ok=True)
            MODE_FILE.write_text("docker")
            print(
                json.dumps(
                    {
                        "ok": True,
                        "action": "started_docker",
                        "web_note": f"docker compose serves {api_base()}",
                        **status_payload(),
                    },
                    indent=2,
                )
            )
            return 0
        time.sleep(2)

    print(json.dumps({"ok": False, "action": "docker_timeout", **status_payload()}, indent=2), file=sys.stderr)
    return 7


def cmd_stop(_: argparse.Namespace) -> int:
    stopped: list[dict] = []
    refused: list[dict] = []
    mode = MODE_FILE.read_text().strip() if MODE_FILE.is_file() else ""
    h = home()

    if mode in ("", "bun") and PID_FILE.is_file():
        try:
            pid = int(PID_FILE.read_text().strip())
        except ValueError:
            refused.append({"bun_pid_file": str(PID_FILE), "reason": "invalid pid"})
            pid = -1
        if pid > 0:
            ok, reason = is_expected_bun_dev(pid, h)
            if not ok:
                refused.append({"bun_pid": pid, "reason": reason})
            else:
                try:
                    os.killpg(pid, signal.SIGTERM)
                except ProcessLookupError:
                    try:
                        os.kill(pid, signal.SIGTERM)
                    except ProcessLookupError:
                        pass
                stopped.append({"bun_pid": pid, "match": reason})
                PID_FILE.unlink(missing_ok=True)

    if mode == "docker":
        ok, reason = is_doop_checkout(h)
        if not ok:
            refused.append({"docker_compose": "refused", "reason": reason})
        elif (h / "docker-compose.yml").is_file() and shutil.which("docker"):
            subprocess.run(["docker", "compose", "down"], cwd=h, capture_output=True)
            stopped.append({"docker_compose": "down"})

    if stopped:
        MODE_FILE.unlink(missing_ok=True)

    payload = {
        "ok": not refused or bool(stopped),
        "action": "stop",
        "stopped": stopped,
        "refused": refused,
        **status_payload(),
    }
    print(json.dumps(payload, indent=2))
    return 0 if not refused or stopped else 9


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Ensure local Doop for bmurrtech doop skill",
        epilog=(
            "Commands: status (probe), ensure (start if Doop identity checks pass), "
            "stop (SIGTERM only if bun cmdline+cwd match DOOP_HOME; docker down only if mode=docker "
            "and checkout is Doop). Ports: DOOP_WEB / DOOP_API (defaults :4300 / :4400)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="JSON probe (checkout + live Doop identity)").set_defaults(func=cmd_status)
    sub.add_parser("ensure", help="Start bun|docker only after Doop checkout identity").set_defaults(func=cmd_ensure)
    sub.add_parser("stop", help="Stop only when process matches expected bun/dev + DOOP_HOME").set_defaults(
        func=cmd_stop
    )
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
