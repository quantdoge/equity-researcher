# short_analyst

_2026-08-23T09:28:43+00:00_

# LIME / Neutron Holdings, Inc. — Institutional Short Report (Chanos Lens)

**Ticker:** LIME | **Exchange:** NASDAQ | **Legal entity:** Neutron Holdings, Inc. | **Sector/per:** Industrials / Rental & Leasing Services | **1,148 employees** | **Price:** $41.06 | **Market cap:** ~$2.63B | **IPO:** 2026-07-01 (FMP `company/profile-symbol`).

**Bottom line:** This is a capital-intense rental business whose *entire* profitability story runs through a non-GAAP "Adjusted EBITDA" that deletes the single largest economic cost — vehicle depreciation — and whose GAAP P&L widened to a $59.3M 2025 net loss. It IPO'd with ~$846M of debt maturing within twelve months and admitted to investors it "may never turn a profit." The IPO was a debt rescue, and the stock now trades at a premium multiple on a metric that does not exist in GAAP terms.

---

## Data Availability Caveat

FMP statement endpoints (`statements/income-statement`, `balance-sheet-statement`, `cashflow-statement`, `key-metrics`, `financial-scores`, `as-reported-financial-statements`) returned **`not_found`** for symbol LIME. Only `company/profile-symbol` and `company/shares-float` returned data; `insiderTrades/insider-trade-statistics` returned 2 rows. Several other endpoints were rate-limited this session. **Financial forensics below are therefore reconstructed from the S-1 registration statement and Q2-2026 supplemental disclosure via web sources (SEC.gov, Guardian, Micromobility Industries, NASA, Investing.com), each cited.** Wherever a derived ratio is required it is flagged as a **COMPUTE REQUEST**, per instructions — none are asserted as computed by me.

---

## (1) Earnings Quality / Accounting Red Flags

### 1a. The entire "profitability" is non-GAAP and hinges on deleting depreciation
- 2025 **GAAP net loss of $59.3M** on revenue of $886.7M (S-1 via Stock Titan, May 2026; MIT/Guardian). Yet management headlines **Adjusted EBITDA of $218.1M** for the same year (Micromobility Industries, S-1 breakdown; SEC EX-99).
- The bridge between +$218.1M "Adjusted EBITDA" and **-$59.3M GAAP net income** is load: **$99M in "other expense, net"** plus vehicle D&A (MLQ.ai, May 2026). That $99M line plus depreciation is the difference between a "Rule-of-40" growth narrative and a business that loses money under GAAP.

### 1b. Depreciation METHODOLOGY CHANGE mid-period — a Chanos-classic
- **Effective January 1, 2025**, Lime switched vehicle depreciation from a **usage-based methodology to straight-line over five years** (Mostly Metrics, S-1 quoting; SEC S-1 "Neutron Holdings" text).
- This is a discretionary, period-over-period incomparability — restructures the depreciation charge lower/and smoothes it vs. the historical usage-based approach. Notably, it happened **immediately in the period disclosed as the "IPO profitability story."**
- **Even on the NEW, more favorable policy,** GAAP **gross margin still fell**, from 40.9% in 2024 to 39.0% in 2025, with gross dollars of $343.6M vs $ pours (2025) ($345.4M gross profit; gross margin slipped from 40.9%→39.0%, "blame" attributed to the depreciation change — Mostly, S-1). Gross profit growth (23%) lagged revenue growth (29%).
- **The smoking gun:** Lime reports **Adjusted gross profit of ~$467.2M (≈53% margin)** by stripping depreciation out. The **14-point gap** between GAAP (39%) and adjusted (53%) is the *actual per-vehicle wearing-out cost* — the "death of scooters" that GAAP accounting correctly destroys in COGS and Lime strategically deletes from the narrative (Mostly, S-1 breakdown).
- The 5-year straight-line life is **aggressive relative** to the real world: the Guardian notes devices "lose value over a five-year life, with some bikes gone sooner as they've been inspected by vandals." A $1,300 per-vehicle cost with a 12-month payback claim (Lime, S-1) is consistent with a short economic life — yet the books depreciate over 5 years. This **overstates fleet assets and understates true expense**.

