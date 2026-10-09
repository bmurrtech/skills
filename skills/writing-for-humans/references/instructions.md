# Instructions

Read when mode is **Instructions** or when a Mixed section is actionable
(procedure, commands, verify, recovery). Goal: make an action easy to
identify, perform, and verify.

For a stricter controlled overlay (short sentences, fixed verb set), also
read [controlled.md](controlled.md) when the user asks for it.

## Direct actions

Prefer imperative verbs: Open, Select, Enter, Create, Run, Compare, Save,
Remove, Verify, Check, Restart, Configure. Name the target (what, where,
required value/state).

Prefer: `Set max_connections to 100.`  
Avoid: `Configure the setting appropriately.`

Do not force a direct verb when it makes the sentence unnatural or wrong.

## Exact names

Preserve UI labels, commands, flags, API parameters, paths, env vars,
config keys, error messages, product/service names, and version ids.

Explain a command in prose if helpful; keep the command itself exact.
Do not replace `systemctl is-active nginx` with a vague paraphrase as the
only instruction.

## Sequence

Order by dependency: prerequisites → actions → verification → recovery.
One primary operation per step when risk, outcome, or verification differs.
Combine tightly coupled actions when splitting only adds clutter.

## Conditions, outcomes, verify, recover

State branches explicitly (`If the service is inactive, inspect the log.`).
State expected outcomes when useful; do not invent exact output — describe
the expected state when it varies.

Verification must be observable, specific, relevant, and proportionate.
Skip decorative checks. For troubleshooting and higher-risk procedures,
add recovery when verification fails.

Prefer decision trees over a fake linear path when symptoms diverge.

## Commands and code

Do not rewrite syntax for style. Explain placeholders
(`<registry>` = registry hostname). Mark illustrative values as examples —
never present sample tokens/hosts as required literals. State execution
context when it matters (OS, shell, container, privileges, version).

## Warnings

When an action can cause data loss, downtime, security exposure, privilege
change, irreversible change, or production impact: state the risk **before**
the dangerous step. Do not decorate routine actions with fake warnings.
