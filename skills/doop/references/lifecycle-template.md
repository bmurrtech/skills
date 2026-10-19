# Lifecycle template (Doop)

**Need:** entity states + labeled transitions (lead status, ticket, subscription).

## Layout

- States as rounded nodes in reading order (left→right or clockwise).
- Transitions as labeled arrows (event / actor / automation).
- Loops drawn explicitly (e.g. follow-up until stale).
- Terminal states heavier (filled or double border).

## HTML hints

State pills min-width ~120px; edge labels carry meaning (not color alone). Soft band for “in progress” if useful.

## Pairing

Often with [pipeline-template.md](pipeline-template.md): pipeline = stages of work; lifecycle = entity status.
