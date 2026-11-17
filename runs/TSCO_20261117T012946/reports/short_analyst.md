# Short Analyst

- Symbol: TSCO
- Elapsed: 136.8s

---
# TSCO — Forensic Short-Seller Analysis
**Tractor Supply Company** | Price $37.95 | Mkt cap $19.68B | Specialty Retail (Consumer Cyclical)

---

## 1. Earnings Quality Assessment: **MEDIUM-HIGH** (not fraudulent)

This is the most important finding, and it is against my own bias: **TSCO's accounting is clean.** There is no short case on manipulation grounds. Any bear thesis must rest on business decay and valuation, not fraud.

| Metric | FY2025 | Read |
|---|---|---|
| Beneish M-Score | **−2.37** | Below both −1.78 and −2.22 thresholds = **low manipulation risk** |
| Accruals ratio (NI − OCF)/assets | **−4.93%** | Negative accruals = conservative, cash-backed |
| Cash conversion (OCF/NI) | **1.49x** | Excellent (quality threshold >1.0x) |
| TATA component | −0.0493 | Favourable |
| Altman Z | **3.11** | Safe zone |
| Piotroski F | 6/9 | Moderate — but see below |

**Where quality is genuinely weak: FCF conversion.** OCF/NI is 1.49x, yet **FCF/NI is only 0.68x** because capex ($895M) is 1.81x D&A ($494M). Reported EPS is flattered by depreciation that substantially understates true reinvestment. FCF/NI has been 53.6% → 52.4% → 57.8% → 67.6% over FY2022–25. The composite quality score is **60/100**, dragged almost entirely by that FCF gap.

---

## 2. Key Red Flags Found

1. **Zero net income growth for four years.** $1,088.7M (FY22) → $1,107.2M → $1,101.2M → **$1,096.1M (FY25)**. A 4-year net income CAGR of **+0.2%**. All apparent EPS progress ($1.942 → $2.06) came from share count reduction (579.1M → 532.2M diluted, −8.1%). This is a financial-engineering growth story, not an operating one.
2. **Guidance credibility failure.** Feb 2026: FY26 guide = net sales +4–6%, diluted EPS **$2.13–$2.23**. Reaffirmed in May 2026. October 2026: FY26 EPS **$1.78–$1.88** (adj. $1.90–$2.00) — a **~17% cut** with no external shock, plus comp guidance slashed from **+1% to 3% → (1%) to flat**. Management was either promotional or blind.
3. **Operating margin is structurally eroding, not temporarily.** 10.27% (FY21) → 10.10% → 10.16% → 9.86% → **9.45% (FY25)** → **8.0–8.3% guided FY26**. ~200bp in two years, with management's stated causes being *price-value investment* (i.e. they are losing on price), transportation/fuel, DC start-up deleverage, and mix shift into lower-margin consumables. Four consecutive quarters of YoY operating-margin compression (Q4'25 −79bp, Q1'26 −69bp, Q2'26 −134bp, Q3'26 −134bp).
4. **Q3 FY2026 shows the operating leverage working in reverse.** Sales +5.1%, comps +0.4% (vs +3.9%), gross margin 36.4% vs 37.4% (−100bp), SG&A 28.6% of sales vs 28.1%, **operating income −10.2%, net income −13.3%, EPS −11.6%**. Revenue growth is now 100% new stores + acquisitions; comps are effectively nil.
5. **Diminishing returns on capital.** Revenue/total assets fell 1.52 → **1.42**; Piotroski loses F3 (ROA improvement), F8 (gross margin), F9 (asset turnover) — all three trend items negative. Capex rose $753M → $895M → **$930–990M guided** = 6.4% of sales, while new-store count grows ~3.5%/yr and comps are negative. They are running harder to stand still.
6. **Leverage rising into an earnings decline.** Total debt $4.27B → **$5.94B** (+39% in three years); net debt $5.75B; cash only **$194M**. Net debt/EBITDA: 2.29x → 2.48x → 2.70x → **2.93x**, and EBITDA is now shrinking — run-rate leverage likely **>3.2x** in FY2026. Interest expense $30.6M → **$69.1M (+126%)** since FY22.
7. **Shareholder returns exceed free cash flow.** FY25: dividends $487.7M + buybacks $361.3M = **$849M** returned vs **$740M FCF (115%)**. Over four years they returned **166% of cumulative FCF** ($4.11B vs $2.48B) — the gap funded by debt. And the buyback shield is now exhausted: FY24 buybacks $584.6M → FY25 $361.3M → Q3'26 just $88.5M. That is precisely why EPS turned negative (−11.6%) for the first time.
8. **Capital-allocation churn in pet.** Closed **74 of 209 Petsense stores** in Q3'26 and took a Petsense impairment in Q2'26 — while simultaneously buying Allivet (online pharmacy) and VIP Petcare (mobile vet). They are impairing one pet bet while buying two more in a category they concede "continues to perform below the Company average."
9. **"Adjusted" creep.** FY26 adjusted net income $990M–$1.05B vs GAAP $930–990M — a ~$60M gap that excludes a Petsense impairment *and* VIP Petcare acquisition costs. Excluding the cost of failed/discretionary strategy from "adjusted" earnings is a mild but real yellow flag.

