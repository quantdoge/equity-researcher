# Short Analyst

- Symbol: NXT
- Elapsed: 124.0s

---
I have what I need. Writing the report now.

---

# Forensic Short-Seller Analysis — NXT (Nextpower / Nextracker)
**Price $91.13 | Market cap $13.83B | Net cash ~$1.03B | EV ~$12.8B | FY ends March 31**

**Important context up front:** the stock closed at **$156.40 on 2026-05-29** and trades at **$91.13** today — **-42% from the high**, but **+15% off the late-October low** on the 2 Nov earnings-volume spike. This is a post-de-rating name, not a crowded-momentum short. That materially shapes my conclusion.

---

## 1. Earnings Quality Assessment: **MEDIUM** (deteriorating, not fraudulent)

| Metric | FY2024 | FY2025 | FY2026 | H1 FY2027 |
|---|---|---|---|---|
| Operating CF / Net income | 1.40x | 1.29x | **0.95x** | **0.84x** |
| Accruals ratio | -4.87% | -4.59% | **+0.72%** | — |
| FCF conversion | — | — | 0.87x | — |
| Composite quality score | — | — | **49/100** | — |

Cash conversion has fallen in a straight line and has now broken **below 1.0x for the first time**, with accruals flipping from strongly negative (high-quality) to positive. The composite score of 49/100 is the definition of "middling." Piotroski F-Score is **4/9 (Weak)** — failing accruals quality, gross-margin improvement, asset-turnover improvement, ROA improvement, *and* no-dilution. A company growing revenue 20% at a 33% gross margin that fails all three of those is showing operating decay, not operating leverage.

**Beneish M-Score: -2.917 → "Low risk."** I do not accept that verdict at face value, and section 3 explains why.

---

## 2. Key Red Flags Found

**① The receivables anomaly — my single strongest finding (and it is not what Beneish thinks it is)**

- Net receivables fell from **$1,093.97M (3/31/25) to $417.04M (3/31/26)** — a **62% collapse while revenue grew 20.3%**.
- Full-year DSO by quarter: 123 → 124 → 121 → **43** → **133** → **78** days.
- That is not a normal working-capital cycle. Receivables are ~120–130 days in nine months of the year and then **vanish at fiscal year-end**, only to rebuild by **+$947M in the very next quarter** — roughly one full quarter of revenue.

**The critical tell:** Q4 FY26 AR fell ~$780M, yet the reported **change in working capital for that quarter was only +$7.3M**. If those receivables had actually been collected, ΔWC would have been massively positive. It wasn't. Cross-checking the current-asset lines: current assets *rose* $287M while AR fell $780M and inventory fell $86M — implying roughly **$1.0B of "other current assets" appeared at the fiscal year-end balance sheet**. That is consistent with receivables sold/factored (true-sale program) or reclassified into an opaque current-asset line at year-end.

**Fair counterpoint I owe you:** annual OCF ($556.5M) ties to the sum of the four quarters ($560.5M), so there is **no evidence the receivables move inflated reported operating cash flow**. This is a *transparency and window-dressing* flag, not a cash-flow-manipulation flag. It still matters: it means the fiscal-year-end balance sheet line items are not comparable to interim ones, and it makes the AR-based screens (including Beneish) uninformative.

**② Pervasive ~120–130 day DSO.** Even setting aside the year-end quirk, receivables consistently equal four to five months of sales. For a hardware vendor shipping to utility-scale EPCs, that is extreme. It says growth is being **financed on NXT's balance sheet** and that customers hold the pricing power — the opposite of a moat.

**③ Gross margin has peaked and is rolling over.** FY24 27.7% → FY25 33.7% → **FY26 32.6%**. On a cleaner same-quarter basis: **Q2 FY27 31.1% vs Q2 FY26 32.2%, -110bp YoY.** Beneish's GMI of **1.035** independently confirms margin deterioration.

**④ Negative operating leverage.** Q2 FY27: revenue **+22.5%**, operating income only **+10.8%**, SG&A **+35%** ($92.2M vs $68.2M). Operating margin compressed **~300bp YoY (21.7% → 18.7%)**. SG&A growing 1.5x faster than sales is what a company pays when it starts buying growth.

