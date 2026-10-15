# Impact accounting

Read completely for every PR report. Inspect primary sources; the report describes delivered facts, not hypothetical savings.

## Test protection

1. Declare the comparison base and delivered snapshot, framework(s), and count unit: for example collected test cases, named test functions, scenarios or test files. State parameterization/dynamic discovery treatment and exclusions. Keep units separate across frameworks; an unavailable collection leaves case totals unknown rather than inferred from filenames.
2. Reconcile baseline and delivered identities. Count additions, removals and modified retained tests under that unit; list moves/renames separately, including moved-and-modified tests as updates. Git rename detection is a clue, not proof of equal behavior. Avoid counting a rename as one removed plus one added. Explain splits/merges and any ambiguous identity mapping rather than forcing totals.
3. Explain the behavior protected by additions/updates, and the protection lost, replaced or demonstrably redundant for each deletion. A redundant deletion still counts as removed; identify the retained equivalent assertion/path and its evidence. Fewer tests are not automatically faster or weaker; more tests are not proof of coverage. Distinguish test-source changes from tests actually executed, skipped, failed or not run.
4. Report totals and meaningful protection consequences. When no tests change, say zero changes under the stated basis; checks of documentation are not newly added application tests. Missing baseline or incomplete collection blocks exact totals, not an honest unknown report.

## CI jobs and measurements

1. Inspect both baseline and delivered CI definitions, referenced scripts/reusable workflows, triggers, matrices, conditions, runner classes, dependencies, caches and external settings where authorized. List added/removed/updated/unchanged jobs and what they check. Renamed jobs and matrix-expanded executions are separate from test counts. CI absent means inspected configuration has no jobs; inaccessible external CI remains unknown, not absent.
2. For measured comparisons, identify baseline/candidate run IDs or retained records, revisions/configuration, date, workload/command, environment/runner/resources, sample size, statistic and units. Expose cache state, concurrency, skips/retries/failures and other confounders. Use like-for-like successful runs or explicitly state the mismatch; a changed workload is not evidence of an optimization.
3. Separate wall-clock/pipeline elapsed time from summed job/runner compute time, CPU time, billed usage and cost. Parallel elapsed time is not compute. Compute cannot be deduced from pipeline duration; billing requires actual billing evidence. State any arithmetic and denominator, and avoid percentage comparisons with a zero/unknown baseline. Qualify one sample as one sample, not a trend or causal proof.
4. If comparable evidence is absent, say duration/compute impact is unmeasured and why. Configuration inspection can establish job changes but not timing savings. Local fixture/test execution duration is not hosted CI performance. Do not run CI, alter CI, spend money or benchmark without separate authority. No CI jobs means CI duration/compute comparison is inapplicable, not “0 seconds saved.”

## Post-merge behavior and reversibility

Inspect merge triggers and deployment/release/publish hooks, repository settings/run evidence when relevant and accessible. Distinguish intended configuration from observed executions; unknown external automation stays unknown. A PR or merge alone proves no deployment, release or installed-copy update.

Identify required manual actions, migrations/backfills, flags, consumer/skill updates, owners and approvals. Explain compatibility, ordering and any interruption/partial-migration risks supported by the change. Classify reversibility from effects: reverting source may restore code but cannot restore deleted data, external state, credentials, tracker operations or installed copies. Give actual rollback prerequisites/steps and remaining consequences; when untested, say so. If no automatic deployment is configured in the inspected sources, say exactly that, rather than suggesting a rollout occurred.
