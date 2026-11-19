# Fin Risk Analyst

- Symbol: FROG
- Elapsed: 45.8s

---
# FROG — JFrog Ltd. | Financial Risk Assessment
**Sector:** Technology / Software–Application (DevOps platform) · **Price:** $114.38 · **Mkt cap:** $13.85B · **Latest data:** Q3 FY2026 (10-Q filed 2026-11-06)

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (structurally debt-free)**

JFrog carries essentially no financial leverage. FY2025 total debt was $19.1M against $705M cash + short-term investments (**net cash $686M**). At Q3 FY2026, cash & ST investments reached **$880.9M** versus $112.0M of total debt, of which **$0 short-term and $0 long-term borrowings** — the $112M line appears to be lease/facility obligations tied to the PPE step-up ($22M → $119M in Q3), not funded debt.

- **Interest coverage:** N/A — interest expense is $0.0M in every reported period. EBIT is negative (FY25: -$66.0M), so coverage is not meaningful; there is no debt service to cover.
- **Net debt/EBITDA:** -$686M / -$41.5M (FY25); trailing EBITDA is +$1.1M, so the ratio is degenerate. **Treated as zero leverage.**
- **Refinancing cliff:** None. No maturity wall, no revolver draw, no convertibles identified in filings.
- **Cash runway:** FCF is *positive* ($207M TTM), so runway is effectively infinite; cash = **1.4x TTM revenue** and **8.5x annual fixed opex**.

**Conclusion:** Default risk is negligible. The Altman Z-Score of **1.353 ("Distress")** is a mechanical artifact of (a) negative retained earnings (x2 = -0.322) and (b) the tool using *book* equity in x4. Substituting market cap ($13.85B) for book equity ($1.01B) into x4 lifts Z to **~21.7**, deep in the safe zone. The Z-score here should be **disregarded** for solvency purposes; it is a profitability/accumulated-deficit signal, not a credit signal.

---

## 2. Key Financial Risk Metrics

