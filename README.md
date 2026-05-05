# Aura Voice Cortex — Research Repository

**Pre-registered N=100 paired study comparing the Aura Voice Cortex prompt against bare-prompt scoring on three frontier-class LLMs.**

> *AI detectors are mostly crap. That's not the point.*
> *Aura is built differently. We publish the data.*

This repository contains the full methodology, dataset, prompt, scripts, and findings for the Aura Voice Cortex 2026-04-28 detection study. Built in plain sight, per the Darke Mode commitment.

## Headline result

**Across three frontier-class LLMs (Anthropic Claude Haiku 4.5, DeepSeek V3.2, OpenAI GPT-5.4-mini), the Aura Voice Cortex prompt reduces AI-likeness scoring error by 4.6–9.8 MAE points (95% CI) compared to a bare "rate 0–100" prompt on the same model.**

| Model | N | Cortex MAE | Native MAE | Mean Δ | 95% CI |
|---|---|------|------|------|------|
| Claude Haiku 4.5 | 100 | 15.12 | 21.87 | +6.75 | [+2.11, +11.63] |
| DeepSeek V3.2 | 94* | 15.97 | 23.41 | +7.45 | [+2.52, +12.19] |
| GPT-5.4-mini | 100 | 16.89 | 24.27 | +7.38 | [+3.43, +11.54] |
| **Cross-model pooled** | **294** | — | — | **+7.19** | **[+4.61, +9.82]** |

Pre-registered "meaningfully better" threshold: CI lower bound ≥ 2.0. Cross-model lower bound: **+4.61** — more than 2× the bar.

*DeepSeek N=94 because 6 samples encountered transient OpenRouter routing failures during the run.

## The class-stratified finding

The Cortex's gain is concentrated on the **human-written** content class. Bare-model APIs systematically over-flag genuine human writing as AI; the Cortex prompt prevents this:

| Class | Haiku Δ | DeepSeek Δ | GPT-5.4-mini Δ |
|-------|---------|-------------|------------------|
| clear_ai | -2.39 | +8.03 | -2.28 |
| **human** | **+23.79** | **+16.31** | **+14.56** |
| ambig | -6.68 | -5.76 | +10.08 |

On the human class, native-prompt MAE is 26–35; Cortex MAE on the same content is 8–20. The 14–24 MAE-point preservation holds across all three model families.

**The Cortex is a human-writing shield.**

## Why this matters for the AI-detection category

To our knowledge, this is the first commercial AI-detection study published with:

1. **Pre-registered hypothesis + threshold** declared before model runs
2. **Bootstrap 95% confidence intervals** on the headline claim
3. **Class-stratified disclosure** (clear-AI / human / ambig as separate columns)
4. **Per-sample raw data** published alongside analysis
5. **Full detection prompt published** in plain text
6. **Negative findings reported** (Cortex hurts on clear_ai class for 2 of 3 models — disclosed openly)

A scan of GPTZero, Originality.ai, Copyleaks, Winston AI, Sapling, Turnitin, ZeroGPT documentation found marketing accuracy claims (typically 99% with no CI), high-level methodology descriptions, and intermittent third-party validation studies — but no commercial vendor publishes pre-registered hypotheses, per-sample data, or the actual detection prompt.

We invite competitors to match the methodology and publish their own.

## Repository structure

```
.
├── README.md                       — this file
├── LICENSE                         — CC0 1.0
├── analysis.md                     — full pre-registered research note
├── cortex-detection-prompt.md      — the Aura Voice Cortex prompt (verbatim from production)
├── run_experiment.py               — paired-comparison runner
├── analyze.py                      — bootstrap 95% CI analysis
└── data/
    ├── labels-v2.json              — N=100 hand-labeled samples
    ├── results-v2.csv              — every (sample × model × condition) score, 600 rows
    ├── experiment-v2.log           — full run trace
    └── build_labels.py             — script that built labels-v2.json
```

## Reproducing the study

You'll need:
- An OpenRouter API key (paid models — total cost ~$5)
- Access to the Aura Voice Cortex API at `aura.darkemode.ai/api/check` (or your own deployment using the prompt in `cortex-detection-prompt.md`)
- Python 3.10+

```bash
# Clone the repo
git clone https://github.com/ldarke-pp/aura-cortex-research
cd aura-cortex-research

# Run the paired comparison
OPENROUTER_API_KEY=sk-or-... python3 run_experiment.py

# Bootstrap analysis with 95% CIs
python3 analyze.py
```

Or — to evaluate just the Cortex prompt against your own dataset — copy `cortex-detection-prompt.md` into your application as the system prompt for any chat-completions-compatible API. Use `temperature=0.2` and parse the JSON response.

## What's in production

The Cortex prompt published here is the version deployed at `aura.darkemode.ai/api/check` as of 2026-04-28 (Sprint 2.1c-trust + template-anchor patch + hard-floor). It runs on `openai/gpt-oss-120b:free` via OpenRouter for free-tier checks (with Gemini-2.5-flash-lite as fallback for resilience). Paid-tier integrations (in development) will use Anthropic Claude Haiku 4.5 with no-training providers.

## Inverse-symmetry implications

Detection is the inverse of voice extraction. The class-stratified result on human content (Cortex preserves human-band scoring; bare models over-flag) maps directly to the voice-extraction problem: bare-model voice extraction would over-flatten distinctive voice toward generic. The +14–24 MAE preservation on human content predicts that Cortex-pattern voice extraction will preserve voice signal where bare-model extraction would wash it out. Aura Sprint 2.3 (voice extraction) inherits the Cortex pattern for this reason.

## Limitations & known caveats

1. **Single primary rater** (Claude). Same-family bias acknowledged for Anthropic Haiku 4.5; mitigated by paired Cortex-vs-native comparison (controls for systematic rater bias) and confirmed across non-Anthropic model families (DeepSeek, GPT-5).
2. **N=100 is moderate.** A larger study (N=500+) would tighten CIs further. Budget capped at $5; future runs can scale.
3. **No ESL stratification yet.** Stanford's finding that AI detectors flag 61% of non-native English essays as AI is not directly tested in this v1. Authentic L2 patterns require curated dataset. v3 priority.
4. **No competitor head-to-head.** Same N=100 dataset run through GPTZero / Originality / Copyleaks for direct comparison would be the natural extension. Deferred to v2 of this study.
5. **Cortex hurts on clear_ai class for 2 of 3 models.** Disclosed openly in `analysis.md`.

## License

This work is licensed under [CC0 1.0](LICENSE). Free to use, study, fork, and adapt; attribution appreciated but not required.

## Citation

If you use this prompt, dataset, or methodology, please cite:

> Aura Voice Cortex Methodology Study (2026-04-28). darkemode.ai/research. CC0 1.0.

## About Aura

Aura is a Darke Mode product — a free AI-likeness checker that doesn't over-flag your writing as AI, plus paid-tier voice extraction that turns five writing samples into a portable voice profile usable across Claude, ChatGPT, Gemini, and other LLM tools.

Built by Lee Darke. An operator who got tired of AI that sounds like everyone else.

- Aura: https://aura.darkemode.ai
- Aura Studio (agency platform): https://studio.darkemode.ai
- Darke Mode: https://darkemode.ai
