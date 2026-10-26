# Quant Analyst

- Symbol: CBRE
- Elapsed: 90.1s

---
# CBRE Group, Inc. (CBRE) — Quantitative Factor Report

**Sector:** Real Estate / Real Estate – Services · **Price:** $123.58–123.67 · **Mkt cap:** ~$35.6–37.2B · **Beta (profile):** 1.23

**Peer-set caveat (read first):** CBRE is a commercial real-estate *services* firm, not a REIT. The `get_sector_peers` output is dominated by mega-cap REITs (PLD, WELL, EQIX…), which are structurally non-comparable. I therefore computed cross-sectional ranks against CBRE's true industry comps — **JLL, CWK, CIGI** — with PLD as a large-cap sector reference. All ranks below are within that 4-name services group. This is a **very small sample**; ranks are directional, not statistically robust.

---

## 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank (services group) | Signal |
|--------|:-------------:|:-----------------------------:|--------|
| **Value** | ~20 | 4 / 4 (most expensive) | **Negative** |
| **Momentum** | ~35 | 1 / 4 (least bad) | **Negative** |
| **Quality** | ~55 | 1 / 4 (best ROE) | **Neutral** |
| **Low Vol** | ~50 | 1 / 4 (lowest vol) | **Neutral** |
| **Earnings Revision** | ~75 | n/a (positive) | **Positive** |

### Supporting raw figures

**Value** — CBRE P/E **32.1x**, P/B **3.86x**, EV/EBITDA **17.8x**, P/FCF **31.2x**.
vs JLL (18.5x / 13.0x / 15.0x), CWK (31.3x / 12.1x / 9.5x), CIGI (45.0x / 9.0x / 14.9x). CBRE carries the **highest EV/EBITDA and highest P/FCF** in the group — expensive on cash-flow multiples despite a middling P/E. Rich valuation is the weakest factor.

**Momentum (12-1, 252d)** — **−7.53%** (signal "negative"). Least negative in the group (JLL −5.01%, CIGI −11.78%, CWK −13.18%), so relatively resilient, but absolute momentum is firmly negative. **Caveat:** the trailing 252-day *total* return was **−35.3%**, versus only −7.5% on the 12-1 (ex-last-21-day) basis — meaning most of the damage is **very recent** (last ~month). That pattern is a momentum-reversal warning, not stabilization.

**Quality** — ROE **12.02%** (2025), best in group (JLL 10.39%, CWK 4.51%, CIGI 3.73%). Accruals **−0.013** (earnings cash-backed — good). BUT ROIC has deteriorated sharply: **12.5% (2022) → 8.0% (2023) → 9.5% (2024) → 6.6% (2025)**; ROE trend 16.4% → 10.9% → 10.5% → 12.0%. GP/assets 0.197 (low; JLL's 1.45 reflects a different gross-profit definition and is not comparable). Piotroski F-Score **5/9 (moderate)** — loses points on ROA improvement, leverage, gross margin, and asset turnover. Quality is "best of a weak group," not high in absolute terms.

**Low Vol** — annualized vol **36.6%**, beta **0.93** (calc) vs 1.23 (profile). Lowest vol in group (JLL 37.3%, CWK 47.6%, CIGI 40.2%); beta second-lowest behind CIGI 0.77. Relative low-vol leader, but **absolute volatility is high** — this is not a defensive name.

**Earnings Revision** — most-recent consensus EPS vs estimate 3 months prior: **+17.75%**, signal **"upgrade."** The strongest positive factor. **Caveat:** the comparison horizon is **FY2030** ($13.48 vs $11.45), an unusually long-dated estimate — positive directionally, but far-horizon revisions carry much weaker near-term predictive power than FY1/FY2 revisions would.

---

## 2. Price Statistics (252-day window, benchmark SPY)

| Metric | Value | Note |
|--------|------:|------|
| **Alpha (annualized)** | **−47.84%** | Severe underperformance vs SPY |
| **Beta** | **0.94** | vs profile 1.23; below-market sensitivity |
| **R²** | **0.11** | **Very low** — CAPM fit poor; alpha estimate is noisy/low-confidence |
| **Annualized return** | −35.29% | Trailing 252d total return |
| **Annualized volatility** | 36.6–36.9% | High absolute vol |
| **Max drawdown** | −28.15% | Per price-vol tool window |
| **Sharpe ratio** | **−0.957** | Negative; risk-adjusted loss |
| **Sortino ratio** | **−1.291** | Downside deviation dominates |

Interpretation: the stock has delivered strongly negative risk-adjusted returns (Sharpe −0.96, Sortino −1.29) with high volatility. The **R² of 0.11** means only ~11% of CBRE's return variance is explained by the market — most of the −47.8% "alpha" is idiosyncratic, and the alpha figure should be treated as a low-confidence estimate rather than a precise skill/quality measure. Note the inconsistency between max drawdown (−28%) and the −35% total return implies the decline was a sustained grind plus a sharp recent leg, not a single peak-to-trough event.

---

## 3. Composite Quant Signal: **NEUTRAL (with negative tilt)**

Factor tally: Value **negative** (most expensive in group), Momentum **negative** (absolute; relative bright spot only), Quality **neutral** (best ROE but declining ROIC, F-score 5), Low-Vol **neutral** (relative leader, absolute high), Earnings Revision **positive** (upgrade, but long-dated). 

One clear positive (revisions) offset by a clear negative (valuation) and negative momentum — net **Neutral, leaning cautious**. The forward revision upgrade is the main offsetting argument; the combination of rich cash-flow multiples + deep, recent negative momentum + falling ROIC caps conviction. Not a Strong Buy or Strong Sell.

---

## 4. Key Quant Risk Flags

- **Momentum reversal risk (HIGH):** 12-1 momentum only −7.5% but trailing 252d return −35.3% → most of the loss is concentrated in the last ~21 days. Falling-knife pattern; no evidence of trend stabilization yet.
- **Low R² / noisy alpha:** R² = 0.11 makes the −47.8% alpha a low-confidence figure — do not treat it as a precise read on manager/company skill. Beta estimate (0.94 calc vs 1.23 profile) is also unstable.
- **Valuation crowding / multiple risk:** P/FCF 31x and EV/EBITDA 17.8x are the richest in the services peer group; limited margin for error if growth disappoints. Cyclical CRE-services exposure amplifies this.
- **Deteriorating capital returns:** ROIC 12.5%→6.6% over three years; F-score components on margin/turnover/leverage all failing. Quality trend is negative even though ROE level leads the group.
- **Earnings-revision quality:** the +17.75% upgrade is measured against an **FY2030** estimate — long-dated and weakly predictive near-term. A positive signal, but low-weight.
- **Sample-size warning:** cross-sectional ranks rest on only 4 comparables (3 services + 1 REIT); sector-relative conclusions are indicative, not statistically significant. The provided sector-peer list is REIT-dominated and not truly comparable to a services firm.
- **Liquidity:** not a concern — large-cap ($35B+), deep liquidity.

*Data note: profile beta (1.23) and calculated beta (0.94) disagree; I report both. Max drawdown and total-return figures come from tools using different window defaults and are not perfectly reconcilable.*
