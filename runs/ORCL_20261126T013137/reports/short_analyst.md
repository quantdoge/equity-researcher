# Short Analyst

- Symbol: ORCL
- Elapsed: 85.7s

---
# Forensic Short-Seller Analysis — ORCL (Oracle Corp.)
**Price $103.88 | Mkt cap $314.1B | Net debt $119.6B | Peak close $323.43 (9/10/25) — now −67.9%**

---

## 1. Earnings Quality Assessment: **MEDIUM** (accounting integrity intact — *economic* quality low)

This is the most important distinction in this report, and the one the market keeps conflating:

| Test | Result | Read |
|---|---|---|
| Beneish M-Score | **−2.561** ("low risk") | No manipulation signature |
| Accruals ratio (FY26) | **−5.69%** | Negative = conservative |
| Cash conversion (OCF/NI) | **187%** | Passes comfortably |
| FCF conversion (FCF/NI) | **−139%** | Catastrophic |
| Piotroski F-Score | **5** (moderate) | Fails on GM, dilution, turnover, ROA trend |
| Altman Z | **0.679 — Distress zone** | Book-equity based; indicative |

**Verdict: this is not a fraud short.** The accrual machinery is clean; there is no DSRI blow-out (1.03), no revenue-recognition tell. The short case rests entirely on capital allocation, ROIC and off-balance-sheet leverage — not on the income statement lying. Anyone pitching ORCL as an accounting fraud has the wrong thesis and will lose money.

But the *economics* are deteriorating measurably:
- **FY26 GAAP EPS of $5.83 is inflated by a one-time $2.7B pre-tax non-operating gain** recognised in Q2 FY26 (GAAP net income $6.1B vs operating income $4.7B — net income exceeded operating income). Underlying EPS ≈ **$4.90**, ~16% lower. Effective GAAP tax rate a low 15.1%.
- **OCF quality is now working-capital driven.** Q1 FY27 OCF was $23.1B against net income of $4.76B — with a **+$13.9B working-capital inflow**, i.e. ~60% of operating cash came from the balance sheet (customer prepayments/deferred revenue, not collections). Receivables rose only $1.0B, so it is not factoring — but it is *pre-paid future obligations*, not earned cash.

## 2. Key Red Flags

1. **Gross margin is collapsing at an accelerating rate, with revenue accelerating.** 79.1% (FY22) → 72.9% → 71.4% → 70.5% (FY25) → **65.8% (FY26) → 60.0% (Q1 FY27)**. Management calls this "multi-year normalization." It is mix-shift into GPU hosting.
2. **Incremental gross margin is ~35%**, versus a ~70% legacy base. FY26 incremental GM 38.8%; Q1 FY27 **35.5%**. Gross profit grew +15.6% on +29.6% revenue. Each dollar of "AI growth" grows profit at half the rate of sales.
3. **COGS growth is double revenue growth**: FY26 COGS +36.0% vs revenue +17.3%; Q1 FY27 COGS +58.3% vs revenue +29.6%.
4. **Core software is shrinking**: software revenues **−3%** YoY — the high-margin annuity is being cannibalised while the low-margin business scales.
5. **Shareholder returns funded by 8%+ debt**: FY26 dividends $5.79B, buybacks cut to $0.21B (from $1.5B), FCF **−$23.7B**, while issuing debt at coupons up to **8.65%**. Borrowing at 8.65% to pay a ~1% dividend yield is economically irrational and signals a management priority to defend the equity narrative.
6. **Dilution has re-started**: diluted shares 2.914B (FY26) → **3.000B (Q1 FY27)**, +3% in one quarter; book equity rose $43.1B → $67.2B, i.e. **~$20B+ of equity issued in a single quarter** while the stock was already down ~60%.
7. **Receivables vs revenue**: FY26 AR +21.4% vs revenue +17.4% (no flag, but directionally loose; FY24 was a flag at 13.9% vs 6.0%).

## 3. The Footnote That Is the Actual Thesis: $288B of Off-Balance-Sheet Leases

`total_debt` of $155.9B is **not** the leverage. Per the FY26 10-K: **$260B of lease commitments signed but not yet commenced** (substantially data-centre), against only $37.9B recorded. At Q1 FY27 this rose a further **$28B to ~$288B — growing slightly faster than the backlog grew (+$26B to $664B).** That is the single most damaging data point in this file: **fixed obligations are compounding marginally faster than contracted revenue.**

