# Progressive disclosure

Keep the top of `SKILL.md` legible. Push material down only when it earns the hop.

## Levels

1. **Metadata** — always available (`name`, `description`)
2. **Body** — loaded on trigger; prefer under ~500 lines
3. **Bundled refs/scripts/assets** — opened when a step says so

## Hierarchy inside the body

1. In-file steps (ordered actions + completion criteria)
2. In-file reference (rules consulted on demand)
3. Disclosed reference (`references/*.md` linked with **when to read**)

Inline what every branch needs. Disclose what only some branches need.

## Patterns

- Variant splits: `references/aws.md` vs `references/gcp.md` with a chooser step
- Long refs: start with a short TOC
- Avoid deep nesting of directories under the skill

## Completion criteria

Every step ends with a checkable done-when. Prefer exhaustive where correctness matters (“every modified skill validated”) over vague (“looks good”).
