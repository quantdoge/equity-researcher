# Short Analyst

- Symbol: ALNY
- Elapsed: 90.6s

---
# FORENSIC SHORT-SELLER ANALYSIS — ALNY (Alnylam Pharmaceuticals)

**Price at analysis: $150.57 (20 Nov 2026) · Market cap ~$20.2B · 134M diluted shares · Net cash balance sheet**

---

## 1. Earnings Quality Assessment: **MEDIUM**

The accounting is **clean**. I went looking for a fraud and did not find one. What I found instead is a *narrative* problem dressed up as a numbers problem: a structural gross-margin collapse, a revenue line contaminated by large non-product items, and a 2026 GAAP EPS figure that is a pure accounting artifact.

| Test | Result | Read |
|---|---|---|
| Accruals ratio (2025) | **−4.24%** | Conservative. Negative for 4 consecutive years (−4.2%, −6.4%, −14.2%, −16.6%) |
| Cash conversion (OCF/NI) | **1.67x** | Well above the 1.0x quality threshold |
| FCF conversion | **1.48x** | Healthy |
| Beneish M-Score | **−1.947** | "Moderate risk" band, but see §3 — benign in composition |
| Piotroski F-Score | **7/9** | Moderate-strong; fails only dilution and gross margin |
| Goodwill / intangibles | **$0** | Zero impairment risk. Rare and genuinely favourable |

**The critical adjustment most screens will miss:** Q3 2026 net income of **$2,167M** embeds a **~$1.87B non-cash tax benefit** (release of a deferred-tax-asset valuation allowance). Operating income was only $346M. Any screen showing ALNY on a trailing P/E of ~9x ($150 ÷ ~$16 GAAP EPS) is looking at a mirage. Normalised 2026 EPS run-rate is closer to **$6.00–6.50**.

Second adjustment: FY2025 operating cash flow of $524M includes a **$348M stock-compensation add-back**. OCF ex-SBC = **$176M**; FCF ex-SBC = **$117M**. On a $20.2B market cap that is ~170x. Alnylam is a *genuinely* profitable business only once you accept SBC as free — it is not. SBC runs 9.4% of revenue and diluted shares have grown 127.7M → 138.2M (+8%) in eighteen months.

Third: the FY2025 "effective tax rate" was **~3%** ($9.5M tax on ~$323M pre-tax). Normalisation to ~23% is a direct forward EPS headwind that consensus has been slow to absorb.

---

## 2. Key Red Flags Found

**Flag 1 — Gross margin is collapsing, and this is the whole story.**
Cost of revenue as a % of total revenue, by quarter:

| | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | Q3'26 |
|---|---|---|---|---|---|---|---|
| COGS % | 11.9% | 18.5% | 15.8% | 24.4% | 18.1% | 23.1% | **24.8%** |

On **product revenue only**, Q3 2026 COGS was $362M on $1,292M = **28.0%**, i.e. a **72.0% product gross margin**, versus ~87% in Q1 2025. FY gross margin has gone 83.0% (2023) → 85.6% (2024) → 81.8% (2025) → ~75% (Q3 2026 run-rate). That is a **~1,200–1,500bp erosion in six quarters** for a company whose entire bull case rests on platform leverage. The Beneish GMI of 1.047 confirms it independently. This is the signature of **pricing power loss in ATTR-CM**, compounded by royalty step-ups and Onpattro write-downs. It is not a one-quarter blip.

**Flag 2 — ~23% of FY2025 revenue was not product revenue.** Q3 2025 total revenue was $1,249M, but implied product revenue was only ~$850M (TTR ~$723M + Rare ~$127M). Roughly **$400M of one-time collaboration/licensing revenue** sat in that quarter. This explains the absurd "Q3 2025 +149% growth" and the following "Q3 2026 +16.7% growth" — neither number means anything. Underlying product growth is **+52%**, decelerating from +187% (Amvuttra, Q1 2026).

**Flag 3 — Receivables outrunning revenue.** FY2025: receivables **+91.9%** vs revenue **+65.2%** — tool flags `red_flag: true`. DSO has drifted from 65.5 (2023) → 65.8 (2024) → **76.4 days** (2025). DSRI 1.161. Notably this appears in a year when accruals were *negative*, which argues against outright channel stuffing — it is more consistent with geographic mix shift and distributor terms. **Watch it, don't hang the thesis on it.**

