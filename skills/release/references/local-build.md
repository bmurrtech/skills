# Local build validation

Read in step 4.

## Levels (where applicable)

1. **Tests** — repository-required checks
2. **Release build** — actual artifact or nearest local equivalent
3. **Artifact verification** — names, contents, exclusions, version, checksums
4. **Container reproduction** — only if contract requires Docker

Remote CI remains authoritative after local success.

## Docker

Conditional. Probe only when the contract needs it. Missing Docker when required
→ stop before tag; explain; do not weaken validation.
