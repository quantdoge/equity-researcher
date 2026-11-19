# Quant Analyst

- Symbol: FROG
- Elapsed: 63.2s

---
## FROG (JFrog Ltd.) — Quantitative Factor Report
Technology / Software–Application · Price $114.38 · Mkt cap $13.85B · EV $12.61B · FY25 revenue $531.8M

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E −184.5 (GAAP loss), EV/EBITDA −303.5 (EBITDA −$41.5M), P/FCF **93.4x** (FCF yield 1.07%), P/B 14.97 | **6 / 7** (only NET richer on FCF) | **Strong Sell** |
| **Momentum** | 12-1: **+11.85%** (tool) / **+60.0%** recomputed from raw OHLCV — see caveat | 1–3 / 7 (GTLB +31.7, ESTC +29.4, FROG, DDOG +10.7, NET +0.1, SNOW −3.4, MDB −11.0) | **Buy** |
| **Quality** | ROE −8.09%, ROIC −9.92%, GP/A 0.3045, accruals −16.2%, **F-Score 5/9** | **5 / 7** (GP/A 6th: GTLB .484, MDB .470, ESTC .420, DDOG .412, SNOW .345, **FROG .305**, NET .268) | **Neutral / Sell** |
| **Low Vol** | Ann. vol **87.9%** (1y) / 74.5% (2y), beta 1.69, max DD −49.6% | **6–7 / 7** (worst-vol name; DDOG 74.7%) | **Strong Sell** |
| **Earnings Revision** | +20.1% (FY28 EPS $1.604 vs prior $1.335) — **period misaligned, see flags** | **1 / 7** (only name with documented upward revisions) | **Buy (low confidence)** |
| *(Piotroski F-Score)* | **5 / 9 — Moderate**. Fails: positive ROA (0), lower leverage (0), **no dilution (0)**, GM improvement (0) | — | Neutral |

**Fundamental trend (supportive):** Revenue $280M → $350M → $428M → $531.8M (+24.1% yoy, 3y CAGR 23.8%); gross margin 76.8%; operating margin improving −32.1% → −20.8% → −16.9%; OCF $21.4M → $74.2M → $110.9M → **$145.7M** (27.4% of revenue). Genuine operating leverage — quality is weak on *earnings* but strong on *cash* (accruals −16.2% is a positive).

### 2. Price Statistics (252d, vs SPY, 0% rf)

| Metric | Value |
|---|---|
| Total return (12m, raw adj-close 48.28 → 114.38) | **+136.9%** |
| Alpha (annualised, OLS) | **+121.2%** — but **R² = 0.077**, t ≈ 1.5 → **not statistically significant** |
| Beta | **1.691** (1y OLS) / 1.683 (vol model) / 1.629 (2y) / 1.306 (vendor) |
| Ann. volatility | **87.9%** (1y), 74.5% (2y) |
| **Sharpe** | **1.55** (consistent with raw +136.9% / 87.9% vol); tool variant 2.18 |
| **Sortino** | **≈3.2** rescaled to consistent return basis; tool 4.50 (vol/downside-dev ratio 2.07 applied) |
| **Max drawdown** | **−49.6%** (peak 68.98 on 2025-12-12 → trough 34.75 on 2026-02-23); tool 1y −34.8%, 2y −49.6% |
| Correlation w/ software peers | 0.38 (SNOW) – 0.49 (ESTC); **vs SPY only 0.28** |
| Liquidity | ~2.2M shares/day ≈ $220M ADTV — no constraint |

### 3. Composite Quant Signal: **NEUTRAL**
Momentum and estimate revisions are the only positive pillars, and both carry data caveats. They are offset by the most expensive value profile in the peer group (93x P/FCF on a GAAP loss), bottom-quintile quality (negative ROE/ROIC, F-Score 5), and the worst low-vol score in the comp set (88% vol, beta 1.69). Cross-sectional scoring: **top-quintile on 1 of 5 factors** — not the rare value+momentum+quality alignment. Bull case rests entirely on cash-flow compounding (OCF +34% yoy) re-rating the multiple, not on factor support.

### 4. Key Quant Risk Flags
1. **Momentum data conflict (material).** The momentum tool reports +11.85% for 12-1; recomputing from raw OHLCV (56.87 @ 2025-11-17 → 91.00 @ 2026-10-19) gives **+60.0%**, and 6-month gives +41.8% vs the tool's +3.97%. The volatility tool's Sharpe corroborates the raw series, so momentum rank is likely **better than 3rd of 7**. Also: trailing-1y return is +137% but 12-1 momentum is only +60% — the entire gain is concentrated in the last month (85 → 114 in 9 sessions) → **short-term reversal risk is elevated**.
2. **Alpha not significant.** R² 0.077 means 92% of variance is idiosyncratic; the +121% alpha has t ≈ 1.5 (p ≈ 0.13). Do not treat this as stock-picking skill evidence. Correlation to SPY of 0.28 also makes beta an unreliable hedge ratio.
3. **Earnings-revision figure is likely overstated.** The tool compares FY2028 consensus ($1.604, only **5 analysts**, range −$29.39 to +$23.09) against a "prior" of $1.33532, which is *exactly* the FY2027 consensus → period misalignment. Real upward drift exists (FY25 $0.79 → FY26 $1.15 → FY27 $1.34 → FY28 $1.60) but treat +20.1% as unverified.
4. **Earnings-gap risk / fat tails.** Single-day gaps dominate the tape: **+35% (2026-11-06), −25% (2026-02-20), +24% (2026-05-08)**. Sortino > Sharpe by 2.07x confirms positive skew, but drawdowns are brutal and fast (49.6% in 10 weeks). Position sizing must assume 20–35% overnight gap risk.
5. **Dilution / leverage.** Share count 99.2M → 116.2M (+17% since 2022); F-Score fails on dilution and leverage. SBC-heavy SGA ($300M vs revenue $532M) — non-GAAP EPS is far from GAAP.
6. **Factor crowding: low.** Peer correlations 0.38–0.49 and SPY 0.28 indicate no crowding in the momentum trade; risk is standalone volatility, not factor unwinding. Peer set is a hand-built software comp (DDOG, SNOW, MDB, NET, GTLB, ESTC) — the vendor "sector" list returned only mega-cap Technology (AAPL, MSFT, NVDA), which is not a valid comparison for a $14B software name; ranks above are therefore **n=7, indicative only, not statistically robust.**
