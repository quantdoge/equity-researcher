# Fin Risk Analyst

- Symbol: FN
- Elapsed: 94.4s

---
I have sufficient data across credit, liquidity, cash flow, market risk, and customer concentration. Writing the assessment now.

---

# FINANCIAL RISK ASSESSMENT — FABRINET (NYSE: FN)

**Sector:** Technology / Hardware, Equipment & Parts (optical & electro-mechanical contract manufacturing) · **Domicile:** Cayman Islands (manufacturing in Thailand) · **FY end:** June · **Latest FY:** FY2026 (ended 2026-06-26) · **Market cap:** ~$13.0B (data snapshot) / ~$15.2B at latest close $424.27

> **Data-staleness note:** the profile snapshot quotes $363.33 while the latest close in the price history (2026-09-30) is $424.27. Metrics derived from market cap (FCF yield) are computed on the snapshot cap; I re-derive ratios at the current price where material. Two tool inconsistencies are flagged in §7.

---

## 1. Credit Risk Assessment

### Rating: INVESTMENT GRADE (de facto — unrated, zero-debt capital structure)

Fabrinet carries **$4.0M of total debt against $875.1M of cash and short-term investments** — net cash of **$871.0M**, or roughly 6.7% of market capitalisation. Long-term debt is **$0**. This is not a leveraged credit in any meaningful sense; there is no bond, no revolver draw, no term loan, no CDS to price.

- **No refinancing cliff.** Total debt maturing is immaterial ($1.19M short-term). There is no maturity wall in any year.
- **No covenants to breach.** With no funded debt, the standard covenant package (net leverage, interest coverage, minimum liquidity) does not exist.
- **Interest coverage: 5,510×** (EBIT $555.2M / interest expense $0.084M). This number is economically meaningless — it simply confirms interest cost is a rounding error.
- **Altman Z-Score: 4.12 — Safe zone** (threshold 2.99). Note the tool uses book equity for x4 (1.685), which *understates* the true score; at market equity the Z-score would be materially higher still.
- **Negative net debt/EBITDA of −1.40×** — the company holds more cash than 1.4 years of EBITDA.

Credit deterioration signals: **none**. The balance sheet is structurally over-capitalised. The realistic credit risk here is not default but **capital misallocation** — a 12%-gross-margin manufacturer sitting on $871M of idle cash earning ~4% rather than returning it or compounding it in the business.

---

## 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | Assessment |
|---|---|---|---|---|
| Revenue ($M) | 4,641.1 | 3,419.3 | 2,882.9 | +35.7% YoY |
| Gross margin | **11.99%** | 12.09% | 12.35% | ⚠ Declining 3 yrs running |
| Operating margin | 9.97% | 9.49% | 9.63% | Thin but stable |
| EBITDA ($M) | 623.6 | 408.6 | 360.5 | +52.6% |
| **Total debt ($M)** | **4.0** | 9.2 | 8.6 | Effectively zero |
| **Net debt ($M)** | **(871.0)** | (297.3) | (401.3) | Net cash |
| Debt / equity | **0.16%** | 0.46% | 0.49% | 🟢 |
| Net debt / EBITDA | **−1.40×** | −0.73× | −1.11× | 🟢 |
| Interest coverage | **5,510×** | n/a (no interest) | 2,512× | 🟢 |
| Debt / assets | 0.10% | 0.32% | 0.37% | 🟢 |
| Current ratio | 2.25 | 3.00 | 3.61 | 🟡 Falling (WC build) |
| Quick ratio | 1.52 | 2.28 | 2.78 | 🟡 Falling |
| Cash ratio | 0.62 | 1.15 | 1.54 | 🟡 Falling |
| Working capital ($M) | 1,757.1 | 1,619.0 | 1,454.7 | 🟢 Rising |
| Equity / assets | 62.8% | 70.0% | 74.7% | 🟡 Diluting |
| **Altman Z-Score** | **4.12 (Safe)** | — | — | 🟢 |
| **Piotroski F-Score** | **5 / 9 (Moderate)** | — | — | 🟡 |
| **Operating cash flow ($M)** | **256.7** | 328.4 | 413.1 | 🔴 Declining |
| **Capex ($M)** | **253.7** | 121.8 | 47.5 | 🔴 5.3× in 2 yrs |
| **Free cash flow ($M)** | **3.0** | 206.5 | 365.6 | 🔴 Collapse |
| FCF margin | **0.07%** | 6.04% | 12.68% | 🔴 |
| OCF / Net income | **54.3%** | 98.8% | 139.5% | 🔴 |
| Inventory days | **91.2** | 70.6 | 58.6 | 🔴 +20.6 days |
| DSO | 80.1 | 81.0 | 75.0 | 🟢 Stable |
| Inventory / revenue growth | **2.1×** | — | — | 🔴 See §6 |
| P/E (diluted, at $424.27) | ~32.5× | | | 🔴 |
| EV / EBITDA | ~23.0× | | | 🔴 |

