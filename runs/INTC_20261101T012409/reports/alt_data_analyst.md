# Alt Data Analyst

- Symbol: INTC
- Elapsed: 37.9s

---
## INTC — Alternative Data Signal Report
**As of Oct 31, 2026 · Price $65.76 · Mkt cap $347.6B · Beta 2.23**

**Data note:** Two business-activity feeds (USPTO patent trend, SimilarWeb traffic) failed on both attempts. Job posting and social data came back as web-search proxies rather than quantitative time series. Those gaps are flagged where relevant.

---

### 1. Consumer Demand Signals — **Sharply Deteriorating**

| Keyword | 12-m Peak | Oct 2026 Level | vs. pre-rally baseline |
|---|---|---|---|
| "Intel" | 100 (Apr 12) | 21–29 | **below** (32–42 in Nov '25) |
| "Intel Foundry" | 100 (May 24) | **9–10** | **far below** (~20–32) |
| "Intel Core Ultra" | 100 (May 17) | 8–11 | **below** (10–13) |

This is the most important finding in the dataset. Search interest peaked in **April–May 2026** and decayed for five straight months *before* the stock topped out at $140.94 on June 22. Alt data led the price move by roughly 5–8 weeks.

The **"Intel Foundry" collapse from 100 to 9** (−90%) is the standout. The foundry customer-win narrative that powered the entire April–September re-rating has evaporated from public attention entirely — now running at a *third* of its pre-rally baseline. Similarly, "Intel Core Ultra" sits *below* its pre-rally level, indicating **no durable product-cycle demand pull** into the client segment. That is consistent with the reported CCG revenue decline of −5% YoY to $8.1B and management's framing of a PC market down 12% in 2026 and another 10% in 2027.

### 2. Business Activity Signals — **Neutral, Low Confidence**

- **Hiring:** Fab and process-engineering postings in Hillsboro, OR and Ocotillo remain active (216 electrical-engineering listings on Indeed; Foundry module development and process-integration roles live). No visible retrenchment, but no acceleration either. **Trend: flat.** Proxy only — LinkedIn's "8,000+ process engineer jobs" count is an inflated aggregation artifact and should be discounted.
- **Patents:** ❌ USPTO feed unavailable (API error, 2 attempts). No read.
- **Web traffic:** ❌ SimilarWeb proxy returned no usable series. No read.

Net: business-activity signals offer no offset to the demand deterioration, but the two most informative feeds are missing. Low confidence here.

### 3. Earnings Preview Signal — **Tracking BELOW consensus**

Next print: Jan 28, 2027 — consensus already reset to **$15.97B revenue / $0.29 EPS**, down from $16.51B / $0.52 in the just-reported quarter. Two things argue the reset is still not conservative enough:

1. Guidance was **$15.0–16.0B**, and consensus sits at the *very top* of that range ($15.97B). Zero cushion.
2. Every leading indicator — search-attention decay, foundry narrative collapse, the memory-cost squeeze on IT budgets, and management's own call for PC declines through at least H1 2027 — points to the low end.

**Caution on the 85.7% beat rate / +530% average surprise.** This is a statistical artifact: estimates in 4 of 7 quarters were sub-$0.02 penny figures (e.g., $0.0068 actual vs. $0.13), producing 1,400–1,800% "surprises" that carry no information. The genuine surprise magnitudes were more like +28% to +93%. Do not extrapolate the headline beat rate to Q4.

### 4. News Sentiment Score — **Neutral by count, clearly Negative in tone**

Score **−0.059** (20 articles; 8 positive, 9 negative). The keyword-counting model is understating the damage. Substance over score:

- "Intel Is Down 45% in October, Its Worst Month Ever"
- **Levi & Korsinsky securities investigation** — probing whether Intel's *August 2026 SEC offering materials* misrepresented customer demand before the below-consensus Q4 outlook
- CEO Lip-Bu Tan citing record memory prices straining corporate IT budgets
- CFO: **2027 unlikely to produce positive free cash flow**
- Analyst PT cuts: Goldman $150→$100; JPMorgan $85→$80 (Neutral). Northland's $120 Outperform is a lone outlier
- Intel dragged AMD and Arm down double digits in sympathy

The securities investigation tied to the August offering is a genuine non-fundamental overhang the sell-side notes are underweighting.

### 5. Social Sentiment — **Capitulation**

Stocktwits mention volume averages ~2,242/day, purely event-driven. Tone swung from "extremely bullish" during the October pre-earnings rally to open hostility post-print (Reddit: "plunges 24% after CFO said 2027 unlikely to produce positive FCF"; accusations management "purposely manipulated the stock"). Retail is now a **seller of rallies**, not a buyer of dips — the marginal momentum bid that carried the stock from $48 to $141 has been removed.

### 6. Overall Alt Data Signal: **BEARISH**

The single highest-conviction takeaway is timing. This alt-data set gave a clean, early warning: search attention peaked in **April–May**, five to eight weeks ahead of the June 22 price peak, and decayed monotonically through the summer. The stock ran another 40% on narrative while public engagement was already collapsing — the classic signature of a momentum unwind building under the surface. The Oct 30 gap-down from $92.07 to $65.76 (−28.6% on 455M shares, ~5x normal volume) was the release, not the cause.

Fundamental confirmation: demand is deteriorating on a *supply-chain input cost* shock (memory) that Intel does not control and management says extends through 2027 — a structurally unhedgeable margin problem. DCAI's +78% to $7.3B is real and genuinely strong, but it is being more than offset at the corporate level by a client segment that is shrinking and a foundry narrative with no visible commercial traction.

**Price context:** −53% from the June peak ($140.94), but still **+37% from April 1** ($48.03). This is a de-rating of an overshoot, not yet a valuation floor. Nothing in this dataset identifies where the momentum unwind exhausts itself.

### 7. Confidence Level: **Medium**

- **High confidence** in the Google Trends consumer-demand read and the news/social tone — clean series, high recency, and the lead/lag relationship with price is verifiable in-sample.
- **Low confidence** in business activity — patent and traffic feeds are missing, hiring is proxy-only.
- Directional confidence in the bearish call is supported by the fact that three *independent* signals (consumer search, news tone, social tone) plus management's own guidance all point the same way. That convergence is more informative than any single feed.
- **Caveat:** Google Trends measures *attention*, not unit demand. Its collapse implies the speculative bid is gone — it does not directly size the revenue miss. And post-crash attention spikes (visible from the Oct 25 uptick to 29) are typically capitulation, not accumulation, so do not read a trends rebound as a buy signal.

**What would flip this:** memory pricing relief into H1 2027, a named external 18A/14A foundry customer, or DCAI growth compounding fast enough to offset CCG decline. None of those appear in this dataset.
