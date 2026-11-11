# Quant Analyst

- Symbol: CHTR
- Elapsed: 27.6s

---
## CHTR (Charter Communications) — Quantitative Factor Report

**Critical data note first:** the price feed lags. OHLCV history ends 2026-04-15 (~$220), while all valuation tools report a **current price of $134.06**. Analyst-target records dated through **2026-11-09** (price when posted $118.81; $102.48 on 2026-10-13) bracket "now" at roughly late-2026. The stock has therefore fallen from ~$275 (Oct-2025) → ~$220 (Apr-2026) → trough ~$102 (Oct-2026) → $134 now. This reconciles the −75.6% 504-day drawdown, which is **not** visible in my truncated series. All price-derived statistics below are computed on the vendor's full (forward-extended) window and are internally consistent with that collapse.

### 1. Factor Scores

| Factor | Score | Sector Rank* | Signal |
|---|---|---|---|
| Value | P/E 3.7 · P/B 0.90 · EV/EBITDA 5.43 · P/FCF 4.18 | **1 / 4 (best)** | Strongly positive, but value-trap watch |
| Momentum | −25.8% (12-1, 252d) | **4 / 4 (worst)** | Negative |
| Quality | ROE 24.3% · GP/Assets 0.165 · Accruals −0.072 · ROIC 11.3% · F-score 7/9 | 2 / 4 | Neutral (tool flags "low" on GP/Assets) |
| Low Vol | Vol 51.3–59.0% · Beta 0.12 · Max DD 75.6% | **4 / 4 (worst)** | Strongly negative |
| Earnings Revision | 2026E $38.96 → 2027E $39.30 (flat); targets slashed | **4 / 4 (worst)** | Negative |

\*Ranked within the 4-name US telecom/cable comp set (CHTR, VZ, T, TMUS). The GICS "Communication Services" sector is dominated by GOOG/META/NFLX and is not a valid comp frame for a levered cable operator.

**Value detail (vs comps):** CHTR is the cheapest name on every metric — P/E 3.7 vs VZ 11.4 / T 7.2 / TMUS 17.4; EV/EBITDA 5.43 vs 7.51 / 5.73 / 9.83; P/FCF 4.18 vs 9.96 / 8.1 / 12.4; P/B 0.90 vs 1.85 / 1.23 / 3.23. Z-score vs peers is roughly −2σ on P/E. **Discount is not free:** revenue fell 0.6% Y/Y ($55.09B → $54.77B), diluted EPS $36.21 vs $34.97, net debt ≈ **$96.6B** (EV $115.1B − mkt cap $18.5B = **4.5x EBITDA**) against $5.04B of interest expense. Book equity of $148.96/sh sits above the $134 price — the market is pricing asset impairment risk, not just earnings compression.

**Revision detail — DATA ARTIFACT FLAGGED:** the `calculate_earnings_revision_score` output (+73.75%, "upgrade") is **spurious**. It compared the 2029E estimate ($53.59) against the 2030E estimate ($93.11, only 2 analysts) — different fiscal periods, not a same-period restatement. Discard it. The genuine revision signal is unambiguously negative: UBS $235→$140, Deutsche Bank $215→$150, Wells Fargo $160→$101, Bernstein $150→$120, Wolfe cut to **Underperform**. 2027E consensus of $39.30 is essentially unchanged vs 2026E $38.96 — zero forward growth.

### 2. Price Statistics

| Metric | 504-day | 252-day |
|---|---|---|
| Annualised return | −61.1% | — |
| Alpha vs SPY (annualised) | **−65.6%** | — |
| Beta vs SPY | 0.124 | −0.101 |
| R² | **0.001** | — |
| Annualised volatility | 51.3% (vol tool: 50.9%) | 59.0% |
| Sharpe (rf = 0) | −1.192 | −0.711 |
| Sortino (rf = 0) | −1.417 | — |
| Max drawdown | 75.6% | 58.8% |

**Interpretation and caveat:** the collapse is almost entirely idiosyncratic — R² of 0.001 means ~0% of CHTR variance is explained by SPY, so the beta of 0.12 (and the 252-day beta of −0.10) should be read as *"no reliable market sensitivity estimate,"* not as a genuinely market-neutral asset. With R² ≈ 0 the alpha intercept absorbs the entire drift (−65.6%) and its standard error is wide; treat alpha as descriptive, not statistically significant. Note also the profile-vendor beta of **0.733** conflicts with the return-based 0.12/0.73 spread — a third sign of estimation instability. Sharpe of −1.19 and Sortino of −1.42 are both decisively negative; Sortino being worse than Sharpe confirms downside volatility dominates. Volatility near 60% on a $134 stock with $96B of debt is a solvency-risk signature, not a mispricing signature.

### 3. Composite Quant Signal: **SELL**

Only one of five factors is positive, and it is the one most prone to value-trap failure in a declining-revenue, over-levered business. Composite z-score approx: Value +2.0, Quality 0.0, Momentum −2.0, Low Vol −2.0, Revisions −1.5 → **net clearly negative**. I stop short of "Strong Sell" only because P/B of 0.90 and P/FCF of 4.18 provide genuine asset/ cash-flow support and a takeover/asset-sale floor; median 2026-vintage price target (~$145) implies just ~8% upside against a 60% realized vol.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk is now the *base case*, not a risk** — the 12-1 signal is −25.8% and accelerating negative. Any bounce is a counter-trend trade, not a factor signal.
2. **Leverage/refinancing risk dominates all factors.** 4.5x EV/EBITDA with $5.0B interest vs $21.2B EBITDA is the single variable that decides the equity. Equity is 16% of EV — a 3% change in enterprise value moves equity ~19%.
3. **Beta/R² instability** — beta estimates range from −0.10 to +0.73 across methods; do not use CHTR in a beta-hedged or market-neutral construction.
4. **Data integrity**: revision-momentum tool output invalid (fiscal-period mismatch); price feed truncated 7+ months vs. current price. Re-run both before any downstream use.
5. **Low liquidity / crowding**: average volume ~1.5–2.0M shares on a now-$18B cap, with 4–9M share capitulation days (2025-07-25: 9.6M; 2026-01-30: 7.2M) — exits are gapped, as the Jul-2025 −18.5% single-session repricing demonstrated.
6. **Earnings quality is actually a bright spot** — accruals ratio −0.072 (negative accruals = conservative accounting) and F-score 7/9. The problem is the income statement's trajectory and the balance sheet, not the accounting.
