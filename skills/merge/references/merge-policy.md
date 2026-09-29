# Merge policy

Read during readiness (step 2) and before submit (step 3).

## Source of truth

**GitHub mergeability and repository rules** are authoritative. Reviewers and
bots provide **evidence**, not policy.

Hard-stop examples (when configured as blocking):

- required status checks failing/pending
- required approving reviews missing
- changes-requested state
- required conversation resolution unmet
- merge queue required but not submitted
- conflict state / not mergeable

## Advisory findings

Optional review comments (including bot “please fix”) that are **not**
GitHub-enforced blockers: list materially before proceeding, then continue under
repository policy if the user still wants merge.

## Strategies

- Default: squash for short-lived review branches
- Use merge commit / rebase only when policy requires or history must be preserved
- Queue when required — do not bypass
