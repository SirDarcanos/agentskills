# Work On single-change cutover evidence

Delivery evidence for [#67](https://github.com/SirDarcanos/agentskills/issues/67), under [#48](https://github.com/SirDarcanos/agentskills/issues/48) and the [accepted design](../../design/composable-delivery.md). Package runtime instructions start at [Work On](../../../workflow/work-on/SKILL.md); [package validation](../../../workflow/work-on/references/single-change-validation.md) describes runnable checks. This record is not an agent-adherence trial or full #48 acceptance.

## Scope and source

Base/initial HEAD: `59fdc2cd64fa720699230c0078a5e3f349f4117c` on `main`; working branch `feat/single-change-work-on`, PR target `main`. Initial tree was clean and no existing branch PR was found. Changes narrow Work On to one accountable change lead, consume current evidence, compose discovered methods and preserve verification/review/repair/recovery/PR gates. Retained dispatch material is inactive until #68 transfers ownership. No installed copy, model permission, issue graph, deployment or release changes.

Paginated native blocked-by read returned #52, #53, #55, #56, #57, #58, #59, #64 and #66, all closed. Native parent read returned #48. Closure was checked against merged PRs and source history rather than used alone: local model updates #77; hosted #82; methods #79–#81/#83–#84; investigation #89; PR #91. Accepted design #75 is merged (`a95a9588ff86304f2390cae8d87df4addf7da1d1`), and Analyze #85, review adaptation #90 and other extracted owners are present in the selected base. No graph mutation occurred.

Complete entry points for Analyze, all five methods, Investigate Bug, PR, Review Delivery and Git preflight were inspected in their repository source locations, with branch-specific contract references. This is explicit source discovery/semantic inspection, not proof of installed runtime discovery. Companion files remain unchanged at the base revision.

## Executed checks

Environment: Python 3.14.7, Git 2.54.0 (Apple Git-157), macOS. Temporary fixtures use synthetic data/identity and finite subprocess timeouts. Final fixture SHA-256: `5dd4f71ae24c8a4bb0857e17dce6303d9e3100e135171ac2d2935a056d6c42ec`.

| Actual check | Observed result and boundary |
| --- | --- |
| `python3 -B work-on/scripts/check-single-change-fixture.py` | Exit 0, 8 named unittest cases; 1.332 s in the final source run. Six requested tool fixtures plus static instruction and Git-isolation regressions. |
| Same script from a temporary copy containing only `work-on` | Exit 0, all 8 cases; 1.292 s. No source-repository or sibling companion imports needed for the fixture. |
| Relative Markdown link/anchor resolution | 96 references resolved in source and isolated Work On copies. Entry/frontmatter and Markdown structure/tables inspected directly. |
| `git diff --check` | Exit 0. Scoped diff inspected for source/privacy/portable paths and preservation of existing notices. |
| Review-owner snapshot `pin`/`check` helper | Before/after initial review matched listed paths; after repair a new snapshot matched. Included tracked dirty layers, both new package files and agreement/policy/design support; no writes into reviewed source while reviewers ran. |

The direct/ready-bug/composition fixtures observed assertion-level whitespace failures before implementation and current passes afterward; unrelated staged/unstaged/untracked bytes, index state, symlink target and base history matched. Stale-source fixture observed changed content identity and a real failure, then refreshed the dependent check. The required-integration fixture observed exit 2 because its check was absent; that result stays unavailable/unverified despite focused green. It triggers no installation or corrective retry.

The Git-isolation regression supplies hostile `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_TEMPLATE_DIR` and command-config variables pointing to a separate sacrificial sandbox. Fixture init/add/commit stayed in the owned probe; external files/modes/HEAD and index stayed unchanged, no hook marker appeared, and no template hooks were installed. All Git-control variables are removed from fixture subprocess environments, global/system config isolated and hooks/templates disabled.

An earlier seven-case run failed only on a literal text guard expecting “not” where the entry said “without”; six tool cases passed. The assertion was corrected and the seven-case run passed. Independent inspection subsequently identified inherited Git-environment exposure; the final eight-case runs above verify the safety repair. These are historical failures, not hidden green claims.

## Verification limits

- Method/caller steps and ledgers are synthetic or statically inspected. Passing fixtures do not prove autonomous routing, no recursive investigation/delegation, repair expenditure/exhaustion/resume or transport-level model budget enforcement.
- No preflight-companion invocation, installed slash-command/discovery test, composed five-method agent run, live tracker mutation, PR publication fixture, service startup or model inference was executed by the fixture. Zero model requests are by construction and applicable repository policy, not a tested transport gate.
- Independent review concerns this actual skill/script change, not independent acceptance of the synthetic formatter. Downstream #70–#73 own broader standalone/composed/failure/policy/discovery trials.
- Local fixture timings are not CI measurements. No repository GitHub Actions jobs or deployment/release hooks were found; external automation is not certified. CI duration/compute impact is unmeasured/inapplicable to the inspected absent CI configuration.

## Review and repair record

The root authorized two fresh read-only contexts per round, one Standards and one Spec, under standing project permission; maximum two active workers, finite eight-minute initial and five-minute renewed bounds, no writer/reviewer recursion or optional assessment. Original axis reports remain separately inspectable in runtime-managed artifacts; public summaries here are dispositions, not rewritten original reports.

Initial contexts: `standards67` / `9252cef3-2f97-4db9-8f3d-db82009973b3`, and `spec67` / `5cdb1016-2f07-4bd1-8a56-41da772fc241`. Both inspected the same dirty state and primary agreements/raw checks; neither reported exposure to excluded conclusions. Standards raised blocking Git-environment isolation finding S1; both axes raised nonblocking acceptance-ID traceability. These were repaired together in **cycle 1** of checkpoint `work-on67-fixture-safety`, retaining original lineage. No model reservations/attempts; no budget reset. Renewed independent inspection covers the final executable/reference changes, while unchanged source retains its original review evidence after explicit snapshot comparison.

Renewed contexts: `standards67repair` / `9ea5300a-e893-4814-bb0a-7b86fb6093ec`, and `spec67repair` / `2edfbf22-5954-47b3-8e7b-426def3ad277`. Both returned no issues in the repaired executable/reference scope; neither ran checks or independently established isolated-copy provenance from the raw logs alone. The root's actual copy-and-run command establishes that narrower provenance. Initial runtime/source review plus renewed affected-file review leaves no unresolved findings in this delivered slice; no full #48 acceptance or merge authority is inferred. Final PR state is recorded in the PR delivery report. This retrospective record is an author-written completion artifact outside neutral reviewer input roots; its facts and relative links receive direct final inspection, not a claim that reviewers authored or independently certified it.

## Documentation and impact

Updated entry, execution contract, build/completion/adapters/recovery and inactive dispatch marker; package/root README, package validation/script and this evidence home. Existing Unreleased Work On Added entry was updated because the package is not yet published. The incompatible broad-to-single-change boundary warrants a major PR impact label; no version/tag/publication is selected. Domain meanings, accepted ADR/design decisions, authority/model policy, label vocabulary, native relationships, licenses and old trial records are unchanged.

Test-count basis is named `unittest` methods in the new script against the selected base: **8 added, 0 removed, 0 updated, 0 moved**. Existing tests/fixtures remain unchanged. New protection covers the bounded checks described above, not an application test quota. Source merge makes updated packages available; separately installed copies and migration require separate approval. Reverting source restores the prior repository boundary, not installations or external state. Keep #67 open until accepted and merged; no merge, deployment, release or installed migration is authorized by this evidence.
