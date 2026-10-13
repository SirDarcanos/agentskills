# Decision model comparison

100 synthetic text cases, shared unchanged across local Nimble, Clef, Clef Flash, and hosted Jev. The corpus contains **120 labeled questions**: 90 Choice, 10 Noul, and 20 Score.

This is a controlled regression suite, not a measure of general intelligence or production accuracy. Ten variations of a rule are related examples, not ten independent real-world tasks. All four models receive the same state, question instructions, and criteria; only the transport and requested model differ.

## What is tested?

Each category has ten cases:

| Category | Known-label basis |
| --- | --- |
| Authorization scope | Match both account and refund; check signer, missing fields, duplicate records, and unresolved conflicts. |
| Policy exceptions | Enumerate possible completions of unknown fields; apply a defect exception before return-window/final-sale restrictions. |
| Revision precedence | Ignore unrelated entities and superseded revisions; check only the highest relevant revision. |
| Negation and scope | Authored annotations distinguish current requests from negation, quotes, history, another speaker, and conditional requests. |
| Evidence support | Match the entity and time before deciding support, contradiction, or insufficient evidence. |
| Semantic routing | Authored annotations apply stated team boundaries to paraphrased requests and explicitly excluded topics. |
| Untrusted instructions | Ignore injected instructions in record notes while applying the actual authority policy. |
| Conjunction and unknowns | Check all required gates; distinguish a known failure from missing evidence. |
| Ordinal rubrics | Apply a four-level urgency rubric with explicit precedence and boundary cases. |
| Independent dimensions | Judge access, receipt presence, and urgency separately, including disagreeing outcomes. |

[`cases.py`](cases.py) is the authoritative corpus definition. It produces exactly 100 distinct request payloads with IDs, categories, expected answers, label sources, and rationales. Rule-based labels are computed by deterministic evaluators. Twenty language cases use explicit authored annotations rather than model-generated predictions; their wording and rationales should be reviewed before treating them as an application benchmark. No evaluation model supplied the gold answers.

Expected labels, rationales, category names, and fixture IDs remain outside model input. Policies and answer criteria naturally describe when each allowed outcome applies. These are the rules being evaluated, not hidden gold labels.

The existing seven-case fixtures inside the individual skills remain quick smoke tests. This larger corpus lives outside those standalone packages so there is one benchmark source of truth.

## Offline validation

Requires Python 3.9 or later; uses only the standard library. From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s benchmarks/decision-models/tests -p 'test_*.py'
PYTHONDONTWRITEBYTECODE=1 python3 benchmarks/decision-models/run.py
```

Offline validation checks case count, category coverage, gold-label types, request schemas, and the corpus hash. Unit tests additionally check reviewed label sequences, mutation/permutation properties, every model's response contract, expected-label isolation, ties, summaries, error handling, transport boundaries, and export compatibility. None accesses a model endpoint or credentials. Passing offline tests establishes consistency, not a human review of every semantic annotation or model accuracy.

## Live comparison

Run only with explicit approval for the selected models and call count. Local Ollama must already be running with the selected models downloaded: 0.35+ for Nimble, 0.35.1+ for Clef variants. The runner does not install, upgrade, download, start, or stop anything.

All three local models, sequentially, **300 requests total**:

```sh
python3 benchmarks/decision-models/run.py --live --models nimble clef clef-flash
```

Hosted Jev, **100 billable requests**, using `TYPESAFE_API_KEY` from the process environment:

```sh
python3 benchmarks/decision-models/run.py --live --models jev-latest --allow-hosted
```

Or explicitly select all four:

```sh
python3 benchmarks/decision-models/run.py --live --models nimble clef clef-flash jev-latest --allow-hosted
```

The environment that launches the process must contain the exported key. A long-running agent process may not inherit exports made in another terminal afterward. Use your existing authorized secret mechanism or launch the command from the shell that has the key; keep the key out of chat, command arguments, and logs.

Before hosted runs, recheck [TypeSafe's API](https://docs.typesafe.ai/api.md) and [models/pricing](https://docs.typesafe.ai/models.md). The runner uses the common text-only schema subset and `POST https://api.typesafe.ai/v1/systemone`. It rejects redirects and requires separate approval/configuration if an HTTPS proxy is present. No API key is accessed without `--live` and an explicitly selected Jev model. Local requests ignore proxies and use the fixed loopback decision endpoint.

Each case is attempted once, with a 300-second local or 120-second hosted timeout. There are no automatic retries, criterion changes, reruns for preferred labels, or model substitutions. A valid label mismatch continues the run. A transport or response-contract failure stops that model's run and reports remaining cases as not run; other explicitly selected models may continue. Ambiguous network failures may have been processed and billed: their usage remains unknown. Explicit 429/529 errors also stop rather than automatically spending retry calls.

## Read the results

The runner prints one JSON line per attempted case and one summary per model:

- **Whole-case correctness:** all requested dimensions must match to pass. Summaries show correct/valid/attempted/planned counts; incomplete runs are not comparable to completed ones.
- **Per-category counts:** identify which kinds of evidence or rules cause failures.
- **Per-question results:** show expected versus observed labels and separate Choice, Noul, and Score counts.
- **Ties:** fail the unique-label check and are counted separately, even when the API's tie-selected Choice happens to match gold.
- **Noul labels:** use which side of 0.5 the result falls on. This is a test-label decision boundary, not a production confidence threshold.
- **Score labels:** compare the uniquely highest-probability level to gold; also report the mean absolute error of the returned probability-weighted score. A diffuse distribution can have the correct modal label while a weighted score lies far from gold.
- **Failures:** keep model mismatches separate from service/contract errors and missing cases. Accuracy on valid responses alone must always be read alongside coverage.
- **Provenance:** corpus SHA-256, returned hosted model versions, local model digests/details, service-reported known usage, and unknown-usage counts.
- **Latency:** first-request time, median including all attempts, and median excluding the first request. Excluding the first is only a rough warm-run comparison—not a guarantee of cache state. Hosted times include the network; local quantizations and hardware differ.

This corpus does not test images, calibrated confidence, forecasts, very long context, external retrieval, agent evidence gathering, or production authorization. Never turn a synthetic pass percentage into the chance that a real-world decision is correct. Freeze the corpus hash for comparisons; keep failures and report wording defects before changing gold or instructions.

## Optional records and fixture export

Retaining regression records requires separate approval. Use a new private directory **outside the repository**; existing directories are refused:

```sh
python3 benchmarks/decision-models/run.py --live --models clef --record-dir /tmp/clef-benchmark-UNIQUE
```

Replace `UNIQUE` with a fresh suffix. Records contain synthetic requests, actual parsed answers, expected labels, rationales, timing, usage, and summaries. Keys are excluded. The runner retains no separate record files by default; ordinary command output may still be kept by the host runtime.

To inspect all 100 labels or reuse a skill's existing replay tool, export offline for one model to a new file:

```sh
python3 benchmarks/decision-models/run.py --models nimble --export-cases /tmp/nimble-fixtures-UNIQUE.json
```

Export uses the existing `version: 1` fixture format. It sends nothing and refuses to overwrite a file. Use the comparison runner for consistent envelope validation and category reporting across all models.

## Contract sources

- [Ollama System One API](https://docs.ollama.com/api/systemone): local schema, body limits, usage, and response fields.
- [Ollama decision guidance](https://docs.ollama.com/capabilities/decision): setup and supported local models.
- [TypeSafe API](https://docs.typesafe.ai/api.md) and [models](https://docs.typesafe.ai/models.md): hosted schema, model aliases, context limits, and billing.