**Piotroski decomposition (5/9):** positive ROA ✓, positive operating CF ✓, ROA improvement ✓, positive equity change ✓, no dilution ✓ — but **accruals quality ✗**, **leverage trend ✗**, **gross margin trend ✗**, **asset turnover trend ✗**. Three of the four failures are *trend* failures, i.e. this is a company whose quality metrics are all inflecting negatively at once even as revenue accelerates. That is the core of the story.

**Asset turnover** declined from 1.208 to 1.187 — the balance sheet is growing faster than the P&L.

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (3yr) | **64.3%** | ~3.9× S&P 500; extreme for a $13–15B cap |
| Beta vs SPY (computed) | **2.18** | Very high market sensitivity |
| Beta (profile field) | 1.345 | ⚠ Materially different — see §7 |
| Max drawdown (3yr, tool) | **−57.8%** | |
| Max drawdown, close-to-close (my calc: $746.47 peak 2026-05-14 → $374.91 trough 2026-09-15) | **−49.8%** | Confirms regime |
| Sharpe ratio (rf=0%) | **0.695** | Respectable return per unit of *total* risk |
| Price vs peak | **−43.2%** from $746.47 close (2026-05-14) to $424.27 (2026-09-30) | Already in a deep drawdown |
| Intraday 3yr high / low | $748.89 / $373.70 | Range of 2.0× |

**Interpretation.** The stock has **already delivered a ~45–50% drawdown** during a period in which the S&P 500 was broadly rising and Fabrinet's own revenue was growing 36%. That is diagnostic: the de-rating is **valuation-driven, not fundamental**. The market is repricing the multiple on a 12%-gross-margin contract manufacturer that had been carried at AI-infrastructure growth multiples.

The high Sharpe (0.695) alongside 64% volatility is the tell — the stock has been a genuine momentum compounder capable of carrying violent drawdowns. That is a *risk profile statement*, not a comfort: a 2.2 beta means a 20% market drawdown mechanically implies a ~44% drawdown in FN, and the observed 50% drawdown demonstrates the beta is real rather than theoretical.

**Gap:** Sortino ratio, CDS spreads, and implied (options) volatility are not available from the toolset.

---

## 4. Downside Scenario Analysis — Revenue −20% / −35%

Modelling assumptions: COGS split 85% variable / 15% fixed (appropriate for a materials-intensive optical contract manufacturer — materials dominate COGS); SG&A 15% variable with modest discretionary cuts. Non-operating income assumed to fade. D&A held at FY26 level.

| Line item | Base FY26 | **−20% revenue** | **−35% revenue** |
|---|---|---|---|
| Revenue | $4,641.1M | $3,712.9M | $3,016.7M |
| Gross profit | $556.5M | $322.7M | $147.3M |
| Gross margin | 11.99% | **8.69%** | **4.88%** |
| SG&A | $93.5M | $88.8M | $87.4M |
| Operating income | $462.9M | **$233.9M** | **$59.9M** |
| Operating margin | 9.97% | 6.30% | 1.99% |
| EBITDA | $623.6M | $302.2M | $128.2M |
| Net income (est.) | $473.0M | ~$239M | ~$61M |
| **Net debt** | **−$871.0M** | **more negative** | **more negative** |
| Interest coverage | 5,510× | still >1,000× | still >500× |
| Altman Z (est.) | 4.12 | ~3.4 (Safe) | ~2.7 (Grey) |

