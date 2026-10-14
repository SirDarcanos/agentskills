# Spec review — #68

## Scope and independence

Reviewed the supplied frozen scope on `feat/work-on-spec`, base/HEAD `330bf0736519b4b96a873050bb542924b1f2fa38`.

Inspected:
- Scope manifest and complete tracked raw patch.
- Both primary agreements.
- Every new `work-on-spec` file, including the complete executable fixture and MIT license.
- Changed Work On sources, both complete fixture scripts, and common build/contracts/verification/completion/recovery libraries.
- Applicable instructions, accepted composable design, inventory/validation mapping, Review Delivery contracts, public documentation changes and all four supplied raw logs.

Read-only and independent: no edits, execution, delegation, assessments, tracker operations or other reviewer conclusions.

## Review

**No issues found.**

### Correct: acceptance traceability

The binding requirements are #68 agreement lines 9–17 and #48 agreement lines 170–184. Coverage below concerns #68’s implementation contribution, not completion of the entire #48 specification.

| Requirement | Inspected source and evidence |
|---|---|
| **AC1 — independent package, portable discovery, single ownership** | `work-on-spec/SKILL.md:10–16` defines invocation, dependencies and blocked routes. `work-on-spec/README.md:9–24` documents complete-package installation and semantic discovery. Work On’s dispatch files now contain compatibility pointers only (`work-on/references/dispatch.md:3–7`, `dispatch-validation.md:3–5`). Common procedures remain in Work On rather than being copied. |
| **AC2 — two delivery scopes** | `work-on-spec/SKILL.md:10–14` establishes one overall lead and bounded writable Work On ticket agents; `work-on/SKILL.md:10–16` preserves local leadership without another worker pool. Missing writable runtime explicitly blocks execution rather than permitting direct whole-spec substitution. |
| **AC3 — lead decisions and integration ownership** | Local decisions are reused while cross-ticket decisions remain with the root (`work-on-spec/SKILL.md:22,32`). Coupled interfaces serialize, including lead writes (`references/dispatch.md:21`); inspected results integrate one at a time (`:41–43`). |
| **AC4 — evidence reuse/invalidation** | `work-on-spec/SKILL.md:22` requires inspection and targeted reassessment, not repeat specialist calls. `references/aggregate.md:7–9` adds integrated acceptance mapping and state-sensitive reruns. The single-change fixture exercises reuse/invalidation; the coordination fixture demonstrates changed fingerprints and cross-ticket sensitivity (`scripts/check-coordination-fixture.py:161–198`). Autonomous composed reuse remains unproven. |
| **AC10/11 — optional models and shared history** | The coordinator consumes Work On’s sole execution contract (`SKILL.md:12`). `work-on/references/contracts.md:78–82` gates calls, reserves shared allowance, retains failed/unknown usage and prohibits silent substitution. `work-on-spec/references/recovery.md:19` preserves those bounds across replacement/resume. Individual assessment-package implementation is outside this review. |
| **AC13 — delivery integrity** | Native relationships, parent coordination and accepted prerequisite integration govern eligibility (`references/dispatch.md:7–19`). Ownership, finite assignments and inspected returns appear at `:27–43`. Aggregate review uses independent axes and retained checkpoint lineage (`references/aggregate.md:15–23`). Recovery retains uncertain owners/effects and reconciles before replay (`references/recovery.md:11–27`). |
| **AC14 — transfer/documentation** | Source transfer matches accepted design `docs/design/composable-delivery.md:53–55,154`. Work On loses duplicate scheduling/overall recovery while retaining local recovery. Listings, package documentation, design implementation pointer and `CHANGELOG.md:12` reflect the new boundary. New and source-package MIT notices name Nicola Mustone. No installed migration is claimed. |
| **AC15 / #68 verification** | Fixture methods cover parent/prerequisite evidence, shared ownership, one unavailable slot, failure, uncertain integration, resume history and actual serial local Git integration (`check-coordination-fixture.py:80–217`). Synthetic decisions and static guards are explicitly distinguished from autonomous execution. |

## Evidence and limitations

- **Executed by the supplied evidence producer, not this reviewer:** coordination and single-change logs each report eight passing tests. Expected assertion failures and unavailable-check failures remain visible.
- **Actual tool behavior:** the coordination script creates disposable Git artifacts, integrates serially, detects an injected cross-ticket regression and verifies restoration/protected state.
- **Synthetic only:** eligibility, acceptance, worker lifecycle and exhausted-budget decisions are authored fixture inputs—not observed ticket-agent decisions.
- **Static/report evidence:** Markdown/frontmatter/link counts and isolated-package results are recorded in the supplied logs. I inspected Markdown source, not rendered HTML or the unavailable checker implementation.
- **Unrun here:** all commands and independent freshness recapture. Frozen-source identity relies on the supplied scope/freeze.
- **Not demonstrated:** live native API/pagination, writable worker-runtime discovery, actual worker interruption, autonomous multi-ticket delivery or installed discovery. These remain explicitly unexecuted (`work-on-spec/references/validation.md:19`), consistent with later #72/#73 trials—not silently satisfied by fixtures.

No blocking, nonblocking or decision-required defect identified.

**Merge verdict: OK with notes** — review recommendation only; no acceptance or merge action authorized.

**Next action:** retain these limitations and complete #72’s observable autonomous failure/resume trial before claiming composed runtime proof.