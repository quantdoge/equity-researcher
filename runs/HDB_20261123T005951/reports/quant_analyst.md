# Quant Analyst

- Symbol: HDB
- Elapsed: 84.7s

---
## HDB (HDFC Bank Ltd. — ADR) — Quantitative Factor Report

### ⚠️ Data integrity warning (read first)

The factor/valuation tools return **materially corrupted multiples**. Evidence:

| Metric | Tool output | Reality check |
|---|---|---|
| P/E | 0.19 | Implies ₹0.19 per ₹1 of earnings — impossible |
| P/B | 0.02 | Book value/share reported at **₹1,159.71** (INR) divided by a **USD $27.42** price |
| EV/EBITDA | 2.56 | EV ₹2.85tn vs USD market cap |
| Div yield | 6.38% | HDB pays ~1.0–1.2% |

**Cause:** INR-denominated fundamentals ÷ USD ADR price, plus an inconsistent share count (5.14bn "diluted shares" vs ~15.3bn actual post-1:1-bonus float). Second, the tools' "current price" of **$27.42 does not exist in the live tape** — verified OHLC shows HDB at **$31.97 on 2026-02-20**. The factor engines are running a stale (~Jan-2025) vintage. **All tool-derived returns/alphas below are therefore on a different window than the verified series, and I report both.**

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | Invalid as computed (P/E 0.19, P/B 0.02). Analyst-derived: **~19x FY26E P/E, ~2.9x P/B, ~1.1% yield** | N/A — no valid peer set* | **Neutral** (in line with IBN) |
| **Momentum** | Tool 12-1: **−4.4%**. Verified 12-1: **+11.1%**; 6M: **−11.7%** | 2 of 2 vs IBN (−0.07%) | **Neutral / deteriorating** |
| **Quality** | ROE **13.41%**, ROA **1.66%**, ROIC 9.16%, accruals **−2.0%** (good), F-Score **6/9** | 2 of 2 vs IBN (ROE 14.28%) | **Moderate** |
| **Low Vol** | Vol **33.2%** (1y), **27.7%** (2y); beta **0.66** but R²=0.09 | 2 of 2 vs IBN (23.3% vol) | **Weak** (high absolute vol) |
| **Earnings Revision** | **+20.6%** flagged "upgrade" — not credible | n=1 analyst | **Insufficient data** |

\* `get_sector_peers` returned only ETFs/funds (VTI, VFIAX…), no bank comparables. IBN is the sole usable comp (same INR-fundamentals/USD-price distortion, so relative ranking is still valid). **N=1 peer is not statistically meaningful.**

**Revision score is an artifact, not a signal:** the tool compares FY2030 EPS of ₹260.68 against a "prior" of ₹216.09 — which is *identical to the current FY2029 estimate*. It rolled the forecast window forward one year rather than revising the same period. The implied growth curve (FY26→27 +9.3%, →28 +16.3%, →29 +15.7%, →30 +20.6%) is smooth and mechanically backward-fitted. **One analyst covers FY2030.** No genuine revision momentum can be inferred.

### 2. Price Statistics

**Tool-computed (stale vintage):**

| Window | Ann. Return | Ann. Vol | Sharpe | Sortino | Max DD | Beta | Alpha (vs SPY) | R² |
|---|---|---|---|---|---|---|---|---|
| 252d | −11.45% | 33.44% | **−0.343** | **−0.489** | −33.71% | 0.656 | **−15.71%** | 0.090 |
| 504d | −12.61% | 27.72% | **−0.455** | **−0.629** | — | 0.518 | **−20.48%** | 0.063 |

**Verified from raw OHLC (2024-01-02 → 2026-02-20):**

| Metric | Value |
|---|---|
| Price (2026-02-20) | $31.97 |
| 1-year price return | **+14.4%** (~+15.4% total w/ dividend) |
| 12-1 momentum | **+11.1%** |
| 6-month return | **−11.7%** |
| 2-year price return | +4.8% (~2.2%/yr — severe EM underperformance) |
| 52-wk range | **$30.98 – $37.67**; now 3.2% off the low, 15.1% off the high |
| 1-yr max drawdown (close basis) | **−17.8%** (Jul-25 $37.67 → Jan-26 $30.98) |
| 2-yr max drawdown | **−21.4%** (Jan–Feb 2024) |

