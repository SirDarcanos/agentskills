# Fixture PR report — fractional discount

Report-only trial; no remote PR is opened for this synthetic product.

## What changes

A subtotal of 100 with a 10% discount now returns 90 rather than 99.9. Zero discount and empty carts retain their contract. The caller's fractional units and public function signature remain unchanged. No rounding, tax, payment integration or invalid-input behavior is added.

## Evidence and state

Investigation confirmed the defect and persisted a complete local ticket **without fixing it**. A separately authorized delivery consumed that ticket, protected existing behavior through characterization, and executed meaningful TDD red, green and refactor checks. Four named tests and the original reproduction pass on the dirty delivered fixture. See [commands](results/commands.json), [ticket](results/ticket.json) and [state](results/state.json).

The fixture is still local, uncommitted and unmerged: staged pricing implementation, unstaged refactor and included untracked checks. Separate Standards and Spec reports/freshness, retained in the execution record, are required before recommending acceptance. Local checks do not imply maintainer acceptance, PR publication or merge.

## Test and CI impact

Counting basis: named `unittest.TestCase` methods in the target, baseline `5fbaa7f0ea2c5f8a5be8f80655848cf2cbf5447a` versus delivered dirty files. Two existing controls remain unchanged; two regression methods are added for fraction and empty-fraction behavior. Removed/updated/moved tests: zero. The reproduction script is separate, not counted as another named test. An isolated characterization perturbation failed the controls; the regression tests failed before production repair.

The synthetic repository has no CI configuration, job, deployment or release hook at baseline or delivery. Job changes: zero. CI duration, runner compute, billing and speedup measurements: unavailable, because no hosted run occurred. Local check timing cannot support those claims.

## After merge and reversal

If someone separately accepted and merged this fixture change, only the source calculation/checks would change; there is no configured automatic deployment or release. Any production adoption requires separate authority, environment-specific validation and domain/rounding decisions. Reverting the source change would restore the overcharge bug; it could not undo payments, customer effects or deployments performed elsewhere. No such external effects occurred in this trial.

## Decision

Implementation and local verification are complete within R1/R2. Report is complete; acceptance depends on current independent review/freshness and the owner's decision. Real payment behavior remains unverified and excluded. No merge, closure, deployment, release or installed-skill action is requested by this report. Fixture documentation is its retained agreement/evidence; no real product changelog exists.
