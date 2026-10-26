# Fin Risk Analyst

- Symbol: FCNCA
- Elapsed: 79.0s

---
I have sufficient data. Note: rounds used = 6 of ~10, and I have regulatory capital, asset quality, and the Purchase Money Note dynamic, which materially changes the picture versus the raw tool output.

---

# FCNCA — First Citizens BancShares, Inc.
## Financial Risk Assessment

**Sector:** Financial Services / Banks–Regional · **Price:** $2,387.36 · **Market cap:** $26.53B · **Total assets:** $229.7B (YE2025) · **Employees:** 18,141

---

## ⚠️ Critical Methodology Caveat (read first)

FCNCA is a **bank holding company**. Three of the seven standard tools I was given produce **structurally invalid output** for a bank and must **not** be read as distress signals:

| Tool | Output | Why it is invalid for a bank |
|---|---|---|
| Altman Z-Score | **0.323 "Distress"** | x4 uses equity/liabilities ≈ 0.11 and x1 working-capital/assets ≈ 0.02. *Every* bank scores here because deposits are 90% of the balance sheet. This is a **false positive** — Z-scores are calibrated on industrials. |
| Current ratio | 1.03 | "Current liabilities" = $162.9B is largely **deposits**, not trade payables. No meaning. |
| Interest coverage | 0.60 | Interest expense ($4.96B) is **deposit interest**, i.e. cost of goods sold for a bank, not debt service. |
| FCF yield | 7.02% | Loan originations are "operating," so bank FCF is an accounting artifact. |

**I have therefore built a bank-appropriate framework below** (CET1, PPNR coverage, NIM, nonaccruals, NCOs, tangible equity) and flag these four tools as *excluded from the rating*.

---

## 1. Credit Risk Assessment

### Rating: **INVESTMENT GRADE** (strong, stable)

