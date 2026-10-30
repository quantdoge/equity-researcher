# Quant Analyst

- Symbol: HLN
- Elapsed: 35.0s

---
## HLN (Haleon plc) — Quantitative Factor Report

*Price $8.57 · Mkt cap $37.7bn · Healthcare / Consumer Health · FY end 2025-12-31*

### 1. Factor Scores

| Factor | Score (0–10) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 5.0 | 3rd of 6 (~50th pct) | Neutral — cheap on P/B & FCF, rich on EBITDA |
| **Momentum** | 1.5 | 6th of 6 (worst) | **Strongly Negative** |
| **Quality** | 6.0 | 3rd–4th of 6 | Mild Positive — improving trend |
| **Low Vol** | 2.0 | 5th of 6 | Negative — high vol, beta anomalous |
| **Earnings Revision** | 5.0 | n/a (n too small) | Flat / unmeasurable |

**Value detail** (HLN vs 6-name consumer-health & large-pharma peer set):

| Metric | HLN | Peer median (ex-HLN) | Rank |
|---|---|---|---|
| P/E | 23.81 | 24.95 | 3/6 |
| P/B (derived*) | ~2.3 | 6.77 | 1/6 (cheapest) |
| EV/EBITDA | 15.94 | 15.16 | 5/6 (expensive) |
| P/FCF | 19.59 | 29.68 | 2/6 (cheap) |

*Derived: NI $1.630bn / ROE 9.91% → equity ≈ $16.4bn → BVPS ≈ $3.74. Direct P/B feed unavailable.

**Quality detail:** ROE 9.91%, ROA 5.01%, ROIC 9.63%, gross profit/assets 0.2145 (below the tool's "high quality" threshold), accruals ratio **−0.0201** (negative accruals = high earnings quality, consistent 2022–25). **Piotroski F-Score 9/9 — perfect**, all nine components positive. ROIC has risen monotonically: 6.79% → 7.62% → 8.38% → 9.63% (FY22→FY25). The "low quality" label is driven purely by the low GP/A, which reflects a goodwill-heavy post-demerger balance sheet, not operating weakness.

**Momentum detail:** 12-1 month return **−10.93%**; 6-month **−14.26%**. Deteriorating at both horizons — no sign of stabilization.

### 2. Price Statistics (252 trading days, vs SPY)

| Statistic | Value |
|---|---|
| Annualised return | **−22.93%** |
| Annualised volatility | 28.94% (29.36% alt. convention) |
| **Alpha (annualised)** | **−16.76%** (1y) / −8.30% (2y) |
| **Beta** | **−0.07** (1y) / −0.045 (2y) |
| R² vs SPY | 0.001 |
| **Sharpe ratio** | **−0.781** (−0.62 alt.) |
| **Sortino ratio** | **−0.91** |
| Max drawdown | −23.48% |

Correlations (1y): KVUE 0.42, AZN 0.32, JNJ 0.28, MRK 0.19 — all low relative to peer-pair norms (JNJ–AZN 0.52), confirming genuine idiosyncratic/diversifying behavior.

### 3. Composite Quant Signal: **NEUTRAL (leaning negative)**

Buy-side support: perfect F-score, negative accruals, record ROIC, cheap on book/FCF, deeply uncorrelated to market. Sell-side weight: negative and worsening momentum, high realized vol, and negative alpha on both windows. Factor scores are internally offsetting — no multi-factor confluence in either direction. This is not a top-quintile value+momentum+quality name; it fails momentum outright.

### 4. Key Quant Risk Flags

- **⚠️ Beta estimate is unreliable.** Beta of −0.07 with R² = 0.001 means SPY explains ~0.1% of HLN variance. The negative beta is a statistical artifact (GBP/USD translation, UK domicile, low sector correlation), **not** a hedge. Do not use this beta in CAPM or for hedging. Company-reported beta is 0.245.
- **⚠️ Momentum reversal risk is low; momentum *persistence* risk is high.** −10.9% 12-1 and −14.3% 6m with no inflection. Trend-following overlays will remain short.
- **⚠️ Earnings-revision score is invalid.** The tool compared the FY2030 estimate ($0.51785, n=2 analysts) against the FY2029 prior ($0.51632) — a period mismatch. Coverage is thin (2–3 analysts for 2029-30, 5 for 2026-27). Treat revision signal as **no information**. Best proxy is the consensus EPS curve, which decelerates: 2026 $0.421 (+8.7% to) 2027 $0.458 (+8.1%) 2028 $0.494 (+4.5%) 2029 $0.516 (+0.3%) 2030 $0.518. Forward P/E on FY26 = ~20.4x.
- **⚠️ Volatility is high for a staples-like name.** 28.9% annualised and −23.5% max drawdown are pharma-like, not consumer-health-like; this will screen poorly on any low-vol/l min-variance construction.
- **Small sample / small peer set.** Sector rank uses n=6 hand-curated comps. The feed's Healthcare peer list is dominated by big pharma (LLY, JNJ, ABBV) — not true consumer-health comparables. **KVUE is the only close analogue** (P/E 25.74, P/B 3.49, EV/EBITDA 15.36, P/FCF 21.85, yield 4.27%); HLN is cheaper on P/B and P/FCF but marginally more expensive on EV/EBITDA.
- **Data gaps:** dividend yield for HLN not returned by the valuation-ratio feed; direct P/B unavailable (derived). No FY2026+ guidance revisions available to test the revision factor properly.

**Bottom line:** A cheap-on-cash-flow, high-quality-earnings compounder in a confirmed downtrend. Quantitatives argue for patience, not accumulation, until momentum inflects — the F-score 9/9 and negative accruals are the only statistically robust positives in the dataset.
