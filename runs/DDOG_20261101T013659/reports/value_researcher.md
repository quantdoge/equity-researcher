# Value Researcher

- Symbol: DDOG
- Elapsed: 51.2s

---
I have sufficient data. One note: the bundled DCF tool mis-parsed my discount rate (returned WACC = 1000%), so I've built the valuation by hand below.

---

# Datadog (DDOG) — Value Investment Analysis

**Price $235.27 (30-Oct-2026) | Market cap $85.5B | EV ≈ $82.6B | FY26E revenue $4.45–4.47B**

---

## 1. Business Quality Assessment — Moat: **Narrow, widening**

Datadog is a genuinely good business. The evidence for a moat is real:

- **80% gross margin**, stable for five straight years (77.2% → 80.0%). That is the signature of software with pricing power, not commodity infrastructure.
- **Switching costs are high.** Instrumentation is embedded in customer code and CI/CD pipelines across dozens of hosts, services and 20+ product modules. Ripping it out is a multi-quarter engineering project — which is why land-and-expand works so well.
- **Multi-product cross-sell engine.** ~4,720 customers at $100k+ ARR, up 23% YoY — growth in large customers *accelerating* even as total revenue grew 36%. Sixth consecutive year as a Leader in Gartner's Observability MQ.
- **Growth is durable, not promotional.** 2021→2026E revenue CAGR ≈ 34% (FY26 guided to $4.45–4.47B, +30%). No evidence of buying growth via discounting — gross margin would show it.

**But the moat is not Wide, and here is why:**

- **Hyperscaler adjacency is a structural threat.** AWS CloudWatch, Azure Monitor and Google Cloud Observability are "free" bundled defaults that get better every year. Datadog wins on breadth and UX, but it prices at a premium into an environment where the platform owner can subsidize the substitute.
- **No network effect in the classic sense.** Data network effects exist within a customer's own telemetry; they do not compound across customers the way a payments network or marketplace does.
- **The cost of the moat is being paid by shareholders, not customers.** This is the crux of the whole analysis; see below.

**Moat trend: widening** (product breadth, security attach, AI-observability positioning). I'd call it a Narrow moat on its way to Wide — probably 5–7 years from earning that adjective.

---

## 2. Financial Quality Score: **6 / 10**

Good growth and gross margin; poor capital returns and heavy shareholder dilution. The gap between headline and economic profitability is enormous.

| Metric | FY2023 | FY2024 | FY2025 | Q2-26 |
|---|---|---|---|---|
| Revenue | $2.13B | $2.68B | $3.43B | $1.12B (+36%) |
| Gross margin | 80.7% | 80.8% | 80.0% | ~80% |
| GAAP operating margin | **-1.6%** | 2.0% | **-1.3%** | **0.0%** |
| Non-GAAP operating margin | — | — | ~22% | 23% |
| **SBC ($M)** | **482** | **570** | **751** | **220/qtr (~$880/yr)** |
| SBC as % of revenue | 22.7% | 21.2% | 21.9% | **~20%** |
| Reported FCF | $632M | $836M | $1,001M | $279M |
| **FCF ex-SBC (economic)** | **$150M** | **$266M** | **$250M** | **~$59M** |
| Owner earnings (NI + D&A – capex) | $65M | $204M | $114M | — |

**Key conclusions:**

1. **ROIC is ~0%.** The tool's ROIC: -2.6% (2022), -1.1% (2023), 1.2% (2024), -0.8% (2025). ROE 2.9%. This is the single most damning fact for a Buffett-style buyer. A business earning its cost of capital *only if you pretend 20% of revenue isn't compensation* does not have a demonstrated economic moat in the financial statements yet.
2. **FCF is an illusion of ~80%.** FY2025 FCF of $1.0B drops to ~$250M once SBC is treated as the real expense it is. FCF/NI conversion looks fantastic only because NI is depressed by SBC — a circularity, not a quality signal.
3. **Cash taxes flatter everything.** Cumulative retained earnings are still only $138M after 16 years; accumulated NOLs are suppressing cash tax to near zero. As NOLs exhaust, FCF takes a second haircut.
4. **Balance sheet is a genuine strength.** $5.0B cash & securities vs ~$1.5B debt (convertibles) → net cash +$3.5B. No solvency risk whatsoever; the company can self-fund.
5. **Dilution: ~4%/yr.** Diluted shares 363.5M (2025) → ~378M guided for Q3-26. Every year shareholders own ~4% less of the company.

---

## 3. Valuation Analysis — intrinsic value ≈ **$100–140/share**

The market is paying for a business Datadog has not yet become. I built the DCF by hand (the bundled tool mangles the discount rate).

**Base case — disciplined owner-earnings model:**
- Revenue: $4.46B (2026E) → 25% CAGR for 5 yrs → $13.6B (2031) → 15% for 3 yrs → $20.7B (2034)
- Owner-earnings margin: 20% today (non-GAAP) less 20% SBC ≈ **3%** → normalizes to **25%** by 2034 (SBC falls to ~5% of revenue; GAAP margin converges on non-GAAP)
- 2034 owner earnings ≈ **$5.2B** — i.e., ~48x today's economic earnings, eight years out
- Discount 10%, terminal growth 3%: TV = $76.5B, PV of TV $35.7B + PV of interim FCFs ~$3B → **EV ≈ $38B ≈ $100/share**

**Generous case** (9% discount, 4% terminal growth, same cash flows): **≈ $143/share.**

**Reverse DCF — what the price requires:** to justify a $82.6B EV at a 10% hurdle, Datadog needs roughly **$10B of owner earnings by ~2033**, implying ~$33B of revenue (7.4x today) at a 30% margin — a ~40%+ revenue CAGR sustained for seven years *with* SBC collapsing to single digits. The current $235 price is discounting that at a **~7% required return**, i.e., equity risk priced like investment-grade credit.

