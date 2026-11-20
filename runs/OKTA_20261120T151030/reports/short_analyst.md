# Short Analyst

- Symbol: OKTA
- Elapsed: 66.1s

---
# OKTA — Forensic Short-Seller Analysis

**As of:** Oct 15, 2026 · Price **$208.52** · Mkt cap **$34.9B** basic / **$37.3B** fully diluted · Latest reported: **Q2 FY2027** (qtr ended 7/31/26) · FY ends Jan 31

---

## 1. Earnings Quality Assessment — **HIGH** (no manipulation signal)

This is where a short-seller normally makes their case, and **there is no case here.** OKTA's books are clean.

- **Beneish M-Score: −2.651** ("Low risk"), well clear of both the −2.22 soft warning and −1.78 manipulation threshold. Every sub-index is benign: DSRI 0.989 (receivables tracking revenue), GMI 0.987 (margins *improving*), TATA **−0.0668** (negative total accruals), LVGI 0.869 (deleveraging).
- **Accruals ratio: −6.68%** — negative accruals mean cash earnings *exceed* accounting earnings. This is the opposite of what aggressive accounting looks like.
- **Cash conversion 3.76x, FCF conversion 3.67x.**
- **Piotroski F-Score: 8/9** ("Strong"). Only miss is F7 (no dilution).
- **DSO stable at 85.9 days** (FY26) vs 86.8 (FY25). AR +10.6% vs revenue +11.8% — **no channel-stuffing signal.**
- No inventory (software), so inventory-days analysis is not applicable.

**But** — the headline quality is flattered by two items, and those are the real findings:

**(a) Free cash flow is 62% stock-based compensation.** FY26 OCF $884M includes a $544M SBC add-back. Strip SBC and "true" operating cash flow is ~$340M, not $884M. SBC is **18.6% of revenue**. Dilution: 163.6M → 169.6M → 175.9M shares (+3.7%/yr), and the $73M buyback offsets only **13%** of SBC issued. Management is paying its workforce in equity and calling the cash saved "free cash flow."

**(b) Roughly 40% of GAAP net income is interest on the cash pile, not operations.** FY26 operating income $149M vs net income $235M — NI *exceeds* operating income by $86M. On $2.55B of cash earning ~4%, OKTA earns ~$90–110M/yr of interest. The market is capitalising that at 53x. It is completely rate-sensitive and has nothing to do with identity software.

**Rating: High on integrity / Medium on sustainability.**

---

## 2. Key Red Flags

| # | Flag | Data |
|---|---|---|
| 1 | **Structural growth decay** | Revenue growth 21.8% (FY24) → 15.3% (FY25) → 11.8% (FY26) → 10.4% guided (FY27). Quarterly YoY: 13.9 → 12.7 → 11.5 → 12.7 → 11.6 → 11.6 → 11.2 → **10.6** |
| 2 | **Margin expansion is partly an accounting roll-off** | Quarterly D&A collapsed **$25M → $12M** in Q2 FY27 (Auth0 acquired intangibles finishing amortisation). That's ~$50M/yr ≈ **155bp** of the **271bp** gross-margin gain (76.9% → 79.6%). Underlying improvement is real but roughly half the headline |
| 3 | **Margin beats bought by cutting growth spend** | Q2 FY27 SG&A **+3.3%** vs revenue **+10.6%**; SG&A fell from 49.3% to 46.1% of revenue. Operating income went $41M → $107M. Classic harvest-the-P&L signature |
| 4 | **Multiple, not business, drove the return** | Stock $62.93 (Apr 2026) → $208.52. EV/sales re-rated from ~3.3x to **~10.9x**. Up +136% YTD. Two earnings gaps of +30% (5/29) and **+29%** (8/27) on *margin* beats while revenue growth *decelerated* |
| 5 | **Goodwill is 80% of book equity, unimpaired** | Goodwill $5.578B vs equity $6.999B; tangible equity only $1.42B. Auth0 bought for ~$6.5B in 2021. Goodwill unchanged three straight years (5.588 → 5.586 → 5.578) with **zero** impairment — just as the amortisation "cover" on the acquired intangibles runs out |
| 6 | **Deteriorating working-capital drag** | Change in WC: −$53M (FY25) → **−$173M** (FY26) while revenue grew. Not receivables (DSO flat), so likely shorter billing durations / slower deferred-revenue build — a leading indicator for the deceleration already visible |
| 7 | **Insider filing density** | 30 Form 4s between June and October 2026, clustered on 6/22 and 9/17, into all-time highs. **Direction not verifiable from the data available** — the pattern (many distinct reporting owners, clustered dates) is equally consistent with mechanical RSU vest-and-sell. Do not over-read |

---

## 3. Beneish / Accruals — Detail

Already covered in §1. Explicitly: **the accruals and manipulation models are exculpatory.** SGAI at 0.928 is the one index that is "suspicious by construction" (SG&A falling relative to sales) — and here that is not a manipulation artefact, it's a disclosed cost-discipline programme. The correct read is *quality of earnings is genuine; the composition of earnings is the problem.*

**Altman Z-Score caveat:** the tool returns **1.681 "Distress"** — this is a **false positive**. It uses book equity for x4. Recomputing with market cap (x4 = 12.86): **Z ≈ 7.9, deep in the safe zone.** Net cash ~$2.1B, current ratio 1.36, debt cut from $1.30B to $0.42B. **There is no solvency or liquidity short here.**

