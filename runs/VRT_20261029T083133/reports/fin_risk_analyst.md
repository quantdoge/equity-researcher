# Fin Risk Analyst

- Symbol: VRT
- Elapsed: 74.7s

---
## VRT (Vertiv Holdings) — Financial Risk Assessment
*Data as of 2026-10-29. Latest financials: Q3'26 (filed 2026-10-28). All TTM figures computed from Q4'25–Q3'26.*

⚠️ **Critical framing note:** The automated ratio tools return **FY2025 (12/31/25) period-end values**, which are now four quarters stale. Vertiv has since (a) IPO'd into investment-grade status, (b) moved from net debt to **net cash**, and (c) grown revenue 28% TTM / 61% in the latest quarter. I present both the tool output and my recomputation on current data; **conclusions are driven by current data.**

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (strong)**

**Rating: Investment Grade.** Confirmed by S&P/Moody's/Fitch upgrades of one notch each in Feb 2026, to **Baa3 / BBB- / BBB**; Fitch **revised outlook to Positive in Aug 2026** and assigned BBB to the senior secured term loan. This is a genuine crossover credit, and the direction of travel is upward, not deteriorating.

The Feb 2026 refinancing significantly de-risked the capital structure: **$2.1B senior unsecured notes + $2.5B senior unsecured revolver**, plus a **2056 maturity note at 5.80%**. This creates a *long-dated* maturity ladder — there is **no refinancing cliff** in the next several years. The term loan's rate step-up beginning Sept 2026 is a minor cost, not a solvency event.

Interest expense has collapsed from $180.1M (FY23) → $150.4M (FY24) → $86.1M (FY25) → **$40.5M TTM**, and just $6.4M in Q3'26 alone. Coverage is now effectively unlimited.

**Verdict: default risk is de minimis over any realistic horizon.** The refinancing-cliff and covenant-breach risks that normally dominate this section simply do not apply here.

## 2. Key Financial Risk Metrics

| Metric | FY2025 (tool) | **Q3'26 TTM (my calc)** | Assessment |
|---|---|---|---|
| Total debt | $3,228M | $3,268M | Flat; refinanced to unsecured |
| Cash | $1,828M | **$3,712M** | Doubled |
| **Net debt** | $1,400–1,500M | **–$245M (net cash)** | ✅ Excellent |
| Net debt / EBITDA | 0.66x | **–0.08x** | ✅ Net cash |
| Total debt / EBITDA | 1.51x | 1.08x | ✅ Very low |
| Debt / equity | 0.82x | **0.59x** | ✅ |
| Debt / assets | 0.26x | 0.18x | ✅ |
| **Interest coverage (EBIT/int)** | 22.0x | **65.5x** | ✅ |
| Current ratio | 1.55 | **1.39** | ⚠️ Weakening |
| Quick ratio | 1.22 | **1.01** | ⚠️ At the line |
| Cash ratio | 0.41 | 0.43 | ✅ |
| Working capital | $2,413M | $3,413M | ✅ |
| Altman Z-Score | **1.97 (Grey)** | **1.89 book / ~6.06 mkt-cap** | See note |
| Piotroski F-Score | **6 / 9** | 6 | Moderate |
| FCF yield | 1.99% | **3.33%** | Thin for the multiple |
| FCF margin | 18.5% | 23.8% | ✅ Improving |

**On the Altman Z-Score:** the 1.97 "Grey zone" reading is a **methodological artifact, not a distress signal.** The tool's X4 uses *book* equity ($3.9B). Using market capitalization ($93.5B) instead, X4 = 7.4 and the Z-Score jumps to **~6.06 — deep safe zone**. A company with net cash and 65x coverage is not a grey-zone credit. I weight this metric near zero.

**Piotroski 6/9** is a fair-to-good score, with the deductions being **F7 (dilution), F8 (gross margin), F9 (asset turnover)**. The F8/F9 failures are the *expected* signature of rapid growth — margins compress and asset turnover falls when you scale a business this fast — not evidence of deterioration. F1–F6 all pass.

