# Alt Data Analyst

- Symbol: CRM
- Elapsed: 55.0s

---
# ALTERNATIVE DATA DASHBOARD — SALESFORCE, INC. (CRM)

**As of:** November 17, 2026 close | **Price:** $194.52 | **Market cap:** $160.1B | **Beta:** 1.24 | **Employees:** 83,334
**Next catalyst:** Q3 FY27 earnings, **December 2, 2026** (consensus EPS $3.45, revenue $11.464B)

---

## 1. Consumer Demand Signals

### Google Trends — "Salesforce" (US, 12-mo) — **STRONGLY NEGATIVE**
| Period | Avg Interest | Change |
|---|---|---|
| Q2 CY26 (May–Jul) | 68.5 | — |
| Q3 CY26 (Aug–Oct) | 43.1 | **−37% QoQ** |
| Q4-to-date (Oct–Nov) | ~39.6 | −8% vs Q3 |
| Latest 2 weeks | 41 → **35** | −15% w/w |

Search interest has roughly **halved from the June 2026 peak (82 → 35)**. The Feb 2026 spike (100) was news-driven and fully decayed. **Q3-to-Q4 decay is 37% — the sharpest sequential drop in the visible series.** For a subscription software business, brand-search interest is a *weak* proxy, but directionally it argues against an inflection in net-new customer activity.

### Google Trends — "Agentforce" (US, 12-m) — **SEVERELY NEGATIVE (key finding)**
- Peak: **100 (late Apr 2026)**, secondary 98 (May 31)
- Jul avg ≈ 46 | Aug ≈ 30 | Sep ≈ 29 | Oct ≈ 32 | **Nov 8: 19**
- **−70% to −80% from the May peak**

This is the single most important alt-data read in the file. Agentforce is the entire bull case, and its **product-level mindshare has decayed by roughly three-quarters.** Critically, this decay *preceded* the stock's decline: Agentforce interest broke down in July, while CRM did not peak until **September 3 ($263.97)**. That is a bearish divergence — price re-rated on the *financial* Anthropic stake gain while the *product's* organic pull was already fading.

### Web Traffic — **MILDLY POSITIVE (offsetting signal)**
| Domain | MoM Change | Bounce | Pages/Visit |
|---|---|---|---|
| salesforce.com | **+2.19%** | 28.1% | 5.52 |
| login.salesforce.com | +1.69% | — | — |
| salesforce-sites.com | +2.08% | — | — |

All three properties up ~2% MoM with healthy engagement (5.5 pages/visit, 28% bounce implies genuine working sessions). **This partially contradicts the search-interest collapse** — traffic is stable-to-up, suggesting the Trends decline is hype/news decay rather than actual usage loss. Session-based activity is a better read on an installed base; I weight this as a genuine if modest positive.

---

## 2. Business Activity Signals

### Job Postings — **NEGATIVE (and the proxy is uninformative)**
The search proxy returned only licensed-skill listings (e.g., "Salesforce experience required" = 30,632 jobs — those are *other* companies hiring Salesforce admins, not Salesforce hiring) and no quantitative posting counts. **Treat the proxy as failed.** However, hard news fills the gap:
- **Nov 17, 2026 (BI):** "Salesforce has started cutting **more** jobs, internal messages show" — following earlier 2026 layoffs.
- **Nov 17, 2026 (BI):** Salesforce imposed **monthly AI token budgets (up to $1,000/employee)** after staff spent "thousands of dollars per month on tokens" last quarter.

Read: hiring/headcount trend is clearly **contracting** — good for near-term margin/EPS, bad for growth-investment signal. The AI-token memo is an under-appreciated datapoint: **AI inference cost is materialising as a real gross-margin headwind** (and a governance problem), not purely a tailwind. This is a COGS creep signal not yet in most models.

### Patent Filings — **NO DATA**
USPTO feed failed on both attempts ("Salesforce" and "salesforce.com, inc."). Gap acknowledged; no inference drawn.

### Distribution/Positioning — **NEGATIVE**
Price/volume action is the strongest business-activity tell available:
- **Sept 3 high: $263.97 → Nov 17: $194.52 = −26.3%**
- **Nov 17: −9.45% on 13.2M shares** vs ~5–8M recent average → **heavy distribution volume**
- Lowest close since **Aug 17**; biggest one-day % decline since **May 2024**
- **The entire post-Q2 (Aug 26) re-rating has been fully round-tripped** — stock closed $205.26 on Aug 26, ran to $251 on the Anthropic gain, and is now *below* the pre-earnings level. The market has explicitly rejected the "Anthropic mark-to-market / Agentforce" narrative.

---

## 3. Earnings Preview Signal: **IN-LINE** (EPS skew above, revenue skew at-risk)

**Historical surprise (7 quarters): 100% beat rate, +22.2% average surprise.**

| Quarter | EPS Est | Actual | Surprise | Rev Beat |
|---|---|---|---|---|
| Aug 2026 | 3.27 | 5.90 | **+80.4%** | +0.13% |
| May 2026 | 3.13 | 3.88 | +24.0% | +0.72% |
| Feb 2026 | 3.05 | 3.81 | +24.9% | +0.08% |
| Dec 2025 | 2.86 | 3.25 | +13.6% | **−0.15%** |
| Sep 2025 | 2.78 | 2.91 | +4.7% | +0.94% |

**The beat is mechanical, not operational.** The +80% August print was driven by the **Anthropic investment gain** — non-operating and non-recurring. Revenue is a metronome: **five of the last five prints landed within −0.2% to +0.9% of consensus.**

