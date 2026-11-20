# Alt Data Analyst

- Symbol: AMD
- Elapsed: 39.9s

---
# AMD — Alternative Data Signal Report
**As of:** November 20, 2026 (intraday/close ~$446.23) | **Sector:** Technology / Semiconductors | **Mkt Cap:** ~$733B | **Beta:** 2.49

---

## 1. Consumer Demand Signals

**Google Trends — uniformly decaying across all product queries (YoY comparison is the cleanest read):**

| Query | 12-mo peak | Current (wk of Nov 8) | Year-ago | YoY |
|---|---|---|---|---|
| "AMD Ryzen" (client CPU) | 100 (Apr 12) | 16–17 | 22 | **~−25%** |
| "AMD EPYC" (data center CPU) | 100 (May 24) | 15–20 (12-mo low) | 34 | **~−45%** |
| "AMD MI350" (AI accelerator) | 100 (May 31) | ~4 (below reporting threshold) | 25 | **~−85%** |
| "AMD stock" (retail attention) | 100 (May 3) | **81** | 46 | **+76%** |

**Interpretation:** A sharp bifurcation. *Product* search interest has collapsed from the spring launch cycle (Ryzen refresh, Venice EPYC, MI350 ramp) to 12-month lows, while *ticker* search interest is spiking. That pattern — product demand queries fading while stock queries surge — is characteristic of a momentum/crowded positioning unwind rather than a fundamental demand inflection. Note the Ryzen April spike (22→100 in three weeks) looks launch-driven and mean-reverted hard, so some of the decline is cycle, not deterioration.

**Web traffic (amd.com):** Tool returned no usable SimilarWeb data — **gap, no read.**

**App data:** Not applicable (no material consumer app surface).

## 2. Business Activity Signals

- **Job postings:** Proxy returned static Indeed listing counts (~200–500) with no time series — **no trend extractable.** Qualitatively, listings skew toward Linux/EPYC software enablement and OS-partner engineering, consistent with ecosystem investment, but this is not a quantitative signal.
- **Patent filings:** USPTO PatentsView API **failed twice** (parse error). **No data.**
- **Proxy for capacity/throughput:** Q3 commentary indicates 6th Gen EPYC "Venice" began *revenue* shipments in Q3 with initial OEM systems in Q4, and Helios rack-scale ramp is underway. Supply-chain ramp (not alt-data) is the real business-activity tell here.

## 3. Earnings Preview Signal: **IN-LINE (slight downside skew to the whisper)**

**Last print (Q3 FY26, Nov 3):** Revenue $13.377B vs $13.10B est (**+2.1%**); EPS $2.09 vs $1.95 (**+7.2%**). Revenue **+44.7% YoY**, **+16.2% QoQ**.

**Surprise history:** 7/7 beats, **100% beat rate**, avg **+5.18%**. But magnitude is decelerating: +15.9% → +6.2% → +2.5% → +7.2%.

**The critical tension — consensus now sits ABOVE the guide:**
- Q4 guide: **~$17.0B ±3%** (vs $16.14B pre-guide consensus — a genuine guidance beat)
- Current Q4 consensus: **$17.08B** — i.e., **~$84M above the guide midpoint**
- Q4 EPS consensus: **$2.90** vs $2.09 delivered = **+38.8% QoQ**

The bar has been fully reset to the guide and then some. A 100% historical beat rate and conservative guidance argue for a beat vs. *guide*; but the *whisper* now requires a raise, and decaying search-interest proxies for both EPYC and MI350 do not support an upside surprise of that magnitude. Net: **in-line**, with the risk skewed to a "beat-and-not-raise-enough" negative reaction.

## 4. News Sentiment Score & Summary

**Score: +0.125** (20 articles/14d; 9 positive, 7 negative) — mechanically positive, **but the score is misleading.** The keyword model tags short-report coverage as "positive" because of Cramer/"buy the dip" framing. The true narrative is sharply negative and event-driven:

- **Nov 19:** Hunterbrook Media published a report alleging AMD firmware kept reaching blacklisted Chinese server maker **IEIT Systems**; alleges **>20% of revenue** billed to China/HK customers and dependence on a Chinese partner to finish most chips. Hunterbrook disclosed a short position. AMD called the claims a misrepresentation. Stock **−7.72% to $489.19** on **71.7M shares (~3x avg volume)**.
- **Nov 20:** Extended losses, closing **$446.23 (−8.8%)**. Broader AI-chip contagion: TSMC −4.2% after Taiwan's worst week since 1991; Samsung −6.1%, SK Hynix −5.8%.
- **Live catalyst:** A **December congressional hearing** on China chip exports, plus newly released Commerce records showing 879,000 NVDA/AMD chips approved for China in six months. This is unresolved headline risk.
- **Counterweight:** Oppenheimer upgraded Perform→Outperform with a **$600 PT** on Nov 9 (stock +13.3%); Street average PT **$640–652**; Cramer publicly buying.

**Price/positioning context:** −31% from the Oct 6 ATH close of $649.42; −24% in six sessions off Nov 12 ($585.30). Stock is **+250% YTD vs NVDA +51%** — a crowded, high-beta name where sentiment shocks transmit violently. *(An unexplained single-day −17.3% on Nov 5 at 71M volume remains unresolved in my data — flagging as a gap.)*

## 5. Social Sentiment

**No quantitative read available.** The Reddit/StockTwits proxy returned only stock-quote landing pages (StreetInsider, ADVFN, QuantisNow), not discussion volume or tone. Directionally, ticker-search interest at 81 (vs 46 a year ago) implies **elevated and rising retail attention into a drawdown** — a volatility amplifier, not a directional signal.

## 6. Overall Alt Data Signal: **NEUTRAL** (near-term skew: bearish)

The honest read: **the dominant driver of this stock right now is not observable in my data.** A short-seller report and pending December policy hearing are regulatory/headline events, not demand or hiring trends. What my data *can* say:
- **Bearish:** all three product-demand search proxies at 12-month lows, −25% to −85% YoY; consensus already above guide; extreme crowding (+250% YTD); news flow deteriorating into a live policy catalyst.
- **Bullish:** 100% beat rate over 7 quarters, $17B guide, Street PTs holding firm at $600–652, and an unresolved short thesis the report's own author concedes may not involve a rule violation.

These roughly offset at the fundamental level, hence **Neutral** — but with a clearly negative near-term sentiment and volatility overlay.

## 7. Confidence Level: **LOW**

Explicit gaps that cap conviction:
- **Patent data: unavailable** (API failure, 2 attempts) — no R&D intensity read.
- **Web traffic: unavailable** (proxy returned unrelated domains).
- **Job postings: no time series** — static counts only.
- **Social sentiment: no quantitative data.**
- **Google Trends lags ~12 days** (data ends Nov 8; does **not** capture the Nov 19–20 short-report event).
- Nov 20 volume (21.9M) appears partial-session — do not compare to full-day averages.
- The Q4 print is **Feb 2, 2027** (~10 weeks out); Q4 demand proxies are only partially formed.

**Bottom line:** Alt data does not corroborate the short thesis (which is a policy/compliance claim, not a demand claim), but it also does not support the aggressive +38.8% QoQ EPS step-up in consensus — product search interest is at 12-month lows across client, server, and AI accelerator lines. Treat this as a **headline-driven de-rating inside an intact fundamental uptrend**: the risk is that December's hearing converts a sentiment problem into a revenue problem, which no amount of Q3 momentum would offset. Alt data is a leading indicator, not a definitive one — and in this name, right now, it is a weak indicator relative to the policy calendar.
