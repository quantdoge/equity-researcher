# Fin Risk Analyst

- Symbol: DT
- Elapsed: 70.6s

---
## DYNASTRACE, INC. (NYSE: DT) — Financial Risk Assessment
*Pricing/data as of Nov 4, 2026 fiscal year-end Mar 31, 2026. Market cap $13.52B, price $46.78.*

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (effectively AAA-quality balance sheet)**

DT carries **net cash** and generates free cash flow at 26% of revenue. There is no meaningful refinancing risk, no near-term maturity wall, and no financial covenant stress.

| Evidence | Value |
|---|---|
| Cash & ST investments | $1,172.1M |
| Total debt (as reported) | $164.3M |
| Net debt | **–$1,007.8M (net cash)** |
| Net debt / EBITDA | **–3.11x** |
| Interest expense | $0 (FY24–FY26 all reported 0) |
| Debt / assets | 4% |

**Interest coverage is effectively infinite** — the reported $0 interest expense is consistent with a zero-coupon exchangeable-notes structure (see Data Gap #1). Interest-rate risk on the debt stack is therefore ~nil.

⚠️ **Important data caveat:** the FY2025–FY2026 SEC filings reference *outstanding 2031 exchangeable notes* and a new **$400M senior secured revolver** (signed Sept 24, 2026, maturing **June 2031**, $399.0M undrawn, $1.0M LCs outstanding). The FMP balance sheet shows `long_term_debt = 0` and `short_term_debt = 0`, which is **inconsistent** with notes that maturities-reference 2031. Most likely FMP is excluding the exchangeable notes from the debt line (a common vendor quirk).

**Bounding the gap:** if the 2031 notes are $750M, gross debt ≈ $914M → gross debt/EBITDA ≈ 2.8x, and DT still holds **~$258M net cash**. At $1.0B, net cash ≈ breakeven. **The conclusion — net-cash, no covenant risk — holds across the entire plausible range.**

---

### 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | Read |
|---|---|---|---|---|
| Revenue ($M) | 2,018.4 | 1,698.7 | 1,430.5 | +18.8% y/y (2-yr CAGR 18.8%) |
| Gross margin | 81.6% | 81.2% | 81.4% | Stable, best-in-class |
| Operating income ($M) | 263.9 | 179.4 | 128.4 | **+47% y/y** |
| Operating margin | 13.1% | 10.6% | 9.0% | Expanding |
| Net income ($M) | 162.7 | 483.7 | 154.6 | ⚠️ –66% (see below) |
| OCF ($M) | 559.4 | 459.4 | 378.1 | +22% |
| FCF ($M) | 527.2 | 433.3 | 351.7 | +22% |
| **FCF margin** | **26.1%** | 25.5% | 24.6% | **Improving** |
| FCF yield | 3.77% | — | — | vs 10Y UST 5.13% |
| Debt/Equity | 0.06 | 0.03 | — | Negligible |
| Interest coverage | n/a (no interest) | n/a | n/a | Infinite |
| **Current ratio** | **1.35** | 1.40 | — | Understated (see below) |
| **Quick ratio** | **1.35** | — | — | No inventory — clean |
| Cash ratio | 0.75 | 0.81 | — | Strong |
| Working capital | $554.4M | $550.2M | — | Positive |
| Cash / liabilities | 0.65 | — | — | Strong |
| **Altman Z-Score** | **1.842 (Grey)** | — | — | ⚠️ Artifact — see below |
| **Piotroski F-Score** | **6 / 9 (Moderate)** | — | — | ⚠️ Artifact — see below |
| Equity / assets | 0.59 | 0.63 | — | Post-buyback |
| Goodwill + intangibles | $1,371.3M | $1,362.0M | — | **31% of assets, 52% of equity** |

**Net income –66% is not deterioration.** FY2025's $483.7M included an outsized non-recurring tax benefit (implied effective rate far below normal). FY2026 EBIT was $299.8M vs $223.4M prior — **operating profit rose 47%**. Judge this company on EBIT/FCF, not net income.

**Altman Z of 1.842 is a structural artifact, not a distress signal.** The score is dragged down by X3 (EBIT/TA = 6.8%) — a mechanical consequence of a $4.4B asset base dominated by goodwill and receivables, typical of asset-light software. X4 (book equity/liabilities = 1.447) carries the score. A company with $1.0B net cash is not a bankruptcy candidate; **the Z-score is not informative here.**

**Piotroski 6/9 is likewise understated.** The three failed tests — lower leverage (F5), positive equity change (F6), ROA improvement (F3) — are all downstream of the **$478.7M share repurchase** in FY2026. Burning cash to retire equity mechanically raises leverage and lowers book equity. That is a capital-allocation decision, not credit stress. The four profitability tests and accruals quality (F4) all pass, and FCF conversion of net income is a healthy 3.2x.

**Current ratio 1.35 materially understates liquidity.** Current liabilities of $1,569.4M are dominated by **deferred revenue** — a non-cash, customer-prepaid obligation that is economically favorable. Ex-deferred revenue, liquidity is very strong. **Data gap:** deferred revenue is not separately disclosed in the extract, so the adjusted ratio cannot be computed.

---

### 3. Market Risk Profile — *this is the real risk in DT*

| Metric | Value | Assessment |
|---|---|---|
| Annualised volatility (3y) | **38.7%** | Very high |
| Beta vs SPY | **0.90** (3y calc) / 0.769 (profile) | ⚠️ **Misleadingly low** |
| **Max drawdown (3y)** | **–48.2%** | Severe |
| Sharpe ratio | **0.098** | **Near-zero risk-adjusted return** |
| Sortino ratio | not available | Data gap |
| 3-year price return | $44.40 → $46.78 = **+5.4% cumulative (~1.8%/yr)** | ~Zero |
| Drawdown from Oct 13, 2026 peak ($66.30) | **–29.4%** | Ongoing |
| Single-day move Nov 3, 2026 | **–14.7%** ($55.13 → $47.03, 22.6M shares) | Guidance cut |

**Beta is the wrong lens for DT.** At 0.77–0.90 the stock screens as defensive, but the realized drawdown history says otherwise: **two separate ~30–50% drawdowns within 18 months** (a –48.1% peak-to-trough from Feb 2025's $62.38 to Apr 2026's $32.36, and now –29.4% since Oct 2026). Nearly all of this is **idiosyncratic**, so beta understates tail risk. Downside is driven by earnings revisions, not market direction.

**Sharpe of 0.098 over three years is the headline finding:** investors took 38.7% volatility and a 48% drawdown to earn roughly 1.8% annualized. Risk-adjusted return quality is **poor**.

**Catalyst:** On Nov 3, 2026 DT **trimmed EPS guidance** while *raising* revenue guidance (FY revenue midpoint $2.34B from $2.31B; Q2 ARR $2.207B, +16%; Q2 revenue $580M). The market is no longer paying for growth alone — it is penalizing **margin/EPS conversion**. With the 10Y at **5.13%** (2s10s +39bp, no inversion), long-duration software cash flows face structural multiple compression. **Duration risk, not credit risk, is the dominant exposure.**

---

### 4. Downside Scenario: Revenue –20%

Base FY2026: revenue $2,018.4M, gross margin 81.6%, total opex $1,382.2M (SG&A $907.9M + R&D ≈$474.3M), operating income $263.9M.

**Assumptions:** gross margin holds at 81.6% (software has near-zero marginal cost; history supports this); management cuts SG&A 10% and R&D 8% within 12 months.

| Line | Base | –20% Stress | Change |
|---|---|---|---|
| Revenue | $2,018.4M | $1,614.7M | –$403.7M |
| Gross profit (81.6%) | $1,646.1M | $1,317.6M | –$328.5M |
| SG&A (–10%) | $907.9M | $817.1M | –$90.8M |
| R&D (–8%) | $474.3M | $436.4M | –$37.9M |
| **Operating income** | **$263.9M** | **$64.1M** | **–$199.8M** |
| Operating margin | 13.1% | **4.0%** | –9.1pp |
| EBITDA (approx.) | $288.0M | $88.2M | –69% |
| Gross debt / EBITDA | 0.6x | **1.9x** | Still comfortable |
| **FCF (approx.)** | **$527.2M** | **~$350–390M** | **–26% to –34%** |
| FCF margin | 26.1% | ~22–24% | Resilient |
| Cash | $1,172.1M | ~$1,500M+ | **Rises** (FCF positive) |
| Net debt | –$1,008M | **~–$1,350M** | Improves |

**Deeper stress (–35% revenue):** revenue $1,312M, gross profit $1,070.6M vs opex near the floor of ~$1,100M → operating income roughly **breakeven to –$30M**; FCF still ~$250M. **DT remains net cash and solvent.**

**Conclusion: DT cannot be killed by a revenue downturn.** There is no cash burn to fund, no maturity wall, no covenant to breach. Cash runway is effectively **infinite** — a 20% revenue decline *increases* the cash balance. The 20% shock is an **EPS and multiple event, not a solvency event**: operating income falls ~$200M and the equity would likely de-rate 30–50% (the stock already fell 48% on far less). Note also that Goodwill + intangibles of $1,371M (52% of equity) could trigger an impairment charge in a prolonged growth stall — a book-equity hit, not a cash hit.

---

### 5. Overall Financial Risk Rating: **LOW (balance-sheet) / MODERATE-HIGH (equity)**

**Balance-sheet and credit risk: LOW.** Net cash of $1.0B, 26% FCF margin, 18.8% revenue CAGR, 81.6% gross margin, zero interest burden, zero near-term maturities, and a $399M undrawn revolver maturing 2031. Covenant breach probability is negligible.

**Equity and market risk: MODERATE-HIGH.** 38.7% volatility, a 48.2% max drawdown, a Sharpe of 0.098, a fresh –29.4% decline, and a management team that just cut EPS guidance. The risk to an equity holder is **valuation and earnings-revision risk, not financial distress**.

**Blended rating: LOW-to-MODERATE financial risk.** The correct framing for the investment memo: *"A fortress balance sheet attached to a volatile, de-rating equity. Own it for the cash-flow floor, not for downside protection in the price."*

---

### 6. Key Red Flags

1. **Margin/EPS guidance cut on Nov 3, 2026.** Revenue guidance was raised but EPS guidance trimmed — a decoupling of growth from profit conversion. Stock –14.7% in one session on 22.6M shares (3x normal volume). **This is the most important forward signal in the dataset.**
2. **Two ~30–50% drawdowns in 18 months.** Max DD 48.2%; Sharpe 0.098. The equity offers no risk-adjusted compensation for its volatility.
3. **Debt composition is unresolved (critical data gap).** FMP reports total debt of $164.3M and long-term debt of $0, yet SEC filings reference **outstanding 2031 exchangeable notes**. At $750M–$1.0B outstanding, gross leverage is 2.7–3.5x rather than 0.6x. Net cash position survives either way, but reported debt/equity of 0.06 **should not be relied upon**.
4. **Free cash flow is not adjusted for stock compensation.** FY2026 SBC is reported as **$0** in the cash flow statement (vs $271.7M in FY2025 and $208.9M in FY2024) — almost certainly a data error. If true SBC is ~$280M, **SBC-adjusted FCF is ~$250M, not $527M**, and the true FCF yield is **~1.8%, not 3.77%** — well below the 5.13% risk-free rate. This materially weakens the valuation case.
5. **Goodwill + intangibles at $1,371M = 52% of equity.** D&A collapsed from $54.9M (FY24) to $24.1M (FY26), indicating acquisition amortization is largely run off while gross goodwill remains. Impairment risk rises sharply if ARR growth decelerates below mid-teens.
6. **$478.7M of buybacks in FY2026** (~3.5% of market cap) reduced equity, raised book leverage, and cut the Piotroski score. Buying back stock at $50–65 into a 48% drawdown is a **capital-allocation red flag** on top of the FY2025 EPS-dilution test failure.
7. **Duration risk under a 5.13% 10-year.** DT's value is long-dated growth; with the 10Y at 5.13%, the discount-rate headwind is structural and is precisely what has driven the de-rating.

**Explicit data gaps:** (a) exchangeable-notes principal amount and terms — 2031 maturity, coupon unknown; (b) interest expense reported as $0 (consistent with zero-coupon notes but unverified); (c) SBC in FY2026 cash flow ($0 — implausible); (d) Sortino ratio not computable; (e) no credit rating or CDS spread available from tools; (f) deferred revenue not separately disclosed, so liquidity cannot be fully adjusted; (g) D&A of $24.1M is inconsistent with EBITDA of $323.8M — EBITDA may be on a different definition than the reported D&A.

**Bottom line:** DT's credit risk is de minimis and the company would survive a 20% (or 35%) revenue decline with cash to spare. **The risk in this security is entirely in the equity: expensive, volatile, mid-de-rating, and with cash generation quality overstated by the SBC reporting.** Price the downside at a 40–50% multiple compression on an EPS guide-down, not at impairment of the balance sheet.
