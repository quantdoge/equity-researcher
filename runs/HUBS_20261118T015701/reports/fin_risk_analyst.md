# Fin Risk Analyst

- Symbol: HUBS
- Elapsed: 73.0s

---
## HUBS — Financial Risk Assessment

**Data currency caveat (important):** the price series ends **2026-02-20** ($233.50) but the financial statements extend to **Q3 2026 (filed 2026-11-04)**. The automated ratio tools all keyed to the FY2025 annual period (2025-12-31) and are therefore **~4 quarters stale**. I report both, and I flag market-risk metrics as computed on a window ending Feb-2026.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (de facto AA-equivalent balance sheet)**

HUBS carries **no bank debt and no notes**. The entire $224.0M of "total debt" is lease obligations (short- and long-term debt lines are both $0). Against that it holds **$1,296.8M** of cash and short-term investments — a **net cash position of +$1,073M**. There is **no refinancing cliff and no maturity wall**. Any conventional covenant test is non-binding: TTM EBIT of $192.8M against ~$1.1M of interest expense is >170x coverage. The company has never had a credit rating because it has never needed to borrow.

The Altman Z-Score of **1.598 ("Distress")** is a **false signal** and should be discarded on first principles. Two mechanical artifacts drive it: (a) X2 = **−0.196** because retained earnings are **−$595M** — the accumulated deficit of a company that spent a decade buying growth, not a sign of impairment; (b) X4 uses **book** equity ($2.07bn) instead of market cap ($11.6bn). Substituting market capitalization lifts X4 from 1.16 to ~6.2 and raises Z to **~4.8 — deep in the safe zone**. The note on the tool itself concedes this limitation.

### 2. Key Financial Risk Metrics

| Metric | FY2025 (tool base) | TTM Q3'26 (current run-rate) | Assessment |
|---|---|---|---|
| Revenue | $3,131.2M | $3,586.6M | +19.2% / +14.5% |
| Gross margin | 83.8% | 83.0% | Stable, slight compression |
| Operating margin | 0.4% | **5.4%** | Inflecting sharply |
| EBITDA | $206.6M | $411.2M | 2x in one year |
| Net income | $45.9M | $213.3M | Now solidly positive |
| Total debt | $262.3M (leases) | $224.0M (leases) | No funded debt |
| Net cash | +$1,441.5M | **+$1,072.8M** | Net cash, shrinking |
| Net debt/EBITDA | −6.98x | **−2.61x** | Net cash |
| Debt/equity | 0.13 | 0.138 | Trivial |
| Debt/assets | 0.07 | 0.064 | Trivial |
| Interest coverage | 13.01x (tool)² | ~181x | Non-binding |
| Current ratio | 1.67 | **1.34** ▼ | Deteriorating |
| Quick ratio | 1.67 | 1.34 ▼ | No inventory — identical |
| Cash ratio | 1.16 | 0.83 ▼ | Deteriorating |
| Working capital | $982.3M | **$524.9M** ▼ | −47% in 9 months |
| Altman Z | 1.598 → **~4.8 adj.** | — | Artifact, not distress |
| Piotroski F-Score | 7/9 | 7–8 (est.) | Strong |
| FCF (TTM) | $707.6M | $773.5M | |
| FCF margin | 22.6% | 21.6% | Healthy |
| FCF yield | 6.15% | **6.7%** | |
| **FCF ex-SBC** | **$179.4M** | **$269.8M** | **23% of reported FCF** |
| SBC / revenue | 16.9% | **14.0%** | Still very high |

² Tool reports 13.01x; EBIT $70.3M / reported interest $0.876M = ~80x on FY2025 figures. Likely methodology difference (broader lease-interest base). Either reading is non-binding.

**Piotroski detail:** 7 points scored; the two misses are F7 (share dilution) — **which has since reversed**, diluted shares fell 52.5M → 49.5M (−5.7% in nine months) — and F8 (gross margin improvement). Diligence on cash generation is strong: F1–F6 all pass.

### 3. Market Risk Profile — **HIGH / EXTREME**

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **60.4%** |
| Beta vs SPY (3y computed) | 1.08 (profile: 1.141) |
| Max drawdown (3y) | **−79.2%** (tool); −76.5% on close-to-close ($881 intraday Feb-2025 → $207 low Feb-2026) |
| Sharpe ratio | **−0.383** (negative = capital destroyed risk-adjusted) |

This is a textbook high-beta, high-tail-risk growth equity. Roughly **2.5x the volatility of the S&P 500** with a drawdown approaching the dot-com cohort. The Sharpe of −0.383 over three years means an investor was paid nothing for the ride. The de-rating was brutal and event-driven: single-day moves of −19% (Feb-2026, to ~$202), −16% (Nov-2025), and −14% (Jan-2026), each on 2–7M share volume vs a normal ~0.6M. The proximate cause per press coverage was **slower customer growth, questions over AI-era pricing, and guidance reset**, not a financial accident. The stock traded **65% below its 52-week high** as of the last observation.

### 4. Downside Scenario — Revenue −20%

Base: TTM revenue $3,586.6M, GM 83.0%, gross profit $2,977.7M, opex $2,784.9M (S&M $1,878.6M / R&D $906.3M), EBITDA $411.2M, cash $1,296.8M, debt $224.0M.

