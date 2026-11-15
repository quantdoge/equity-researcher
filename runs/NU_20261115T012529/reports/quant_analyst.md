# Quant Analyst

- Symbol: NU
- Elapsed: 81.9s

---
# NU (Nu Holdings) — Quantitative Factor Scorecard

**Latest close: $13.22 | Market cap ~$64.9bn | Sector: Financial Services / Banks–Regional (Brazil) | 5,720 P/B, 22.8x trailing P/E**

Note on peer set: `get_sector_peers` returned only index funds/ETFs (VSMPX, VTSAX, VTI…), which are not valid comparables. I built an explicit proxy peer set of **ITUB** (closest LatAm comp), **JPM** (US bank benchmark), **C** (global bank), **SOFI** (digital fintech). All sector ranks below are against n=5 names — a very coarse percentile, so ranks are ordinal only.

---

## 1. Factor Scores Table

| Factor | Raw Score | Sector Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | P/E 22.8x, P/B 5.72x, EV/EBITDA 13.6x, P/FCF 18.6x | **4.3 avg → 5th** | **Expensive / bottom quintile** |
| **Momentum** | +3.12% (12-1m) | **2nd** | Mild positive |
| **Quality** | ROE 25.3%, GP/assets 9.51%, accruals −0.84% | **1st** | **Top quintile (relative)** |
| **Low Vol** | Vol 50.5%, beta 1.33, max DD −34.0% | **4th** | **Poor / high-vol** |
| **Earnings Revision** | +28.0% (see caveat) | **2nd** | Upgrade — *but artifact* |

**Value detail (lower = better):** P/E — ITUB 1.9, JPM 17.3, C 17.7, **NU 22.8**, SOFI 39.5. EV/EBITDA — JPM 5.2, C 11.2, ITUB 11.6, **NU 13.6**, SOFI 18.3. P/FCF — ITUB 0.7, then JPM/C/SOFI all **negative** (n/m), **NU 18.6**. NU is 4th or 5th on all three legs; only ITUB and NU generate positive FCF, and NU's FCF yield (~5.4%) is far thinner. **Verdict: unambiguously the most expensive name in the set.**

**Quality detail:** ROE 25.3% (best; ITUB 20.9, JPM 15.7, C 6.7, SOFI 4.6); GP/assets 9.51% (best; ITUB 4.31, SOFI 7.07, JPM 3.79, C 2.82); accruals −0.84% (2nd best; ITUB −2.75, JPM +4.63, C +3.08, SOFI +8.34). **Verdict: best profitability and cleanest accruals in the peer set.** But the tool's absolute-threshold `quality_signal` reads **"low"** — its cutoffs are calibrated for non-financials where 9.5% GP/assets is weak. Both readings are true: top-quartile *relative* to banks, unremarkable *absolute* on a cross-industry scale. Supporting evidence for caution: **Piotroski F-Score 4/9 ("Weak")** — profitability legs pass (positive ROA, positive OCF, good accruals) but ROA *deteriorated* (3.95%→3.83%), leverage did not fall, asset turnover did not improve, and **share count rose** (F7 = 0, dilution).

**Momentum detail:** NU +3.12% vs ITUB +15.54%, JPM −4.18%, C −7.15%, SOFI −19.61%. Positive in absolute terms and 2nd in the group, but the group is weak — this is relative strength in a soft cohort, not strong momentum.

**Low-vol detail:** vol 50.5% (2nd highest; SOFI 54.0, ITUB 44.3, C 30.0, JPM 21.7); beta 1.33 (2nd highest; SOFI 2.22, C 1.26, ITUB 1.05, JPM 0.71). Sharpe of −0.45 vs JPM +0.62 — NU is the *opposite* of a low-vol name.

---

## 2. Price Statistics (252 trading days, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **−19.06%** |
| Annualised volatility | 50.5% (51.2% per Sharpe calc) |
| **Alpha (annualised)** | **−40.83%** |
| **Beta** | **1.334** (R² = 0.141) |
| Sharpe | **−0.372** |
| Sortino | **−0.505** |
| Max drawdown | **−33.98%** |

**Critical statistical flag — the alpha is not significant.** R² of 0.141 means only 14% of NU's variance is explained by the market; 86% is idiosyncratic. Residual vol ≈ 51.2% × √0.859 ≈ **47.5%**, so the standard error on the annualised alpha is on the order of **~47pp**, giving **t ≈ −0.9 (p ≈ 0.4)**. The −40.8% alpha is directionally damning but statistically indistinguishable from zero on one year of daily data. **Do not cite it as a precise estimate.** Same caveat applies to the Sharpe/Sortino — 252 observations is a thin sample for a 51%-vol stock.

