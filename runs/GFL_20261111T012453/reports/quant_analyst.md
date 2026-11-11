# Quant Analyst

- Symbol: GFL
- Elapsed: 49.0s

---
All factor data gathered. The peer scan revealed a systematic problem I need to flag prominently: **every waste peer shows a negative beta** to SPY (WM −0.47, RSG −0.50, WCN −0.25, CWST −0.08). That is economically impossible and means the regression output is unreliable across the board.

---

# GFL Environmental Inc. (GFL) — Quantitative Factor Report

**Price:** $42.41 | **Mkt Cap:** $16.06bn | **EV:** $23.91bn | **Sector:** Industrials / Waste Management

## 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | 50 | **3 / 5** | Mixed — cheap EV/EBITDA, expensive FCF |
| **Momentum** (12-1) | 60 | **2 / 5** | Mildly positive (+1.79%) |
| **Quality** | 10 | **5 / 5** | Strong negative — worst in group |
| **Low Vol** | 25 | **4 / 5** | Negative — 33.2% vol, 26.0% drawdown |
| **Earnings Revision** | 60* | n/a | *Invalid as measured — see note |
| **TOTAL COMPOSITE** | **41** | 3 / 5 | **Neutral** |

### Value — rank 3/5, genuinely mixed
| Metric | GFL | WM | RSG | WCN | CWST | GFL Rank |
|---|---|---|---|---|---|---|
| EV/EBITDA | **11.96** | 23.39 | 17.85 | 19.43 | 17.85 | **1st (cheapest)** |
| P/E (trailing) | 4.25 ⚠️ | 35.43 | 36.15 | 45.73 | 775.0 | 1st ⚠️ *artifact* |
| P/FCF | **91.98** | 34.07 | 32.06 | 40.19 | 69.79 | **5th (priciest)** |
| P/B | 2.15 | n/a | n/a | n/a | n/a | n/a |

GFL trades at a **~40% EV/EBITDA discount** to the waste group — the one unambiguously attractive valuation datapoint. But it is the group's **most expensive on free cash flow (92x)**. The 4.25x P/E is not real: 2025 net income of **$3.83bn** against operating cash flow of only **$1.32bn** reflects the one-off gain on the Environmental Services disposal. On forward consensus, P/E is **51.7x (FY26)** and **37.0x (FY27)** — the opposite of cheap. Strip the artifact and value is ordinary.

### Quality — rank 5/5, the decisive negative
| Metric | GFL | WM | RSG | WCN | CWST |
|---|---|---|---|---|---|
| ROIC | **2.24%** | 14.00% | 12.89% | 9.77% | 3.18% |
| Gross profit / assets | **0.0709** | 0.1599 | 0.2026 | 0.1744 | 0.0918 |
| Accruals ratio | **+0.1305** ⚠️ | −0.0728 | −0.0628 | −0.0628 | −0.0943 |

GFL is **last on all three** measured quality sub-factors. ROIC of 2.24% is far below any plausible cost of capital — the company destroys economic value on invested capital despite the optically strong 51% ROE (an artifact of a shrinking post-divestiture equity base). Critically, GFL is the **only name in the group with positive accruals** (+0.13, flagged "warning"); all four peers run negative accruals, i.e. cash earnings exceed book earnings. Piotroski F-Score is 8/9 "Strong," but its accruals component scores **0** — consistent with the above.

### Momentum — rank 2/5, best-in-group relative
| GFL | RSG | WM | CWST | WCN |
|---|---|---|---|---|
| **+1.79%** | +5.25% | −6.04% | −7.31% | −8.23% |

Positive but weak in absolute terms; the sector is broadly in negative momentum, so GFL's relative standing is better than its absolute.

### Low Vol — rank 4/5 (vol & drawdown only; beta unusable)
| Metric | GFL | RSG | WM | WCN | CWST |
|---|---|---|---|---|---|
| Annualised vol | **33.23%** | 21.54% | 22.21% | 27.50% | 40.80% |
| Max drawdown | **−25.98%** | −14.63% | −17.05% | −13.75% | −30.16% |
| Sharpe (approx) | **0.145** | 0.988 | 0.544 | 0.779 | −0.103 |

GFL runs **~1.5x the volatility** of WM/RSG with a drawdown nearly twice as deep. It is decidedly *not* a low-volatility holding.

## 2. Price Statistics