**Two false positives I will not use (rigour cuts both ways):**
- **The receivables "red flag" is an artifact.** The feed flags AR growth of +25% (FY25) and +779% (FY24) vs revenue growth of 4.3% and 2.3%. But receivables are **$27.0M on $15.5B of revenue (0.17%)** — the +779% was growth off a $2.5M base. TSCO is a cash-and-card business with essentially no trade receivables. **There is no channel-stuffing signal here.**
- **Inventory days: 107.1 → 103.5 → 109.3 → 108.6.** Flat-to-falling. No demand-weakness tell.
- **Data caveat:** the feed's `cost_of_revenue`/`sga` split is internally inconsistent for several periods (gross profit minus SG&A does not reconcile to reported operating income). The press release confirms Q3'26 gross margin of **36.4%**, not the ~33% implied by the feed. I have therefore built the thesis on operating income, cash flow and balance-sheet lines, which reconcile, and on company-reported margins — not on the corrupt line items.

---

## 3. Beneish & Accruals Detail

M-Score **−2.37**: Low risk. Component notes — **DSRI 1.198** is the only elevated index, and it is meaningless at 0.17% of sales. **GMI 1.091** correctly captures the ~90bp gross-margin deterioration but is driven by mix and price investment, not accounting. **TATA −0.0493** is strongly favourable. **LVGI 0.994** understates true leverage risk because Altman/Beneish leverage ratios use book equity, and most of TSCO's "debt" sits in operating leases (~$4.2B of the $5.94B).

**Conclusion: earnings are real, cash-backed, and conservatively stated. The problem is that real earnings are shrinking.**

---

## 4. Competitive Threat Assessment: **Moderate and rising**

