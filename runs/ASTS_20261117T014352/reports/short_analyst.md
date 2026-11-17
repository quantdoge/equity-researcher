# Short Analyst

- Symbol: ASTS
- Elapsed: 94.8s

---
# ASTS — Forensic Short-Seller Analysis
**AST SpaceMobile, Inc.** | Price $28.58 (16-Nov-2026) | Mkt cap ~$11.7B | Beta 2.85
*Peak $133.09 (28-May-2026) → −78.5%. Prior peak $122.09 (29-Jan-2026).*

---

## 1. Earnings Quality Assessment: **LOW** (but *not* Fraudulent Risk)

I want to be precise here, because the headline scores are misleading and a lazy short would misread them.

| Metric | Value | My read |
|---|---|---|
| Composite quality score | **14 / 100** | Genuine, but driven by capex intensity, not accounting |
| Accruals ratio (2025) | **−0.054** | *Conservative* — negative accruals, "ok" |
| Cash conversion (OCF/NI) | 0.209 | **Inverted signal** — see below |
| FCF conversion (FCF/NI) | 3.32 | The real problem: capex 3x the loss |
| Piotroski F-Score | 5 / 9 | Moderate; fails on ROA, OCF, leverage, dilution |

**The critical nuance:** for a company with a *negative* numerator and denominator, cash conversion ratios invert their meaning. Net loss of −$341.9M against operating cash burn of only −$71.5M means the P&L loss *overstates* cash burn — the opposite of an earnings-quality red flag. The 14/100 score is really a **capital-intensity** score (FCF −$1,136M vs net loss −$342M), not a manipulation score. I will not dress it up as fraud.

**Where quality genuinely is poor:** revenue is lumpy, contract-based, and low-margin. Q4-2025 alone booked $54.3M of the year's $70.9M — with COGS of $91.3M, producing a **−$37.0M gross profit quarter**. That is not a commercial service ramp; that is a small number of large, loss-making contracts landing at year-end.

⚠️ **Data integrity flag:** FY2025 COGS is reported as $33.0M, but the sum of the four reported quarters is $124.0M. Annual and quarterly gross profit do not reconcile (−$53.1M vs +$37.9M). This must be verified against the 10-K before any position is sized. I could not retrieve the 10-K (SEC returned 403; the tool reported no 10-K on file).

---

## 2. Key Red Flags Found

**a) Receivables ballooning — the one classic accruals flag that IS present.**
Net receivables went from **$0 (2024) → $37.7M (2025)** against revenue of $70.9M. That is **DSO ≈ 194 days**, and receivables equal **53% of annual revenue**. Revenue is being recognised far faster than it is being collected. This is the single most legitimate accounting concern in the file.

**b) Revenue per share has gone nowhere despite 7.5x dilution.**
- 2022: $13.8M rev / 54.4M shares = **$0.254**
- 2025: $70.9M rev / 256.0M shares = **$0.277**

Four years, ~$4B+ of capital raised, and revenue per share is up **9%**. Every dollar of "growth" has been purchased with shareholder equity. This is the cleanest statement of the bear case.

**c) Interest expense is consuming the business.**
$0.2M (2022) → $4.5M (2023) → $18.7M (2024) → $36.1M (2025) → **$30.3M in Q3-2026 alone (~$121M annualised)**. Interest is now ~**73% of consensus 2026 revenue**. This is cash interest on ~$4B+ of converts, not a non-cash mark.

**d) Serial convertible issuance — four raises in ~18 months, each a double-digit drawdown.**
| Date | Event | 1-day move |
|---|---|---|
| Sep-2025 | UBS downgrade (EchoStar/SpaceX competition) | −9.5% |
| Oct-2025 | Prices $1.0B converts | −9.2% |
| Jan-2026 | Scotiabank downgrade (competition, slow adoption) | −12.1% |
| Feb-2026 | Prices $1.0B converts (1.625%, conv. ~$116.30) | −15.2% |
| Jul-2026 | Announces $1.0B converts (2.25%, conv. $149.20) | −17.0% |

Plus an earlier $400M 4.25% 2032 convertible. Management repeatedly signalled capital sufficiency, then raised again — at progressively worse terms relative to the share price.

**e) New $245.1M of goodwill & intangibles appeared in 2025** — 3.5x revenue, 10% of total assets, on a company that previously carried none. Origin unverified; needs checking for related-party or spectrum-deal accounting.

