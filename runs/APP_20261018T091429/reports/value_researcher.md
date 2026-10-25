# Value Researcher

- Symbol: APP
- Elapsed: 126.1s

---
I now have enough to build the analysis. The DCF tool returned malformed output (it read WACC as 1200bp), so I built the valuation by hand from reported owner earnings.

---

# AppLovin Corporation (APP) — Value Investment Analysis
**Price: $266.13 | Market cap: ~$89.4B | Net debt: ~$1.06B | EV: ~$90.5B | Date: mid-Oct 2026**

---

## 1. Business Quality Assessment — Moat Rating: **NARROW** (widening operationally, but unproven durability)

AppLovin is now, after the 2025 divestiture of its mobile-gaming studio portfolio, a **pure-play advertising technology company**. Its asset is AXON (rebranded AppLovin Ads in 2026): a machine-learning recommendation engine that bids for ad inventory across ~1bn+ daily mobile users, predominantly inside mobile games, and matches it against advertiser demand — increasingly e-commerce/DTC brands, not just game publishers.

**Evidence of a real moat:**
- **Cost/scale advantage in a two-sided auction.** More advertisers → better yield per impression → more publishers → more inventory. This is a genuine network effect, though a *local* one (it does not extend to social or search).
- **Extraordinary capital efficiency.** FY25 ROIC of **73%** (up from 41% in FY24, 17% in FY23) against a ~12% cost of capital. Capex is essentially nil ($28M in FY25 on $5.5B of revenue). This is software-margin economics on an ad-network revenue base.
- **Margin expansion is real and steep.** Gross margin 55.4% (2022) → 80.6% (2023) → 83.9% (2024) → **87.9% (2025)**; Q2'26 gross margin 88.3%, adjusted EBITDA margin **83.9%**, net margin 65.8%. Very few businesses in any industry earn 84% EBITDA margins.
- **Switching costs are moderate for publishers** (MAX mediation integration) but **low for advertisers** — a budget can be moved in a day. That asymmetry is the core weakness of the moat.

**Evidence the moat is not "Wide":**
- **Growth is a function of model iteration, not recurring contracts.** In Q2'26 the company missed its own guidance because "AXON model improvements moved slower than projected" during an architecture upgrade. A business whose growth rate can be set back by one quarter's model-training cadence does not have the predictability of a classic wide-moat franchise. Q2'26 revenue of $1.924B (+53% y/y, +4.4% q/q) was ~$20M below consensus; Q3'26 guidance of ~$2.07B also came in light.
- **Competitive intensity is the highest in the world.** AXON must out-predict Meta Advantage+, Google, Amazon and TikTok for conversion credit. These are vastly larger companies with first-party data that AppLovin does not have. Its edge is narrower inventory (mobile games) and a cheaper auction — not proprietary demand data.
- **Revenue quality is contested.** 2025–26 short-seller reports (Muddy Waters, Culper, and a January 2026 report) alleged attribution/ad-stacking improprieties and, in one case, money laundering; the SEC reportedly opened a probe (Oct 2025) into data-collection and ad-targeting practices. Management denies wrongdoing. I cannot independently verify the allegations — but in a business where the product *is* measurement, even an unproven allegation of measurement inflation is a genuine threat to the moat, because advertiser trust is the asset.

**Verdict on moat:** Narrow, and *directionally widening* on economics (margins, ROIC) while *directionally unproven* on durability. This is a superb business model with a single point of failure: continued algorithmic superiority.

---

## 2. Financial Quality Score: **9 / 10**

| Metric | FY2023 | FY2024 | FY2025 | TTM (Q3'25–Q2'26) |
|---|---|---|---|---|
| Revenue | $1.84B | $3.22B | $5.48B | **$6.83B** |
| Gross margin | 80.6% | 83.9% | 87.9% | ~88% |
| Operating margin | 41.9% | 59.3% | 75.8% | **77.4%** |
| Net income | $357M | $1.58B | $3.33B | **$4.41B** |
| FCF | $1.06B | $2.09B | $3.94B | **$4.50B** |
| ROIC | 17.4% | 41.1% | **73.1%** | n/a |
| Diluted shares | 362.6M | 347.8M | 342.0M | 337.9M |

