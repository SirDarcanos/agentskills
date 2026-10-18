# Perplexity Decider: workings and assessment design

Read before designing the first assessment. This reference describes the published model and recommends task design; it does not authorize inference or establish local runtime performance.

## What is being scored

Perplexity describes `pplx-decider-v1-27b` as a decision model fine-tuned from Qwen3.8-27B. The published inference implementation uses a multimodal backbone and a trained 255-option linear readout rather than generating a natural-language answer:

1. Render the supplied state, question and option descriptions, with images when present.
2. Assign options single-token letter codes and disable thinking in the prompt template.
3. Read the final hidden state, compute readout logits and mask unused option positions.
4. Divide logits by a positive saved temperature and apply softmax over the available candidates.
5. Map probabilities back to named Choice options, the true side of Noul, or zero-based Score levels.

The inspected checkpoint saves a temperature of approximately 2.208. This is calibration scaling, not sampling temperature or a request parameter to tune for preferred results. Ollama's decision endpoint does not accept generation controls. Let Ollama construct the model-specific prompt; do not reproduce this Python wrapper or install its dependencies to use the skill.

No explanation or reasoning trace is returned. The agent's evidence-based interpretation must remain separately attributed. A batch is an API convenience: answers are not inputs to subsequent questions and do not independently verify one another. The model page's single-forward-pass description is not a latency or shared-computation guarantee for every runner.

## Probabilities and confidence

Probabilities are conditional on the supplied state, instructions and candidate set. A dominant candidate may still be wrong because the evidence is misleading, the rule is unclear, or the correct outcome was omitted. Use contrasting, mutually exclusive choices, with explicit missing-data and no-match outcomes as needed. Keep a stable candidate order; inspect and preserve ties rather than treating tie-breaking as stronger evidence.

Noul returns probability of true, not a severity score. Score returns the probability-weighted level index; a middle average may conceal mass at opposite ends of a rubric. Report the distribution when that matters.

Ollama documents Choice/Score confidence as `1 - H(p) / ln(N)`, a measure of distribution concentration. The pinned Hugging Face wrapper uses different formulas: Choice rescales the maximum probability above uniform; Score uses distance from the modal level. Do not mix confidence values/formulas across transports or claim that concentration measures correctness. Validate finite ranges and distributions without fabricating a reasoning trace or imposing a universal confidence threshold.

The model card's 85.71% aggregate across 11 benchmarks was measured through the Perplexity API. It is not an accuracy guarantee for local quantized Ollama inference, image judgments or a new domain. The model does not outperform Jev on every listed benchmark. Any operational thresholds require separate, authorized evaluation on relevant independently labeled examples.

## Artifact and runtime distinctions

At inspection, Ollama's default/27b tag selected a roughly 17 GB Q4_K_M artifact, digest prefix `733585a9ebb6`, advertising a 256K context window. Tags are mutable: record the actual installed digest after authorized discovery; neither the tag nor returned model name proves an immutable revision.

The Hugging Face example requires Python 3.12 and about 49 GiB of weights plus working memory on CUDA. Those are requirements of that full-precision example, not requirements to copy into an Ollama skill. Download size is not runtime RAM, and advertised context is not loaded context. The published Python wrapper defaults to an 8,192-token question-branch limit; do not mislabel that as Ollama's model context limit. Use the [API reference](ollama-api.md) for separate byte, question, image and context constraints.

The card's Qwen3.8 identity and the config's `qwen3_5` architecture identifier are distinct metadata fields; neither grants support for ordinary chat, tool use or video through System One.

## Sources and freshness

Inspected October 18, 2026; documentation pages are mutable and their publication dates are unspecified. Hugging Face revision `d8c3bd18e31dc1804433d38528b3e770019bf00c` was reported last modified October 12, 2026. Published-source inspection is not an executed model test. Recheck model/transport facts when the installed digest or relevant runtime changes; keep the skill local and fixed-model unless a separately approved change updates that contract.

- [Pinned model card](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/d8c3bd18e31dc1804433d38528b3e770019bf00c/README.md): identity, benchmark scope and full-precision example requirements.
- [Pinned inference source](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/d8c3bd18e31dc1804433d38528b3e770019bf00c/source/src/autojev/model.py): `decision_messages`, `DecisionModel.prepare/forward/predict`, and `answer`.
- [Pinned decision configuration](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b/blob/d8c3bd18e31dc1804433d38528b3e770019bf00c/decision_config.json): base identity, readout vocabulary and calibration temperature.
- [Ollama model page](https://ollama.com/library/pplx-decider) and [tags](https://ollama.com/library/pplx-decider/tags): System One integration, multimodal input and artifacts.
- [Ollama System One API](https://docs.ollama.com/api/systemone): transport limits, independent questions, response semantics and entropy-based confidence.

The skill's own code/instructions use the bundled MIT license. The separately downloaded model is Apache-2.0 according to its model card; this package does not redistribute weights, inference source or third-party SDKs.