---

## 4. Competitive Threat Assessment — **the real bear case**

- **Microsoft Entra is the structural problem.** Okta Workforce lists at ~$6/user; Entra ID P1 at ~$7/user — but Entra is *already bundled inside M365 E5*, so the marginal cost to an existing Microsoft customer is **effectively zero**. Okta is selling a standalone product against a line item in a bundle the buyer already owns. That is a permanent ceiling on price and on net-new workforce-identity seats. ETR's 2026 observatory still ranks **Entra ahead of Okta**.
- **Customer identity (Auth0) is commoditising** — developer-first CIAM is crowded with low-cost entrants; Auth0 is the premium-priced incumbent in a segment moving down-market.
- **The next battleground (agentic / non-human identity) is a knife fight** on day one, with Palo Alto/CyberArk and a wave of startups. OKTA enters it as one of many, not as the default.
- **Trust is the product.** OKTA has had two serious breaches (Lapsus$ 2022; the Oct 2023 support-system breach that exposed every customer-support user's data). In a category where the entire value proposition is "we are the safe chokepoint," one more incident is a step-function revenue risk that does not appear in any DCF.

**Gross margin has risen every year (70.6% → 77.4%)** — a genuine bull point on mix, but see flag #2: a large slice is amortisation mechanics, not pricing power. I would not underwrite further margin expansion from mix alone.

---

## 5. Management Red Flags

- **No accounting or governance red flag.** No auditor change, no restatement, no related-party issue identified. (Caveat: I could not retrieve 10-Q/10-K text — see gaps.)
- **Compensation structure is the issue, not integrity.** Founder-CEO Todd McKinnon; 18.6% of revenue paid in stock with only 13% of it retired is a slow transfer of value from shareholders to employees. Over five years this is a ~3.7%/yr headwind that fully offsets a third of the FCF yield.
- **Guidance posture is conservative, not promotional** — FY27 revenue guided up to $3.216–3.226B, and cRPO guided to decelerate to 11–12% when Q2 delivered 14%. Sandbagging, not hype. This cuts *against* the promotional-management red flag.

---

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes, but it is a valuation thesis, not a fraud thesis.**

The bear case in one line: *a 10%-growth identity vendor trading at 10.9x EV/sales, 53x non-GAAP EPS and ~110x SBC-adjusted FCF, where the EPS inflection came from cutting SG&A growth to 3% and from acquired-intangible amortisation rolling off, and where a third of GAAP profit is interest income.*

- EV (diluted) ≈ **$35.2B**. FY27E revenue $3.22B → **10.9x**; FY27E non-GAAP EPS $3.93 → **P/E 53x**; EV/EBITDA **40x**; PEG ≈ **4.8**.
- Rule of 40: passes on headline FCF margin (10.6% + 29.6% = 40.2 — right at the line). **Fails badly on SBC-adjusted FCF margin (10.6% + 10.9% = 21.5).**
- The stock already discounted the entire margin story in two 30% gaps. There is no remaining margin lever of that size, and revenue is decelerating into the print.

**The other side — and it is strong.** I have to be honest: this is not a broken business.
- **RPO $4.858B, +17% YoY; cRPO +14%.** Both are growing *faster* than revenue (+10.6%). That directly contradicts the "demand is cracking" thesis. (Caveat: RPO growth can be duration-driven rather than booking-driven, and duration isn't disclosed — but it is not dismissible.)
- **Subscription revenue +12%** vs total +11%; operating margin 5.6% → 13.3% YoY is real operating leverage, not just accounting.
- **Net cash, no refinancing risk, beta 0.73**, Fortress balance sheet means no forced catalyst.
- Accounting is genuinely clean — a short here has no "reveal" moment to trade on.

---

## 7. Contrarian Rating: **SHORT — low conviction, valuation-driven. Fraud/accounting short thesis: REJECTED.**

The forensic work is exculpatory. Beneish −2.65, negative accruals, Piotroski 8/9, stable DSO — an accounting short would be wrong and would lose money. The bear case rests entirely on multiple compression, and multiples can stay irrational longer than a short can stay solvent, especially with RPO +17% and momentum at all-time highs.

**If expressed, express it defensively:**
- **Preferred:** relative-value short vs. a basket of clean-FCF software peers, or a defined-risk put spread rather than a naked short. Do not short a 0.73-beta name outright into +136% YTD momentum.
- **Size:** small, ≤50bp NAV.
- **Invalidation / stop:** cRPO growth re-accelerating above 15%, or gross margin holding >79% *after* the amortisation roll-off annualises (i.e. proving the margin isn't accounting), or Entra displacement evidence turning in OKTA's favour.
- **Catalyst to wait for:** Q3 FY27 cRPO print guided to 11–12%. If it lands at 14%+ again, **cover.**

**Net: the bull case is currently stronger than the bear case. I would not initiate. Watchlist for a multiple, not a fundamental, break.**

---

**Data gaps (disclosed honestly):** 10-Q/10-K text retrieval failed (`No 10-Q found for OKTA`), so no disclosure-level forensics on related-party transactions, auditor changes, or RPO duration. SEC Form 4 data returned filing metadata only — **insider buy/sell direction could not be verified**, so flag #7 is not load-bearing. Sector peer set returned mega-caps (AAPL, MSFT, NVDA) rather than IAM comparables, so no clean peer-multiple table.
