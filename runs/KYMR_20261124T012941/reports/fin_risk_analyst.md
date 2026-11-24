# Fin Risk Analyst

- Symbol: KYMR
- Elapsed: 68.0s

---
All data gathered. Writing the assessment.

---

# KYMR — Kymera Therapeutics, Inc.
## Financial Risk Assessment

**Company:** Clinical-stage biotech (targeted protein degradation) | Watertown, MA | 273 FTE | IPO Aug 2020
**Price:** $150.37 | **Market cap:** $12.84B | **TTM revenue:** $102.2M | **TTM FCF:** −$288.9M
**Fiscal data through:** Q3 FY2026 (period end 2026-09-30)

> **Framing note:** KYMR is a pre-commercial company. Conventional credit metrics must be read against that fact. The central finding of this report is a **divergence between creditor risk and equity risk**: the balance sheet is fortress-grade and the company cannot plausibly default in the next several years, yet the *equity* is a binary, pipeline-priced asset that has historically drawn down ~60%. Do not conflate the two.

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE-equivalent (functionally debt-free). Unrated — no public debt or CDS exists.**

| Item | Value (Q3'26) | Read |
|---|---|---|
| Total debt | $76.6M | Lease-dominated; interest expense only **$62K/quarter** (~0.3% implied rate) |
| Cash & ST investments | $971.2M | — |
| Total cash incl. LT investments | **~$1.6B** (company-reported) | Confirmed by $1.77B total assets vs $998.6M current assets |
| Net cash | **+$894.6M** (ST basis); ~+$1.5B incl. LT | Negative net debt |
| Debt/equity | 0.05 | No financial leverage |
| Debt/assets | 0.05 | — |
| Interest coverage | −1,403x | **Economically meaningless** — interest burden is trivial, not a constraint |
| Net debt/EBITDA | 2.53 (tool) | **Invalid** — both numerator and EBITDA are negative. Discard. |

**Altman Z-Score: 4.93 "Safe" — but treat as unreliable.** The score is carried entirely by x4 (book equity / liabilities = 9.68) — an artifact of $2.9B+ of cumulative equity issuance. The two genuine earnings-based components are distress-level: x2 (retained earnings/assets) = **−0.61**, x3 (EBIT/assets) = **−0.18**. Z-score was built for leveraged industrials; for an equity-funded clinical biotech it measures the size of the equity cushion, not solvency quality.

**No refinancing cliff, no covenant risk.** Long-term debt is $0 on the reported lines; the $76.6M is largely lease obligations ($13.8M short-term at YE2025). There are no bond maturities, no revolver dependence, and no financial maintenance covenants in evidence. *Data gap: no detailed debt maturity schedule is available from the feed.*

---

## 2. Key Financial Risk Metrics

| Metric | Q3'26 / FY25 | Assessment |
|---|---|---|
| Current ratio | **10.47x** | Exceptional |
| Quick ratio | 10.47x | No inventory (no product) |
| Cash ratio | 10.19x | Exceptional |
| Working capital | $788M (YE25) | — |
| Assets/liabilities | **10.68x** | — |
| Equity/assets | 0.91 | All contributed capital; retained earnings **−$1.33B** |
| Debt/equity | 0.05 | — |
| **Piotroski F-Score** | **4 / 9 "Weak"** | Low validity here — see below |
| FCF yield | **−1.85%** | Negative, structurally |
| EV (mkt cap − net cash) | ~$11.9B | ~117x TTM revenue |

**Piotroski F-Score caveat:** the score fails on positive ROA, positive OCF, no-dilution, gross-margin improvement and asset-turnover improvement. For a pre-revenue biotech, negative OCF and dilution are *structural features of the business model*, not deterioration signals. The one genuinely informative fail is **F7 (dilution)** — see red flags.

**FCF trajectory — the real story**

| Period | FCF | Δ |
|---|---|---|
| FY2023 | −$137.3M | — |
| FY2024 | −$207.3M | +51% burn |
| FY2025 | −$234.3M | +13% burn |
| TTM (Q4'25–Q3'26) | **−$288.9M** | +23% burn |

Quarterly: Q4'25 −$66.9M → Q1'26 −$89.3M → Q2'26 −$54.5M → Q3'26 −$78.2M. Quarterly opex ex-revenue has stepped up sharply: **$118.6M → $140.6M → $147.2M** (~$580M annualized) as Phase 3 / Phase IIb asthma spending begins. Burn is inflecting upward, not stabilizing.

**Cash runway:** $1.6B liquidity ÷ ~$290M current annual burn = **~5.5 years**; management guides **runway into 2029**, which implies burn ramping toward $450–500M/yr. Even on the conservative short-term-only basis ($971M ÷ $289M), runway is **~3.4 years**. **No financing need before 2028 at the earliest.** This is the single strongest element of the risk profile.

---

## 3. Market Risk Profile

| Metric | 1-Year | 3-Year |
|---|---|---|
| Annualised volatility | **59.5%** | **71.1%** |
| Beta vs SPY | 1.62 | 1.59 |
| **Max drawdown** | 25.0% | **59.4%** |
| Sharpe (rf = 0%) | 1.53 | 1.09 |

- Company-reported beta: **2.03** — at the high end; a 20% market drawdown implies a **32–40%** KYMR decline on beta alone, before idiosyncratic moves.
- The gap between the 1-yr (25%) and 3-yr (59.4%) drawdown is the most important market-risk fact: **the stock is in a powerful uptrend that is masking a history of violent repricing.** Recent low realized drawdown is not evidence of low risk.
- Sharpe of 1.09–1.53 looks attractive but is a **misleading measure for a binary-outcome asset** — returns are fat-tailed and non-normal, so standard deviation understates true tail risk. *Data gap: Sortino ratio not available from the tool.*
- **Valuation concentration risk:** $12.8B cap on $102M TTM revenue (~126x) with **zero product revenue**. 100% of enterprise value is pipeline NPV. This is the transmission channel through which all other risks reach the equity.

---

## 4. Downside Scenario Analysis

**Scenario A — Revenue −20% (as specified).** Revenue falls $102.2M → $81.8M; costs held flat. Net loss widens to ~−$332M; FCF to ~−$255M. Runway shortens from ~5.5 to ~6.3 years (denominator falls, so runway barely moves). **Solvency and credit rating unchanged. Immaterial.** A 20% revenue stress is the wrong stress for this company — revenue is lumpy, milestone-driven collaboration income (Sanofi IRAK4 partnership) and already printed **$0 in Q3'26**.

**Scenario B — Lead program clinical failure (the binding risk).** Historic biotech binary events reprice 50–70%. At a 60% drawdown, market cap $12.8B → **~$5.1B**. The **balance sheet is untouched**: cash still ~$1.6B, debt $76.6M, equity $1.61B. **Solvency intact; the equity is not.** Post-event, cash would represent ~31% of market cap — a real but partial floor, and the company would face raising capital into a broken story or cutting the pipeline sharply.

**Scenario C — Equity financing window closes (2022-style biotech freeze).** Burn $289M/yr at current spend → ~5.5 yrs; at the planned $500M/yr Phase 3 ramp → **~3.2 years**. Because the next raise is not needed until ~2028, this is a **manageable, not acute**, risk — the direct benefit of the $1.6B position. A 40–50% spend cut would extend runway materially if required.

**Scenario D — Sanofi partnership terminated.** The $102M TTM revenue base largely disappears and KT-474/SAR444656 economics are lost. Again absorbed by the cash cushion without solvency consequence, but removes the validation premium embedded in the $12.8B cap.

---

## 5. Overall Financial Risk Rating

# MODERATE

**Split assessment — this is the key output:**

- **Credit / solvency risk: LOW.** Net cash ~$895M (ST basis) to ~$1.5B total, D/E 0.05, current ratio 10.5x, no maturities, no covenants, runway into 2029. Default is not a realistic near- or medium-term scenario.
- **Equity / market risk: HIGH.** Negative FCF, ~17%/yr structural dilution, ~126x TTM revenue on zero product revenue, 71% volatility, 59.4% three-year max drawdown, beta 1.6–2.0.

The **MODERATE** overall rating reflects that the enterprise is financially sound but the security is not. An investor in KYMR is not underwriting balance-sheet survival — they are underwriting clinical outcomes and the price of future equity.

---

## 6. Key Red Flags

1. **Revenue quality is poor and deteriorating in visibility.** Q3'26 revenue was **$0**. TTM $102.2M is milestone/collaboration income, not a durable base; annual revenue has declined from $78.6M (2023) → $47.1M (2024) → $39.2M (2025). The business has no revenue engine independent of partners and milestones.

2. **Structural dilution — the most underappreciated risk.** Share count: 54.0M (2022) → 58.4M (2023) → 75.0M (2024) → 84.4M (2025) → 98.2M (Q2'26) → **100.1M (Q3'26)**. **+85% since 2022 (~17%/yr).** EPS has worsened despite revenue growth: −$2.87 → −$3.69. Piotroski F7 flags it. Cumulative retained deficit of **−$1.33B** means the entire $1.61B equity base is contributed capital, not earned — prior investors have funded $1.33B of losses. Expect continued issuance; runway "into 2029" is only achieved via the equity market.

3. **Burn is inflecting upward, not flattening.** Quarterly opex ex-revenue rose from $118.6M to $147.2M across Q1'26–Q3'26 (+24%). Guidance to 2029 assumes both clinical success and capital access.

4. **Valuation leaves no margin for error.** ~117x EV/TTM revenue and ~126x P/revenue on zero product revenue. The 59.4% three-year max drawdown demonstrates the market's willingness to reprice this violently.

5. **Two of the standard screens in this framework are invalid for KYMR** and should not be cited as reassurance: the Altman Z of 4.93 is an equity-cushion artifact, and the negative interest coverage is a trivial-debt artifact. Using either as evidence of health would be an error.

6. **Aggressive-looking leverage metrics are a mirage in both directions.** Net debt/EBITDA of 2.53 is mathematically meaningless (negative numerator and denominator); the "$82M debt" is largely lease obligations at ~0.3% implied cost. KYMR has no meaningful financial leverage — neither a strength to celebrate nor a weakness to fear.

---

### Data Gaps (explicit)
- **No credit rating or CDS spread** — KYMR is unrated with no public debt, so no market-implied credit signal exists.
- **No debt maturity schedule** broken out; $76.6M treated as lease-dominated on the basis of the ~0.3% implied interest rate.
- **Sortino ratio unavailable** from the toolset.
- **Peer comparables unavailable** — `get_sector_peers` returned only mega-cap pharma (LLY $1.28T, JNJ, ABBV, MRK); no clinical-stage biotech comparables were provided, so no relative credit or valuation benchmarking was possible.
- Q3'26 press release fetch returned **403**; company cash/runway figures were taken from search-result excerpts of that release and cross-checked against reported balance-sheet totals ($1.77B assets vs $998.6M current assets, consistent with ~$690M of long-term investments).
- Note a **feed inconsistency** in the balance-sheet `net_debt` field (reported −$296.8M at Q3'26 vs. cash less debt of −$894.6M). All net-debt figures in this report were recomputed directly from cash and total-debt line items.