**Capital adequacy (the dominant bank credit variable):**
- **CET1 ≈ 13.0%** (12.99% at YE2024 per S&P Global Ratings; Q3'26 earnings retention plus stable equity imply ~13.0–13.5% — *not directly reported in tool data, flagged as estimated*)
- Regulatory minimum for a **Category IV** bank incl. stress capital buffer ≈ 7–8% → **~500–600bp of headroom**
- Equity/assets: **9.68%**; Tangible common equity/tangible assets: **9.47%** (equity $22.24B less $541M goodwill/intangibles)
- Liabilities/equity: **9.33x** — normal and appropriate for a regional bank; not comparable to industrial leverage

**Asset quality — improving:**
| Metric | Q2'26 | Q3'26 | Direction |
|---|---|---|---|
| Nonaccrual loans | $1.45B (0.96%) | **$1.37B (0.87%)** | ✅ Improving |
| Net charge-offs / loans | — | **0.27%** | ✅ Benign |
| Provision expense | — | $55M | ⚠️ Below NCOs |

**Pre-provision earnings power:** FY2025 pre-tax operating income $2,971M vs. estimated ~$500M annual provision → **PPNR covers credit costs ~6x**. Even a 3x rise in provisioning is absorbable from earnings without touching capital.

**Verdict:** Balance-sheet credit risk is genuinely low. The bank is over-capitalized relative to requirements and has demonstrated it can absorb a large credit shock (the SVB acquisition) and de-risk it profitably.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| **Capital** | | |
| CET1 ratio (est.) | ~13.0% | ✅ Strong — ~550bp above minimum |
| Equity / assets | 9.68% | ✅ Solid |
| Tangible common equity / TA | 9.47% | ✅ Solid |
| Liabilities / equity | 9.33x | ✅ Normal for bank |
| **Leverage (borrowings)** | | |
| Total debt (YE2025) | $36.01B (15.7% of assets) | ✅ Declining fast |
| Net debt / EBITDA | 4.49x | ⚠️ Not a bank metric — EBITDA excludes interest *income* |
| Debt/equity | 1.62x | ✅ Low |
| **Profitability / debt service** | | |
| Net interest margin (Q3'26) | 3.07% (2.99% ex-PAA) | ⚠️ Compressing |
| PPNR / provisions | ~6x | ✅ Strong |
| Efficiency ratio (Q3'26) | ~63.4% | ✅ Acceptable |
| ROA | 0.96% (FY25) → ~1.04% (Q3'26 ann.) | ⚠️ Down from 1.24% (FY24) |
| ROE | 9.92% (FY25) → ~10.9% (Q3'26 ann.) | ⚠️ Down from 12.49% (FY24) |
| **Liquidity** | | |
| Cash & ST investments | $20.83B (9.1% of assets) | ✅ Adequate |
| Cash / liabilities | 10.0% | ✅ |
| Working capital | $5.05B | — (deposit-driven, not meaningful) |
| **Solvency scores** | | |
| Altman Z | 0.323 | ❌ **INVALID for banks — excluded** |
| Piotroski F-Score | **5 / 9 (Moderate)** | ⚠️ Partially valid; see below |
| **Valuation** | | |
| Price / tangible book | **1.22x** | ✅ Thin cushion vs. peers |
| P/E (TTM) | 12.2x ($195.15 TTM EPS) | ✅ Reasonable |

**Piotroski detail — the failures are informative:** F5 (leverage) ✗, F3 (ROA improvement) ✗, F8 (margin) ✗, F9 (asset turnover) ✗. F1, F2, F4, F6, F7 ✓. This is a coherent read: **profitable, cash-generative, non-dilutive — but returns and margins are deteriorating and leverage rose.** Consistent with my independent NIM/ROA analysis.

**FCNCA’s balance sheet has de-risked materially since the last annual report (this is the single most important update):**
> The $36B "total debt" is dominated by the **FDIC Purchase Money Note** issued in the SVB transaction. FCNCA repaid **$2.5B in Q2'26 and $8.0B in Q3'26** — roughly **$10.5B+ retired in six months**. Interest expense on borrowings fell $19M q/q. The YE2025 annual metrics above therefore **overstate current leverage and funding costs**, and the trajectory is strongly favorable.

---

## 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (3Y daily) | **33.45%** | 🔴 High — ~2x a large-cap bank; driven by low share count (~11.2M shares) and SVB-era gaps |
| Beta vs SPY (3Y daily) | **1.024** | 🟡 Market-like in practice |
| Beta (FMP profile, 5Y) | **0.581** | ⚠️ **Conflicts with 3Y figure** — different frequency/window. I weight the 3Y daily beta (1.02) as more current |
| Max drawdown (3Y) | **-33.51%** | 🟡 Meaningful but not extreme; largely dates to the 2023 regional-bank crisis |
| Sharpe ratio | **0.42** | 🟡 Mediocre risk-adjusted return |
| Sortino ratio | *Not available from tools* | — Data gap |

**Interpretation:** The stock is **not** low-beta despite the headline 0.581 profile figure. Volatility of 33.5% with a 33.5% max drawdown means a 20–25% equity drawdown in a market correction is a realistic planning assumption. Price level ($2,387) with only ~11.25M shares outstanding creates genuine liquidity and gap risk for larger positions.

**Macro backdrop (yield curve, as of 2026-10-26):** 2Y 4.65% / 5Y 4.80% / 10Y 4.99% / 30Y 5.37% — **+34bp 2s10s, not inverted.** A steeper curve is structurally **positive for NIM**, but a 5.37% 30Y yield is a **duration/AOCI risk** for the legacy SVB securities book (see red flags).

---

## 4. Downside Scenario: Revenue −20%

**Base (FY2025):** Revenue $14,497M · Operating income $2,971M · Net income $2,206M · Provision ~$500M

**Mechanics:** Noninterest expense ≈ $6.56B (~45% of revenue) is semi-fixed; deposit interest ≈ $4.96B is variable.

| Line | Base | −20% Revenue Stress |
|---|---|---|
| Revenue | $14,497M | **$11,598M** (−$2,899M) |
| Deposit/funding interest (−10%, repricing offsets) | $4,964M | $4,468M |
| Noninterest expense (−5% variable) | $6,562M | $6,233M |
| **Pre-provision operating income** | **$2,971M** | **~$897M** (−70%) |
| Provision for credit losses (NCO → ~0.9–1.0% of $148.7B loans) | ~$500M | **~$1,400M** |
| **Pre-tax income** | $2,971M | **~($503M) — a loss** |
| **Net income** | **$2,206M** | **~($375M)** |
| **EPS** | $165.76 | **~−$33** |
| **ROA / ROE** | 0.96% / 9.9% | **−0.16% / −1.7%** |

**Capital impact — the key mitigation:**
- A $375M after-tax loss = **~1.7% of the $22.2B equity base** → CET1 falls from ~13.0% to **~11.3%**
- That remains **~350bp above** the regulatory minimum. **No covenant breach. No capital raise required. No dividend cut forced.**

**Milder scenario (revenue −20% but credit benign, provision +$500M):** Net income ~$310M, EPS ~$28, ROE ~1.4%, CET1 ~12.7%. Survivable with room to spare.

**Conclusion:** FCNCA **survives a 20% revenue decline with capital intact.** The earnings model breaks (the bank goes loss-making) but the balance sheet does not. This is the defining characteristic of a well-capitalized bank. Cash runway is a non-issue — deposit-funded, and the Federal Home Loan Bank/broker deposit channels remain open.

---

## 5. Overall Financial Risk Rating: **MODERATE**

*(Balance-sheet/credit risk: **LOW**. Earnings & market risk: **MODERATE**.)*

**Why not "Low":** Earning-asset returns are compressing on both axes — ROA 1.24%→0.96%, ROE 12.5%→9.9%, NIM 3.10%→3.07% with NIM ex-PAA now **below 3.0%**, while funding costs *rise* (rate on interest-bearing liabilities +6bp q/q to 3.01%). FY2025 capital return of $3.19B (buybacks $3.03B + dividends $0.16B) exceeded net income of $2.21B — a **145% payout**. A 33.5% volatility / 33.5% max drawdown profile adds meaningful market risk.

**Why not "High":** CET1 ~13% with ~550bp of headroom, nonaccruals falling (0.96%→0.87%), NCOs at 0.27%, PPNR covering provisions ~6x, $20.8B cash (9.1% of assets), 1.22x tangible book, and a $10.5B+ Purchase Money Note paydown that structurally lowers interest cost going forward. Capital return is now ~99% of earnings (Q3'26: $600M buyback vs $606M NI) — sustainable.

---

## 6. Key Red Flags

1. **🔴 Deposit mix shifting to higher-cost, less-sticky funding.** Management explicitly cites growth in **Direct Bank and brokered deposits** driving deposit interest expense up $90M q/q. Brokered deposits are the funding source that killed SVB, Signature and First Republic. NIM ex-PAA is now 2.99% and falling. **This is the top risk to monitor.**
2. **🟠 Provisioning below charge-offs.** Q3'26 provision $55M vs. net charge-offs $103M — a **reserve release**. Nonaccruals are falling, but allowance coverage is being drawn down. If credit inflects, the provision line snaps back hard (see scenario).
3. **🟠 AOCI / securities duration exposure — DATA GAP.** The tool data contains **no AOCI breakdown** and no held-to-maturity vs. available-for-sale split. FCNCA inherited a large, long-duration SVB securities book. With the **30Y at 5.37%**, unrealized losses could be material and are not reflected in the book-value/tangible-book ratios I computed. **This is the largest unquantified risk in this report.**
4. **🟠 Capital return exceeded earnings in FY2025** (145% payout). Self-funded in 2026, but FY2025 relied on balance-sheet capacity rather than earnings.
5. **🟡 Beta data conflict** — 0.581 (5Y FMP) vs. 1.024 (3Y daily). Resolved in favor of the higher, more current figure; investors should not treat FCNCA as low-beta.
6. **🟡 Structural illiquidity** — ~11.25M shares outstanding at $2,387/share. Meaningful slippage risk on position entry/exit.
7. **🟡 Earnings volatility from non-core items** — quarterly results swing on equity warrant fair-value marks, tax-credit investment gains, and marketable-equity adjustments (Q3'26 noninterest income fell $42M largely on a $37M warrant mark). GAAP EPS understates core earnings power but also obscures deterioration.

---

## Data Gaps (explicitly flagged)

| Gap | Impact |
|---|---|
| **CET1 / regulatory capital ratios not in statement data** | Estimated from S&P (12.99% YE2024) + earnings; Q3'26 figure unconfirmed |
| **AOCI / HTM securities unrealized losses** | Largest unquantified risk; book value may be overstated |
| **Deposit composition** (insured %, uninsured %, brokered %) | Cannot size run-risk precisely |
| **Peer multiples unavailable** — `get_sector_peers` returned Vanguard index funds and ETFs, not banks | Cannot compute relative valuation/leverage vs. regional bank peers |
| **Sortino ratio, CDS spreads, credit rating not retrieved** | S&P revised FCNCA's outlook in 2025 (direction not confirmed from source) |
| **Market cap inconsistency** — $26.53B (profile) vs. $29.52B (FCF tool) | Used $26.53B; P/TBV of 1.22x is derived from it |
| **Balance-sheet line inconsistency** — cash fell $56.1B→$20.8B while "net receivables" jumped $3.5B→$146.4B | Clearly a taxonomy reclassification (AFS securities moved out of cash); **not** a real 63% cash decline. Treated as a data artifact |
| **FY2023 net income $11.47B** | Includes ~$9.8B SVB bargain-purchase gain — excluded from all trend analysis as non-recurring |

---

### Bottom Line
FCNCA is a **well-capitalized, over-collateralized survivor** that has already proven it can absorb a systemic shock. Credit risk is **low**. The risk is entirely on the **earnings and market side**: a sub-3.0% NIM, rising brokered/direct deposit funding costs, declining ROA/ROE, and a 33.5% volatility profile. It survives a 20% revenue decline with CET1 near 11.3% and no covenant pressure — but it would post a loss doing so. **Watch the deposit mix and the AOCI disclosure; those are the two items that could move this rating to High.**
