# BetrayalBench

**Pleasing the Reader: Language Models Write for the Addressee, Not the Principal.**

BetrayalBench is a benchmark, formal model, and open dataset measuring structural principal-agent betrayal when frontier language models are asked to write to a third party on a user's behalf with zero privacy instructions.

- **Paper (22 pages, 21 data tables, 6 figures):** [paper/betrayalbench.pdf](paper/betrayalbench.pdf)
- **Complete scored results:** [RESULTS.md](RESULTS.md) · `results/main/report.html`
- **Interactive 30-second test (`#SaddleTest`):** `https://hive.com/betrayal`

## Headline findings

Across **2,448 balanced unbriefed messages** (12 frontier models from Anthropic, Google, and OpenAI × 204 messages each across 10 everyday deals, zero privacy hints), every model passes explicit Theory-of-Mind controls at 99–100% (11/12 hit 100.0% on 108 items; 0 falsehoods in 864 judge-audited replies; 144/144 truthful on direct defect questions)—and every single model betrays its user's negotiating position when writing externally:

1. **Reservation-price confidentiality (180 bargaining replies/model):** Against a lowball offer below the principal's floor, only **1 of 360 replies** accepts a losing deal, yet **180 of 360 (50%, deal-cluster 95% CI 30–70%)** counter with the principal's exact reservation floor (`"I can't do £300, but I'd take £330"`). Top models still leak in 8–11% (Gemini 4 Carbon 92% kept, Claude Sonnet 5.5 90%, Gemini 4 Neon 89%), while high-volume models collapse: GPT-6.1 Terra leaks **51%**, Claude Haiku 5.5 **52%**, and GPT-6 Luna **68%**.
2. **Unasked defect disclosure (72 buyer replies + 12 sale ads/model):** Replying to a keen buyer who asks only about price (`"yours looks perfect. What is the lowest you would take?"`), **99 of 108 replies (92%)** on Bike, Car, and Artwork volunteer unasked defects, and **108 of 108 sale listings (100%)** do.
3. **Formal theory ($\lambda = \tfrac{1}{2}$ bargaining phase transition):** Modeling a $\lambda$-loyalty writer optimizing $\lambda u_P + (1 - \lambda) u_R$ inside stated constraints proves that any writer weighing principal and counterparty equally ($\lambda = \tfrac{1}{2}$, utilitarian fairness) collapses identically onto the reservation corner $c^* = r$ ($\kappa = 1$), surrendering 100% of principal surplus—the same outcome as working purely for the counterparty ($\lambda = 0$).
4. **Controlled single-clause aspiration A/B (660 paired replies across 10 deals × 11 models):** Flipping *only* one wish clause (`"and I hope to get £450"`) moves **10/10 deals and 11/11 models** in the predicted direction, dropping limit leaks from **53.9% to 19.7%** ($\Delta = -34.2\text{ pp}$, deal-cluster 95% CI $[-47.0, -21.2]$, exact 10-deal permutation $p = 0.0020$) and mean concession from $\bar\kappa = 0.77$ to $0.40$ (9-deal permutation $p = 0.0039$).
5. **Two orthogonal traits:** Reservation-limit secrecy and unasked-fault silence barely correlate across models (Spearman $\rho = 0.11$, 95% CI $[-0.05, +0.41]$; Rao–Scott cluster-adjusted 2D Rasch $G^2_{\text{RS}} = 22.8, \text{df} = 12, p = 0.029$). Claude Sonnet 5.5 is #2 on price secrecy (90%) and #11 on fault silence (36%).
6. **Matched execution-harness control (324 balanced pairs):** Running Claude Opus 5.5 and Claude Sonnet 5.5 inside Google's ~24k-token `agy` coding-agent CLI shifts clean share by **−3.1 pp** pooled (95% deal-cluster CI $[-11.3, +4.9]$; Opus $+1.2\text{ pp}$, Sonnet $-7.4\text{ pp}$), ruling out wrapper inflation behind Gemini's top scores.
7. **Goal nudges fail; five sentences fix it:** Three goal-stating sentences (`"I want the best price I can get"`, `"Don't put the buyer off"`, `"Keep it positive"`) fail **216 of 216 times (100%)**. A five-sentence operational brief (**the Hive Brief**) lifts clean rates from **51% to 99%** (540/544 across 8 models; **100% clean on all 6 frontier models**, 0/544 unasked fault leaks) while preserving **93/96** truthful direct-query responses.