**The −33.71% max drawdown is not reproducible** on the verified series (true 1-yr DD −17.8%). Treat the tool's risk statistics as unreliable in level, though the *direction* (negative risk-adjusted returns, vol well above peer) holds.

**Correlations (252d):** IBN **0.66** · KBE 0.37 · SPY **0.30**

### 3. Statistical Significance

- **Alpha is "significant" but not meaningful.** SE(β) ≈ 0.13; SE(α) ≈ 2.0pp → t ≈ −7.8. However **R² of 0.09 means 91% of HDB's variance is unexplained by SPY.** SPY is the wrong benchmark for an Indian bank ADR (correlation 0.30 vs 0.66 to IBN). Much of the reported "alpha" is INR depreciation (~−3–5%/yr), EM equity de-rating and foreign-flow reversal — benchmark error, not manager-relevant skill shortfall. Re-run against INDA/FINX before trusting any alpha figure.
- **Sharpe/Sortino assume rf = 0%.** At a ~4.3% T-bill rate, true Sharpe falls another ~0.13 → roughly **−0.47 (1y)**. Reported Sortino (−0.489) is *worse* than Sharpe, meaning downside deviation exceeds total deviation — a left-tail-skewed return distribution.
- n = 252/504 is adequate for volatility and beta; **n = 1 analyst and n = 1 peer are not.** No claim on revisions or relative ranking survives significance testing.

### 4. Composite Quant Signal: **NEUTRAL** (bias negative)

Roughly 4.5/10. Quality is real (ROE 13.4% recovering from the merger-diluted 7.8–7.9% in FY24–25, negative accruals, F-Score 6) but sits *below* its own pre-merger history (ROE 17.0% FY23) and *below* IBN. Value is fair, not cheap. Momentum has flipped negative over 6M with price pressed against the 52-week low. On the tools' stale vintage this screens **Sell**; on verified data it screens **Neutral**. I weight the verified series.

### 5. Key Quant Risk Flags

1. **Momentum reversal risk — ACTIVE.** −11.7% over 6M, within 3.2% of the 52-week low, and a −12% gap-down in Jan-2026. Classic negative-momentum regime.
2. **Benchmark/factor-model risk — HIGH.** R² = 0.06–0.09 vs SPY. Any market-model risk decomposition (beta, alpha, tracking error) built on SPY for this name is misspecified.
3. **Dividend/ADR basis risk.** Two-year USD return (+4.8%) vs what local INR shareholders experienced differs by cumulative INR depreciation; ADR pricing carries FX plus a persistent liquidity discount.
4. **Factor crowding — untestable here.** No valid bank peer set was returned, so I cannot assess crowding in Indian financials. Do not treat the momentum/value scores as cross-sectionally z-scored.
5. **Liquidity — moderate.** ADR volume ~3–8mn shares/day typical, with 10–30mn spikes on earnings; adequate but thin versus US large-caps, and gap risk around quarterly results is visible in the tape (Jan-17-2024: −9.1% in one session).
6. **Estimate coverage thin (1–2 analysts on out-years).** Consensus is not robust; single-analyst revisions should never be traded as signal.

### Gaps (not obtainable in budget)
- Price targets returned no data.
- No usable sector peer multiples — value/quality ranks are 2-way, not quintile.
- FY2026 is the latest annual actual (Indian FY ends March); the "2026-03-31" balance-sheet figures used by the quality tools are partially forecast-derived.

**Recommendation for the memo:** Do not use the tool-reported P/E, P/B, EV/EBITDA, dividend yield, Sharpe, alpha, or max drawdown. Use the verified OHLC statistics and the quality/Piotroski outputs only. Re-run value and alpha against an Indian-financials or EM benchmark before this name is ranked in any factor portfolio.