- **The moat is real but narrow.** 2,486 stores in 49 states serving a rural customer who values proximity and one-stop need-based shopping. No national competitor replicates that density. This is a genuine advantage and I will not pretend otherwise.
- **But the moat is not pricing power.** Management is *investing in price-value position* — that is the language of a retailer defending against pressure, not one with pricing power. Gross margin −100bp is the evidence.
- **Attack vectors:** TSC Store (Tractor Supply Company's rival — TSC), Bomgaars, Rural King, plus Amazon/Walmart in consumables and pet, plus Chewy in companion animal (the category TSCO admits is underperforming). Big-ticket and companion animal weakness suggests discretionary leakage to e-commerce.
- **The unit-growth runway is the crux.** With comps guided **negative**, growth now depends on opening stores into an already-saturated 2,486-store footprint, at rising capex and falling asset turnover. That is the definition of a maturing chain, and mature chains do not sustain 20x earnings.

---

## 5. Management Red Flags

- **Guidance credibility (moderate).** The Feb→Oct FY26 EPS cut of ~17% and comp guide reset from +1–3% to (1%)–flat is the clearest governance signal. Language in Q3'26 ("moving with urgency," "deliberate choices," "restore operating margins") is a tell that prior strategy is being unwound.
- **Routine-looking Form 4 flow.** ~30 filings cluster on quarterly vest dates and on 2026-05-18 (multi-CIK director grant date). The pattern is consistent with RSU vesting and sell-to-cover, not conviction signals. **Notably, there is no visible cluster of open-market purchases during the April–May 2026 collapse to ~$29** despite management "reaffirming" guidance at the time. Insiders not buying a 50% drawdown is a mild negative. *Caveat: the feed returns filing metadata only, not buy/sell direction — I cannot confirm the sign of these transactions, so I weight this lightly.*
- No auditor change, no related-party disclosure issues found.

---

## 6. Short Thesis Summary — and the other side

**The bear case (credible, multi-year):** TSCO is a maturing, capex-hungry retailer whose four-year earnings plateau has now become an outright decline. Negative comps, ~200bp of structural operating-margin erosion, capex at 6.4% of sales with declining asset turnover, net leverage heading through 3x, and shareholder returns that exceed free cash flow by ~15–35% annually. Consensus FY2027 EPS of **$2.055** requires a **+12% rebound** from FY2026's ~$1.83 — an assumption that is inconsistent with guided negative comps and guided margin compression. Estimate revisions remain skewed down. At ~20x GAAP / ~19x adjusted, TSCO is not cheap.

**Relative valuation is the sharpest point.** Peer multiples computed from the same feed:

| | Price | Diluted EPS | P/E | Operating margin |
|---|---|---|---|---|
| **TSCO** | $37.95 | $1.83 (FY26E mid) | **~20.7x** | **8.0–8.3%** |
| LOW | $224.94 | $11.85 | 19.0x | 11.8% |
| HD | $347.51 | $14.23 | 24.4x | 12.7% |

TSCO trades at rough parity with Lowe's (19.0x) while earning **350–450bp less operating margin with negative comps**. TSCO EV/EBITDA ≈ **13.0x** (EV $25.4B / EBITDA $1.96B) on a *declining* EBITDA base. It has not de-rated to reflect a low-growth, high-capex, levered profile — the historic 22–25x was earned by 15–20% EPS growth that no longer exists.

**The bull case — which is stronger than the bears admit:**
1. **Pristine earnings quality.** Beneish −2.37, accruals −4.9%, OCF/NI 1.49x. This is a cash machine, not a fiction.
2. **Comps are inflecting.** Q2'26 −1.5% → Q3'26 **+0.4%**, with intra-quarter improvement (July negative → August positive → September stronger). Digital growing double digits.
3. **The bar has been reset.** FY26 guidance has been cut and reaffirmed; adjusted EPS $1.90–$2.00 is now the number to beat.
4. **Balance sheet is not distressed.** Altman 3.11; long-term debt ex-leases only $1.76B; dividend and buyback continuing; $930–990M of tariff refunds and vendor support identified.
5. **The short is crowded.** Short interest ~39.5–46.4M shares, roughly **7.7% of float, up ~15% recently** — high for a large-cap retailer. The stock is already −38% from its $60.92 (Aug-2025) peak and **+31% off its $28.94 low**. Late shorts are the marginal seller.

---

## 7. Contrarian Rating: **SHORT** (moderate conviction — *but poor entry; prefer a pair*)

The bear case is **fundamentally valid**: real earnings decline, structural margin erosion, negative comps, leverage through 3x, capex-funded-at-a-deficit, and a still-full ~20x multiple against consensus that requires a rebound the guidance does not support. Downside to 14x FY2027E ($2.055) is ~**$28.75, or −24%**.

But I will not sell a fresh naked short at $37.95 with 7.7% of float already short and comps turning positive. The risk/reward is roughly −24% downside against +30%+ squeeze risk if Q4 comps confirm the inflection.

**Recommended expression:**
- **Preferred:** long LOW or HD / short TSCO — captures the ~350–450bp margin-quality gap at parity multiples without taking the crowded-short beta. This is the highest-quality version of the idea.
- **Outright short only on strength:** add above ~$44 (prior support, −27% below the 2025 peak but +52% off the low), stops through $51.
- **Do not short on accounting or fraud grounds. There is nothing there.**
- **Kill criteria:** two consecutive quarters of positive comps *with* gross margin stabilising at ≥36.5%, or FY2027 EPS revisions turning up. Either would make the multiple defensible and the thesis wrong.

**Bottom line:** This is a *cleanly-reported, genuinely deteriorating* business priced as though it will reaccelerate. The fraud screen is negative, the decay screen is positive, and the crowding screen says you are late. Short the fundamentals, not the financials — and preferably hedged.