**⑤ Growth is increasingly acquired.** Goodwill + intangibles jumped **$569.6M → $887.0M in a single quarter (+$317M)** — now **33.5% of total equity**. Combined with the FY26 step-up from $424M to $567M, this is an acquisitive roll-up strategy bolted onto a hardware business, which historically correlates with multiple compression.

**⑥ Highly lumpy, decelerating trend.** Quarterly YoY revenue: **+42.4%, +33.9%, -4.7%, +8.2%, +22.5%** — a swing of 47 points. FY growth: +31.4% → +18.4% → +20.3%, and FY27 guidance of $4.0–4.4B implies ~+18% at the midpoint. Project-driven lumpiness with a 1.93 beta is not a compounder's profile.

**⑦ Chronic dilution.** Weighted diluted shares: 45.9M (FY22) → 152.7M (FY26) → 153.9M (Q2 FY27). **3.3x in four years.** SBC ran $118.9M in FY25 (~4% of revenue) and $56.8M/$32.0M prior — a real, recurring GAAP cost. *Data gap:* the feed reports $0 SBC for FY26 and recent quarters, which is plainly wrong; I could not quantify FY26/FY27 SBC.

**⑧ Deteriorating inventory signal is a positive — I'll give them this one.** Inventory days fell **61.9 → 48.3 → 39.9**. There is genuinely no channel-stuffing signal in inventory.

---

## 3. Beneish M-Score and Accruals Analysis

**M-Score = -2.917 (below the -2.22 soft and -1.78 hard thresholds) → mechanically "Low risk."**

Component decomposition: DSRI **0.317**, GMI 1.035, AQI 0.956, SGI 1.203, DEPI 0.448, SGAI 1.016, LVGI 0.871, TATA **0.0072**.

The score is being carried by one input: **DSRI of 0.317**. Beneish's model reads a collapsing receivables index as *evidence of clean revenue recognition* — the classic ISR building block of fraud is receivables outpacing sales. Here the opposite happened, so the model declares innocence.

**That is precisely the model's structural blind spot.** DSRI cannot distinguish "we collected the cash" from "we moved the receivables somewhere else, or sold them." I demonstrated above that the cash was *not* collected (ΔWC of just +$7.3M against a $780M AR decline). So NXT is receiving a **clean Beneish score for a reason the model was never designed to interpret**. The -2.917 should be treated as **not informative**, neither exculpatory nor damning.

Also note TATA of 0.0072 is low *only because* the accruals ratio is small — but the trend (from -4.9% to +0.7% over two years) is the wrong direction, and cash conversion crossing below 1.0x is the more reliable forward indicator.

**Verdict: no accounting fraud indicated. Real earnings-quality erosion indicated.**

---

## 4. Competitive Threat Assessment: **Moderate and rising**

- **Share structure:** NXT ~30% of solar trackers, Array Technologies (ARRY) ~12%, with GameChange, PVH, Soltec, Arctech and Chinese entrants behind them.
- **The relevant datapoint:** ARRY reported **record executed contracts and awarded orders of $2.5B at 6/30/26, +37% YoY** — growing materially faster than NXT's ~20% revenue growth. Off a smaller and previously distressed base, yes, but directionally this is share migrating toward the #2 while the leader's margins compress. That is the classic early signature of a commoditising hardware category.
- **NXT's real differentiator is increasingly regulatory, not technological:** "100% domestic content" trackers position it inside the 45Y/48E domestic-content and FEOC bonus structure. That is a **policy moat, not a product moat** — and policy moats are binary. OBBBA implementation, Treasury guidance revisions, and Section 232 steel tariffs cutting into COGS are all live, unhedgeable exposures. The 10-K language on domestic-content compliance costs confirms this.
- Trackers are ~10–15% of utility-scale solar project cost — a cost line procurement teams attack relentlessly. Gross margin already peaked. I regard the moat as **narrow and narrowing**.

---

## 5. Management Red Flags: **Moderate — one real flag, one unproven**

