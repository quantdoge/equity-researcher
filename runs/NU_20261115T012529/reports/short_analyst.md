# Short Analyst

- Symbol: NU
- Elapsed: 92.2s

---
# NU Holdings (NU) — Forensic Short-Seller Analysis

**Price $13.22 | Market cap $63.9B | Q3'26 ROE 32% | P/E (TTM) ~16.5x | P/B ~4.5x**

---

## 1. Earnings Quality Assessment: **MEDIUM–HIGH**

The reported numbers survive the core forensic tests. I went looking for manipulation and did not find it.

| Metric | FY25 | FY24 | FY23 | Verdict |
|---|---|---|---|---|
| Accruals ratio | **-0.0084** | -0.0086 | -0.0054 | Clean (negative) |
| Cash conversion (OCF/NI) | **1.22x** | 1.22x | 1.23x | >100% = quality |
| FCF conversion | **1.22x** | 1.13x | 1.06x | Quality |
| Receivables growth vs revenue | 38.7% vs 43.0% | -4.4% vs 44.8% | 61.5% vs 69.7% | **No channel stuffing** |
| DSRI (Beneish) | **0.97** | — | — | Receivables lagging revenue — *bullish* |
| SBC / net income | 9.5% | 13.8% | 20.6% | Improving |

Three consecutive years of negative accruals and a cash conversion ratio persistently *above* 1.0x is the opposite of what a fraud looks like. Revenue is growing slower than the loan book, not faster — the classic channel-stuffing signature is absent. **Rating: Medium-High quality, with one genuine disclosure concern (below).**

**Caveat I must state plainly:** operating cash flow for a bank is heavily contaminated by deposit inflows and loan-book movements, so OCF/NI is a weaker signal here than for an industrial. I weight it, but I don't lean on it.

---

## 2. Key Red Flags Found

**Red Flag #1 — Provisions are growing at 2x the rate of the loan book. This is the real story.**
Deriving implied credit provisions (cost of revenue less interest expense) from the quarterly data:

| Quarter | Revenue | Interest exp | Implied provisions | % of revenue |
|---|---|---|---|---|
| Q3'25 | $4,173M | $1,276M | $951M | 22.8% |
| Q2'26 | $5,520M | $1,557M | $1,464M | 26.5% |
| Q3'26 | $5,602M | $1,572M | **$1,668M** | **29.8%** |

Provisions **+75% YoY** against revenue +34%. Management's own disclosure confirms the cause: **90+ day NPLs rose to 7.3% from 6.9% in Q2'26 and 6.5% in Q1'26** — an 80bp deterioration in two quarters, with 15–90 day NPL at 4.9% (still building). This is a seasoning consumer-credit book rolling over.

**Red Flag #2 — Gross margin (revenue less cost of revenue) is contracting.**
Q3'26 42.2% vs Q3'25 46.6% — **440bp of compression**. Because interest expense actually *fell* as a share of revenue (30.6% → 28.1%), the entire compression is credit cost. Pricing power is intact on the asset side; loss content is not.

**Red Flag #3 — Revenue growth has decelerated violently, and the tool's "stable" label is wrong.**
YoY: 24.4% → 23.1% → 33.9% → 46.1% → **64.6% (Q4'25)** → 53.4% → 49.9% → **34.2% (Q3'26)**.
Sequential revenue growth: +8.9%, +5.9%, +10.8%, **+1.5%**. Net income sequential: +21.6%, **+2.9%**. Growth has not merely decelerated — it has nearly stalled quarter-on-quarter at the same moment credit costs accelerate. That combination is the late-cycle signature.

**Red Flag #4 — Balance sheet transformation: liquidity down, wholesale debt up.**
Cash & short-term investments fell from **$23.1B to $16.1B (-30%)** while total assets grew **+50%**. Cash/STI as a share of assets collapsed from 46.4% to 21.6%. Simultaneously total debt went from **$887M to $5,211M (+487%)**. Loan growth is being funded by running down the securities book and adding wholesale funding. Defensible as balance-sheet optimisation — but it reduces the liquidity cushion exactly as NPLs rise.

