# Accepted residual security risk

Thin pointer — posture SoT is
[ADR 0011](adr/0011-ADR-skill-scanner-posture-prereqs.md)
(prerequisite-driven skills; no agent CLI download; local Spec; no font CDNs).

**Residual floor (expected):** `docx` may still MEDIUM on untrusted Word ingest /
CLI invoke after prereqs are met. Gate on unexplained new capabilities,
unreviewed remote execution, privilege escalation, or new untrusted→instructions
paths — not “zero MEDIUM.”

**`doop` / `ensure_doop.py`:** may invoke local `bun install` / `bun run dev` or
`docker compose` **only after** checkout identity (`package.json` name `doop` +
marker files) and live identity (`/healthz` or Doop HTML markers). Operator
clones Doop; the skill does not download it. `stop` kills only when cmdline/cwd
match expected bun-dev under `DOOP_HOME`. Residual MEDIUM on local subprocess
invoke is acceptable under ADR 0011 prerequisite posture — not agent-side
binary download.

Deferred: optional `gh` issue Spec for `code-review` →
`.scratch/ideas/code-review-optional-gh-issue-context.md` (promote via **`roadmap`**
only if asked).
