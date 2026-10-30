# Fin Risk Analyst

- Symbol: FTAI
- Elapsed: 30.6s

---
# FTAI Aviation Ltd. (FTAI) — Financial Risk Assessment

**Assessment date:** latest FY = 2025-12-31 (10-K filed 2026-02-27); market data through 2026-02-27
**Price (latest close):** $304.08 | **Shares (diluted, FY25):** 103.8M → **market cap ≈ $31.6B**

> **Data note / flag:** the company-profile and `fcf_yield` tools return a stale market cap of ~$20.1–20.4B (implied price $196). The price history shows $304.08 on 2026-02-27, a 55% move since. I use the current-market-cap figure and flag ratios where the choice matters.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (speculative) — BB / BB-**

- **S&P raised FTAI to 'BB' from 'B+'** (issue level on unsecured debt); **Fitch 'BB-'** on the perpetual preferred. This is a crossover-adjacent, speculative-grade profile — one notch below investment grade at the issuer level is plausible on leverage alone, but the rating is capped by earnings-quality and structural subordination items, not by leverage math.
- Capital structure: **~$3.5B senior unsecured notes** + a **$2.025B revolver due 2031**. Total debt **$3.45B**, **100% long-term ($0 short-term debt)**.
- The company is *not* in distress on covenant math — but the rating agencies are explicitly underwriting a business whose GAAP earnings are not converting to cash.

**Verdict:** Solvent, refinanced, and liquid *via facilities* — but the credit sits on a thin book-equity base (**$334M equity vs $4.04B liabilities; equity/assets = 7.6%**). Book equity is the shock absorber, and there is very little of it.

---

## 2. Key Financial Risk Metrics Table

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Revenue | $2,507M | $1,750M | $1,186M | +43% YoY |
| EBITDA | $1,080M | $470M | $531M | 2.3x in one year |
| EBIT | $854M | $236M | $346M | Volatile |
| Net income | $501M | $8.6M | $244M | — |
| **Total debt** | **$3,449M** | $3,440M | $2,517M | +37% since FY23 |
| Cash | $300M | $115M | $91M | Thin |
| Net debt | $3,148M | $3,325M | $2,426M | — |
| **Net debt / EBITDA** | **2.91x** | 7.08x | 4.57x | Comfortable *only* because EBITDA spiked |
| **Debt / equity (book)** | **10.32x** | 42.3x | 14.3x | Extreme |
| **Debt / assets** | **0.79** | 0.85 | 0.85 | Asset-heavy, thin equity |
| Equity / assets | 7.6% | 2.0% | 5.9% | **Very thin cushion** |
| **Interest coverage (EBIT/int.)** | **3.45x** | **1.06x** | 2.14x | FY24 was a near-miss |
| EBITDA / interest | 4.36x | 2.12x | 3.28x | — |
| Interest expense | $248M | $222M | $162M | +53% since FY23 |
| **Current ratio** | **5.28x** | 3.53x | 4.63x | Flattered by inventory |
| Quick ratio | 2.30x | 1.94x | 1.82x | OK |
| **Cash ratio** | **0.75x** | 0.33x | 0.80x | — |
| Cash / total liabilities | **0.07x** | 0.03x | 0.03x | **Structural thinness** |
| **Altman Z-Score** | **1.83 (GREY)** | — | — | 0.02 above the 1.81 distress line |
| **Piotroski F-Score** | **5 / 9 (Moderate)** | — | — | — |
| **FCF** | **–$1,063M** | –$1,345M | –$648M | Negative 5 yrs running |
| **FCF yield** | **–3.4%** (current mkt cap) / –5.2% (stale) | — | — | Destroys cash |

**Altman decomposition (indicative, book-equity x4):** X1 WC/TA 0.392 | X2 RE/TA 0.065 | X3 EBIT/TA 0.195 | X4 BVE/TL **0.083** | X5 Sales/TA 0.573. The score is dragged down almost entirely by **X4 = 0.083** — i.e. book equity is ~8% of liabilities. Note this materially *understates* FTAI: using market cap (~$31.6B) instead of book equity, X4 becomes ~7.8x and the Z-score jumps to the **safe zone**. Treat the 1.83 as a book-value warning, not a bankruptcy probability.

