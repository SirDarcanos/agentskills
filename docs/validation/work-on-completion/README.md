# #26 repair/completion evidence

Repository-local evidence, outside the installable package. Runtime behavior is owned by [repair/completion](../../../work-on/references/completion.md); [completion validation](../../../work-on/references/completion-validation.md) contains authored scenarios and the execution boundary.

## Reproduction and actual execution

From the repository root, with Python 3.9+ and Git:

```sh
python3 -B docs/validation/work-on-completion/exercise.py
```

The author ran and inspected [exercise.py](exercise.py) with Python 3.14.7 and Git 2.54.0. Exit 0 means its synthetic assertions matched the expected passes, failures and drift; it does not mean delivery acceptance passed. The script uses Review Delivery's existing snapshot helper, creates/removes only its disposable Git target and separate exhausted-budget fixture, and performs no model/agent launch, installation, live tracker mutation, merge or release. Raw temporary output was inspected locally rather than committed with workstation paths.

Actual snapshot: base/HEAD `702161eb86877ecdee8ba963d30d0304a82d3a6b`; scoped files `service.py`, `test_service.py`, `agreement.md`, ordinary mode 0644. Commit IDs vary on rerun. Initial service SHA-256 `9d68cbba15e04541121b1f0cc752d7de9eca48e4850239a8aa96965c7462a34d`; repaired service `8cdae810aba736b3c120628f7f0689f1f009ead817724a97fb4a9bc12e175984`. Repaired unstaged patch SHA-256 `e9a3bdae8c9c86ac0a2762e4d1d1fcbe39a1f1205156cd539f4928279655ac82`; committed/staged patches were empty. The script prints complete scoped fingerprints and actual corrective diff; HEAD alone would miss the repair.

## Inspected dispositions against procedure

| Executed observation | Lead's direct walkthrough decision |
| --- | --- |
| Existing public-name assertion passes; privacy assertion fails because `token` is returned; check exits 1 | Completion steps 1/3: material unresolved finding blocks acceptance; an honest blocked report can be ready-to-report. No unrelated success compensates. |
| Checkpoint `projection-acceptance`, cycle 1, direct behavior-owner correction from `dict(record)` to name-only projection | Step 2: actual diff inspected; old helper check exits 1 with changed files/status/unstaged fields. Old evidence is stale, not a verdict for the repair. |
| Repinned dirty scope; both assertions pass, check exits 0; helper freshness exits 0 | Steps 2/3: C1 public name and C2 privacy verified at repaired state. Significant behavior fix requires renewed independent review; none was authorized/executed, so acceptance stays blocked. |
| Agreement changed to add C3 recovery; helper detects drift | Step 3: old agreement evidence does not cover C3. Passing C1/C2 supplies no recovery evidence; ready-to-accept is blocked until evidence or authorized acceptance change. |
| Separate authored exhausted-budget scenario: two incomplete corrective candidates still fail privacy; spent count 2 preserved after renaming | Step 2: no third candidate applied; failed attempts consume cycles. Stop with preserved work and recommend reassessment. This counterfactual branch is not permission to reset a real finding's budget or a session-resume test. |
| Synthetic accepted design decision makes parent actionable; proposed exact readiness delta; no mutation authority | Step 4: proposal only, observed labels unchanged. Parent coordination readiness differs from child execution eligibility. |
| Child criteria actionable and label ready; predecessor closed but accepted integration absent | Step 4: child execution remains blocked. After synthetic accepted predecessor merge evidence, eligibility changes without copying parent labels. |
| Exact mock approval for parent label delta; in-memory write and read-back match; child labels/parent and blocker observations preserved | Step 4: fixture reconciliation succeeds; rerun has no delta. This is not live API/native-relationship evidence. |

The fixture is deliberately small: privacy is a material disclosure rule; projection has no destructive or persistence effects. Added recovery is a missing obligation, not a tested behavior. Two failed candidates use a fresh counterfactual target/checkpoint, distinct from the successful scenario, to inspect counting; no real checkpoint was moved to obtain fresh retries.

## Gates and delivery limits

This implementation's build gate has approved #26 criteria, accepted #18 package/limit decisions, integrated predecessors, clean preflight and one direct author. Acceptance for the changed skill remains **unaccepted**, with independent Standards/Spec review absent. Direct inspection and fixture execution are not independent review. Ready-to-report describes this evidence-backed partial outcome, not user acceptance. PR readiness/merge/issue closing remain subject to repository policy; #26 stays open until accepted and merged.

Authored but not executed here: autonomous repair assignment/result inspection, significant-fix renewed independent review, failed/timed-out workers, read-back/API failures, non-Git scope, dirty untracked/mode/symlink changes, content-identical commits, alternate target release schemes, full dispatch/recovery and end-to-end #29/#30 trials. The in-memory label assertions encode expected fixture transitions; they do not execute the instruction workflow or prove future agent compliance. No live readiness-label or relationship mutation occurred.

## Documentation and source state

Preflight: clean `main` at `c2010faed33cb484b73e898be5bdd054a591ada1`, matching fetched `origin/main`; created `feat/repair-completion`, base/PR target `main`, no existing PR or unrelated changes. Native #26 blocked-by observations returned #24/#25, both closed; merged PR #39 (`95c42ef05baff60e1747f6d6ab2aac742e5565fe`) and #41 (`c2010faed33cb484b73e898be5bdd054a591ada1`) provide integrated predecessor outputs. Native parent is #14; blocking observations returned #27/#29. The PR commit identifies the package/fixture revision; fixture commit IDs above identify only the disposable target.

Updated authoritative runtime procedure/validation and entry/shared-contract pointers, package/repository overviews, design implementation pointer and Unreleased changelog. No domain definition, ADR, project authority, label mapping or native edge changed, so those homes need no edits. New compatible functionality has minor release impact; an impact recommendation is not label-mutation or publication permission. Legacy and globally installed copies remain unchanged.

No Markdown renderer was available (`pandoc`, `markdownlint`, Python `markdown`/`mistune` absent); headings/tables/source were directly inspected instead, without installing tooling. Executed structural checks passed: 114 repository relative links/anchors, 76 links/anchors after copying only Work On, frontmatter/body inspection, Python 3.9 syntax parsing and `git diff --check`. Actual execution used Python 3.14.7, not 3.9. Direct diff inspection found no private material, generated artifacts or nonportable paths in authored changes. These checks do not replace rendered Markdown inspection or independent review.
