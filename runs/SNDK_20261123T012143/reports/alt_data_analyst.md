# Alt Data Analyst

- Symbol: SNDK
- Elapsed: 38.6s

---
# SNDK (SanDisk) — Alternative Data Signal Report

**As of:** Nov 20–22, 2026 | **Price:** $79.24 split-adj. (≈$790 actual) | **Mkt cap:** ~$90B (split-adj. basis, ~$115–122B actual)

### ⚠️ Data Integrity Note (read first)
1. **Split distortion.** The historical series returned to me is retro-adjusted by ~10x. Barron's ("Sandisk Stock Looked Like it Fell 87%. Here's What Really Happened") and 24/7 Wall St ("a stock split is about to put it under a microscope") confirm an announced ~10-for-1 split. **All percentage moves and relative comparisons below are valid; absolute dollar levels are 1/10th of traded prices.** This also explains the apparent $4.50 price at the Feb-2025 WD spinoff — the stock actually spun off near $45.
2. **My initial price pull stopped at Feb-2026.** I re-pulled through Nov 20, 2026 — the real story is a **73% drawdown from the June 2026 peak**, not the 17x run-up I first saw.
3. **Failures:** USPTO patent trend returned a parse error twice (gap). Social sentiment returned only generic page metadata, no score (gap). Sandisk IR press release blocked (403) — EPS guidance not retrieved.

---

## 1. Consumer Demand Signals
| Signal | Reading | Direction |
|---|---|---|
| Google Trends, "SanDisk" (US, 5y) | 20 (Nov-25) → **100 peak (Apr-26)** → **22–27 trough (Sep–Oct-26)** → 42 (mid-Nov-26) | ⚠️ **-73% off peak**; Nov bounce is crash-driven |
| Google Trends, "NAND flash price" (12m) | Elevated Jan–Jul-26, **peak 100 late-Jun-26** → ~0 Aug–Oct-26 → 4–5 Nov-26 | 🔻 **Collapsed** |
| Web traffic, sandisk.com | More visits than westerndigital.com (Oct-26); support-it subdomain **-53.6% MoM** | 🔻 Mild |

**Interpretation — this is the most important nuance in the report.** Search interest in "SanDisk" peaked in April 2026 and decayed ~75% into the autumn. The recent uptick to 42 coincides exactly with the November equity crash, i.e. it is *retail rubbernecking, not demand*. Meanwhile "NAND flash price" search interest — a genuine leading proxy for the pricing cycle — **peaked in late June 2026 and went to zero by August.** That turn came roughly **four months before the stock broke.** (Zero readings are partly Trends data-completeness artifacts; the directional collapse is not.)

Also note: web traffic is a *consumer-brand* metric, while SanDisk's growth is now **data-center led (+64% QoQ datacenter revenue; data-center portfolio up ~1,700%)**. Consumer funnel data has low read-through to the actual revenue driver. Treat as low-weight.