- Adjusted obligations ≈ $156B debt + ~$210B PV of leases ≈ **$365B+** against **$67B of equity** (~5x adjusted net leverage).
- Lease-adjusted EV ≈ $314B + $120B + ~$210B ≈ **$644B**.

**The depreciation contradiction that breaks the consensus model:** at steady state, annual D&A converges on the annual capex run-rate. Q1 FY27 capex was **$28.5B in one quarter** (~$114B annualised) against D&A of $3.36B (**$13.4B annualised**). Either capex collapses — in which case the $264B FY31 revenue in consensus never gets built — or D&A rises roughly 7x and destroys the earnings. **Both cannot be true.** Consensus net income of $33.7B (FY28) rising to $78.8B (FY31) is not compatible with a data-centre fleet financed at current capex levels.

## 4. Competitive Threat Assessment — **Severe, and structural**

- **Counterparty concentration**: $664B RPO, of which an estimated **~$300B (~45%) is OpenAI** — a loss-making counterparty that must itself raise capital to pay. Oracle has converted from a software licensor into a **leveraged, single-counterparty lessor**.
- **No pricing power in the growth line**: 60% GM and falling, with management already pre-announcing further "normalization," is the definition of a commoditising business. Hyperscalers (MSFT, AMZN, GOOGL) have lower cost of capital and their own silicon; CoreWeave and the neoclouds are taking the same low-margin workload at even thinner spreads.
- **Technology advantage absent**: Oracle is reselling Nvidia compute in leased buildings. The moat is capital access, and Oracle pays 8.65% for it while Microsoft and Google pay ~5%.

## 5. Management Red Flags — **Moderate**

- "Multi-year normalization" for a 700bp margin decline; "fully funded" language deployed immediately before a further $10B raise at 7–8.65%.
- Dividend maintained + buyback eliminated + equity issued + debt at 8.65%, all simultaneously. Capital-allocation discipline has broken down.
- **Insider data gap**: 25 Form 4s in the tool output, heavily clustered (13 on a single day, 10/19/26) — pattern consistent with RSU vesting/tax withholding rather than open-market selling, but **transaction direction and size were not retrievable**. I am not asserting insider selling; this is an honest gap, not a red flag.

## 6. Short Thesis Summary — Credible, but **already paid**

**The bear case is real and I believe the consensus model is wrong.** FY28–FY31 EPS estimates ($11.10 / $15.77 / $20.29 / $27.06) are a linear extrapolation of backlog conversion that ignores (a) depreciation converging on a $100B+ capex run-rate, (b) ~$15–19B/yr of rent commencing on $288B of signed leases, (c) interest annualising to ~$5.7B and rising, and (d) 3–6%/yr dilution. Lease-adjusted EV of ~$644B on 7x sales with negative FCF and a 45% single-counterparty concentration is not a value setup.

**But the other side is stronger than the bears admit:** at $103.88 the stock is **12.7x FY27 consensus EPS** and roughly **7x lease-adjusted EV/sales** — and down 68% from the peak. The legacy Fusion/NetSuite/Database annuity (~$50B revenue at 85%+ gross margin) is plausibly worth $375–425B standalone, meaning the market currently capitalises the entire $288B lease stack and the OCI build at **approximately zero or less**. Michael Burry has already publicised the depreciation argument; the $664B backlog, the OpenAI concentration and the debt are front-page news. The borrow is expensive and the squeeze risk on any backlog headline (or an OpenAI funding announcement) is severe — the stock traded from $145 to $194 in a two-week span in April–May 2026.

**Triggers that would re-arm the short:** capex guided above $110B with FCF still negative; a disclosed OpenAI funding shortfall or contract renegotiation; gross margin below 55%; the lease footnote growing faster than RPO for two more quarters; or a rally back above ~$160 on backlog headlines.

## 7. Contrarian Rating: **NO EDGE — Reject Short Thesis at $104**
*(Directionally correct thesis, structurally correct diagnosis, but the re-rating has already happened. This is a "watch and wait for a rally" name, not a new short. If forced to express a view, the correct instrument is Oracle **credit**, not equity — the equity stub is optionality on the AI build, and the bonds carry the actual downside.)*

**Honest caveats:** gross PPE and lease PV are estimates; insider transaction direction unavailable; no peer multiples gathered, so the 12.7x is absolute, not relative.
