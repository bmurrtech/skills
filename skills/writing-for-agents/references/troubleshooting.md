# Skill packaging and runtime troubleshooting

Read when a skill fails to validate, trigger, or execute. Pair with
[mechanics.md](mechanics.md) (layout + description) and **`tdd`**
[skill-testing.md](../../tdd/references/skill-testing.md) (behavior suites).

## Won't validate / won't load as a skill

### Missing or wrong entry file

**Error shape:** could not find `SKILL.md` in the skill folder  
**Cause:** file not named exactly `SKILL.md`  
**Fix:** rename (case-sensitive). `ls` / directory listing must show `SKILL.md`.

### Invalid frontmatter

**Cause:** YAML delimiters or quotes broken.

```yaml
# Wrong — missing --- delimiters
name: my-skill
description: Does things

# Wrong — unclosed quotes
description: "Does things

# Correct
---
name: my-skill
description: Does things
---
```

### Invalid skill name

**Cause:** spaces, capitals, or underscores.

```yaml
# Wrong
name: My Cool Skill

# Correct
name: my-cool-skill
```

Folder name must match `name`. This library: also require `agents/openai.yaml`;
no skill-folder `README.md`. Run `python3 scripts/quick_validate.py skills/<name>`
when present.

## Doesn't trigger

**Symptom:** skill never loads automatically.

**Fix:** revise `description` (what + when + key capabilities; real user
phrases). Checklist:

- Too generic? (“Helps with projects” fails)
- Missing trigger phrases users would say?
- Missing file types when relevant?

**Debug:** ask the agent “When would you use the `<skill-name>` skill?” — it
should surface the description. Adjust what is missing. Then re-run **`tdd`**
triggering suites.

## Triggers too often

**Symptom:** loads on unrelated queries; users disable it.

1. Add **negative** triggers:

```yaml
description: >
  Advanced data analysis for CSV files. Use for statistical modeling,
  regression, clustering. Do NOT use for simple data exploration (use
  data-viz skill instead).
```

2. Narrow scope (“PDF legal documents for contract review” not “processes
   documents”).
3. Clarify product/domain boundaries.

## MCP / tool connection issues

**Symptom:** skill loads but tool calls fail.

1. Confirm the MCP/server is connected in the host.
2. Auth: keys valid, scopes granted, tokens refreshed.
3. Test the tool **without** the skill (“use X to fetch my projects”). If that
   fails, the skill is not the root cause.
4. Verify tool names in the skill match the server (case-sensitive).

## Instructions not followed

| Cause | Fix |
|-------|-----|
| Too verbose | Shorten; bullets/numbers; move detail to `references/` |
| Buried rules | Put critical rules near the top; `## Critical` when needed |
| Ambiguous language | Concrete checks before side effects (lists, not “validate properly”) |
| Critical exactness | Prefer a bundled **script** for deterministic checks — language is not |
| Skipping steps | Explicit “do not skip validation”; thoroughness cues often work better in the **user prompt** than buried in `SKILL.md` |

## Large context / slow or degraded replies

| Cause | Fix |
|-------|-----|
| Fat `SKILL.md` | Move detail to `references/`; link with when-to-read; keep body lean (aim well under ~5k words) |
| Too many skills enabled | Prefer selective enablement; related “packs” over enabling everything |
| No progressive disclosure | Inline only what every branch needs; disclose the rest |
