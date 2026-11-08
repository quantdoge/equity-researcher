# Alt Data Analyst

- Symbol: MCHP
- Elapsed: 56.8s

---
## MCHP — Alternative Data Signal Report
**As of:** Nov 6, 2026 close ($58.35) · **Sector:** Semiconductors (MCU/analog, broadline) · **Mkt cap:** ~$31.7B · **Next print:** Feb 4, 2027 (Q3 FY27)
**Context:** Q2 FY27 reported Nov 5 — rev $1.622B (+42.2% y/y, +9.2% q/q), EPS $0.97 vs $0.94 est. Stock fell **-22.6% in two sessions** (75.34 → 58.35) on Dec-quarter guidance for a slight sequential decline plus a CEO comment calling data center a "bubble."

---

### 1. Consumer Demand Signals
*Materiality caveat: MCHP is a B2B component supplier — no app-store or DTC funnel. These series read **investor/retail attention**, not end demand.*

| Signal | Reading | Direction |
|---|---|---|
| Google Trends "Microchip Technology" (US, 12m) | Peaked 100 (wk of Apr 19, 2026); secondary peaks 97 (May 10), 92 (May 31). Then step-down: Jul 38→28→23; Aug 47→40→28→21; Sep 18–21; Oct 18–21; **Nov 1 = 21** | **Sharply down** — ~79% below peak, at 12-month lows |
| microchip.com web traffic (SimilarWeb public) | **-3.61% m/m** | Flat-to-down (low precision) |
| "microchip shortage" (Google Trends) | Dormant all year, then spike to **100 (wk Oct 25)** and 64 (Nov 1) | **Up** — shortage narrative re-igniting |
| "8-bit microcontroller" (Google Trends) | Zero-filled series, single anomalous print | **Unusable** |

**Interpretation:** Attention has fully normalized/decayed from the April–June euphoria even though the stock made new highs into late October — a classic divergence where price momentum ran ahead of retail interest. The *only* demand-adjacent series moving up is "microchip shortage," which is a **supply** signal, not a demand one.

### 2. Business Activity Signals
- **Hiring (LinkedIn/Indeed proxy):** ~**667 open jobs** on LinkedIn; active reqs in Chandler AZ, Colorado Springs CO, Portland OR — concentrated in **Test/Yield engineering** (parametric test) and engineering planning. No quantitative time series available, so I can confirm **level, not trend**. Cannot validate hiring acceleration. → *Inconclusive.*
- **Patents (USPTO PatentsView):** API failed on two attempts (parse error). → **No patent signal available — gap disclosed.**
- **Supply-chain / lead-time alt data (strongest business-activity read):** Distributor and lead-time trackers show MCU lead times extending hard through 2026 — industry average ~**26 weeks** (Susquehanna LTI), MCU families at **17–19 weeks** and some general-purpose lines pushed toward **52 weeks**, up from 13–14 weeks in Aug 2025. Distributor notices cite **Microchip price adjustments** on inventory/lead-time/pricing stress. → **Up / tightening.**

**Interpretation:** This is the most valuable alt signal here. MCHP's revenue shortfall next quarter is a **capacity/allocation problem, not a demand problem** — management explicitly said supply constraints are delaying shipments of *high-margin* products. Extended lead times plus price increases historically precede 4–6 quarters of pricing and mix benefit.

### 3. Earnings Preview Signal — **In-Line on the quarter; Below on guidance**
- Consensus Feb 4, 2027: **EPS $0.96, rev $1.627B** → implies **-1% EPS** and **+0.3% revenue** q/q vs Q2 actuals. Company guided a *slight sequential decline*; analysts cut estimates/PTs post-print. **Consensus sits at or above the guided midpoint — no cushion.**
- **Surprise-magnitude decay is the key leading indicator.** Seven consecutive beats (100% beat rate, avg +7.39%), but magnitude is rolling over: 5.1% → 13.0% → 5.9% → 2.7% → 12.9% → 8.6% → **3.6%** (latest, and that print *still* missed on guidance by 2.5% on revenue vs the guidance midpoint of $1.604B it did beat... yet guided down). Beat quality is deteriorating while the bar is being set higher.
- Verdict: **headline beat is achievable (supply-deferred revenue plus pricing), but "beat-and-raise" — the pattern of the prior six quarters — is at risk.** Asymmetry has shifted from the EPS line to the guide.

