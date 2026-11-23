# Alt Data Analyst

- Symbol: GPN
- Elapsed: 50.1s

---
## Alternative Data Report — GPN (Global Payments Inc.)
**Data as of ~Nov 22, 2026 | Last close $91.83 (Nov 20) | Mkt cap $24.3B | Beta 0.82 | 52-wk range $61.16–$101.32**

**Critical framing up front:** GPN is currently a *deal-arbitrage instrument*, not an operating-story stock. On Oct 30 the shares gapped **+13% to $96.84 on 16.7M shares (~8x normal volume)** on a Bloomberg report that CD&R + GTCR were preparing a ~$40B+ take-private. On Nov 12 the stock **collapsed −13% to $88.19 on 9.9M volume** when the consortium dropped its pursuit. On Nov 20 it **rebounded +10% to $91.83 on 9.5M volume** after GTCR filed with the SEC that it is unilaterally exploring a ~$50B buyout (including debt), with "no definitive decision." Every alt-data signal below is therefore *second-order* to a binary event that alt data cannot price. I say so explicitly rather than dressing up operating signals as edge.

---

### 1. Consumer Demand Signals — **Weak / Declining**

| Signal | Read | Direction |
|---|---|---|
| Google Trends "Global Payments" (US, 12m) | May–Jun avg ≈31.6 → Aug–Nov avg ≈12.1, **−62%**; Nov 2025 ≈20–28 vs Nov 2026 ≈12, **−45% YoY**. Last 3 wks flat at 12/12/12 — low, not falling | ↓ |
| Google Trends "Netspend" (consumer brand) | Nov 2025 ≈76–79 → Nov 2026 ≈58–59, **−25% YoY**; off Oct lows (52–55), modest uptick | ↓ then stabilizing |
| Web traffic, globalpayments.com | Last month **+6.8% MoM**; bounce 41.7%, 2:11 duration, 4.4 pages/visit. But a SimilarWeb comparison shows a smaller rival (upayments.com) drawing *more* total visits in Oct 2026 | → / slightly ↓ |
| Web traffic, developer.globalpayments.com | **+394% MoM** — API/integration portal surging, a genuine positive leading indicator for merchant onboarding pipeline | ↑ |

**Interpretation:** These are the weakest signals in the pack. GPN is a B2B merchant acquirer — consumer search intent is a poor proxy for its revenue, which is driven by card volume, enterprise contract wins, and pricing. The Trends decline most likely reflects *post-deal-news noise and normalization*, not demand decay. **Important caveat:** both "Global Payments" and "Netspend" peak at exactly 100 in the week of Feb 22, 2026 — identical peak weeks across unrelated keywords is a hallmark of index normalization to a single high-volume event, so cross-keyword level comparisons are unreliable. My 5-year Trends request returned only the same 12-month window, so I could not validate whether the recent decline is secular or cyclical.

The developer-portal surge is the one genuinely encouraging data point: rising API engagement is consistent with management's "Genius adoption / higher enterprise volumes" narrative from the Q3 call.

### 2. Business Activity Signals — **Neutral, modestly constructive**

- **Job postings (qualitative only):** ~75 open roles in Georgia alone per Indeed; postings cluster in **platform/data engineering** (Senior Platform Engineer – Kafka & Streaming Data, NetSuite Developer, Product Owner) and **revenue capacity** (B2B Outside Sales, Field Software Sales), plus compliance/credit. This is a *Worldpay-integration + tech-modernization* hiring mix, not an aggressive growth-investment surge. Consistent with cost-synergy execution rather than top-line offense. **No quantitative count or trend series available** — the tool returns search snippets, not time series, so I cannot compute a hiring acceleration rate.
- **Patents:** USPTO PatentsView API **failed** (parse error). No patent series obtained. One retry not warranted given GPN's patent intensity is structurally low and non-informative for a payments processor.
- **Corroborating operating datapoint:** Q3 2026 call — management **raised the Worldpay cost-savings target** and **reaffirmed FY guidance**, with Genius adoption and higher enterprise volumes driving the beat and margins expanding. That is the single most reliable business-activity read I have, and it is company-sourced rather than alternative.

### 3. Earnings Preview Signal — **In-Line** (decaying from "Above")

GPN's beat record is immaculate but **the magnitude is collapsing** — this is the most actionable finding in the pack:

| Quarter | EPS Est → Act | Surprise % | Revenue Est → Act | Rev Surprise |
|---|---|---|---|---|
| Q3'26 (Nov 5) | 3.58 → 3.58 | **0.0%** | 3,181.7 → 3,182.0M | +0.05% |
| Q2'26 (Aug 5) | 3.44 → 3.46 | +0.58% | 3,163.7 → 3,159.1M | **−0.15%** |
| Q1'26 (May 6) | 2.78 → 2.96 | **+6.47%** | 2,812.9 → 2,856.3M | +1.5% |
| Q4'25 (Feb 18) | 3.16 → 3.18 | +0.63% | 2,305.8 → 2,320.3M | +0.6% |

