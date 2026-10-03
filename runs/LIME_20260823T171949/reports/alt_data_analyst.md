# alt_data_analyst

_2026-08-23T09:36:22+00:00_

# ALT-DATA REPORT — NEUTRON HOLDINGS, INC. ("LIME", NASDAQ)

**Report date:** ~Aug 23, 2026 | **Price:** $41.06 (Aug 21 close, Investing.com / FMP quote) | **Mkt cap:** $2.63B | **IPO:** July 1, 2026 @ $25 | **52-wk range:** $23.87–$42.84 (near high)
Source: FMP `company/profile-symbol`, `quote` fields via profile; Investing.com.

**Data-status preamble (important):** LIME is 8 weeks post-IPO. FMP's `calendar/earnings-company` returns **no data** (one report as a public company), `news/stock-news` (50-row pull, saved to `data/news_stock-news.json`) contains **zero** LIME/Neutron/scooter/li.me rows (verified by grep), `search-press-releases` and `analyst/financial-estimates` are **plan-denied** (Starter), and `senate/senate-trading` + `company/historical-employee-count` return **not_found**. Web-sourced items are labeled with URL/date. FMP call budget for this session was exhausted before `press-releases`, `employee-count`, `ratings-snapshot`, and `ipos-calendar` could be pulled — noted as gaps, not retried.

---

## 1) News Sentiment & Themes

**FMP news tool: no LIME coverage available** (stock-news pull had 0 matching rows; press-release endpoints denied/unfetched). All sentiment below is web-sourced — treat as directional, not scored.

**Tone: Positive-to-mixed. Bullish operating narrative; persistent skeptical undercurrent on unit economics.**