- **FCF conversion:** TTM FCF $4.50B vs. net income $4.41B = **102%**. Excellent (>80% threshold). Note Q2'26 FCF of $869M was depressed by a $490M working-capital outflow (receivables growing with revenue) — a timing issue, not an earnings-quality one, but one to monitor.
- **Balance sheet:** cash $2.49B vs. debt $3.54B → net debt $1.06B, or **0.2x EBITDA**. Effectively net-cash. Interest cost $51M/quarter on ~$3.5B of debt is a legacy low-coupon structure.
- **Owner earnings:** TTM net income + D&A − maintenance capex ≈ **$4.52B**. Subtracting real stock-based comp (~$282M) gives true economic earnings of **~$4.23B** — an economic earnings yield of **4.7%**.
- **Deduction (why not 10/10):** revenue is concentrated in a single, competitively violent category; the company divested its counter-cyclical gaming annuity, which increased both margin *and* variance; and SBC plus heavy buybacks at high prices dilute the quality of per-share compounding.

---

## 3. Valuation Analysis

**Multiples at $266.13:**

| Metric | APP | Comment |
|---|---|---|
| P/E (FY25 EPS $9.75) | 27.3x | |
| P/E (TTM EPS $13.01) | **20.5x** | |
| P/E (FY26E EPS ~$15.1) | **~17.6x** | Q1 $3.56 + Q2 $3.76 + Q3E $4.04 + Q4E ~$3.75 |
| EV/EBITDA (TTM $5.55B) | 16.3x | FY26E EBITDA ~$6.7B → **13.5x** |
| FCF yield (TTM) | **5.0%** | |
| Sector-peer median P/E | 43.7x | Peer set is mega-cap semis/software — not a true comp; use directionally only |

**Intrinsic value (my own DCF, base = $4.52B owner earnings, WACC 12.5%, terminal 3%):**

| Scenario | Yrs 1–5 growth | Yrs 6–10 growth | Value/share |
|---|---|---|---|
| Bear (ad-tech commoditizes) | 8% | 3% | **~$175** |
| Conservative | 15% | 5% | **~$240** |
| **Central** | **22%** | **8%** | **~$347** |
| Optimistic (e-comm scales) | 30% | 12% | **~$470** |

Cross-check via owner-earnings multiple: $4.23B economic earnings at 30–35x (justified only if 15–20% growth persists a decade) = $127–148B = **$376–438/share**; at a defensive 22x = $275.

**What the current price implies:** $266 requires roughly **15% FCF growth for five years, then ~7%** — versus FY26E revenue growth of ~47% and Q3'26 guided sequential growth of +7.6%. The market is pricing a sharp, near-term deceleration.

**Fair value estimate: ~$345 (range $240–$440).** At $266 the stock trades at a **~23% discount**. That is inside, but at the very bottom edge of, my 20–30% margin-of-safety requirement — and given this is a business whose growth rate missed guidance last quarter because of a *model-training schedule*, I require the full 30%. **Buy threshold: ~$242.**

---

## 4. Management Quality Assessment — **Good, with one material asterisk**

- **Owner-operator:** CEO Adam Foroughi is a founder with a large personal stake; the team is lean (887 employees generating $6.8B of revenue — ~$7.7M revenue per head). Capital-light, founder-led, high-agency culture. Positive.
- **Capital allocation:** Debt is modest and legacy. No dividend — appropriate, since at 73% ROIC every dollar retained beats a distribution. **However:** $2.19B of buybacks in 2025 and $1.53B in H1'26 were executed at average prices far above today's $266 (the stock peaked at $733 in Dec 2025). Diluted shares only fell from 362.6M to 337.9M over three years — i.e., buybacks largely offset SBC rather than creating value. Aggressive repurchase at 40–50x earnings is a **capital-allocation error** and a mark against discipline.

