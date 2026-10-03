# Fin Risk Analyst

- Symbol: JPM
- Elapsed: 688.7s

---
I now have a complete dataset covering fundamentals (5 annual + 8 quarterly periods), price history (3+ years), market risk metrics, external credit data, and the macro rate backdrop. Here is the full assessment.

---

# JPMorgan Chase & Co. (JPM) — Financial Risk Assessment
**Sector:** Financial Services / Banks – Diversified | **Market Cap:** ~$919B | **Price:** ~$343 | **FY2025 (ended Dec-2025) primary reference period**

> ⚠️ **Critical methodological note up front:** JPM is a Global Systemically Important Bank (G-SIB). Several of the standard corporate-risk models in the toolkit — Altman Z-Score, Piotroski F-Score, interest-coverage-as-EBIT/interest, current ratio, and FCF yield — are **structurally inapplicable to a deposit-funded bank**. They produce readings (e.g., Z = −0.16 "distress," FCF yield = −15%) that are model artifacts of a bank's balance-sheet-heavy business model, **not** signs of financial distress. I flag each below and re-interpret with bank-appropriate context. The genuine risk picture for JPM is **Low**.

---

## 1. Credit Risk Assessment: **INVESTMENT GRADE** ✅

JPMorgan is rated among the highest-quality credits in the global banking system (A1 / A+ / AA– across Moody's / S&P / Fitch on senior unsecured debt, per filings referenced in web research), and it consistently operates with the strongest capital ratios of any U.S. money-center bank (CET1 ≈ **15%**, well above the ~10–11% regulatory minimum-plus-buffers; ~6.7% tangible common equity-to-assets).

**Why the raw tool outputs do NOT indicate credit distress — and what actually does:**

| Metric (tool output) | Reading | Re-interpretation for a bank |
|---|---|---|
| Altman Z-Score **−0.16** → "Distress" | ❌ Model artifact | Altman Z is built for manufacturing firms. Banks run equity/assets of ~8% by design, which crushes the X1/X3/X4 components. The Z-score has almost no discriminatory power for regulated banks. **Disregard.** |
| Piotroski F-Score **4/9** → "Weak" | ❌ Partially artifact | F2 (positive OCF) fails only because FY2025 operating cash flow was −$147.8B — driven by **balance-sheet growth** (working-capital outflow of −$218.8B from loan/security/deposit flows), not by cash burn. F5 fails on modestly higher debt/assets. Earnings quality (F1, F6–F8) is genuinely strong. |
| Interest coverage **0.74x** | ❌ Not comparable | Interest expense of $97.9B is dominated by **customer deposit funding costs** (~60–70% of the total) — an operating cost of the deposit franchise, not debt-service burden. A bank is not "failing to cover debt" when it earns $57B net income. |
| Current ratio **0.52** | ❌ Normal for banks | Deposits (current liabilities) fund long-dated loans/securities by design. Cash alone ($1.48T) covers 36% of *all* liabilities. |
| FCF yield **−15.4%** | ❌ Misleading | Tool sets capex = 0, so FCF = OCF; OCF is negative purely from $218.8B of working-capital deployment (new loans/securities). Free cash flow is not a meaningful solvency metric for banks. |

**What actually supports Investment Grade:**
- **Net cash position:** Cash & equivalents of **$1.48T vs. total debt of $942B** → net debt is **−$537B** (net debt/EBITDA −6.6x). JPM borrows to fund its balance sheet, not because it lacks liquidity.
- **Earnings power:** $57.0B net income, $81.4B EBITDA, $72.6B operating income in FY2025; ROE ≈ 15.7%; ROA ≈ 1.29% — best-in-class among U.S. money centers.
- **Capital self-generation:** Dividends ($16.6B) + buybacks ($34.6B) ≈ $51B returned to shareholders while CET1 stayed near 15% — capital is internally replenishing.
- **External ratings:** Moody's A1 / S&P A+ / Fitch AA– (senior) with the bank/deposit entities rated a notch higher.

---

## 2. Key Financial Risk Metrics (FY2025)

| Metric | Value | Bank-context read |
|---|---|---|
| Debt / Equity | **2.6x** | Moderate for a bank; includes ST funding ($508B) + LT debt ($434B) |
| Net Debt / EBITDA | **−6.6x** | Negative net debt — cash exceeds all borrowings |
| Debt / Assets | **0.21x** | Low; funding is largely deposits, not debt |
| Interest coverage (EBIT/interest) | **0.74x** | Not meaningful (deposit funding embedded in interest) |
| Equity / Assets | **8.2%** | Healthy for G-SIB |
| Tangible common equity / assets | **~6.7%** (TCE ≈ $298B) | Strong |
| CET1 ratio | **~15%** (web-sourced, mid-2025) | ~400–500bp above requirements |
| ROE / ROA | **15.7% / 1.29%** | Best-in-class |
| Current ratio / Quick ratio | **0.52 / 0.52** | Normal for banks (not a liquidity signal) |
| Cash & ST investments | **$1.48T** | Massive liquidity war chest |
| Cash / Total liabilities | **36%** | High-margin liquidity buffer |
| Assets / Liabilities | **1.09x** | Positive equity cushion |
| Altman Z-Score | **−0.16 ("Distress")** | ❌ Inapplicable to banks — disregard |
| Piotroski F-Score | **4/9 ("Weak")** | ⚠️ Distorted by bank OCF mechanics; underlying earnings quality strong |

**Liquidity & funding view:** JPM's cash position alone covers ~1.5x its *entire* debt stock. Its deposit franchise is a flight-to-quality beneficiary (it *gained* deposits during the March-2023 regional-bank stress). The $508B short-term debt line is routine wholesale funding (federal-funds purchased, commercial paper, ST borrowings) that a money-center bank rolls continuously — not a refinancing cliff. I could not pull a full contractual debt-maturity schedule, LCR, or NSFR from the tools (**data gap**), but the cash/debt mix and rating profile make near-term funding risk negligible in any realistic scenario.

---

## 3. Market Risk Profile (3-year window, vs. SPY; data to Feb-2026)

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility | **24.8%** | Elevated absolute vol — typical for bank equities (rate + credit sensitivity) |
| Beta vs. SPY | **0.93** | Slightly below-market sensitivity; behaves as a defensive cyclical |
| Max drawdown (3yr) | **−24.4%** | Set during the Apr-2025 tariff shock (~$271 → ~$205) and 2023 SVB scare (~$134 → ~$116). Recovered within ~4 months both times |
| Sharpe ratio (0% Rf) | **1.14** | Strong risk-adjusted return over window |
| Sortino ratio | **n/a (data gap)** | Not provided by tool |

**Rate backdrop (supportive):** 2Y 4.22% / 10Y 4.68% / 30Y 5.22%; 2s-10s **+46bp, not inverted** — a steepening, non-inverted curve is a *positive* for bank net interest margin and removes the curve's recession signal. Market risk for JPM is fundamentally **moderate-low**: low beta, resilient drawdowns, and strong Sharpe, offset by genuinely high single-name vol for an equity in this cyclical industry.

---

## 4. Downside Scenario Analysis — Revenue −20% (severe, GFC-class recession stress)

Worst-case construct: fee income and lending volume collapse, spreads widen, credit costs spike. Noninterest expenses only partially flex.

| Line item (FY2025 baseline) | Baseline | Stress (−20% revenue) |
|---|---|---|
| Revenue | $279.7B | ~$224B |
| Operating income | $72.6B | ~$38–48B (op-leverage hit; sticky expenses) |
| Net charge-offs / provision add | ~normalized | +$15–25B incremental credit cost |
| Net income | $57.0B | **~$18–28B (still solidly positive)** |
| ROE | ~15.7% | ~5–8% |
| CET1 ratio | ~15% | ~13–14% (loan growth stalls; earnings absorb losses) |
| Cash position | $1.48T | Essentially intact |
| **Outcome** | — | **No capital breach, no insolvency risk, positive earnings, no covenant stress** |

**Sensitivity logic:** Even with a −20% top line (a true tail event — during the 2008 crisis JPM's revenue did not fall 20%, and in 2020 it fell only ~5%), JPM's CET1 declines by only ~150–200bp and remains far above regulatory minimums; its $298B of tangible common equity and $1.48T cash absorb the shock. This is the defining characteristic of JPM's risk profile: **the downside scenario is an earnings hit, not a survival question.**

---

## 5. Overall Financial Risk Rating: **LOW** ✅

- **Credit risk:** Investment Grade — negative net debt, ~15% CET1, top-rating tier, self-replenishing capital. 
- **Liquidity risk:** Minimal — $1.48T cash, flight-to-quality deposit franchise, no refinancing cliff.
- **Market risk:** Moderate (single-name vol 24.8%, beta 0.93) but with strong risk-adjusted returns and shallow, recoverable drawdowns.
- **Sustainability:** FCF metrics are uninformative for a bank; the economically meaningful gauges (earnings, capital generation, dividend coverage) are all robust. Payout of ~90% of net income (div + buyback) is aggressive but financed wholly out of retained earnings while capital ratios rise.

---

## 6. Key Red Flags

**Genuine (watch-list) risks:**
1. **Duration & securities book:** JPM carries a large investment-securities portfolio; elevated HTM/AFS unrealized losses versus the low-rate era remain an AOCI drag and a rate-spike sensitivity (mitigated by its cash-rich, deposit-funded model).
2. **CRE & consumer credit exposure:** Office/commercial-real-estate and early-stage credit-card delinquencies warrant monitoring through the next cycle — the main channel through which a −20% revenue recession would actually bite.
3. **Concentrated revenue streams:** Investment-banking & markets revenue (CIB) and net-interest income are both cyclical and rate-sensitive; deposit-beta compression could pressure NIM if the Fed cuts aggressively (current curve is steep, so this is a 2027+ concern, not imminent).
4. **Regulatory/capital agenda:** Basel III "endgame," G-SIB surcharge, and potential TLAC/long-term-debt changes can raise required capital — manageable given the ~15% CET1 buffer.
5. **Concentration & key-man:** Size and succession (CEO transition pending) are structural, not acute, risks.

**Model-application red flags (must NOT be read as risk):**
- Altman Z "Distress" (−0.16), Piotroski "Weak" (4/9), FCF yield (−15.4%), and 0.74x coverage are all artifacts of applying non-bank models to a bank. Ignore them for decision-making.

**Data gaps explicitly flagged:**
- No CDS spreads, no contractual debt-maturity schedule, no LCR/NSFR/HQLA figures from the tools (capital ratios and ratings pulled via web research, not direct feeds).
- Capex field returned 0 in the cash-flow feed, so tool-computed FCF = OCF (misleading for banks).
- Sortino ratio not provided (Sharpe only).
- Sector-peer tool returned index funds rather than bank comparables (BAC/C/WFC/GS/MS), so no direct peer-ratio table was built.

---

**Bottom line:** JPMorgan Chase is a **Low-risk, Investment-Grade** credit built to survive and compound through a prolonged downturn. The apparent "distress" flags in the raw tool outputs are model-misapplication artifacts, not economic reality — the genuine risks are cyclical earnings/credit-quality pressure and rate/curve dynamics, none of which threaten solvency or funding under feasible stress.