### The critical insight: **FCF inflects POSITIVELY in the downside**

The FY26 FCF collapse to $3.0M was caused by **growth investment, not distress** — $253.7M capex plus a **$259.9M working-capital build** absorbed $513.6M of cash to fund a 35.7% revenue increase. Both reverse dramatically in a contraction:

| FCF bridge, −20% scenario | $M |
|---|---|
| Operating income | 233.9 |
| + D&A | 68.4 |
| − Working capital release (WC/revenue held at 37.9%, revenue falls → ~$350M released) | **+350** |
| − Capex (discretionary, cut to ~$150M) | (150) |
| **≈ Free cash flow** | **~$500M** |

That is roughly a **3.3% FCF yield at the current $15.2B market cap** — from a business currently yielding 0.02%. Fabrinet's working-capital intensity (37.9% of revenue) is the balance-sheet asset that converts a revenue decline into a cash *inflow*, because 91 days of inventory and 80 days of receivables liquidate.

**Survival conclusion:** Fabrinet survives a −20% and even a −35% revenue shock **without raising capital, without covenant relief, and without touching debt markets**. There is no solvency scenario short of a >50% revenue collapse combined with total inventory write-off that impairs this balance sheet. The downside risk is **entirely to the equity**, not to the enterprise.

**Valuation at −20%:** $15.2B / ~$239M = **~64× depressed earnings**; EV/EBITDA ~47×. A −20% revenue year would likely compress the multiple toward the mid-teens, implying a further 40–55% equity decline even with the business still solidly profitable. **This is the real downside — multiple compression on a de-rating growth story, amplified by beta 2.18.**

**Gap:** COGS fixed/variable split is not disclosed in the data pulled; my 85/15 assumption is an estimate. AP/DPO is not available, so cash conversion cycle cannot be fully closed.

---

## 5. Overall Financial Risk Rating

# MODERATE

**Decomposed, because a single number misrepresents this profile:**

| Risk dimension | Rating | Driver |
|---|---|---|
| **Credit / solvency risk** | **LOW** | Net cash $871M, 0.16% debt/equity, Z-score 4.12, no maturity wall, no covenants |
| **Liquidity risk** | **LOW** | Current 2.25, quick 1.52, WC $1,757M, OCF-positive; liquidity *improves* in a downturn |
| **FCF sustainability risk** | **HIGH** | FCF $3.0M; OCF/NI 54%; capex + WC = 111% of OCF; gross margin thinning |
| **Market / equity risk** | **HIGH** | 64% vol, beta 2.18, −50% peak-to-trough, ~32× P/E, ~23× EV/EBITDA |
| **Concentration / business risk** | **HIGH** | Four customers ≈ 57%+ of revenue |

The company **cannot fail on its balance sheet**. It can very easily **halve again on its income statement and multiple**. For a risk analyst: the credit is not the question; the equity is.

---

## 6. Key Red Flags

**1. 🔴 Free cash flow has gone to zero — $365.6M → $206.5M → $3.0M in two years.**
Revenue grew 61% over the same span. A 0.02% FCF yield on a $13–15B market cap means investors are paying for earnings the company cannot currently convert to cash. Capex alone is now 5.5% of revenue (up from 1.6% in FY24). Notably, FY26 net income ($473.0M) **exceeded operating income ($462.9M)**, i.e. non-operating income and a favourable tax structure are contributing — Fabrinet's Cayman/Thailand tax position is a structural earnings support that deserves scrutiny in its own right (composition not broken out in available data — **gap**).

**2. 🔴 Inventory is growing at 2.1× the rate of revenue.**
Inventory +75.8% ($581.0M → $1,021.2M) against revenue +35.7%. Inventory days jumped **+20.6 days to 91.2**. For optical transceivers and datacom components — short-lifecycle products subject to rapid speed/format obsolescence (400G→800G→1.6T) — a 91-day position built ahead of demand is the single most dangerous item on the balance sheet. If the NVIDIA/AI-datacom order book softens, this inventory does not liquidate at book; it is written down. **A 15% inventory write-down = ~$153M, or 32% of FY26 net income.**

