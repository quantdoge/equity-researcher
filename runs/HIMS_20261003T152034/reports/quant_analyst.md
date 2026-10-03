# Quant Analyst

- Symbol: HIMS
- Elapsed: 60.5s

---
All data gathered. Sector-rank tooling is broken (schema rejects list and string alike), so sector rank is estimated from the cross-sectional multiples I pulled directly. Final report below.

---

# HIMS — Hims & Hers Health, Inc. — Quantitative Factor Report

**Symbol:** HIMS (Healthcare / Medical-Care Facilities, digital health DTC)
**Price:** $29.00 · **Mkt cap:** ~$6.5B · **EV:** ~$8.0B · **Sector peers:** mega-cap pharma (LLY, JNJ, ABBV, MRK, UNH, NVS, AZN, TMO, AMGN, GILD, ABT, NVO) — comparability limited; HIMS is the only small-cap consumer-health name in the screen.
**Sample window:** 252 trading days (~1yr), benchmark SPY. R² = 0.14 → **headline caveat: factor covariance with the benchmark is low; treat alpha/beta as descriptive, not predictive.**

## 1. Factor Scores

| Factor | Score (raw) | Sector Rank (est., n=13) | Signal |
|---|---|---|---|
| **Value** | P/E 56.9 · P/B 13.9 · EV/EBITDA 45.0 · P/FCF 101.3 · div yield 0% | **13/13** (bottom of sector) | **Strong Sell** |
| **Momentum** | 12-1 mo (252d) return **−14.9%** | ~12/13 | **Sell** |
| **Quality** | ROE 23.7% · Gross profit/assets 0.80 · Accruals **−0.08** (neg = high quality) · ROIC 6.4% | ~4/13 (top quartile) | **Buy** |
| **Low Vol** | Ann. vol **96.2%** · β vs SPY **2.72** · Max drawdown **59.1%** | 13/13 (worst in sector) | **Strong Sell** |
| **Earnings Revision** | FY2030 EPS est 0.85 vs 0.783 3-mo ago = **+8.5% upgrade** (n = 2–4 analysts) | — (positive) | **Buy** (low confidence) |

**Composite factor tilt: 2 Strong-Sell, 1 Sell, 2 Buy** → asymmetric bearish. Classic *pricey momentum-reversal* profile: elite-quality operator, catastrophic valuation and risk statistics.

## 2. Price Statistics (252d, vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **−22.2%** |
| Beta | **2.74** (R² = 0.138 — mostly idiosyncratic, low benchmark fit) |
| Sharpe | **0.21** |
| Sortino | **0.39** |
| Volatility (ann.) | **96–97%** |
| Max drawdown | **59.1%** |
| Ann. return | +20.7% (yet 12-1 momentum negative → recent-month reversal) |

## 3. Composite Quant Signal: **SELL** (leaning Strong Sell on risk-adjusted grounds)

Supporting detail — the five signals rarely agree this badly:
- **Valuation is indefensible on every metric:** 56.9× trailing EPS (0.51 diluted EPS), 45× EBITDA, **101× FCF**. Dozens of sector peers sit at 12–20× EPS.
- **Momentum has reversed:** −14.9% 12-1 despite +20.7% 1-yr annualised return — the driver was a prior run-up, now unwinding.
- **Risk statistics are the sector's worst:** ~96% vol, β 2.7, 59% max drawdown, Sharpe 0.2 / Sortino 0.4; alpha −22% vs SPY.
- **Only real bull case:** quality (ROE 23.7%, gross-profit-to-assets 0.80, negative accruals) and a +8.5% EPS revision — but the revision is for **FY2030** with n=2–4 analysts: small-sample, far-forward, low weight.
- **Fundamental cross-check confirms:** Piotroski F = **4/9 (Weak)** — failing on ROA improvement, leverage change, dilution (shares 216M→258M, +19%), gross-margin improvement, asset turnover. Revenue ramp (FY25 $2.35B; ests to ~$4.6–5.0B) is real but SGA is 51% of revenue.

## 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** 12-1 momentum negative after a volatile ascent; at β 2.7 the stock will amplify any market drawdown while your farewell alpha (−22%) is paid regardless.
2. **Factor crowding / valuation stretch — HIGH.** 101× FCF and 45× EBITDA leave zero multiple cushion; any growth deceleration (note FY2030 analyst revenue est is *below* FY2029 — extrapolation artifact) forces violent de-rating. Analyst target range $26–42 (median ~$32) brackets spot price — little stated upside, real downside.
3. **Small-sample statistical noise.** Alpha/beta R² = 0.14; EPS revision n = 2–4; price-target set is 5 analysts spanning $26–$42 (i.e., no consensus, wide dispersion). Sector-rank tooling was unavailable (rejected list and string inputs) — ranks above are estimated from pulled multiples, not a formal z-score.
4. **No liquidity flag** — $6.5B cap, actively traded, deep float. Not a factor here.

**Bottom line:** A genuinely high-quality business impossible to buy at the current price. Sell / avoid at $29; the edge case to revisit is the **earnings-revision + quality** combination if the multiple ever compresses below ~20× EPS and beta normalises below 2.
