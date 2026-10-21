# Alt Data Analyst

- Symbol: GM
- Elapsed: 63.7s

---
Verification paid off: the "122 days supply vs 80" figure traced to a **September 27, 2011** article — discarded. Industry days' supply entered 2026 at ~76 days (normal), so I have no credible evidence of 2026 inventory bloat. Writing the report now.

---

# GM — Alternative Data Signal Report
**As of Oct 22, 2026 | Price $77.09 | Mkt cap $67.6B | Next print: Jan 26, 2027**

## 1. Consumer Demand Signals — Brand interest intact YoY, decelerating sequentially ➡️↘️

| Keyword (US, Google Trends) | YoY read (Oct '25 → Oct '26) | Peak (12m) | Latest | From peak |
|---|---|---|---|---|
| Chevrolet | 57 → 61 (**+7%**) | 100 (Apr 12) | 61 | **−39%** |
| Silverado | 77 → 82 (**+6.5%**) | 100 (Mar 29–May 17) | 82 | −18% |
| GMC | 75 → 77 (**+2.7%**) | 100 (Jun 21/Jul 5) | 77 | −23% |

**Read:** Every GM brand is *up* year-over-year — this is not a demand collapse. But the within-year path is a clear downward glide: Chevrolet's last six weeks average 65 vs ~80 in Jul–Aug (−18%), and Silverado is off 18% from spring. Some of this is normal spring selling-season seasonality, and my 5-year seasonality baseline request silently returned 12-month data, so I **cannot cleanly separate seasonal from secular here** — that is the single biggest limitation on this section.

**Dealer-level evidence of promotional intensity** (October 2026 posts): model-year-end offers of **$15,000–$17,500 off MSRP** on Sierra/Silverado plus **0% APR for 60 months**. Model-year-end is seasonally normal, but this magnitude alongside a truck production pause points to GM buying volume with price rather than harvesting organic demand — a mix/margin headwind into Q4.

⚠️ **Web traffic: unavailable** (gm.com proxy returned no visit data). **App-store data: unavailable.**

## 2. Business Activity Signals — Neutral / low signal
- **Patents:** USPTO PatentsView API failed twice (empty response). **Gap — no R&D signal.**
- **Job postings:** Only qualitative proxy output. Third-party trackers show low absolute counts of GM software roles (34 in Detroit, 33 in Austin) — *suggestive* of restrained software hiring rather than the aggressive ramp the Super Cruise/software narrative implies, but sample is too thin to be actionable. **Treat as noise.**
- **Corporate actions (hard data, not alt):** Inventory discipline is the real business signal. GM is **pausing some truck production** and closing a Detroit battery assembly plant. I could not corroborate elevated 2026 inventory quantitatively — industry days' supply started 2026 at ~76 days (normal), and the widely-cited "122 days vs 80 normal" figure I found traces to a **2011 article** and was discarded.

## 3. Earnings Preview Signal — **In-Line, with downside skew**
Beat history is perfect on paper but **the cushion has visibly collapsed**:

| Qtr | Surprise % |
|---|---|
| Q3'26 (Oct 20) | **+0.27%** ← smallest |
| Q2'26 | +11.9% |
| Q1'26 | +41.8% |
| Q4'25 | +11.1% |
| Q3'25 | +22.3% |
| Q2'25 | +8.1% |
| Q1'25 | +3.7% |

7/7 beat rate, +14.2% average — but two consecutive quarters of decelerating surprise (11.9% → 0.3%). Q3 delivered **record revenue ($50.0B, +3% YoY; est. $48.8B)** and EBIT $4.1B (+22%), yet guidance was **narrowed to $14.5–15.5B from $14–16B** — a $500M cut to the top end — citing rising input costs and "intensifying" challenges.

Consensus for the Jan 26 print is **$2.82 EPS (+12% YoY on $45.2B rev)**. Alt data does not support an acceleration to +12%: brand interest is flat-to-down sequentially, incentives are heavy, and truck build is being throttled. Historically this setup still produces a small beat, so **In-Line** is the call — but the days of double-digit surprise upside appear over. Risk skews to the downside of $2.82.

## 4. News Sentiment — **+0.684 (Positive), but diverging from price** ⚠️
20 articles/14 days: 16 positive, 3 negative. The tone is flattered by the record-revenue/$20B-buyback headlines. **This is a classic sentiment-price divergence:** headlines score +0.68 while the stock fell **6.8% on 4× volume** (24.6M vs ~6M avg) — its worst day in over a year — and sits **15.6% below the July 28 peak of $90.11**. Negative threads: UAW + Michigan political attacks, battery plant closure, affordability, tariff/input cost inflation, and narrowing profit outlook. Sentiment score is stale/backward-looking; the tape is the truer signal.

## 5. Social Sentiment — **Unavailable**
Both Reddit and StockTwits proxies returned generic landing pages, not ticker discussion data. **No social signal.** Noting as a gap rather than guessing.

## 6. Overall Alt Data Signal: **NEUTRAL (cautious tilt)**

Genuine positives: brand search interest up YoY across all three brands, record revenue, $20B buyback, raised FCF outlook, record EV quarter (32,195 units, +60% — though I could not date-confirm this to 2026). Genuine negatives: earnings surprise cushion exhausted, guidance top-end cut, production pauses, heavy incentive spend, and a search-interest glide path that is not being offset by any positive alt-data offset (no traffic, hiring, patent, or social signal to lean on).

Net: alt data says GM's demand is **stable but soft, and being propped up by incentives** — not deteriorating fast enough to be Bearish, not strong enough to be Bullish.

## 7. Confidence Level: **MEDIUM-LOW**
Strong inputs: Google Trends (3 keywords, clean series), earnings surprise history, price/volume, news flow. Missing/degraded: web traffic, app data, patents (API failure), quantitative job postings, social sentiment (proxy failure), 5-year seasonality baseline (request returned 12m), and 2026 days'-supply (only a discredited 2011 figure). **Also unresolved:** one source reports GM US Q3'26 sales **−5.5%** (EV demand hit post-credit-expiry) while another reports **+7.7% to 710,347 units** — I could not adjudicate; this is the largest factual uncertainty in the report.

**Data lag note:** Google Trends is weekly and lags ~3 days; news sentiment is a headline-keyword count, not NLP. Alt data is leading, not definitive — and here the leading signals (incentives, production pauses, surprise compression) modestly precede a Q4 that consensus still models at +12% EPS growth.
