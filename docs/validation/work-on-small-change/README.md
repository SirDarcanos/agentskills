# Executed small-change workflow trial

Repository-only evidence for [#29](https://github.com/SirDarcanos/agentskills/issues/29)
under [#14](https://github.com/SirDarcanos/agentskills/issues/14). Tested Work On
and Review Delivery at `e171a9b5f18495d5f388a1daeaa0dcdfba08527e`.
No shipped skill or globally installed copy was changed.

**Outcome:** the lead executed the lightweight route for one synthetic filename
filter fix; baseline → relevant assertion failure → fix → integrated pass →
two independent reviews → current-scope check → completion report. F1–F4 have
current evidence; both reviewers found no issues. No repair was needed.
Ready-to-accept is a recommendation, not maintainer acceptance or a merge.

## Evidence index

| Record | Purpose |
| --- | --- |
| [Entry/technical plan](plan.md) | Authority, predecessor integration, direct route, design, risks and build gate |
| [Frozen packet](scope.md) / [manifest](scope.json) | Full non-Git before/after and supporting-input scope |
| [Baseline](fixture/baseline/) / [delivered](fixture/delivered/) / [diff](delivered.diff) | Actual source copies and bounded change |
| [Baseline check](evidence/baseline.json), [red](evidence/red.json), [green](evidence/green.json), [integrated](evidence/integrated.json) | Exact commands, Python version, exits, sanitized raw output and manifests |
| [Standards](reports/standards.md) / [Spec](reports/spec.md) | Complete original independent reviewer returns |
| [Review receipt](review-receipt.json) | Sanitized ordinary runtime lifecycle/context pointers, not an attestation |
| [Action record](actions.md) | Ordered actual operations, gate decisions, freshness and findings disposition |
| [Capture](capture.py) / [offline verification](verify.py) | Standard-library supporting checks; replay does not launch agents |

## Evaluation against the fixture agreement and #29

| Question | Observed result |
| --- | --- |
| Small explicit fixture/policy/oracle | Non-Git temporary project, fixed F1–F4, original source/tests, unrelated executable note and symlink |
| Entry and lightweight brief | Reused the clear synthetic agreement and its concern dispositions; no discovery questions, spec publication, setup or ticket hierarchy |
| Technical readiness and direct build | Inspected implementation, caller and assertions; one local suffix expression change, two relevant test methods, one README sentence |
| Verification | Existing baseline passed; new direct/caller assertions failed for missing case recognition; fixed and integrated executions passed; protected hashes/modes/link target remained identical |
| Independent review | Two fresh read-only contexts inspected the same actual sources and raw evidence on separate axes; reports explicitly bound their static inspection |
| Missed requirements | None identified within F1–F4 by lead checks or either reviewer; this narrow result does not establish complete workflow correctness |
| Meaningful findings/rework | No material or nonmaterial findings; zero acceptance repair cycles. Planned test-first red is not a failed repair. Repair/recovery were not exercised |
| Maintenance burden | Target adds no dependency, abstraction or configuration. Evidence remains outside installable packages; capture/replay tools have fixture-specific, single-level scope |
| User interventions | One required delegation permission exchange; no routine technical questions or manual phase/agent coordination. No authority was inferred from issue readiness |

The trial intentionally favors a small clear route, not hidden-defect injection.
It therefore shows review execution/coverage and preservation, not reviewer
finding-detection sensitivity, unsuccessful repair bounds or recovery. #24's
separate review evidence and #30's failure route remain distinct.

## Completion and documentation

- **Implemented:** case-insensitive final `.md` classification, preserving
  original output strings/order/duplicates; only the three owned fixture paths
  changed. Baseline and final retained snapshots match actual execution inputs.
- **Verified:** F1–F4 by executed checks/manifests, direct source inspection and
  separate independent Standards/Spec reports. Final scoped path/input comparison
  passed after both returns and again when consumed for reporting.
- **Unverified:** Git dirty/index preservation inside a target project, installed
  slash-command expansion, cross-runtime/package-copy execution, reviewer
  defect-detection sensitivity, repair/recovery and multi-ticket/failure routes.
  None is claimed as this small-change trial's executed result.
- **Deferred:** additional filename extensions only on a future product request;
  broader workflow trial/installation coverage belongs to #30/#31.
- **Blocked:** no material F1–F4 or #29 evidence blocker; maintainer acceptance
  and merge remain pending. #29 stays open until accepted and merged.

Build, acceptance-readiness and truthful report gates pass within this fixture.
No fixture acceptance, production use, deployment, release or global installation
occurred. No production issue or tracker relationships were mutated.

Documentation affected: fixture README behavior text and this repository-only
trial record. Runtime instructions, project policy, design/ADR and domain facts
remain unchanged. No changelog entry or release-impact label: retaining evidence
adds no public skill behavior or installation contract. #31 can link this record
when reconciling the final coverage/install documentation.

## Offline reproduction and limitations

From the repository root, on the recorded Python/POSIX environment:

```sh
python3 -B docs/validation/work-on-small-change/verify.py
python3 -B docs/validation/work-on-small-change/verify.py --replay
```

The first compares retained records, complete fixture membership and supporting
inputs against the original pin. The second additionally replays baseline,
red and delivered checks in a disposable directory; it expects the red check's
exit 1. Neither is a new Work On agent trial or independent review. Capture
utility success is not test success. Historical fingerprints pin the tested
source: later runtime/document changes correctly make the original pin stale;
inspect at the evidence commit rather than replacing it to manufacture freshness.

Environment observed: Python 3.14.7, Git 2.54.0 (Apple Git-157), macOS, native Pi
read/edit/bash tools and fresh reviewer agents. Python standard library only.
Full observed permissions and symlink metadata are platform-specific; another
filesystem/OS may differ, and no Windows or alternate-runtime support is certified.
The raw green/integrated records happen to be byte-identical (including elapsed
test output); distinct calls are documented in the actual action record, not
independently proven by those identical records. No claim of cryptographic
execution attestation or model consensus as proof is made.

Final repository-only checks: `verify.py --replay` again passed expected exits
and full scope freshness; 36 relative Markdown links resolved; all six retained
JSON files parsed; original report SHA-256 values matched; direct text/diff
inspection found no workstation paths, credentials, bytecode or unrelated
changes. Markdown headings/tables were inspected directly; HTML rendering and
an independent review of the later completion prose were not performed.
Default staged `git diff --check` flags the retained patch's blank context markers
and original review Markdown's two-space hard breaks. Those artifacts are kept
byte-for-byte; all other staged paths pass the whitespace check, and the flagged
lines were inspected as these expected artifact forms.