**f) Inventory of $12.0M appeared in 2025** (132.7 days). Small, but new — watch for build-ahead of demand that hasn't materialised.

---

## 3. Beneish M-Score and Accruals Analysis

**M-Score = 30.134 → "HIGH RISK — likely manipulator." I reject this reading.**

The score is a mathematical artifact of a company crossing from zero revenue. Decomposing it:

| Index | Value | Why it's meaningless here |
|---|---|---|
| GMI | **−24.97** | Gross margin went from −1,333% (2024) to +53% (2025). Ratio explodes on a near-zero denominator. |
| AQI | **82.29** | PPE jumped $352M → $1,418M as satellites were capitalised. That's the business model, not manipulation. |
| SGI | **16.05** | Revenue grew 16x off a $4.4M base. |
| DSRI | 1.00 | No receivables-days deterioration in the model's terms |
| **TATA** | **−0.054** | **Negative total accruals — conservative, not aggressive** |
| **LVGI** | **1.749** | **The one genuinely informative component: leverage ratio up 75%** |

**Conclusion:** the M-Score is not applicable to ASTS and should be discarded. The only component carrying real information is **LVGI 1.749** — leverage is rising fast, which is independently confirmed by the debt trajectory ($12.8M → $2,239M in three years).

**Accruals trend:** +0.285 (2022) → +0.170 (2023) → −0.182 (2024) → −0.054 (2025). The early positive readings were driven by warrant/derivative fair-value marks, not operations. Current accruals are conservative. **No evidence of earnings manipulation. The problem is dilution and capital structure, not the P&L.**

**Altman Z-Score = 0.605 ("Distress") — also an artifact.** The model uses *book* equity ($2.39B) against a market value of $11.7B. Substituting market cap: x4 rises from 0.91 to 4.45, and **Z ≈ 2.73 — grey zone, not distress.** Liquidity is genuinely strong (current ratio 16.4x, net cash at YE2025). I will not claim solvency risk.

---

## 4. Competitive Threat Assessment: **SEVERE — this is the real thesis**

The moat has materially eroded, and the market has already begun to price it.

- **The EchoStar transaction is the pivotal event.** SpaceX acquired EchoStar's AWS-4 spectrum for direct-to-cell, giving Starlink *dedicated low-band D2C spectrum*. ASTS's core differentiator was that Starlink lacked the low-band spectrum needed for indoor/vehicular penetration. That argument is now substantially weakened. UBS downgraded ASTS specifically on this.
- **Structural supplier-competitor conflict:** ASTS must buy launches from SpaceX — its primary competitor. This is an unhedgeable dependency.
- **Execution risk has been realised, not theorised:** BlueBird 7 **failed to reach correct low-earth orbit**. Guidance slipped from "45–60 satellites by end-2026" to "45 satellites by early 2027."
- **Adoption is slow where it matters.** The class action and the Scotiabank downgrade both cite slow user adoption in the **US and Japan** — the highest-ARPU markets.
- **Capital asymmetry:** Starlink funds its constellation from free cash flow; ASTS funds its from converts at 1.6–4.25% while burning ~$1.1B/yr. Amazon Kuiper is a third entrant.

**The honest counterweight:** ASTS's Block 2 BlueBird apertures (~223 m²) deliver materially higher capacity per satellite than Starlink's DTC design, and the wholesale MNO model (50/50 revenue share, ~45 partners, ~3B reachable subscribers, with Google/AT&T/Vodafone/Verizon/Rakuten as both partners and equity holders) avoids consumer acquisition cost entirely. This is a real technology with real partners — not a story stock with nothing behind it.

---

## 5. Management & Governance Red Flags

