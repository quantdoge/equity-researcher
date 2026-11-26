# Alt Data Analyst

- Symbol: HPQ
- Elapsed: 50.3s

---
## HP Inc. (HPQ) — Alternative Data Signal Report
**Price $31.15 | Mkt cap $28.1B | Next print: 2027-02-23 (fiscal Q1 FY27, quarter ends 31-Jan-2027)**

---

### 1. Consumer Demand Signals — **Deteriorating**

| Metric (US, Google Trends) | Nov-2025 | Nov-2026 | YoY |
|---|---|---|---|
| "HP laptop" | 40 | 27 | **−32%** |
| "laptop" (category control) | 52 | 40 | −23% |
| "Dell laptop" (peer control) | 32 | 23 | −28% |
| **"HP printer"** | 31 | 34 | **+10%** |

- **Sequential is improving, YoY is not.** "HP laptop" bottomed at 22 in mid-October and has risen four straight weeks to 27 (+23%). The category control shows the same shape (36→40), so this is seasonal holiday shopping onset — not HP-specific recovery.
- **HP is losing a modest amount of search share.** HP's −32% YoY outpaces the category's −23% by ~9 points, while Dell (−28%) sits between. HP is at best holding parity with Dell in a shrinking-interest category.
- **Printing is the lone bright spot** and it matters: Printing is 19.7% operating margin vs Personal Systems' 3.0%. "HP printer" is the only keyword up YoY and is flat-to-firm sequentially. Supplies engagement is the most reliable profit proxy in the model, and it is *not* deteriorating.
- **Web traffic:** hp.com visits **−5.44% MoM** (SimilarWeb, Oct-2026), avg. visit duration 4:02. Directionally consistent with softening consumer pull.

⚠️ **Methodological caveat:** all four keywords spike simultaneously to index-100 in the week of 12-Apr-2026. Unrelated products don't spike together — this is a **brand/category-wide news event** (consistent with the memory-price crisis driving "why are laptops so expensive" search). It compresses the index and adds noise to YoY math, but the *relative* HP-vs-category gap survives the distortion.

### 2. Business Activity Signals — **No usable data (gap)**

- **Job postings:** proxy returned only generic Indeed landing pages with no counts or time series. No signal extracted.
- **Patent filings:** USPTO PatentsView API returned an error; one retry also failed. No signal extracted.
- This is a genuine blind spot. Neither corroborates nor contradicts the demand read.

### 3. Earnings Preview Signal: **BELOW consensus** (on quality; headline roughly in-line)

The most important thing in the alt data is what the Q4 "beat" was actually made of:

- **Reported** Q4 FY26 non-GAAP EPS $0.83 vs $0.748 est (+11.0%) — a headline beat.
- **Tariff refunds contributed $0.15/share.** Strip them out and EPS was **~$0.68 — a ~9% MISS.** Guidance explicitly assumes **no further refunds** in FY27. The beat was not operational.
- **Revenue grew 9.3% on 29% fewer units.** Commercial units −28% / revenue +23%; **consumer units −31% / consumer revenue −7%**. Growth is price-and-mix pass-through of memory inflation, not demand.
- **Consumer channel inventory is rising**, and HP cut prices to clear it — which is why Personal Systems margin landed at 3.0%, below its own guided floor and far from the 5–7% FY27 target.
- Memory/storage went from 15–18% to **~40% of PC BOM** in one year, and HP guides *further* increases in FY27 (slower).

**The alt-data cross-check agrees with the unit story.** Google Trends showing "HP laptop" down 32% YoY is exactly what −31% consumer units should look like. Two independent datasets, same conclusion: end-market unit demand is contracting at a high-teens-to-low-30s rate.

**On the setup:** beat rate 85.7% (6 of 7), avg surprise +8.0%, with FY26 surprises accelerating (+5.9%, +21.0%, +25.0%, +11.0%). Management has a documented sandbagging pattern and guided Q1 to $0.66–$0.76 against consensus of $0.74 (our feed) / $0.70 (street). A modest headline beat is the base case. **But the beat will be low-quality, and Q1 consensus for $14.81B revenue (+2.6% YoY) is the number actually at risk** — holiday-quarter consumer softness plus a channel-inventory flush is a bad combination.

⚠️ Note the **non-GAAP definition change**: Q1 FY27 excludes stock-based comp, worth ~$0.38/share on FY26 (~$0.09–0.10/quarter). Optically the YoY EPS comparison will look ~$0.10/quarter better than underlying reality.

### 4. News Sentiment Score: **+0.73 (Positive, 20 articles)** — but stale and low-information

- 13 positive / 2 negative signals over 30 days; the 7-day window returns an identical score, i.e. **all coverage is from a single day (25-Nov-2026)** and nothing has printed since.
- Tone is euphoric on the beat: *"Why HP Inc. Stock Jumped Nearly 15%"*, *"standout gainer in the tech rout."*
- Dissenting notes are the ones that matter for forward returns: *"Prudent Guidance Amid Rising Memory Costs"* (WSJ), *"Memory Costs Are The Risk"*, *"PC Margin Pressure and Cautious Outlook."*
- **Sentiment is fully priced.** A +11.5% single-day re-rating on a "prudent" guide that *assumes no repeat tariff refunds* means the bar for the February print has been raised, not lowered.

### 5. Social Sentiment — **No usable data (gap)**

Reddit/StockTwits proxy returned only price-quote aggregator pages, no discussion volume or tone. Cannot confirm whether retail positioning is crowded long after the earnings pop. Open gap.

### 6. Overall Alt Data Signal: **BEARISH** (moderate conviction)

The bear case is not "HP misses Q4-style." It is that **the revenue line is being propped up by price increases on collapsing unit volumes** — a self-limiting mechanism. Consumer units are down 31%, channel inventory is building, search interest is down 32% YoY, traffic is down 5% MoM, and the segment margin is 3.0% against a 5–7% target. The one offset — Print — is stable, not growing.

What would change this view: a sustained print in printer search interest (the profit engine) or a decisive turn up in the category control before the January quarter close.

**Caveat on timing:** HP's sandbagging history means the Q1 *headline* likely beats. The bearish signal is about beat quality and the FY27 trajectory, not the February print alone.

### 7. Confidence Level: **Medium**

**Why not High:**
- **Only ~2 weeks of the target quarter is observable.** Google Trends data ends 15-Nov-2026; the quarter closes 31-Jan-2027. ~85% of Q1 is unobserved. This is the binding limitation.
- Two of four business-activity feeds (job postings, patents) produced nothing.
- Web traffic is a single Oct-2026 point estimate scraped from a search snippet, not a time series — one data point cannot establish a trend.
- News sentiment is keyword-count based, n=20, and entirely clustered on one day; it tells us about the Q4 print, not the Q1 outlook.
- Google Trends is normalized per-window and distorted by the April-2026 category-wide spike.

**What raises confidence in the directional call:** the Google Trends read is confirmed by three independent controls (category, peer, printer) and — critically — corroborated by hard reported unit data (−31% consumer units, −28% commercial units). That's two unrelated datasets converging, not a single noisy feed.

**Lag note:** alt data leads, it does not confirm. Consumer search weakness typically precedes reported revenue by one to two quarters, which puts the impact squarely on the Feb-2027 print and FY27 guidance. Leadership transition adds noise — **Emma Walmsley becomes CEO on 4-Jan-2027**, mid-quarter, and a new CEO has every incentive to reset the bar.
