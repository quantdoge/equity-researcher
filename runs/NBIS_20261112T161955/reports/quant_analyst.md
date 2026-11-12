# Quant Analyst

- Symbol: NBIS
- Elapsed: 176.3s

---
# NBIS — Nebius Group N.V. | Quantitative Factor Report
**Sector:** Technology — Software/Application (AI cloud infrastructure) | **Country:** NL | **Mkt Cap:** ~$31.3–32.2B | **Price used:** $130.06–130.30

---

## ⚠️ Data-Quality Preamble (read before the table)

Three internal inconsistencies materially affect interpretation — I flag them rather than paper over them:

1. **Price conflict.** `calculate_valuation_ratios` uses $130.06; `get_company_profile` uses $130.295; the `get_price_history` series ends **2026-02-20 at $97.92**. Separately, price targets are dated up to **2026-10-21** at a posted price of $171.45. The feeds are not aligned to a common as-of date. I use **$130** as the reference price and treat the Feb-2026 close as a stale series.
2. **Momentum score appears broken.** Tool output: 12-1 momentum = **−13.96%**. Raw price history implies 2025-02-20 ($46.25) → 2026-01-20 ($99.29) = **+114.7%**. A −14% reading is impossible against that series. Note the reported 12M annualised return (**+107.33%**) is only arithmetically consistent with −13.96% if the final 21 trading days returned **+24%** — i.e. a violent V-shaped reversal. **I report the tool value but treat it as low-confidence.**
3. **Earnings revision is a period-mismatch artifact.** The "prior estimate" of **4.96431** is *identical* to the published **2029-12-31** consensus EPS, while "current" 12.24 is the **2030-12-31** estimate. The +146.56% "upgrade" is comparing **two different fiscal years**, not a true 3-month revision. It is **not a valid signal.**

---

## 1. Factor Scores Table

Peer set = 5-name custom AI/cloud-infra comparable group (NBIS, PLTR, ORCL, MSFT, AMD). Rank 1 = best. The tool-supplied "sector" peer list is 40,000-symbol mega-cap tech (AAPL/NVDA/MSFT) and is **not** a valid comparable set for a $32B pre-profit AI-cloud name — I built the tighter group manually.

| Factor | Raw Value | Score (0–10) | Peer Rank | Signal |
|---|---|---|---|---|
| **Value** | P/E 394.1 · P/B 6.98 · EV/EBITDA 67.9 · P/FCF **−8.75** | **1.5** | **4/5** | **Sell** |
| **Momentum** | 12-1 return −13.96% (tool); +114.7% raw-series (conflict) | **2.0** | **5/5** | **Sell / unreliable** |
| **Quality** | ROE 1.79% · ROA 0.66% · ROIC **−6.38%** · GP/Assets 0.029 | **1.0** | **5/5** | **Sell** |
| **Low Volatility** | σ 120.1% · β 3.89 · MDD 58.0% | **1.0** | **5/5** | **Strong Sell** |
| **Earnings Revision** | +146.6% (2030 vs 2029 — **invalid**) | **n/a** | **n/a** | **Unreliable** |

**Peer detail:**

| Metric | NBIS | PLTR | ORCL | MSFT | AMD |
|---|---|---|---|---|---|
| P/E | 394.1 | 273.4 | 22.1 | 29.4 | 221.6 |
| EV/EBITDA | 67.9 | 258.3 | 14.9 | 19.2 | 131.2 |
| P/FCF | −8.75 | 210.3 | −15.9 | 58.8 | 142.6 |
| ROE % | 1.79 | 21.70 | 39.69 | 30.23 | 6.88 |
| GP/Assets | 0.029 | 0.414 | 0.168 | 0.297 | 0.223 |
| Accruals | −0.024 | −0.057 | −0.057 | −0.065 | −0.044 |
| 12-1 Mom % | −13.96 | +26.55 | −6.53 | +10.87 | +16.63 |
| Vol % | 120.1 | 64.0 | 62.3 | — | — |
| Beta | 3.89 | 1.86 | 2.25 | — | — |

**Cross-sectional verdict: bottom quintile on 4 of 4 core factors. Only EV/EBITDA (3rd/5) is mid-pack.** A stock in the 5th percentile on value, momentum, quality *and* low-vol simultaneously is the mirror image of the "rare attractive" profile — it is the rare *unattractive* profile.

**Critical caveat — the model is structurally biased here.** NBIS is a pre-profit capex-ramp company: consensus EPS is **−$1.97 (2026), −$3.53 (2027), −$0.40 (2028)** before turning **+$4.96 (2029)** and **+$12.24 (2030)**. Revenue ramps $0.55B (2025) → $3.35B (2026) → $12.1B (2027) → $22.9B (2028) → $35.8B (2029) → $54.8B (2030). **Value and Quality factors score near-zero by mechanical construction when earnings are 4 years out.** Low GP/Assets (0.029) is what a GPU-cluster build-out looks like in an early capex cycle, not evidence of franchise decay. Treat the Value/Quality "Sell" as *low information content*, not as a damning fundamental judgment.

**The Piotroski F-Score directly contradicts the Quality factor: 8/9 — "Strong."** Components: positive ROA ✓, positive operating CF ✓, ROA improvement ✓, accrual quality ✓, **leverage increase ✗**, positive equity change ✓, no dilution ✓, gross-margin improvement ✓, asset-turnover improvement ✓. The resolution: **F-Score measures direction of change; the Quality factor measures level.** NBIS is a *deteriorating-from-low-base... no — improving-from-a-low-base* business. Trajectory positive, absolute quality still poor. Both readings are correct.

---

## 2. Price Statistics

| Metric | Value |
|---|---|
| Annualised volatility | **120.1%** (Sharpe tool: 119.3%) |
| Beta vs SPY | **3.89** (alpha regression: 3.909) |
| Alpha (annualised, OLS vs SPY) | **+59.2%** |
| R² vs SPY | **0.219** → correlation **0.47** |
| Sharpe ratio | **0.90** (volatility tool: 0.98) |
| Sortino ratio | **1.65** |
| Annualised return (12M) | **+107.3%** |
| Max drawdown | **−58.0%** |

**Interpretation:**

- **Alpha is statistically weak.** With R² = 0.219 and σ = 120%, residual (idiosyncratic) volatility ≈ 120 × √0.7808 ≈ **106%**. Standard error on annualised alpha over a 1-year sample ≈ 106/√1 ≈ **106%**. **t-stat ≈ 59.2 / 106 ≈ 0.56.** The +59% alpha is **not statistically distinguishable from zero** — and the sample is a single 252-day window. *Do not underwrite this alpha as skill; it is one draw from a 120%-vol distribution.*
- **78% of variance is unexplained by the market.** With β = 3.89 this is not a diversifying holding — it is a leveraged, idiosyncratic AI-capex bet. The high beta *and* low R² combination means SPY-hedging only removes ~22% of the risk.
- **Sortino (1.65) > Sharpe (0.90) by a wide margin** — returns are driven by large upside excursions with contained downside deviation relative to total vol. But max drawdown of 58% (raw series peak-to-trough Oct-2025 $141.10 → Feb-2026 $73.52 ≈ −48%) is a real
