# Decision tree template (Doop)

**Need:** branching rules (status → path; bought vs declined vs stale).

## Layout

- Root at left/top; decision nodes marked; each outbound edge has a **guard** label.
- Leaves = actions or terminals; restack instead of crossing spaghetti.

Pair with [lifecycle-template.md](lifecycle-template.md) when the room argues branching policy.