**Red Flag #5 — The SG&A line has broken comparability.**
FY25 SG&A of $602M vs FY24 $1,439M — a **58% absolute decline** while revenue grew 43%. That is not operationally possible; it is a reclassification. The residual "other opex" bucket (revenue less CoR, SG&A, and operating income) tripled from **$866M to $2,652M**. Roughly $1.8B of expense has moved into a line the standard dataset does not identify. This needs to be verified directly against the 6-K cost breakdown. It is a *transparency* flag, not evidence of fraud — but any analyst modelling "operating leverage" off the SG&A line is being misled.

**Red Flag #6 — Asset turnover has peaked.** Revenue/assets: 0.177 (FY23) → 0.222 (FY24) → **0.212 (FY25)**. The balance sheet is now growing faster than the P&L. Each incremental dollar of assets is generating less revenue — margin compression plus capital bloat.

---

## 3. Beneish M-Score and Accruals Analysis

**M-Score: -1.62 ("HIGH RISK — likely manipulator"). I am rejecting this signal as a false positive.**

The decomposition makes the case:

| Index | Value | Interpretation |
|---|---|---|
| **AQI** | **2.071** | *Mechanical artifact.* "Current assets" exclude the loan book, so AQI spikes as loans grow from 25% to 53% of assets. Not an accounting signal. |
| **SGI** | **1.43** | *Growth artifact.* Beneish is documented to over-flag fast growers. |
| **SGAI** | **0.293** | *Reclassification artifact* (see Red Flag #5). |
| DSRI | 0.97 | **Clean** — the actual manipulation vector |
| TATA | -0.0084 | **Clean** — negative total accruals |
| GMI | 1.024 | Mild margin deterioration (real, ~240bp) |
| DEPI | 0.801 | Not meaningful (asset-light) |
| LVGI | 1.002 | Neutral |

Strip the three artifacts and there is **nothing left** of the manipulation thesis. Every *genuine* manipulation detector — DSRI, TATA — points the right way. The model is simply not specified for a deposit-funded lender.

**Altman Z-Score: 0.219 ("Distress"). I reject this outright.** X1 of -0.3255 is current liabilities (deposits) exceeding current assets — the structural definition of banking. Applying Altman to a bank is malpractice; I would be embarrassed to present it as evidence.

**Piotroski F-Score: 4 (Weak).** This one I accept, because the failures are substantive and corroborate my findings: no ROA improvement (F3=0), **leverage increased (F5=0)**, dilution (F7=0), gross margin down (F8=0), asset turnover down (F9=0).

---

## 4. Competitive Threat Assessment

**This is where the bull case is genuinely at risk, and where I think consensus is too relaxed.**

- **Nubank is the *high-cost* lender, not the low-cost one.** Reuters (Sept 2026) reports revolving credit rates of **103.37% p.a. at Nubank** vs 178.69% at a peer. Nubank's growth has come from serving riskier borrowers at very high rates. That is precisely the segment most exposed when unemployment rises or when politicians need a villain.
- **Political/regulatory tail risk is under-priced.** Brazilian voters are "feeling burned by the fintech revolution" ahead of an election cycle, with card rates at triple digits as the obvious target. Congress has repeatedly floated usury caps. A cap on revolving credit would hit the highest-yield, highest-margin slice of the book directly. This is a fat left tail that no accrual ratio captures.
- **Selic at ~14.75%** keeps consumer debt-service burdens extreme — the mechanism by which NPLs keep climbing. Nubank's deposit franchise helps funding cost, but deposit costs track the policy rate, so the tailwind is limited.
- **IMF research** estimates fintech competition cut Brazilian lending rates by 2.7pp between 2018–2024. Nubank was the disruptor; it is now the incumbent being disrupted by Mercado Pago, PicPay, and the digital arms of Itaú, BB and Caixa. Moat erosion on the *pricing* side is the durable threat.
- **Mexico/Colombia** offer growth optionality but are unseasoned books — new-cohort credit risk on top of a deteriorating Brazilian core.

---

## 5. Management Red Flags

- **Persistent insider selling.** ~30 Form 4 filings in six months (clustered 11 Aug, 26 Aug, 27 Oct 2026). CEO David Vélez sold 33M shares (~3.5% of his holding) in Aug 2025 and continued selling into Oct 2026. Much of this is characterised as in-kind sales to cover option exercise costs and 10b5-1 programs — normal for a 2021-vintage founder-CEO, and I will not overstate it. But it is a **persistent supply overhang with no offsetting insider buying**, and the cadence clusters immediately post-earnings.
- **Dilution:** diluted shares 4,858M → 4,888M → 4,907M (~0.5%/yr). SBC $272M = 9.5% of net income. Modest but relentless.
- **Dual-class control** — founder-controlled, standard governance discount.
- **No evidence found** of auditor changes, related-party self-dealing, or aggressive capitalisation. Goodwill & intangibles are only $1.0B (1.4% of assets) — no roll-up accounting games.

---

## 6. Short Thesis Summary — Is there a credible bear case?

**Yes, but it is a credit-cycle and deceleration thesis, not a fraud thesis.** I want to be unambiguous: I could not build an accounting-fraud short on this company, and I am not going to pretend otherwise. The books are clean on the metrics that detect fraud.

The credible bear case:

> Nubank's growth engine is decelerating faster than the market expects (YoY revenue 64.6% → 34.2%, sequential +1.5%) at precisely the moment its credit book is seasoning badly (90+ NPL 6.5% → 7.3% in two quarters; implied provisions +75% YoY vs revenue +34%), compressing gross margin 440bp. Balance-sheet efficiency is deteriorating (asset turnover down, debt +487%, cash buffer -30%). The franchise earns 32% ROE by charging 103% on revolving credit — a rate that is politically unsustainable in an election cycle with Selic at 14.75%. Consensus still underwrites a high-growth, low-loss trajectory that the last two quarters no longer support.

**The other side, stated honestly — and it is strong:**
- Negative accruals, 1.22x cash conversion, DSRI of 0.97. No manipulation.
- **30%+ ROE** is genuinely elite (vs Itaú ~23%).
- **16.5x TTM P/E against ~30% earnings growth** is not an expensive stock — PEG below 0.6.
- The stock is already **-30% from its January 2026 high of $18.76**, with four separate 6–10% earnings-day drawdowns (26 Feb -9.4%, 15 May -5.7%, 2 Jun -8.2%, 28 Sep -10.0% on 2.5x volume). A meaningful part of the de-rating has occurred.
- Management is *disclosing* NPL deterioration transparently and quarterly — that is the behaviour of a bank working through a cycle, not hiding one.

---

## 7. Contrarian Rating: **NO EDGE**

**Not a forensic short. A tactical/cyclical short is defensible; a structural short is not.**

Rationale:
1. **The forensic case fails.** Every genuine manipulation detector (accruals, cash conversion, DSRI, TATA, goodwill intensity) reads clean. The two headline "red flags" the models threw — Beneish -1.62 and Altman 0.219 — are both artifacts of misapplying industrial models to a bank. I will not build a short on a false positive.
2. **The fundamental case is real but not yet mispriced.** Credit deterioration and deceleration are visible, disclosed quarterly, and already cost the stock 30%. Shorting a 16.5x P/E, 32%-ROE franchise after a 30% drawdown requires the deterioration to *accelerate* beyond what's now discounted.
3. **The asymmetry is wrong for a fresh short.** Upside surprise (NPLs stabilise, Selic cuts, Mexico inflects) is a 30–40% move; downside on a credit cycle is maybe 25–30% to the prior base. Poor risk/reward.

**What would turn this into a Short:** two consecutive quarters of 90+ NPL above 8.0%, provisions exceeding 32% of revenue, or any legislative proposal with real committee traction to cap revolving credit rates. Any of those converts a cyclical concern into a structural one, and I would short it hard at that point.

**What would make me Reject the short entirely:** 90+ NPL peaking below 7.5% in Q4'26, sequential revenue growth re-accelerating above 5%, and gross margin stabilising above 44%. On that path the current multiple is too low and this is a long.

**Monitoring priorities:** the cost-of-revenue breakdown in the next 6-K (to resolve the $1.8B reclassification), the 15–90 day NPL bucket as the leading indicator for Q4'26 provisions, and Brazilian legislative activity on card rates.

---

*Data gaps: I could not retrieve transaction-level direction for the Form 4 filings (the feed returned metadata only), nor peer multiples for Itaú/Mercado Pago to benchmark the 16.5x P/E and 4.5x P/B. The implied-provisions series is derived (cost of revenue less interest expense) and is noisy in Q1'26; it is directional, not exact.*
