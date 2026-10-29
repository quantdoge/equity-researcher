# Alt Data Analyst

- Symbol: LPLA
- Elapsed: 160.3s

---
## LPL Financial Holdings (LPLA) — Alternative Data Signal Report
**Data through 2026-10-28 | Next catalyst: Q4'26 print, 2027-02-04**

### Company context (why the alt-data set is unusual here)
LPLA is a B2B advisor-mediated platform — >32,000 advisors, ~1,100 financial institutions, $2.6T client assets. So the classic consumer alt-data stack (app downloads, retail web traffic) is a weak fit. The meaningful "demand" signal is **advisor recruitment and asset gathering**, which I proxied via company disclosures, hiring activity, and search interest. Critically, LPLA just printed Q3'26 on 10/27 and fell **-15.2% on 5.2M shares (~5x ADV)** the next day *despite* an EPS beat — a massive distribution event that any alt-data read has to be reconciled against.

---

### 1. Consumer Demand Signals — MIXED, leaning negative

**Google Trends, "LPL Financial" (US, 12-m):** Quarterly average interest has rolled over steadily.

| Period | Avg interest | Change |
|---|---|---|
| Q1'26 | 85.9 | — |
| Q2'26 | 83.1 | -3% |
| Q3'26 | 68.5 | **-18%** |
| Oct'26 MTD | 66.7 | -3% |