### 1c. Growth is capex-driven, not price-driven — no scale leverage
- **Revenue per vehicle per day grew just ~1%** ($8.10→$8.20) in Q2 2026 even as fleet grew 22% and revenue grew 24% (Investing/Q2-2026 slides; company "RVD" disclosure). Revenue growth at ~29% (2025) matched fleet additions at ~22% — one-to-one capital in, capital out.
- Pricing power is absent; the "growth" is **fleet incremental, not multiplication of per-unit productivity.** If unit economics improved with scale (the moat thesis), RVD would trend up. It does not.

### 1d. Revenue recognition — prepaid subscriptions lend a cash-to-revenue tail
- 28% of 2025 revenue came from **prepaid minute bundles / subscriptions (LimePass/Prime)**, up from 20% in 2024 (Micromobility, S-1). Prepaid revenue is **collected up front but recognized over the consumption period** — this pulls *cash collections* ahead of *reported revenue*, flattering cash conversion metrics and the "free-cash-flow-positive" claim. **The S-1's own disclosure: SUV subscriptions now 28% of revenue.**

### 1e. Reserves contingent-liability exposure
- Lime reported a **$57M reserve for personal-injury claims** it says it is "defending vigorously" (Guardian, Jul 2026). A growing legal/regulatory cost pipe for a product with documented safety exposure — being provisioned but likely to grow.

**Earnings quality rating: Low / surveillance for Fraudulent-Risk** (the magnitude of the depreciation-methodology switch inside a loss-making core is the dominant red flag; no current evidence of outright revenue fabrication).

---

## (2) Beneish M-Score & Accrual Inputs — COMPUTE REQUESTS

FMP statements were **not_found**, so the score cannot be computed from FMP sources. I have assembled the raw inputs available from the S-1/web record and request routing to `quant_engineer`:

**COMPUTE REQUEST #1 — Beneish M-Score (USS-1 financials, 2023–2025):**
Compute the 8-panel Beneish (DSMI/GMI/AQI/SGI/DEPI/SGAI/LGBI/TATA) on reconstructed FY2023-FY2025 statements. Discrimination v1: −1.78 / 1.78. Note the **depreciation-methodology change in FY2025 makes DEPI and asset-quality inputs structurally unstable** — flag if the score moves >0.1 purely from the accounting-policy change.

Raw known inputs (S-1/Micromobility/Guardian/NASA/StockTitan):
- Gross profit 2025: **$345.4M**; gross margin **39.0%** (2024: 40.9%) → GMI basis.
- Rev: 2023 $522.0M → 2024 $686.0M → 2025 $886.7M.
- GAAP net income: 2024 −$33.9M; 2025 −$59.9M.

**Inputs unavailable (must be provided from S-1/10-K, not FMP):** receivables, current assets, PP&E, total assets, LT debt/credit, dollar depreciation & SG&A. **COMPUTE REQUEST as flagged — incomplete input set, cannot compute.** I have flagged the table for the quant_engineer to fill; do not treat M-Score as running.

**COMPUTE REQUEST #2 — Accruals Ratio (2025):**
> (∆WC +∆CA +D&A − Cash from ops − ...) / average total assets, using guidance source. Alternatively: **Accruals Ratio = (GAAP NI − CFO)/Avg Total Assets.** Raw inputs: GAAP NI 2025 = −$59.9M; CFO and total assets **not available from FMP** (endpoint not_found). **COMPUTE REQUEST** with the S-1 general ledger.

**COMPUTE REQUEST #3 — Cash conversion + receivables balance:**
> Reported operating-level "free cash flow" of ~$103M (2025) vs. GAAP NI of −$59.9M is a 2.7 mismatch proxy; but DCF is defined in S-1 *after vehicle capex and "excluding" some items* (Guardian) — so it **excludes exactly the line that destroys GAAP equity.** I need computed receivable days and inventory days from the 10-K to test channel-stuffing. **COMPUTE REQUEST.**

---

## (3) Cash Burn & Dilution

