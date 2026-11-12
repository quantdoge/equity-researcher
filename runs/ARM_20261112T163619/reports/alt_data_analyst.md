# Alt Data Analyst

- Symbol: ARM
- Elapsed: 35.8s

---
# ARM Holdings (ARM) — Alternative Data Signal Report
**As of: Nov 12, 2026 close ($202.34) | Mkt cap ~$215.7B | Sector: Semiconductors (UK-domiciled, US ADR)**

**Price context (essential for reading alt data):** $109 (Dec-25) → blow-off peak $439 close / $452.70 intraday (Jun 18-26) → −54% drawdown to $166.72 (Nov 5) → bounce to $202. The stock is halfway down a violent de-rating, one week after a Q2 FY27 print (Nov 4) that beat on revenue but missed on profit.

---

## 1. Consumer Demand Signals

**Google Trends — "Arm Holdings" (US, 12m):** Trend direction: **sharply deteriorating, at trough.**
- Pre-surge baseline (Nov-25 → Feb-26): 15–27
- Surge: 44 (Apr-19) → 67 (May-3) → **100 (week of May 31)** — peak attention coincided with the equity blow-off top (late May/early Jun)
- Decay: 71 (Jun-14) → 41 (Jun-28) → 21 (Jul-19) → **7–18 range** for the last 3 months; latest print 12 (Nov 1)
- Current level is **~40% BELOW the pre-surge baseline**. Retail attention has fully round-tripped and then some.

**Google Trends — "ARM stock":** peaked 100 (May 31) → 28 (Nov 1) vs. baseline 21–27. Only a modest earnings-week blip (26→28); no re-acceleration.

**Interpretation — two findings that matter:**
1. **Attention led price.** Trends rolled over in mid-June/July while the stock held $240–340 through August–September. Search interest was a genuine 6–8 week leading indicator of this de-rating.
2. **Attention is not confirming the bounce.** Price is +22% off the Nov 5 low, yet consumer search interest sits at multi-year lows. Historically in this series, rallies without attention support are thin, low-conviction squeezes, not accumulation. Rebound volume confirms this: Nov 5 capitulation 15.4M shares, then 6.5M / 6.2M / 4.2M / 6.8M / 1.9M on the way up — **declining volume into rising price**.

**Web traffic:** *Not available* — SimilarWeb proxy returned only navigational/competitor pages, no monthly visit series for arm.com. Gap noted.

---

## 2. Business Activity Signals

**Hiring — Trend direction: indeterminate.** Indeed listings show **~121 "Arm Holdings PLC" postings** (UK), with 81–84 "Arm careers" results concentrated in Cambridge; mix skews toward corporate/support roles (Indirect Tax, Deskside Support, Project Management) with some technical (SoC Software, GPU). No time series available, so **acceleration cannot be computed** — this is a level, not a trend. Low informational value this cycle.

**Patents — Data gap.** PatentsView API failed on two attempts (Arm Limited, Arm Holdings). **No R&D intensity read available.**

**Best available business-activity proxy — revenue mix (hard data from the Nov 4 print):**
- Total revenue $1,443M, **+27% YoY** (record, beat $1,379M est)
- **License & other $773M, +50% YoY** ← drove the beat; lumpy, deal-timing dependent
- **Royalty $670M, only +8% YoY**, and **−6% sequentially** from $715M in Q1 (which grew +22% YoY)
- Profit **missed** despite the revenue beat

**This is the single most important alt-data-adjacent signal in the dataset.** Arm's royalty line is the recurring, unit-volume-linked line (smartphones, consumer IoT, China handsets). Its deceleration from +22% to +8% and sequential decline is consistent with the collapse in consumer search interest and with soft consumer end-markets — and it means the growth "beat" was **quality-poor**: it came from pull-forward-able licensing and AI data-center deals, not from recurring royalty annuity expansion.

---

## 3. Earnings Preview Signal

**Next catalyst: Feb 3, 2027** (FQ3 FY27) — 11+ weeks out. Consensus: **EPS $0.56 (+30% YoY), revenue $1,541M (+24% YoY)**. Note consensus is already modelling *re-acceleration* off a $1,443M base.

**Signal: IN-LINE to BELOW consensus (quality-adjusted).**

| Quarter | EPS Est | Actual | Surprise |
|---|---|---|---|
| Nov-26 (Q2 FY27) | 0.48 | 0.52 | **+8.3%** |
| Jul-26 | 0.40 | 0.45 | +12.5% |
| May-26 | 0.58 | 0.60 | +3.5% |
| Feb-26 | 0.41 | 0.43 | +4.9% |
| Nov-25 | 0.329 | 0.39 | +18.7% |
| Jul-25 | 0.34 | 0.35 | +2.9% |
| May-25 | 0.52 | 0.55 | +5.8% |

