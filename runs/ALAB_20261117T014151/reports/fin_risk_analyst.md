# Fin Risk Analyst

- Symbol: ALAB
- Elapsed: 89.5s

---
# ALAB — Astera Labs, Inc. | Complete Financial Risk Assessment

**Sector:** Technology / Semiconductors — AI data-centre connectivity (Aries/Leo/Scorpio)
**Price:** $202.34 | **Market cap:** ~$35.4B | **IPO:** 20-Mar-2024 | **Employees:** 756

> **⚠️ Data currency warning:** the price-history feed returned data only through **2026-02-20** ($129.68 close), while the company profile, financials and web sources place the current date near **Nov-2026**. All market-risk statistics computed by the tools (vol, beta, drawdown, Sharpe) are therefore measured over a **stale 365-day window** and *materially understate* present risk. I flag each affected metric below. Fundamental data (FY2025 annual, Q1–Q3 2026 quarterly) is current.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade (effectively net-cash, unrated)**

ALAB has essentially **no funded debt**. FY2025 total debt of $35.1M consists of lease obligations; long-term and short-term debt lines are both **$0**. Against $1,188.8M of cash and short-term investments, the company carries **net cash of ~$1,154M** (net debt/EBITDA of **−5.13x**).

There is no interest expense (interest coverage returns `null` — this is the *absence* of debt service, not a data gap), **no debt maturity schedule, and no refinancing cliff**. CDS spreads and agency ratings are unavailable/not applicable (unrated). Altman Z-Score of **6.86** sits deep in the safe zone, and that figure is conservative because it uses *book* equity ($1.36B) rather than the $35.4B market value — substituting market cap pushes x4 to ~210 and the Z-score far higher.

The only genuine credit observation is that **total liabilities grew 87% YoY** ($89.7M → $168.2M) as deferred revenue and payables scaled — a growth artifact, not leverage.

---

## 2. Key Financial Risk Metrics

