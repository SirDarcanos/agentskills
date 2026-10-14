# TDD validation

Read when changing or validating this package. These are repeatable checks and authored workflow cases, not a claim that an agent followed the skill.

## Package and executable checks

1. Read the complete entry point and rendered Markdown. Check frontmatter: `name: tdd`, matching-request/handoff description, and no command-only invocation gate.
2. Resolve every relative link from its containing file. Copy the entire package to an isolated directory with no sibling skills; check internal links again and run the fixture there.
3. With Python 3.9+ and no additional dependencies, execute:

   ```sh
   python3 tdd/scripts/check-fixture.py
   ```

   From an isolated copy, use that copy's `scripts/check-fixture.py`. The script creates/removes only a temporary synthetic target. It invokes Python's unittest runner with bounded subprocess timeouts, no network, models, Git/tracker mutations or installed skill changes.
4. Inspect actual output: existing free-shipping coverage passes; an added shipping-cost example fails with `30 != 35`; minimal implementation passes both; a refactor removes repeated subtotal calculation and both unchanged behavioral tests pass. The known expected totals come from the fixture agreement: shipping is 5 below a subtotal of 50, otherwise free.
5. Inspect the two diagnostic anti-examples: a self-comparison passes faulty code, so it cannot protect shipping behavior; an internal-expression assertion fails after equivalent refactoring. Both are removed before the final retained suite. Their execution demonstrates the failure modes, not automated general test-quality classification.
6. Inspect the integrated diff for scope, notices, private data and nonportable paths. Preserve historical evidence and unrelated files.

## Authored workflow cases

Exercise these directly or in an authorized runtime trial; record actual actions separately from expected outcomes:

| Case | Expected result |
| --- | --- |
| Standalone bug fix | Context/authority and Git preflight are inspected; one sensitive red precedes minimal green; refactor runs while green; return local evidence and stop. |
| Bounded Work On handoff | Lead supplies current agreement/analysis/preflight; TDD checks freshness and reuses it; lead retains method choice, verification, review and acceptance. |
| Existing coverage | Inspect assertions first; reuse a current failing behavioral check or extend a gap. Correct passing behavior yields an honest already-covered result, not manufactured red. |
| Wrong-reason red | Syntax/tool/discovery failure is labeled harness/environment failure and blocks the green claim until the intended failure is observed. |
| Bad test oracle or coupling | Replace self-derived expectations with an independent example; assert at a consumer boundary; retain a demonstrated red for the intended behavior. |
| Missing/ambiguous/incompatible preflight | Git writes block; planning can return. No sibling assumption, installation or legacy fallback. Non-Git work marks this dependency inapplicable. |
| Plan-only or unapproved scope change | Inspect/propose only; preserve partial work and seek the consequential decision from its owner. No inferred delegation/model/installation authority. |
| Stale evidence or competing owner | Invalidate dependent checks and reconcile ownership before conflicting writes; preserve current unaffected evidence and unrelated work. |
| Failed refactor or regression | Restore current green within authority; no next increment with a material regression. Report unresolved failures without claiming acceptance. |
| Recorded acceptance repair / delegated route | Discover shared Work On contract and retain root ledger/limits/lineage; missing contract blocks that route; ordinary planned TDD increments do not spend acceptance-repair cycles. |

## Evidence limits

Fixture execution verifies a synthetic code/test sequence and the illustrated anti-patterns. Static package checks verify packaging and inspected instructions. Neither establishes installed discovery, autonomous routing, cross-runtime behavior, delegated lifecycle, independent review or whole-delivery acceptance. Live agent trials require their own authority. Keep repository execution evidence outside this installable package, with command, environment, source state, actual outcomes and unrun cases.
