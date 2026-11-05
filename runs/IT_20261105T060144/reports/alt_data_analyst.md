# Alt Data Analyst

- Symbol: IT
- Elapsed: 111.0s

---
Both retries failed (Business Wire timeout; Google Trends 429 — second block on that keyword). That's my one retry each. Writing up with what I have.

---

# Alternative Data Signal Report — Gartner, Inc. (NYSE: IT)
**Price $207.19 (2026-11-04) | Mkt cap $13.1B | Next catalyst: Q4'26 print, 2027-02-02**

**Context that frames everything below:** Q3'26 (reported 2026-11-03) was a clean beat — adj EPS $3.59 vs $2.84 est (+26%), revenue $1,504.8M vs $1,486.8M, FY26 guidance *raised*. The stock fell **−13.2% on the day** (235.26 → 204.22). This is the second time in nine months (Feb 3, 2026: −20.9% on a beat). Gartner's EPS no longer sets the price; **contract value (CV) growth does**. Q3 CV was $5.3B, +2.5% YoY FX-neutral, +1.1% QoQ — a third consecutive quarter of acceleration — but management walked back the "4% by year-end" target. Every alt signal must be read against that single number, not against EPS.

## 1. Consumer Demand Signals
Gartner is B2B, so "consumer" here means top-of-funnel research demand and brand engagement.

- **Google Trends, "Gartner" (US, 12m): NEGATIVE, but low signal quality.** Oct-2026 weekly avg **36.5** vs Q2'26 avg **88.4** vs Nov-2025 ~**50**. Current reading **33** — down **~59%** from the June-2026 peak of 100 and **~28%** below year-ago levels. This is the weakest reading in the entire window outside the late-December holiday trough.
  - **Critical caveat:** the series is *negatively* correlated with the stock. Interest peaked at 100 in June 2026 — the exact month IT bottomed at $125.73 — and has collapsed through a +65% rally to $235. That behaviour is characteristic of an **attention/news-cycle proxy** (the Feb-2026 crash, the "does AI make Gartner obsolete" debate, MQ season), not an enterprise-demand proxy. I am **not** treating this as a demand signal; I'm treating it as fading narrative heat.
- **Web traffic, gartner.com: POSITIVE.** **+5.54% MoM**, against a flat peer read (g2.com). Engagement quality is healthy: 2:15 avg visit duration, 2.69 pages/visit, 48.4% bounce. Gartner.com also drew more visits than g2.com over the trailing 3 months. This is the single cleanest positive demand read I have, and it **contradicts** the Trends decline — reinforcing that Trends is noise here.

## 2. Business Activity Signals
- **Job postings: MIXED, slight positive for forward CV.** Posting mix is heavily front-office: Account Executive (LE/GE), Client Success Partner, New Client Engagement, Sales Development Associate, Client Engagement Specialist. Sustained quota-carrying and client-success hiring signals management is investing into the demand recovery rather than cutting — consistent with the retention improvement cited on the call.
  - **One flag:** recurring **Collections Specialist** postings across FL/TX. Late-cycle collections hiring can precede receivables/DSO deterioration. Directional only — I have no posting counts or trend line (search proxy returns existence, not volume).
- **Patents: NO DATA / NOT MATERIAL.** USPTO fetch failed. Gartner is a research-and-advisory business; patent intensity is structurally irrelevant. Excluding this signal rather than treating the gap as a negative.

## 3. Earnings Preview Signal — **IN-LINE (EPS above, revenue in-line, CV the risk)**
Consensus for 2027-02-02: **EPS $3.88, revenue $1,744.0M**. Against Q4'25 actuals ($3.94 / $1,752.6M) that is **−1.5% EPS and −0.5% revenue YoY** — the Street already models a Q4 decline, which is why the guide reaction was so brutal.

