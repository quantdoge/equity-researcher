# Quant Analyst

- Symbol: FSLR
- Elapsed: 42.6s

---
## FSLR — Quantitative Factor Report
*Price reference: $241.88 (OHLC 2026-02-20 close). Market cap ≈ $26.0B on 107.5M diluted shares.*

**Data-integrity flags up front (material):**
1. `calculate_valuation_ratios` / `calculate_value_factor_score` returned a price of **$191.61** (mcap $20.6B), which conflicts with the OHLC series ($241.88 last, $220–$286 range over the window). I use the multiples as ratios (unaffected) but recompute price-dependent figures off $241.88.
2. The earnings-revision tool's "prior 3-months-ago" estimate for FY2030 (**$33.738**) is *identical* to the current FY2029 consensus. This looks like a period-mapping error. Treat the −8.45% as **directionally indicative, not precise**.
3. Price targets are dated Oct–Nov **2026**, i.e. later than the price history endpoint — another feed inconsistency. Targets are reported, not relied upon.

---

### 1. Factor Scores

| Factor | Score / Raw Input | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E 13.5x; EV/EBITDA 8.5x; P/FCF 17.4x (FCF yield 5.8%) | **2 of 5** (1 of 4 on positive-FCF basis) | **Positive** |
| **Momentum** (12-1) | **−14.84%** | **2 of 5** (least-bad of a uniformly negative group) | **Negative** |
| **Quality** | ROE 16.0%; ROIC 15.9%; GP/Assets 0.159; Accruals **−0.040**; F-Score **7/9** | **2 of 5** | **Neutral-Positive** |
| **Low Vol** | σ 52.8%; β 1.431; Max DD **−47.2%** | n/a (peer vols not retrieved — *gap*) | **Strongly Negative** |
| **Earnings Revision** | −8.45% (suspect, see flag #2) | n/a | **Negative** |

\*Peer set = FSLR, ENPH, NXT, RUN, ARRY. **n = 5 — ranks are ordinal only, not statistically robust.** The tool's "sector" (Energy: XOM, CVX, SHEL…) is an oil-major classification and is *not* a valid comparable set for a CdTe module manufacturer; I substituted solar specialists.

**Peer detail (the basis for ranks):**

| | P/E | EV/EBITDA | P/FCF | ROE | GP/Assets | Accruals | 12-1 Mom |
|---|---|---|---|---|---|---|---|
| **FSLR** | **13.5** | **8.5** | **17.4** | 16.0% | 0.159 | **−0.040** | −14.8% |
| NXT | 27.3 | 20.1 | 31.3 | **25.1%** | **0.285** | 0.007 | **−5.6%** |
| ENPH | 22.5 | 15.9 | 40.9 | 15.8% | 0.196 | 0.010 | −16.1% |
| RUN | 5.7 | 8.3 | n.m. (−6.2) | 9.0% | 0.033 | 0.036 | −22.6% |
| ARRY | n.m. | 28.9 | 9.9 | −20.1% | 0.206 | −0.106 | −31.0% |

FSLR is the **cheapest profitable name in the group on every multiple**, and the only one with a negative accruals ratio (−0.040 → cash earnings exceed book earnings, the single best quality marker here). It loses to NXT on ROE and gross-profitability, hence rank 2, not 1.

**Revision curve concern (independent of flag #2):** consensus EPS runs $23.09 (FY27) → $27.79 (FY28) → $33.74 (FY29) → **$30.89 (FY30)**. The implied **decline in FY2030 earnings** is the notable signal — the sell-side is already discounting a post-incentive margin step-down. FY2028 dispersion is extreme ($18.91–$34.58, ±28% around the mean, 28 analysts): **the forecast distribution is not tight enough to support a high-conviction valuation call.** Price-target median $257 vs $241.88 = **+6.3% upside** (range $199–$328).

---

### 2. Price Statistics (252 trading days)

| Metric | Value | Significance |
|---|---|---|
| Annualised return | **−9.22%** | — |
| Alpha (vs SPY, annualised) | **−27.77%** | t ≈ **−0.57** → **NOT significant** |
| Beta (OLS, vs SPY) | **1.431–1.438** | SE ≈ 0.19, t ≈ 7.5 → **highly significant** |
| R² vs SPY | **0.154** | **85% of variance is idiosyncratic** |
| Annualised volatility | **52.83%** (~3.3x SPY) | — |
| Sharpe (rf = 0%) | **−0.174** | t ≈ −0.17 → not significant |
| Sortino | **−0.259** | downside dev > total vol |
| Max drawdown | **−47.16%** | — |

**Interpretation:** The −27.8% alpha is large but carries a ±48.6% standard error, so it cannot be distinguished from zero at any conventional level. What *is* statistically solid is the **beta of ~1.43** and the fact that **only 15% of FSLR's returns are explained by the market** — this is a stock-specific bet, not a market beta trade. Its low correlation to SPY (0.39) and moderate correlation to solar peers (NXT 0.53, ENPH 0.48) means sector diversification within clean energy is limited but market-hedging value is real.

Caveat: Sharpe/Sortino computed at a **0% risk-free rate**. At ~4% rf the Sharpe falls to roughly **−0.25**, and the Sortino to ~−0.37. Both are worse than reported.

**Realised drawdown check:** peak $285.99 (2025-12-22) → $218.73 (2026-02-06) = **−23.5%** in six weeks. Liquidity is not a concern: ~2.5M shares/day ≈ **$600M dollar volume**.

---

### 3. Composite Quant Signal

**NEUTRAL (Hold), with a negative tactical tilt.**

| Factor | Signal | Weight rationale |
|---|---|---|
| Value | + | Genuine and broad-based across 3 multiples |
| Quality | ~+ | Franchise-grade accruals, F-Score 7; short of top on ROE |
| Momentum | − | Negative 12-1, and momentum empirically persists |
| Revision | − | Downgrade, plus FY30 EPS *below* FY29 |
| Low Vol | − | 52.8% vol, β 1.43, −47% MDD |
| Alpha | ~0 | Economically large, statistically indistinguishable from zero |

The classic value-plus-quality combination is present and is the entire bull case; it is offset by **negative momentum and negative revisions simultaneously** — the pairing that historically produces value traps. Value cannot be upgraded beyond rank-2-of-5 on an n=5 sample. I will not issue Buy on a sample this small with two factors pointing the wrong way.

---

### 4. Key Quant Risk Flags

1. **Momentum-reversal / value-trap risk (highest).** −14.8% 12-1 momentum *with* −8.5% earnings revisions is the canonical value-trap signature. Cheapness is not a catalyst.
2. **Sample-size insufficiency.** Peer n = 5; single-year regression window; 12-1 momentum from one lookback. Cross-sectional ranks have no meaningful confidence interval. Factor z-scores across a true solar universe (≥15 names) are required before any sizing decision.
3. **Latent policy/idiosyncratic risk.** R² = 0.154 means FSLR is effectively a policy-and-tariff derivative. Alpha's standard error (±48.6%) exceeds the return itself. No quant model here can price IRA credit step-downs — the FY2030 EPS dip is the market's proxy for exactly that.
4. **Factor crowding.** Solar is a crowded, retail-heavy thematic; the uniform negative momentum across all five names (FSLR, ENPH, NXT, RUN, ARRY) indicates **sector-wide de-risking, not stock-specific mispricing**. Diversifying within the theme will not help.
5. **Forecast dispersion.** FY28 EPS $18.91–$34.58. Any DCF or multiple-based target is dominated by assumption choice, not data.
6. **Data quality.** Price conflict ($191.61 vs $241.88), future-dated price targets, and a revision figure whose comparator matches the wrong fiscal year. All multiples should be re-run on a single consistent price before execution.

**Bottom line:** statistically defensible statements are limited to *"FSLR is 1.4-beta, ~53%-vol, 85% idiosyncratic, cheap versus solar peers, with negative momentum and negative revisions."* Directionally that argues for a small, volatility-scaled position at most — not a quant Buy.
