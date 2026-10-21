# Short Analyst

- Symbol: IT
- Elapsed: 170.3s

---
# Forensic Short-Seller Analysis — Gartner, Inc. (NYSE: IT)

**Price context (critical):** $219.64 (20 Oct 2026) vs. all-time high ~$548 (Nov 2024) and cycle low $125.73 (22 Jun 2026). The stock is **+75% off its low and at a 52-week high**. Any short thesis must be judged *here*, not at $500.

---

## 1. Earnings Quality Assessment: **HIGH**

This is not a fraud. On every cash-based test I ran, Gartner passes cleanly — and that matters, because the easy bear case ("AI killed the model, and the numbers are dressed up") is not supported by the accounting.

| Test | 2022 | 2023 | 2024 | 2025 | Verdict |
|---|---|---|---|---|---|
| Accruals ratio | −0.040 | −0.035 | −0.027 | **−0.069** | Negative every year = cash ahead of earnings |
| Op CF / Net income | 1.36x | 1.31x | 1.18x | **1.77x** | Structurally >100% |
| FCF / Net income | 1.23x | 1.19x | 1.10x | **1.61x** | Strong |
| FCF ($M) | 993 | 1,053 | 1,383 | 1,175 | ~18% of revenue |
| Receivables growth vs revenue | +2.9% vs +7.9% | +5.9% vs +6.1% | **−0.7% vs +3.7%** | No channel stuffing |
| Inventory | none | none | none | none | N/A |

Gartner's business model is a **negative-working-capital float**: clients prepay annual subscriptions, so cash arrives before revenue is recognised. This structurally produces negative accruals — the opposite of an earnings-management profile.

**Ratings:** Earnings Quality = High. Fraudulent Risk = Low.

## 2. Beneish M-Score & Accruals

**M-Score = −2.877** (threshold for concern: >−2.22; >−1.78 = likely manipulation). Driving components:
- **DSRI 0.958** — receivables *falling* relative to sales. The single best anti-fraud signal available here.
- **TATA −0.069** — strongly negative total accruals.
- **GMI 1.001** — gross margin flat YoY (no margin-mix games).
- **SGAI 1.026** — mild SG&A bloat (see §4; this is the one soft spot).
- **LVGI 1.142** — **leverage genuinely rising**. The only legitimately negative index.

**Piotroski F-Score = 5/9** (moderate): loses points on ROA deterioration, higher leverage, negative equity change, and no gross-margin improvement. **Altman Z = 2.41 (grey zone)** — but read with care: x1 (working capital/assets) is −0.0007 *only because deferred revenue sits in current liabilities*, and x4 uses book equity of just $320M after ~$6B of buybacks. Both scores are **distorted by capital structure, not by distress**. On an operating basis the company is sound.

## 3. Key Red Flags Found

**(a) Revenue has turned negative — and the automated deceleration screen misses it.** `detect_revenue_deceleration` returns "stable." That is a **false negative**. The raw quarterly YoY series is a near-unbroken slide:

8.1% → 5.4% → 5.7% → 4.2% → 2.7% → 2.2% → **−1.5% → −0.6%**

FY2026 guidance of ≥$6.375B implies a **−1.9% revenue decline** — the first annual decline in over a decade. Any screen relying on "stable" is under-weighting this.

**(b) Contract value (CV) growth has collapsed to ~2%.** Research CV — the leading indicator and the metric the entire bull case rests on — decelerated from 7% (Q1 2025) to 5% (Q2 2025, which triggered a **−27.6% single-day drop**) to **+2% total in Q2 2026 (+3.3% ex-federal)**. Note that CV is a **management-defined, unaudited, non-GAAP metric** — the market values IT off a number no auditor signs off on. That is a legitimate forensic concern in its own right.

**(c) Growth is now being bought with price, not won with value.** Q2 2026 detail: **client count fell from 13,374 to 12,775 (−4.5%)** while **average contract value per enterprise rose to $414,000**. CV growth is being manufactured by raising price on a **shrinking** customer base. That is the classic late-stage signature of a subscription franchise losing relevance — the opposite of a widening moat. It also means reported CV overstates underlying demand by roughly the rate of client attrition.

**(d) Negative operating leverage → then cost cuts.** SG&A/revenue rose from 45.3% (2022) to 47.2% (2025), pushing operating margin from 20.9% (2023) to 15.8% (2025). Management then cut cost: Q1 2026 operating margin 20.9%, Q2 2026 22.6%. Margins are recovering while revenue shrinks — **cost-cutting is masking the top-line problem, and you can only cut once.** A 2027 margin cliff is the obvious follow-on risk.

**(e) Reported EPS is close to uninformative.** Three consecutive years of material items make headline growth an optical illusion: FY2024 net income of $1.254B exceeded operating income of $1.156B (a ~$170M below-the-line gain, visible in Q3 2024: net income $415M vs. operating income $246M); FY2025 was then depressed by a Q3 charge (operating margin 5.7% vs. 16.6% prior year). FY2026 consensus EPS of ~$14.47 is therefore a **base-effect recovery**, up ~50% off a charge-depressed $9.65 — not 50% earnings power growth. Normalised, EPS has compounded in the low single digits since 2024 on a shrinking revenue base.

**(f) Balance sheet fragility.** Total equity **$320M** on $8.09B of assets; **goodwill $3.08B** implies **tangible equity of roughly −$2.8B**. Total debt $3.62B (up $720M in 2025 while $1.99B of stock was repurchased). Gross debt/EBITDA ~2.9x, net ~1.5x — manageable, but with essentially no equity cushion a further 15% EBITDA decline bites hard.