| Statistic | Value | Assessment |
|---|---|---|
| Annualised return | 9.08% | Below quality peers |
| Annualised volatility | 33.01–33.23% | High |
| **Sharpe ratio** | **0.275** | Weak (peers 0.54–0.99) |
| **Sortino ratio** | **0.411** | Weak; downside not well compensated |
| Max drawdown | −25.98% | ~1.8x peer average |
| **Beta vs SPY** | **0.126** ⚠️ | **Statistically void** |
| **Alpha (annualised)** | **+3.33%** ⚠️ | **Not reliable** |
| **R²** | **0.003** | 99.7% of variance unexplained |
| Correlation vs WM / RSG / WCN / CWST | 0.41 / 0.40 / 0.45 / 0.43 | vs WM–RSG 0.83 |

**Two Sharpe figures are reported (0.145 and 0.275) due to differing annualisation conventions in the calc engines — treat the range 0.15–0.28 as the estimate. Either way it is bottom-quartile.**

**Beta/alpha must be discarded.** R² of 0.003 means the regression explains essentially nothing; the beta of 0.126 (vs a profile beta of 0.492) carries no statistical content, and the +3.33% alpha inherits that. The corroborating evidence is damning: WM, RSG, WCN and CWST all return *negative* betas (−0.08 to −0.50), which is economically impossible for waste-management equities, and GFL's correlation with direct peers (0.40–0.45) is roughly half the WM–RSG figure (0.83). The return series is contaminated — likely stale pricing, dual-listing (TSX/NYSE) or CAD/USD splicing. **Any risk figure derived from beta here should be ignored.**

## 3. Composite Quant Signal: **NEUTRAL** (41/100)

The headline screener output ("P/E 4.25, ROE 51%, upgrades, 8/9 Piotroski") describes a very different company from the one in the data. Value is a **distorted artifact plus one real discount (EV/EBITDA)**; quality is **demonstrably last in its peer group on every measured metric**; risk-adjusted returns are **bottom-quartile**. Offsetting: cheapest EV/EBITDA in the group, second-best momentum, a consensus EPS path rising from $0.59 (FY25) to $2.53 (FY30), and sell-side targets at a median **~$57 (+35% vs $42.41)**.

Quality and low-vol are the factors that persist; value and momentum are the ones that mean-revert. The persistent factors argue against owning this; the cyclical ones argue against shorting it. **Neutral is the data-supported call — this is not the deep-value opportunity the trailing multiples advertise.**

## 4. Key Quant Risk Flags

1. **⚠️ Accounting distortion (highest severity).** Trailing P/E 4.25 and ROE 51.22% are driven by the Environmental Services disposal gain. Accruals ratio +0.1305 is the only positive reading in the peer group. Use EV/EBITDA and forward EPS, never GAAP P/E.
2. **⚠️ Broken beta/alpha inputs.** R² 0.003; negative betas for all five waste names. Any risk model, cost-of-equity or hedging calculation using this beta will be wrong. Rebuild from a clean price series before relying on it.
3. **Leverage.** Net debt ≈ $7.85bn (EV $23.91bn − mkt cap $16.06bn) ≈ **3.9x FY25E EBITDA of $2.09bn**. Elevated for the industry and the core driver of the equity's 33% volatility.
4. **FCF quality.** FCF ≈ $175m on a $16bn cap (P/FCF 92x); capex ≈ $1.14bn against $1.32bn OCF. Cash conversion, not earnings, is the binding constraint.
5. **Estimate dispersion / thin coverage.** FY27 EPS consensus $1.145 spans **$0.36–$1.92 (5.4x spread)**; FY29 and FY30 rest on **1 analyst**. The revision score of +21.27% is **not a 3-month revision** — the engine compared FY2030 ($2.526) against FY2029 ($2.084), a multi-year growth rate. Discard it as a revision signal.
6. **Momentum reversal risk.** +1.79% is thin, and the stock sits near the low end of its 12-month range after peaking ~$51.50. Weak momentum plus weak quality is the worst combination for drawdown.
7. **Analyst target drift negative.** Though median target is ~$57, recent direction is down: Scotiabank $57→**$55** (latest), UBS $63→$58. Goldman initiated only **Neutral** at $50.
8. **Liquidity: adequate, not deep.** ADV ~1.0–1.5m shares (~$45–65m), with sporadic 3–5m share days. Position sizing above ~1% of ADV will incur real impact.

**Sample-size note:** 252 daily observations is sufficient for volatility and drawdown (reliable), marginal for stable correlation estimates, and — given the evident data contamination — invalid for beta/alpha regardless of window length.
