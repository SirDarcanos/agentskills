# Single-change validation

Read when changing or exercising #67's entry, method composition or shared ledger. [Entry checks](validation.md#reproducible-static-checks) still apply; preserve historical #14 trial records rather than rewriting their outcomes. This package contains instructions, not an executable delivery controller.

## Offline fixtures

With Python 3.9+ and Git, from the repository root:

```sh
python3 -B workflow/work-on/scripts/check-single-change-fixture.py
```

From a copied package resolve `scripts/check-single-change-fixture.py` relative to that package. The script creates temporary local Git fixtures with a synthetic commit identity, runs bounded subprocesses and removes only its own temporary directory. Git-control environment variables are stripped, global/system configuration is isolated, and hooks/templates are disabled. A separate sacrificial sandbox verifies hostile repository/worktree/index/template/config overrides cannot escape the fixture. No remote tracker/PR, installed discovery, delegation, services or model calls occur. Do not run it against a user's project.

| Fixture | Executed scope and failure protected |
| --- | --- |
| Direct change | Local branch, existing baseline, meaningful whitespace regression red, implementation green, protected staged/unstaged/untracked/link state unchanged |
| Ready bug ticket | Retained synthetic cause/reproduction/source identity consumed directly; implementation/regression check without a second diagnostic run |
| Stale evidence | Deciding source digest drifts; actual check rejects the new bad state, dependent check refreshed while unaffected evidence remains current |
| Method composition | Baseline protection then test-first increment; baseline artifact preserved and one ledger/history retained |
| Missing optional model | Explicit none/absent endpoint fixture performs ordinary implementation/checks with zero attempted model requests |
| Material-check blocker | Focused pass plus truly absent required integration check; observed process failure remains unavailable, no install or repair retry |
| Git environment isolation | Hostile Git variables target a separate sacrificial repository/index and hook templates; fixture init/add/commit remain local, external bytes/modes/HEAD stay unchanged and no hook marker appears |
| Static guard assertions | Metadata/body handoff gates, no routine method questionnaire/self-review substitution/nested pools, retained shared repair/model history and inactive dispatch boundary |
| Portable authority/source-target guards | Required-review grant and limits remain in the shipped contract; entry points to it, blanket delegation denial does not return, and reusable fixes target tracked sources rather than local policy or installed copies |

The caller steps and ledger objects in these fixtures are synthetic test oracles, not runtime enforcement. They demonstrate executable checks, dirty-work preservation, drift and the modeled handoffs. Static text assertions guard accidental deletion of instructions; they do not prove an agent follows them. These fixtures neither independently review the formatter nor accept its delivery. Full autonomous composed agent/installed-runtime and live tracker/PR/model paths remain unexecuted by this script.

## Required-review authority cases

Read [required-review authority](contracts.md#required-review-authority) and the discovered Review Delivery handoff when exercising these cases. Use independently copied packages and a synthetic target with no local standing-permission policy. The table specifies expected decisions, not executed agent behavior; source guards check instruction presence only.

| Case | Required observation |
| --- | --- |
| Explicit Work On delivery, no local permission policy | Originating request supplies review authority; root reserves bounded Standards/Spec contexts without asking for delegation again. |
| Work On Spec delivery / assigned ticket | Same authority is inherited from the overall request; ticket lead asks the existing root to launch reviews, never a nested pool. |
| Explicit user/project/runtime prohibition | Restriction wins; no unauthorized reviewer launches, and independent acceptance remains blocked. |
| One slot / missing bounded runtime | Sequence axes with one available slot; genuinely missing capability preserves implemented-but-unaccepted work, not a fictitious permission gap. |
| New disclosure/spending or optional worker/assessment | Required review grants none of those extra effects; obtain their separate approval or report the affected blocker. |
| Library read or investigation-only request | No delivery execution authority is originated; standalone review must establish its own permission. |
| Reusable-skill correction | Actual diff changes tracked skill behavior; local policy alone cannot satisfy acceptance and installed copies remain protected. |

When running an agent exercise, record actual launches, prompts, protected manifests, reviewer outputs and limitations separately from this authored matrix. No live tracker mutation, service call or installation is needed to inspect these instructions.

## Acceptance mapping

- #48 AC1–AC4: independently owned procedures and authorized single-change lead/handoff; discovery and retained adapters consume specialist returns rather than duplicate them.
- AC6–AC7: all five method capabilities are inspected at cutover; selected packages own their loops, with explicit sequential returns and retained evidence/ledger.
- AC4/AC7: complete current bug evidence bypasses reinvestigation; invalidated facts get targeted refresh.
- AC10/AC11: [optional model allocations](contracts.md#optional-model-allocations) consume exact policy and root reservations, retain shared attempted usage and keep unavailable/insufficient-data outcomes distinct. No autonomous calls occur without permission.
- AC12: PR owns impact/report/publication; Work On keeps verification, review and delivery gates. No report or fixture pass implies acceptance.
- AC13–AC15: root-owned capacity, finding/repair/model history, independent dirty-scope review, documentation and isolated-package checks remain explicit. Installed replacement and whole-spec scheduling are excluded.

For agent exercises, additionally record actual invocation/approval, runtime, companion source identities, tools/effects, protected manifests, root ledger/repair counts, local versus integrated snapshots, independent axis reports and all failed/stale/not-run checks. A hand-authored scenario is not an executed agent trial.

## Evidence retention

Retain per-change results through the [lead evidence record](contracts.md#lead-evidence-record). The runnable script and this reference provide the reusable validation procedure.

## Documentation disposition

Entry/contract/build/adapters/recovery and retained dispatch status, package/root README and the existing Unreleased Work On Added entry change. No domain meaning, product agreement, ADR decision, label vocabulary, native graph or model policy changes; accepted design remains the rationale. Work On is unreleased, so update its one Added entry rather than create per-ticket history. The invocation boundary is incompatible; delivery PR impact is major, not publication authority.