**Disclosure/transparency: a negative.** Divesting the gaming segment, opening self-serve, and the AXON "model pause" were all communicated with limited forward visibility. Combined with the SEC data-practice probe and repeated short-seller attention, I apply a governance discount. Management has been candid about the Q2 miss, which counts in its favor.

---

## 5. Investment Verdict: **HOLD** (accumulate below ~$242)

This is a genuinely exceptional economic machine — 88% gross margins, 77% operating margins, 73% ROIC, 100%+ FCF conversion, near-net-cash — trading at 17.6x forward earnings and a 5% FCF yield. On the numbers alone that is cheap.

But two things keep me from buying at $266:

1. **The moat is not yet proven across a cycle.** Growth is contingent on out-innovating Meta, Google, Amazon and TikTok in machine learning quarter after quarter. The Q2'26 miss showed how thin the margin for algorithmic error is. Widening margins are not the same as a widening moat.
2. **The margin of safety is 23%, not 30%.** For a 2.56-beta, single-product, litigation-overhung business, 30% is the right bar. That bar is $242.

**Hold.** If the SEC matter resolves without enforcement action, or if the price reaches ~$240–250 (roughly 15x forward earnings with a 5.6% FCF yield), this becomes a **Buy**. I would size it modestly — no more than 3–4% of a portfolio — because the failure mode is a step-change in advertiser trust, not a slow fade.

---

## 6. Key Risks to the Value Thesis

1. **Revenue quality / attribution integrity (highest severity).** An SEC probe into data-collection and ad-targeting practices, plus short-seller allegations of measurement and ad-stacking improprieties. If any are substantiated, advertiser trust — the entire asset — erodes quickly. Unverifiable from public data; treat as binary-ish tail risk.
2. **Model-decay risk.** AXON's advantage is empirical, not structural. A single quarter of slower model improvement already cost 20% of the share price. A *durable* slowdown in model ROI would collapse both growth and the 84% EBITDA margin.
3. **Competitive encroachment.** Meta Advantage+, Google PMax and Amazon have first-party purchase data AppLovin lacks; TikTok Shop is attacking the same DTC budget. AppLovin's inventory is largely third-party mobile-game supply — a narrower and lower-intent pool.
4. **Growth deceleration already visible.** Y/Y growth: +70% (FY25) → +59% (Q1'26) → +53% (Q2'26) → ~+47% guided (Q3'26). Sequential growth has slowed to +4.4%. The multiple compressed for a reason; extrapolating 2024–25 growth would be a mistake.
5. **E-commerce execution.** Self-serve opened to all advertisers only in June 2026; e-commerce is modeled at ~$1.45B for 2026. This is the entire incremental growth story and it is early, unproven, and being tested by mid-market brands with low switching costs.
6. **Capital allocation at peak multiples.** Continued buybacks at 40x+ would destroy value if growth mean-reverts; compute investment (~$0.10 per incremental revenue dollar) may pressure the 84% margin structure.
7. **Platform dependency.** Apple ATT/privacy changes and Android/DMA rules can impair targeting without warning — the 2022 revenue decline (-34.6% in 2023) was exactly this.
8. **Extreme volatility.** Beta 2.56; four separate >15% single-day drawdowns in the past 18 months. Position sizing must reflect this.

**Honest caveats on data:** the DCF tool returned malformed output (WACC mis-parsed), so all intrinsic values are hand-built from reported owner earnings; the sector-peer comparison returns mega-cap semiconductors rather than ad-tech comps, so I have relied on my own multiple work and the analyst target range ($325–$560, median ~$425, all recently cut). No dividend history is relevant — the company pays none.