**Piotroski breakdown — the weak points are the important ones:**
- ✗ **F2 positive operating cash flow (FAILED)** — OCF –$311M
- ✗ **F4 accruals quality (FAILED)** — NI far exceeds OCF
- ✗ **F7 no dilution (FAILED)** — share count rising
- ✗ F8 gross margin improvement (FAILED)
- ✓ F1 positive ROA, F3 ROA improvement, F5 lower leverage, F6 positive equity change, F9 asset turnover improvement

---

## 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (3y, 756d) | **72.8%** | ~3x the market; very high |
| **Beta vs SPY** | **1.93** (profile: 1.57) | Nearly 2x market sensitivity |
| **Max drawdown (3y)** | **–52.1%** | Peak $178.84 (Jan-10-2025) → $82.50 (Jan-21-2025) |
| Sharpe (0% rf) | 0.69 | Decent, but earned through a 270% rally |
| Price 2023-01-03 → 2026-02-27 | **$16.67 → $304.08** | ~1,725% |

**The drawdown is the story.** In the five sessions around the **15 Jan 2025 Muddy Waters short report**, the stock fell from $171 to $82.50 — a **54% loss in four trading days** on *no change in reported fundamentals*. The stock has since more than tripled from that low. This is the empirical definition of **narrative/factor risk, not operating risk**: the equity is priced on the credibility of the earnings, so a re-litigation of the accounting question is the dominant tail risk, and it re-prices in days, not quarters.

**Downside beta is the relevant one here:** at 1.93 beta, a 20% market drawdown mechanically implies ~35–40% downside, and the historical drawdown proves the stock can do 52% in a week.

---

## 4. Downside Scenario: Revenue –20%

**Base:** revenue $2,507M, gross margin 31.1%, opex (SGA) $9.5M, D&A $226M, interest $248M.

| Line | Base FY25 | –20% revenue | Change |
|---|---|---|---|
| Revenue | $2,507M | $2,006M | –$501M |
| Gross profit (31.1%) | $779M | $623M | –$156M |
| EBIT | $854M | ~$614M | –$240M |
| EBITDA | $1,080M | ~$840M | –$240M |
| Interest | $248M | $248M | — |
| **Interest coverage** | **3.45x** | **2.48x** | Still >1.5x, but thin |
| **Net debt / EBITDA** | **2.91x** | **3.75x** | Approaches typical 4.0x incurrence covenant |
| Pretax income | $606M | ~$366M | –40% |

**Interpretation:** on an *EBIT* basis the company survives a 20% revenue decline comfortably — coverage stays above 2.4x. **But that analysis is worth very little here, because FY25 already proves EBIT does not convert to cash.**

**The real downside scenario is the cash-flow one:**
- FY25 OCF was **–$311M** *at record revenue*. Holding working capital intensity constant, a 20% revenue decline does not fix OCF; it likely worsens the inventory/receivable unwind risk.
- **Cash runway on cash alone: $300M / ($1,063M ÷ 4) ≈ 3.4 months.** This is why the $2.025B revolver is not optional — with it drawn, liquidity covers ~2.2 years of current burn.
- **The dividend is debt-funded.** $145M of dividends paid in FY25 against –$1,063M FCF, plus **$124M of buybacks** executed into a rising stock. Combined **$269M of shareholder returns** funded entirely by balance sheet. This is the single most aggressive capital-allocation decision in the filing and would be the first thing cut under stress.

**A –20% revenue scenario does not threaten solvency. A –20% revenue scenario *combined with a credit-market closure* (no revolver access, notes needing refinancing) does — because cash covers 3.4 months.**

---

## 5. Overall Financial Risk Rating: **HIGH**

Not Critical — the company is profitable, has no near-term maturities, has a $2.0B revolver to 2031, and interest coverage of 3.45x. But **High** is warranted because three distinct risks compound:

