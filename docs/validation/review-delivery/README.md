# Review Delivery delivery evidence

Repository-only evidence for [#24](https://github.com/SirDarcanos/agentskills/issues/24), delivered through PRs [#39](https://github.com/SirDarcanos/agentskills/pull/39) and [#40](https://github.com/SirDarcanos/agentskills/pull/40). These records are not part of the independently installed `review-delivery` package and are not runtime instructions.

| Record | Purpose |
| --- | --- |
| [Specialist handoff checks](specialist-handoffs.md) | #65 adaptation checks, acceptance mapping and independent-review permission blocker |
| [Implementation checks](implementation-checks.md) | Historical direct/static/offline checks and initial evidence limits |
| [First trial attempt](trial-attempt.md) | Actual reviewer startup failure, preserved as history |
| [Executed retry](trial-results.md) | Independent dirty/untracked findings, stale-scope and unavailable-capability outcomes; scope and limitations |
| [Standards report](reports/standards.md) | Full portable reviewer output, initial report plus separate phase-two outcomes |
| [Spec report](reports/spec.md) | Full portable reviewer output, initial report plus separate phase-two outcomes |

## Package boundary

The maintainer requested that session-specific trial history and full model reports remain repository evidence rather than ship to consumers. They were moved here from `review-delivery/references/`; the initial implementation record was also extracted from the package's validation reference. Original report content and hashes remain recorded; relative links and evidence ownership pointers were reconciled.

The installable package retains its entry point, runtime [scope](../../../review-delivery/references/scope.md) and [report](../../../review-delivery/references/report.md) contracts, concise [validation instructions](../../../review-delivery/references/validation.md), and reusable scripts/checks. Package-local Markdown links stay within that copied directory; the skill does not require this evidence tree or load a ticket's execution history during use.

## Relocation verification

Executed with Python 3.14.7 / Git 2.54.0: all 11 helper checks passed in the source package and again in an isolated copy. The copied package also generated a fresh matching fixture without the repository evidence tree. Link/anchor assertions passed for 9 package-local links and 33 repository links, with every package target remaining inside the installable directory; both moved reviewer reports were byte-identical to their prior committed copies. The first isolation check caught an obsolete empty `trial-reports/` directory, which was removed before the passing rerun. Final `git diff --cached --check` passed before commit. These are direct local checks, not another reviewer trial or HTML rendering run.

This is documentation/evidence placement, not changed review behavior or a new architectural/package decision. No additional changelog entry, release-impact label, domain/ADR change, runtime installation or renewed agent trial is required. Existing independent trial evidence remains tied to its recorded sources and scope; the relocation is validated through link, content-preservation, privacy and isolated-package checks. Keep #24 open pending acceptance/merge under project policy.
