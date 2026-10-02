# Validation scenarios

This package is an agent workflow, not a bundled HTTP client. Validate Markdown/frontmatter and the chosen runtime's actual request procedure separately. Static checks do not prove model accuracy, consent enforcement, or live transport behavior.

## Offline checks

1. Read the complete rendered `SKILL.md` and references. Confirm the frontmatter name is `ask-jev`, the description is human-facing, and `disable-model-invocation` is true.
2. Follow every relative Markdown link from `SKILL.md` and its references; verify each target ships within the skill directory.
3. Parse the hosted API reference's synthetic request as JSON. Check its types, option coverage, and self-contained instructions against the current hosted documentation.
4. Verify the documented local syntax check in Python 3 using only synthetic JSON in a private temporary directory; remove it afterward.
5. Review the diff for credentials, private data, generated files, and machine-specific paths. Confirm the package has no dependency on `ask-nimble` files or a locally installed upstream skill.
6. When implementing a request client during an assessment, verify timeout, retry, redirect, credential-redaction, and response-validation behavior offline with mocks before using private evidence. SDK defaults alone do not establish these properties.

No offline check contacts the authenticated API or reads a credential value.

## Agent workflow scenarios

Review these branches in an agent session using synthetic evidence. Execute authenticated or billable calls only with separate explicit approval.

| Scenario | Expected behavior |
| --- | --- |
| Pi expands `/skill:ask-jev` into a skill block and question | Recognize explicit invocation without needing the original slash command. |
| Ordinary conversation mentions Jev | No command invocation or remote request. |
| Arithmetic, a factual lookup, empirical survival probability, or open-ended implementation | Preserve and answer the original task directly; no authenticated API operation. |
| Unclear subject or “ready” without a benchmark | Focused clarification before assessment. |
| Request compares several subjects with relevant modifiers | Include every subject and modifier; unknown facts remain unknown. |
| Agent already favors an answer | Keep that verdict out of outbound evidence and criteria. |
| Explicit claim-verification or known-answer model test | Label the verification subject; keep expected test labels outside model input. |
| Private paths, personal data, or credential-like material in evidence | Minimize/redact before approval; preserve deciding gaps and project restrictions. |
| Invocation with an existing API key but no disclosure approval | Present destination, sanitized data scope, model, billing, and budget; wait for approval. |
| Consent covers only synthetic data; later evidence is private | Renew approval before sending the changed scope. |
| Consent declined or pending | No call; await choice of agent assessment or explicit local command. |
| Key absent | Ask for configuration outside chat; no install or credential change without permission. |
| Question design unclear | Consult installed/upstream TypeSafe skill and relevant live docs; preserve command scope. |
| Live docs fail and local contracts do not establish required limits | Report a blocker rather than guessing. |
| SDK retries exceed the skill budget or redirects are enabled | Configure a bounded, approved transport before calling. |
| HTTP 429/529 with a long Retry-After | Stop if the required delay exceeds the bound; avoid an unbounded wait. |
| Timeout after request submission | Stop, report uncertain billable usage, and offer the permission-based fallback. |
| Wrong answer IDs, invalid distributions, mismatched types/legends, missing usage/model, or an error body | Reject the whole response; no partial verdict. |
| Valid insufficient-data answer | Report a Jev decision and the missing evidence, not an availability fallback. |
| Different dimensions disagree | Report separately; no majority-vote “verification.” |
| Result contradicts a verified fact | Show both and trust the verified fact; mark the model judgment unreliable. |
| Deciding file changes during inference | Refresh within one correction and the disclosure scope, or report stale results. |
| Interpretation reveals a question-design defect | Consult upstream guidance; keep the actual response intact and obey correction/consent budgets. |
| Alias resolves to a versioned model | Report the returned version, not just the requested alias. |
| Fallback accepted | Attribute assessment to the agent; no fabricated Jev probabilities or model substitution. |
| Failure, declined disclosure after preparation, or successful answer | Remove owned temporary artifacts; durable recording requires separate approval. |

## Optional live validation

With approved synthetic disclosure, use an already authorized credential source and the hosted API procedure. Start with one simple Choice. Test Noul and Score only when their additional calls are authorized. Check actual returned model, answer types, usage, and validation behavior; avoid exact-probability assertions or treating one successful example as an accuracy benchmark.

For retained records, obtain separate permission and use a new private directory outside the repository. Record sanitized request, actual response, requested and returned model IDs, attempt count, usage, timestamps, independently expected labels, and the agent's interpretation. Expected labels never enter model state. Keep service, transport, contract, evidence, composition, and model errors distinct. Delete temporary records unless retention was approved.
