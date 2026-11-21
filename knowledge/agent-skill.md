---
title: Skill
description: >
  How this library mints, modifies, and improves Agent Skills under skills/ —
  layout, frontmatter, body practices, patterns, and skill TDD.
type: concept
tags: [skills, authoring, tdd]
---

# Skill

A **Skill** in this repository is a directory at `skills/<name>/` containing:

```text
skills/<kebab-name>/
├── SKILL.md          # required — exact name (case-sensitive)
├── agents/
│   └── openai.yaml   # required in this library
├── scripts/          # optional
├── references/       # optional
└── assets/           # optional
```

| Piece | Role |
|-------|------|
| `SKILL.md` | Frontmatter triggers + body instructions |
| `agents/openai.yaml` | Host UI metadata + `policy.allow_implicit_invocation` |
| `scripts/` | Deterministic helpers (see [skill-scripts.md](skill-scripts.md)) |
| `references/` | Docs loaded on demand |
| `assets/` | Output templates/binaries — not context stuffing |

## Rules (mint / modify)

- Create and edit **only** under [`skills/`](../skills/). Never dual-track SoT into agent dirs; delete skill-named **repo-root** noise.
- Folder + frontmatter `name`: kebab-case only; must match; ≤64 chars.
- Entry file is exactly `SKILL.md` — not `skill.md` / `SKILL.MD`.
- **No** `README.md` inside the skill folder; docs live in `SKILL.md` or `references/`.
- Create `scripts/` / `references/` / `assets/` **only when needed**; omit empty dirs.
- Frontmatter required: `name` + **description** = **what + when + key capabilities** (user trigger phrases; ≤1024 chars; no `<` / `>`).
- Lean body: specific steps + **Done when**; error recovery when useful; disclose branch-only detail under `references/` with when-to-read links.
- Align `policy.allow_implicit_invocation` with whether the skill may model-trigger.
- Before adding `scripts/`, apply [Skill scripts vs LLM](skill-scripts.md).

## Description (first progressive-disclosure level)

Metadata alone should tell the host **when** to load the skill without pulling the body. Structure: **[What it does] + [When to use it] + [Key capabilities]**. Third person; front-load the leading word; one trigger per distinct branch; concrete user phrases and file types when relevant.

Good / bad examples, body template, instruction practices: shipped
[`skills/writing-for-agents/references/mechanics.md`](../skills/writing-for-agents/references/mechanics.md).

## Patterns and troubleshooting

- Workflow patterns (problem- vs tool-first; sequential; multi-MCP; iterative; …): [`references/patterns.md`](../skills/writing-for-agents/references/patterns.md)
- Packaging / trigger / MCP / instruction failures: [`references/troubleshooting.md`](../skills/writing-for-agents/references/troubleshooting.md)

## Improve / test (skill TDD)

After authoring or editing:

1. Structural: `python3 scripts/quick_validate.py skills/<name>` (CI also validates all skills).
2. Behavioral under **`tdd`**: triggering (should / should-not), functional outputs, baseline comparison when claiming improvement.
3. Prefer **one hard task** until it succeeds, then extract into the skill; expand suites after.

Depth: [`skills/tdd/references/skill-testing.md`](../skills/tdd/references/skill-testing.md).

Scaffold CLI: `python3 scripts/init_skill.py <name>` (optional `--resources scripts,references,assets`).

## Related

- Glossary: [CONTEXT.md](../CONTEXT.md)
- Ops commands: [AGENTS.md](../AGENTS.md) (Setup / Testing / Code style pointers)
- Writing levers: [`skills/writing-for-agents`](../skills/writing-for-agents/SKILL.md)
- Scripts policy: [skill-scripts.md](skill-scripts.md)
- How-to maintainers: [docs/how-to-bmurrtech-skills.md](../docs/how-to-bmurrtech-skills.md#library-maintainers-this-repo)
