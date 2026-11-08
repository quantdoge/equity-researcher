# Alt Data Analyst

- Symbol: AMD
- Elapsed: 27.7s

---
Patents API is dead (two attempts, both errors) — noting as a data gap. Writing up now.

---

# AMD — Alternative Data Signal Report
**As of:** Nov 6–8, 2026 | **Price:** $449.04 | **Mkt cap:** $733B | **Next print:** Feb 2, 2027

**Context:** AMD is in a sharp drawdown — peak $649 (Oct 6) → $449, **-31%**, with a -17% single-day crash on Nov 5 (broad AI-infra de-rating) and a +11% snap-back Nov 6. It has exited the $1T club it entered in September. Beta 2.49 — this is a high-torque name where sentiment, not fundamentals, is currently setting the price.

---

## 1. Consumer Demand Signals — **Bearish / Decaying**
| Series | Peak (12m) | Now | vs. Year-Ago Base |
|---|---|---|---|
| "AMD Ryzen" (US) | 100 (mid-Apr '26) | **13** | 21–24 → **-40%** |
| "AMD EPYC" (US) | 100 (May 24 '26) | **17** | 34–37 → **-52%** |
| "AMD stock" (US) | 100 (May 3 '26) | **64** | 48–55 → **+20%** |

- Product-level search interest for **both** client (Ryzen) and server (EPYC) silicon is at **12-month lows**, down 83–87% from spring peaks and roughly **half the year-ago baseline**. The Mar–Jun spike was launch/event-driven and has fully unwound.
- **Divergence worth flagging:** *stock* search interest (64) is near 4-month highs while *product* search sits at lows. Retail attention is being driven by price action and AI narrative, **not** by organic product pull. That is a flow-driven tape, not a demand-driven one.
- **Interpretation caveat:** Google Trends is a weak proxy for server silicon — EPYC demand is set by hyperscaler procurement contracts, not consumer search. Weight this signal **low-to-medium** for the data center segment; weight it **medium** for the Client/PC segment, where the Ryzen decay genuinely argues for softer Q4 client revenue.

## 2. Business Activity Signals — **Bullish (qualitative only)**
- **Hiring:** Active and *forward-leaning* postings — "CVP, Business Development – NeoCloud & Data Center Providers" (Seattle), Data Center Technical Due Diligence & Assurance Engineer, Senior Linux/EPYC OS-enablement engineers, Data Scientist (Sales Ops). ~137 data-center-tagged AMD roles visible. The mix skews toward **new-customer/channel expansion** rather than maintenance — consistent with the guidance raise.
- **Patents:** ❌ **Data gap.** USPTO PatentsView API failed on three attempts. R&D-intensity trend unavailable.
- **Web traffic:** ❌ **Data gap.** SimilarWeb proxy returned no usable amd.com series.
- **Critical limitation:** hiring data here is a **web-search proxy with no time series** — I can confirm AMD is hiring into data center/neocloud, but I *cannot* measure acceleration vs. last quarter. Treat as directional color only, not a scored signal.

## 3. Earnings Preview Signal: **In-Line** (near-term) / **Above** (just-delivered)
- **Just reported (Nov 3):** EPS **$2.09 vs $1.95 est (+7.2%)**; revenue **$13.38B vs $13.10B (+2.1%)**. Data center revenue **doubled YoY**; record EPYC shipments.
- **Surprise history: 7-for-7 beat rate, +5.18% average magnitude.** Most recent four quarters beat by +7.2%, +2.5%, +6.2%, +15.9% — the beat cadence is *stable to improving*, not decaying.
- **The bar for Feb 2, 2027 is very high:** consensus **$17.01B revenue (+27% QoQ)** and **$2.91 EPS (+39% QoQ)**, against FY27 growth guided at **>80%** (more than doubled from prior forecast).
- **My read:** alt data supports the *data center* half of that ramp (hiring skew, EPYC share gains, competitor supply delays through H2'27) but **does not** support a +27% QoQ step-up in the *client* half given the Ryzen search collapse. Net: **In-Line for Q4**, with the beat/miss risk concentrated in Client and the upside optionality in Data Center. Note this is a ~3-month-out preview — alt-data lead times don't yet cover the Feb quarter.

## 4. News Sentiment Score — **+0.913 (Highly Positive)** ⚠️
20 articles / 14 days: 22 positive signals vs 1 negative.
- Tone is dominated by **"buy the dip"** framing (Motley Fool: *"Fell Below the Price I'd Pay"*, *"Should You Buy the Dip?"*, *"1 Reason to Buy Before 2027"*), plus *"Wall Street Is Dumping AI Stocks Even as Business Booms."*
- **But there is real two-sided disagreement:** Seeking Alpha published an **upgrade to Buy** ("AI Panic Meets Outsized CPU/GPU Gains") and a **downgrade to Hold** ("This Selloff Isn't Enough" — valuation + NVDA/Arm competition) *on consecutive days*. Zacks favored NVDA over AMD on profitability and ROE.
- **Interpretation:** a 0.91 score is a keyword-counter artifact, and on a name still trading at ~50x forward earnings after a -31% drawdown, uniformly bullish retail-facing coverage is a **crowded-long risk flag**, not confirmation. I discount this score materially.

## 5. Social Sentiment — **Volatile / Two-Sided, no score**
- Reddit r/wallstreetbets: *"AMD -17% Thursday, +11% Friday. What a week"* — extreme realized-vol regime. Also *"AMD is as overvalued as it gets. Numbers are just bonkers"* vs. bulls citing data center revenue nearly doubling.
- r/investing shows **capitulation**: a multi-year holder reports having "completely pulled out."
- **Data gap:** StockTwits proxy returned irrelevant results (no usable sentiment score). No quantitative social metric available — qualitative read only.

## 6. Overall Alt Data Signal: **NEUTRAL (slight cautious tilt)**
The alt-data set is **internally conflicted**, and the conflict is the signal:

| Dimension | Signal |
|---|---|
| Earnings-surprise track record | **Bullish** (7/7 beats, +5.2% avg) |
| Business activity / hiring | **Bullish** (qualitative) |
| News sentiment | Bullish but **crowded** |
| Product search demand | **Bearish** (-40% to -52% YoY) |
| Attention divergence (stock↑, product↓) | **Cautionary** |

**Bottom line:** fundamental alt data says the business is accelerating — 100% beat rate, doubling data center revenue, an >80% FY27 guide, and hiring pointed at neocloud expansion. Demand-side alt data says organic product pull has faded to 12-month lows. The reconciling story is that **AMD's 2027 is a data-center-procurement story, not a consumer-demand story** — which means the Feb guide is achievable on the data center leg but vulnerable on Client, and the stock's -31% drawdown has reset valuation without yet resetting the >80%-growth expectation embedded in it. **No differentiated edge to add or remove risk here.**

## 7. Confidence Level: **LOW-TO-MEDIUM**
**Why medium (fundamentals):** earnings calendar and surprise history are complete, hard data, 7-quarter depth.
**Why low (demand/sentiment):** three of six planned data sources failed outright (**patents, web traffic, StockTwits**), job postings returned no time series, and the MI300 search keyword returned unusable sparse-zero data. The Google Trends signal is real but a weak proxy for B2B silicon demand and is distorted by an anomalous Mar–Jun launch spike.

**Data limitations & lag:** Google Trends is weekly and revision-prone; news sentiment is a naive keyword counter over a 14-day window; hiring is a search proxy, not a Thinknum/LinkedIn count; no satellite, app-store, or channel-inventory data available. Alt data is a *leading* indicator — it does not resolve valuation, and at 50x forward earnings on a 2.49-beta name, multiple compression can dominate fundamentals for several quarters regardless of what these signals say.