- **Beat rate: 100% (7/7), avg surprise +2.21%** — but that average is carried by one outlier quarter (+6.47%). Ex-outlier, avg is ~+0.75%.
- Trajectory of surprise: 6.47% → 0.58% → **0.00%**. Revenue surprise: +1.5% → −0.15% → +0.05%. **The beat is fully priced and compressing toward a coin-flip.**
- Consensus for next print (Feb 17, 2027): **EPS $3.68, revenue $3.151B**. The sequential revenue *decline* implied ($3.182B → $3.151B) is consistent with a business no longer growing organically at the pace the 2026 roll-in quarters showed.
- **Verdict: In-Line.** Raised synergy targets support a small EPS beat, but revenue is already at parity with consensus. I see **no alt-data evidence of an upside surprise** — nothing in traffic, hiring, or search suggests accelerating volume.

### 4. News Sentiment Score and Summary — **Positive (0.75), but contaminated**

17 articles/30d: 7 positive, 1 negative, 0.75 score. **I discount this heavily.** The positivity is a mechanical artifact of (a) earnings-beat coverage on Nov 5 and (b) takeover speculation. The lone "negative" tag was applied to a *constructive* article ("GPN Bets on AI and Visa to Win More Transactions") — proof the keyword model is unreliable here. Substantive reads:
- **Nov 20 (SEC filing) / Nov 22:** GTCR exploring ~$50B takeout; no decision made. Deal-news-driven upside.
- **Nov 12:** consortium collapse — the source of the −13% de-rating.
- **Nov 13 Benzinga:** "Where is the Bottom for Global Payments?" — coverage tone shifted from momentum to capitulation-hunting.
- **Nov 10:** Visa IDX API partnership for AI-powered authentication (approval-rate lift, fewer false declines) — a real, if small, competitive positive.
- **13F cross-currents:** Danske Bank −16.6%; International Assets +1,029%. Institutional flow is mixed and backward-looking.
- **Nov 2:** Michael Burry publicly framed the GPN buyout math as a valuation benchmark for legacy payments (FISV to $100) — GPN is now the sector's M&A comp.

### 5. Social Sentiment — **Mildly bullish, thin and stale**
Proxy only (search snippets, no API). StockTwits snapshot shows price $97.66, prev close $94.98, **50-DMA $86.58** — retail framing is "breakout / approaching 52-week highs." YouTube content titled "GPN Stock Breakout! Is This the Start of a Major Move?" with implausible targets ($650) signals retail froth around the deal story. No quantified Reddit/StockTwits message-volume or bull/bear ratio available. **Low weight** — the quoted prices are stale relative to the $91.83 close, and retail chatter here is deal-driven momentum, not fundamental conviction.

### 6. Overall Alt Data Signal — **NEUTRAL**

Operating alt data is **in-line at best**: search interest weak but methodologically unreliable, consumer-brand (Netspend) interest down ~25% YoY, web traffic modestly positive with a strong developer-portal datapoint, hiring consistent with integration rather than growth, and earnings surprises compressing to zero. Nothing here generates an independent bullish or bearish operating call.

**The dominant variable — a live $50B take-private process — is invisible to every alt-data source I have.** Deal probability is not measurable from search, traffic, or hiring. Investors should treat GPN as a spread trade with an operating floor (100% beat rate, reaffirmed guidance, expanding margins, raised synergies) rather than as a stock where leading indicators have predictive power. Note the Feb 17, 2027 print may be moot if a transaction is announced first.

### 7. Confidence Level — **Medium-Low**

**Why not higher:**
- **Structural:** GPN is B2B; consumer-style alt data (Trends, app, social) is a weak proxy for a merchant acquirer's economics.
- **Trends normalization artifact:** identical 100-peak week across two unrelated keywords; the 5-year request silently returned 12 months, so no multi-year validation was possible.
- **Web traffic:** only relative SimilarWeb comparison snippets — no absolute monthly visit series, no MoM trend.
- **Job postings & social:** qualitative search proxies only; no counts, no time series, no bull/bear ratio.
- **Patents:** API failed outright — no data.
- **Peer benchmarking:** unavailable. `get_sector_peers` returned only ETFs/funds (VTI, VOO, BRK-A) — zero payment-processor comparables, so I could not contextualize GPN's multiple or relative performance.
- **Sentiment model:** keyword-based and demonstrably mislabels (flagged a positive article as negative).
- **Revenue base discontinuity:** FY2025 revenue actuals missed estimates by 17–19% in two quarters (e.g., $2.008B actual vs $2.410B est) due to the Worldpay acquisition and Issuer Solutions divestiture. **YoY comparisons are not apples-to-apples**, which undermines any "acceleration/deceleration" read across the series.
- **Recency:** Trends through wk of Nov 15; news through Nov 22; price through Nov 20. The deal situation is moving faster than any of these feeds.

**Bottom line for the investment memo:** Alt data does not add incremental edge on GPN this quarter — it corroborates a "steady, decelerating-to-in-line" operating picture that is already in consensus, and it is entirely dominated by an unmodelable M&A catalyst. Use it as a floor-check on fundamentals, not as a directional signal.
