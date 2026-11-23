# Alt Data Analyst

- Symbol: MKC
- Elapsed: 28.2s

---
# MKC — Alternative Data Signal Report
**As of:** ~Nov 25, 2026 | **Next print:** Jan 28, 2027 (FQ4'26) | **Price:** $47.40 | **Mkt cap:** $12.75B

---

## 1. Consumer Demand Signals — **Net Negative**

| Keyword (US, 12-mo) | Nov '25 | Apr '26 peak | Current | Read |
|---|---|---|---|---|
| "Cholula hot sauce" | 55–69 | 100 | 47 | **-20 to -25% YoY** |
| "Frank's RedHot" | 24–35 | 100 | 6 | **Severe decay** |
| "McCormick spices" | 43–50 | — | 47 | Flat/seasonal |
| "McCormick" (brand) | 20–21 | 34 | 27 | Flat, slight holiday lift |

This is the most important alt-data finding and it is **not** in the consensus narrative.

- **Cholula**: Genuine YoY deterioration. Spring peak (Cinco de Mayo seasonality) was real, but the off-season baseline has stepped down from ~55–65 to ~47–54. Hot sauce is McCormick's highest-growth, highest-margin flank — a decelerating baseline there argues the "hot sauce growth engine" is maturing.
- **Frank's RedHot**: Readings collapsed from 24–35 to **0–12** and stayed there Jul–Nov. Low absolute search volume means some of the zeros are noise, but the *summer grilling season* (Jun–Aug) reading of 6–12 vs. 31–45 a year earlier is not a seasonal artifact — that's a demand signal. Consistent with management's repeated "volume pressure" commentary.
- **McCormick brand / "spices"**: Flat at ~20 baseline all year. No evidence of brand share gain. Weekly volatility (e.g., the 100 spike on Oct 11) is news/press-driven, not consumer pull — treat as noise.
- **Web traffic**: `mccormick.com` +8.2% MoM (SimilarWeb comparison page); a second source implies +28% MoM in September. Directionally modest-positive, but **low confidence** — I could not obtain a clean monthly time series and the two data points disagree.

**Signal: brand demand is flat at the core and decaying in the faster-growth hot-sauce portfolio.**

## 2. Business Activity Signals — **Neutral / Low Signal**

- **Job postings**: ~141 open roles on LinkedIn. For a 14,100-employee company this is unremarkable — no hiring acceleration. **Cannot establish trend** (no historical series available).
- **Patents**: USPTO PatentsView API **failed** (parse error). No data. One retry, then abandoned — noted as a gap. For a packaged-foods company patent intensity is a weak signal regardless.

## 3. Earnings Preview Signal — **In-Line (mixed composition)**

**Beat history is strong and accelerating:** 71.4% beat rate (5 of 7), avg surprise +5.83%, with the last three quarters at **+11.1%, +15.6%, +13.9%**.

**But the quality of the beat is deteriorating, and the tape has figured it out.** On Oct 1 MKC beat EPS ($0.86 vs $0.755) *and* revenue (+17.4% to $2.02B) and **still fell 4.8%** (45.91 → 43.68). Why:
- Organic sales growth was only **+1.9%** — the 17.4% headline was McCormick de Mexico M&A plus FX. Buy-side wants organic.
- Guidance was **reaffirmed, not raised** — FY26 organic at low end to midpoint of 1–3%.
- Margin expansion came from **price/mix and cost, against volume pressure.**

**Alt-data corroboration:** my brand-demand readings (Cholula down, Frank's down hard, McCormick flat) are *consistent* with ~2% organic — they do **not** support an organic reacceleration. The Jan '27 consensus of $0.77 vs. $0.86 prior-year implies a ~10% YoY EPS decline, which looks conservative enough that another **EPS beat is likely on cost/margin/price** — but an **organic volume miss is the higher-probability surprise.**

**Verdict: EPS modestly Above / organic sales Below.** Net: **In-Line** on the number, with skew to a negative price reaction if organic prints ≤2% again.

## 4. News Sentiment Score and Summary — **+0.20 (mildly positive, low conviction)**

12 articles / 30 days, 3 positive vs 2 negative. Composition matters more than the score:
- **Positive:** Nov 17 quarterly dividend increase announced (reinforces Dividend Aristocrat status, ~4% yield); several "dividend aristocrat on sale" pieces.
- **The dominant story is regulatory, not fundamental:** the **$65B Unilever Foods combination** (Reverse Morris Trust, $15.7B cash to Unilever, close not expected until **mid-2027**). UK CMA Phase 1 found competition concerns in **dry mixes / dry sauces** (Schwartz, Knorr overlap), set a **Nov 18 remedies deadline**, and threatened an in-depth Phase 2 probe; Unilever is offering to sell **Colman's** as a remedy. US FTC has already cleared.
- Negative-keyword flag on the Seeking Alpha piece is a false positive (it's a constructive yield piece).

I could not confirm whether remedies were submitted/accepted by the Nov 18 deadline — **this is the single largest unresolved variable for MKC** and is binary for the equity.

## 5. Social Sentiment — **No usable signal (gap)**

Reddit/StockTwits proxy returned only options chains, quote pages, and estimate pages — zero substantive retail commentary. MKC is a low-retail-beta defensive name, so thin social volume is expected. **Explicit gap; no score assigned.**

## 6. Overall Alt Data Signal: **NEUTRAL (with a bearish tilt on organic demand)**

The alt data splits cleanly, and the split is the insight:

- **Bearish leg:** every consumer pull signal I can measure — Cholula YoY, Frank's RedHot, McCormick brand — is flat-to-decaying. This corroborates the ~2% organic growth and the "volume pressure" language. The market is not mispricing this; it's why the stock is down **~35% from its $72.41 high**.
- **Bullish leg:** earnings execution is genuinely strong (3 straight double-digit beats), margins are expanding, the dividend was just raised, and the stock sits near the low end of its range at ~4% yield — a valuation floor for a defensive name.
- **The dominant variable is exogenous:** the Unilever Foods RMT. Size, timing (mid-2027), integration risk, and CMA remedy conditions will drive the next 12 months far more than spice sell-through. That is a regulatory/event outcome, not something alt data can forecast.

**Scenario framing:** On the Jan 28 print I'd expect an EPS beat with soft organic and a muted-to-negative reaction — a repeat of Oct 1. The setup becomes interesting only if (a) CMA accepts remedies and clears Phase 2 risk, or (b) Cholula/Frank's search trends trough and inflect, which would be the earliest evidence of an organic turn.

## 7. Confidence Level: **MEDIUM**

**Why not High:**
- Google Trends is a proxy for interest, not units; the Frank's series has near-zero absolute volume (0-value readings), so its magnitude is unreliable even though its *direction* is not.
- Web traffic and job postings came from web-search proxies, not API time series — no trend derivable.
- **Patent data unavailable** (API error).
- **Social sentiment unavailable.**
- Google Trends long-window pull returned only ~12 months despite a 2023 request — I could not validate multi-year brand decay, only a one-year step-down.
- **Remedy outcome on the CMA Nov 18 deadline unconfirmed** — material to the thesis.

**What raises confidence:** the consumer demand decay is directionally confirmed by *three independent brand keywords* and independently corroborated by management's own volume-pressure commentary and the stock's 4.8% decline on a genuine double-beat. When alt data and the tape agree on the *reason*, the signal is real.

**Data lag note:** Trends data through ~Nov 15, news through ~Nov 19, prices through Nov 20. There is a ~2-month lead into the Jan 28 print, which is the useful window — but alt data is a leading indicator, not a definitive one.
