# Short Analyst

- Symbol: SE
- Elapsed: 264.9s

---
# Forensic Short-Seller Analysis — Sea Limited (NYSE: SE)

**Snapshot:** Price ~$88.47, market cap ~$54.2B, net cash $3.05B, EV ~$51.1B. TTM (Q3'25–Q2'26): revenue $27.72B, net income $1.64B, EBITDA $2.86B → **P/S 1.96x, P/E 33x, EV/EBITDA 17.9x.** Stock is −50% from $196 (Sep-25).

---

## 1. Earnings Quality Assessment: **MEDIUM**

Not *Fraudulent Risk*. The manipulation models are clean, and I want to be explicit about that up front — this is not a Hindenburg-style accounting-fraud short. The problem is **quality of incremental earnings**, not veracity of reported earnings.

| Metric | Reading | Interpretation |
|---|---|---|
| Beneish M-Score | **−2.789** (Low risk) | Well below −2.22 soft threshold |
| Accruals ratio (2025) | **−0.1175** | Negative = high quality |
| Cash conversion (OCF/NI) | **319%** | Superficially exceptional — see caveat |
| Piotroski F-Score | **8/9** | Strong (only failure: dilution) |
| Altman Z | 1.53 "Distress" | **Misleading** — book equity x4. On market equity x4 = 3.24, Z ≈ **3.0, safe** |
| Gross margin | 44.7% (2025), 45.6% (Q2'26) | Stable, marginally down YoY (45.8% Q2'25) |

The F-Score of 8 and negative accruals force intellectual honesty: there is no evidence of channel stuffing, expense capitalisation games, or receivables manipulation. DSRI of 1.01 (receivables tracking revenue) rules out the classic stuffing signal. I checked receivables — $8.26B, **36% of revenue**, growing 37.7% vs revenue 36.4%, which trips the automated red flag. **The flag is a false positive:** the receivable is overwhelmingly the Monee consumer/SME loan book (gross ~$9.2B at YE25), not trade receivables. Say so plainly.

