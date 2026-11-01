# Quant Analyst

- Symbol: DDOG
- Elapsed: 38.3s

---
All data gathered. Writing the report now.

## Quantitative Report — DDOG (Datadog, Inc.)
**Sector:** Technology / Software–Application (Observability & Cloud Monitoring) · **Price:** $235.27 · **Mkt cap:** $84.5B · **EV:** $82.6B
**Note on benchmarking:** `get_sector_peers` returns only mega-cap Tech (AAPL/NVDA/MSFT/semis), which are not economic comparables. I substituted a hand-built observability/security-SaaS peer set — **SNOW, NET, CRWD, MDB** — for cross-sectional ranks (n=5). Treat all "Sector Rank" figures as *small-sample peer ranks*, not universe percentiles.

---

### 1. Factor Scores

| Factor | Score / Raw | Peer Rank (n=5) | Signal |
|---|---|---|---|
| **Value** | P/E 784x · P/B 22.9x · EV/EBITDA 426x · P/FCF 85.5x · FCF yield 1.17% | **2 of 5** | Negative (absolute) / Least-bad (relative) |
| **Momentum (12-1)** | +13.43% | **5 of 5** (SNOW +28.6, NET +33.1, MDB +19.7, CRWD +47.2) | Positive but weakest in group |
| **Quality** | ROE 2.89% · ROIC **−0.84%** · GP/Assets 0.412 · Accruals −0.142 · F-Score **6/9** | **2 of 5** | Neutral–Weak |
| **Low Vol** | Ann. vol 73.9% · Beta 1.44 (1.51 reported) · MaxDD 27.4% | n/a (peer vols not computed) | Negative (high vol) |
| **Earnings Revision** | FY30 EPS 5.26 vs 4.34 prior = **+21.2%** | n/a | Upgrade — but **weak evidence** (see flags) |

**Value detail:** DDOG is the only GAAP-profitable name in the peer set. On P/FCF it ranks 2nd (85.5x vs MDB 57.3x, SNOW 92.2x, CRWD 197.4x, NET 301.6x). On EV/EBITDA it is one of only two with positive EBITDA (426x vs NET 920x). Relative attractiveness is an artifact of peers being loss-making — the absolute multiple remains extreme: **92.8x FY26E EPS** ($2.536), 79.1x FY27E ($2.975), 64.6x FY28E ($3.641).

**Quality detail:** ROIC is negative in 3 of 4 years (2022 −2.61%, 2023 −1.14%, 2024 +1.19%, 2025 **−0.84%**) — the company destroys capital on a GAAP operating basis. ROE collapsed from 6.77% → 2.89%. Piotroski 6/9, failing on ROA improvement, gross-margin improvement, and share dilution (diluted shares 350.3M → 363.5M, +3.8% — persistent SBC dilution). Offsetting positives: gross margin 80.0%, gross profit/assets 0.412 (2nd, behind MDB 0.470), and strongly negative accruals (−0.142) — cash conversion is genuinely high, with FY25 operating CF $1,050M (30.6% of revenue) vs net income only $108M.

**Fundamental trend (context for the quality score):** Revenue $1,675M → $2,128M → $2,684M → $3,427M (+27.1%, +26.1%, +27.7% — remarkably stable ~27%). But operating margin slipped from +2.0% (FY24) to **−1.3%** (FY25), and SGA grew +28.5% vs revenue +27.7% — growth is being bought.

---

### 2. Price Statistics (252 trading days, benchmark SPY)

| Metric | Value |
|---|---|
| Annualised alpha | **+83.4%** |
| Beta | **1.449** (R² **0.066**) |
| Annualised return | +107.1% |
| Annualised volatility | 74.1% |
| **Sharpe ratio** | **1.445** |
| **Sortino ratio** | **2.277** |
| Max drawdown | −27.4% |

**Correlation structure** (365d): CRWD 0.628 · MDB 0.593 · SNOW 0.561 · NET 0.509 · **SPY 0.256**. DDOG's correlation to the market is very low (0.26), which is *why* R² is only 0.066 — the alpha is real in a point-estimate sense but the model explains almost none of the variance.

---

### 3. Composite Quant Signal: **NEUTRAL** (score +0.5 of ±5)

Reasoning: strong absolute price appreciation, positive and accelerating estimate revisions, and best-in-class relative profitability within its peer cohort are offset by (a) negative ROIC and deteriorating operating margin, (b) an extreme absolute multiple with a 1.2% FCF yield, (c) weakest 12-1 momentum among direct peers despite the best trailing return, and (d) a statistically unreliable alpha (R² 0.07). **Upgrade to Buy would require** positive operating leverage (op margin >5%) plus decelerating SBC. **Downgrade to Sell triggers** on any break of 12-1 momentum below 0% or a negative revision to FY26/FY27 consensus.

---

### 4. Key Quant Risk Flags

1. **MOMENTUM REVERSAL RISK — most important.** Total 252d return is +107.1% but 12-1 momentum (excluding the last 21 days) is only +13.43%. That arithmetically implies **~+83% in the final 21 trading days** (2.0712 / 1.1343 − 1 = +82.6%). This is the classic 1-month-reversal setup: the stock is in the bottom quintile of *peer* momentum while sitting on a violent short-term spike. Quantitatively the worst possible momentum configuration — high recent gain, low sustained trend. *Verify this spike against a raw price series; if genuine, expect mean reversion.*
2. **Factor crowding / beta-1.45 in a 74%-vol name.** Max drawdown of 27.4% occurred within a year that returned +107% — the path is extremely convex. Correlation to CRWD at 0.63 makes DDOG a partial proxy on the crowded "AI-adjacent enterprise software" trade.
3. **Earnings revision signal is fragile.** The +21.2% revision compares the FY2030 estimate (5.26, **only 4 analysts**) to 4.34 — which is now the *FY2029* consensus. This is a **period roll-forward artifact**, not a clean same-period revision. The credible numbers are FY26E $2.536 (26 analysts) and FY27E $2.975 (27 analysts); **no prior-vintage consensus was available**, so I cannot confirm the direction of revisions on the periods that matter. Do not underwrite the bull case on this signal alone.
4. **Alpha is not statistically significant.** R² = 0.066 means 93% of DDOG's returns are idiosyncratic. The +83.4% alpha has a very wide standard error; with n=252 and this residual variance, the t-statistic is unlikely to clear conventional hurdles.
5. **Valuation has no floor.** 784x GAAP P/E on $0.30 EPS, 426x EV/EBITDA, 85x FCF. The entire multiple rests on the 20% EPS CAGR implied by consensus (FY26 $2.54 → FY30 $5.26). Any deceleration compresses both E and the multiple simultaneously.
6. **Data gaps:** peer low-volatility scores were not computed (only absolute DDOG vol/beta available), so the Low Vol rank is unranked; peer earnings-revision scores likewise unavailable; the ranked universe tool covers only 25 mega-caps and excludes DDOG, so no true universe percentile exists for any factor.
