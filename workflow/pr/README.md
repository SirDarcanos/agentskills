# PR

Prepare an outcome-first PR summary a maintainer can judge without reading code: what changed or was fixed, whether meaningful verification succeeded, and what decision or action remains. Aim for 100–200 words for routine changes, with more room for consequential risks or migrations.

Keep technical accounting and original review reports in separate supporting evidence, linked once when useful. Unchanged infrastructure needs no public boilerplate; material failed/unrun/stale checks, findings, protection changes and required actions stay visible. Use `Closes #X` for intended issue closure and `Refs #X` for related issues that should remain open.

Ask “write a PR report” or “open/update this PR,” or supply a bounded delivery handoff. Reporting does not authorize publication. Current complete implementation/review evidence is reused; unknown measurements and stale checks remain visible. A complete report may describe blocked delivery.

## Installation and dependencies

After approving installation:

```sh
npx skills add SirDarcanos/agentskills --skill pr
```

Copy the complete package, including [MIT notice](LICENSE). Start at [SKILL.md](SKILL.md). This is an original implementation using repository-owned delivery contracts; it does not import the installed diagram-first PR/show-me template. It does not replace an installed same-name skill.

File inspection and existing evidence suffice for a report. Git/host tools are conditional on repository/PR actions; GitHub examples use authenticated `gh`. Discover companions through the target/runtime catalog or explicit approved source, not sibling paths:

- `review-delivery` owns independent Standards/Spec review and full dirty-scope snapshots when missing review evidence must be obtained. Its absence blocks acceptance claims, not an honest report.
- `implementation-preflight` is required before authorized branch/commit preparation, not for ordinary report drafting.
- `work-on`'s execution library and the root ledger are required before delegated/corrective routes; reading the library does not invoke delivery. PR does not implement repairs.

Read complete resolved entries and conditional references and check semantic compatibility. Missing/ambiguous/incompatible helpers block only their dependent route; installation, paid benchmarks and model calls are never automatic fallbacks. No worker/model service is required. Public mutation needs task/project authority and disclosure approval; publication is read back. Merge, closure, deployment, release and installed migration remain separate.

See [validation](references/validation.md) for checks and fixture expectations. Repository-only execution evidence is kept outside this installable package. Offline fixtures establish accounting/report checks, not hosted CI speed, live PR behavior or cross-runtime certification.
