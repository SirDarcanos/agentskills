# Session-oriented workflow: ownership and transition

Design for [#133](https://github.com/SirDarcanos/agentskills/issues/133), under the authoritative [#132 product agreement](https://github.com/SirDarcanos/agentskills/issues/132). **Proposed — consequential ownership and authority decisions await maintainer acceptance.** This document neither changes the shipped skills nor approves ADR supersession, project-policy changes, installations, model calls or downstream execution. #133 remains incomplete until the decisions below are accepted and required record reconciliation is authorized and available.

## Inputs and scope

Inspected source baseline: `45e5a24`. Current comparison: `dd02798` (the #142 advisor rename is the only intervening source delta). The accepted [composable design](composable-delivery.md), its [inventory](composable-delivery-inventory.md), [validation mapping](composable-delivery-validation.md), and [ADR 0002](../adr/0002-composable-delivery-ownership.md) establish the existing ownership and guarantees. Their historical results remain unchanged. This design proposes only the deltas needed by #132; it does not redesign the five methods or the two delivery scopes.

The inventory below covers all 22 engineering packages, all five writing packages and all five model packages at the inspected revision. Package entry points and their conditional links were inspected; model integration inspection covers the operating/authorization seams, not live service behavior. [Reading paths and design sketches](session-oriented-reading-paths.md) pin representative loads and observable examples. Those sketches are design material, not installable replacements or executed agent trials.

## 1. Smallest useful project agreement

The target project owns common operating guidance. Setup authors or reconciles that guidance; it is not the runtime owner of each project's decisions. Preserve existing meaningful homes and customizations. A concise entry point links the agreement; context can be inline or separately linked. There is no mandatory filename, template version, hash, glossary, ADR directory, tracker, model-policy file or installed common-contract package.

A usable agreement resolves these responsibilities, in prose or existing equivalents:

| Responsibility | Minimum meaningful guidance | Conditional detail, not common loading |
| --- | --- | --- |
| Context and decisions | Purpose, relevant operating constraints, who confirms intent/consequential commitments, and agent ownership of routine engineering | Product sources and affected domain records |
| Requested effects | Which ordinary actions are allowed; explicit restrictions; user-selected stage transitions; authority for artifact publication and branch operations | Tracker destination/role mappings, settings and release procedures |
| Safety | Preserve unrelated work/history/links; truthful evidence; no inferred permission for destruction, sensitive disclosure, spending, installation, credentials, merge, deployment or release | Exact environment/action approvals |
| Verification and review | Risk-appropriate checks, missing-material-check blockers, applicable independent Standards/Spec review, freshness and repair expectations | Snapshot mechanics, method loops, review packet, repair counting |
| Documentation | Maintain confirmed authorized meanings in their authoritative home; selective ADRs need explicit agreement/permission and preserved rationale/history; maintain changed docs/changelog as applicable | Actual glossary/ADR/release homes, when used |
| Evidence and continuation | Same-session evidence may remain in conversation; user selects persistence; active owners, uncertain effects and spent allowances survive interruptions | Coordination/recovery and explicit handoff procedures |

Do not require an explicit permission value for every imaginable action before read-only analysis can proceed. Unknown permission remains ungranted for the affected effect. An explicit prohibition of all model assessments is meaningful guidance, not an incompatible agreement. No model policy means no autonomous assessment permission. A project without a tracker can support shaping, diagnosis and direct local work; tracker publication remains unavailable until its destination and authority exist.

### Semantic compatibility check

Each project-oriented entry performs this short check, using guidance already in its context:

1. Locate applicable entry-point rules and the actual agreement; follow relevant context/authority pointers. Check directory and runtime restrictions too. Read fully when needed; recover truncated reads and resolve links from their containing source. Do not read every optional record.
2. Compare the responsibilities above with the requested operation. Reuse compatible guidance regardless of filenames, wording or whether Setup originally produced it. Record a specific absent, conflicting or unverifiable responsibility, not a generic “setup not run.”
3. Continue supported work within authority. Missing common decision/safety/verification guidance blocks the dependent project workflow with a recommendation for explicit setup/reconciliation. Missing tracker/model/domain detail blocks only that capability. Do not invoke setup, create empty records or fabricate policy to proceed.
4. When a newer skill conflicts with existing guidance, identify the exact behavioral consequence and propose reconciliation to the authority owner. Preserve current permissions and decisions. A compatible unchanged project requires no setup ceremony or rewrite.

This check is a routing reminder in each entry, not another long shared library. The project's agreement is the authority. Skills retain their distinctive procedures and capability checks. Restrictions can make a requested effect unavailable without making the entire project invalid.

### Prerequisite classes

- **P — project work:** established agreement or meaningful equivalent; contextual/task-specific guidance only. Independent invocation does not bypass this prerequisite.
- **B — bootstrap:** explicit setup or repository setup can establish guidance before it exists; existing instructions, exact plan approval and safety gates still apply.
- **S — standalone, non-project:** general research, supplied-text writing or a named bounded assessment can use request-specific scope/authority without manufacturing a project. When applied to a project, P applies. Standalone assessment still requires its own exact invocation/permission gates.
- **A — advisor:** What Now works before setup and remains explicit-invocation, read-only and recommendation-only. It can recommend resolving prerequisites, never run setup or another skill.

Preflight, conflict resolution and handoff may safely inspect or describe an unconfigured project's state. They must report missing project authority rather than invent it; inspection is not authorization to continue writes/integration.

## 2. Package and caller map

Every P row consumes the agreement once per context and only relevant project context. References below are relative to the named package. `references/validation.md` (or assessment `testing.md`) is for package maintenance/exercises, not ordinary invocation. No blanket README/LICENSE loading is added; notices remain shipped and import/attribution work still inspects them when relevant.

| Package | Prerequisite and distinctive responsibility | Required shared guidance / conditional operational material | Completion boundary |
| --- | --- | --- | --- |
| `workflow/setup-project` | B; establish/reconcile agreement | Existing authorities; `documentation-contract.md`, `discovery.md`; `reconciliation.md` for existing/interrupted setup; `model-use.md` for permission decisions, `releases.md` for history, `issue-tracker.md` for tracker work, `domain-records.md` for actual domain work | Approved operations read back, partial/blocked effects explicit; no application/backlog/model execution |
| `workflow/github-repo-setup` | B; exact approved repository/settings operations | Existing agreement when present; `references/handoff.md` for setup assignments; actual organization/security constraints | Settings/files verified or explicitly blocked; no operating-policy rewrite |
| `workflow/shape-work` | P; clarify relevant intent and obtain plan confirmation | Agreement/product sources; Analyze/Research only for deciding gaps, Domain Modeling only for meanings/decisions | Confirmed plan and concern dispositions; offer next stage without starting it |
| `workflow/write-spec` | P; express supplied agreement with stable acceptance IDs | Publication destination/mapped spec role and readiness convention; `references/publication.md` and tracker library when publishing; analysis/domain only for gaps | Selected artifact authored and, by configured invocation default, published/read back; draft/local/review overrides honored; no tickets/build |
| `workflow/write-tickets` | P; cohesive decomposition/publication/reconciliation | Approved scope and exact native relationship/label effects; tracker procedure only for actual tracker work | Persisted bodies/roles/graph read back and concise linked ID/description table; no scheduling; partial writes explicit |
| `workflow/analyze` | P; technical readiness and method/check recommendation | Affected source/callers/coverage; Research/Domain only for gaps; method entries only for needed capability claims | Supported recommendation, missing facts explicit; no build |
| `workflow/research` | P or S; bounded cited source findings | Source/disclosure/retention authority; `references/delegation.md` only for authorized delegation | Findings with applicability/freshness/gaps; no implementation/publication transition |
| `workflow/domain-modeling` | P; authoritative meanings and selective ADRs | Existing document mapping; `references/handoff.md` for caller use; `vocabulary.md` or `decisions.md` only for the affected branch | Plan-only delta without writes, or approved records and preserved history; no application work |
| `workflow/investigate-bug` | P; finite reproduction/cause diagnosis and probe account | Expected behavior/source/environment; Analyze/Research only for gaps; Write Tickets only if ticket stage requested | Ticket-ready conversation diagnosis or honest investigation gap; no mandatory tracker outcome, no fix |
| `workflow/tdd` | P; meaningful red–green–refactor | Current agreement/checks; Preflight before Git writes; Domain only for changes; conditional coordination/repair library only if used | Current local evidence, wrong-reason failures rejected; no independent acceptance or next method |
| `workflow/prototype` | P; bounded runnable experiment | Same conditional owners as TDD; explicit hypotheses/run bounds/artifact disposition | Observations/learning and production limits; no automatic promotion |
| `workflow/characterize` | P; protect relevant legacy behavior | Same conditional owners as TDD; provenance, nondeterminism and sensitivity | Intended/unknown/defect distinctions and baseline protection; no new behavior acceptance |
| `workflow/acceptance-first` | P; executable approved workflow examples and checked increments | Same conditional owners as TDD; criterion-level environment/intent evidence | Local criterion results or blockers; no stubbed integration/acceptance claim |
| `workflow/build-and-check` | P; increment then immediate relevant check | Same conditional owners as TDD; adequate coverage reuse, proportionate non-code inspection | Checked increments or preserved partial work; no accumulated unchecked progress |
| `workflow/implementation-preflight` | P; safe branch/base/target preparation | Project Git flow, actual dirty/index/PR state | Suitable branch/target or blocker; no delivery/PR action |
| `workflow/resolve-merge-conflicts` | P; preserve compatible intent in authorized active operation | Integration approval and protected work; `references/git-mechanics.md` before resolution | Checked authorized continuation or preserved conflict; no new merge/rebase or broad cleanup |
| `workflow/work-on` | P; accountable single-change lead | Local build/verification/completion; selected method, Preflight, independent Review; conditional tracker, coordination, recovery and model policy | Implemented/verified/unverified/blocked result, PR-ready only when evidenced; no ordinary PR publication |
| `workflow/work-on-spec` | P; whole-spec frontier, bounded assignments, serial integration, aggregate evidence | Native tracker, `references/dispatch.md`, `aggregate.md`; Work On local verification/completion libraries and conditional coordination/recovery; writable bounded runtime required | Per-ticket and overall result, local versus integrated gates; no automatic PR or merge |
| `workflow/review-delivery` | P; independent Standards and Spec contexts | `references/handoff.md`, `scope.md`, `report.md`; agreement review authority and conditional coordination mechanics | Original separate current reports or independence/freshness blocker; no repairs/acceptance |
| `workflow/pr` | P; selected PR report/publication | Current delivery evidence; `references/impact.md`; `publication.md` only for requested remote action | Concise decision report and actual publication read-back; no repeated delivery, merge/closure/release |
| `workflow/handoff` | P (state-description exception above); explicit session transfer | Disclosure/destination/retention rules; existing recovery pointers only for interrupted active work | Accessible purpose-specific handoff or storage gap; no automatic continuation/new ledger |
| `workflow/what-now` | A; installed-workflow advice | Relevant existing restrictions; candidate entries and references only to substantiate recommendations | Advice only; no routing-engine redesign or execution |
| `writing/writing-for-agents` | P or S; checkable agent-facing instructions | Existing meaning/authority; `references/structure.md` for routing/pointers, `validation.md` finish gate; project-shipped helper provenance restriction retained | Scoped writing/review result; no policy invention or installed replacement |
| `writing/slop-guard` | S, P for project prose; preserve meaning/voice | Supplied text/claims; `references/pattern-catalog.md`; `fiction-patterns.md` only for fiction; load installed Stay Positive in the same mode only when constructive framing is requested/required, without reloading it when already active | Requested prose/critique; no workflow invocation |
| `writing/stay-positive` | S, P for project prose; constructive framing | Meaning/risk constraints; `references/decision-guide.md` and `casebook.md`; load and apply installed Slop Guard in the same mode. Both writing companion-loading rules remain unchanged by extraction | Requested prose/findings without weakened warnings or forced optimism |
| `writing/create-changelog` | P; evidence-backed initial history | Actual release convention/history; `references/example-changelog.md` for the creation format; explicit first-changelog invocation retained | Approved history, no invented releases or automatic publication |
| `writing/update-changelog` | P; notable change history | Existing complete changelog and release convention; example reference when the existing convention is Keep a Changelog | Concise authorized entry/correction; no version/tag/release action |
| `models/ask-clef` | S with exact named invocation; P and exact policy for autonomous project use | `references/authorization.md`, `judgment-design.md`, `ollama-api.md`; no Work On entry for policy alone | Validated advisory assessment or no-call/unavailable/gap; named local route unchanged |
| `models/ask-clef-flash` | Same gate; distinct named Clef Flash owner | Its own authorization/judgment/API references, never inferred from Clef permission | Advisory/no-call result, no substitution or delivery authority |
| `models/ask-nimble` | Same gate; distinct named Nimble owner | Its own authorization/judgment/API references, shared allocation if composed | Advisory/no-call result, bounded attempts/service ownership retained |
| `models/ask-jev` | Same gate; hosted named assessment | Its own authorization/judgment/`hosted-api.md`; disclosure/spend and exact route limits | Advisory/no-call result; no credential/service/retention expansion |
| `models/build-with-nimble` | P; application integration, not one-off consultation | `references/integration.md`, actual serving/API contracts when needed; task/service/data authority | Checked integration and gaps; no implicit model install, inference spend or production acceptance |

### One owner per rule

The project owns policy values; the specialist owns how to carry out its procedure. A short caller gate/pointer is not a second policy definition.

| Rule | Authoritative owner after migration | Caller disposition |
| --- | --- | --- |
| Common authority, stage selection, safety, documentation, evidence truth/freshness | Target agreement, authored through Setup's documentation contract | All P entries consume it; remove repeated general-policy paragraphs, retain distinctive failure modes |
| Agreement discovery/semantic prerequisite test | Setup documentation contract defines the output responsibilities; each entry performs the short compatibility check | No mandatory installed Setup read just to consume established guidance |
| Companion discovery, complete-read recovery, missing-helper behavior | Target agreement's common operating guidance | Local entries name needed capabilities and unavailable-route boundary, not a universal dependency catalog |
| Product confirmation / stable spec IDs / cohesive tickets | Shape Work / Write Spec / Write Tickets respectively | Leads reuse returns; no repeated interviews or prose approval for unchanged commitments |
| Native IDs, pagination, parent/blocker graphs, cycles and remote read-back | Setup's maintained tracker library (existing owner) | Load only on native graph/publication work; library access never invokes setup |
| Branch/base/protected Git preparation | Implementation Preflight | Methods/leads inspect current result, not duplicate algorithm |
| Method loop, oracle and artifact semantics | Each of the five methods | Work On selects method and inspects return, does not repeat loops |
| Snapshot mechanics and review independence/neutral packets | Review Delivery | Leads supply current full dirty scope and raw checks; no HEAD-only substitutes |
| Local evidence sufficiency, findings, repair counting and delivery gates | Work On verification/completion | Work On Spec supplies aggregate scope; standalone corrective callers load only needed library |
| Worker lifecycle/ownership/root allocation | Conditional Work On coordination reference, split from `contracts.md` | Used by research, specialists, review and both leads only on delegation/active-worker routes; no installed common-contract package |
| Cross-ticket eligibility, frontier, rolling scheduling and serial integration | Work On Spec dispatch | Uses native procedure and coordination library, adds no parallel ledger or limits |
| Concurrency restrictions and finite repair allowance | Target agreement, preserving approved restrictions; two automatic repair cycles remain the delivery ceiling | Conditional coordination implements lead-chosen concurrency; completion implements counting/lineage without raising the ceiling |
| Exact model permissions/budgets/lifecycle/fallback and approval provenance | Target's approved model policy, if any | Setup authors; lead reserves; named assessment rechecks/enforces transport/attempt ceilings; no mandatory Work On policy library |
| Evidence persistence destination | User-selected destination under target retention policy | Handoff/PR/ticket owners persist only their requested artifact; active-operation records are not unsolicited handoffs |
| PR impact accounting/publication | PR | Delivery returns its own outcome; PR runs only when that stage is selected |

### What leaves Work On's common contract

Move common authority, semantic discovery, compact scope/evidence/return expectations and ordinary evidence-location defaults into project guidance. Move model policy values/accounting authority to the existing model-policy home, retaining API-specific enforcement in named packages. Keep coordination mechanics as a **conditional local reference** in Work On; keep repair counting in completion, snapshot mechanics in Review, graph mechanics in Setup and recovery at the responsible lead. Remove the global capability table after every live caller names its actual needed capabilities. Do not replace `contracts.md` with an equally large always-read project manual.

For ordinary same-session work the sufficient record is the request/agreement, scoped actual changes, deciding evidence, check results/limits and next action already in context. No run ID, worker reservation table, hypothetical future-session pointer or durable report is required when those obligations do not exist.

Delegation adds root/assignment identity, owned scope/interfaces, finite runtime, actual lifecycle and uncertain operations. Recorded acceptance repairs add checkpoint/finding lineage and spent cycles. Authorized assessment use adds reservations/actual attempts and uncertain charges. These are live safety records, not optional facts erased at a session boundary. Reconcile them before replacement, conflicting writes or retries. If a session cannot safely continue, stop/isolate or preserve the necessary active-work record at an approved location; if no safe retention/stop route is authorized, report the blocker rather than fabricate a freed owner or zero budget. Ordinary inactive work need not acquire these records just because another session is imaginable.

## 3. Staged compatibility and caller reconciliation

These are implementation gates, not a new ticket schedule or graph mutation. Existing native blockers remain authoritative. The approved tickets #134–#143 own the affected packages; #145's separate readiness correction must be reconciled where it overlaps #137. #142 is already integrated and must retain its recommendation-only behavior.

1. **Accept design and authorize record delta.** Obtain decisions D1–D4 below; perform only the specifically approved ADR/operating-record reconciliation. Until then, dependent implementation cannot treat this proposal as policy. #133 can retain a reviewed proposal without claiming completion.
2. **Establish output and conservative bridge (#134).** Setup learns compact agreement authoring/semantic reconciliation. Existing consumer permissions remain unchanged. Keep every live Work On library target and its unique guarantees intact. New output must support both migrated package gates and legacy consumers until their caller updates land. A bridge does not make old investigation/PR endpoints equivalent to #132; declare those routes not yet migrated rather than relabeling their behavior.
3. **Migrate procedure owners with their callers (#135–#141).** In each cohesive source change, update entry, relevant references, frontmatter/metadata, README and validation together. A new pointer and its target ship together. Research delegation, Analyze/Shape/Write Spec/Write Tickets delegation, all five methods' delegation/correction gates, Review handoff, PR delegated/corrective route, Work On Spec entry/dispatch/aggregate/recovery, and Handoff recovery pointers must stop requiring the old universal contract before it is retired. Assessment authorization references already own direct/shared reservations without requiring a delivery companion; preserve that independence and reconcile any affected caller pointers without introducing a new dependency. Work On's thin product/readiness/ticketing/dispatch adapters also remain discoverable until their callers are reconciled. Audit Markdown, scripts, fixtures and embedded instruction strings, not just entry links.
4. **Cut over endpoints coherently.** Investigation and Work On readiness adapters accept complete conversation diagnosis without a ticket. Artifact owners implement selected publication without duplicate full-text approval. Both delivery leads and PR remove the competing automatic-publication default; dispatch reports a required predecessor PR/merge as a user-selected-stage blocker, not implicit permission to publish. Cross-ticket integration cannot bypass project-required accepted merge. Handoff never becomes a mandatory storage workaround. Stage-compatible releases must identify the coherent source revision and semantic requirements; an unmigrated package retains its old boundary or blocks the affected new route explicitly.
5. **Retire compatibility only after caller proof (#139/#140 with #143 validation).** Search the full tracked source/test/docs set for old library targets, classify historical versus live references, and inspect every live caller. Remove obsolete bodies/targets only with zero unreconciled live callers and working replacement paths; preserve history. A temporary adapter forwards to the sole owner and states unavailable behavior, never carries a second permanent policy. Verify copied-package links, non-sibling discovery and old/new mixed-set failures. No automatic installation, aliases or service are introduced.
6. **Validate complete paths and document actual delivery (#143).** Human guide teaches stage choices; catalog, package docs and changelog describe only shipped behavior. Execute representative and failure-path checks, compare real mandatory read closures, and distinguish static measurements from observed agent behavior. Source integration does not migrate installed copies; any later installed operation needs its own exact inventory/approval/backup scope.

## 4. Proposed decision-record and operating-policy delta

Domain Modeling was followed inline in **plan-only** mode for this bounded ownership question: its entry, handoff and decision-record procedures, CONTEXT, ADR 0002 and the accepted design were inspected. The owner returns the following mutation-free plan; this design records that plan under #133's explicit design authority. No ADR draft, glossary edit, accepted-status change or operating-policy edit is applied here.

The ownership change qualifies for an ADR: copied packages gain a project prerequisite, compatibility changes have ongoing maintenance cost, and common-library reuse versus project-owned guidance is a real trade-off. Existing glossary meanings suffice; no CONTEXT delta is needed.

| Decision | Recommended proposed delta | Preserved material / approval needed |
| --- | --- | --- |
| **D1: guidance ownership and prerequisites** | Accept sections 1–2: project-owned common agreement, semantic equivalence, explicit bootstrap/non-project exceptions, conditional package mechanics rather than mandatory Work On common library | Independent packages/two leads remain. Approve this ownership change before #134+ rely on it |
| **D2: endpoints and persistence** | Accept sections 2–3: configured spec/ticket invocation selects publication; diagnosis ends without ticket; delivery ends before PR; persistence is user-selected except actual live safety obligations | #132 already supplies product direction; approval here settles concrete shared/caller ownership and bridge, not a new product interview |
| **D3: ADR reconciliation** | After separate permission, create next available `docs/adr/0003-session-oriented-project-agreement.md` (recheck numbering); record D1/D2, alternatives and consequences. Mark ADR 0002 superseded for common-guidance/endpoint/persistence ownership, linking replacement and retained decisions reciprocally | Preserve ADR 0002's full rationale, ADR 0001 history and #48 evidence. Record that #130 already changed the old worker ceiling; preserve two-cycle repairs and current concurrency restrictions, no new safety limit. Do not mark accepted until explicit acceptance; a proposed replacement leaves ADR 0002 in force |
| **D4: operating reconciliation** | In `docs/agents/workflow.md`, Authority and Branches/PRs: retain branch/commit/push permission within approved scope, require explicit user-selected PR preparation/publication rather than delivery-triggered PR; Verification: keep applicable independent review/truthful checks; Documentation: point conditionally to accepted replacement after authorization. In `AGENTS.md`, add conditional #132 design/status pointer once accepted; do not load design on unrelated work. Keep project context unless a changed constraint is approved | No widening optional delegation/model permissions; current repository permits only bounded independent-review delegation without a separate grant. No settings/label/edge changes. Apply exact prose delta only after approval; don't use the proposed sketch as current repository policy |

Accepted composable-design sections affected: **Ownership and standalone boundaries** (write-spec, investigation and delivery rows); **Current procedure destination map** (`contracts.md` destination); **Minimal handoff and reusable evidence** (ordinary versus active state, persistence); **Companion compatibility and invocation** (project prerequisites/conditional libraries); **One execution and repair ledger** (conditional recording, unchanged guarantees); **Staged publication and migration** (this transition, no installed effects). After approval, add a concise supersession pointer/delta notice to that accepted design rather than rewriting old inventories, paper checks or executed results. Model-use permission, migration transaction/rollback, method loops, snapshot integrity and the two delivery scopes are retained. This proposal changes no domain definition.

**Decision boundary:** accepting this design can settle D1/D2; applying D3/D4 still needs approval of those exact record/policy operations. #133 completion requires accepted consequential decisions and available authorized record reconciliation, not merely a merged document labeled proposed. Do not close it or unlock #134 based on a design-file merge alone.

## 5. Acceptance and observable validation

The [path evidence](session-oriented-reading-paths.md) includes baseline manifests, proposed design-only reading surfaces, counting rules and examples. It establishes inspectable design costs and expected boundaries, not implemented WF-11 compliance. Each downstream owner must measure the actual final closure (including contextual and reviewer loads) and run relevant checks.

| #132 | Design coverage / downstream verification |
| --- | --- |
| WF-01 | One target agreement; Setup output mapping and no layout mandate; #134 new/existing fixtures |
| WF-02 | Semantic check and P/B/S/A inventory; #134–#141 missing/compatible/conflicting cases |
| WF-03 | Routine lead decisions retained in each responsibility; no seam/worker questionnaire; #135/#136/#139/#140 |
| WF-04 | Completion column plus stage examples; explicit compound request can cross authorized stages; #137–#140 |
| WF-05 | Shape owns confirmation/concern dispositions, not publication; #137 |
| WF-06 | Spec/ticket selected publication, exact scope/graph authority and concise links/table; #137 and overlapping #145 readiness reconciliation |
| WF-07 | Conversation diagnosis and optional ticket stage; Work On adapter consumes it; #138/#139 |
| WF-08 | Both leads stop before PR, including dispatch's accepted-merge waiting case; #139/#140 and PR integration |
| WF-09 | Ordinary context versus active ownership/repair/model state distinguished; explicit Handoff owns chosen persistence; #140 |
| WF-10 | Current work maintains confirmed authorized domain records; ADR plan-only/approved boundary; #135 and D3 |
| WF-11 | Reproducible baseline/illustrative proposed paths, conditional references, per-context accounting; actual closure/trials required in #143 |
| WF-12 | Existing equivalent agreement reuse and exact conflict reconciliation; no skill-update permission import; #134 |
| WF-13 | #142's rename integrated at current comparison, unchanged advisory contract preserved; #143 confirms routing/references |
| WF-14 | Rule-owner map and safety examples retain material-check blockers, independent review, protected work, repair lineage and consequential gates; all affected owners |

#133's five acceptance items map respectively to: package/caller map and prerequisite classes; minimal agreement/semantic check and extraction; staged compatibility/live-state distinction; path evidence and examples; D1–D4/accepted-design delta. Items 1–4 are design deliverables, not runtime acceptance. Item 5 remains pending maintainer decisions and authorized record reconciliation.

Documentation disposition for this design change: add this design and its reading-path companion only. No changed public runtime behavior means no changelog/release-impact entry, package README/catalog update, installed replacement or glossary change yet. Historical evidence and accepted ADRs remain untouched. Independent design review and document checks can verify the proposal's consistency; they cannot supply maintainer acceptance or demonstrate runtime efficiency.