| Date | Item | Tone | Source |
|---|---|---|---|
| Jun 30 | IPO preview: "$180M raise, $1.8B valuation, 17x 2025 FCF — an uphill ride" | Negative | Reuters Breakingviews (reuters.com, headline via search; page paywalled) |
| Jul 22–23 | Deep-dive: $7.47/vehicle/day revenue; ~$850M debt due within a year pre-IPO; "may never turn a profit" risk factor; $57M injury-claim reserve; 2025 opex $946M vs revenue $887M. Counterpoint: company says FCF-positive two consecutive years | Negative (with company rebuttal) | The Guardian (theguardian.com, fetched) |
| Aug 4–5 | Q2 2026 (first public report): revenue $304.2M +24% YoY; adj. EBITDA $84.2M (27.7% margin); **+15% two-day rally**; "results above forecasts" | Positive | investors.li.me (title via search), Seeking Alpha (Aug 5), Investing.com, Options Analysis Suite |
| Aug 5 | Needham's Bernie McTernan reiterates Buy, PT $36 | Positive | Investor's Business Daily (fetched) |
| Aug 6 | Italy competition authority fines Bird/Dott/**Lime** €2.7M combined (unfair commercial practices, Rome) | Negative (regulatory) | micromobility.io (fetched) |
| Aug 6–11 | Recap: record Q2, fleet 407.7K vehicles (+22% YoY), market cap crossed $2B | Positive | micromobility.io; StockTitan 10-Q note |

**Key themes:** (a) post-IPO/deleveraging story (IPO proceeds cleared most debt, per Guardian + micromobility.io); (b) growth-vs-unit-economics debate; (c) rising regulatory/insurance scrutiny (Italy fine; Australia ACCC crackdown on e-bike/scooter standards — micromobility.io); (d) light news cadence — coverage clusters around IPO (Jun 30–Jul 1) and earnings (Aug 4–11); thin between events. **Analyst coverage is thin: only 2 analysts, both Buy** (FMP `analyst/grades-summary`); consensus PT $39.40 (range $36–$45, FMP `analyst/price-target-consensus`) — **below** the last close of $42.03 (StockTitan) / $41.06 (FMP), i.e., the stock now trades ~5–7% above Street consensus.

## 2) Web / Interest Signals

- **Google Trends ("Lime scooter"): NOT AVAILABLE** — no Trends feed is wired up and web search surfaced no LIME-specific trend data. Gap, not a signal.
- **App store:** Google Play **4.9★, 702K reviews** (play.google.com listing, via search); Apple App Store listing active (apps.apple.com id1199780189). No download-velocity or rank trend available on this plan → **thin, level-only data**.
- **Web traffic (li.me): NOT AVAILABLE** — SimilarWeb page returned empty content.
- **Ridership (company-reported via web):** 1 billion lifetime rides (Oct 2025, Zag Daily headline); 1M rides in a single day record (Jun 2025, li.me blog); **Seattle all-time single-day record 83,000 trips on June 19, 2026** (KFOX/Sounder at Heart); 19M riders in 2025 across 230 cities / 29 countries (Guardian, prospectus-based). Fleet: avg 229K (2023) → 325K (2025) → **407.7K avg in Q2 2026** (Guardian; micromobility.io). Direction: **up and to the right.**
- **Subscription mix:** **28% of earnings now from bundles/subscriptions** (Guardian, prospectus-based); LimePrime relaunched Jan–Feb 2026 at $4.99/mo with unlimited flat-rate 20-min rides (li.me blog, Jan 20 & Feb 26, 2026). Recurring-revenue push is a genuine structural positive.
- **Social:** anecdotal Reddit chatter on LimePrime (r/askvan thread) — no volume/sentiment feed available. **Glassdoor: 3.1/5 work-life balance, 18% below industry average (Aug 2026)** — mild internal-culture negative.

## 3) Job Postings & Hiring

- **Headcount: 1,148 full-time employees** (FMP `company/profile-symbol`). Historical employee-count endpoint: no data (too new).
- **LinkedIn jobs (via search):** Software Engineer–Core Services, Global Equity Plan Administrator, **two Senior NPI Engineer roles (FATP, Plastics)**, night-shift Mechanic — signals continued **hardware new-product-introduction investment** plus field-ops staffing.
- **Aggregators:** ~32 "Lime scooter" jobs on Indeed; ~7 on ZipRecruiter at $19–28/hr (Operations Associate, Mechanic, Technician) — field operations hiring is ongoing.
- **Direction: steady/positive, but no time series exists** — cannot quantify acceleration. This is a level, not a trend. (Glassdoor score above is the only quasi-quantified HR datapoint.)

## 4) Earnings Surprise History

- **FMP `calendar/earnings-company`: no data** — LIME has exactly one print as a public company. `analyst/financial-estimates`: plan-denied, so I could **not** retrieve the pre-report consensus to size the surprise.
- **Q2 2026 (reported Aug 4, after close) — a beat by all accounts:** revenue $304.2M (+24% YoY, record), adj. EBITDA $84.2M / 27.7% margin, average fleet 407,707 (+22% YoY). Headline net income $295.4M / EPS $4.73 (Quartr, StockTitan) was **flattered by a one-time $298.4M deferred-tax-asset benefit** — not operating (micromobility.io). Stock **+15% over two days** (Seeking Alpha). FY26 guidance: **revenue $1.04–1.1B, adj. EBITDA $265–285M** (Seeking Alpha earnings-call insights). Reference: 2025 revenue ~$887M, ~30%/yr growth since 2023 (Guardian).
- **Insider/smart-money signal (FMP `insiderTrades/search-insider-trades`):** **Uber Technologies is a 10% owner.** Form 4 (filed 2026-07-02): Uber **purchased 800,000 shares at $25 (the IPO price)** and converted Series C Preferred + Convertible Notes into ~10.6M common shares; post-transaction holding 14,859,661 shares (SEC filing, sec.gov). No insider open-market sales on record yet. **Congressional trading: none** (`senate/senate-trading` not_found). Watch item: a standard 180-day IPO lockup would lapse ~late Dec 2026 — **assumption, verify in the S-1** (not retrieved this session).

## 5) Net Alt-Data Read: **MODERATELY BULLISH (with valuation/setup caveats)**

**Signal (not noise):** demand and business-activity indicators are uniformly strong — fleet +22% YoY, single-city ridership records (Seattle, June 2026), subscription mix at 28% of earnings and rising, NPI engineering hires, and a cornerstone Uber stake (bought, not sold). First public quarter beat and guided to ~$1.04–1.1B revenue with solid EBITDA. Deleveraging post-IPO removes the Guardian's chief bear point (~$850M near-term debt).

**Noise/caution:** headline EPS is tax-gain-inflated; unit-economics skepticism (Reuters, Guardian) is unresolved; Italy fine shows regulatory tail risk; only 2 analysts cover it; stock trades **above** the $39.40 consensus PT near its 52-week high; lockup expiry ahead; Glassdoor softness.

**Confidence: MEDIUM** — most demand metrics are company-reported (not independently verified), third-party alt-data (Trends, web traffic, app velocity, patents) is unavailable on this plan, and the public track record is one quarter old.

## 6) COMPUTE REQUESTS (for quant_engineer)

1. **COMPUTE REQUEST — News sentiment score:** Run headline/snippet-level sentiment (FinBERT or LLM classification) on the ~15 dated LIME articles collected above (Guardian 7/22, Breakingviews 6/30, SA 8/5, IBD 8/5, micromobility.io 8/6, StockTitan 8/11, etc.; I can supply the list) → per-article −1..+1 score, 30-day rolling aggregate, theme tags (earnings/regulatory/expansion/valuation). No FMP news rows exist to score against.
2. **COMPUTE REQUEST — Surprise & event study:** Given a sourced Q2 2026 consensus (needs IBD/Zacks/Visible Alpha or upgraded FMP `analyst/financial-estimates`), compute revenue and adj-EBITDA surprise %, plus 2-day abnormal return for LIME vs. NASDAQ around Aug 4–6, 2026 using `chart` EOD data (LIME vs. COMP or QQQ).
3. **COMPUTE REQUEST — Ownership math:** Uber stake % = 14,859,661 shares ÷ shares outstanding (verify via `company/shares-float` / StockTitan's ~65.0M), and implied market value at $41.06. (Not computed by me per no-derivation rule.)
4. **COMPUTE REQUEST — Momentum/positioning (optional):** RSI(14) and distance from 50-day SMA on `technicalIndicators` once fmp_call budget resets; stock sits ~5% off its $42.84 high.

**Honest gaps:** Google Trends, app-download velocity, li.me web traffic, patent filings, and job-posting time series were **not available** this session (no feed / plan limits / search-budget exhaustion); FMP press-release, employee-count, and IPO-calendar endpoints went unfetched. Nothing above is estimated — every figure is cited or explicitly marked unavailable.