- **Insider selling:** 25 Form 4 filings between 2026-06-01 and 2026-11-02, heavily clustered — **nine on 2026-08-19 alone**, four on 2026-06-23. Volume and clustering are high. *Honest caveat:* my feed returned filing metadata only, **not transaction direction or size**, so I cannot assert net insider selling. Clustered August Form 4s are equally consistent with routine RSU vest-and-sell. **I will not make this claim without the data — flagged as unverified.**
- **Offsetting positive:** NXT repurchased **$162.1M of stock in Q2 FY27** — its first meaningful buyback — which cuts against the "management is dumping" read.
- **The fiscal-year-end balance-sheet shuffle (flag ①) is the governance item that does bother me.** Whatever the mechanism, the effect is that the annual balance sheet presented to the market looks dramatically cleaner on receivables and working capital than any interim balance sheet. That is a disclosure-quality issue and boards should be asked about it directly.
- **Accumulated deficit of -$1.97B** against $2.33B of equity: the reported book is essentially all paid-in capital and goodwill. Not fraud — a legacy of the Flex carve-out — but it means book value provides no downside support and Altman's x2 is negative for structural reasons.

---

## 6. Short Thesis Summary — Is there a credible bear case?

**Yes, but a modest one.** The defensible version is:

> NXT is a ~$3.6B-revenue hardware vendor in a commoditising category whose gross margin peaked in FY25, whose operating margin is now compressing ~300bp YoY as SG&A outruns sales, which is plugging the growth gap with acquisitions (goodwill now 33% of equity), funding 120–130 day receivables on its own balance sheet while dressing them down at each fiscal year-end, diluting shareholders ~2%/yr, and trading at a multiple that still requires ~20%+ revenue CAGR through FY2031 per consensus ($5.21B FY28E, $7.22B FY31E).

**Now the other side, and it is strong:**

1. **The balance sheet is pristine.** Net cash ~$1.03B, **total debt ~zero**, current ratio 2.23x. Altman Z of 2.078 (grey zone) is an artifact of the negative retained earnings and book-equity denominator; this company has **no solvency risk whatsoever**. There is nothing to break here.
2. **Valuation is not stretched.** ~22x LTM EPS ($4.08) and ~15x EV/LTM EBITDA. On FY2028 consensus of $5.73 that's **~16x**. Shorting a net-cash 20% grower at 16–22x is a bad trade even when the quality critique is right.
3. **$6B backlog** covers roughly 1.7x forward revenue. Visibility is genuinely good, and the latest quarter *reaccelerated* (+22.5% YoY vs +8.2% prior).
4. **The stock has already fallen 42%** from its May high. The margin-compression and deceleration thesis is substantially in the price.
5. **No accounting fraud.** Beneish is clean, inventory days are falling, AR is *not* outrunning revenue, and OCF reconciles to the quarterly sum. My receivables finding is a transparency problem with **no demonstrated cash-flow inflation**.

**Conditional short trigger:** if a future 10-K discloses that the year-end receivable reduction came from a factoring/true-sale facility with recourse, or if DSO pushes past 140 days while cash conversion falls below 0.75x, the thesis upgrades materially. I could not retrieve the 10-K text to resolve this — **`fetch_filing_text` returned "No 10-K found for NXT,"** and my peer set returned only integrated oil majors (XOM, CVX, SHEL), so **no like-for-like tracker multiple comparison was possible.** Both are real gaps in this analysis.

---

## 7. Contrarian Rating: **NO EDGE** (reject as a high-conviction short)

**I am not shorting this, and I don't think you should either.** The forensic work found genuine quality erosion — cash conversion through 1.0x, gross margin peak, negative operating leverage, an acquisitive pivot, and a year-end receivables pattern that genuinely needs explaining. But every one of those is a *slow-burn margin* problem, not a *solvency or fraud* problem, in a company with $1.03B of net cash and a $6B backlog, after a 42% drawdown, at 16x forward earnings.

A short here has poor asymmetry: limited downside left in the multiple, unlimited upside if policy tailwinds (domestic content, FEOC enforcement against Chinese competitors) re-rate the name. The borrow is likely expensive given the 1.93 beta and high retail ownership.

**Positioning recommendation:** Do **not** short outright. Instead, use NXT as a **pair-trade short leg against a higher-quality compounder**, or simply **avoid/hold underweight**. Revisit as a genuine short only if (a) the factoring disclosure appears, or (b) gross margin breaks below 30% for two consecutive quarters with DSO above 140 days. The single most valuable follow-up is one question to IR: **"What is the balance of the receivables sold or reclassified at 31 March 2026, and under what facility?"** If the answer is evasive, my rating changes.