| | Revenue | Gross profit | Opex | EBIT | EBITDA |
|---|---|---|---|---|---|
| Base | $3,586.6 | $2,977.7 | $2,784.9 | **+$192.8** | **+$411.2** |
| −20%, **no cost action** | $2,869.3 | $2,381.5 | $2,784.9 | **−$403.4** | **−$234.0** |
| −20%, **10% opex cut** | $2,869.3 | $2,381.5 | $2,506.4 | **−$124.9** | **+$44.5** |
| −20%, **15% opex cut** | $2,869.3 | $2,381.5 | $2,367.2 | **−$2.5** | **+$166.9** |

**Survivability: not in question.** At the harshest reading (−$403M EBIT, zero cost action) the company burns ~$400M/yr against $1,297M of cash — roughly a **3.2-year runway before any management response**. But there are two enormous discretionary levers: (1) **suspending the buyback** — HUBS repurchased **$973.7M in the first nine months of 2026**, alone worth over $1.3bn annualized of preserved liquidity; (2) opex flexibility, as demonstrated by the 2026 restructuring. With just a 10% opex cut and buybacks paused, HUBS is **EBITDA-positive at −20% revenue**. Interest coverage never goes below ~100x because interest expense is ~$1M. **No liquidity crisis is constructible in this capital structure.** The realistic downside is to *valuation and equity price*, not to solvency.

### 5. Overall Financial Risk Rating: **LOW–MODERATE**

Rating split, because a single number obscures the truth here:
- **Solvency / credit risk: LOW.** Net cash, zero funded debt, no maturities, no covenants, positive and growing FCF.
- **Liquidity risk: LOW–MODERATE.** Cash ratio fell 1.16 → 0.83 and working capital halved in nine months — but this is **voluntary**, the product of a $974M buyback funded from the balance sheet, not of operating stress. Reversible instantly.
- **Market risk: HIGH.** 60% vol, 79% drawdown, negative Sharpe.
- **Earnings/cash quality risk: MODERATE.** SBC at 14% of revenue consumes **~77% of reported FCF**.

### 6. Key Red Flags

1. **Stock-based compensation is the dominant cash-flow distortion.** Reported FCF of $773.5M TTM includes a $503.7M non-cash SBC add-back. **SBC-adjusted FCF is only $269.8M** — a 2.3% true FCF yield, not 6.7%. GAAP net income of $213M is also flattered by SBC accounting and by interest income (Q3'26 net income $83.0M exceeded operating income $71.9M).
2. **Revenue growth is decelerating every single quarter.** YoY: Q1'26 **+23.3%** → Q2'26 **+19.8%** → Q3'26 **+17.1%**. For a 25x EV/EBITDA name, deceleration is the thesis risk.
3. **Capex is inflecting sharply upward.** Q3'26 capex alone was **$54.7M** — more than all of FY2025 ($53.2M). TTM capex $133.5M vs FY2025 $53.2M. If AI-infrastructure spend is structural, FCF margin compresses from 22% toward the high teens.
4. **Liquidity ratios deteriorating fast.** Current ratio 1.67 → 1.34; cash ratio 1.16 → 0.83; working capital −47%. Buyback-driven and reversible, but it removes the cushion if a downturn arrives simultaneously.
5. **Gross margin eroding:** 85.0% (FY2024) → 83.8% (FY2025) → 82.6% (Q3'26). Hosting and AI-inference costs are diluting a pristine software margin. This is the single most important structural metric to monitor.
6. **Negative retained earnings (−$595M)** with book equity *falling* ($2.07bn → $1.63bn) because buybacks exceed net income. Book-equity-based leverage and Z-score metrics will keep deteriorating even as economics improve — do not trade on them.
7. **Restructuring / narrative risk.** Management framed 2026 cuts as building "a flatter organization around AI-driven customer outcomes, not driven by AI efficiencies" — a distinction the market is skeptical of. The AI-disruption debate over seat-based pricing is a live, unresolved overhang.

### 7. Data Gaps (explicit)

- **No credit rating and no CDS spread** — not applicable; HUBS has no rated debt.
- **No revolver capacity or covenant package disclosed** in the available data. Immaterial given zero funded debt, but unverified.
- **Price series is 9 months stale relative to fundamentals.** All market-risk metrics (vol, beta, drawdown, Sharpe) end 2026-02-20. Current EV multiples are computed on that stale $233.50 price and should be treated as directional only.
- **R&D line is derived**, not reported (inferred as revenue − COGS − SGA − operating income = $906.3M TTM).
- **Sector peer set returned is unusable** for comparability — the screener surfaced AAPL, MSFT, NVDA, TSM, AVGO, SKHY, AMD, MU (mega-cap hardware/semis), not application-software comps. **No peer multiples computed; no relative-valuation claim is made.**
- **Cash-flow statement does not isolate restructuring charges**, so the 2026 cost-cut impact on one-time cash items is unquantified.

**Bottom line:** This is not a credit story — it is a *valuation* story. The balance sheet is among the strongest in software: $1.07bn net cash, no debt, no maturities, FCF of $774M. The company would survive a 20% revenue decline without touching its credit profile. What has been destroyed is not solvency but the equity risk premium: a 79% drawdown on 60% volatility, with true (SBC-adjusted) cash generation roughly one-quarter of headline FCF. Monitor gross margin, quarterly revenue growth, and the SBC ratio — those three, not leverage, determine whether the de-rating is complete.