| Metric | FY2024 | FY2025 | LTM (to Q3'26) | Assessment |
|---|---|---|---|---|
| Revenue | $396.3M | $852.5M | $1,556.3M | +115% / +~150% YoY — hyper-growth |
| Gross margin | 76.4% | 75.7% | 73.9% | **Contracting** (Q3'26: 72.3%) |
| Operating margin | −29.3% | 20.3% | 25.5% | Strong inflection to profit |
| EBITDA | −$78.6M | $225.0M | ~$450M | Turned positive FY25 |
| Net income | −$83.4M | $219.1M | $461.3M | Includes ~$45M interest income |
| **Debt / Equity** | 0.00 | **0.03** | ~0.03 | Negligible |
| **Net debt / EBITDA** | net cash | **−5.13x** | net cash | Net cash position |
| **Interest coverage (EBIT/int.)** | n/a | **n/a (no debt)** | n/a | No debt service burden |
| Debt / Assets | 0.00 | **0.02** | ~0.02 | Negligible |
| **Current ratio** | 11.71 | **10.24** | ~10x+ | Exceptional |
| **Quick ratio** | 11.21 | **9.79** | — | Exceptional |
| Cash ratio | — | **8.94** | — | Exceptional |
| Working capital | $927M | **$1,229M** | — | Deeply positive |
| **Altman Z-Score** | — | **6.86 (Safe)** | — | >2.99 threshold |
| **Piotroski F-Score** | — | **6 / 9 (Moderate)** | — | See flags |
| CFO | $136.7M | $319.3M | $519.5M | Strong |
| **FCF** | $102.4M | $281.8M | $344.7M | Positive, scaling |
| FCF margin | 25.8% | 33.1% | 22.2% | Deteriorating on WC drag |
| **SBC** | $234.6M | $160.0M | $236.9M | **18.8% of revenue (FY25)** |
| Cash & ST inv. | $914.3M | $1,188.8M | ~$1.45B est. | Fortress |
| Total equity | $964.8M | $1,363.6M | — | Equity/assets 0.89 |

**Piotroski decomposition (6/9):** scored on positive ROA, positive CFO, ROA improvement, accruals quality, positive equity change, asset-turnover improvement. **Lost points on:** F5 leverage/liquidity (rising liabilities), **F7 no-dilution (failed — share count 131M → 175M)**, F8 gross-margin improvement (failed).

---

## 3. Market Risk Profile

| Metric | Value | Note |
|---|---|---|
| Annualised volatility | **99.95%** | ~5–6x a broad index — extreme |
| Beta vs SOXX | **1.48** | Computed over stale window |
| Beta vs broad market | **3.86** (profile) | Implies ~4x market drawdown sensitivity |
| Max drawdown (365d window) | **−62.8%** | Stale window; see actual below |
| Sharpe ratio (rf = 0%) | **0.741** | Mediocre for the risk taken |
| FCF yield (reported) | **0.78%** | On FY25 FCF / $36.3B cap |
| **LTM FCF yield (adjusted)** | **~0.97%** | $344.7M / $35.4B |
| **SBC-adjusted FCF yield** | **~0.30%** | $107.8M / $35.4B — the true number |
| EV / LTM revenue | **~22x** | EV ≈ $34.2B |
| P/E (LTM) | **~77x** | On $461M LTM net income |

**Realised drawdown history is worse than the computed figure.** Since the Mar-2024 IPO the stock has suffered **two separate >50% peak-to-trough declines**:
- Peak $145.81 (26-Dec-24) → $52.94 (4-Apr-25): **−63.7%**
- Peak $251.88 (18-Sep-25) → $123.69 (17-Feb-26): **−50.9%**, including a **−31% two-day collapse** on 11–12 Feb 2026 (16.4M and 11.4M shares — ~5x normal volume)
- Post-recovery, the stock reached ~$290 before falling **−19.6% in a single session on 5-Nov-2026** on Q3-2026 results, settling at the current $202.34.

This is a **high-torque, narrative-driven equity** where single-day 20–30% gaps are routine. Position-sizing risk dominates balance-sheet risk by an order of magnitude.

---

## 4. Downside Scenario Analysis (revenue −20%)

Base = LTM to Q3'26: Revenue $1,556M, gross margin 73.9%, opex $753M, EBIT $397M.

| Scenario | Revenue | GM | EBIT | EBIT margin | Net income | FCF | Cash runway |
|---|---|---|---|---|---|---|---|
| **Base (LTM)** | $1,556M | 73.9% | $397M | 25.5% | ~$461M | $345M | Infinite |
| **−20% rev** | $1,245M | 72% | $144M | 11.5% | ~$164M | ~$150M | Infinite |
| **−20% + GM to 68%** | $1,245M | 68% | $94M | 7.5% | ~$130M | ~$110M | Infinite |
| **−40% rev** | $934M | 68% | −$43M | −4.6% | ~−$20M | ~breakeven | >15 yrs |
| **−50% + GM 60%** | $778M | 60% | −$211M | −27% | ~−$180M | ~−$100M | >10 yrs |

**Conclusion:** a 20% revenue decline is **entirely survivable** — the company remains solidly profitable (~11% EBIT margin) with FCF still positive. Even a 50% revenue collapse with severe margin compression produces only ~$100M of annual cash burn against **$1.19B+ of cash and zero debt** — a decade-plus of runway without touching capital markets.

**This is not a solvency story; it is an equity-duration story.** The damage in a downside scenario is borne by the *multiple*, not the balance sheet. At 22x LTM sales, a 20% revenue miss plus multiple compression to 8x sales would imply an ~**$11B enterprise value — a ~65% equity decline** from $35.4B. Note the Feb-2026 precedent: the stock fell 51% *while fundamentals were accelerating*.

---

## 5. Overall Financial Risk Rating

# MODERATE
### (barbell: **LOW** balance-sheet/solvency risk | **VERY HIGH** market & equity risk)

The rating is genuinely bifurcated and should be read that way:

- **Solvency / credit / liquidity: LOW.** Net cash $1.15B, D/E 0.03, current ratio 10.2, Z-score 6.86, no maturities, positive FCF. This company cannot go bust from leverage in any realistic scenario. Effectively an **Investment Grade** balance sheet.
- **Market / valuation / dilution: VERY HIGH.** ~100% vol, beta 3.86 vs market, repeated 50–64% drawdowns, ~77x earnings, ~22x sales, ~0.3% SBC-adjusted FCF yield. There is no valuation cushion whatsoever.

If forced to a single word for an equity-holder's risk of permanent capital loss, I would lean **High**; for a credit-holder or lender, **Low**.

---

## 6. Key Red Flags

1. **Systematic dilution — the largest single red flag.** Share count has gone 131M (2023) → 166M (2025) → 175M (Q3'26), **+33%**. SBC was $160M in FY2025 (18.8% of revenue) and is *accelerating*: $48.9M → $64.0M → $82.6M across Q1–Q3'26, an annualised run-rate near **$330M**. Piotroski F7 = 0. Management is paying employees in equity at a rate that consumes roughly a fifth of the top line.

2. **FCF quality is poor.** LTM reported FCF of $344.7M is flattered by a $236.9M non-cash SBC add-back — **69% of reported FCF is stock compensation**. Economic (owner) FCF is **~$108M**, a **0.30% yield** on a $35.4B cap. The reported 0.78–0.97% FCF yield overstates cash generation by ~3x.

3. **Extreme, repeated drawdowns.** −63.7% and −50.9% peak-to-trough within 24 months; −31% in two days (Feb-26); −19.6% in one day (Nov-26). Beta of 3.86 vs the market means a 10% index decline plausibly costs ALAB ~38%.

4. **Severe customer concentration.** The 10-K and 10-Qs explicitly identify *"our customer concentration, with a limited number of end customers driving our revenue"* as a principal risk — the customer base is a handful of hyperscalers and their ODM/system-integrator supply chains. (Exact percentage disclosure not retrieved — **data gap**.) Loss or in-sourcing of a single AI-platform program is a growth-story-ending event, and the Feb-2026 and Nov-2026 selloffs are consistent with the market pricing exactly that risk.

5. **Gross margin is compressing into the growth.** 76.4% (FY24) → 75.7% (FY25) → 73.3% (Q2'26) → **72.3% (Q3'26)**. Mix shift toward larger-volume Scorpio fabric systems and/or competitive pricing. F8 = 0. If this continues, the operating leverage thesis inverts.

6. **Cash conversion deteriorating.** Working-capital drag of **−$143.5M** (Q2'26) and **−$115.8M** (Q3'26) as receivables and inventory scale. FCF margin fell from 33.1% (FY25) to 22.2% LTM despite revenue nearly doubling — the cash engine is not scaling with the P&L.

7. **Earnings quality relies on two fading props.** FY2025 net income of $219.1M sits *above* EBIT of $218.2M and far above operating income of $173.4M, because of ~$45M of interest income on the cash pile (~20% of net income) and a near-zero effective tax rate from NOL shields. Lower rates and NOL exhaustion both compress reported EPS independent of operations.

8. **Valuation leaves no room for error.** ~22x LTM sales and ~77x LTM earnings with a sub-1% (sub-0.5% adjusted) FCF yield. The equity is priced for flawless execution of a concentrated, single-architecture AI buildout.

---

## Data Gaps & Caveats (explicit)

- **Price history is stale** (ends 2026-02-20). All computed vol/beta/drawdown/Sharpe figures are window-misaligned and **understate current risk**; I substituted documented drawdown events from public reporting.
- **No credit rating and no CDS spread** — ALAB is unrated; spread data not available.
- **Customer concentration percentages not retrieved** — qualitative 10-K language only.
- **No peer leverage/coverage comparables pulled.** Peer set (NVDA, AVGO, AMD, MU, TSM) is dominated by mega-caps with mature capital structures and would not be like-for-like for a 2-year-old, $35B-cap growth name.
- **Q1-2025 quarterly detail is missing** from the feed (FY2025 annual is complete and internally consistent).
- Interest coverage is genuinely N/A (zero interest expense), not a failed calculation.
- Cash/EV estimates for LTM periods extrapolate from the 31-Dec-2025 balance sheet; intra-year cash rose with $268M of Q1–Q3'26 FCF, so EV is modestly *overstated* here.

---

**Bottom line for the investment memo:** ALAB presents a **fortress balance sheet attached to a fragile equity**. Credit and liquidity risk are effectively nil — the company could fund operations from cash for a decade in a severe downturn, and no covenant, maturity, or refinancing exposure exists. The financial risk that matters is **dilution (SBC at ~19–21% of revenue) and the absence of any valuation margin of safety in a stock with ~100% volatility that has already twice halved.** Recommendation from a risk standpoint: size positions to survive a 50% drawdown as a base-case-permissible event, and treat reported FCF as roughly one-third of headline.
