# Skill mechanics

Read when the document is a **skill** (`SKILL.md` + optional bundle). Covers
frontmatter, invocation, routers, and a must-pass checklist. For shared writing
levers (any agent doc), see [levers.md](levers.md).

## Frontmatter

Required:

- `name` — kebab-case, ≤64 chars, matches folder
- `description` — what **and** when; ≤1024 chars; the always-loaded **context
  pointer** (see levers)

Optional host fields (`license`, `allowed-tools`, `metadata`, …): prefer omit
unknowns.

Description rules (pointer jobs):

- Third person; front-load the **leading word**
- One trigger phrase per distinct **branch** (collapse synonyms)
- No identity fluff the body already states

## Invocation choice

Decide whether the host may model-trigger the skill:

| Intent | Frontmatter / policy |
|--------|----------------------|
| User-only / explicit invoke | `disable-model-invocation: true` and `policy.allow_implicit_invocation: false` |
| Model may auto-route | omit disable; `policy.allow_implicit_invocation: true` |

Keep description human/routing-facing either way. Align yaml policy with whether
the skill may model-trigger — mismatch is a variance bug.

**Split by invocation** when one folder tries to serve both a rare explicit
procedure and a high-frequency auto-route: two skills (or a thin router +
bodies), not one overloaded description.

## Router skills

A **router** skill's job is to choose or dispatch other skills — not to inline
their workflows.

- Description lists genuinely distinct branches (one trigger each)
- Body: short chooser + links/names of target skills
- Never paste a second skill's full steps; name it and stop
- Disclose long branch matrices under `references/` with when-to-read

## Must-pass checklist

Score before ship. Waive only with reason.

### Description (trigger pointer)

- [ ] Third person; what **and** when; front-load the leading word
- [ ] One trigger per distinct branch
- [ ] ≤1024 chars; no identity the body already carries
- [ ] If user-only, description stays routing-facing; policy matches

### Body shape

- [ ] Imperative steps in order; each ends with checkable **Done when**
      (clarity + demand — see levers)
- [ ] **Boundaries** (or equivalent) holds negative-imperative guardrails for
      real avoid-behaviours; omit only if none; no soft “prefer not” hedges
- [ ] Degrees of freedom match fragility (high prose / medium templates / low scripts)
- [ ] Repo-relative POSIX paths only

### Progressive disclosure

- [ ] Always-needed rules stay inline
- [ ] Branch-only / long lists in `references/` with when-to-read links
- [ ] Refs one level deep from `SKILL.md`
- [ ] Scripts are run (or “read as reference”), not pasted wholesale

### Anti-bloat

- [ ] No restating always-loaded host/ops/glossary material the environment already provides
- [ ] No host-only orchestration unless this skill's product is that host
- [ ] No second skill's full workflow inlined — link the skill name
- [ ] Output templates only when format is part of the contract
- [ ] No **no-ops** / **sediment** (see levers pruning)

### `agents/openai.yaml`

- [ ] `display_name`, `short_description` (25–64 chars)
- [ ] `policy.allow_implicit_invocation` matches model-trigger intent
