# Quant Analyst

- Symbol: TEM
- Elapsed: 59.3s

---
# TEM (Tempus AI) — Quantitative Factor & Risk Report

**Data vintage note:** price file ends 2026-02-20 (close $58.37); quote used by ratio engine $55.45; mkt cap $9.66bn, EV $10.24bn, 174.3m sh. IPO 2024-06-14 → only ~20 months of trading history. All 252-day statistics are **single-regime and low-powered**.

## 1. Factor Scores

| Factor | Score (0–100) | Cohort Rank | Signal |
|---|---|---|---|
| Value | 3 | 3 of 3 | Strong negative — P/E −39.3, EV/EBITDA −86.4, P/FCF −39.4, **P/B 19.7** (BVPS $2.82). No positive denominator exists; EV/Sales 8.1x FY25A / 6.4x FY26E |
| Momentum | 45 (conflict) | 2 of 3 (vendor) / 3 of 3 (recompute) | **Vendor says +24.5% (12‑1). My recompute from raw OHLCV: −14.3% trailing 12m ($76.72→$58.37) and ≈ −2% on true 12‑1 basis ($68.09→$66.78).** Price −46.4% from 103.42 high. Net: Neutral/rolling over |
| Quality | 22 | 2 of 3 (GP/assets) | ROE −49.9%, ROIC −13.9%, ROA −10.8%. Offsets: gross margin 62.7% (+7.7pp y/y), GP/assets 0.351 (NTRA 0.624, GH 0.314), accruals −0.012 (clean). Piotroski 5/9 (fails ROA>0, OCF>0, no dilution) |
| Low Vol | 3 | 3 of 3 | Vol 82.7% vs GH 55.0%, NTRA 56.5%. Beta 2.43 (regression) / 3.61 (vendor 5y). Worst in cohort by a wide margin |
| Earnings Revision | 75 | n/a | Upgrades. FY26E rev $1.60bn (+25.9%), FY27E $1.99bn (+24.2%), FY28E $2.41bn (+21.3%); FY26E EPS −0.05 → FY28E +0.55. ⚠ Headline +94.3% is on the **FY2030** line, n=4 analysts — a period-mapping artifact, not a near-term revision. Treat direction as valid, magnitude as unusable |

## 2. Price Statistics (252d, vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+24.5%** — but R²=0.185, residual vol 75% → **t ≈ 0.3, statistically indistinguishable from zero** |
| Beta | 2.44 (R² 0.185) / 2.43 (vol model) / 3.61 (vendor) |
| Ann. return / vol | +29.2% / 83.1% |
| Sharpe | 0.352 (vol model alternative: 0.455) |
| Sortino | 0.661 → Sortino/Sharpe 1.88, downside vol materially below total vol |
| Max drawdown | 34.8% (tool) — **my recompute: −50.8% close-to-close (103.25 → 50.78), −52.2% intraday.** Tool figure materially understates |
| Correlations | SPY 0.43, GH 0.54, NTRA 0.47, EXAS −0.37 |

**Fundamental scale check:** FY25 revenue $1.272bn (+83.4%; 2024 +30.4%), GM 62.7%, EBITDA −$118.5m (−9.3% mgn), net income −$245.0m, OCF −$218.1m, FCF −$245.4m (−2.5% FCF yield). SBC $124.7m = 9.8% of revenue. SG&A $715m = 56% of revenue. Consensus needs +$258m EBITDA swing in FY26E to $139m — the single most aggressive line in the model.

## 3. Composite Quant Signal: **NEUTRAL** (high-risk; 33/100)

Weights: Value 20, Momentum 25, Quality 25, LowVol 10, Revisions 20 → 0.2(3)+0.25(45)+0.25(22)+0.1(3)+0.2(75) = **32.7**. Genuine upward estimate revisions and an improving margin structure are offset by the market's most expensive book multiple among unprofitable comps, extreme volatility, and a broken price trend. Nothing here clears the bar for Buy; nothing justifies Sell given revision direction and 62.7% gross margin. Sell-side target cluster $66–100 (median ~$85) implies ~+45% upside — but those notes carry Neutral-equivalent ratings from Jefferies, UBS, Goldman, Redburn; PTs are not ratings.

## 4. Key Quant Risk Flags

1. **Momentum reversal / trend break** — −46% from the October high on a −50.8% drawdown. The vendor momentum reading conflicts with the raw tape; I weight the tape. Any systematic momentum exposure is likely exiting, not entering.
2. **Alpha is not real** — +24.5% alpha on R²=0.185 is noise. Beta 2.4–3.6 means this is a levered market/growth-sentiment proxy, not idiosyncratic value creation yet.
3. **Small-sample everything** — 20-month history, 3-name comp cohort, 4 analysts on long-dated EPS. Cross-sectional ranks carry no statistical significance; do not size on them.
4. **Factor crowding / theme beta** — 0.47–0.54 correlation with GH/NTRA puts TEM inside the same "AI-genomics" crowded trade; a de-rating of that theme hits all three together.
5. **Dilution + balance sheet** — $124.7m SBC (F-score fails on share issuance), net debt ~$572m, interest expense $70.3m, FCF −$245m/yr. Funding is not an immediate risk but equity is the marginal currency.
6. **Data gaps:** sector-peer API returns 20 mega-cap pharma/medtech names with **zero true comparables**; EXAS returned insufficient price history (likely delisted/acquired). Price-target published dates (Nov 2026) post-date the price file (Feb 2026) — vintage mismatch, cluster-level use only.
