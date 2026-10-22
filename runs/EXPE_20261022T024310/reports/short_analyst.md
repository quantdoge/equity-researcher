# Short Analyst

- Symbol: EXPE
- Elapsed: 678.5s

---
## FORENSIC SHORT-SELLER ANALYSIS — EXPEDIA GROUP, INC. (NASDAQ: EXPE)

**Price at analysis: $285.64 | Market cap $32.7B | Sector: Consumer Cyclical / Travel Services | Beta 1.36**

---

### 1. Earnings Quality Assessment: **MEDIUM-HIGH** (not a manipulation short)

The accounting forensics come back clean on the dimensions that typically precede fraud. Accruals are *negative* in all four years, cash conversion runs at 250–300%, and the Beneish model sits comfortably below the manipulation threshold. This is not a company manufacturing earnings — it is a company whose *reported cash flow* is flattered by structural float. That distinction matters: the risk here is **quality of cash, not integrity of earnings**.

| Metric | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Net income ($M) | 352 | 797 | 1,234 | 1,294 |
| Operating cash flow ($M) | 3,440 | 2,690 | 3,085 | 3,880 |
| Accruals ratio | −0.143 | −0.088 | −0.083 | −0.106 |
| Cash conversion | 977% | 338% | 250% | 300% |
| Working-capital inflow ($M) | 1,261 | 271 | 419 | 1,173 |
| WC as % of OCF | 37% | 10% | 14% | **30%** |

Cumulative 2022–2025 OCF was $12.10B against $3.67B of net income (330% conversion), but **$3.12B — 26% — came from working-capital float rather than earnings.** In 2025 the figure jumped to 30% of OCF. Strip out float and stock comp ($398M) and underlying free cash flow is ~**$1.54B**, a 4.7% yield on the $32.7B cap — not the 9.5% headline FCF yield the sell-side quotes. Float-funded FCF is real only while bookings grow; it reverses violently when they don't. That is the single most important number in this file.

**Data caveat worth flagging:** the reported FY25 EBITDA ($2,301M) does not tie to EBIT + D&A ($2,163M + $138M = $2,301M ✓ against an *income-statement* D&A of only $138M, versus $887M in the cash-flow statement and $838M the prior year). Using cash-flow D&A, EBITDA is ~**$3.05B** — i.e. margin *expanded* to 20.7% from 19.2%, not contracted. The "EBITDA fell while revenue rose" read is an artifact. I use the $3.05B figure below.

---

### 2. Key Red Flags Found

**Red Flag #1 — Receivables are outrunning revenue by a factor of four. This is the file's centrepiece.**
- Revenue growth 2025: **+7.6%**; accounts receivable growth: **+29.3%**
- 2024: revenue +6.6%, AR +14.8%. 2023: revenue +10.1%, AR +33.8%. Three consecutive years.
- Days sales outstanding: **66 days (2022) → 81 → 87 → 104 days (2025)** — a 38-day deterioration.
- AR is now **$4.20B, or 28.5% of revenue and 325% of net income.**

This is consistent with the deliberate mix shift toward B2B (Expedia Partner Solutions) and merchant-model bookings, where Expedia extends settlement credit to partners and travel resellers. That explanation is legitimate — but it converts a capital-light marketplace into a **working-capital lender to the travel trade**, a sector with high failure rates in downturns. It also means incremental revenue is being bought with balance-sheet credit rather than collected in cash. The DSRI of 1.201 in the Beneish model is the only component signalling concern, and it is pointing at exactly this.

**Red Flag #2 — "Adjusted EBITDA" and FCF narratives mask a structurally sub-scale margin.** FY25 GAAP operating margin 12.7% against Booking Holdings at roughly 30%. SG&A is **60.8% of revenue ($8.95B)** — overwhelmingly performance marketing. Expedia is a $14.7B-revenue business earning $1.29B of net income; Booking earns more than four times that on less than double the revenue. The margin gap is the moat gap.

**Red Flag #3 — Goodwill of $7.69B sits on $2.55B of book equity; tangible book value is approximately −$5.1B.** Goodwill and intangibles are 31.5% of total assets and 302% of equity. Goodwill has been written down incrementally every year since 2022 ($8.35B → $7.69B), implying recurring underperformance in acquired units. Trivago in particular is structurally exposed to Google Hotel Ads. A single large impairment wipes out book equity entirely — and with $1.93B of buybacks having already shrunk the equity base, there is no cushion.

