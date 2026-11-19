# Alt Data Analyst

- Symbol: CBRS
- Elapsed: 40.4s

---
I have enough to write. Patent data failed twice (noted as a gap). Writing the report now.

---

# CBRS — Cerebras Systems Inc. | Alternative Data Signal Report
**As of market close Nov 18, 2026** · Price $94.15 · Mkt cap ~$21.3B · Semiconductor / AI inference hardware

**Context:** Cerebras IPO'd May 14, 2026 (opened $350, closed $311.07 day one). The stock is now **-70% from its IPO close** and **-76% from its $386.34 intraday high**, having printed a low of $81.71 on Nov 5. Q3 FY26 was reported Nov 12.

---

## 1. Consumer Demand Signals

**Google Trends — "Cerebras" (US, 12-mo weekly)**
| Period | Interest |
|---|---|
| IPO week (5/10/26) | **100** (series peak) |
| Late Jun | 15–24 |
| Aug | 6–13 |
| Sep–Oct | 4–8 |
| Week of 11/1 | 7 |
| Week of 11/8 (earnings) | **10** |

**Direction: structurally decaying, tactical bounce.** Search interest is down ~90% from the IPO peak and sits in the 4–10 band — near-irrelevance for a $21B-cap name. The only positive is a +43% w/w lift into earnings week (7→10). This is a **retail attention decay** signal: the marginal buyer that absorbed the IPO has moved on. *Caveat: I pulled an NVDA series as a benchmark but Trends scales each keyword independently (100 = each series' own max), so cross-series comparison is invalid — only within-series trend is usable.*

**Web traffic — cerebras.ai (SimilarWeb, relative)**
- Last-month change: **+19.51% m/m**
- Pages/visit 3.29 · Avg duration 2:13 · Bounce 43.2%

**Direction: strongly up — the single best alt-data reading in this name.** Rising site traffic is consistent with management's reported **cloud & services revenue +272% YoY** (to $144.9M, cloud gross margin +510bps sequentially to 46.9%). Traffic and the fastest-growing revenue line are confirming each other. Caveat: only relative % change was retrievable, not absolute visits, and SimilarWeb estimates carry meaningful error bars.

**App data:** N/A — enterprise/infrastructure business, no consumer app surface.

## 2. Business Activity Signals

**Job postings — Direction: expanding, but skewed to the bottleneck.**
- ~19 software-engineering roles live on Indeed (CA); LinkedIn page at 131k followers
- Notable mix: **"Senior construction manager – colocation datacenter fit-outs," "Infrastructure Engineer (Data Center Operations)"** in Sunnyvale, plus roles in Tokyo, Toronto, Bengaluru

The hiring signal is positive on growth investment but diagnostically revealing: capacity-weighted labor demand (construction, DC ops) rather than pure silicon R&D. That corroborates the CEO's own on-air admission on Nov 13: **"We are behind schedule"** on data-center builds. Headcount data is inconsistent across sources (708 per profile vs "1000+" per a jobs board) — treat with caution.

**Patent filings — NO DATA (gap).** USPTO/PatentsView API returned a parse error on two attempts. I cannot confirm or deny R&D intensity from IP filings. This is a genuine blind spot given the company's wafer-scale differentiation claim.

## 3. Earnings Preview Signal — **In-Line, with downside skew to revenue *timing***

Revenue beat streak is intact and stable — this is the highest-quality signal I have:

| Quarter | Revenue | Consensus | Surprise |
|---|---|---|---|
| Q1 (4/17) | $171.4M | n/a | — |
| Q2 (6/23) | $191.3M | $181.2M | **+5.6%** |
| Q3 (8/12) | $209.9M | $190.6M | **+10.1%** |
| Q4 (11/12) | $230.9M | $214.7M | **+7.6%** |

4-for-4 revenue beats, +70% YoY, with adjusted EPS of **+$0.12 vs -$0.14 expected**. FY26 guidance was **raised**.

⚠️ **Critical data-integrity flag:** the earnings-surprise tool reports Q3 as a **-333% miss** (actual -$0.67 vs est -$0.155) and an average surprise of **-60.4%**. That is **GAAP** EPS versus an **adjusted** consensus — the two series are not comparable. The headline "66.7% beat rate, -60.4% avg surprise" is an artifact and should be discarded. Revenue is the only clean series here.

**Next print (Q4 FY26, ~Feb 2027):** Management guides **core revenue of $310–330M**, implying +34–43% q/q. Demand-side alt data supports it (traffic +19.5% m/m, $26.1B backlog, Microsoft/Oracle/AWS wins). Capacity-side alt data (construction-manager hiring, CEO's "behind schedule," OpenAI delivery delays) argues the ramp slips right. **Verdict: In-Line on demand, at-risk on recognition — expect the low end, and the OpenAI concentration (~majority of backlog) is an unhedged single-counterparty risk.**

## 4. News Sentiment Score and Summary

**Score: +0.84 (very positive)** — 20 articles, 23 positive vs 2 negative signals, 30-day window.

Coverage is dominated by post-earnings analyst upgrades: *"Strong Buy at 45% Below Its IPO Price"* ($199 target), *"Timely Buying Opportunity After The Collapse," "The Bull Case Just Got Stronger," "An Absolute Game Changer."* The Microsoft deal and raised guidance drove most of it.

**But treat this score as contaminated.** Three caveats: (a) the score is a naive keyword count that cannot distinguish tone nuance; (b) roughly half the sample is Seeking Alpha contributor opinion, not sell-side estimates — that is *narrative*, not consensus revision; and (c) **the positive tone directly contradicts the price action and a fresh legal event**. The single negative signal is material: **Pomerantz LLP opened an investor investigation on Nov 17** into Cerebras — a securities-claim precursor typical of a post-IPO collapse. A +0.84 score at all-time lows with a law firm circling is a **contrarian warning, not a buy signal.**

## 5. Social Sentiment

**StockTwits: ~71–73% bullish**, message volume flagged High (71/100 index), participation ratio 84 (High). Aggregator splits: next month 66% bull / 34% bear; next quarter 75% bull / 25% bear.

**Direction: retail is aggressively long into a -70% drawdown.** Combined with High message volume and a leveraged 2x ETF (CBRG) that "lost more than half its value in a month" before ripping +16% on Nov 13, this reads as a **crowded, momentum-addicted retail base** — a headwind and a volatility multiplier, not support. Reddit discussion was thin/indirect (search-proxy only).

## 6. Overall Alt Data Signal: **NEUTRAL** (bullish fundamentals, bearish tape & positioning)

The signals genuinely conflict, and the conflict is the finding:

**Constructive (high-quality):** Revenue beat streak 4/4 with stable magnitude · web traffic +19.5% m/m confirming +272% cloud growth · $26.1B backlog · marquee wins (Microsoft, Oracle, AWS) diversifying away from OpenAI · ~8–10x forward revenue after a 70% de-rating, vs 16x in August.

**Bearish (also high-quality):** **Price is the loudest alt signal.** CBRS gapped +11.2% on record results and 36.9M shares (3x normal volume) on Nov 13 — then **gave back the entire gap in three sessions**, closing Nov 18 at $94.15, *below* its pre-earnings level. That is textbook distribution into good news. It aligns with search interest at 90% below peak, 73% retail bullishness (no one left to convert), and a fresh securities investigation.

**Why Neutral rather than Bullish:** every demand-side alt signal is pointing the right way, but when a stock cannot hold a +11% earnings gap on triple volume, the market is discounting something the alt data doesn't capture — most plausibly the 2027 capacity ramp and OpenAI concentration. **Why not Bearish:** the revenue beat streak and traffic data are real, verifiable, and improving; this is a de-rating, not a demand breakdown.

**Watch triggers:** (1) Q4 revenue vs the $310M low end — a miss here breaks the beat streak and validates the bears; (2) construction-manager hiring as the cleanest proxy for whether the DC bottleneck is clearing; (3) whether the Pomerantz probe escalates to a filed class action; (4) Google Trends recovering above ~20, which would signal retail re-engagement.

## 7. Confidence Level: **MEDIUM**

Downgraded from High for these specific reasons:
- **Patent data unavailable** (API failure, 2 attempts) — R&D intensity is the core of the wafer-scale thesis and I have zero visibility
- **Earnings-surprise tool is corrupted** by GAAP/adjusted mismatch — I discarded it and rebuilt the analysis from raw revenue actuals
- **Social and web-traffic feeds are web-search proxies**, not API-grade; no absolute traffic, no quantitative sentiment distribution
- **Google Trends cross-series comparison invalid** due to independent scaling
- Company is **~6 months public** — no history of quarterly seasonality or revision patterns to anchor against
- News sentiment score is naive keyword counting and is contradicted by price, limiting its standalone value

**Lag note:** alt data leads revenue by 1–2 quarters; web traffic and hiring are the earliest, Trends is coincident with retail flows at best. All readings here are as of ~Nov 18, 2026 and predate any Q4 datapoints. This is a leading indicator, not a verdict.
