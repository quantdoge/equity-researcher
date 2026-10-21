# Short Analyst

- Symbol: RVMD
- Elapsed: 148.4s

---
# RVMD — Forensic Short-Seller Analysis

## Framing Note (Important)

RVMD is a **pre-revenue/early-commercial precision oncology company**, not a candidate for classic accounting forensics. Three of the requested screens return technically correct but economically meaningless output:

| Screen | Result | Forensic Read |
|---|---|---|
| Beneish M-Score | **-3.51** ("low risk") | Meaningless: DSRI=1, SGI=1, receivables/COGS ≈ 0. No revenue to manipulate. |
| Accruals ratio | **-0.099** ("ok") | Actually *conservative* — negative accruals because losses are funded by SBC, not accrual inflation. |
| Altman Z | **-0.995** "Distress" | Artifact. Retained earnings -$2.87B from cumulative R&D losses, not insolvency. Company holds **$3.94B cash**. |
| Piotroski F | **1 / 9** "Weak" | Artifact — scores 0 on all profitability/turnover tests by construction. |
| Earnings Quality Score | **26 / 100** | Artifact — "cash conversion 0.79" just reflects SBC + prepaid/wc timing on a zero-revenue base. |

**There is no accounting manipulation signature here.** I could not construct a fraud case, and I won't manufacture one. The only live bear case is **valuation and binary catalyst risk** — which is a very different (and much weaker) short than the mandate usually targets.

---

## 1. Earnings Quality Assessment: **High (for a clinical biotech)**

- **Revenue: $0** through Q2 2026. No receivables, no inventory, no channel-stuffing surface area at all.
- Net receivables $0 (vs. $4.7M in 2022 — that was Sanofi collaboration revenue, now wound down).
- Gross margin is **negative but not a margin issue** — Q1 2026 "cost of revenue" $4.5M is pre-approval manufacturing expense that cannot be inventoried. Normal.
- **No accrual inflation, no capitalisation games detected.** R&D is expensed ($1.18B operating loss in 2025). Clean.
- **Assessment: High quality bookkeeping, no fraud risk identified.**

## 2. Key Red Flags Found

**A. Dilution is severe and accelerating — the single most defensible bear point**
- Shares outstanding: **80.6M (2022) → 113.1M (2023) → 167.7M (2024) → 190.1M (2025) → ~214M (now)** = **+166% in under four years**.
- +10.9% in just six months (Q4'25 → Q2'26).
- Q2 2026 raise: ~**$2.1B net proceeds** plus debt, taking total debt from $159M → **$642M** (they levered up while the equity window was open — prudently, but note it).
- Q1 2026 SBC hit **$87.3M in a single quarter** vs. $118M for all of FY2025 — annualising toward **~$350M (~0.8% of market cap/yr)**.

**B. Burn accelerating into launch**
- FY2025 FCF: **-$914M**. Q2 2026 FCF: **-$390M** → ~**$1.56B annualised**.
- Cash $3.94B → roughly **2.5 years runway** on current burn, before launch-era commercial spend.
- **Another raise is highly likely**, and management's incentive is now to raise aggressively while the stock is at $196 post-approval.

**C. Insider selling at scale into post-approval strength**
- ~**101 insider transactions in the past quarter**, overwhelmingly sales. CDO Alan Sandler (Sept 29, 2026 options exercise + sale), CFO Jack Anders, one insider (Kelsey) with ~$26.4M across 12 transactions. CEO **Mark Goldsmith's sale is reported as the largest insider sale in over a year**.
- Filings cluster on 6/18–6/23/2026 and 9/18/2026 — classic vest-and-sell / 10b5-1 patterns. **Caveat: I could not verify net direction from the filing metadata tool; much of this is likely mechanical RSU-related and 10b5-1 pre-scheduled.** Selling into a 2x is rational for executives who had illiquid paper for six years. Still, **zero offsetting open-market purchases observed** — nobody on the inside is buying at $196.

**D. List price $39,800/month (~$478k/yr) into a Medicare-heavy population**
- ~70% of PDAC patients are 65+; payer friction, gross-to-net erosion and eventual IRA negotiation are real revenue-headwind risks, and the price invites competitive/political attack.

**E. Extremely wide analyst dispersion = the "consensus" is fiction**
- 2030 revenue range: **$3.7B to $13.5B (3.7x spread)**. 2030 EPS: **$4.62 to $27.82 (6x spread)**. Anyone citing "consensus $7.5B" is quoting a midpoint with no predictive power.

## 3. Beneish / Accruals — Verdict

Non-diagnostic. M-Score -3.51 reflects a company with no revenue, no receivables and no inventory. FY2025 accruals of **-$0.099** of assets are *negative* (income better than operating CF could have been), driven by SBC of $118M and working capital. If anything, cash flow quality is **higher** than reported earnings.

**I found no forensic accounting basis for a short.**

## 4. Competitive Threat Assessment: **Moderate — this is the least-bad part of the bear case**