1. **CEO selling at scale into the raises.** Abel Avellan filed a **Form 144 for 2.5 million shares in a structured sale to Citigroup worth ~$183M**. He also withheld 32,754 shares at $113.41 to cover RSU tax. A founder-CEO liquidating ~$183M while simultaneously issuing $2B+ of converts is a textbook signal.
2. **Clustered Form 4 distribution.** 30 filings in 2026, including **10 on 18–19 Aug 2026**, 5 on 16 Jun, 5 on 2 Jun. Systematic, calendar-driven insider distribution. (I could not parse buy/sell direction from filing metadata — treat the *pattern* as the signal, not the individual lines.)
3. **Securities class action, class period 4-Mar-2025 → 15-Jul-2026**, naming **Avellan and CFO/CLO Andrew Johnson**. Allegations map almost exactly onto my findings: overstated capital sufficiency, overstated competitive durability post-EchoStar, concealed slow US/Japan adoption, and dilution "at greater frequency and at greater scale than signalled." Lead-plaintiff deadline has passed; the case is live.
4. **CFO doubles as Chief Legal Officer** — no independent legal check on disclosure at a company under securities litigation.
5. **SPAC origin (2019/2021 merger) with super-voting share classes.** Avellan controls the company on a minority economic stake; public holders cannot effect change. Total shares ~408M vs 300M weighted-average diluted — the gap is insider super-voting stock.

---

## 6. Short Thesis Summary

**Is there a credible bear case? Yes — and it has been substantially validated.**

The thesis is not fraud. It is **permanent capital impairment through dilution**:
- 54.4M → ~408M shares in four years (7.5x), with revenue per share flat at ~$0.27.
- ~$4B+ of converts raised, interest now ~73% of forward revenue.
- Capex of $1,065M in 2025 alone; a 45–90 satellite constellation at ~$20–25M each implies **$1–2B more** to come.
- Consensus has the company **still loss-making in 2028** (EPS −$0.16) with first real profit in 2029 ($1.82) — on 1–4 analysts, i.e. extremely low-confidence numbers.
- Every capital raise has been a 9–17% one-day drawdown. That pattern is repeatable.

**But the trade has already worked.** At $133 the stock was ~370x trailing sales. At $28.58 it is ~70x 2026E revenue and ~24x 2027E — still expensive, but no longer absurd. The 78% drawdown has transferred most of the alpha to whoever shorted in January.

**What would still break the stock:** a failed launch campaign, a fifth convertible raise, an adverse litigation outcome, or Starlink DTC scaling in the US/Japan. **What would break the short:** a clean multi-launch cadence, a major MNO service launch, or a short squeeze in a 2.85-beta retail name with expensive borrow.

---

## 7. Contrarian Rating: **NO EDGE** (at $28.58)

**This was a Strong Short above $90. It is not a short here.**

I am explicitly declining to recommend a new short position, and I want to be clear that this is a judgement about *price*, not about the company. The forensic work confirms genuine, serious problems — flat revenue per share, 194-day DSO, interest at 73% of revenue, a live securities class action, and a CEO selling $183M while raising converts. None of that has been fixed.

But a short seller's edge is the gap between price and reality, and that gap has largely closed. Downside to a realistic bear-case fair value of $15–20 is 30–50%; upside on a successful launch cadence is a return toward $60–80. That is roughly 1:1 with a high-beta squeeze profile and costly borrow — a bad risk/reward, not a good one.

**Where I would re-engage short:** rallies above ~$60 into a financing window, or immediately following any announcement of a fifth convertible offering. **Where I would abandon the short entirely:** evidence of sustained launch cadence plus a Tier-1 MNO commercial launch in the US or Japan — at that point the wholesale model would be proving itself and the dilution thesis would lose its engine.

**The bull case is not weak.** Real patented technology, demonstrated direct-to-handset video calls, ~45 MNO partners, strategic equity from Google/AT&T/Vodafone, positive gross margin in Q3-2026 (40%), and ~$2.3B+ of cash. If management executes the constellation, the 2029 consensus of $2.6B revenue is not fantasy. My scepticism is about the *price paid per share of that outcome* — not about whether the outcome is possible.

---

### Gaps in this analysis (stated honestly)
- **10-K unavailable** (SEC 403 / no filing returned) — risk factors and the $245M goodwill origin are unverified.
- **Annual vs. quarterly COGS do not reconcile** ($33.0M vs $124.0M) — a data-integrity issue that must be resolved before sizing any position.
- **Insider Form 4 direction not parsed** — the clustering is documented; net buy/sell direction is inferred from the Form 144 and secondary reporting, not from the filings themselves.
- **Peer multiples unavailable** — the sector peer set returned mega-cap telecoms (VZ, TMUS, T) that are not meaningful comparables for a pre-revenue satellite operator. Valuation is therefore anchored to consensus estimates rather than a peer multiple.
