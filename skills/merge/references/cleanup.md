# Safe cleanup

Read after a confirmed merge (step 4).

Delete a review branch only when all hold:

- PR actually merged (not merely queued)
- branch no longer needed
- remote has no intentionally retained work
- local branch has no unique commits vs merged result
- no worktree or workflow depends on it

Otherwise: retain; report cleanup deferred.

Never use destructive reset as routine canonical sync. Prefer fetch +
fast-forward or rebase only when unique local work is absent or explicitly
handled.