## 2. Business Activity Signals
- **Job postings (low confidence):** LinkedIn listings concentrate in hard engineering — *Staff FPGA Emulation Engineer, Staff Platform Firmware Engineer, Senior Engineer DFT, Staff System Design*. R&D/firmware-weighted, with no visible sales/GTM surge. Reads as **capacity and technology investment**, not demand expansion — consistent with a company spending into a cycle top. No quantitative counts available (Indeed's "1 open job" is a scraping artifact).
- **Patents:** **No data** — tool failed twice. Cannot assess R&D intensity trend.

## 3. Earnings Preview Signal: **Above on the print / Below on the guide**
- **Track record: 7/7 beats (100%), avg surprise +1,128%** (magnitude distorted by near-zero estimates early in the ramp). Recent quarters: **+6.2%, +12.4%, +701%.**
- Revenue ramp is extraordinary: $1.95B → $1.90B → $2.31B → $3.03B → $5.95B → $8.97B → **$11.03B** (Oct-26 quarter). ~5.7x YoY.
- **Consensus for Feb 4, 2027: EPS $7.10, revenue $12.48B.** Company guidance is **$12.2–12.6B** — midpoint $12.4B, i.e. **essentially in line, marginally light at the midpoint.**
- **Corroboration:** TrendForce has **4Q26 NAND contract prices +15–20% QoQ** — the strongest quarter of the cycle — and that pricing lands inside SanDisk's fiscal Q2. So the *reported* quarter should be solid, and a 8th consecutive beat is likely.
- **The problem is the guide, not the quarter.** TrendForce then sees **1Q27 flat-to-–5% QoQ, with declines spreading across all product categories from 2Q27**, and one report cites **-20% in 2027**, with **Chinese buyers cutting NAND purchases**. A Feb-2027 call that guides fiscal Q3 against that backdrop is **at high risk of being the first negative sequential guide in six quarters.** The market will trade the guide, not the beat.

## 4. News Sentiment Score and Summary
**Score: -0.067 ("neutral") | 20 articles/14d | 7 positive / 8 negative.**

A neutral score understates a real regime shift. The composition is the signal:
- **Negative, and new:** TrendForce's bearish 2027 NAND call (Nov 20) — *"SanDisk slides over 14% as bearish NAND pricing outlook hits chip stocks"*; *"Micron and SanDisk Plunge as Tech Rout Pushes Index Into Correction"*; *"Chinese buyers are cutting NAND purchases."*
- **Positive, and stale:** Barron's *"agonizingly cheap"*; Renaissance Technologies' 55x stake increase to $481M (a weeks-old 13F — *"a quant fund that never explains its trades just bet big on memory chips, right before the stock cratered"*); multiple Motley Fool buy recommendations.

**Flagging an unusual negative-coverage surge** concentrated in a single week (Nov 20–22) — a genuine shock, not drift. Most telling is MarketWatch's framing: *"Micron and Sandisk stocks might look like bargains, but analysts say that's actually a red flag — cheap valuation multiples for memory stocks have historically been associated with peak pricing levels."*

## 5. Social Sentiment
**Low confidence — no quantitative score retrievable.** Stocktwits shows retail sentiment at **"bullish," downgraded from "extremely bullish"** earlier in the cycle. Reddit proxy returned only generic quote pages. Directionally: retail conviction is decaying off a euphoric base, consistent with the -73% drawdown.

## 6. Overall Alt Data Signal: **BEARISH**
Weight of evidence, not headline count:

| Driver | Signal |
|---|---|
| NAND pricing cycle (TrendForce, Google Trends) | 🔻🔻 Decisively negative, and **led the equity by ~4 months** |
| Forward estimate direction | 🔻 Consensus still +13% QoQ, directly against 1Q27 flat/down |
| News flow | 🔻 Negative surge, peak-cycle valuation debate |
| Position/fund flow | 🟡 RenTech 55x adds — but stale, pre-crash |
| Company fundamentals | 🟢 100% beat rate, $5B buyback, datacenter +1,700% — **backward-looking** |
| Consumer demand alt data | ⚪ Not the driver; no offset available |

The decisive point: **the pricing-cycle alt data turned in July 2026, four months ahead of the November crash.** That is exactly the lead time alt data is supposed to provide, and it is unambiguously negative. Everything still bullish in the data set (beats, buyback, datacenter growth, cheap multiples) is either backward-looking or a classic cycle-top trap. The offsets are real, though: the equity has **already de-rated 73% from the June peak and 55% in three weeks**, so a meaningful amount of the 2027 pricing decline may already be discounted. That caps conviction rather than reversing the signal.

## 7. Confidence Level: **MEDIUM**
**Strengths:** The pricing-cycle signal is high-quality, corroborated by three independent sources (TrendForce contract data, Google Trends, sell-side/news narrative), and is precisely timed against the equity.
**Why not High:** (a) Patent trend and social sentiment both failed — half the "business activity" framework is empty; (b) job postings and web traffic are directional anecdotes with no quantitative series; (c) EPS guidance for the Feb-2027 quarter could not be retrieved (403); (d) the split-adjustment issue required correction, and I'd want a second source confirming the ratio; (e) **~2-month lag** between the Nov-20 pricing shock and the Feb-4 print — this signal could decay materially before it is testable.

**Bottom line:** Alt data says the NAND pricing cycle has rolled over and equity consensus has not caught up. The Feb-4 print will probably beat; the guide is where the risk sits. Watch 1Q27 contract price confirmations and any datacenter contract-length disclosure as the two falsifiers of this bearish read.
