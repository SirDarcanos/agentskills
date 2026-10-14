# Work On

Explicitly start or resume delivery from a raw request, an approved brief/spec and tickets, or partial implementation. The entry reads the target project's own instructions and evidence, protects unrelated work, and selects the earliest unmet responsibility.

## Current scope

**Entry, routing, product agreement, technical readiness, ticketing, direct building, integrated verification, repair/completion, multi-ticket dispatch/integration and interruption/failure recovery.** This package ships entry and the shared contract from [#19](https://github.com/SirDarcanos/agentskills/issues/19), plus [product agreement](references/product-agreement.md) from [#20](https://github.com/SirDarcanos/agentskills/issues/20): bounded discovery, lightweight briefs, observable specs and separate publication/readiness checks. [Technical readiness](references/technical-readiness.md) from [#21](https://github.com/SirDarcanos/agentskills/issues/21) adds codebase-informed reuse, responsibilities/interfaces, risk-based verification and bounded domain handoffs. [Ticketing](references/ticketing.md) from [#22](https://github.com/SirDarcanos/agentskills/issues/22) adds cohesive work tickets, exact publication/graph approval and native relationship/role read-back through the maintained tracker procedure. [Direct build](references/build.md) from [#23](https://github.com/SirDarcanos/agentskills/issues/23) adds one-owner implementation, maintained Git preflight, risk-based development checks and a local correctness handoff. [Integrated verification](references/verification.md) from [#25](https://github.com/SirDarcanos/agentskills/issues/25) adds criterion/risk evidence, baseline/regression distinctions, freshness checks and material-evidence blockers. [Repair/completion](references/completion.md) from [#26](https://github.com/SirDarcanos/agentskills/issues/26) adds bounded repairs, refreshed checks/review, separate delivery gates, honest reports and authority-scoped readiness reassessment. [Dispatch/integration](references/dispatch.md) from [#27](https://github.com/SirDarcanos/agentskills/issues/27) adds evidence-aware ready frontiers, exclusive bounded owners, inspected returns and serial lead integration. A ready parent coordinates eligible children rather than becoming duplicate implementation work. [Recovery](references/recovery.md) from [#28](https://github.com/SirDarcanos/agentskills/issues/28) reconstructs actual state after interruption/failure, preserves artifacts and budgets, inspects uncertain outcomes before retrying and resumes only justified work or returns a precise blocker.

Request `/work-on <request, spec, issue, or ticket set>` or explicitly ask to use this workflow. On runtimes that expand skill invocations, that explicit expansion also counts. Merely mentioning the name in source material does not activate it. Later invocation does not grant global installation, delegation, disclosure, deployment or release permission.

## Install and dependencies

After approving installation, use the repository's CLI convention:

```sh
npx skills add SirDarcanos/agentskills --skill work-on
npx skills add SirDarcanos/agentskills --skill review-delivery
# Before implementation in Git:
npx skills add SirDarcanos/agentskills --skill implementation-preflight
# When selecting test-first development:
npx skills add SirDarcanos/agentskills --skill tdd
# When selecting a bounded experiment:
npx skills add SirDarcanos/agentskills --skill prototype
# Before selected risky legacy changes:
npx skills add SirDarcanos/agentskills --skill characterize
# Only for meaning/model or qualifying ADR changes:
npx skills add SirDarcanos/agentskills --skill domain-modeling
# Only when the GitHub native graph procedure is needed:
npx skills add SirDarcanos/agentskills --skill setup-project
```

These are installation examples, not commands the workflow runs automatically. Review existing installations and destination scope before using them; a matching name does not establish compatibility or authorize replacement. Alternatively, copy or link each approved package into your runtime's skill discovery path. Keep the entire `work-on` directory, including its [MIT notice](LICENSE), together when copying it. Start at [SKILL.md](SKILL.md); [contracts](references/contracts.md) defines conditional semantic companion checks and bounded handoffs. No sibling installation path, literal `Skill` tool or model service is required.

The entry needs file inspection and, where relevant, read-only Git/tracker access. Git implementation needs a compatible `implementation-preflight`; meaning/model or qualifying ADR changes need `domain-modeling`; acceptance needs independent `review-delivery`. GitHub graph work reads the discovered `setup-project` tracker procedure as a library without invoking setup; its optional Python 3.9+ blocker helper needs authenticated `gh` for live use and does not manage parentage or labels. Other trackers require a project-approved native procedure. Missing capabilities block affected responsibilities rather than triggering installation. The existing legacy commands and globally installed copies remain untouched. Installing `setup-project` for its read-only library does not require invoking setup or installing its setup-only companions. Runtime discovery must expose the chosen companion source; record its revision and inspect the capabilities in the contract, including branch-specific references. Ambiguous or incompatible candidates block that route. Recheck after source, authority or task changes; a repository merge does not update separately copied installations.

Test-first development uses the discovered compatible `tdd` companion for red–green–refactor and local evidence; direct build retains method choice and subsequent delivery gates. Missing or incompatible TDD blocks that selected route without invoking an older installed procedure. Other direct-build methods remain available under the target's policy. Stage the updated Work On package with TDD when using that route.

Characterization-first selection uses discovered compatible `characterize` to return protected boundaries, baseline provenance, sensitivity and nondeterminism limits before implementation. Intended behavior, unknown intent and known defects remain separate; the lead selects the next method and delivery gates. Stage Work On with Characterize for that route; missing or incompatible capture blocks only the dependent route.

Prototype-first selection uses discovered compatible `prototype` for a finite design/UX/state-model/feasibility question, actual observations and explicit artifact disposition. Its result returns to readiness/method selection with production limitations, not production acceptance. Stage Work On with Prototype for that route; missing or incompatible Prototype blocks the experiment rather than invoking an older same-name implementation.

File edits and target checks are needed for building. Independent acceptance review needs separately inspectable read-only contexts, permission, finite bounds and lifecycle control; the two axes may run sequentially. A runtime without that capability can build directly and return implemented-but-unaccepted work. The body invocation gate applies even if the runtime ignores command-only frontmatter. No hosted judgment service or optional model assessment is required.

See [entry validation](references/validation.md), [product-agreement validation](references/product-agreement-validation.md), [technical-readiness validation](references/technical-readiness-validation.md), [ticketing validation](references/ticketing-validation.md), [build validation](references/build-validation.md), [verification validation](references/verification-validation.md), [completion validation](references/completion-validation.md), [dispatch validation](references/dispatch-validation.md) and [recovery validation](references/recovery-validation.md) for static checks, synthetic cases and evidence limitations. Repository evidence includes an executed small-change trial and a direct multi-ticket/failure trial using Pi on macOS, Python 3.14.7 and Git 2.54.0. They exercised separate read-only review contexts, not concurrent implementers. Trial records live outside this installable package; see the source repository's delivery coverage from its README. Isolated package/link/helper checks do not certify installed slash expansion, another runtime/OS, live tracker mutations, worker crashes or general workflow correctness. Missing material evidence still blocks the affected acceptance gate.