For Dec 2: Q3 revenue guide is **$11.42–11.50B**; consensus **$11.464B** sits in the **upper half** of the range — leaving little room for a standard beat. Cost cuts support another EPS beat (est $3.45 vs. recent patterns), but search-interest decay and headcount contraction argue the *top line* skews to the low end. **cRPO accelerating to +14% YoY ($33.5B) is the one genuinely bullish hard datapoint** — but it is reported data, already public since Aug 26, and thus *not* an alt-data edge.

> **Verdict:** likely modest EPS beat (cost-cut driven, lower quality), in-line revenue. Not a differentiated positive.

---

## 4. News Sentiment Score: 0.692 (11 pos / 2 neg / 20 articles) — **SCORE IS UNRELIABLE, IGNORE IT**

The keyword counter is contaminated. It labelled *"Stock Market Today: Salesforce **Plummets 9%**"* as **positive**, and scored the layoffs story "neutral." True 7–14 day tone is **deteriorating with a sharp negative inflection on Nov 17**.

Actual news mix:
- **Negative/structural:** −9.45% session; tech-outage scare hitting software reliability ("particularly vulnerable to AI misuse" — analyst via MarketWatch); **new internal layoffs**; AI token-cost blowup; Freshworks alums raise $53M (Dreamteam) for **AI-native CRM** — direct new entrant.
- **Positive:** Slack momentum (Slackbot adoption surge, **premium upgrades tripled**, Agentforce integration); Agentforce described as "booming"; Zacks ranks CRM over ORCL on AI monetisation; stock >30% below Dec-2024 high (value framing).
- **Genuine bull/bear crux:** *"Agentforce is booming, yet shares keep sliding as investors fear AI agents will gut the software model."*

---

## 5. Social Sentiment: **BIFURCATED / BEAR-NARRATIVE DOMINANT** (qualitative only)

Reddit (r/investing, r/wallstreetbets) themes, roughly balanced in volume but the bears have the coherent thesis:
- **Bear (thesis-driven):** *"Next time you're told to buy Salesforce, think again"* — AI (incl. Anthropic's own models) is a structural threat to seat-based per-seat pricing; *"Salesforce investors ignoring the obvious AI concerns."* This is a **model-disruption** argument, not a multiple argument — the more durable kind.
- **Bull (mean-reversion):** *"CRM oversold, asymmetric opportunity for massive re-rate"* — trading at ~50% discount to ATH (note: actual is −26% from Sept high / −33% from Dec-2024 high, so retail is overstating the discount).

High two-sided debate volume at a 52-week-adjacent low is a classic **bifurcation/bottoming characteristic**, but it is not a catalyst. No actionable directional edge; no quantitative score available.

---

## 6. Overall Alt Data Signal: **BEARISH** (moderate conviction)

| Signal | Direction | Weight |
|---|---|---|
| Agentforce product interest (−70/80% from peak) | Strongly negative | High |
| Salesforce brand search (−37% QoQ) | Negative | Medium |
| Web traffic (+2% MoM) | Positive | Medium |
| Hiring / headcount (layoffs, token caps) | Negative | Medium |
| Patent filings | No data | — |
| News sentiment (true tone) | Negative, inflecting | Medium |
| Social sentiment | Bifurcated, bear thesis coherent | Low |
| Earnings mechanical beat (cost cuts) | Positive but low-quality | Low |

**The core insight:** CRM's problem is not the quarter — it is a **demand-mindshare decay that the alt data saw first**. Agentforce search interest broke down in **July**, two months before the stock peaked on **September 3**. Web traffic holding up while search interest halves tells us this is a *narrative and mindshare* problem rather than a churn problem — but narrative problems are what compress the multiple on a 26%-drawdown, $160B-cap software name with a live "AI eats the seat" debate and a well-funded AI-native competitive wave. The Nov 17 tape (−9.45% on 1.7–2x normal volume, full round-trip of the post-earnings gap) confirms the market is now pricing model risk, not execution risk.

**What would flip this to Neutral:** Agentforce search interest stabilising above ~35–40, or salesforce.com traffic accelerating beyond +4% MoM — i.e., evidence the AI product is re-accelerating mindshare into the Dec 2 print.

---

## 7. Confidence Level: **MEDIUM**

**Strengths:** Google Trends at weekly granularity for both the corporate brand and the flagship product; complete 7-quarter surprise history; fresh (same-day) Nov 17 news including internal memos; full price/volume confirmation.

**Limitations and lag:**
- Google Trends is a **hype/news proxy**, not a revenue proxy — enterprise software procurement is RFP-driven and invisible in search. Directionally informative, not predictive of a specific quarter.
- Trends series stale through **Nov 8** (9-day lag); the Nov 8 Agentforce print of 19 is a single week and noisy.
- **Web traffic and job postings were low-quality search proxies, not SimilarWeb/Thinknum API pulls** — the +2.19% figure is an unsourced search snippet, and the job-postings feed returned licensed-skill listings rather than Salesforce headcount. Both should be treated as weak evidence.
- **Patent filings: unavailable** after two attempts — no R&D-intensity read.
- **News sentiment score (0.692) is demonstrably mis-signed** and should not be used; my negative read is based on manual article review.
- Social sentiment is **qualitative only** (search results, no quantitative Reddit/StockTwits score).
- No comparable alt-data read on peers → **cannot isolate Salesforce-specific signal from software-sector beta.** The Nov 17 decline was partly sector-wide (outage/AI-misuse scare, tech jitters, Nvidia earnings).

**Bottom line:** Alt data is a leading indicator, not a verdict. Here it leads bearish on forward demand and mindshare while the confirmed cRPO (+14%) and stable web traffic argue the installed base is not yet cracking. I would treat this as a **multiple-compression / de-rating signal** — set up for an in-line Dec 2 with likely EPS beat — rather than an imminent fundamental break.
