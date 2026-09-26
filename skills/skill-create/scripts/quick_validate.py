#!/usr/bin/env python3
"""Validate Agent Skill frontmatter and basic layout (stdlib only)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_NAME_LEN = 64
MAX_DESC_LEN = 1024
ALLOWED_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
    "disable-model-invocation",
}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def parse_simple_yaml_map(text: str) -> dict[str, str]:
    """Parse a flat-ish YAML mapping for skill frontmatter without PyYAML.

    Supports single-line `key: value` and folded `key: >` / `key: |` blocks.
    """
    result: dict[str, str] = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" not in line:
            raise ValueError(f"expected key: value, got: {line!r}")
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest in (">", "|", ">-", "|-"):
            block: list[str] = []
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt and not nxt.startswith((" ", "\t")) and ":" in nxt:
                    break
                block.append(nxt.strip() if rest.startswith(">") else nxt)
                i += 1
            value = " ".join(x for x in block if x) if rest.startswith(">") else "\n".join(block)
            result[key] = value.strip()
            continue
        result[key] = rest.strip().strip("\"'")
        i += 1
    return result


def validate_skill(skill_path: Path) -> tuple[bool, str]:
    skill_md = skill_path / "SKILL.md"
    if not skill_md.is_file():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    if not match:
        return False, "Invalid or missing YAML frontmatter"

    try:
        frontmatter = parse_simple_yaml_map(match.group(1))
    except ValueError as exc:
        return False, f"Invalid frontmatter: {exc}"

    unexpected = set(frontmatter) - ALLOWED_KEYS
    if unexpected:
        return (
            False,
            "Unexpected key(s): "
            + ", ".join(sorted(unexpected))
            + ". Allowed: "
            + ", ".join(sorted(ALLOWED_KEYS)),
        )

    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = frontmatter["name"].strip()
    if not NAME_RE.match(name):
        return False, f"Name '{name}' must be kebab-case"
    if len(name) > MAX_NAME_LEN:
        return False, f"Name too long ({len(name)} > {MAX_NAME_LEN})"
    if skill_path.name != name:
        return False, f"Folder name '{skill_path.name}' must match frontmatter name '{name}'"

    description = frontmatter["description"].strip()
    if not description:
        return False, "Description must be non-empty"
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets (< or >)"
    if len(description) > MAX_DESC_LEN:
        return False, f"Description too long ({len(description)} > {MAX_DESC_LEN})"

    return True, "Skill is valid!"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 quick_validate.py <skill_directory>", file=sys.stderr)
        return 1
    path = Path(sys.argv[1])
    ok, message = validate_skill(path)
    print(message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
