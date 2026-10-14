# Composable delivery design validation

For [#50](https://github.com/SirDarcanos/agentskills/issues/50), read with the [contract](composable-delivery.md) and [inventory](composable-delivery-inventory.md). This matrix assigns obligations, not completion. The paper checks below are authored and directly inspected design exercises, **not executed agent workflows, mock-transport tests, independent review or installed migration**.

## #48 acceptance traceability

| #48 criterion | Procedure owner / contract coverage | Downstream implementation and executed evidence owner |
| --- | --- | --- |
| AC1 independent packages | Every specialist/method row; envelope, semantic discovery and standalone stop boundary | #54–#66 and conditional existing companions; #70/#73 isolated/discovery checks |
| AC2 two delivery scopes | `work-on` local lead; `work-on-spec` overall lead and ticket agents | #67/#68; #71/#72 |
| AC3 lead decisions | `analyze` recommends, lead selects methods/checks; overall lead owns cross-ticket decisions | #60/#67/#68; #71/#72 |
| AC4 reusable evidence | `analyze`, research/investigation sources and both leads; deciding-input invalidation, no repeat-call loop | #54/#60/#64/#67/#68; #71/#72/#73 reuse and invalidation trials |
| AC5 discovery/artifacts | `shape-work`, `write-spec`, `write-tickets`; four dispositions and exact native persistence/read-back | #61–#63; #70 |
| AC6 methods now | All five method owners and sequential composition with local returns | #55–#59; #67 availability gate; #71/#73 all-five executed examples |
| AC7 bug to ticket | `investigate-bug` and `write-tickets`; complete ticket, duplicate/unconfirmed/unresolved/stale routes, no fix on investigation-only request | #64/#63/#67; #71 |
| AC8 research/domain reuse | `research`, `domain-modeling`; direct/authorized delegated research and selective record changes | #54/#60/#61/#64; #70/#73 |
| AC9 model agreement | `setup-project` owns approval/equivalent policy home, limits/rationale and no broadening on rerun | #51; #73 setup rerun/preservation/policy fixtures |
| AC10 model invocation | Each named `ask-*` rechecks exact policy or explicit invocation; frontmatter/body/references/checks reconcile together | #52/#53; #73 zero-forbidden-call mock coverage |
| AC11 optional/advisory models | Root lead budget reservations plus assessment enforcement; no substitution/install/disclosure implication, deterministic facts and independent review retained | #51–#53/#67/#68; #72/#73 shared/exhausted budget and denial fixtures |
| AC12 decision-ready PR | `pr` owns plain-language report and authorized publication; actual baseline/count/CI/merge effects and unknowns | #66; #71/#73 report trials |
| AC13 delivery integrity | Both leads; tracker library, preflight, shared capacity/repair lineage, scope freezes, independent dirty review and recovery | #63/#65/#67/#68; #71/#72/#73 |
| AC14 migration/docs | ADR/design status and preservation; every package owns its changed docs/notices, setup policy, lead listings/changelog | #50/#51–#69/#73; #69 fixtures and #74 separately approved actual installed migration |
| AC15 validation evidence | Package-specific validation and separate repository executed records; this document explicitly paper-only | All implementers; #70–#73 cover composed standalone/failure/permission trials; #74 actual migration |
| AC16 backup/retire replacements | #69 procedure/fixtures and #74 exact local inventory/approval/backup/restore/activation/discovery/report | #69/#73 readiness, #74 actual retirement including same-name/shared symlink/partial failure |

#50 addresses design portions of AC1/2/3/4/6/9/10/11/13/14/16 and traces all sixteen obligations. It does not claim implementation acceptance or satisfy requirements for executed examples. Every downstream ticket still follows its actual scope and native prerequisites.

## Paper check 1: independent invocation and missing helpers

Synthetic input: an authorized local caller asks `analyze` to assess a small interface change. The supplied behavior is already agreed. Current sources cover code/callers/checks. No writes/delegation/model authority is supplied.

Expected: inspect sources, retain settled behavior, return bounded readiness, risk/check mapping and method recommendation; stop without spec/tickets/build. A standalone method request uses its own scope/authority and stops at local evidence, not a PR. A copied package in a non-sibling directory resolves internal references relative to itself and companions via discovery. Missing domain companion blocks a required ADR change, not ordinary inspection. Ambiguous review implementations block acceptance rather than selecting by name. Missing optional worker runtime yields direct research where authorized; absent material source/check remains a gap. This paper check does not show actual isolated-package behavior; #73 executes it.

## Paper check 2: current bug ticket reused

Synthetic input: ticket B names expected/actual behavior and impact, pinned reproduction/environment, observed red result, established cause at deciding sources, bounded fix/exclusions/dependencies, acceptance, regression strategy and TDD recommendation. Its underlying inputs match the receiving lead's inspection. Request explicitly authorizes the fix.

Expected: `work-on` consumes B's diagnostic/readiness evidence; no automatic `analyze`, investigation, research or classifier repeat. Inspect current graph/preflight/ownership, select method and implement. Record new meaningful local/integrated checks and independent review rather than treating old red evidence as a green fix result. Separate ready-to-accept from merge/closure. Investigation-only invocation would have stopped at B's publication/read-back with no shipped fix. #71 executes the reuse path.

## Paper check 3: stale or incomplete bug evidence

Synthetic variant: B's cause depends on a now-changed caller; an unrelated module and the agreed expected behavior remain unchanged.

Expected: invalidate cause/check mapping dependent on that caller, inspect the changed path and rerun only relevant reproduction/analysis. Preserve current unaffected evidence and product intent. Do not restart all discovery or repeat an optional model call by default. If reproduction no longer confirms the symptom, report that outcome; if cause is unresolved, ticket remains investigation work rather than implementation-ready. Duplicate match is reconciled through `write-tickets` within authority, not newly published as another bug. Temporary probes remain accounted for. If staleness impact is unclear, expand the affected evidence set honestly. #71/#73 execute variants.

## Paper check 4: methods compose without promoted prototype

Synthetic input: interface uncertainty merits a prototype; then an intended behavioral change must be delivered.

Expected: lead owns one bounded question, method returns observations and artifact disposition, not production acceptance. Lead uses findings to update only affected analysis/decisions, then selects TDD for production scope. Red fails for intended behavior; green implements; refactor keeps relevant checks green. One authority/repair ledger persists across the methods. Characterization of existing invariants can precede TDD without canonizing known defects. Acceptance-first establishes executable workflow examples; build-and-check runs immediately per small increment. All five standalone/composed examples still need execution in #71/#73; this prose is not five passed method trials.

## Paper check 5: model denial and policy reconciliation

Synthetic cases and expected outcomes:

| Starting state | Expected design outcome |
| --- | --- |
| Missing policy, explicit none, or conflicting permission | Zero autonomous calls. Ordinary engineering continues where sufficient; report material gaps rather than invent model evidence |
| Local-only Clef policy | Only exact authorized local skill/model/endpoint/data/purpose within budget; Jev and Clef Flash are not aliases |
| Bounded hosted permission | Reserve shared call/spend allowance, sanitize minimum approved evidence and recheck named route; authorized use needs no repeated confirmation |
| Sensitive disclosure denied | No affected send; redact/narrow only when deciding facts remain adequate, otherwise gap. Local permission cannot authorize remote fallback |
| Budget exhausted or cost of reservation unknown | No automatic/unsafe paid send. Retries/corrections already attempted count, including unknown charges |
| Service unavailable and substitution prohibited | No alternate model/endpoint, install/download or implicit startup; autonomous policy-permitted direct judgment is labeled agent-only; explicit assessment offers fallback and waits unless preauthorized |
| Valid insufficient-data | Keep missing evidence; no service-failure substitution or repeated voting |
| Explicit Jev request under compatible project restriction | Normal named billable assessment authorization and package bounds apply; an explicit project ban remains a conflict, not overridden by generated command text |
| Setup rerun with authoritative equivalent policy | Preserve home/approval/rationale/values, propose only true delta and pointers; zero calls/service operations, no silent expanded opt-in |

Both lead and named package check authority before transport. A model's classification cannot replace deterministic facts, checks, independently authored review or a policy decision. #51–#53 and #73 must execute mock transport assertions for zero forbidden calls, allowed payload/response handling, bounded retry/correction and lifecycle, separately from real inference. No live inference is needed here.

## Paper check 6: nested-worker capacity, failure and resume

Synthetic spec has independent tickets A/B and C blocked by accepted integration of A. Root launches two `work-on` ticket agents within authorized runtime/ownership/bounds. Both slots remain occupied until assignments finish or are confirmed stopped/isolated.

Expected: A uses specialists/methods inline; a request for research/review/model allocation goes to root. A cannot launch two more workers or treat itself as a new lead pool. Root queues additional work until a slot is available. Standards and Spec reviewers are independent of authors and each other's conclusions; they can run sequentially in the available slot. No writer/integration changes the pinned review scope.

If A fails after partial writes, preserve artifacts, known/unknown operation state and ownership; C stays waiting even if A issue closes. B can integrate serially under target policy with new overall snapshot/evidence. Confirm A stopped/isolated before reassignment; resume reconciles graph, worker state, revisions, findings and spent budget rather than replaying launches.

A has already spent two corrective cycles with its material finding unresolved. Resume or moving that finding to final integration provides no new allowance; root stops affected repair and recommends a revised plan/budget for explicit approval. A genuinely new cross-ticket finding uses the integrated checkpoint. B local green results do not establish whole-spec pass; integrated checks/review refresh after material changes. #72 executes this scenario with observable lifecycle/budget evidence, not merely a lead narration.

## Paper check 7: staged publication and migration rollback

Synthetic installation includes renamed legacy skills, a locally modified same-name `tdd`, two active discovery registrations and a symlink whose source is shared with another runtime.

Expected: stage extraction ownership/caller pointers coherently; interim broad `work-on` remains truthful about required new companions. Single-change cutover cannot claim multi-ticket support until the coordinator exists; complete first delivery waits for all five methods. If a required companion is absent, block that route, never call an incompatible installed legacy command.

For local migration, obtain exact-target/removal/activation/rollback approval. Back up the complete packages/modifications/modes/links/registration metadata outside all discovery roots/public repository; verify checksums and isolated restoration before retiring anything. Stage validated replacements/companions. Invalid backup or incomplete replacement leaves working old copies intact. Remove only approved registrations/links/copies; shared source stays. Refresh discovery and verify exact new sources plus absence of competing old active implementations.

Activation fails after one registration changes: use the journal and actual discovery to inspect applied/unknown operations, deactivate only transaction-owned replacement effects, restore backed-up package/link/registration state and verify old resolution. An interrupted rerun does not back up the new copy as the original or blindly repeat removal. Intervening unrelated changes cause a conflict/blocker rather than overwrite. Retain backup after successful restore/activation. Report incomplete recovery precisely if restore fails. Reverting source commits cannot undo installed migration. #69 executes safe fixtures; #74 separately performs actual migration after approval. Neither is executed here.

## Actual #50 checks and evidence

Preflight and authority inspection were executed directly: clean input worktree, previous branch PR #49 merged, fetched origin, created `docs/composable-skill-contracts` from `origin/main` at the input revision in inventory, targeting `main`. Read-only #50 blocker endpoint returned none. Read #48's approved table and paginated native sub-issues; all #50–#74 are present. Read #50's blocking direction (#51/#54/#55/#56/#57/#58/#59/#62/#63/#65/#69). Native graph comparison details and final document-check outcomes belong in the #50 PR/evidence at the reviewed revision; no mutation is authorized by those reads.

Executed document checks: Node/Marked rendering and structural inspection passed for seven changed Markdown documents, 14 tables, 57 headings and 41 relative links/anchors; all sixteen acceptance rows are present. `git diff --cached --check` passed. Direct integrated review checked proposed/accepted status, reciprocal ADR pointers, scope and sensitive/local-path leakage. A scoped-path/history check confirmed only seven Markdown files changed; historical inventory/validation, glossary, public listings, changelog and runtime packages remain unchanged. `CLAUDE.md` remains a symlink to `AGENTS.md`. Rendered HTML and temporary check scripts are local evidence, not shipped infrastructure or browser visual inspection. Record the exact reviewed commit and final graph outcome in the PR; authored expected outcomes above remain paper checks regardless of document-check success.

No new executable behavior exists to exercise in #50. Package frontmatter, isolated-package or script execution tests are inapplicable to unchanged skill packages; their downstream owners execute them when implemented. No independent review, delegated agent, classifier, hosted model, installed mutation or workflow trial was run for this design. Test additions/removals/updates: zero; no CI changes, no repository CI workflow or timing claim. Runtime README/listings/changelog deliberately unchanged because this proposal ships no public skill behavior. CONTEXT unchanged because existing domain meanings suffice. Approval, supersession status on acceptance and merge remain pending.
