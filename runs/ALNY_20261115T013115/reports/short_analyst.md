# Short Analyst

- Symbol: ALNY
- Elapsed: 87.4s

---
I have what I need. Writing the report now.

---

# ALNY — Forensic Short-Seller Analysis
**Price: $165.04 (13-Nov-2026) | Mkt cap $22.1B | EV ≈ $19.8B | Down 66% from $491 peak (Oct-2025)**

---

## 1. Earnings Quality Assessment: **LOW** (not Fraudulent Risk)

The reported earnings are arithmetically clean but economically hollow. FY2025 GAAP net income of $313.7M was real enough, backed by $524.1M operating cash flow (cash conversion 167%) and negative accruals (−4.2%). **That is genuinely good quality.** The problem is FY2026, where the income statement detonates:

| Q3-2026 | $M |
|---|---|
| Revenue | 1,458.1 |
| Operating income | 345.8 |
| **Net income** | **2,167.3** |
| Operating cash flow | 341.0 |
| **Cash conversion** | **15.7%** |

Net income was **6.3x operating income**. Retained earnings jumped from −$6,332M (Jun-30) to −$4,165M (Sep-30) — precisely the $2,167M of net income — while total assets rose $2.44B and equity rose $2.25B with no matching cash. This is a **non-cash deferred-tax valuation-allowance release**: a one-time accounting event as cumulative profitability flipped the DTA onto the balance sheet.

**Trailing-twelve-month distortion:** TTM net income $2,724M, TTM OCF $650M → **cash conversion 23.9%**. Screeners will show ALNY at a **~8x P/E**, implying a deep-value biopharma. That is a phantom. Strip the $2.17B tax gain and core TTM net income is roughly **$750–800M**, implying **~28x**. The market is not wrong at $165; the P/E screen is.

## 2. Key Red Flags Found

1. **Gross margin collapse — the single most important finding.** FY2024 85.6% → FY2025 81.8% → **Q3-2026 75.2%** (vs 84.2% in Q3-2025). That is **~900bps of contraction YoY**, and TTM GM is 77.3%. For a company whose entire thesis is a differentiated, patent-protected RNAi platform, this is what **loss of pricing power** looks like. It is consistent with channel mix shifting to ATTR-CM (larger, more payer-scrutinised population), chargeback/rebate escalation and royalty step-ups — not a one-quarter blip (Q4-25 75.6%, Q2-26 76.9%).
2. **Revenue deceleration into a guidance cut.** YoY growth: Q2-26 **+66.9%** → Q3-26 **+16.7%**. The `detect_revenue_deceleration` tool returns "stable" — I disagree; that reading is corrupted by the +149% Q3-25 comp. Management cut 2026 TTR guidance to **$4.2–4.5B (~$200M trim)** on "slower Amvuttra patient starts," and had already cut at Q2 (Amvuttra $1.01B, ~4% miss — the "one-two punch" with Onpattro erosion).
3. **Receivables outrunning revenue.** AR grew **+91.9%** vs revenue **+65.2%** in FY2025 (flagged by the tool). At Q3-26, DSO has crept 65.8 → 76.4 → **79.0 days** over three years, and AR rose +18.9% sequentially in Q3-26 against +12.9% revenue growth. Not channel stuffing yet — but a persistent, one-directional drift that warrants monitoring.
4. **Persistent dilution.** SBC of $348M = **9.4% of FY2025 revenue** and 49% of operating cash flow. Diluted weighted shares 129.7M (Q1-25) → 138.0M (Q3-26) = **+6.4% in six quarters**. Piotroski scores F7 (no dilution) = **0**. SBC-adjusted TTM FCF is ~$194M, not $501M.
5. **Interest expense rising with flat debt.** FY2025 interest expense $252.6M vs $141.9M in FY2024 on *essentially unchanged* gross debt (~$1.28B). A ~19.8% effective rate on reported debt signals large imputed/non-cash financing costs (royalty monetisation) that flatter "operating income" while burdening the true economics.
6. **Class-level mechanistic doubt.** CARDIO-TTRansform (eplontersen/Wainua) **missed its primary endpoint in ATTR-CM despite achieving the expected TTR suppression** — a read-across that "muddies the water for TTR silencers" generally, and the proximate cause of the 9-Jul-2026 intraday −17% reversal from $380 to $311 on 5.9M shares.

**Where the fraud tools come out benign — said plainly:** Beneish M-Score **−1.947** sits in the "moderate" band, but it is driven almost entirely by SGI 1.652 (high sales growth mechanically inflates the score) and DSRI 1.161. TATA is **−0.0424**, i.e. *negative* accruals. I see **no evidence of manipulation or fraud.** This is a narrative-and-execution story, not an accounting fraud.

## 3. Beneish M-Score & Accruals Analysis

| Metric | Value | Read |
|---|---|---|
| M-Score (FY2025) | **−1.947** | Moderate band (−2.22 to −1.78); growth-driven, not fraud |
| DSRI | 1.161 | Receivables index +16% — mild flag |
| SGI | 1.652 | Mechanically inflates M; growth artefact |
| TATA | −0.0424 | Negative total accruals — **high quality** |
| Accruals ratio (BS) | **−0.0424** | Negative = conservative (FY24 −0.064, FY23 −0.142) |
| Cash conversion FY2025 | 1.67x | High quality |
| Composite EQ score | **43/100** | Hurt by FCF/NI of 1.48x being non-recurring |