- **Beat rate 7/7 (100%), avg surprise +8.1%** — but the *magnitude is compressing* (+18.7% → +2.9% → +4.9% → +3.5% → +12.5% → +8.3%), and the last two beats were licensing-driven, not royalty-driven.
- **Critically: beats no longer pay.** The Nov 4 revenue beat was met with a **−13% next-day move** ($191.80 → $166.72) on 15.4M shares. The "beat-and-raise premium" embedded in this name through H1 2026 has fully decayed. Alt data (dead search interest, decelerating royalties, no hiring acceleration) does **not** support the +24% YoY revenue re-acceleration consensus needs for the Feb guide.
- Estimate revision direction: unavailable in this dataset — gap noted.

---

## 4. News Sentiment Score and Summary

**Score: +0.684 (Positive) — 20 articles / 14 days: 16 positive, 3 negative.** ⚠️ Treat with heavy discount.

**Composition is the problem.** The positive skew is dominated by *buy-the-dip / valuation-debate* content, not fundamental upgrades:
- "Is Arm Stock a Buy on the Dip as Agentic AI Opportunity Emerges?" (Fool, positive)
- "Think Arm Is Too Expensive? 1 Thing You Need To Understand" (Fool, positive)
- "Intel, Arm, and Marvell Have Each Been Cut in Half Since June. Only 1 I'd Buy Now" (neutral)
- "Chip Stocks Rally After Slide" (positive)
- "OpenAI, Arm and Qualcomm executives react to post-midterm AI sell-off" (CNBC, neutral)

This is the classic **post-drawdown "is it cheap yet" media pattern**, which historically clusters *mid-de-rating*, not at bottoms — it marks attention returning to valuation rather than to fundamentals. The keyword-based score cannot see that "cut in half since June" is the actual operative fact. Also note the **macro overlay**: a post-midterm AI-capex/tech sell-off is pressuring the whole complex, so ~all ARM news flow is beta, not alpha.

---

## 5. Social Sentiment

**Reddit / StockTwits proxy — Mixed, two-sided, contrarian. No quantitative score available (gap).**
- r/investing: *"Someone talk me out of going long on ARM..."* — bears and bulls openly fighting; poster cites IPO $51 vs current price as valuation anchor
- r/wallstreetbets: *"Regard opens YOLO 5:1 long on ARM"* (leveraged long), *"ARM Earnings Puts"* (directional short into the print) — **simultaneous 5:1 leveraged longs and earnings puts**
- Older threads: *"The reason ARM is mooning 🚀"* — stale euphoria, now absent

**Read:** retail positioning is **split and agnostic**, with leverage on both sides. That is a *high-realised-volatility* signal, not a directional one. Notably, the euphoric "mooning" tone that characterised the May–June top is gone — bullish conviction has been broken even though price is +22% off the low.

---

## 6. Overall Alt Data Signal: **NEUTRAL (with a bearish quality-of-earnings tilt)**

**The bull case the alt data sees:** 7/7 beat record, +27% YoY revenue, licensing +50%, agentic-AI narrative intact, sentiment score +0.68, price +22% off the low, 100% beat rate.

**The bear case the alt data sees (and it is the higher-information half):**
1. **Royalty growth halved** (+22% → +8%) and fell sequentially — the recurring annuity is decelerating
2. **Search interest at multi-year low**, 40% below pre-surge baseline, *not* confirming the price bounce
3. **Rebound on declining volume** — no accumulation footprint
4. **Beats no longer rewarded** (−13% on a clean revenue beat)
5. **Consensus needs +24% YoY re-acceleration** in Feb, which no alt-data series supports
6. News positivity is a valuation-debate artefact, not an upgrade cycle

Net: the *momentum* signals that drove the 4x H1 rally are unambiguously exhausted; the *fundamental* signals are decelerating in the one line that matters (royalties). But price has already fallen 54% and the immediate post-earnings capitulation has been absorbed — so this is a **broken-momentum, quality-questioned name in a bottoming process**, not a fresh short or a fresh long. Neutral, tilted defensive.

---

## 7. Confidence Level: MEDIUM-LOW

**Reasons for restraint:**
- **Failed feeds (3):** patent filing trend (API error, 2 attempts — no R&D read), quantitative web traffic (no visit series), quantitative social sentiment (no scored data — all proxies are qualitative web-search snippets)
- **No hiring time series** — only a static count (~121 UK postings); acceleration, the only useful form of this signal, is unobservable
- **Google Trends lag:** data ends Nov 1; the post-earnings (Nov 4-12) attention read is missing, exactly the window that matters most
- **News sentiment is keyword-based** and structurally mis-weights the "cut in half" narrative
- **One-name, one-sector, high-beta (β 3.94)** — ARM is a pure AI-sentiment instrument; alpha from company-specific alt data is routinely swamped by sector flows (post-midterm AI sell-off in progress)

**What would change the call:** a re-acceleration in "ARM stock" search interest *with* rising volume (would signal real accumulation), a royalty number above +15% YoY in the Feb 3 print, or hiring data showing engineering acceleration. Absent those, treat the current bounce as a low-conviction retracement.

*Alt data is a leading indicator, not a definitive one. All trend readings above are directional and qualitative except the revenue/EPS history and price/volume series, which are hard data.*
