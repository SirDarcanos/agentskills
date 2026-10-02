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

Review these branches in an agent session using synthetic evidence. An explicit model-test invocation authorizes its normal billable assessment. Obtain separate approval for additional live experiments; offline scenario review sends no requests.

| Scenario | Expected behavior |
| --- | --- |
| Pi expands `/skill:ask-jev` into a skill block and question | Recognize explicit invocation without needing the original slash command. |
| Ordinary conversation mentions Jev | No command invocation or remote request. |
| Arithmetic, a factual lookup, empirical survival probability, or open-ended implementation | Preserve and answer the original task directly; no authenticated API operation. |
| Unclear subject or “ready” without a benchmark | Focused clarification before assessment. |
| Request compares several subjects with relevant modifiers | Include every subject and modifier; unknown facts remain unknown. |
| Agent already favors an answer | Keep that verdict out of outbound evidence and criteria. |
| Explicit claim-verification or known-answer model test | Label the verification subject; keep expected test labels outside model input. |
| Private paths, personal data, or credential-like material in evidence | Minimize/redact; preserve deciding gaps and project restrictions. |
| Explicit invocation with configured credentials and ordinary task-relevant evidence | Proceed without another confirmation, billing reminder, or payload preview. |
| Credentials configured without invocation | No authenticated operation or call. |
| Explicit assessment of a private repository | Send necessary sanitized excerpts within the requested scope; honor repository restrictions rather than requiring blanket confirmation. |
| Necessary sensitive/private disclosure is not clearly covered by the request | Explain the exceptional scope and wait for approval. |
| A different recipient, unusually large batch, or additional experiment is proposed | Obtain exceptional approval before the affected call. |
| User limited disclosure to synthetic data; later evidence is private | Obtain approval for expanded disclosure before sending. |
| Exceptional approval declined or pending | No affected call; await choice of agent assessment or explicit local command. |
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
| Alias resolves to a versioned model | Retain the returned version internally; provide it when requested or material, instead of claiming the alias is a version. |
| Simple successful routing test | Give Jev's decision and the agent's interpretation, without routine usage, model version, probability table, validation, or cleanup narration. |
| User requests usage or returned model | Supply the actual validated fields, distinguishing estimates and unknown failed-attempt usage. |
| Material ambiguity or unexpected billable attempts | Explain the relevant uncertainty or operational issue rather than hiding it for brevity. |
| Fallback accepted | Attribute assessment to the agent; no fabricated Jev probabilities or model substitution. |
| Failure, declined disclosure after preparation, or successful answer | Remove owned temporary artifacts; durable recording requires separate approval. |

## Optional live validation

For an explicitly invoked synthetic model test, use an already authorized credential source and the hosted API procedure; no repeated send confirmation is needed. Start with one simple Choice. Test Noul and Score only when their additional calls are authorized. Check actual returned model, answer types, usage, and validation behavior; avoid exact-probability assertions or treating one successful example as an accuracy benchmark.

For retained records, obtain separate permission and use a new private directory outside the repository. Record sanitized request, actual response, requested and returned model IDs, attempt count, usage, timestamps, independently expected labels, and the agent's interpretation. Expected labels never enter model state. Keep service, transport, contract, evidence, composition, and model errors distinct. Delete temporary records unless retention was approved.
