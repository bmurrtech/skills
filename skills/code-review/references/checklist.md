# Review checklist

Read on the **Standards** axis when the diff touches code, config, or scripts. Skip items tooling already enforces in the target repo. Cite `file:line` (or hunk) per finding.

## Security

- Hardcoded secrets, tokens, `.env` commits
- Untrusted input reaching queries, shells, HTML, or eval
- AuthZ gaps on state-changing paths
- Unsafe install/docs (`curl | sh` without read-first)

## Quality

- Functions / nesting that obscure the change (guideline: shallow diffs preferred)
- Clear names; no commented-out dead blocks in the diff
- Error handling at boundaries; no silent swallow in new paths

## Performance

- Obvious N+1 / repeated work in hot paths introduced by the diff
- Unnecessary full-suite or network work in tests added here

## Maintainability

- Duplication of logic already in-tree
- Coupling / wrong-layer imports introduced by the change
- Public API / docs drift when the diff changes a contract

## Tests

Align with **`tdd`** when that skill is loaded (see SKILL.md TDD gate). Always apply:

- Critical new/changed behavior has a regression seam (or an explicit “no seam” note)
- Assertions check **behavior** through public interfaces — not private structure
- Expected values come from an independent source of truth (literals, worked examples, spec) — not a tautology that rebuilds the implementation
- No implementation-coupled mocks of internals as the only proof
- Session-scoped runs preferred (OKF test-maps / AGENTS Test index when present) — flag suite-stuffing or narrating the whole `tests/` tree as the review plan
