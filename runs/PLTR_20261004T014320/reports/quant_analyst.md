# Quant Analyst

- Symbol: PLTR
- Elapsed: 87.7s

---
All quant factors computed for **PLTR (Palantir Technologies Inc., Software-Infrastructure, $188.75, mcap $433.4B)**. Sector ranking is cross-sectional vs. software comps MSFT, ORCL, CRWD, SNOW (5-name peer set, IPO-2020 name vs. mature comps — flagged where relevant).

## 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank (of 5) | Signal |
|---|---|---|---|
| Value | P/E 299.6; EV/EBITDA 283.5; P/FCF 230.5; P/B 64.6 | **5/5 (worst)** | **Strong Sell** — 10x MSFT's P/E (28.8), 12x ORCL's (24.4). Bottom percentile globally. |
| Momentum | +60.8% (12-1m, 252d) | **1/5** (SNOW +57.8, MSFT +39.9) | **Strong positive** |
| Quality | ROE 21.7%, GP/Assets 0.41, Accruals −0.057, Piotroski F=8/9, ROIC 18.3% (vs −5.6% in '22) | **1/5** (only "high" vs. all "low" comps) | **Strong positive** — accelerating, not static |
| Low Vol | Ann. vol 63.1%; beta 1.63 vs SPY; max DD 43.2% | **5/5 (worst) vs mega-caps; ≈3/5 vs CRWD/SNOW** (inferred) | **Strong negative** — top-decile risk profile |
| Earnings Revision | FY30 EPS est +114.6% (6.70 → 14.38) | n/a (n=1 vs peers) | **Positive, LOW reliability** — see flag 4 |

## 2. Price Statistics (252d window vs. SPY)

| Stat | Value |
|---|---|
| Alpha (annualized) | **−7.45%** |
| Beta | 1.635 (profile beta 1.62) |
| R² | **0.115** — market explains ~11% of variance |
| Sharpe | 0.47 |
| Sortino | 0.86 |
| Ann. return / vol | +30.0% / 63.4% |
| Max drawdown | **−43.2%** |
| Peer correlation | MSFT 0.41, ORCL 0.38, CRWD 0.45, SNOW 0.48 — idiosyncratic mover |

## 3. Composite Quant Signal: **NEUTRAL**

Bimodal profile: top-of-sector momentum + quality + revision momentum vs. **off-the-chart valuation** and top-decile volatility. Alpha is negative (−7.4%) despite a +30% trailing return — PLTR over-earned only by taking far more beta than it should; on a pure factor model the extreme value factor (P/E ~300, EV/EBITDA ~283) is the dominant long-run predictor and it says the price embeds ~5 years of hyper-growth already. Balanced composite: **Neutral** — momentum/quality funds will love it, value/risk-parity mandates will not. (A value-strict lens alone = Strong Sell.)

## 4. Key Quant Risk Flags

1. **Momentum reversal exposure:** +60.8% 12m return with a −43.2% max drawdown *inside the same window*; R² of 0.11 means this is an idiosyncratic NAV, not a sector bet — reversal risk is real and violent.
2. **Factor crowding / multiple-compression:** Consensus models imply revenue $17.9B (FY28) → $33.4B (FY29) → $70.1B (FY30), i.e. ~2x/year compounding to ~2030. Any guidance miss re-rates a 283x EV/EBITDA simultaneously — asymmetric downside.
3. **Statistically unreliable alpha:** R² = 0.115 → the −7.45% alpha has wide error bars; treat as directional, not precise. Sortino (0.86) vs Sharpe (0.47) confirms downside is comparatively contained but magnitude of vol is the binding constraint.
4. **Small-sample revision:** +114.6% EPS revision rests on n=3 analysts and compares FY2030-vs-prior-FY2030 far-forward estimates — likely model extrapolation, not genuine forecast upgrade. Meanwhile **near-term consensus** (FY27, n=19) is the more trustworthy anchor; price targets (UBS $250, DA Davidson $250, Needham $215 — all raised Aug–Sep 2026) corroborate the upgrade direction at +32% implied upside to current price, but they carry no ratings.

**Bottom line:** Exceptional quality and momentum, priced at a multiple that only survives if 40%+ growth compounds for half a decade, with 63% vol and a −7% alpha. Neutral composite, high-conviction on the *inputs* (quality & revision momentum are genuinely strong), zero margin of safety on the *price*.
