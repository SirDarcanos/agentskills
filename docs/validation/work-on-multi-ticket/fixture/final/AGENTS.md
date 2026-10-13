# Synthetic project policy

Read REQUEST.md for approved behavior and tracker.json for mocked observations.
Lead owns the two ticket scopes and serial local integration. Scoped direct commits
on feature/name-report count as integration; synthetic acceptance requires current
relevant checks and independent Standards/Spec reports. Commit only owned paths.
Preserve sentinel.txt index/worktree bytes and executable mode, untracked-note.txt
and note-link. Freeze owned source/support files during reviews. Reviewers are
read-only and do not accept, close, mutate tracker state or delegate.
No production GitHub writes, installation, deployment or release. This disposable
fixture can be retained outside the repository; cleanup needs explicit disposition.
No fixture changelog or release publication; document behavior in README.md.