Peak = 100 (week of 2026-02-08, around Q4'25 earnings/Commonwealth news). Latest 4 weeks ≈ 65.8 vs prior 4 weeks ≈ 63.3 — **flattening, not falling**, so the deterioration is a 9-month trend that has recently stabilized. Direction: **down ~22% from Feb peak, stabilizing over the last ~6 weeks.**

*Caveat: this series is dominated by investor/news interest, not end-client demand. It partly tracks controversy and earnings events, so a decline is ambiguous — it can mean "less bad news," not "less demand." I weight it accordingly.*

**Web traffic:** Only snippet-level SimilarWeb data was retrievable (no monthly time series). `lplfinancial.lpl.com` showed **+29.4% over 3 months**; `accountview.lpl.com` **+3.35% MoM** with low bounce rate (12.7%) and 5.5 pages/visit — consistent with sticky advisor/client portal usage. Direction: **flat-to-modestly positive**, low confidence.

### 2. Business Activity Signals — NEGATIVE (the core issue)

**Advisor recruitment (the real demand proxy):**
- **Recruited assets $24B in Q3'26, DOWN 26% YoY** — the single most important negative alt/fundamental datapoint. TTM recruited assets $81B.
- Company framing: individual advisor recruiting "largely returned to" normal, with institutional conversions being lumpy/large-deal dependent. Pipeline described as strong, but the *realized* number decelerated hard.
- One secondary source (InvestmentNews) cited "$25B, up 35% YoY" and "pipeline hits new high" — this contradicts the company's own release and appears to be a **stale prior-year article**. I anchor on the official 10/27 release.

**Hiring:** Active, broad-based postings (Wealth Advisor, Business Development Associate, Security Ops Analyst, onboarding roles); ~100+ listings in the Charlotte hub and 132 in South Carolina. **No evidence of a hiring freeze or retrenchment** — steady-state growth investment against 10,081 FTEs. Direction: **neutral/stable**. Limitation: proxy is qualitative search results, not a time-series count — I cannot measure the *trend*.

**Patents:** USPTO feed failed twice (parse error) — **gap, not signal.** Low relevance for a broker-dealer/RIA custodian anyway.

**Product/tech signal (positive, early):** Rollout of proprietary AI agent **"Cyan"** to advisors — a genuine productivity lever for advisor capacity, though unquantified.

### 3. Earnings Preview Signal — **IN-LINE (mechanically above, qualitatively below)**

Consensus for 2027-02-04: **EPS $6.40, revenue $5.461B.**

- **EPS beat rate: 100% (7/7), average surprise +7.83%** — the strongest single stat in the dataset. Last four: +5.5%, +8.4%, +2.2%, +6.3%.
- **But surprise magnitude is compressing** (+15.8% in Q3'25 → +5.5% in Q3'26) as estimates have caught up.
- **Revenue quality deteriorating:** revenue *missed* in Q3 (-0.20%) and Q1'26 (-0.86%); beat in Q2 (+2.98%) and Q4'25 (+4.59%). 5/7 beat overall but the last two quarters split one miss/one beat.
- **Forward headwinds alt data confirms:** client cash $57B = **2.2% of client assets, down from 2.4% a year ago** (flat QoQ) → cash-sweep revenue drag; Commonwealth asset retention guidance **cut to ~83%** (run-rate EBITDA now $415M); Q4 contains the Commonwealth conversion — execution risk.
- **Offsets:** organic NNA $29B / ~5% annualized, the *best quarterly pace in over a year*; advisory assets +16% to $1.6T and 60.9% of total (up from 58.2%); gross profit +12%, core G&A +11% vs revenue +17.4% → positive operating leverage.

Verdict: another headline EPS beat is likely on a 7/7 base rate and cost discipline, but the beat is increasingly **low-quality** — driven by expense control, not organic growth. I'd expect the Q4 print to land in-line-to-slightly-above on EPS with **downward pressure on forward estimates**.

### 4. News Sentiment Score — **+0.60 POSITIVE (but stale; treat as lagging)**

8 articles/14d, 4 positive vs 1 negative; 3-day window +0.50 (6 articles). The positivity is entirely earnings-day recap ("Beats Q3 Earnings Estimates," "Record Adjusted EPS") plus routine advisor-welcome PRs. **This score is computed from headline keywords and structurally cannot capture the Commonwealth retention cut or the -15% price reaction** — the negative narrative broke after these headlines posted. I discount it heavily as a leading indicator. The genuine news narrative is: *"LPL Sinks 13% as Commonwealth Retention Slips to 83% and Recruited Assets Drop 26%."*

### 5. Social Sentiment — **BULLISH but low quality / likely stale**

StockTwits aggregates read **100/100 bullish** (altindex). Retail chatter volume on LPLA is thin and the sample skews to pre-earnings posts ("beaten EPS 8 of last 8 — I'm bullish"). No meaningful Reddit signal surfaced. Given the price collapse on 10/28, this reading is almost certainly **pre-event and not refreshed** — I assign it near-zero weight. Limitation: search-proxy only, no API-level post/volume time series.

### 6. Overall Alt Data Signal: **BEARISH (moderate)**

The forward-looking alt signals point the same way:
- Search interest **-22%** from Feb peak (stabilizing recently)
- **Recruited assets -26% YoY** — the growth engine's intake is slowing
- Commonwealth retention cut to 83%, cash mix at 2.2% vs 2.4%
- Confirmed by tape: **-15.2% on 5x volume**, -24.7% YTD, ~31% below the $393 52-week high

Offsetting positives (genuine, but backward-looking): 100% EPS beat rate, record adjusted EPS $5.97 (+15%), organic NNA at a multi-quarter best ~5%, advisory mix shift improving, Cyan AI rollout, stable hiring. This is a company executing well on a decelerating intake — the market is repricing the *quality* of growth, not the current quarter.

### 7. Confidence Level: **MEDIUM**

Confidence is medium, not high, because the best-quality data here (recruited assets, retention, cash mix) is **company-disclosed, not independent alt data** — it's already in the price. The genuinely independent alt signals are the weakest: Google Trends is an ambiguous proxy for a B2B platform; web traffic is snippet-only with no time series; social sentiment is stale; patent data is unavailable; and the sector-peer tool returned only Vanguard index funds (VITSX/VTI/VFIAX), so **no valid peer comparison was possible**.

**Data gaps:** patent filing trend (2 failed attempts); SimilarWeb monthly visit history; Reddit/StockTwits quantitative time series; peer multiples.

**Bottom line:** Alt data does not support buying the -15% dip on a demand-inflection thesis. The leading indicators — advisor recruitment intake, search interest, cash balances — say growth is slowing into the Commonwealth conversion. Wait for evidence that recruited assets re-accelerate (or a Q4 organic NNA print above ~5%) before treating this as a trough.
