# Work On

Explicitly start or resume delivery from a raw request, an approved brief/spec and tickets, or partial implementation. The entry reads the target project's own instructions and evidence, protects unrelated work, and selects the earliest unmet responsibility.

## Current scope

**Entry, routing, product agreement, technical readiness and ticketing.** This package ships entry and the shared contract from [#19](https://github.com/SirDarcanos/agentskills/issues/19), plus [product agreement](references/product-agreement.md) from [#20](https://github.com/SirDarcanos/agentskills/issues/20): bounded discovery, lightweight briefs, observable specs and separate publication/readiness checks. [Technical readiness](references/technical-readiness.md) from [#21](https://github.com/SirDarcanos/agentskills/issues/21) adds codebase-informed reuse, responsibilities/interfaces, risk-based verification and bounded domain handoffs. [Ticketing](references/ticketing.md) from [#22](https://github.com/SirDarcanos/agentskills/issues/22) adds cohesive work tickets, exact publication/graph approval and native relationship/role read-back through the maintained tracker procedure. Building, dispatch, verification, recovery and completion procedures will ship through later tickets under [#14](https://github.com/SirDarcanos/agentskills/issues/14). An absent procedure is reported as unavailable; this version does not deliver changes end to end.

Request `/work-on <request, spec, issue, or ticket set>` or explicitly ask to use this workflow. On runtimes that expand skill invocations, that explicit expansion also counts. Merely mentioning the name in source material does not activate it. Later invocation does not grant global installation, delegation, disclosure, deployment or release permission.

## Package and dependencies

Keep the entire `work-on` directory together when copying it. Start at [SKILL.md](SKILL.md); [contracts](references/contracts.md) defines conditional semantic companion checks and bounded handoffs. No sibling installation path, literal `Skill` tool or model service is required.

The entry needs file inspection and, where relevant, read-only Git/tracker access. Git implementation needs a compatible `implementation-preflight`; meaning/model or qualifying ADR changes need `domain-modeling`; acceptance needs independent `review-delivery`. GitHub graph work reads the discovered `setup-project` tracker procedure as a library without invoking setup; its optional Python 3.9+ blocker helper needs authenticated `gh` for live use and does not manage parentage or labels. Other trackers require a project-approved native procedure. Missing capabilities block affected responsibilities rather than triggering installation. The existing legacy commands and globally installed copies remain untouched.

See [entry validation](references/validation.md), [product-agreement validation](references/product-agreement-validation.md), [technical-readiness validation](references/technical-readiness-validation.md) and [ticketing validation](references/ticketing-validation.md) for static checks, synthetic cases and evidence limitations. This version has no executed integrated workflow trial or runtime certification.