## 3. Market Risk Profile — **this is where the risk actually lives**

| Metric | Value | Assessment |
|---|---|---|
| Annualised volatility (252d) | **71.0%** | 🔴 Extreme — ~3.5x market |
| Beta vs SPY (252d) | **2.82** | 🔴 Very high |
| Beta (5y, profile) | 2.05 | 🔴 High |
| Max drawdown (tool, 252d) | **–48.3%** | 🔴 Severe |
| Sharpe ratio | 0.945 | 🟡 Mediocre for the vol taken |
| Price (2026-10-28) | $242.94 | +16.5% single-day jump |

**Observed drawdown (verified from daily prices):** peak close **$376.07 (2026-05-14)** → trough close **$194.32 (2026-10-23)** = **–48.3%**, confirmed independently. Note it also fell to $149.73 intra-year (Dec 2025) — this stock has traded a ~2.5x range within twelve months.

The **Sharpe of 0.945** is the damning number: you are absorbing 71% volatility to earn a sub-1.0 risk-adjusted return. The Sortino would be somewhat better given the sharp upside recoveries, but the point stands — **this is a high-beta, long-duration momentum equity, not a compounder with stable risk-adjusted returns.**

**Macro overlay (yield curve, 2026-10-29):** 2Y 4.65%, 5Y 4.80%, **10Y 4.99%, 30Y 5.37%**, spread +0.34 (no inversion). A 30Y at 5.37% is a direct headwind for a security trading at ~45x earnings — rising long rates compress exactly this kind of multiple.

**Note on data gaps:** the `calculate_price_volatility` tool **ignored the `window_days` parameter** on retry and returned the identical 252-day figure both times. I therefore could not compute a true 3-year beta/max drawdown; the 48.3% figure is 1-year. Three-year drawdown would likely be *larger* given the 2022 de-rating.

## 4. Downside Scenario Analysis — Revenue –20%

Model (TTM base): revenue $13,117M, gross margin 38.1% (COGS 61.9% variable), SG&A 15.0% of sales split ~50/50 fixed-variable, D&A ~$377M, tax 21%.

| Line item | TTM Actual | **–20% Revenue** | Change |
|---|---|---|---|
| Revenue | $13,117M | **$10,493M** | –20.0% |
| Gross profit (38.1%) | $4,999M | $4,001M | –20.0% |
| SG&A | $1,970M | $1,772M | –10.1% |
| **EBITDA** | $3,029M | **$2,229M** | **–26.4%** |
| **EBIT** | $2,652M | $1,852M | –30.2% |
| Interest expense | $40.5M | $45M | +11% |
| **Interest coverage** | 65.5x | **41.1x** | ✅ Still exceptional |
| Net income | $2,098M | **$1,428M** | –31.9% |
| **FCF** | $3,117M | **~$1,500M** | –52% (WC release offsets) |
| **Net debt / EBITDA** | –0.08x | **–0.11x** | ✅ Stays net cash |
| Net debt / EBITDA @ –40% rev | — | **–0.17x** | ✅ Still net cash |

**The central conclusion of this report:** even at **–20% revenue**, Vertiv retains **41x interest coverage, a net cash balance sheet, and ~$1.5B of positive free cash flow.** At a **–40%** revenue shock it *still* generates roughly **$700M+ FCF** and 26x coverage. **Vertiv cannot be killed by an operating downturn.** There is no plausible demand scenario that threatens its solvency.

**But the equity is a different question.** The vulnerability is entirely in the *multiple*:
- If EBITDA falls 26% to $2,229M and the market re-rates a decelerating industrial from ~31x to ~20x EV/EBITDA, EV = $44.6B → **equity value ≈ $44.8B, or roughly –52% from today's $93.5B.**
- Add multiple compression from the 5.37% 30-year yield and the downside case is **–50% to –60% on the stock, with a perfectly healthy balance sheet.**
- This is precisely what the –48% May–October drawdown already demonstrated: the equity halved while fundamentals *improved* every quarter.

