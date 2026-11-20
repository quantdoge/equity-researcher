# Fin Risk Analyst

- Symbol: TEVA
- Elapsed: 109.5s

---
I have sufficient data, including the FY2025 annuals, nine months of FY2026 actuals, the 2026 rating actions, and the rate environment. Writing the assessment now.

---

# TEVA Pharmaceutical Industries — Financial Risk Assessment
**As of:** Q3 FY2026 (period ended 30-Sep-2026) | Price $39.34 | Market cap $45.9B | Sector: Healthcare / Specialty & Generic Drugs

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE** (recently crossed over)

Teva completed a full rehabilitation to investment grade during 2026, after a decade in high yield:

| Agency | Rating | Prior | Date |
|---|---|---|---|
| Fitch | **BBB-** (Stable) | BB- | May 2026 |
| Moody's | **Baa3** (Stable) | Ba1 | Aug 2026 |
| S&P | **BBB-** | BB+ | Sep 2026 |

This is the single most important fact in the file, and it creates a **genuine tension with the reported financials**: the GAAP-based metrics below look sub-investment-grade. The reconciliation is that agency metrics use *adjusted* EBITDA and strip out non-cash impairments. That reconciliation is the central analytical risk — it depends entirely on how much credit you give management's adjusted figures.

**Governing constraint:** Moody's stated upgrade criterion is **gross debt/EBITDA below 3.75x** on their basis. This is the de facto covenant. Teva has limited headroom above it.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (audited) | Q3'26 TTM | Assessment |
|---|---|---|---|
| Revenue | $17,258M | $17,229M | Flat; growth stalled |
| Reported EBITDA | $3,141M | $2,040M | **−35%** |
| Adjusted EBITDA (est.) | — | ~$3,414M | Excl. Q2'26 charge |
| Debt / Equity | 2.20x | 2.13x | High |
| Debt / Assets | 0.43 | 0.42 | High |
| **Net Debt / EBITDA (reported)** | **4.40x** | **6.32x** | Deteriorating |
| **Net Debt / EBITDA (adjusted)** | — | **~3.78x** | Just inside 3.75x target |
| Interest coverage (EBIT/Int) | 2.35x | 1.18x reported / ~2.7x adj. | **Thin** |
| Current ratio | 1.04 | **0.95** | Below 1.0 — weakened |
| Quick ratio | 0.80 | ~0.62 | Weak |
| Working capital | +$490M | **−$823M** | **Turned negative** |
| Altman Z-Score | 0.28 (Distress) | ~0.16 | Distress zone |
| Altman Z (mkt-cap x4) | — | ~0.87 | Still distress |
| Piotroski F-Score | **8 / 9** | — | **Strong** |
| Cash | $3,556M | $4,085M | Adequate |
| Total debt | $17,382M | $16,984M | Deleveraging |

**The Z-score/F-score divergence is the headline of this report.** These two models disagree violently — Z says "distress," F says "strong." Both are telling the truth about different things:

- **Z-score is structurally broken for TEVA.** X2 (retained earnings / assets) is **−0.337**, i.e. a **−$13.7B accumulated deficit** from the 2017 Actavis acquisition writedowns. Altman was never designed to handle a company whose book equity was destroyed by a past M&A mistake. Even substituting market cap for book equity only lifts Z to ~0.87 — still distress, but the *distance* between 0.16 and 0.87 tells you the metric is being driven by book-value artifacts, not default probability.
- **F-Score of 8/9 is more forward-looking and confirms genuine improvement:** positive ROA, positive operating cash flow, ROA improvement, accrual quality, lower leverage, positive equity change, gross-margin improvement (51.8% vs 48.7%), asset-turnover improvement. Only F7 (no dilution) fails — modest ~1.2% annual share creep from stock comp.

**Caveat I must flag honestly:** book equity of **$7,984M** sits against **$19,045M of goodwill and intangibles**. Write off goodwill entirely and equity is deeply negative. Another large impairment *can* crush book equity — though credit metrics here are EBITDA-based, not equity-based, so this is a book-value/optics risk, not a default trigger.

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (3Y) | **43.84%** |
| Beta vs SPY | **0.758** (profile: 0.842) |
| Max drawdown (3Y) | **−43.7%** |
| Sharpe (0% RF) | 1.072 |
| Sharpe (vs ~4.9% RF) | ~0.96 |
| Sortino | *not available* |

**Interpretation:** Beta of 0.76–0.84 says the *business* is defensive — generic drugs and CNS therapies are non-discretionary, and revenue held up through every stress period (revenue rose every year 2022→2026). But **43.8% realised volatility is wildly out of line with that low beta**. That gap is pure idiosyncratic risk: litigation, generic price erosion, and serial impairment charges. This is a low-beta stock with high-beta volatility — the worst combination for a portfolio, because beta-based risk models will systematically understate its drawdown potential.

Max drawdown of −43.7% over three years, against a 0.76 beta, confirms the tail risk is company-specific and not diversifiable via market-hedged positioning.

---

## 4. Downside Scenario Analysis — Revenue −20%

