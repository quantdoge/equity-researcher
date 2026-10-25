# Quant Analyst

- Symbol: RVMD
- Elapsed: 68.3s

---
# RVMD — Revolution Medicines, Inc. | Quantitative Factor Report

**Sector:** Healthcare / Biotechnology (clinical-stage precision oncology) · **Price:** $196.55 · **Mkt cap:** $42.1B · **Beta (reported):** 1.40

> **Critical framing before the numbers:** RVMD is a **pre-revenue, clinical-stage** RAS(ON) oncology company (lead assets RMC-6236, RMC-6291, RMC-4630). Classic value/quality/low-vol factors are structurally *not applicable* — the company has no earnings, no revenue, negative FCF. Factor scores below are reported faithfully but must be read as "not-investable-on-this-factor" rather than "cheap/expensive." The only factors carrying real signal here are **estimate revisions, momentum, and price/catalyst dynamics.**

---

## 1. Factor Scores

| Factor | Score / Raw | Sector Rank | Signal |
|--------|-------------|-------------|--------|
| **Value** | P/E −33.0 · EV/EBITDA −32.6 · P/FCF −40.9 · ROE −69.4% | **n/a** (negative multiples unrankable) | **Strong Sell / N/A** — pre-revenue, no valuation anchor |
| **Momentum** | 12-1 return **+4.84%** (252d, tool) — *see caveat* | n/a | **Positive but concentrated** (gain is gap-driven) |
| **Quality** | ROE −69.4% · GP/Assets −0.7% · Accruals −9.9% · **F-Score 1/9** | n/a | **Weak** (structural cash-burn, 0/4 profitability pts) |
| **Low Vol** | Ann. vol **65.8%** · β 1.22 (SPY) / 0.85 (XBI) · MaxDD 25.0% | n/a | **Unattractive** (high-vol, low-vol factor penalty) |
| **Earnings Revision** | +164.8% on **FY2030** EPS ($5.13→$13.59) | n/a | **Upgrade — LOW confidence** (see note) |

**Cross-sectional rank note:** The FMP "Healthcare" peer group returned is mega-cap pharma (LLY, JNJ, ABBV, MRK…). These are **not valid comparables** for a clinical-stage biotech — quintile ranks against them would be meaningless. No true pre-revenue oncology peers were available, so I have not fabricated sector ranks.

**Revision-score caveat:** The +164.8% "upgrade" is computed on the **FY2030** consensus (8 analysts, EPS range a huge **$4.62–$27.82**). It reflects analysts building out the post-approval RAS(ON) franchise, *not* near-term momentum. Near-term estimates remain deeply negative and are the honest picture:

| FY | EPS Est | Revenue Est | #Analysts |
|----|---------|-------------|-----------|
| 2025 | −$5.65 | $3.5M | 14 |
| 2026 | −$9.49 | $198M | 19 |
| 2027 | −$5.87 | $1.22B | 19 |
| 2028 | −$2.62 | $2.45B | 18 |
| 2030 | +$13.59 | $7.50B | 8 |

The consensus path implies **profitability only from ~2028–2030** — the revision signal is a long-dated DCF input, not a near-term trade signal.

---

## 2. Price Statistics

| Metric | Value | Comment |
|--------|-------|---------|
| **Alpha (ann., vs XBI)** | **+59.2%** | Large, but R² only 0.155 → alpha estimate carries wide error |
| **Beta (vs XBI)** | **0.852** | <1 to biotech index despite higher absolute vol |
| **Beta (vs SPY)** | **1.224** | Reported profile beta 1.40 |
| **R² (vs XBI)** | **0.155** | **~84.5% of variance is idiosyncratic** — a stock-specific, catalyst-driven name |
| **Sharpe** | **1.317** | Good, but on a 66% vol base |
| **Sortino** | **2.42** | Strong upside/downside ratio |
| **Ann. volatility** | **65.8%** (66.8% alt calc) | ~3–4× market; top-decile risk |
| **Max drawdown** | **24.95%** | Tool figure — see caveat |
| **Ann. return (tool)** | 87.9% | Directionally strong |

**Correlations (252d):** RVMD–XBI **0.39** · RVMD–IBB **0.39** · RVMD–SPY **0.24**. Low market correlation → little diversification benefit from index beta; the stock trades on its own catalysts.

---

## 3. Composite Quant Signal: **NEUTRAL**

On a **strict factor-model basis**, RVMD scores poorly: it fails Value (negative on every metric), Quality (F-Score 1/9, −69% ROE), and Low-Vol (66% vol). It passes **only** on revisions (long-dated) and momentum (concentrated). A mechanical 5-factor cross-sectional model would rank it **bottom-quintile ex-momentum → Neutral-at-best.**

However, factor models have **low explanatory power** for a binary pipeline name (R² 0.155). The offsetting evidence is real: analyst price targets cluster **$230–$318** (RBC $260, Goldman $267, Morgan Stanley $255 Overweight, Loop $318) = **+17% to +62%** vs $196.55, and revisions are up. Net: **Neutral from the factor engine; the bull case is catalyst/analyst-momentum, not factors.**

---

## 4. Key Quant Risk Flags

1. **⚠️ DATA-INTEGRITY FLAG (material):** The pipeline's momentum (+4.84%) and annualized-return (87.9%) figures **do not reconcile** with the raw adjusted-close series, which shows ~$40 (Sep-2025) → ~$197 (Oct-2026), a **~5× move**. The gains were *gap-driven*: +$40→+$120 in Jan-2026, and +$96→+$150 in Apr-2026. Treat all point estimates (alpha, Sharpe, drawdown, momentum) as **directionally indicative only** — the return distribution is non-normal with discrete event jumps, so regression-based stats are unreliable.

2. **Momentum reversal / event risk:** With 12-1 momentum only +4.84% against a ~5× absolute run, returns are **highly concentrated in a few gap days.** Substantial mean-reversion risk; a single pipeline disappointment (e.g., RMC-6236 trial data) could retrace a large share of the move.

3. **Cash burn & dilution:** Operating CF **−$898M (2025)** vs −$557M (2024), −$351M (2023) — accelerating burn. Cash & ST investments **$2.03B** → roughly **~2 years runway** at current pace; revenue inflection not modeled until FY2028. F-Score dilution component = 0 → **equity issuance likely**.

4. **Binary/idiosyncratic:** Correlations 0.24–0.39; R² 0.155. No meaningful index hedge — this is a single-asset clinical bet, not a beta exposure.

5. **Factor-model non-applicability:** Value/Quality/Low-Vol scores are mechanically negative and should **not** be read as relative attractiveness; they are an artifact of being pre-revenue. The F-Score of 1/9 carries almost no information beyond "no earnings."

6. **Revision dispersion:** FY2030 EPS estimates span $4.62–$27.82 across 8 analysts (6× range) — extremely wide, so the "upgrade" signal has **low statistical confidence**. (Small-sample caveat: 8–19 analysts, and far-dated estimates are thinly covered.)

**Bottom line:** Strong **event-driven / analyst-momentum** name with genuine alpha vs biotech (R²-adjusted caveats apply), but it is **not a factor-investable stock** — Value, Quality, and Low-Vol are disqualifying, and the positive signals (revisions, momentum, price targets) are all **long-dated and gap-concentrated**. Net quant read: **Neutral (factor model) / speculative Buy (catalyst premise)** — position for the binary, size for 66% vol and a ~2-year cash runway.