**The risk is valuation risk, not credit risk.** Do not confuse the two.

## 5. Overall Financial Risk Rating: **LOW**

On the dimensions I am chartered to assess — solvency, liquidity, covenant, refinancing, tail-risk of impairment — Vertiv scores **LOW**. Net cash, 65x coverage, investment-grade ratings on positive outlook, a maturity ladder out to 2056, and a downside model that never breaches net cash. A –20% revenue shock is comfortably survivable.

I explicitly flag that this **LOW financial-distress rating coexists with a very HIGH equity-market risk** (71% vol, 2.82 beta, –48% demonstrated drawdown, 31x EV/EBITDA). Those are not contradictory; they are the defining feature of the name.

## 6. Key Red Flags

1. 🔴 **Valuation / duration risk is the dominant risk, not leverage.** ~31x EV/EBITDA and ~45x TTM P/E with a 3.33% FCF yield. A 71% vol, 2.82-beta stock with a Sharpe below 1.0. Any growth disappointment or rate move produces 30–50% drawdowns, as already occurred.

2. 🟠 **Working-capital build is deteriorating sharply — the single most important fundamental warning.** Inventory has risen **126% YoY** ($1,456M → $3,288M) against revenue growth of only 28%. **Days inventory outstanding has blown out from ~82 days to ~148 days.** Days sales outstanding rose from ~111 to ~122. This drove the current ratio down from 1.55 to 1.39 and the quick ratio to **1.01 — right at the line.** This may be legitimate pre-build against an order book growing >100% organic, but if the AI/data-center capex cycle rolls over, **this inventory becomes a writedown**, and it is the transmission mechanism by which a demand shock hits the P&L.

3. 🟠 **Current liabilities nearly doubled (+98%) to $8,711M** against current assets +63%. Liquidity headroom is thinner than the large cash balance suggests.

4. 🟡 **Extreme single-customer/end-market concentration** by inference: revenue is levered to hyperscale AI data-center capex. Orders growing >100% is a boom signal that cuts both ways — order growth of that magnitude is inherently mean-reverting, and the backlog is only as good as the hyperscalers' willingness to fund it.

5. 🟡 **Piotroski F-Score 6/9**, failing on dilution (share count still creeping: 381.7M → 392.7M diluted), gross margin, and asset turnover. The latter two are growth artifacts; the dilution is real but modest (SBC only ~$58M TTM, ~0.8% of revenue — genuinely low).

6. 🟡 **Data quality flag:** D&A is inconsistent across quarters (Q3'26 $39.8M vs Q2'26 $115.8M vs Q1'26 $107.7M). Interest expense of **$0** reported in Q1'26 is clearly a placeholder. These do not change conclusions at the scale of the margin of safety here, but the quarterly EBITDA series should not be taken at face value.

**Explicit data gaps:** (a) true 3-year max drawdown/beta unavailable — tool ignored `window_days`; (b) no detailed debt maturity schedule by year obtained (mitigated by the 2026 refinancing and 2056 notes confirming no near-term cliff); (c) no peer multiple comparison — the sector-peer endpoint returned mega-caps (CAT, GE, RTX) that are not meaningful comparables for a data-center electrical equipment pure-play; (d) no covenant package detail.

---

**Bottom line for the investment memo:** Vertiv is a **financially fortress-like company wrapped in a fragile stock.** On every solvency, liquidity, and credit metric it is investment grade or better, with genuine balance-sheet improvement (net debt $1.5B → net cash $245M) funded by real, rising free cash flow ($3.1B TTM, 23.8% margin). It would survive a severe demand shock intact. **The risk an investor is actually underwriting is a 50%+ equity drawdown from multiple compression** — already demonstrated once this year — compounded by a ballooning inventory position that is the visible seam where an AI capex slowdown would first show up. Size positions against the 71% volatility and 2.82 beta, not against the balance sheet.