**(g) Capital allocation: the strongest bear point remaining.** ~$6.0B repurchased 2021–2025 (plus $1.99B in 2025 alone, largely between $300 and $450) shrank the share count from 85.0M to 66.5M. Those purchases were executed at 25–35x earnings **into a decelerating core**, funded partly with debt, and now sit roughly 40–60% underwater versus today's $220. This management accurately called the *demand* environment for its clients while systematically misjudging the value of its own equity.

## 4. Competitive Threat Assessment — **the real issue, and it is structural**

- **AI disintermediation is the operative threat.** Reporting on the Aug-2025 and Feb-2026 drawdowns is unambiguous that the market believes syndicated research, benchmark data, and analyst-inquiry hours are being substituted by generative AI — the core inventory of the Research segment.
- **Erosion fingerprints:** gross margin down ~180bp since 2021 (69.5% → 67.7%); SG&A ratio up ~190bp; client count down 4.5%; CV growth at 2%. Pricing power is intact for now (ACV/client rising) but volume is leaking.
- **Federal exposure** is a second, idiosyncratic shock (CV ex-federal +3.3% vs. total +2%). Government consulting cancellations hit an already-thin growth rate.
- **Mitigant:** Gartner retains genuine switching costs (embedded workflow, benchmark datasets, conference network) and 67.7% gross margins. Q2 2026 beat and a guidance raise, plus a 22.6% single-day rally on that print, show the "AI kills Gartner instantly" thesis was over-owned. The structural decline is likely *gradual*, not cliff-edged.

## 5. Management & Governance Red Flags

1. **Active securities class action** (lead-plaintiff deadline 18 May 2026), alleging materially false/misleading statements about business operations and CV growth during the deceleration. Standard post-drawdown litigation, but it directly attacks the credibility of the CV disclosure regime — the metric that anchors valuation.
2. **Serial "one-time" items** in both directions (2024 gains, 2025 charges, 2026 base-effect recovery).
3. **Buyback-driven equity destruction** (§3g) with 100% of FCF returned via repurchase and no dividend.
4. **Promotional-vs-delivery gap** across 2024–25: repeated affirmation of mid-single-digit CV growth followed by 7%→5%→2%.
5. **Insider data — inconclusive.** 25 Form 4s since Jul 2026, **13 filed on a single day (5 Oct 2026)**, a pattern consistent with RSU vesting/tax withholding rather than conviction selling. The feed does not expose buy/sell direction, so I **cannot substantiate net insider selling** — flagging the gap rather than asserting it.

## 6. Short Thesis Summary

**The bear case was excellent — in 2024 and early 2025. It has already been paid out.**

The credible residual bear case at $220:
- Total CV at 2%, clients shrinking 4.5%, revenue guided down ~2%;
- 2026 margins flattered by cost cuts that cannot repeat, setting up a 2027 air pocket;
- AI substitution potentially converting a cyclical CV slowdown into secular decline;
- tangible equity of ≈−$2.8B and rising leverage removing the balance-sheet cushion;
- a 52-week-high entry after a +75% rebound gives no valuation protection on disappointment (Q3 prints 3 Nov 2026; consensus $2.84).

**But the arithmetic does not cooperate with a fresh short:**
- FY2026E EPS ~$14.47 → **~15x**; EV ≈ $16.5B on ~$1.2B FCF → **~14x EV/FCF, ~8% FCF yield**;
- 24.6%+ EBITDA margin guidance, $1.2B+ FCF, 1.5x net leverage — not a solvency story;
- a short into a 52-week high, post-beat-and-raise momentum, with a binary catalyst days away, is a low-quality setup.

**Bear/bull symmetry:** bear path (EBITDA → $1.4B on 9x) ≈ $160 (−27%); bull path (CV reaccelerates to 5%, revenue +3%, EPS $17–18 at 17x) ≈ $290–300 (+35%). Roughly even odds with 8% annual carry cost against you.

**The other side, stated fairly:** the bull case is stronger *than the current price implies*. Cash conversion of 177%, negative accruals, receivables shrinking, zero inventory, a 67.7% gross-margin subscription base, 2% CV growth *and* rising ACV/client, and a Q2 2026 beat-and-raise with adjusted EPS +24% YoY. Gartner's problem is relevance, not integrity — and relevance decays slowly against a 14x FCF multiple.

## 7. Contrarian Rating: **NO EDGE — REJECT SHORT THESIS**

Not because the business is healthy (it isn't — it is a shrinking, price-led franchise with a governance blemish and a real AI question), but because **the mispricing has been harvested**: −72% from peak, two −20%+ air pockets already taken, and the security now trades at ~14x EV/FCF with a 24.6% EBITDA margin and no solvency risk.

**What would reopen a short:** Q3 2026 (3 Nov) showing **total CV growth below 2%**, **client count falling below ~12,500**, or management guiding FY2027 revenue down >3% while margins stop expanding. In that scenario the structural-decline thesis re-prices to ~10x and $150–160 becomes live again. Until then, this is a crowded short at a bad price.

**Data gaps disclosed:** SEC 10-K text retrieval failed ("No 10-K found for IT"); no short-interest, borrow-cost, or peer-multiple data available (no clean listed comparable for syndicated IT research — Forrester is sub-scale, IDC private); insider transaction direction unavailable; several quotes above are drawn from search summaries of earnings coverage rather than the filings themselves.