**Red Flag #4 — Thin equity and negative working capital create acute cyclical fragility.** Current ratio **0.73** ($12.20B current assets vs $16.66B current liabilities); equity/assets just **10.4%**. The liability side is dominated by deferred merchant bookings — customer prepayments. This is an interest-free funding source in normal times and a liquidity call in a shock. With a 1.36 beta and a 2025 price range of $128–$341 (a 166% spread), the market has already demonstrated how fast this de-rates.

**Red Flag #5 — Unexplained cash build.** Cash and short-term investments rose $2,813M in 2025 while FCF was $3,110M against $2,130M of buybacks and dividends — leaving ~$980M of expected build. Roughly **$1.8B of the increase is not explained by the reported cash-flow statement.** The benign explanation is reclassification of short-term investments or investment maturities; the uncharitable one is asset sales flattering the "net cash" headline. This needs verification against the 10-K and I could not retrieve the filing text (tool returned no 10-K). *Flagged as unverified, not asserted as a finding.*

**Red Flag #6 — Altman Z-Score of 0.843 puts EXPE in the "distress" zone.** I regard this as largely a false positive: the score uses *book* equity ($2.55B) against $21.9B of liabilities. Substituting the $32.7B market cap gives x4 = 1.49 and a Z of **~1.67 — grey zone, not distress**, and the company holds $7.30B cash against $6.67B debt (net cash $307M). But the underlying structural point stands: this is a levered, thin-equity, negative-working-capital business wearing an asset-light costume.

---

### 3. Beneish M-Score and Accruals Analysis

**M-Score: −2.327 → "Low risk"** (below both the −1.78 and −2.22 thresholds).

Component read:
| Index | Value | Interpretation |
|---|---|---|
| DSRI | **1.201** | ⚠ Receivables days rising sharply — the one real flag |
| GMI | 0.993 | Gross margin improving |
| AQI | 0.884 | Asset quality improving |
| SGI | 1.076 | Modest sales growth |
| DEPI | 4.92 | Depreciation-rate artifact from the D&A inconsistency noted above — not economically meaningful |
| SGAI | 0.986 | SG&A efficiency marginally better |
| LVGI | 1.024 | Slight leverage increase |
| TATA | **−0.106** | Negative total accruals — high-quality earnings |

**Conclusion: no evidence of earnings manipulation.** The M-Score's only substantive warning is DSRI, and that warning is about *receivables credit quality*, not revenue fabrication. Accruals-to-revenue is −17.6%, deeply negative. If I were building a fraud short, this would fail the first screen — and I'd say so plainly rather than manufacture a thesis.

---

### 4. Competitive Threat Assessment: **ELEVATED AND RISING**

1. **AI-driven search disintermediation.** The structural bear case is that Google AI Overviews and LLM travel agents compress the paid-click funnel Expedia depends on. Expedia spends ~$9B annually on sales and marketing, largely performance-based, and is therefore a price-taker on customer acquisition cost. Any shift in referral economics hits operating margin directly. This is the thesis with genuine long-tail risk — and the market has already gapped the stock twice on AI-related news (Feb 3, 2026: $275 → $233 on 6.8M shares; Sep 22–23, 2026: $281 → $259 on 5–6M shares).
2. **Booking Holdings ($119B cap, ~3.6x EXPE) with structurally superior margins and a larger alternative-accommodation footprint.** Booking has out-earned Expedia for a decade; the scale gap funds superior marketing efficiency.
3. **Airbnb pressuring Vrbo** in alternative accommodations — a segment Expedia paid up for and where it holds the weaker brand.
4. **Supplier direct-booking and loyalty disintermediation.** Marriott and Hilton have pushed direct channels and co-branded loyalty hard; every point of share taken direct is a point of OTA take-rate lost.
5. **Partially offsetting:** B2B/Partner Solutions is genuinely counter-cyclical to consumer search costs — it buys distribution through partners rather than paying Google. That is precisely why B2B is growing and why receivables are ballooning. The two facts are the same fact.

---

### 5. Management Red Flags: **MODERATE, NOT DISQUALIFYING**

