# Short Analyst

- Symbol: CBOE
- Elapsed: 93.2s

---
# CBOE Global Markets — Forensic Short-Seller Analysis

**Price $335.53 · Market cap $35.0B · 104.5M diluted shares · Net cash ~$1.11B (Q3'26)**
**Data as of filing dated 2026-10-30; license extension 2026-09-29**

---

## 1. Earnings Quality Assessment: **HIGH**

Every quantitative earnings-quality gate I run is passed. There is no accounting case here.

| Test | Result | Read |
|---|---|---|
| Beneish M-Score | **−2.537** | Below both thresholds (−1.78 / −2.22) → low manipulation risk |
| Accruals ratio (2025) | **−1.33%** of assets | Negative accruals = conservative, four straight years negative |
| Cash conversion (OCF/NI) | **111.3%** | Cash exceeds reported earnings |
| FCF conversion (FCF/NI) | **104.8%** | Quality confirmed at the free-cash-flow line |
| Receivables vs revenue | Revenue +15.1%, **AR −11.4%** | Fastest collections in years — *opposite* of channel stuffing |
| Piotroski F-Score | **7 / 9** | Solid |
| Inventory days | N/A | No inventory — test not applicable |

The four-year accruals series is uniformly negative: −1.33%, −3.33%, −0.42%, −9.05%. A company inflating earnings does not produce a consistently negative accrual book and 111% cash conversion. **Rating: High.**

**One caveat on the composite score:** the Earnings Quality composite returned **52/100** despite its own three inputs being excellent (1.113 cash conversion, 1.048 FCF conversion, −2.63% accruals-to-revenue). The composite is internally inconsistent with its components — I treat the 52 as a model artifact, not a signal, and weight the components, which are unambiguous.

## 2. Key Red Flags Found

Honest list — none of these rise to a short thesis, but they are real:

1. **Peak-cycle operating leverage (the strongest bear point).** Operating margin on net revenue reached **71.7% for 9M26 vs 60.5% for 9M25** — a 1,120bp expansion. Adjusted opex is guided to only **$830–845M** against ~$2.85B of 2026E net revenue. The cost base is ~70% fixed. **Model: a 15% decline in net revenue cuts operating income ~23% and EPS ~25%.** That asymmetry is the only genuine short-side math in this name.
2. **Consensus already assumes the cycle rolls over.** 2027E EPS $15.31 vs FY26E ~$15.2 — **flat**. 2028E $16.83 (+10%). At $335.53 that is **21.9x forward earnings for zero consensus growth.** You are paying a quality multiple for no growth.
3. **Revenue growth is violently lumpy and volatility-linked.** Quarterly YoY: Q1'26 **+6.5%**, Q2'26 **+23.0%**, Q3'26 **+19.0%**. A 16-point swing in one quarter. Volume, not pricing, drives this.
4. **Pricing pressure in the commoditised segment.** Multi-listed options RPC **$0.052 vs $0.054** prior (Sept 2026) — ~4% compression from multi-exchange competition. (Offset: proprietary index options RPC improved.)
5. **Asset turnover deteriorating** (Piotroski F9 fail): revenue/assets **0.507 vs 0.526**; net revenue/assets **0.248 vs 0.266**. Cash grew $1.03B → $2.66B while buybacks collapsed from $225.7M (2024) to $96.5M (2025) to ~$80M 9M26. Capital is accumulating faster than it is deployed.
6. **Goodwill concentration:** $4.22B = **71% of $5.93B equity**. Precedent for it biting: FY2022 revenue *rose* 13% to $3,958M yet operating income collapsed to $490M (12.4% margin) from $806M (23.1%) — a ~$300M+ impairment/charge year. The acquisition book is not mark-proof.

**Flags I investigated and dismissed (do not use these):**
- **FY25 "gross margin compression" (50.6% → 48.9%) is an artifact,** not pricing pressure. SG&A collapsed $603M → $91.5M while cost of revenue rose $2,022M → $2,408M — a ~$511M reclassification between line items that does not touch operating income. Confirmation: 2026 net revenue margin *rebounded* to 51.6% (H1) and 52.4% (Q3). This reclassification also distorts Beneish **SGAI to 0.132**; normalising SGAI to ~1.0 only moves the M-score to **−2.39**, still below the soft threshold. Conclusion holds.
- **Altman Z of 2.619 ("grey zone") is a false positive.** x4 uses *book* equity ($5.1B), not the $35B market cap. On market value, x4 ≈ 6.8x and Z is comfortably in the safe zone. The company holds **$1.11B net cash**. Not a distress signal.
- **The apparent 2026 cash-flow collapse is corrupted data, not a red flag.** Q1'26 OCF +$82M and Q2'26 OCF −$503M against $739M of net income looks alarming, but the Q3'26 row returns literal zeros across every field (null-fill), and cash *rose* $2,253M → $2,663M over 9M26 while paying ~$227M of dividends. The swing traces to a ~$1.7B simultaneous drop in both current assets and current liabilities between Q4'25 and Q1'26 — a balance-sheet reclassification of restricted/clearing balances, not cash burn. **I cannot use this, and neither should anyone else without the 10-Q MD&A.**

## 3. Beneish M-Score and Accruals Analysis

**M-Score −2.537 — Low risk.** Index decomposition:
- **DSRI 0.770** — receivables *falling* relative to revenue. This is the single most important index for a short-seller and it points emphatically bullish on revenue quality. No channel stuffing.
- **TATA −0.0133** — negative total accruals, the cleanest possible reading.
- **AQI 0.766** — asset quality improving, no aggressive capitalisation.
- **GMI 1.034** — marginal gross-margin deterioration, consistent with the multi-list RPC compression (and partly the reclassification noted above).
- **SGI 1.151** — growth itself adds to the score mechanically, not a red flag.
- **SGAI 0.132** — distorted by reclassification; flagged, immaterial to the conclusion.
- **LVGI 0.994** — leverage flat, and net cash positive.

**Accruals:** four consecutive years negative. On a balance-sheet basis the company is *under*-reporting relative to cash, which is the opposite of a manipulation profile. Cash conversion 111.3% clears the >100% quality bar. **Verdict: no earnings manipulation case exists.**

## 4. Competitive Threat Assessment: **Materially de-risked — the moat got stronger, not weaker**

This is the decisive finding. On **2026-09-29** Cboe signed a **25-year extension of exclusive S&P 500 Index options licensing through 2051**. Updated royalty fees begin **2027-01-01**, and management guides the impact as **"de minimis" to 2027 net revenue growth**. The existential bear case — loss of SPX exclusivity at renewal — is now off the table for a generation, and the economics were absorbed without breaking the model.

Residual threats, in order of substance:
- **Single-index, single-licensor concentration.** The crown jewel is one index licensed by one counterparty (S&P DJI) for 25 years. Royalties reset in 2027 and reset again over the term; "de minimis" is a 2027 statement, not a 2051 one.
- **Volatility mean reversion.** The real competitive threat is not a rival exchange, it is a calm market. Index options volumes and 0DTE activity are the growth engine and they are regime-dependent.
- **Regulatory/structural:** potential rule changes to 0DTE or index-option market structure; event-contract competition (Kalshi/Polymarket) — which Cboe is now entering, importing regulatory risk into the growth story.
- **Commoditised multi-list pricing** ($0.052 vs $0.054) — real but confined to the low-margin segment, while mix shifts toward proprietary products.

Gross/net-revenue margin is *expanding*, not contracting. **Moat erosion: not observed.**

## 5. Management & Governance Red Flags: **None substantiated**

- **Insider activity:** 40 Form 4s reviewed. Filings cluster heavily on single dates (11 on 2026-05-18; 8 on 2026-02-23; 7 on 2026-02-17) — the signature of scheduled grants/vesting, not discretionary selling. **Honest gap: metadata does not disclose transaction direction, so net insider buying/selling cannot be quantified.** No unusual pattern is evident.
- **Auditor:** no changes disclosed. **Related-party:** none identified.
- **Capital allocation is the one legitimate criticism.** Divesting Cboe Canada (announced Oct 2025) and Cboe Australia (sold Q3'26), plus the Cboe Digital wind-down, mark a retreat from international and crypto expansion. Meanwhile $2.66B of cash sits idle with buybacks throttled to ~$80M/yr. **The principal identifiable risk to per-share value is a large, expensive acquisition, not fraud.**
- Management language is promotional but has been *matched by delivery*: 2026 organic revenue growth guidance raised twice ("low double-digit to mid-teens" → **"mid to high teens"**), opex guidance *cut* to $830–845M, Q2'26 adj EPS +45%. No guidance-to-delivery gap.

## 6. Short Thesis Summary: Is there a credible bear case?

**The forensic bear case fails outright.** Clean accruals, 111% cash conversion, receivables shrinking while revenue grows, low-risk M-Score, net cash, no governance flags, and — critically — the 25-year SPX license extension removes the only structural thesis worth shorting. On the specific mandate of this analysis (accounting forensics, moat erosion, management behaviour, fraud), the answer is unambiguous: **there is nothing to short.**

**The only survivable bear case is a cyclical/valuation one, and it is not a forensic short:**
- FY26 is a record year: 71.7% operating margin on net revenue, all-time-high volumes, "overall proprietary index options quarterly ADV record of 6.2 million contracts."
- The cost base is fixed; margins are at a cyclical peak that collapses fast on volume normalisation.
- Consensus already models **flat 2027 EPS**, yet the stock carries a **21.9x forward multiple**. You are paying a growth multiple for no growth at peak margins.

**Rough short math:** EPS −25% on a 15% net revenue decline, at 20x = **~$228 (−32%)**. Multiple compression alone to 18x on $15.31 = **~$275 (−18%)**. Both = ~$243 (−28%).
**But the upside is comparable and better-supported:** continued volatility plus re-rating to 26x on $16.83 (2028E) = **~$437 (+30%)**. And the stock has already round-tripped: it fell from $364.92 (May 13) to $230.87 (June 29) — a 37% drawdown driven by a **global tech selloff and lower volatility, not company-specific news** — then recovered to $335.53 after the license extension. **You would be shorting an all-time-high recovery, with raised guidance, a de-risked license, and clean books.**

**The bull case is stronger than the bear case.** Records across every segment, two guidance raises, opex discipline, a 25-year exclusivity lock, net cash, and 105% FCF conversion. The bear case requires a volatility call that the fundamentals currently contradict.

## 7. Contrarian Rating: **NO EDGE — REJECT SHORT THESIS**

This is not a reflexive-bearishness failure; it is the finding. I ran the manipulation models, followed the cash, stress-tested the moat, and read the 8-K. CBOE passes every test I would use to build a short. The 37% June drawdown was beta, not discovery — and the market has already repaired it.

**What I would do:**
- **Do not short CBOE on a fundamental basis.** There is no edge, and the license extension removed the tail risk that made the trade interesting.
- **If forced to express the peak-cycle view,** do it through defined-risk put spreads sized small, timed to a VIX collapse, and never as a naked short into earnings momentum. It is a macro/volatility position, not a forensic one.
- **Watch list for a future short thesis** (none are actionable today): (1) royalty reset language in the 2027 10-K if "de minimis" proves optimistic; (2) a large acquisition funded with the $2.66B cash hoard; (3) another receivables-outpacing-revenue year like 2024 (AR +25.9% vs revenue +8.5%) — the one genuine quality flag in the series; (4) impairment of the $4.22B goodwill book, given the FY2022 precedent.
- **The open data gap to close before any action:** 2026 operating cash flow is unreliable in the feed (Q3 row null-filled, H1 showing a $1.29B working-capital outflow against rising cash). It is almost certainly a clearing/restricted-balance reclassification, but until the 10-Q MD&A is read directly, 2026 cash conversion is unverified — a gap worth acknowledging rather than papering over.

**Rated: No Edge. The bear case does not survive contact with the filings.**