**Base case (TTM Q3'26, adjusted):** Revenue $17,229M; EBITDA $3,414M (19.8%); interest $893M; capex ~$505M; net debt $12,899M.

I model two flow-through assumptions, because generic-drug economics have high fixed-cost absorption — a revenue loss carries an outsized EBITDA hit:

| | **Mild** (45% flow-through) | **Severe** (60% flow-through) |
|---|---|---|
| Revenue | $13,783M | $13,783M |
| Adjusted EBITDA | $1,863M | $1,346M |
| **Net Debt / EBITDA** | **6.9x** | **9.6x** |
| **EBITDA / Interest** | **2.09x** | **1.51x** |
| FCF (after interest & capex) | **+$365M** | **−$52M** |
| Rating implication | Downgrade to BB | Deep high-yield / BB− |

**Verdict: a 20% revenue decline breaks the capital structure.** Leverage roughly doubles to 7–10x, and in the severe case free cash flow turns negative *before* any debt amortisation. The company would be forced to: suspend all discretionary spend (already no dividend, no buyback), cut R&D, draw revolver, and likely raise equity — dilutive at a depressed price.

**Mitigants that materially soften this:**
1. **$4,085M cash** now exceeds short-term debt of $4,038M (1.01x cover).
2. **The refinancing wall is largely solved.** Teva priced **$4.9B of senior notes in September 2026** and ran $2.0B of tender offers for 2026–2031 maturities. The near-term cliff has been termed out.
3. **Zero capital returns.** No dividend, no buyback — the entire FCF stream is discretionary and can be redirected to debt service. This is a genuine, rare source of resilience.
4. **Deleveraging trend intact:** total debt $20,153M (2023) → $18,079M (2024) → $17,382M (2025) → $16,984M (Q3'26). Net debt down $927M in nine months.
5. Post-2023 opioid settlement, the largest contingent liability is largely quantified and reserved.

**A 20% revenue decline is a genuine tail, not a base case** — revenue has risen four consecutive years. But the test's purpose is to show the cushion, and the cushion is roughly **zero**.

**Refinancing cost headwind:** with the 10Y UST at **5.13%** and 30Y at **5.47%**, Teva's ~$900M annual interest bill on $17.0B (5.3% average) will not fall much as it refinances — even at IG, new issuance prices near 5.5–6.0%. All notes are fixed-rate (per Q1'26 10-Q), which protects against rate spikes but locks in the current high cost. **Interest expense may stay flat-to-up even as debt falls**, which caps the pace of coverage improvement.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Upgraded from High. The trajectory — three IG upgrades, $3.2B of net debt reduction since 2023, refi wall cleared, F-Score 8, defensive revenue — is genuinely strong and deserves credit. But this is a **lower-quality investment grade**: coverage at 2.35x FY2025, FCF/interest of roughly 1.25x, a current ratio that just fell below 1.0, and adjusted leverage sitting right at the 3.75x rating threshold. There is very little room for error.

**The rating hinges on one assumption:** that the Q2'26 impairment is genuinely non-recurring. If adjusted EBITDA is being flattered and charges recur, this flips to **High** and the IG ratings are at risk.

---

## 6. Key Red Flags

1. **Current ratio fell below 1.0** — 0.95 at Q3'26 (from 1.04 at FY25). Working capital swung from **+$490M to −$823M** in nine months. Short-term debt jumped to $4,038M when 2027 maturities became current. Liquidity buffer is now issued-note-dependent, not organic.

2. **Serial impairments undermine "adjusted" EBITDA.** Q2'26 carried ~$1.35B of charges (operating income −$231M vs. ~$1,119M underlying). FY2024 showed the same pattern (operating income −$303M vs. EBIT $3,372M); FY2022 had a −$2.2B operating loss. **This is a recurring pattern, not an isolated event** — which is precisely why reported net leverage is 6.3x while adjusted is 3.8x. A 2.5-turn gap between GAAP and adjusted is a large amount of faith to place in management's numbers.

3. **FCF deterioration is the most under-appreciated risk.** Nine-month FY2026 FCF was just **$220M** versus $1,148M for all of FY2025. Q3'26 alone generated only $121M. Against ~$900M annual interest, FCF coverage of interest is roughly **1.2–1.4x**. Cash generation — not leverage — is the binding constraint.

4. **Thin book equity vs. intangible-heavy assets.** $7,984M equity supporting $19,045M goodwill/intangibles and a −$13,736M retained-earnings deficit. Negative equity on a full write-down.

5. **High idiosyncratic volatility with low beta.** 43.8% vol and a −43.7% three-year max drawdown on a 0.76-beta stock means risk models will understate tail exposure.

6. **Growth concentration.** Austedo and Ajovy are carrying the growth story against Copaxone/generic erosion. Revenue was flat TTM ($17,229M vs $17,258M) — the pivot-to-growth narrative is not yet visible in the top line.

---

## Data Gaps (explicitly flagged)

- **Debt maturity schedule by year** is not available from the financial data tools; the refinancing picture above is reconstructed from press releases ($4.9B Sept-2026 notes, $2.0B tender offers) and is directionally, not precisely, reliable.
- **CDS spreads unavailable** — I could not independently verify market-implied default probability to cross-check the IG ratings.
- **Q3'26 interest expense reported as $0** (data error); ~$200M/qtr inferred from Q1–Q2'26. TTM interest of ~$893M is therefore an estimate.
- **TTM free cash flow is approximate** — Q4'25 quarterly cash flow was not retrievable, so TTM FCF (~$0.7–1.0B, implying 1.5–2.2% yield versus the 2.52% tool reading on FY2025) is estimated.
- **Sortino ratio and peer leverage comparables unavailable** — no relative credit positioning versus generic-pharma peers.
- **S&P outlook ambiguity:** one source references a "Negative" outlook dated Sep-2026 while Teva's own release describes a Stable outlook at BBB−. I have used Stable but cannot fully reconcile the discrepancy.

---

**Bottom line:** TEVA has executed a real balance-sheet turnaround and now sits at the bottom rung of investment grade. It can service its debt