**Flag 4 — Inventory stuffing at the sequential level.** Management disclosed that Q3 2026's $99M sequential U.S. TTR increase comprised "$81M demand, a **$17M inventory benefit**, and ~$10M favorable gross-to-net adjustments." Roughly **$27M of a $99M sequential gain (~27%) was non-demand**. Numerator-level quality is slipping even as the top line grows. (Note: *annual* inventory days are actually falling — 44.6 vs 88.6 vs 104.8 — so the balance sheet is not deteriorating. A genuinely mixed signal.)

**Flag 5 — Fiscal-year seasonality is being managed into guidance.** Q4 2025 COGS jumped to 24.4% from 15.8% the prior quarter, the same quarter revenue fell sequentially. Combined with the Q2/Q3 2026 margin step-down, the 2026 guidance cut ("on track to achieve 2026 financial guidance" while having cut the range by $200M in July) suggests a pattern of resetting expectations after the fact rather than before.

---

## 3. Beneish M-Score and Accruals Analysis

**M = −1.947** → lands in the "moderate risk / possible manipulator" band (−2.22 to −1.78). **I explicitly reject the manipulation reading.** Decomposition:

| Index | Value | Direction | Interpretation |
|---|---|---|---|
| DSRI | 1.161 | ⚠ Unfavourable | DSO drift — the only genuine warning |
| GMI | 1.047 | ⚠ Unfavourable | Confirms margin deterioration (corroborates Flag 1) |
| AQI | 0.707 | ✓ Favourable | Asset quality improving sharply |
| SGI | 1.652 | ⚠ Mechanical | High sales growth — penalises *every* fast grower |
| DEPI | 1.036 | Neutral | — |
| SGAI | 0.751 | ✓ Favourable | Strong SG&A operating leverage |
| LVGI | 0.855 | ✓ Favourable | Deleveraging |
| TATA | −0.0424 | ✓ Favourable | Negative total accruals = conservative accounting |

**Five of eight indices are favourable.** The elevated score is driven almost entirely by SGI — a mechanical function of 65% revenue growth — plus the DSO drift. This is the classic **false positive for a hyper-growth commercial-stage biotech**. Combined with negative accruals across four straight years and cash conversion of 167%, the conclusion is firm: **this is not an accounting fraud.**

**Where the real earnings distortion sits** is the sub-operating line. FY2025 operating income was $502M (13.5% margin), but net income was $314M (8.4%). The $253M gap is "interest expense" — which is **implausible as debt cost** on only $1.28B of largely convertible debt (~20% implied rate). This is almost certainly the **effective cost of the Blackstone royalty monetisation**, buried below the operating line. Economically it is a *cost of goods*, not financing — so the true operating margin is materially lower than the 13.5% headline. Deduct it, apply a normalised 23% tax rate, and FY2025's sustainable net margin is closer to **5%**.

---

## 4. Competitive Threat Assessment: **SEVERE — the core of the bear case**

ATTR-CM is the entire growth engine, and Alnylam is **third to market**:

- **Pfizer (Vyndaqel/Vyndamax)** — entrenched incumbent, massive primary-care cardiology footprint.
- **BridgeBio (Attruby/acoramidis)** — Q3 2026 revenue **$222.4M**, 2026 sales tracking **>$1B**, explicitly targeting **30–40% of the ATTR-CM market**. Oral, stabiliser mechanism, price-aggressive.
- **Alnylam (Amvuttra)** — Q3 2026 **$1,012M** across all indications, +52%, but repeatedly **"falls short of expectations"** and forced a **$200M guidance cut** (to $4.2–4.5B) in July 2026.

The moat question is answered by the gross margin: **72% and falling** is what a third entrant with a reimbursement-fighting payer base looks like. The mechanism (RNAi, quarterly subcutaneous dosing) is differentiated on convenience and outcomes, but it is *not* defending price.

