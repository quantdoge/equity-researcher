# Short Analyst

- Symbol: NBIS
- Elapsed: 134.9s

---
# Forensic Short-Seller Analysis — Nebius Group N.V. (NBIS)

**Price $130.30 | Mkt cap ~$31.3–36.5B | Q2'26 revenue $582.3M (+454% YoY) | TTM FCF −$3.68B**
*Note: vendor market cap ($31.3B) and price × Q2'26 diluted shares (280.4M × $130.30 = $36.5B) disagree; using shares × price ≈ $36.5B as live, flagging the discrepancy. Stock is −54% from the 18-Jun-26 close of $286.69 and fell 15.6% on 42.8M shares on 12-Nov-26, its Q3 report date.*

---

## 1. Earnings Quality Assessment: **LOW**

The accounting is not fraudulent in the Enron sense — there is no evidence of fabricated revenue, and the backlog is contractually real. But **reported profitability is almost entirely an artifact of three discretionary choices**: (a) an accounting-driven D&A lag, (b) the exclusion of ~$155M/quarter of "adjustments" from Adjusted EBITDA, and (c) a GAAP net income line dominated by non-cash revaluation gains. On a cash basis the business destroys ~$3.7B a year.

The headline quality score (60/100) and "ok" accruals (−0.024) are **misleading for mechanical reasons**, explained below.

## 2. Key Red Flags

