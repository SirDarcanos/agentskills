# TDD

Implement a bounded feature or bug fix through red–green–refactor. Tests observe consumer-visible behavior, implementation grows one increment at a time, and refactoring keeps the relevant checks green.

Use it directly for a test-first request or through an authorized delivery handoff. The technical lead chooses routine test boundaries and strategy. Existing coverage is reused where sufficient; the method does not impose TDD on every project change or claim independent review or delivery acceptance.

## Installation and dependencies

After approving the installation scope:

```sh
npx skills add SirDarcanos/agentskills --skill tdd
```

Alternatively, copy or link this complete directory into your runtime's skill discovery path. Keep [SKILL.md](SKILL.md), shipped references/scripts and the [MIT notice](LICENSE) together. This is an installation example, not an automatically executed action. Installing a same-name replacement requires separate approval; repository merging does not update installed copies.

Established project guidance (or a meaningful equivalent) is required, including for direct use. Missing or conflicting common guidance returns a specific setup/reconciliation prerequisite; the method never runs Setup automatically. Ordinary scope, evidence and outcomes may remain in conversation under that agreement.

The method needs file inspection/editing and the target's relevant test tools. Before Git writes it needs a discovered compatible `implementation-preflight` or a current inspected result from the caller. Required domain/ADR changes use `domain-modeling`. Companions may live anywhere exposed by the runtime or an explicit approved location; a matching name alone does not prove compatibility. Missing helpers block only dependent work and never trigger installation.

Only delegation or recorded acceptance correction needs Work On's documented conditional coordination/repair library. Preserve root ownership, finite bounds and existing finding lineage/budgets; an old universal-contract-only package blocks those routes, not ordinary direct work. No installation or next stage is automatic.

## Attribution

This package is inspired by [Matt Pocock's TDD skill at revision `49dd158`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/tdd/SKILL.md), particularly behavioral tests, independent expected outcomes, rejection of implementation coupling and small test-first increments. Its [MIT license](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/LICENSE) notice is retained in this package's [LICENSE](LICENSE), alongside Nicola Mustone's notice for this implementation.

The procedure is newly written rather than a verbatim copy. It adds the approved authority/handoff contract, green refactoring and lead-selected seams; it does not inherit the older procedure's user-confirmation or review-only-refactoring rules.

## Validation

See [validation](references/validation.md) for package checks, an offline Python 3.9+ fixture and authored workflow cases. Run `python3 workflow/tdd/scripts/check-fixture.py` from the repository root. The fixture executes a synthetic red–green–refactor sequence, retains existing behavioral coverage and illustrates two rejected test anti-patterns. It is not an executed agent workflow or installed-runtime certification. No model service is required.