Beta also conflicts by window: 1.33 (1y daily, regression) vs 0.968 (company profile, 5y monthly). Treat 1.1–1.3 as the working range; either way NU is a **high-beta, high-vol, negative-Sharpe** name.

Sortino (−0.505) is worse than Sharpe (−0.372), meaning **downside deviation exceeds total deviation** — losses are large and clustered, not symmetric. That is the most important line in this table.

---

## 3. Composite Quant Signal

**NEUTRAL** (composite 3.1 / 5.0 on a 1–5 percentile scale)

| Weight | Factor | Score | Contribution |
|---|---|---|---|
| 25% | Value | 1.5 | 0.38 |
| 25% | Quality | 4.0 | 1.00 |
| 20% | Momentum | 4.0 | 0.80 |
| 15% | Low Vol | 2.0 | 0.30 |
| 15% | Revision | 4.0 | 0.60 |
| | **Total** | | **3.08** |

**Rationale:** The quality/growth case is genuinely strong — 25.3% ROE, negative accruals, revenue CAGR of **52%** (2022 $4.52bn → 2025 $15.88bn), net income swinging from −$365m to +$2.87bn. But the quant screen cannot upgrade past Neutral because three independent legs are negative: **bottom-quintile valuation**, **4th-of-5 on volatility**, and **negative realized alpha/Sharpe**. A stock scoring top-quintile on quality while bottom-quintile on value and low-vol is a *growth-at-a-reasonable-price* debate, not a factor-driven buy. Price is 13.22 against 2026E EPS of $0.865 (**15.3x forward**, 12.0x on 2027E $1.10, 9.5x on 2028E $1.39) — the forward multiple is defensible, but the trailing 22.8x and 5.7x book require the growth to persist.

---

## 4. Key Quant Risk Flags

1. **⚠️ Earnings-revision signal is a data artifact — do not trade on it.** The tool reports "forward_period 2029-12-31, current 1.7819 vs prior 1.39167, +28.0%." But 1.39167 is *exactly* the 2028 consensus estimate. The "revision" is comparing **2029E against 2028E**, i.e. implied two-year EPS growth, not a 3-month same-period revision. The same defect appears in every peer (JPM 2028 vs prior, C 2030 vs prior, SOFI 2029 vs prior) — periods are inconsistent across names, so even the 2nd-of-5 rank is apples-to-oranges. **Genuine 3-month revision history is unavailable in this dataset.** Corroborating evidence that these long-dated estimates are low quality: the 2029 revenue estimate ($30.9bn) is *below* 2028 ($34.5bn) while EPS rises — internally inconsistent.
2. **Momentum reversal risk (high).** 12-1 momentum is +3.1%, but the 21-day exclusion means recent action is excluded. Every one of the six price targets was set at a *higher* spot than today's $13.22 ($13.59–$15.16), i.e. the stock has drifted down through the period when analysts were publishing $17–20.50 targets. A positive 12-1 reading sitting on a weakening recent tape is the classic reversal setup. Median target ~$19.0 implies ~+44% upside — but targets have been falling *with* the price (Wolfe cut 18→17), so the gap is not being closed by upgrades.
3. **Factor crowding / concentration — moderate.** NU's correlation with ITUB is **0.73**, but only 0.29 with JPM, 0.38 with SOFI, 0.33 with C. NU is a Brazil-macro proxy masquerading as a fintech: it is *not* diversifying within "Financial Services," and a Brazil/BRL or LatAm-rate shock hits it and ITUB together. The 0.73 ITUB correlation is the crowding risk that matters.
4. **Liquidity — not a concern.** $64.9bn market cap, 4.91bn diluted shares; no illiquidity discount applies. Sample size is the binding constraint, not float.
5. **Dilution.** Diluted shares 4.907bn vs 4.833bn weighted average — Piotroski F7 = 0. Modest, but it caps per-share compounding.
6. **Estimate-count thinness.** Revenue estimates rest on only **3–7 analysts** per period (3 for 2026, 4 for 2029) vs 10–13 on EPS. Revenue-side consensus is fragile; treat revenue-surprise-based signals as low-confidence.

**Bottom line:** Quality is real and top-of-class; valuation is bottom-of-class; momentum is positive but fragile; risk-adjusted realized performance is negative and statistically weak. **Neutral — no factor-driven edge.** The bull case rests on forward growth delivery (15x 2026E, 52% historical revenue CAGR), not on any signal this screen can validate.