**Genuine moat:** first-in-class, first-approved *pan-RAS(ON)* agent. Label is **broader than expected**: metastatic PDAC *with or without an identified RAS mutation*, and **no companion diagnostic required**. RAS mutations occur in >90% of PDAC, so RVMD owns the whole market rather than a G12C/G12D sliver. Companion diagnostics would normally be the gatekeeper for competitors; not here.

**Erosion vectors:**
1. **Erasca** and others are explicitly positioning pan-RAS programs against Rasonque — the field is now crowded and every major pharma with a RAS asset is racing.
2. **Selective G12D agents** (e.g., RVMD's own zoldonrasib, AZN and Chinese entrants) may offer better tolerability in subsets — the classic "pan-first, then segment away from the pioneer" pattern that eventually compresses price and share.
3. **The real value is front-line PDAC and NSCLC/CRC.** All the incremental upside sits in trials not yet read out (RASolute 304 / 303 / 309, zoldonrasib combos). Approval in 2L does **not** de-risk front-line outcomes.

**But the toll-keeping risk I expected did not materialise** — discontinuation due to AEs was **1.2% vs 11.2%** on chemo, and the label tolerates Grade 2 rash/stomatitis/diarrhoea with restart guidance. My standard "multi-selective RAS = narrow therapeutic index" bear argument is **weak on the evidence**.

## 5. Management & Governance Red Flags: **Mild**

- **No related-party transactions, no auditor change, no restatement, no SEC investigation found** in the material reviewed.
- **CLEAN on the biggest test that matters:** RASolute 302 was a *plenary* ASCO 2026 presentation with a **real, multi-institutional Phase 3 dataset** — HR ~0.4, mOS 13.2 vs 6.7 months, 60% reduction in risk of death, FDA approval and Breakthrough designation. **This is not an exaggerated press release; this is genuine, verified, life-extending data.** Promotional-language red flags that normally apply do not apply here.
- **Real yellow flag:** executive selling de-risks management personally while retail and institutions hold the front-line readout risk. That's incentive misalignment, not fraud.

## 6. Short Thesis Summary: Is there a credible bear case?

**The bear case exists, but it is a valuation/FCF-dilution case, not a fraud case.**

**Valuation math (the one real edge):**
- Market cap **$42.1B**; net of $3.94B cash and $642M debt → **EV ≈ $38.8B**.
- For a 10% annual return, RVMD needs ~**$56B+ EV by 2030**. At a mature oncology multiple of 5x sales that requires **~$11B+ of 2030 revenue** — i.e., **the top quartile of the analyst range**, not the midpoint.
- Another way: the stock now prices **2L PDAC + front-line PDAC winning + at least one of NSCLC/CRC working.** There is **no margin of safety** for a front-line failure.

**Downside scenarios:**
| Scenario | Peak sales | Implied equity value | Per share |
|---|---|---|---|
| 2L PDAC only, modest expansion | $3–4B | $16–24B | **$75–115** (−45% to −60%) |
| Front-line PDAC works | +$4–6B | $35–50B | $165–235 (flat to +20%) |
| Full RAS franchise (PDAC 1L/2L + NSCLC + CRC) | $12B+ | $60–80B | $280–375 (+45% to +90%) |

**Probability-weighted, the risk is roughly symmetric with a positive skew** — the opposite of what a short-seller wants. The catalyst that would break the stock (a front-line miss) has maybe 20–35% probability and reads out in 2027–2028; the carry cost of a short into that (beta 1.40, crowded biotech, 22 analysts almost all Buy) is punitive.

**What I checked and could NOT substantiate:**
- No receivables/inventory manipulation (no revenue to manipulate).
- No accrual inflation, no capitalisation games, no auditor issues, no insider buying being masked.
- The clinical data is real and independently verified, not promotional.

## 7. Contrarian Rating: **Reject Short Thesis**

**This is not a short.** The bear case reduces to "expensive at 5.2x 2030 revenue with no margin of safety, plus 11% annual dilution and a high-price label" — all true, all already visible to a sell-side that still has 21 of 22 at Buy with a $207–260 target. Shorting a first-in-class, FDA-approved, survival-doubling asset with 1.2% discontinuation because it trades at a full multiple is how short sellers lose their capital.

**What I would actually do:**
1. **Stand aside, do not short.** Batting into a -$56B-EV-required valuation is a hedge-fund expression, not a forensic short.
2. **Watch the Q3/Q4 2026 launch numbers** for the first real test: gross-to-net, duration of therapy in real-world (less-fit) patients, and whether 2L PDAC scripts track the trial population. The Phase 3 population was fitter than the commercial population — **that's the genuine vulnerability**, and it will show up as disappointing duration-of-therapy before it shows up as anything else.
3. **The one legitimate short setup** would be a pre-announcement run-up into the RASolute 304 (front-line) readout, sized small and defined-risk. Not now.

**Other side, stated fairly:** the bull case is strong and I could not break it. An oral pan-RAS inhibitor that nearly doubles survival in a cancer with a ~6-month historical survival, approved without a companion diagnostic, with 1.2% discontinuation, targeting >90% of pancreatic tumours and with NSCLC/CRC optionality, is a legitimate $40B+ oncology franchise candidate. **My conclusion is "no edge," not "overvalued."** Scepticism should be calibrated, not reflexive.