| Metric | Q3 FY26 / TTM | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|---|
| Revenue | $642.2M TTM | $531.8M | $428.5M | $349.9M | +24% FY25, **+31% y/y in Q3'26** |
| Gross margin | 78.4% TTM | 76.8% | 77.1% | 78.0% | Stable, high |
| Operating margin | -7.4% TTM | -16.9% | -20.8% | -21.5% | **Improving sharply** (Q3'26: -1.0%) |
| Net income | -$21.1M TTM | -$71.8M | -$69.2M | -$61.3M | Q3'26: **+$6.6M (first profit)** |
| EBITDA | +$1.1M TTM | -$41.5M | -$44.4M | -$39.2M | Just inflecting |
| **Debt/Equity** | 0.11x (incl. leases) | **0.02x** | 0.03x | 0.05x | Negligible |
| Net debt | **-$768.9M (net cash)** | -$686.0M | -$304.7M | -$486.0M | Net cash |
| Interest coverage | N/M (no interest) | N/M | N/M | N/M | No debt service |
| Current ratio | **2.15** | 2.09 | 2.04 | 2.46 | Strong |
| Quick ratio | 2.15 | 2.09 | — | — | No inventory risk |
| Cash ratio | **1.76** | 1.73 | 1.64 | 2.08 | Exceptional |
| Working capital | $577.2M | $443.2M | $331.7M | $383.6M | |
| Equity/Assets | 60.9% | 66.2% | 68.5% | 69.8% | Deleveraging by equity build |
| **Altman Z** | 1.35 (misleading) | — | — | — | Market-value Z ≈ 21.7 |
| **Piotroski F** | **5 / 9 (Moderate)** | — | — | — | Fails on ROA, leverage, dilution, GM |
| FCF | **$207.4M TTM** | $142.3M | $107.8M | $72.2M | 32.3% margin, rising |
| FCF yield | **1.50%** | 1.07% | — | — | Low (valuation-driven) |
| FCF less SBC | **$45.4M** | -$14.4M | -$23.3M | -$23.0M | ⚠️ The real number |
| SBC / revenue | **25.2%** | 29.5% | 30.6% | 27.2% | ⚠️ Very high |
| Diluted shares | 129.5M | 116.2M | 109.7M | 103.3M | ⚠️ +6.7% in 9M, +25% since FY22 |

**Quality-of-earnings note:** The 32% FCF margin is real cash but is substantially *compensation the company pays in stock*. Against $161.9M TTM SBC, true cash FCF is **$45.4M** (7.1% of revenue, **0.33% yield**). On FY2025 the SBC-adjusted FCF was **negative**. This is the single most important caveat in the entire analysis.

---

## 3. Market Risk Profile

| Metric | 3-Year (756d) | 1-Year (252d) |
|---|---|---|
| Annualised volatility | **66.1%** | **87.9%** |
| Beta vs SPY | 1.385 | **1.683** |
| Max drawdown | **-49.6%** | -34.8% |
| Sharpe (rf=0%) | 1.30 | 1.55 |

Unlike most high-vol software names, the *return* has been good — Sharpe of 1.3–1.55 on 66–88% vol implies a huge realized rally (price $114 vs. a much lower 3-year base). But the risk profile is aggressive and **deteriorating on a 1-year basis**: beta has risen from 1.39 to 1.68 and vol from 66% to 88%. In a market drawdown of -20%, FROG's beta implies roughly **-30% to -34%**, and its 90th-percentile (1.65σ annual) downside is **-40% to -45%** before any fundamental shock. Liquidity in the stock itself is fine (mid-cap, $13.9B).

---

## 4. Downside Scenario: Revenue -20%

**Applied to TTM revenue of $642M → $514M** (a shock roughly equivalent to losing a large enterprise cohort / a severe IT-budget freeze; RPO of $812M, of which $422.6M billed, provides meaningful near-term backlog protection — a genuine mitigant).

| Line | Base TTM | -20% Revenue Shock | Comment |
|---|---|---|---|
| Revenue | $642M | $514M | Back to FY2025 level |
| Gross profit (78.4%) | $504M | $403M | -$101M |
| Opex (assume 70/30 fixed/variable) | $551M | $521M | Modest flex; mgmt would cut harder |
| Operating income | -$47M | **-$118M** | Loss widens ~2.5x |
| FCF (SBC non-cash) | $207M | **~$20M to +$50M** | Still not materially cash-negative |
| Cash & ST inv. | $881M | $880M+ | No debt to impair |
| Net cash | $769M | ~$750M | |
| Cash runway at -$150M/yr burn | — | **~5.9 years** | Stress case; realistic burn is far lower |
| Debt/EBITDA | net cash | net cash | No covenant exists to breach |

**Findings:**
- **Solvency is not at risk in any plausible revenue scenario.** Even a -40% revenue shock with zero cost action leaves >3 years of runway and no maturities. There is no covenant, no revolver, no refinancing event. The company can survive a prolonged multi-year downturn *on its own balance sheet*.
- **The risk is valuation, not viability.** EV ≈ $13.08B = **20.4x TTM revenue** and **63x TTM FCF** (288x SBC-adjusted FCF). A -20% revenue scenario that pushes operating losses to -$118M would likely compress the multiple to 8–10x forward sales — implying an **equity drawdown of 45–60%**, well beyond beta-implied downside.
- **Second-order risk:** at 20x sales with negative GAAP earnings, the equity is a duration asset — its value is a function of the discount rate. A 100bp move in real rates is worth more to FROG's price than a 5-point change in gross margin.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Split explicitly, because the two halves point in opposite directions:

| Dimension | Rating | Rationale |
|---|---|---|
| **Credit / solvency risk** | **LOW** | Net cash $769M, no funded debt, no maturities, positive FCF, current ratio 2.15 |
| **Liquidity risk** | **LOW** | Cash ratio 1.76; cash = 1.4x annual revenue; RPO $812M |
| **Market / equity risk** | **HIGH** | 66–88% vol, beta 1.4–1.7, -49.6% 3yr drawdown, 20x EV/Sales |
| **Cash-flow quality risk** | **MODERATE–HIGH** | SBC = 25% of revenue; SBC-adjusted FCF $45M (0.33% yield) |

The company **cannot go bust**; the shareholder **can lose half their capital**. For an investment memo, that distinction is the whole story.

---

## 6. Key Red Flags

1. **⚠️ SBC-driven earnings quality.** $161.9M TTM stock compensation against $45.4M SBC-adjusted FCF. Reported 32% FCF margin overstates distributable cash by ~4.6x. FY2025 SBC-adjusted FCF was *negative*.
2. **⚠️ Persistent dilution.** Diluted shares 103.3M (FY22) → 116.2M (FY25) → 129.5M (Q3'26) = **+25% over ~3 years, ~8–9% annualised**. Per-share value creation is materially below enterprise value creation. Piotroski F7 (no new shares) fails, correctly.
3. **⚠️ Valuation leaves no margin for error.** 20.4x TTM EV/Sales, 63x FCF. The -20% scenario implies a 45–60% equity decline even though the balance sheet is pristine.
4. **⚠️ Still GAAP-unprofitable at the operating line** across FY2022–FY2025 (four consecutive operating losses); TTM operating margin -7.4%. Only Q3'26 crossed into positive operating/net income — **one quarter is not a trend**.
5. **Goodwill & intangibles $399M = 39% of equity.** An acquisition-driven asset base with impairment exposure if growth decelerates.
6. **Extreme realized volatility** (88% 1yr) and rising beta. Position sizing risk is real regardless of fundamentals.

## 7. Positives Worth Weighting
- Revenue growth **accelerating** to +31% y/y with FY26 guidance of $680–682M (+28%).
- Operating margin improved ~9.5pts y/y FY25 (-16.9% vs -20.8%); Q3'26 near break-even. Genuine operating leverage emerging.
- Gross margin 78–80%, capex only 1.2% of revenue — an intrinsically high-return business model.
- $769M net cash and $880M gross cash: no external capital *required* to fund the downturn scenario.

## 8. Data Gaps & Caveats (flagged)
- **Interest coverage is N/A** — interest expense is $0 in all reported periods; no coverage ratio can be computed.
- **Net debt/EBITDA is not economically meaningful** (negative EBITDA in FY25; toolkit returned +16.52 on a sign artifact). Use net cash of $769M instead.
- **Altman Z (1.353) is unreliable here** — book-equity x4 and negative retained earnings. Market-value-adjusted Z ≈ 21.7.
- **Q3 FY2026 total debt ($112.0M) is unresolved:** reported short-term and long-term debt are both $0 while total debt is $112M and PPE jumped $97M. Most likely a finance-lease/facility purchase; **not confirmed in the data provided**. Even if it is funded debt, leverage remains ~0.1x equity.
- **Peer benchmarking unavailable.** The sector-peer tool returned only mega-caps (AAPL, MSFT, NVDA, TSM, AVGO, AMD) — not valid comparables for a $14B DevOps software company. No peer-relative multiple validation was possible.
- Quarterly balance sheet detail prior to Q1 FY2026 was not retrieved; DSO trend (69.6 days in Q3'26 vs 75.6 in Q2'26) is improving but the comparison window is short.
- No CDS spreads or agency ratings available for this issuer (no public debt outstanding — none exist).