**Verdict on accruals: clean in FY2025, and I will not manufacture a fraud case where the cash backs the earnings.** The forensic problem is entirely in FY2026, where a $2.17B non-cash tax item makes GAAP earnings meaningless and every trailing metric (P/E, ROE, EPS growth) uninterpretable. **Altman Z of −0.02 "Distress" is an artefact**, not a signal — it uses book equity of $3.6B against a $22.1B market cap; x4 is understated ~6x, and the retained-earnings deficit is a legacy of 20 years of R&D expensing. Presenting that Z-score as a distress flag would be dishonest.

## 4. Competitive Threat Assessment — **materially eroding**

- **Acoramidis (BridgeBio)** approved in ATTR-CM; physician surveys show 50% see it as "similar" to tafamidis, 40% "incrementally better." Share is being contested by stabilisers, not just silencers.
- **Tafamidis (Pfizer)** remains entrenched first-line; the tafamidis market alone is ~$5.1B in 2026 growing ~8.7% CAGR — Alnylam is fighting for share in a market where the incumbent has a decade of outcomes data.
- **Nex-z (Intellia)** — in-vivo CRISPR, a **one-time** therapy. Clinical holds have been lifted and Phase 3 MAGNITUDE/HAELO are resuming. A functional cure is structurally superior to a quarterly-injection annuity. This is an **existential, not incremental**, threat to Amvuttra's terminal value and is not in anyone's DCF.
- **The eplontersen failure cuts both ways.** It hurts class credibility — but Amvuttra has its *own* positive HELIOS-B cardiovascular outcomes data that eplontersen never generated. The bull can legitimately argue no read-across. I weight this against the bear case.
- Offsetting strength: the TAM is genuinely large (company targets 75,000+ US-treated ATTR-CM patients by 2030), and the pipeline (zilebesiran in hypertension, cemdisiran, Regeneron CNS/ocular) is real optionality.

## 5. Management & Governance Red Flags

- **Sell-side/investor communication gap:** "We knew expectations for 2026 were ambitious, but we weren't expecting a guidance cut" (analyst, post-Q2). Two consecutive guidance cuts within one quarter of each other is the classic pattern of management anchoring expectations too high and then walking them down — not fraud, but poor credibility.
- **Insider activity:** 30 Form 4 filings in 2026, including **three on 12-Nov-2026** (the day before this $165 print) and a **15-filing cluster on 22-May-2026**. ⚠️ **Data limitation: I retrieved filing metadata only, not transaction direction or size.** These clusters are consistent with both 10b5-1 scheduled sales and RSU vesting. I will not assert net insider selling without the underlying Forms 4.
- No related-party, auditor-change or restatement flags surfaced.
- **Gaps I could not close:** no 10-K text available via the tool ("No 10-K found"), no short-interest/borrow data, and the sector peer set returned only mega-cap pharma (LLY, JNJ, ABBV) — no valid RNAi/ATTR comps. Peer multiples unavailable.

## 6. Short Thesis Summary — is there a credible bear case?

**Yes, a credible one — and the market has already found it.** The bear case is: *a single-molecule franchise (Amvuttra) facing a 900bp gross-margin slide, decelerating growth (66.9% → 16.7%), two guidance cuts, a class-level mechanistic challenge, a one-time CRISPR cure on the horizon, and GAAP earnings that are 6x inflated by a non-recurring tax benefit — with estimates dispersing to a 5x spread (2028 EPS $5.24 to $27.46).*

**But the contrarian's discipline applies to shorts too.** At $165:
- **The easy 66% is gone.** $491 → $165. The thesis is now consensus; shorting here is crowded and late.
- **Balance sheet is fortress-like:** $3.59B cash vs $1.26B debt = **$2.3B net cash**, no refinancing cliff.
- **Cash generation is real and improving:** TTM FCF **+$501M**, four consecutive positive quarters.
- **Valuation has de-rated hard:** EV/TTM sales **3.9x**, EV/FCF 39.5x, and 18.4x on 2027 consensus EPS of $8.96. For a 78%-gross-margin franchise with a large TAM, that is no longer expensive.
- Amvuttra holds outcomes data eplontersen lacks.

## 7. Contrarian Rating: **NO EDGE — short thesis has largely played out**

This was a **Short at $400–490**. It is **no edge at $165**. The forensic red flags are genuine — Low earnings quality, real gross-margin erosion, DSO creep, chronic dilution — and the stock deserves to trade well below its 2025 peak. But the residual bear case now requires a *third* guidance cut or an Intellia/bridge-bio clinical catalyst, and you are being paid nothing to wait against $2.3B of net cash and $500M of FCF.

**Actionable framing:**
- **Do not initiate a short here.** Asymmetric squeeze risk into any stabilisation of Amvuttra patient starts.
- **Re-short on strength above ~$250–270** (a ~1.6x bounce), where EV/sales returns above 5.5x and the phantom 8x P/E is being quoted again.
- **Watch, in order:** (1) Q4-26 Amvuttra net patient adds and any further TTR guidance reset; (2) gross margin — a print below 74% confirms structural pricing-power loss; (3) DSO above 85 days or AR growth >1.5x revenue growth; (4) Intellia nex-z Phase 3 readouts; (5) a fresh Form 4 analysis on true net insider direction, which I could not verify.

**The honest other side:** if management stabilises Amvuttra and 2027 EPS of ~$9 is delivered, $165 is a **contrarian long** at 18x with $2.3B net cash — and the "value trap" P/E screeners are flagging would, in that scenario, be roughly right. My bearishness is on *earnings quality and moat durability*, not on the current price.