**The real quality issue is the cash conversion figure.** 319% OCF/NI in a year the loan book grew ~$4B is not a coincidence — credit-loss provisions are a non-cash add-back to operating cash flow while loan originations largely sit outside it. OCF of $5.03B is therefore not a clean measure of distributable cash for a business that is now materially a lender. Working capital contributed +$1.10B despite receivables rising ~$2.3B; that reconciliation is unverifiable with the data available and should be pulled from the 20-F. (Note: no 10-K/20-F text was retrievable via the filings tool — SE files as a foreign private issuer and the fetch returned nothing. **Governance/related-party review is therefore incomplete.** That's a gap, not an all-clear.)

---

## 2. Key Red Flags Found

**Red flag #1 — The profitability inflection. This is the core of the thesis.**
Revenue growth has accelerated all year. YoY *operating margin change* has simultaneously gone negative:

| Quarter | Rev growth YoY | Op margin | Δ vs prior-year |
|---|---|---|---|
| Q3'25 | 38.3% | 7.95% | **+327bp** |
| Q4'25 | 38.4% | 7.85% | **+167bp** |
| Q1'26 | 46.6% | 7.97% | **−146bp** |
| Q2'26 | 48.1% | 8.04% | **−123bp** |

Growth is accelerating from 38% to 48% while operating leverage has **flipped from sharply positive to negative**. Reported group adjusted EBITDA growth in 2026 has been ~9% against ~48% revenue growth, and guidance is for group adjusted EBITDA "at least flat" versus 2025 on ~40% revenue growth. This is not a demand problem — it is a **monetisation-quality** problem.

**Red flag #2 — Monee: credit cost is outgrowing credit revenue.**
Loan book: $9.2B YE25 (+80%) → $9.9B Q1'26 (+71%) → **$11.1B Q2'26 (+63%)**. Monee revenue +69% YoY to ~$1.4B. Provision for credit losses **+71.5% to $555.2M** (vs $323.7M). Provisions compounding *faster* than the revenue funding them is the definition of deteriorating unit economics — and it is the direct cause of Red Flag #1.

Two forensic points that the 1.0% "90-day NPL" headline conceals:
- **Denominator illusion.** A book growing 63% doubles roughly every 14 months. Any point-in-time NPL *ratio* on a fast-growing short-duration book is mechanically suppressed by new originations. Vintage-level loss data, not the ratio, is what matters.
- **Lag.** Charge-offs trail origination by ~4–6 months in this product set. The book added ~$4B in 12 months; the loss cohort on that $4B has not yet fully seasoned.
- **Scale vs equity.** $11.1B loan book against $12.65B of book equity = **88% of equity at risk**, inside a company the market values on e-commerce multiples.

**Red flag #3 — Phantom stock comp / real dilution.**
FY25 cash-flow statement reports **SBC = $0**, versus $716M (FY24) and $685M (FY23) — implausible for a 20,000+ person tech company. Yet diluted shares went 604.7M → 638.2M (**+5.5%**), and Q2'26 diluted 654.5M vs basic 612.5M (**+6.9% gap**). That is ~42M dilutive shares ≈ **$3.7B of annualised value transfer at $88**. Any "adjusted EBITDA" that adds back a zeroed SBC line is overstating economic profit. This is the single line item I would press management on.

**Red flag #4 — Take-rate ambition meets a hard ceiling.** Q4'25: Shopee revenue +35.8%, Shopee adjusted EBITDA +33% — no leverage *despite* raising seller take rates. Meanwhile TikTok Shop is the fastest grower (Indonesia 18–22% share vs Shopee 52–55%; Vietnam/Thailand tilting to TikTok) and already charges 21–24% on Mall FMCG — Shopee cannot under-price it forever. On top of that, Indonesia has mandated ≥50% service-fee cuts for eligible micro/small sellers: **direct regulatory confiscation of the primary profit lever in the largest market.**

**Red flag #5 — Garena is a single-franchise profit pool.** Q4'25 bookings +23.8% YoY but **−20% Q/Q**. A hit-driven Free Fire dependency with 20% quarterly variance is the segment funding the entire loss-leader expansion. High-margin, low-durability.

**Red flag #6 — Insider filing cadence.** 25 Form 4 filings between Sep 11 and Oct 19, 2026 — including four on Sep 21 and three on Sep 15/17. The metadata gives no transaction direction or size, so I cannot assert net selling; but this density is **not** consistent with routine vesting alone and needs verification before sizing a short.

**Red flag #7 — The tape has rejected every rally.** Aug 12, 2025 +19%; Mar 3, 2026 **−19%** on 34.8M shares (Q4 miss on provisions + Garena Q/Q decline); May 12, 2026 +13%; Aug 11, 2026 +14.6% **which fully round-tripped to −16% within seven weeks.** Buyers of good news are being distributed to. Lower highs: $196 → $178 → $131 → $123.

---

## 3. Beneish & Accruals Detail

| Index | Value | Read |
|---|---|---|
| DSRI | 1.01 | Neutral — no receivables inflation |
| GMI | 0.959 | Gross margin improved YoY |
| AQI | 0.722 | Asset quality improved |
| SGI | **1.364** | Main M-score driver: high-growth firms score worse by construction |
| DEPI | 1.279 | Depreciation rate slowing — mild aggressive-capitalisation flag |
| SGAI | **1.117** | **SG&A growing faster than sales — efficiency deterioration, corroborates margin compression** |
| LVGI | 0.911 | Leverage falling |
| TATA | −0.1175 | Excellent |

M = **−2.789**, comfortably in low-risk territory. **No manipulation case exists here.** Anyone pitching SE as a fraud short is wrong, and the SGI/SGAI readings are the only corroborating signals — both explainable by the margin story rather than by fraud.

---

## 4. Competitive Threat Assessment

**Moat: eroding at the edges, intact at the core.** Shopee's logistics density, local payments rails and merchant relationships in Indonesia/Vietnam are genuine and hard to replicate. But 2026 evidence shows **pricing power is weaker than the consensus moat narrative**:

- Take-rate increases produced *no* EBITDA leverage (Red Flag #4) — a market leader raising prices and getting nothing is a moat warning, not a strength.
- TikTok Shop is taking share in exactly the highest-monetisation markets (Vietnam, Thailand, urban Indonesia).
- Indonesian fee-cut regulation caps the take-rate lever outright.
- Cross-border competition (Temu/Shein) plus tariff/de-minimis volatility pressures the low-ASP segment Shopee monetises best.

The moat protects *volume share*, not *margin*. That distinction is the whole short.

---

## 5. Management & Governance

Mixed. Positives: no auditor changes found, no evidence of related-party self-dealing surfaced (though the 20-F was unavailable — **gap**), founder-led with aligned equity, no dividends being drained.
Negatives: (a) SBC reported as zero while diluting 5.5%/yr — an accounting choice, not an error; (b) heavy Form 4 cadence in Sep–Oct 2026 requiring verification; (c) promotional framing — "at least flat" EBITDA guidance buried inside 48% growth headlines; (d) FY25 filing date of 2026-04-17 for a Dec year-end is a slow close.

---

## 6. Short Thesis Summary — Is there a credible bear case?

**Yes, but it is a margin/credit short, not an accounting short.**

*The thesis:* Sea is converting a high-quality, capital-light gaming/marketplace cash flow into a low-quality, balance-sheet-heavy consumer lending book. Group revenue is accelerating to 48% precisely *because* the mix is shifting toward credit-funded e-commerce and Monee. That revenue is arriving with negative incremental operating leverage (YoY margin delta: +327bp → −123bp in four quarters), with provisions growing faster than the Monee revenue that justifies them, against a loan book now equal to **88% of book equity**, with a 4–6 month charge-off lag hiding the 2026 vintage, in a high-rate world (US 10yr 5.14%). If SEA consumer credit normalises, the provision line — not e-commerce demand — sets 2027 EPS, and consensus $4.71 is 25–30% too high. Meanwhile Garena's −20% Q/Q bookings shows the profit pool is narrow.

*Bear math:* 2027 EPS $3.30–3.60 vs $4.71 consensus → 25x current price. De-rate to 20x → **$66–72 (−20 to −25%)**.

**The other side — and it is genuinely strong.** Revenue is *accelerating*, not decaying; gross margin is intact at ~45.6%; the balance sheet carries $12.8B cash and net cash of $3.0B; FCF was $4.5B in 2025; Beneish −2.79 and accruals −0.12 are clean; Monee reportedly earns 20%+ adj EBITDA margins; and 2028 consensus EPS of $5.86 puts the stock at **15x** with a $4.06–$7.74 dispersion that reflects real optionality, not just risk. The stock has already halved — 90% of a classic "overvalued growth" short's edge is gone. Shorting a net-cash, share-gaining market leader whose revenue is accelerating is how short sellers get carried out; beta is 1.55 and single-day earnings gaps have run ±19%.

---

## 7. Contrarian Rating: **SHORT** (moderate conviction, tactical — NOT a Strong Short)

**Why not Strong Short:** no fraud signal exists (Beneish −2.79, accruals −0.12, F-Score 8), the balance sheet is net cash, revenue is accelerating, and the stock is already −50%. The "overvalued/aggressive-accounting" short thesis is dead. Refexively bearish here would be malpractice.

**Why not Reject:** the margin inflection is real, quantified and four quarters old; provisions are outrunning revenue; the loan book is 88% of equity; and guidance for flat group EBITDA on 40% growth is management conceding the point.

**How to trade it:** small size, defined risk. Catalysts are the Q3'26 print (~Nov 2026) and any Indonesian fee-regulation detail or Monee NPL/vintage disclosure. Invalidation: two consecutive quarters of *positive* YoY operating-margin delta with provisions growing slower than Monee revenue — that would prove the credit book is seasoning normally and kill the thesis. Stop above ~$125 (the 2026 lower-high). Verification tasks before adding: Form 4 net insider flow, and the 20-F credit-loss vintage table and SBC note.

**Earnings Quality: MEDIUM. Fraud Risk: LOW. Bear case: CREDIBLE but not exceptional. Rating: SHORT.**
