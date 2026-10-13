# Review Delivery

Review delivered changes from two independent perspectives: **Standards** and **Spec**. Scope includes committed changes, staged and unstaged work, and relevant untracked files. Pinned manifests and a final freshness comparison keep old reviews from covering new work.

Use `/review-delivery <scope>` or supply a bounded review handoff. The entry point is discoverable by delivery workflows; loading it does not authorize delegation. This package coexists with `code-review` and does not change its installed copy.

## Install

After approving installation:

```sh
npx skills add SirDarcanos/agentskills --skill review-delivery
```

Alternatively, copy or link this entire directory, including its [MIT notice](LICENSE), into your runtime's discovery path. Inspect colliding installations before replacement. No sibling `work-on` directory or legacy review command is required. Callers discover the package, read its complete entry point and selected references, and check semantic compatibility rather than relying on a name or version string. Record the resolved source/revision and recheck when it changes. Repository merges do not update separately copied installations.

## Requirements and limits

- File inspection and actual project instructions, approved spec/brief, raw verification evidence.
- Permission and runtime support for two distinct read-only reviewer contexts, independent of authors and each other's conclusions. They may run sequentially; finite bounds and separately inspectable results are required.
- Git for Git comparisons; an authorized before/after manifest outside Git.
- Optional Python 3.9+ and Git for the shipped scope fingerprint helper. It uses only the standard library, captures explicit file paths and does not discover scope, run reviewers or repair findings.

Missing independence or material scope/evidence blocks delivery acceptance. Lead self-review remains useful but is not independent review. No hosted service, model voting, installation or global command replacement is required. Reports do not imply merge or release permission.

Read [SKILL.md](SKILL.md) for the procedure, [scope](references/scope.md) for fingerprinting and freshness limits, [report](references/report.md) for findings, and [validation](references/validation.md) for portable local checks and behavioral trial scenarios. Keep this whole directory when copying the package. Repository trial evidence exercised dirty/untracked findings, stale review and a small-change plus multi-ticket/failure route with separate Pi contexts on macOS. It remains outside the installed package; the source repository's README links the evidence and gaps. Isolated copying and helper tests verify packaging, not installed slash expansion or cross-runtime certification. No runtime adapter is claimed.