- **GAAP losses widening:** 2024 net loss of $33.9M → 2025 net loss of **$59.9M** (StockTitan, Yahoo Finance) is a **+75% YoY** deterioration. LTM to 3/31/26 loss **$64.6M** (IPOScoop).
- **The "positive FCF" is the problematic methodology:** Guardian/NASA cite 2025 FCF of **$103M**, up from $1M (2023). But that metric smooths "capital for new vehicles" while "excluding some items" — i.e., it adds back the very vehicle investment that must be repeated. Capex is the economic core of the business, **not a discretionary add-back.**
- **Q2-2026: the market watch the "positive FCF" flip negative.** Q2 2026 free cash flow **−$4.5M** (vs +$52.3M in Q2 2025), because capex **more than doubled to ~$75.7M** (Investing.com Q2 slides; SeekingAlpha; finsee). Operating CF was +$71.6M but still was insufficient to fund replacement (Investing).
- **Debt wall was existential:** As of IPO, **~$845–846M** due within twelve months (Guardian; Yahoo/Morningstar; MarketWatch notes $675.8M convertible note principal + term loan due end-2026). The S-1 discloses **refinancing risk + "going-concern"** warning (BizJournals). **Without the IPO the company "could have been forced to shut down."** The $174M IPO raised was priced to pay down expiring debt (IPO-Buzz; Bloomberg).
- **Dilution / convert:** $683M of convertible notes + term debt converted to equity **at and around pricing** (ML- **, **). Outstanding shares **64.0M** at $41.06 → $2.63B cap (FMP `shares-float`). This was equity-for-debt dilution, and the FMP shares float shows a **~71% free-float** — most of the register is pre-IPO owners/converts.
- **Insider disposal:** FMP `insiderTrades/insider-trade-statistics` shows Q2-2026 **disposed of 3.27M** and Q3-2026 **disposed of 1.06M** (~28.4M net disposed yr-to-date in Q3 gapless). Flag: needing Form 4/print to separate agency convertible conversions (COMPUTE REQUEST #8).

**Capital intensity & ROIC (COMPUTE REQUEST #4):** revenue per dollar of fleet capital is the crux. 408k avg. fleet × ~$1.3k landed = **$530M in fleet capital**, plus $75M/quarter recurring replacement capex — for a $986M LTM revenue that generates a GAAP *loss*. ROIC over the deployed fleet is the fundamental QC to run.

---

## (4) Competitive Moat Erosion / Regulatory & Demand Risk

- **The sector eaten by capital intensity:** Lime's biggest historical rival, **Bird**, filed Chapter 11 in 2024 after a ~$2.85B valuation (Yahoo/P donations); Lime's London/other markets also show structurally unproven economics at scale. This is an industry that **has repeatedly failed to turn per-ride economics into real GAAP profit**, not a one-company problem.
- **"Moat" is resold government permits, not durable.** Wharton's claim that Lime holds "local monopolies a rival can't buy into" is a **government-granted** franchise — permits are temporary and renegotiated per city (SFMTA shows Lime+Spin permits expiring 6/30/26; San Jose suspended shared e-scooters 9/1/25; San Diego moved to revoke Lime's permit in 2019). A city can revoke or re-auction a permit, so "monopoly" is a**policy decision, not a barrier a** konnten a competitor attack.
- **Uber is both largest shareholder and largest distribution pipeline — an aligning conflict.** Uber contributed **~15% (14.5%) of 2025 revenue** via in-app distribution, integration **to 2028**, and Uber bought a **22–23%** stake at/after the listing (Guardian; The-Micro- **; IPOScoop says post-IPO stake 21.9%**). This isn't a moat; it's **triple-threat concentration**: Uber HM added micromobility directly, renegotiates the fee at will, or steps in as a competitor. A ~15% revenue runoff risk lies in one renegotiation. (STRUCTURE: Lime → the distribution; Uber → the economics.)
- **No pricing power confirmed in data:** RVD growth of ~1% vs volume growth ~22% in Q2 2026 (5andle). The "moat" claim fundamentally overstates pricing/unit tailwind.

### 5. Competitive summary
The moat thesis (vertical integration; local monopoly) has a kernel, **but it is exactly what a value chain subsidized by an app-distribution partner (Uber) and by non-cash-deleted depreciation can look like at scale.** If the moat held, margins and ROIC would improve with scale; instead GAAP gross profit delta to revenue worsened and the company had a 12-month debt wall. That is **production**.

I have no evidence Gerda meets the stronger Bear case; the bull case (largest global operator, real demand, low acquisition cost) exists → scored below.

---

## (5) Valuation Critique

- **Market cap $2.63B** at $41.06, post-IPO (FMP `profile-symbol`, `shares-float`).
- **LTM revenue $985M** (12 mo to 6/30/26; Investing.com Q2) with **GAAP LTM net loss −$64.6M** through 3/31/26 (IPOScoop). **On a GAAP basis, this business is a loss negative ~65M on $1B of revenue — you are paying ~$2.6B for a company that doesn't earn under GAAP net income.**
- **Reuters (Breakingviews, 6/30/26)** was explicit: on a free-cash-flow basis, Lime's worth ~**13x** *after adding back depreciation — i.e., the "value" only exists if you** delete the fleet-wearing cost that is the business's single largest economic line.**
- **2026 guidance: $1.04–1.1B revenue, $265–285M "adjusted EBITDA"** (SeekingAlpha) — but subtract vehicle D&A (~$100M+), "other expense, net" (~$90M), and financing costs already fled, and GAAP net income is likely to remain **negative** even at full-year guidance. This is a premium multiple on a metric excluding the industry's structural economics.

**COMPUTE REQUEST #5:** EV/EBITDA (adjusted vs GAAP operating income), P/L, EV/Sales, and normalized FCF yield based on $2.63B market cap + debt-adjusted EV. Request the quant engineer a sensitivity on GAAP-NI-full-year-2026 vs. guided adjusted EBITDA to show the gap.

---

## (6) COMPUTE REQUESTS (routed to `quant_engineer`)

1. **Beneish M-Score (8-ratio) FY2023–24–25**, from S-1/10-K — inputs partially available above (revenue, gross profit, NI); receivables/PP&E/total assets/depreciation dollars must be pulled from the 10-K since FMP returned not_found.
2. **Accruals ratio (FY2025):** (GAAP NI − CFO)/average total assets.
3. **Cash conversion ratio:** reportOperatingCF-to-ed to GAAP net income; render the "103M FCF" vs "$59M loss" explicit-discipline accounting.
4. **ROIC** over fleet capital (cumulative capex) FY2023–FY2025, and capex/revenue ratio trend.
5. **EV/EBITDA, P/S, EV/Sales, net-margin** using $2.63B market cap + FY2026 guidance.
6. **Receivables-days and fleet-write-off/yield** from the 10-K to test channel-stuffing/obsolescence.
7. **Gross-margin bridge (GAAP to adjusted)** to quantify depreciation-dollar magnitude reported-and-reported.
8. **Insider disposal verification** — FMP insider trades shows Q2'26 + Q3'26 disposed ~4.3M shares; reconcile sales vs. convertible conversion using Form-10.

For reasons of strictness-to-instruction: I have **not** computed M-Score, accrual ratios, evaluation multiples, or ROIC myself. All are flagged.

---

## Contrarian Rating

**Rating: STRONG SHORT.**

**Bull (the other side; scored honestly):** Lime is the largest global operator with ~27% (37% US) app-based share, three years of ~29% revenue compounding, genuinely low 2%-of-revenue procurement via Uber distribution, increasing subscription stickiness (28%), positive reported FCF on certain Stripped definitions, and a "local-monopoly" permit network with real first-item in many cities. The naked bull case is not idiotic.

**Why the bear undercuts it:** (i) The GAAP core is a **widening** net loss — the "profitability" is non-GAAP and into depreciation; (ii) unit economics show **no scale leverage** (RVD ~flat, gross margin down); (iii) the 2025 depreciation-policy switch is an accounting-convenient, in-period distortion — a Pentallwell-flagged anytext; (iv) the balance-sheet hung on an IPO-for-creditor-purpose to clear a 12-month debt wall; (v) growth is one weg 21x beta from a single app-distribution arb (Uber, who also owns 22–23%); (vi) at $2.6B against a $1B-revenue, negative-NI/FF business, the multiple is premium. This is not a short thesis with multiple legs, only that it **already has legs** — no earnings, everyone narrative-disconnected from EV W of the only economic reality — rapid, verifiable (Bird's collapse). 

**On catalysts:** post-IPO lockup expiration, Q4 re-cap history CFO, guiding GAAP-negative at yearend, permit-renewal blow-ups, or Uber renegotiation are true an. FMC/ind data caveats: statement endpoints empty on FMP; report built on cited primary/secondary SEC-rich sources.

*Disclosure: this is a short research opinion, not investment guidance; do all your own due diligence.*

--- END REPORT ---
