#!/usr/bin/env python3
"""Scaffold a new skill under skills/<name>/ (repo default)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_NAME_LEN = 64
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_RESOURCES = ("scripts", "references", "assets")

SKILL_STUB = """---
name: {name}
description: >
  [TODO: what this skill does and when to use it — trigger branches, leading word first]
---

# {title}

## Overview

[TODO: one or two sentences]

## Workflow

### 1. [First step]

[Instructions]

**Done when:** [checkable criterion]

### 2. [Next step]

[Instructions]

**Done when:** [checkable criterion]
"""

OPENAI_YAML_STUB = """interface:
  display_name: "{title}"
  short_description: "[TODO: 25-64 char UI blurb]"
policy:
  allow_implicit_invocation: false
"""


def title_case(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def validate_name(name: str) -> str | None:
    if not NAME_RE.match(name):
        return "name must be kebab-case (lowercase, digits, single hyphens)"
    if len(name) > MAX_NAME_LEN:
        return f"name exceeds {MAX_NAME_LEN} characters"
    return None


def repo_root_from_script() -> Path:
    # skills/skill-create/scripts/init_skill.py → repo root
    return Path(__file__).resolve().parents[3]


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a skill under skills/")
    parser.add_argument("name", help="kebab-case skill name")
    parser.add_argument(
        "--path",
        default=None,
        help="parent directory (default: <repo>/skills)",
    )
    parser.add_argument(
        "--resources",
        default="",
        help="comma list: scripts,references,assets",
    )
    parser.add_argument(
        "--allow-implicit",
        action="store_true",
        help="set policy.allow_implicit_invocation: true",
    )
    args = parser.parse_args()

    err = validate_name(args.name)
    if err:
        print(err, file=sys.stderr)
        return 1

    parent = Path(args.path) if args.path else repo_root_from_script() / "skills"
    skill_dir = parent / args.name
    if skill_dir.exists():
        print(f"refusing to overwrite existing path: {skill_dir}", file=sys.stderr)
        return 1

    resources = [r.strip() for r in args.resources.split(",") if r.strip()]
    for r in resources:
        if r not in ALLOWED_RESOURCES:
            print(
                f"unknown resource '{r}'; allowed: {', '.join(ALLOWED_RESOURCES)}",
                file=sys.stderr,
            )
            return 1

    title = title_case(args.name)
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        SKILL_STUB.format(name=args.name, title=title),
        encoding="utf-8",
    )

    agents = skill_dir / "agents"
    agents.mkdir()
    implicit = "true" if args.allow_implicit else "false"
    (agents / "openai.yaml").write_text(
        f'interface:\n  display_name: "{title}"\n'
        f'  short_description: "[TODO: 25-64 char UI blurb]"\n'
        f"policy:\n  allow_implicit_invocation: {implicit}\n",
        encoding="utf-8",
    )

    for r in resources:
        (skill_dir / r).mkdir()
        (skill_dir / r / ".gitkeep").write_text("", encoding="utf-8")

    print(f"created {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
