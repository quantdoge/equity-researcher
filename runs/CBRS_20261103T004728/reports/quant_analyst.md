# Quant Analyst

- Symbol: CBRS
- Elapsed: 27.1s

---
## CBRS — Cerebras Systems Inc. | Quantitative Factor Report
*Pricing date: 2026-11-02 | Price $96.36 | Mkt cap $21.83B | Sector: Technology / Semiconductors*

> **⚠️ CRITICAL DATA-QUALITY FLAG — read before the tables.** CBRS IPO'd **2026-05-14**; the full price history spans only ~120 trading days (≈5.5 months, through 2026-11-02). The factor/risk tools label their window "252 days," but **no `<1yr` annualization is statistically meaningful**. The −186% "annualized return," −195% "alpha," and 113% "annualized vol" are all artifacts of annualizing a short, violent post-IPO decay. **Treat all annualized/régression statistics as directionally indicative only, not as estimates of forward distribution.** Additionally, the config's `beta` field (1.85) disagrees with the regression beta (3.06) — I report both.

### 1. Factor Scores

| Factor | Raw Metric | Approx. Sector Rank | Signal |
|--------|-----------|---------------------|--------|
| **Value** | P/E 235.0, EV/EBITDA 71.2, P/FCF −52.8 (neg FCF) | Bottom quintile (worst ~5%) | **Strong Sell** |
| **Momentum** (12-1, really ~6-1) | −8.8% (ex-last-21d) | Bottom quintile vs strong semi cohort | **Sell** |
| **Quality** | ROE −41.1%, GP/Assets 8.6%, accruals 0.107 (high); F-Score 5 | Bottom quintile | **Sell** |
| **Low Vol** | Vol 113% ann., beta 3.0, max DD 69% | Bottom quintile (highest-risk) | **Strong Sell** |
| **Earnings Revision** | +542% to 2028E... **artifact** (see note) | n/a — unreliable | **Neutral (unusable)** |

**Earnings-revision caveat:** the "+542% upgrade" compares the 2028E consensus EPS of $7.97 against a "prior" value of $1.24 — but **$1.24 is literally the 2027E estimate**. This is a slot-migration artifact from a tiny analyst base (**n=4** for 2028 EPS, spread $4.55–$14.81 — an 8× range). Consensus already models FY26 EPS of **−$0.52** (loss) before a step-change to profit in FY27/28. **The revision signal cannot be trusted.**

### 2. Price Statistics (window ≈120 trading days — small sample)

| Metric | Value | Note |
|--------|-------|------|
| Alpha (ann., vs SPY) | **−195.8%** | Artifact; inflated by short-sample annualization |
| Beta (regression) | **3.06** | Config field says 1.85 — discrepancy noted |
| R² vs SPY | **0.112** | **89% idiosyncratic** — market explains almost nothing |
| Annualized vol | 112.96% | Extreme |
| Sharpe | **−1.653** | |
| Sortino | **−3.201** | Downside dev far exceeds total vol |
| Max drawdown | **69.0%** | IPO $311 → $96.36 = −69% |
| Cumulative return (since IPO) | **−69.0%** | Persistent lower-highs; no base formed |

**Statistical significance:** With R²≈0.11 and <120 observations, the OLS alpha/beta are not statistically reliable (huge standard errors). Beta of 3.0 should be read as "very high" not "3.06 ± precision."

### 3. Composite Quant Signal: **STRONG SELL**

Unambiguous bottom-quintile on **four of five** factors (value, momentum, quality, low-vol). The lone apparent positive (earnings revision) is a data artifact from a 4-analyst, 8×-spread estimate. Negative FCF, 235× trailing P/E, −41% ROE, high accruals (0.107), and a 69% post-IPO drawdown with 89% idiosyncratic risk. This is a high-beta, loss-making story stock in a maximum-uncertainty phase.

### 4. Key Quant Risk Flags

- **Momentum-reversal / falling-knife:** persistent lower-highs since IPO; no stabilization. Shorting into a high-beta name can snap violently (see +40% single-day moves within the series).
- **Factor crowding (inverse):** sits in the crowded *growth/AI-semis* trade while scoring worst on the factors that historically outperform — a de-rating risk if the AI-narrative cools.
- **Small-sample invalidity:** all annualized/regression stats underpowered (<1yr, n≈120, R² 0.11). Do **not** size on these numbers.
- **Estimate-fragility:** 4 analysts, 2028E EPS range $4.55–$14.81; a single downgrade swings consensus materially.
- **Data-integrity concerns:** ROIC (45.9%) contradicts ROE (−41%) and high accruals; prior-year ROA swings (−63%→+10%). Accounting/verification uncertain post-IPO.
- **Liquidity:** adequate (10–20M shares/day on active days) but volume is episodic and event-driven — slippage risk in size.
- **FCF-negative (P/FCF −52.8):** no valuation floor; entirely dependent on the 2027–28 profitability inflection the estimate base is too thin to validate.

**Bottom line for the memo:** No quantitative support for ownership at current levels. Any bull case rests on a 2027–28 earnings inflection that is *not* corroborated by a credible revision trend (four analysts, un-annualizable history). Flag to the fundamental team: **revisit once ≥2 quarters of post-IPO trading data and a stabilized estimate base exist.**
