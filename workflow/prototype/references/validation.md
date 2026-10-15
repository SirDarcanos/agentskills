# Prototype validation

Read when changing or validating this package. Expected workflow cases below are authored scenarios, not executed agent evidence.

## Package and executable checks

1. Read the complete entry and rendered Markdown. Check `name: prototype`, a specific matching-request/handoff description, and no command-only gate. Verify each step's stopping/completion condition.
2. Follow all relative links from their containing files. Copy the entire package into an isolated directory without sibling skills, recheck internal links and execute the fixture there.
3. With Python 3.9+ and no additional dependencies, run:

   ```sh
   python3 workflow/prototype/scripts/check-fixture.py
   ```

   Use that copy's `scripts/check-fixture.py` from an isolated package. The fixture creates only its own temporary synthetic target, runs bounded Python subprocesses with five-second timeouts, and removes the temporary target on exit. No network, model, Git/tracker mutation, installed-skill change or user-project cleanup occurs.
4. Inspect actual output. Two cases ask whether an in-memory absorbing cancellation state ignores late completion. The two-case run supports that narrow hypothesis; a one-case bound leaves the question inconclusive. A counter-hypothesis is rejected. All results explicitly retain `production_ready: false`; limitations include real concurrency, persistence/recovery and integration.
5. Inspect disposition checks: useful runnable probe and learning remain inside the fixture until its temporary target ends; unauthorized deletion is refused, explicitly authorized scratch is removed, unowned and interveningly changed files are preserved, and removing an owned symlink preserves its shared target. This tests a synthetic conservative cleanup helper, not a production cleanup utility.
6. Inspect the integrated diff for scope, portable paths, notices, protected work and private data. Record actual command/environment/source state/results separately from this package's expected scenarios.

## Authored workflow cases

| Case | Expected outcome |
| --- | --- |
| Standalone feasibility request | One question, finite cases/iterations/time limit, runnable probe and raw observations; narrow recommendation, limitations and artifact account; no automatic production work. |
| Authorized Work On handoff | Consume current agreement/readiness/preflight, check deciding inputs, run method inline and return; caller retains next-method and delivery decisions. |
| UX question | Observe actual interactions/authorized participant feedback as needed; unavailable feedback remains a gap, not proven preference or usability. |
| Plan-only or unavailable run tools | Return bounded plan/blocker; no writes, install, service startup or invented observations. |
| Question answered early / bound reached | Stop at the first stopping condition; inconclusive is a legitimate completed experiment, not an excuse to expand the loop. |
| Contradictory or harness-failure results | Separate facts from assumptions; retain uncertainty or environment blocker and recommend targeted next evidence without executing it. |
| Current/stale handoff | Reuse unchanged evidence; invalidate only findings dependent on changed deciding files/environment/agreement; report unclear impact honestly. |
| Missing/ambiguous/incompatible companion | Dependent Git/domain/delegation route blocks; non-Git direct experiment remains possible where authorized; no sibling assumption or automatic installation. |
| Cleanup/retention conflict | Preserve useful work by default; exact owned authorized unchanged artifacts only may be removed; preserve intervening edits and symlink targets. |
| Favorable recommendation / production promotion | Return prototype limitations and subsequent production scope/check recommendation; never label prototype output accepted production implementation. |
| Delegated or recorded-finding correction | Discover shared execution contract, retain root ledger/limits/lineage and request work through root; changing methods does not replenish budgets. |

## Evidence limits

Static packaging checks and the executable synthetic fixture do not establish agent adherence, installed discovery/routing, independent review, human UX quality, cross-runtime certification or delivery acceptance. Runtime trials and any participant/service use need their own authority. Keep actual repository evidence outside the independently installable package; retain unrun cases explicitly.
