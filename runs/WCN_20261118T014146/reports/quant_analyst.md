# Quant Analyst

- Symbol: WCN
- Elapsed: 62.9s

---
All data gathered. One material data-integrity finding emerged that changes how the beta/alpha numbers must be read.

---

# WCN — Waste Connections, Inc. | Quantitative Factor Report
**Sector:** Industrials / Waste Management · **Price:** $181.50 (2026-11-17) · **Mkt Cap:** $45.4B · **Benchmark:** SPY (see integrity flag)

## ⚠️ Data Integrity Finding (read first)

**The supplied SPY benchmark series is misaligned, which corrupts every vs-SPY statistic.**

| Pair | Correlation (252d) |
|---|---|
| WCN–WM | **+0.734** |
| WCN–RSG | **+0.757** |
| WCN–SPY | **−0.103** |
| WM–SPY | **−0.289** |
| RSG–SPY | **−0.335** |

Three large-cap US Industrials all showing *negative* market correlation is not economically possible. The SPY series is stale/mis-dated. Therefore WCN's reported **beta vs SPY of −0.206, R² = 0.011**, and **alpha vs SPY of +14.15%** are artifacts and are discarded.

Substituting **WM** as the benchmark yields a cleanly specified regression: **beta 0.962, R² 0.545, alpha +1.96%**. This is the beta I carry forward. (Company-profile beta of 0.481 is the better estimate of true *market* beta — WCN is genuinely a below-market-beta asset; the −0.21 was noise.)

## 1. Factor Scores

Scores are percentile-style (0–100, 50 = sector median) against the true waste-comp set: WM, RSG, GFL, CWST.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 30 | 4 of 5 | **Negative** — P/E 43.5x (richest of the big three), EV/EBITDA 18.9x, P/FCF 37.9x, div yield 0.79% (lowest of trio) |
| **Momentum** | 35 | 3 of 3 | **Negative** — 12-1 momentum **+1.96%** vs RSG +8.90%, WM +2.71% |
| **Quality** | 50 | 3 of 3 | **Neutral** — ROE 13.1% (lowest of trio vs WM 27.1%, RSG 17.9%); GP/assets 0.189 (2nd, ahead of WM 0.160); accruals −0.063 (clean); F-Score 7/9 |
| **Low Vol** | 35 | 3 of 3 | **Negative** — 28.9% vol vs WM 22.2%, RSG 21.4%. Fails its "defensive" mandate |
| **Earnings Revision** | 65 | 2 of 3 | **Positive** — 2030E EPS revised **+7.75%** (7.948 vs 7.376); WM +9.18%, RSG +6.85% |

**Revision breadth corroboration:** eight brokers raised targets in the Oct-2026 cluster — UBS $215, TD Cowen $215, CIBC $207, BMO $206, Scotiabank $201, MS $200, Oppenheimer $200, Citi $192. Median **$203.5** ≈ +12% vs spot. Note the +7.75% score rests on only **4 analysts** for the 2030 period — statistically thin.

**Underlying fundamentals are genuinely improving:** revenue CAGR 2022–25 = 9.5% ($7.21B→$9.47B); operating margin 12.0%→18.1%; ROIC 6.57%→9.70% (2024→2025); diluted EPS 2.39→4.17. Value score suffers purely from multiple, not from business decay.

## 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| 12-mo total return | **+8.55%** | Verified from prices (167.21→181.50) |
| Annualised return (tool, arithmetic) | 16.8% | Overstated vs geometric — see flag |
| Annualised volatility | **28.9%** | Highest of peer trio |
| Beta vs WM (sector) | **0.962** | R² 0.545 — well specified |
| Alpha vs WM | **+1.96%** | Modest, ~2% |
| Beta vs SPY | −0.206 | **UNUSABLE** — misaligned series |
| Alpha vs SPY | +14.15% | **UNUSABLE** |
| Sharpe / Sortino (reported) | **0.61 / 1.01** | vs RSG 1.00/1.95, WM 0.42/0.68 |
| Sharpe (recomputed on verified return) | **≈0.30** | 8.55 / 28.9 |
| Max drawdown | −13.75% (tool) | Price-derived intra-window ≈ **−16.2%** (174.5→146.3) |

**Key read:** WCN beats WM on Sharpe (0.61 vs 0.42) but is decisively beaten by RSG (1.00/1.95) on both ratio and drawdown. The 28.9% vol is inflated by a handful of extreme days but is *realized* — 2026-10-22 +11.1%, 2026-11-17 −8.1%, 2026-02-12 −7.9%. A waste-hauler moving 11% in a session is a regime change, not noise.

## 3. Composite Quant Signal: **NEUTRAL** (44/100) — negative tactical bias

Weights: Quality 25% | Value 20% | Momentum 20% | Revision 20% | Low Vol 15% → 0.25(50)+0.20(30)+0.20(35)+0.20(65)+0.15(35) = **44.5**

WCN fails to clear the bar on any factor except earnings revision, and it **ranks last or tied-last on three of five** within its own narrow comp set. The improving ROIC, clean accruals, and broad target raises prevent a Sell. But this is not a factor-compounder today — it is a fairly-priced quality asset with deteriorating price behaviour. **RSG dominates WCN on momentum, value, Sharpe, Sortino, and drawdown** and is the better vehicle for the same cash-flow thesis.

## 4. Key Quant Risk Flags

1. **Fresh momentum break (highest concern).** 2026-11-17: **−8.1% on 5.59M shares (~4.3× the ~1.3M average)** — the largest volume print in the two-year sample. This lands five weeks after an +11.1% earnings-day pop (Oct-22). A full retracement of an earnings gap on heavy volume is a classic signal-decay pattern. The 12-1 momentum score (+1.96%) **excludes** this event via its 21-day skip, so the factor table understates the damage.
2. **Benchmark contamination (methodological).** Any beta/alpha/Sharpe quoted vs SPY from this feed is invalid. Do not pass the +14.15% alpha to the memo. Alpha vs WM (+1.96%) is the only defensible figure.
3. **Return-figure overstatement.** The 16.8% annualised return is arithmetic; realized geometric 12-month return is **+8.55%**. Reported Sharpe 0.61 flatters the true reward-to-risk (~0.30 geometric). Half the apparent performance is an annualization artifact.
4. **Multiple compression exposure.** At 43.5x trailing / **32.4x 2026E** adjusted EPS (5.61) / **30.0x 2027E** (6.06), WCN is the most expensive of WM/RSG/WCN on P/E while carrying the **lowest ROE (13.1%)**. The quality multiple is unsupported by the quality metric.
5. **Volatility regime shift.** Realized vol 28.9% vs 22.2%/21.4% for WM/RSG — WCN's low-vol trait (profile beta 0.48) has not held. Clients holding WCN for defensiveness are getting growth-stock dispersion.
6. **Factor crowding / substitution risk.** WCN–WM correlation 0.734, WCN–RSG 0.757. Little diversification benefit, and WCN is the *weakest* leg of a crowded quality-defensive trio — high risk of rotation into RSG.
7. **Thin estimate base.** Revision score depends on 4 analysts for 2030E; wider periods carry 16–19. Treat +7.75% as directional only.
8. **Liquidity: not a concern.** ~$235M/day traded.

*Sample sizes: 252-day return window (adequate, n≈251). Regression vs WM R²=0.545 (adequately specified). Peer set n=5 is small — sector ranks should be read as ordinal within waste management, not as universe-wide percentiles.*
