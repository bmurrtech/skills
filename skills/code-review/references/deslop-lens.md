# Deslop lens (review-only)

Read on the **Standards** axis when the diff looks AI-generated, over-abstracted, or noisy. This is a **finding lens**, not a full cleanup skill — report smells; do not start a rewrite unless the user asks to fix.

## Smell categories (prefer these names)

| Smell | Signal |
|-------|--------|
| Dead code | Unused exports, unreachable branches, stale flags, debug leftovers in the diff |
| Duplication | Copy-paste branches, near-identical helpers |
| Needless abstraction | Pass-through wrappers, speculative indirection, single-use layers |
| Boundary violation | Wrong-layer imports, hidden side effects, leaky responsibilities |
| Missing tests | Behavior changed with no seam lock |

## Severity hint

- **HIGH** — smell likely causes a bug, security hole, or blocks merge
- **MEDIUM** — real debt in the touched hunks; fix when cheap
- **LOW** — style / optional tidy

If the user asks to fix after review: lock behavior with the smallest regression check first, then one smell category at a time (dead → dup → naming/errors → tests).
