# Skill anatomy

## Required

```
skills/<name>/
├── SKILL.md              # YAML frontmatter + Markdown body
└── agents/
    └── openai.yaml       # Host UI metadata + invocation policy
```

`init_skill.py` always creates `agents/openai.yaml`.

### agents/openai.yaml

```yaml
interface:
  display_name: "Implement"
  short_description: "Build work from a spec or tickets"
policy:
  allow_implicit_invocation: false
```

- Quote string values; keep keys unquoted.
- `allow_implicit_invocation: true` only when the skill should model-trigger (aligned with a model-facing `description` and no `disable-model-invocation`).
- Optional later: `interface.default_prompt`, icons, `dependencies.tools` (host-specific).

## Optional bundled resources

| Dir | Role | Load into context? |
|-----|------|--------------------|
| `scripts/` | Deterministic helpers (Python/shell) | Usually run, not pasted |
| `references/` | On-demand docs | Yes, when linked step says so |
| `assets/` | Output templates / binaries | Copied into outputs, not as guidance |

Create a resource directory only when the skill needs it.

## Degrees of freedom

- **High** — prose steps when many approaches work
- **Medium** — parameterized scripts when a preferred path exists
- **Low** — fixed scripts when sequence must not vary

Match freedom to fragility: narrow bridges get guardrails; open fields do not.