- **Leadership churn.** CEO transition from Peter Kern to Ariane Gorin (2024), alongside CFO turnover. Two senior finance/leadership changes within a short window in a business undergoing a technology re-platform is a governance item to monitor.
- **Insider activity is one-directional — selling.** Form 4 filings cluster heavily: seven filings on 2026-08-18, five on 2026-10-05, plus 2026-08-13/17 and 2026-10-16. Confirmed sales near the highs include Director Craig Jacobson (~3,133 shares at $328.52, ~$1.0M) and Chief Legal Officer Robert Dzielak (1,004 shares at $335.00). Third-party tracking indicates the most recent open-market insider *purchase* dates to May 2022 — meaning insiders have not bought a single share in over four years while the stock roughly doubled from ~$144 to $286. The clustering pattern is consistent with scheduled vest-and-sell rather than conviction, but the absence of any offsetting buying at a 2x is a real signal.
- **Headcount runway is largely spent.** 16,000 full-time employees versus ~24,000 pre-2020. A meaningful share of the margin expansion to date came from cost extraction that is finite and largely complete. The next leg of margin must come from mix and marketing efficiency — harder and less certain.
- **No evidence of related-party self-dealing, auditor changes, or aggressive capitalisation.** Capex/revenue is actually *falling* (6.6% in 2023 → 5.2% in 2025), so expense capitalisation is not an escalating lever. Credit where due.

---

### 6. Short Thesis Summary: Is there a credible bear case?

**Yes — but it is a quality/cyclicality/valuation bear case, not a fraud bear case.**

The coherent short argument: *Expedia is a mid-single-digit revenue grower trading at ~29x trailing earnings ($285.64 vs. $9.81 diluted EPS) after a 2x run, whose free cash flow is 26–30% manufactured by working-capital float that only exists while bookings grow; whose receivables have grown four times faster than revenue for three straight years, converting an asset-light marketplace into a credit underwriter of the travel trade; whose $7.69B of goodwill rests on $2.55B of equity; whose margins remain roughly half of Booking's; and whose insiders have sold into strength without buying a share since 2022.*

**The other side — and it is stronger than I expected going in:**

- **The deceleration thesis is factually wrong right now.** Quarterly YoY revenue growth: 3.4% (Q1'25) → 6.4% → 8.7% → 11.4% → **14.7% (Q1'26)** → 14.0% (Q2'26). Revenue is *accelerating*, not decelerating. The B2B and advertising engines are working. Any short positioned for a growth stall is fighting the tape.
- **Manipulation risk is genuinely low** (M-Score −2.33, TATA −0.106). I looked hard and found no fraud.
- **Margins are expanding, not eroding:** gross margin 85.8% → 90.1% and operating margin 9.3% → 12.7% over 2022–25. Moat-erosion is a forecast, not an observation.
- **Balance sheet materially improved:** net debt swung from +$2.35B to a **net cash position of −$307M**, with $7.30B cash. Share count fell 4.6% in 2025 alone (131.4M → 125.4M). Buybacks plus mid-teens revenue growth is a powerful EPS compounding machine — which is exactly why consensus sees EPS going from $9.81 to $28.49 by 2028.
- **Piotroski F-Score 5** — moderate, with accruals quality and gross-margin improvement both scoring positively.
- The stock has already de-rated ~16% from its $341 August high. Two-thirds of the "bad news" may already be in the price.

The bear case's weakest link is timing and valuation: a 5.9% FCF yield ex-float plus a 4.6% annual buyback shrink plus 14% revenue growth is not an obviously overvalued package. The consensus 2028 EPS of $28.49 is aggressive and vulnerable to disappointment — that is a genuine bear vector — but "consensus is too optimistic" is a much weaker short than "the numbers are fake."

---

### 7. Contrarian Rating: **NO EDGE — Reject Short Thesis**

I went looking for a fraud and did not find one. The Beneish model, the accruals ratio, and cash conversion all say the earnings are real; the only elevated index (DSRI 1.201) points at receivables credit quality, which is a *quality* concern the market can see and has partly priced. Altman's "distress" reading is a book-equity artifact — on market cap the Z is ~1.67 and the company is net cash.

What I would *not* do is short EXPE here on the forensic file. The receivables trend is the item that belongs on a watch list — if DSO breaks past ~120 days or a large B2B partner fails, the write-down and the float reversal arrive together, and that is when the short becomes interesting. The condition that would convert "no edge" into a genuine short is **bookings growth stalling while receivables keep growing** — the classic channel-stuffing signature. That is not happening today; revenue is accelerating to 14%.

The honest verdict: **this is a MEDIUM-HIGH quality earnings profile with one real balance-sheet red flag, a structural margin gap versus Booking, and a valuation that has already run hard.** A tactical short on a growth-to-mid-single-digit deceleration in 2027 and a goodwill write-down is defensible. A short on accounting manipulation is not. Rating: **No Edge.**

*Data caveats: the 10-K text could not be retrieved (tool returned no filing); the ~$1.8B unexplained cash build and the FY25 EBITDA/D&A inconsistency require verification against the filed statements before either is relied upon. Peer multiple comparisons are unavailable in this dataset — the Booking comparison above is directional, based on relative market cap and margin structure, not computed from a peer multiple set.*