**Multiple check (all vs. a peer median P/E of 41.8x):**

| Metric | DDOG | Comment |
|---|---|---|
| P/E (GAAP) | **784x** | 1,778% premium to peers |
| EV/EBITDA | **426x** | |
| P/FCF (reported) | **85x** | |
| P/owner earnings (FCF ex-SBC) | **~330x** | 0.30% yield |
| EV/Sales (FY26E) | **~18.5x** | Peer software ~5–7x |
| P/B | 22.9x | |

**Verdict on price: the stock trades at 1.7–2.4x my estimate of intrinsic value. There is no margin of safety — there is a margin of *danger*.** To be clear about the discipline: I would need ~$95–115/share to buy a 20–30% discount to the generous case.

*Caveat: the price data feed had an internal inconsistency (a segment ending Feb-2026 at $115.66 vs. the $235.27 current quote, confirmed against Oct-2026 prints of $235–293). I used $235.27, which reconciles with the stated market cap and share count.*

---

## 4. Management Quality Assessment — **7 / 10**

**Positives:**
- **Founder-led and technical.** Olivier Pomel (CEO) and Alexis Lê-Quôc (CTO) co-founded the company in 2010 and both still run it. Owner-operator temperament; the product roadmap (Bits AI, AI Guard, agentic observability) shows genuine technical conviction rather than financial engineering.
- **Capital allocation is conservative.** No debt-funded acquisitions, no buybacks at 85x FCF (a blessing), no dividend. M&amp;A is small tuck-in technology (Adaptive ML, RL-ops) — capability acquisition, not empire building.
- **Under-promise, over-deliver.** Q1-26 beat by 31% on the print (+31.3% stock move), Q2-26 beat and raised. Guidance is consistently conservative.

**Negatives:**
- **SBC of ~20% of revenue is the defining capital allocation decision**, and it is a transfer of ~$880M/yr of shareholder value to employees. Yes, this is how you retain elite engineers against hyperscaler comp — but it means "profitability" is a choice management has not yet made, and shareholders have no evidence management *will* make it.
- **No buyback, no dividend, no capital return** — entirely defensible at this valuation, but the shareholder has no cash-return floor under the price.
- Insider ownership is meaningful but not dominant; founders are not control shareholders.

---

## 5. Investment Verdict: **SELL** (Do not initiate; trim existing positions)

This is the hardest kind of call in value investing: **an excellent business at an indefensible price.**

Datadog passes the qualitative moat test — 80% gross margins, high switching costs, multi-product land-and-expand, 36% growth at $4.5B of scale, net cash, founder-led. It fails the *entire rest* of the Buffett checklist:

1. **ROIC ≈ 0%.** The single non-negotiable test for a moated business is failing on a GAAP-honest basis.
2. **Owner earnings yield of 0.30%** against a 10-year Treasury near 4%. You are receiving ~1/13th of the risk-free rate to own equity risk.
3. **No margin of safety** — the opposite: intrinsic value ≈ $100–140 vs. $235.
4. **Price implies a ~7% required return**, meaning you are being paid roughly nothing above the risk-free rate for a business that must compound 40%/yr for seven years to earn it back.

The stock has already shown what happens when expectations reset: **-19% in a single session on 6-Aug-2026 despite a beat-and-raise**, and -17% again after Q2. When a stock falls double digits on *good* news, expectations are the entire asset. The Feb-2026 low of $106 is a plausible reminder of what a 20x sales multiple looks like at 15x sales.

**Verdict scale: Strong Buy / Buy / Hold / Sell / Strong Sell → SELL.** Not "Strong Sell" only because the franchise is real and the balance sheet is fortress-like. I would become a **Buyer below ~$110/share** (roughly 12x FY27E sales, ~a 25% discount to my generous-case intrinsic value) and a **Strong Buyer below ~$85**.

---

## 6. Key Risks to the Value Thesis

**Risks to owning it (why the price can fall further):**
1. **Growth deceleration.** At 18.5x sales, a move from 36% to 22% growth compresses multiples violently. Q3-26 guide of $1.135–1.145B implies only ~28% growth — the deceleration has already begun.
2. **SBC never normalizes.** If SBC stays at 20% of revenue, owner earnings never arrive and the 330x multiple never compresses through earnings growth alone.
3. **Hyperscaler bundling.** AWS/Azure/GCP improving native observability is a permanent, subsidized competitor; AI-driven cost optimization by customers (the original Feb-2025 warning) remains a recurring risk.
4. **AI-native disruption.** If observability gets absorbed into LLM-agent platforms, the instrumentation moat erodes faster than expected. Datadog is spending heavily (Adaptive ML) to pre-empt this — an admission the risk is real.
5. **Cash tax normalization.** NOL exhaustion turns ~$250M of economic FCF into conspicuously less.
6. **Multiple compression without any fundamental deterioration** — the most likely path to a permanent loss of capital here.

**Risks to my bear case (what would make me wrong):**
- If Datadog sustains 35%+ growth through 2030 *and* SBC falls to ~8% of revenue (GAAP margins of 20%+), the generous case moves toward $200+/share and today's price becomes merely expensive rather than absurd. Watch **GAAP operating margin** and **SBC/revenue** — those two lines, not revenue growth, are what determine whether this becomes a great business or an expensive one.
- A dramatic decline in the discount rate would also re-rate it, but that is speculation, not investment.

**What I would monitor before revisiting:** (a) GAAP operating margin sustainably above 10%; (b) SBC/revenue below 12%; (c) price below $130. Until at least two of those three hold, this is a wonderful company I am content to admire from a distance.