- **Beat mechanics strongly favour another EPS beat:** 7/7 beat rate, avg surprise **+13.8%**, and a *rising* sequence of the last three quarters: **+11.0% → +16.2% → +26.4%**. Positive surprise momentum is accelerating, not mean-reverting.
- **But beats do not pay here.** Both of the last two beats were sold (−21% and −13%) on forward CV framing.
- **Alt-data read on CV:** web traffic +5.5% MoM, improved retention, a third straight quarter of CV acceleration and continued sales hiring all support a **steady ~3.0–3.5% YoY exit rate**. Nothing in my data supports the **4%+** reacceleration the stock needs to re-rate. Longer sales cycles and rising costs (per call commentary) are corroborated by the front-loaded sales hiring without matching productivity evidence.

## 4. News Sentiment Score and Summary — **Neutral, tilting negative on framing**
Tool output: score **1.00** (14 positive / 0 negative of 20 articles). **I am discounting this heavily** — it is a keyword artifact. Headlines containing "Stock Crashed," "Stock Sinks," "Downgrade," and "Fourth-Quarter Forecast Disappoints" were scored positive or neutral.

Manual read of the 7–14 day window (Nov 3–4): **genuinely two-sided.**
- *Positive:* beat and raise; third consecutive CV acceleration; retention improved across core research; CEO Gene Hall's demand narrative that enterprises which "handed everyone AI tools" are seeing little payoff and are turning to Gartner; Baron Focused Growth flagged IT as a top Q3 contributor (institutional accumulation).
- *Negative:* implied Q4 guide below Street; CV 2.5% with 4% by YE called unlikely; longer sales cycles; rising costs; at least one analyst downgrade ("no longer bullish," Nov 4).
- Net: the **beat is fully priced and the forward CV deceleration is not resolved.** Coverage skews to "good quarter, bad outlook."

## 5. Social Sentiment — **NO DATA**
Reddit/StockTwits proxy returned only false positives from the literal word "it" — the ticker is unsearchable on retail platforms. Gartner has a structurally thin retail/social footprint (institutional, low-beta 0.95, no meme characteristics). **Materiality is low; I treat this as a non-signal rather than a gap in the thesis.** (One low-quality item: a Benzinga "Power Inflow / +9%" order-flow alert dated the same day the stock closed −13%. I'd disregard it — the headline contradicts the tape.)

## 6. Overall Alt Data Signal: **NEUTRAL**
No alt-data evidence of either a demand inflection or a demand break. The positives (web traffic, retention, sales hiring, accelerating beat magnitude) describe a business **grinding slowly better** — consistent with ~3% CV growth. The negatives (search interest decay, collections hiring, longer sales cycles) are either noisy or second-order. The stock's problem is a **valuation/expectations problem**: consensus already models a Q4 revenue decline, yet the multiple still requires a CV reacceleration my data cannot corroborate.

**Actionable asymmetry:** I'd expect a **Q4 EPS beat** (high confidence, mechanical) with **in-line revenue and CV in the 3.0–3.5% range** — i.e., a third consecutive "beat-and-fade" setup on 2027-02-02. The signal that would change this view is a CV print ≥3.5% with the 4% target reinstated; nothing I see pre-positions for that.

## 7. Confidence Level: **LOW-TO-MEDIUM**
Data quality is the binding constraint, not conviction:
- Google Trends is a **single noisy proxy** here, demonstrably anti-correlated with the stock over 12 months; its 5-year baseline request silently returned the same 12-month window, so I could **not** seasonally adjust. The "Gartner Magic Quadrant" second-keyword cross-check was **rate-limited out (429, twice)** — unvalidated.
- Web traffic is a **single-point MoM estimate** from a search-proxy wrapper, not a SimilarWeb time series — no trend vector.
- Job postings are **qualitative only** — no counts, no YoY comparison.
- **No social data, no patent data, Q4 guidance detail lost** to a Business Wire timeout.
- **Lag:** price/news through 2026-11-04, Trends through 2026-10-25; the next earnings event is ~3 months out, longer than alt-data's useful lead time.

*Alt data is a leading indicator, not a definitive one. Given the thin, partially-degraded feed set, I'd weight this report as a corroborating input to the fundamentals, not a standalone signal.*