**The pipeline gap is the underappreciated problem.** Nucresiran in ATTR-CM is guided to launch **"by 2030"** — and this quarter they *expanded* TRITON-CM enrolment from 1,750 to 2,250 patients, which adds cost and time. Brezosiran (Huntington's) goes pivotal in 2027 at the earliest. Meanwhile the Rare franchise (Givlaari + Oxlumo) grew only **+12%**. So **Amvuttra alone must carry 2027–2029**, against two well-capitalised competitors, with deteriorating unit economics. That is a three-year air pocket.

---

## 5. Management & Governance Red Flags: **LOW–MODERATE**

**Positives (stated plainly):** no auditor change, no restatement, no related-party games, $0 goodwill, no buybacks/leverage games, 100% of assets are hard assets. The July guidance cut was blunt rather than evasive. The CEO certification is unremarkable. This is **not** a governance short.

**Concerns:**
- **Form 4 cadence is heavy and one-directional-looking.** 25 filings in 2026, clustered hard: **11 separate Form 4s on 2026-05-22**, six on 2026-03-06, four on 2026-11-12. The May cluster preceded the **−28.5% July 30 collapse** by ~10 weeks. *Honest caveat: the filing metadata available to me does not disclose transaction direction or share counts, so I cannot confirm these are net sales rather than option exercises. The pattern is consistent with systematic 10b5-1 programmes — but I observed no insider buying into a 70% drawdown, which is itself informative.*
- **Piotroski F7 (no dilution) = 0.** Shares +8% in eighteen months while repurchasing nothing. Shareholders are funding the P&L.
- **Guidance credibility:** the "on track to achieve 2026 financial guidance" language in the Q3 release sits awkwardly against a $200M mid-year cut.

---

## 6. Short Thesis Summary — and Why It Is Mostly Spent

**The bear case** (all evidence-backed): decelerating product growth (+52% and falling, vs +187% a year ago); gross margin down ~1,500bp; $200M guidance cut; share loss to Attruby and Pfizer; no new product until 2030; SBC-funded "profitability"; and a 2026 GAAP EPS inflated by $1.87B of non-cash tax benefit that will make the stock screen artificially cheap.

**But here is what a reflexive bear would miss — and the reason I am not recommending a fresh short:**

The thesis already worked. The stock closed at **$491.22 on 20 Oct 2025** and trades at **$150.57 today — a 69% drawdown**, including two catastrophic single-day gaps (**−28.5% on 30 Jul 2026** after the guidance cut, ~$12B of market value erased; **−25.1% on 29 Oct 2026**). Every item in the bear list above is now public, widely published, and in the price. There is no informational edge left in "Amvuttra is losing share to Attruby."

**Scenario maths at $150.57 (EV ~$19B):**

| Scenario | 2028 revenue | GM | Normalised net income | Multiple | Value/share |
|---|---|---|---|---|---|
| Bear (share loss, GM 72%, opex creep) | $5.65B | 72% | ~$560M | 20x | **~$84 (−44%)** |
| Bull (consensus, GM 78%, leverage returns) | $7.39B | 78% | ~$1.73B | 25x | **~$321 (+113%)** |

That is a near-symmetric distribution around a ~3.4x EV/sales, ~25x normalised-earnings stock with **$2.9B of cash, ~$1.0B of long-term debt, and positive operating cash flow**. Consensus 2028 EPS dispersion is a giveaway: low estimate **−$3.63**, high **+$25.79** — the market has no idea, and at $150 that uncertainty is fairly compensated.

**A note on the tools' scary outputs, which I do not accept as bear evidence:** the Altman Z-Score of **−0.02 ("Distress")** is a false positive. X2 is −1.35 purely because of a **$6.7B accumulated deficit** built over 20 years of legitimate R&D losses, and X4 penalises book (not market) equity. A company with $2.9B cash, $1.0B of long-term debt, positive OCF and no goodwill is not in distress. Citing this Z-score would be exactly the reflexive bearishness that destroys short-seller credibility.

---

## 7. Contrarian Rating: **NO EDGE** (lean tactical short on strength only)

- **Reject the fraud/manipulation thesis outright.** Negative accruals across four years, 1.67x cash conversion, zero goodwill, clean audit trail. This is not a Hindenburg name.
- **The fundamental bear case is real but priced.** At 3.4x EV/product sales and ~25x normalised earnings, post a 69% decline, with a net-cash balance sheet, the risk/reward no longer favours initiating a short.
- **The single most actionable insight for the portfolio is not "short ALNY" — it is "do not be long ALNY on the basis of its P/E."** The $1.87B DTA benefit creates a trailing P/E of ~9x that will mechanically reverse and make the stock
