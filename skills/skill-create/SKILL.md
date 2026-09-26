---
name: skill-create
description: >
  Create or update Agent Skills under skills/ only: capture intent, plan
  bundled resources, scaffold with init_skill.py, write SKILL.md (description as
  trigger pointer), validate with quick_validate.py, iterate on real use. Use
  when adding a new skill, restructuring an existing one, or checking skill
  frontmatter and layout.
---

# skill-create

Build skills that change agent process — not dump knowledge the model already has.

## Hard constraint

Scaffold and edit skills **only** under `skills/<name>/`. Never use `.agents/`, `.claude/`, or `.cursor/` as this repo’s SoT.

## Workflow

### 1. Capture intent

Collect 2–3 concrete usage examples (user ask → expected agent behavior).

**Done when:** examples are written and the skill’s one-sentence purpose is clear.

### 2. Plan the bundle

Decide what belongs in the body vs `scripts/` vs `references/` vs `assets/`. Read [references/anatomy.md](references/anatomy.md) when unsure.

**Done when:** resource list is explicit (including “none”).

### 3. Initialize

```bash
python3 skills/skill-create/scripts/init_skill.py <skill-name>
```

Optional: `--resources scripts,references,assets` · `--allow-implicit` (sets `policy.allow_implicit_invocation: true`)

**Done when:** `skills/<skill-name>/SKILL.md` and `skills/<skill-name>/agents/openai.yaml` exist.

### 4. Write

- Frontmatter: `name` (kebab-case, matches folder) + `description` (what + when; trigger branches; front-load the leading word).
- `agents/openai.yaml`: set `display_name`, `short_description` (25–64 chars), and `policy.allow_implicit_invocation` aligned with whether the skill may model-trigger.
- Body: ordered steps with completion criteria; imperative voice; lean.
- Push branch-only material behind `references/` with when-to-read links.

Read [references/frontmatter.md](references/frontmatter.md) and [references/progressive-disclosure.md](references/progressive-disclosure.md) when drafting.

**Done when:** description alone would route the right queries; body has no always-irrelevant branches.

### 5. Validate

```bash
python3 skills/skill-create/scripts/quick_validate.py skills/<skill-name>
```

**Done when:** script exits 0.

### 6. Iterate

Run the skill on the examples from step 1; tighten description and steps from failures.

**Done when:** examples succeed without the skill fighting the default model.

## Further reading

- [references/anatomy.md](references/anatomy.md)
- [references/frontmatter.md](references/frontmatter.md)
- [references/progressive-disclosure.md](references/progressive-disclosure.md)