1. **Earnings quality risk (highest severity):** NI $501M vs OCF –$311M. Accruals of **$812M = 19.3% of total assets** — a top-decile red flag by any accrual-quality screen. This is the exact mechanism the Muddy Waters report described (one-time engine/module sales booked as recurring aftermarket revenue).
2. **Balance-sheet fragility:** 7.6% equity/assets, Z-score 1.83 (grey, at the distress boundary on book values).
3. **Market/narrative risk:** 73% vol, 1.93 beta, 52% max drawdown, all triggered by a research report rather than by operations.

---

## 6. Key Red Flags

1. **Cash conversion failure — the headline.** FY25 net income **+$501M** vs operating cash flow **–$311M**. An **$812M gap**, equal to 19.3% of total assets. Piotroski flags *both* F2 (positive OCF) and F4 (accruals quality) as failed. Any valuation or credit model built on the $501M of GAAP earnings is not supported by cash.
2. **Inventory ballooning.** Inventory **+117%** ($551M → $1,193M) against revenue **+43%**. Days-inventory **172 → 252 days (+80 days)**. A 46% inventory build in excess of revenue growth, in a business where inventory is engine/module kits, is precisely the item at issue in the short-seller allegations.
3. **Negative FCF five years running** (–$790M, –$834M, –$648M, –$1,345M, –$1,063M). Mitigant: this is substantially *discretionary growth capex* ($752M in FY25) in an asset-leasing model, not operating distress — but the market is being asked to fund the growth externally indefinitely.
4. **Debt-funded shareholder returns.** $145M dividends + $124M buybacks = $269M returned while FCF was –$1,063M. Buybacks at $150–300/share on a stock already up 1,700% is a value-destructive use of borrowing capacity.
5. **Book equity cushion of 7.6% of assets.** $334M of equity supporting $4.37B of assets and $3.45B of debt (10.3x D/E). Retained earnings are only $282M despite five years of existence.
6. **Interest coverage nearly broke in FY24** — 1.06x (EBIT $236M vs interest $222M). The comfortable 3.45x in FY25 rests entirely on the 2.3x EBITDA jump. A single bad year re-runs FY24.
7. **Unsecured, structurally subordinated debt.** ~$3.5B of senior *unsecured* notes ranking behind secured aviation-asset lenders (a separate secured facility complex exists at subsidiary level), with a rated preferred stack above common.
8. **Litigation overhang.** Class action filed Jan-2025 (Case 1:25-cv-00541) following the short report. Non-quantifiable but reflexive — it re-triggers the drawdown mechanism.

---

### Data Gaps (explicit)
- **No CDS spreads** available — cannot read the market's own credit view.
- **No debt maturity ladder** by year in the data. ~$3.5B unsecured notes with staggered maturities and a $2.025B revolver to 2031 are disclosed in ratings commentary, but the **exact refinancing wall is unquantified** — this is the single most important missing item for a true liquidity assessment.
- **No covenant thresholds** disclosed; the 3.75x downside net-debt/EBITDA vs a hypothetical 4.0x incurrence test is my estimate, not a filed number.
- **Revolver availability/usage** unknown — cash runway of 3.4 months assumes the revolver is available.
- **`get_income_statement` returned annual data when quarterly was requested** — no intra-year trajectory available, so I cannot see whether the working-capital bleed is accelerating or reversing in H2 FY25. **This is material** and worth resolving before relying on these conclusions.
- Peer comparison limited: `get_sector_peers` returned mega-caps (GE, RTX, CAT) with no aerospace-leasing comparables; **no peer FCF or leverage multiples obtained**. FTAI should be compared to aircraft/engine lessors (AerCap, Avolon, Fly Leasing-type), not to GE Aerospace.

**Bottom line:** FTAI is a **solvent but aggressively financed, cash-consumptive lessor whose reported earnings are not currently validated by its cash flow statement**, trading at $304 after a 1,700% run and a 52%-in-a-week scare. Credit risk is real but medium-term; **earnings-quality risk is immediate and is what would actually reprice this security.**