### 4. News Sentiment Score and Summary
- **30-day score: +0.667** (20 articles, 10 pos / 2 neg) · **7-day: +0.636** (14 articles, 9 pos / 2 neg) — both "positive."
- **I flag this score as a false positive.** Keyword counting latches onto "beat," "rise," "growth," "demand recovery" while missing the market's actual read on guidance. A +0.64 sentiment score coexisting with a -22.6% two-day drawdown is a textbook divergence — the model is lagging and structurally blind to guidance tone.
- True tone of the negative cluster: *"Analysts Slash Their Forecasts,"* *"Data Center Market Is in a Bubble,"* *"supply constraints delay shipments of some high-margin products,"* *"Has Other Problems Besides A Data Center Slowdown,"* *"beat its own forecast, yet the stock still got hammered."* Note also the data-center segment is **16.7% of sales but the fastest-growing (+55%)** — the regulatory/political/execution risk sits exactly where the growth is.

### 5. Social Sentiment
- **Stocktwits:** ~**6 mentions/day, down 83% vs three months ago** — "a sign of cooling retail chatter." No retail bid to absorb the drawdown; also no capitulation panic. (Embedded price quotes on that page are stale — ignore.)
- **Reddit:** sparse and contrarian-valuation framed ("one of the cheapest semiconductors"), no organized thesis, no squeeze dynamics.

### 6. Overall Alt Data Signal: **NEUTRAL** (near-term tilt bearish; 2–4 quarter tilt constructive)
- **Bearish weights:** attention collapse (Trends -79%, mentions -83%), guidance miss with no consensus cushion, decaying surprise magnitude, idiosyncratic de-rate.
- **Bullish weights:** lead times extending to 17–26+ weeks with price increases = supply-constrained upcycle and pricing power; Q2 revenue +42% y/y with margins 66.5%; the selloff is **>2x the peer de-rate** (MCHP -22.6% vs **TXN -11.0%** and **NXPI -6.3%** over the same two days), meaning the market is pricing an MCHP-specific guide cut, not a broad demand break.

### 7. Confidence Level: **MEDIUM-LOW**
**Why not higher — data limitations and lag, stated plainly:**
1. **No usable patent data** (API failure twice) and **no quantitative job-posting series** — two of the four core business-activity pillars are missing for a B2B semi where they matter most.
2. **Google Trends on a B2B name measures investor attention, not product demand.** It should be weighted as a sentiment proxy, not a revenue proxy — it was already at 12-month lows in September while the stock rallied 40%, which demonstrates its low predictive value here.
3. **News sentiment model is contradicted by price action** — keyword-based, no guidance awareness; treat as unreliable for this event.
4. **Web traffic is a single public snapshot** (-3.61% m/m), not a monthly series — precision insufficient to call a trend.
5. **The supply-demand tension is unresolved in the data:** extended lead times can mean either (a) pricing power = good, or (b) double-ordering/customer inventory build = bad. Distributor price-increase notices and management's own "high-margin product delay" language favor (a), but lead-time data cannot distinguish them, and this is the single biggest swing factor in the thesis.

**What would change the call:** distributor lead-time direction into December, confirmation that high-margin shipments slip only one quarter, and whether Dec-quarter consensus holds at $1.62B (a cut toward ~$1.55B would flip this to Bearish). Alt data is a leading indicator here, not a verdict — the honest read is that fundamentals are strengthening into a supply-constrained cycle while the near-term estimate setup is exhausted.