| # | Red Flag | Data |
|---|---|---|
| **1** | **Depreciation life extension — the smoking gun** | Servers/network equipment useful life extended **4 → 5 years effective Jan-2026**. Directly flatters D&A and margin. Confirmed by the Beneish sub-index: **DEPI 1.451** (>1 = depreciating slower relative to the asset base). |
| **2** | **Capex/revenue ≈ 6–7x** | 2026 capex guide **$20–25B** vs revenue guidance **$3.0–3.4B**. H1'26 alone spent **~$8.1B**. FY25 capex $4.07B vs OCF $385M → **FCF −$3.68B**; FCF/NI = **−44.6x**. |
| **3** | **Adjusted EBITDA is ~3x GAAP-implied EBITDA** | Q2'26 company Adj. EBITDA margin **41%** (~$239M) vs GAAP-derived EBITDA **$83.8M (14.4%)**. Gap ≈ **$155M/quarter (~$620M/yr = 27% of revenue)**. SBC is only $83M *per year*, so the bulk of the adjustment is unexplained by comp. |
| **4** | **True margin after depreciation** | Q2'26 gross margin **77.1%** looks like best-in-class software — but COGS **excludes the GPU fleet's depreciation**. Gross profit $448.7M − D&A $259.7M = **$189.0M = 32.5% of revenue**. That is the real gross margin, and it is still *understated* because the fleet is young and D&A lags capex. |
| **5** | **Receivables vs revenue** | FY25 **AR +1,823% vs revenue +479%** → hard red flag. Quarterly AR is wildly unstable: **$1,526M (Q1'26) vs quarterly revenue of $399M** (≈349 days of sales), then collapsing to **$288.6M** in Q2'26. Either a reclassification of supplier prepayments or aggressive recognition — **I could not resolve this from filings (SEC EDGAR returned 403)**. Treated as unresolved, not proven. |
| **6** | **GAAP net income is not operating income** | Q1'26: net income **+$621.2M** against operating income **−$128.0M** (+$749M non-operating). Q2'25: **+$584.4M** vs **−$111.2M**. FY25: NI **+$82.5M** vs operating income **−$611.7M**. Positive net income exists *only* because of mark-to-market gains on equity stakes (ClickHouse et al.) — non-cash, reversal-prone, unrelated to the AI cloud. |
| **7** | **Working capital hemorrhage** | FY25 change in working capital **−$1,173.4M** on $530M of revenue. Cash is being consumed in prepayments to hardware vendors faster than it is generated. |
| **8** | **Interest expense inflection** | $4.8M (Q2'25) → **$95.0M** (Q2'26), a 20x rise; some sources cite **$119.1M** including lease interest. Annualised $380–476M vs GAAP EBITDA $335M → **interest coverage < 1.0x on GAAP EBITDA**, ~2.5x even on generous Adj. EBITDA. |
| **9** | **Serial dilution / liability stacking** | Three convertible raises in ~12 months ($3.75B → upsized $5.0B → **$5.75B closing**); ~**$10.0B convertible principal**, **$12.1B future lease obligations**, $775M GPU-backed loan, **12.3M shares still available on the ATM**. Shares outstanding 236M → 280.4M (**+19%**). |

## 3. Beneish M-Score and Accruals

**M-Score = +2.479** (threshold −1.78) → "HIGH RISK — likely manipulator."

I assign this **partial weight only**. Decomposing:

- **Mechanically inflated (ignore for fraud purposes):** SGI 5.79 (479% revenue growth), LVGI 7.574, AQI 2.883 — all are genuine hyper-growth/refinancing artifacts, not manipulation signals.
- **Genuinely diagnostic:** **DEPI 1.451** (useful-life extension — real, confirmed, discretionary) and **DSRI 3.321** (receivables days explosion — real but possibly reclassification).

**Accruals:** −0.0243 ("ok"). This is a **denominator illusion** — average total assets ballooned from $3.4B to $28.0B in five quarters, so any accrual numerator looks trivial. More importantly the numerator (net income $82.5M) is *flattered* by revaluation gains; strip those and accruals are deeply negative in economic terms. **Cash conversion 4.66x is meaningless** (tiny, fake-positive NI denominator). The only honest cash metric here is FCF conversion: **−44.6x**.

**Piotroski F 8/9 "Strong"** — I explicitly discount this. An F-score rewards positive OCF, ROA improvement and leverage direction; all three are structurally distorted for a company mid-$20B buildout. It is a mean-reversion screen, not a fraud screen.

**Altman Z 1.096 "Distress"** — also discount the level (X5 asset turnover of 0.043 is meaningless for a pre-revenue-scale asset base; X4 uses book equity). The *direction* is the message: the Z-score has fallen as debt went $188M → $10.06B in five quarters. Liquidity is genuinely adequate ($8.04B cash vs $2.01B net debt), so this is a **solvency-gradual, not solvency-imminent**, story.

## 4. Competitive Threat Assessment: **SEVERE, and structural**

- **No moat.** Nebius buys NVIDIA GPUs at market price, rents or builds shells, and resells compute. No proprietary silicon, no software lock-in, no switching costs. CoreWeave, Oracle (OCI), Microsoft, Amazon, Google and every sovereign fund are building the identical asset.
- **Customer concentration is the existential risk:** three customers = **24%, 21%, 14% = 59% of Q2'26 revenue**. ~$32B of the ~$40B commitment book is **Microsoft + Meta**. These are simultaneously the company's two largest customers and its two most capable potential competitors/self-builders. A landlord whose only tenants are two entities richer than it is has **zero pricing power at renewal**.
- **Commoditisation is already forecast:** Gartner projects **>80% of neoclouds will not be independent by 2030**. That is the base rate for this business model.
- **Group-level overstatement of the "moat":** the description still lists Toloka, TripleTen and Avride as core; AI cloud is **98% of revenue**. The equity story and the business have diverged.

## 5. Management & Governance Red Flags: **MODERATE**

- **Overly promotional framing:** "we could sell today our entire 2027 capacity," alongside a 41% Adjusted EBITDA margin that is a 3x markup to GAAP-implied EBITDA, plus a mid-year useful-life extension that raises reported margin. Each is defensible alone; together they compound.
- **Insider filings:** **25+ Form 4s in ~2 months**, including **10 on a single day (3-Sep-26)** and a continuous weekly cadence through 2-Nov-26. This density right after the June top is worth attention — but I **could not verify direction** (EDGAR returned 403). Could equally be scheduled RSU vesting and 10b5-1 sales. **Unconfirmed; do not trade on it.**
- **Continuous capital-markets dependence:** three converts in twelve months plus an open ATM is a management team that has concluded the equity price, not the business, is the product.
- **Dutch incorporation / 20-F (foreign private issuer) status** means materially lighter disclosure than a domestic 10-K — including on segment economics and customer contracts. That is a structural information disadvantage for shorts.

## 6. Short Thesis Summary

**The credible bear case is ROIC and credit, not fraud.**

Nebius is a capital-intensive landlord deploying **$20–25B of capex in 2026 against $3.0–3.4B of revenue** — roughly 7x. It funds the gap with customer prepayments (~$9B, covering only 50–60% of related capex), convertibles (~$10B, three raises), an ATM, and $12.1B of future leases. Depreciation is deliberately lagging the asset base (4→5 year lives, plus a fleet that is still young), so *reported* margins peak precisely when *cash* losses are largest: **−$3.68B FCF in FY25, and H1'26 alone consumed ~$8.1B of capex.** Interest expense has gone from $4.8M to $95M/quarter in a year and already exceeds GAAP EBITDA on an annualised basis.

The endgame for a price-taking landlord with 59% revenue concentration in two counterparties who could build it themselves is a spread business with no spread: **the assets get built, the depreciation catches up, and the equity is the residual claimant on a commodity.** The terminal-value problem is where the 54% drawdown already comes from, and where the remaining downside sits.

**Why not a Strong Short — and where the bull case is genuinely stronger than I expected:**

I have to be honest about the other side, and it is substantial:

1. **Demand is real and accelerating.** Revenue $43M → $582M over eight quarters; YoY growth re-accelerated to **+454%**; every quarter beat consensus.
2. **The backlog is contracted, not aspirational.** **$37.5B RPO**, with ~$32B firmly signed with Microsoft and Meta — the two best-capitalised counterparties on earth. That is not a hope trade.
3. **Pricing is going *up*, not down.** The first capacity auction cleared **15% above the highest price ever charged**; 2027 capacity is sold out. Gross margin rose 27% → 77% over eight quarters — **the opposite of moat erosion**, which is the single strongest fact against my thesis.
4. **Liquidity is fine.** $8.04B cash, $2.01B net debt, positive Adjusted EBITDA, and prepayments covering 50–60% of related capex. There is no near-term solvency event to force the re-rate.
5. **The depreciation bear case may be wrong on timing.** If GPU scarcity persists and utilisation holds, 5-year lives may prove *conservative*, not aggressive.

**Where I am right and the bulls are wrong:** the gross-margin "improvement" is an artefact of a depreciation curve that has not yet met the asset base. When the $20–25B of 2026 capex is fully in service, D&A alone plausibly reaches **$5–7B/year** against a revenue base management hopes reaches $7–9B ARR. That arithmetic leaves very little for interest on $22B+ of debt-plus-leases. **The margin story is a timing loan against future depreciation, and the loan comes due.**

**Notable risk to the short:** this is a **1.56-beta credit-spread proxy**. It moved +45.7% in a single session on 9-Sep-25. On 12-Nov-26 (Q3 report day) it fell 15.6%. Shorting a name with this realised volatility carries severe path risk — the thesis is directionally right and can still be marked out of the position.

## 7. Contrarian Rating: **SHORT (moderate conviction — sized small, credit-not-fraud thesis)**

**Not** "Strong Short" — that label requires either accounting fraud or an imminent liquidity wall, and NBIS has neither demonstrably. **Not** "No Edge" — the capex/D&A/ROIC arithmetic is a genuine, quantifiable mispricing in a stock still priced at ~13x annualised revenue and ~21x EV/Sales including $12.1B of lease obligations.

**What would make me press the short:** (1) any reduction in the $7–9B year-end ARR target; (2) an auction price clearing *below* prior highs; (3) further useful-life extension or a second ATM increase; (4) high-yield AI spreads widening past 360bp; (5) proof that the Q1'26 $1.53B receivables balance was revenue recognition rather than prepayment reclassification — **this is the one open item I could not verify, and it should be the first thing checked before sizing up.**

**What would make me cover:** evidence that D&A on the fully-installed fleet still leaves >30% EBITDA margins, or Microsoft/Meta converting commitments into multi-year take-or-pay with price floors.
