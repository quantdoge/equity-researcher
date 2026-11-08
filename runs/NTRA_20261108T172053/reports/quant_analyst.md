# Quant Analyst

- Symbol: NTRA
- Elapsed: 60.0s

---
# NTRA (Natera, Inc.) — Quantitative Factor Report

**Sector:** Healthcare / Medical – Diagnostics & Research · **Price:** $310.67 · **Mkt cap:** $44.8B (≈$42.5B on 136.7M diluted shares) · **Report date:** 2026-11-06 close

**Peer cohort:** The `sector_peers` API returns broad Healthcare (mostly large-cap pharma: LLY, JNJ, ABBV, MRK…), which is not a valid factor benchmark for a molecular-diagnostics company. I therefore hand-built a **6-name diagnostics cohort {NTRA, ILMN, TMO, GH, TXG, EXAS}**. This is a small, hand-constructed sample — **n=6 means one rank ≈ 17 percentile points**, so treat ranks as coarse terciles, not precise quintiles.

---

## 1. Factor Scores Table

| Factor | Score (−2 to +2) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **−2.0** | 3 of 6 cohort, but **bottom decile absolute** | **Strongly Bearish** |
| **Momentum (12-1)** | **+1.5** | **2 of 6** (top tercile) | **Bullish — but fragile** |
| **Quality** | **−0.5** | 4 of 6 | Neutral / mild Bearish |
| **Low Volatility** | **−1.5** | **4 of 4 valid — last** | **Bearish** |
| **Earnings Revision** | **+1.0** | n/a (6-analyst coverage) | Bullish, **low confidence** |

**Value detail.** P/E −204.4, EV/EBITDA −188.7, P/FCF 389.3, P/B 24.81 (BVPS $12.52), dividend: none. EV ≈ $41.6B ⇒ **EV/Sales 14.3x FY26E, 11.8x FY27E**. The "3 of 6" cohort rank is an artifact — NTRA only ranks mid-pack because GH, TXG and EXAS are *also* loss-making (GH has negative P/FCF and EV/EBITDA; EXAS returns nulls). On an absolute screen against profitable companies, NTRA is unrankable. Only ILMN (P/E 39.1, EV/EBITDA 23.5, P/FCF 35.7) and TMO (39.2 / 25.4 / 41.6) are genuinely cheap relative to earnings in this cohort.

**Quality detail.** Mixed with a real positive core: **gross profit/assets 0.596 — highest in the cohort** (vs ILMN 0.435, TXG 0.426, EXAS 0.386, GH 0.314, TMO 0.165) and **accruals ratio −0.169 — best in cohort**, i.e. operating cash flow *exceeds* net income by a wide margin (OCF +$215.3M vs net income −$208.2M in FY25). But ROE −12.2% / ROA −8.3% / ROIC −16.1%. The tool labels quality "low" on the ROE leg; two of three legs are top-quartile. **Piotroski F-Score 5/9 (Moderate)** — passes positive OCF, ROA improvement, accruals quality, positive equity change, gross-margin improvement; **fails F5 (leverage up), F7 (share count increased = dilution), F1 and F9.** Trajectory is genuinely improving: ROE −77.6% → −56.8% → −15.9% → −12.2% (FY22→FY25).

**Momentum detail.** 12-1 return **+48.6%** (6-month +22.3%). Cohort: TXG +63.2%, **NTRA +48.6%**, ILMN +35.6%, TMO +14.2%, GH +9.9%, EXAS n/a (insufficient history).

**Low-vol detail.** 56.8% annualised vol, beta 1.43 (profile β 1.534) — **highest vol and highest beta of the four names with valid data** (GH 55.9%/1.375; ILMN 52.1%/1.073; TMO 31.8%/0.627).

**Earnings revision detail — important caveat.** Tool reports **+70.2%** (current FY2030E EPS $3.647 vs prior $2.143). **The "prior" figure of $2.143 is exactly the current FY2029 consensus**, which strongly suggests the tool compared *adjacent fiscal years* rather than the same period 3 months ago. I treat this as a probable **fiscal-year alignment artifact, not a genuine revision.** Independent evidence is nonetheless constructive: revenue consensus $2.24B (FY25) → $2.91B (FY26E, +29.7%) → $3.52B → $4.26B → $5.13B → $6.19B (FY30E) — a consistent ~20-30% growth ladder with EBITDA crossing positive in FY28 (~$263M) from −$137M in FY26E. **Coverage is thin: only 6 analysts for FY2030E** (8-15 for nearer years).

---

## 2. Price Statistics

| Metric | 252d | 504d |
|---|---|---|
| Annualised return | **67.62%** | 57.35% |
| Annualised volatility | 56.01% | 47.73% |
| **Sharpe (0% RF)** | **1.207** | 1.202 |
| Sharpe @ 4% RF (my adjustment) | ~1.14 | ~1.12 |
| **Sortino** | **1.753** | 1.700 |
| **Alpha (ann., vs SPY)** | **+40.09%** | — |
| **Beta** | **1.44** | — |
| **R²** | **0.129** | — |
| **Max drawdown** | **−28.75%** | — |

**Alpha is not statistically significant.** With R² = 0.129, residual volatility = 56.01% × √(1−0.129) = **52.3% ann.**, ≈15.1%/month. Monthly alpha = 40.09/12 = 3.34%, so **t(α) ≈ 0.22 monthly ≈ 0.8 annualised** — well short of significance. **87% of NTRA's variance is idiosyncratic; the "alpha" is not distinguishable from noise.**

**The max drawdown is live, not historical.** The −28.75% figure is the *current* drawdown: peak close **$436.19 (2026-10-29) → $310.67**, i.e. **−28.8% in six sessions**, and the stock is sitting at the bottom of that range. Trailing-year closing low $186.36 (2026-05-15); price sits at the **50th percentile** of its 52-week range. Down −28.8% from high, +66.7% off the low.

**Event signature:** 2026-11-06 gapped from $363.76 to a $319.99 open and closed **$310.67 (−14