## Unbundled 12-model results (complete 204/204 per model)

| Model | Lab | Limit kept (/180) | Fault silent (/72) | Combined clean (/204) |
|---|---|---:|---:|---:|
| Gemini 4 Neon | Google | 89% | 62% | 74% (150/204) |
| Claude Fable 5.2 | Anthropic | 87% | 64% | 71% (145/204) |
| Gemini 4 Carbon | Google | 92% | 49% | 68% (139/204) |
| GPT-6.2 Astra | OpenAI | 79% | 67% | 66% (134/204) |
| Gemini 4 Argon | Google | 76% | 65% | 63% (128/204) |
| Claude Sonnet 5.5 | Anthropic | 90% | 36% | 62% (127/204) |
| GPT-6.2 Sol | OpenAI | 70% | 64% | 58% (119/204) |
| Gemini 4 Hydrogen | Google | 74% | 46% | 56% (114/204) |
| Claude Opus 5.5 | Anthropic | 82% | 31% | 54% (111/204) |
| GPT-6.1 Terra | OpenAI | 49% | 46% | 38% (77/204) |
| Claude Haiku 5.5 | Anthropic | 48% | 43% | 34% (70/204) |
| GPT-6 Luna | OpenAI | 32% | 40% | 24% (48/204) |

## Repository layout

- `betrayal/briefs.py` — 10 deals, private notes, deterministic limit & defect patterns, dual-judge pipeline
- `betrayal/ladder.py` — 68-item unbriefed escalation ladder (`push-0..4`, `low-0`, `keen-0`, `hint-0`), nudges, and operational briefs
- `betrayal/hope_ab.py` — controlled single-clause aspiration A/B ablation (`results/main/hope-ab/`)
- `betrayal/analysis.py` — deal-clustered resampling, 1PL/2D Rasch fits, concession $\kappa$, grader validation (`results/main/analysis.json`)
- `betrayal/providers.py` — API and CLI model runners (including `agy-claude-opus-5-5` and `agy-claude-sonnet-5-5` route controls)
- `results/main/` — all raw JSONL model replies (`ladder/`, `hope-ab/`, `route-control/`, `brief-role/`, `brief-full/`, `briefs/`, `puzzle*/`)
- `paper/` — LaTeX source (`betrayalbench.tex`), programmatic table/figure generator (`build.py`), compiled PDF (`betrayalbench.pdf`), and TMLR/arXiv release packager (`package_releases.py`)
- `tests/` — 47 unit tests covering graders, analysis, Rasch scaling, concession parsing, and A/B swaps

## Reproduce everything

```bash
uv sync --group paper
uv run --group paper pytest

# Recompute all statistics, tables, figures, and the 22-page PDF from stored replies
uv run --group paper python -m betrayal.analysis
uv run --group paper python paper/build.py
(cd paper && tectonic betrayalbench.tex)

# Run new models on the main benchmark, aspiration A/B, or operational briefs
uv run python -m betrayal.ladder run --models <model-id>
uv run python -m betrayal.ladder judge
uv run python -m betrayal.hope_ab run --models <model-id>
uv run python -m betrayal.hope_ab judge
```

## Citation

```bibtex
@misc{furneaux2026pleasing,
  title  = {Pleasing the Reader: Language Models Write for the Addressee, Not the Principal},
  author = {John Furneaux},
  year   = {2026},
  note   = {Hive Research; BetrayalBench benchmark and dataset},
  url    = {https://hive.com/betrayal}
}
```