**3. 🔴 Severe customer concentration — and the largest customer is Cisco at 20%.**
Per FY2026 disclosure: **Cisco 20%, NVIDIA 16%, Nokia 11%**, plus a fourth customer ≥10% → **~57%+ of revenue in four counterparties**. This is a single-customer-loss-away business: losing NVIDIA alone removes 16% of revenue and, given fixed-cost absorption at a 12% gross margin, roughly a third of operating income. It also means Fabrinet has **no pricing power** — evidenced by three consecutive years of gross margin erosion (12.35% → 12.09% → 11.99%) despite explosive volume growth. It is a price-taker to hyperscalers.

**4. 🟡 The drawdown has already happened, and it is multiple-driven.**
−49.8% close-to-close from the May 2026 peak, in a rising market, on accelerating revenues. That is de-rating, and de-rating is not self-limiting. At ~32.5× diluted EPS and ~23× EV/EBITDA, there is no valuation cushion to absorb a demand disappointment or a single customer insourcing decision. Beta 2.18 means any market-level stress is roughly doubled.

**5. 🟡 Every Piotroski trend variable is negative.**
Accruals quality, leverage trend, gross margin trend, and asset turnover trend all failed. This is the signature of a company whose reported growth is outrunning its cash generation and its margin structure — a classic late-cycle quality deterioration pattern even while headline revenue compounds at 36%.

**6. 🟢 (Mitigant, stated for balance) The one thing that is unambiguously strong is the balance sheet.**
$871M net cash, no debt, no covenants, no maturities, Z-score 4.12. In a sector where AI-supply-chain names are increasingly levering up to fund capacity, Fabrinet is self-funding. Its working-capital intensity is a *liability in expansion and an asset in contraction* — it will generate cash exactly when peers need it.

---

## 7. Data Gaps & Tool Inconsistencies (flagged explicitly)

1. **Beta conflict:** computed beta 2.179 vs profile field 1.345. The computed figure uses a 3-year window vs SPY and is the more relevant risk measure; the profile beta is likely a 5-year monthly regression. I have used the computed 2.18 for market-risk conclusions and flagged sensitivity.
2. **Max drawdown conflict:** tool reports −57.8%; my close-to-close calculation from the price history gives −49.8%. Both indicate a ~50%-plus drawdown; I report both rather than picking one.
3. **Net debt conflict:** leverage tool reports net debt of −$871.0M (= cash $875.1M − total debt $4.0M), but the balance-sheet row computes −$342.7M. The $528M difference implies debt-like items (most likely operating lease liabilities) excluded from `total_debt`. Even on the conservative −$342.7M reading, the company is net-cash.
4. **Market cap staleness:** profile price $363.33 vs latest close $424.27; FCF yield tool uses $13.17B cap. At the current price, market cap is ~$15.2B and the FCF yield remains ~0.02% — the conclusion is unaffected.
5. **Not available:** Sortino ratio, credit rating and CDS (none exist — no public debt), DPO/cash conversion cycle, COGS fixed-variable split, tax rate, segment and geographic revenue mix, and quarterly seasonality. **Peer benchmarking was not performed** — no comparable leverage/coverage data was pulled for the optical/EMS peer set, so all ratios are absolute rather than relative.

---

### Bottom line for the investment memo

Fabrinet is a **financially unbreakable company attached to a highly breakable stock.** Zero debt and $871M of net cash eliminate credit risk entirely and make a 20–35% revenue decline survivable with room to spare — and, counter-intuitively, cash-generative. The risks that matter are (a) a free cash flow conversion that has gone to zero while revenue grew 36%, (b) inventory accumulated at twice the rate of sales in an obsolescence-prone product category, (c) 57%+ of revenue concentrated in four customers at a 12% gross margin that leaves no buffer, and (d) a ~32× earnings multiple that has already begun de-rating (−50% from peak) with beta 2.18 to amplify whatever comes next. **The downside case is a 40–55% further equity decline on a business that remains profitable throughout.**
