# Ask Clef feasibility

## Finding

An explicitly invoked `ask-clef` workflow can reuse the evidence-gathering and bounded-judgment approach of `ask-nimble` and `ask-jev`. Local Ollama support is documented; this does not require a custom PyTorch server.

## Local route

- Ollama lists both `clef` (27B) and `clef-flash` (9B). Clef models require Ollama 0.35.1 or later and use `POST /v1/systemone`, with `model`, `state`, and named `questions`. Local requests require no API key. Sources: [decision documentation](https://docs.ollama.com/capabilities/decision), [Clef](https://ollama.com/library/clef), [Clef Flash](https://ollama.com/library/clef-flash).
- Questions support `choice`, `noul`, and `score`. Images may be supplied as base64 PNG, JPEG, or WebP; image URLs and data URLs are unsupported. Source: [Clef Flash API and examples](https://ollama.com/library/clef-flash).
- Use the HTTP API or TypeSafe SDK, not an ordinary chat prompt or `ollama run` decision workflow. The model page says decision models are not yet supported in the Ollama CLI or Ollama Python/JavaScript libraries. Source: [Clef Flash](https://ollama.com/library/clef-flash).
- The installed Ollama executable reported version 0.35.0 during this investigation, below the documented Clef requirement. No upgrade, download, server startup, or inference was performed. Hardware fit and local latency remain untested.

## Other routes

- Cloudflare hosts the models on Workers AI; Clef is available at `@cf/cloudflare/clef`. Hosted requests require a Cloudflare account ID and token, incur service billing, and disclose supplied evidence to Cloudflare. Sources: [Workers AI Clef documentation](https://developers.cloudflare.com/workers-ai/models/clef/), [announcement](https://blog.cloudflare.com/clef-decision-models/).
- The weights and custom schema head are released under Apache 2.0. The official Clef Flash Python example uses PyTorch 2.11 and Transformers 5.10.2, tested on an H200 CUDA GPU. Its `systemone` function accepts Jev/SystemOne request bodies. Sources: [Clef Flash model card](https://huggingface.co/Cloudflare/clef-flash/blob/main/README.md), [inference code](https://huggingface.co/Cloudflare/clef-flash/blob/main/joint_schema_model.py).

## Initial proposal (superseded)

The implemented packages use separate explicitly invoked `ask-clef` and `ask-clef-flash` commands, each pinned to its named local model. The paragraph below records the earlier proposal, not the shipped selection behavior.

Start with a local-only `ask-clef`, defaulting to `clef-flash`, with explicit selection of the larger `clef`. Reuse neutral evidence gathering, explicit criteria, insufficient-data outcomes, validated responses, and advisory interpretation. Preserve permission requirements for installations, upgrades, model downloads, and server startup. Never fall back silently to hosted inference. If hosted support is added, document its different disclosure and billing authorization explicitly.

Validate the current Ollama response contract rather than assuming all confidence and usage semantics match another implementation. Benchmark evidence-checking judgments locally before making speed or quality claims; vendor benchmarks do not establish performance on this machine or task set.
