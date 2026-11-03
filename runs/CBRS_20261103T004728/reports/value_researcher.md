# Value Researcher

- Symbol: CBRS
- Elapsed: 38.7s

---
I now have what I need. Two data inconsistencies are worth flagging up front, and I'll use the audited quarterly statements as the authoritative source.

# Cerebras Systems (CBRS) — Value Investment Analysis
**Price: $96.36 (Nov 2, 2026) · Market cap ≈ $21.8B · Net cash ≈ $6.0–7.1B · EV ≈ $15.8B**

---

## 1. Business Quality Assessment — **Moat Rating: None (trending toward Narrow only if margins recover)**

Cerebras builds wafer-scale AI chips (the WSE fills an entire silicon wafer, rather than being diced) plus rack-scale systems and a software compiler stack. It sells to hyperscalers, frontier labs, sovereign AI programs, and enterprises. It IPO'd May 14, 2026 at $185, opened at $350, and closed its first day at $311.

**The technology is genuinely differentiated.** A wafer-scale engine with on-chip memory bandwidth that GPUs cannot match for large-model inference is a real engineering achievement, protected by a decade of development and a deep patent/IP position. That is a legitimate *candidate* moat.

**But the financial evidence does not support a moat claim:**

- **Gross margin is the tell.** FY2025 gross margin was 39% (down from 42% in 2024). In Q1 2026 it was 44.6% — then **collapsed to 14.2% in Q2 2026** (gross profit $25.6M on $180.1M revenue). A business with pricing power does not earn 14% gross margins in a quarter where revenue was $180M. Either the mix is shifting toward low-margin pass-through systems, or pricing is being competed away. Nvidia earns roughly 70–75% gross margin on data center. This gap *is* the moat gap.
- **Customer concentration is extreme.** Two UAE-affiliated customers — G42 and MBZUAI — accounted for ~86% of 2025 revenue (G42 alone was 87% of H1 2024 revenue). That is not a moat; it is a dependency. A single sovereign counterparty's procurement decision can halve the business.
- **Sequential revenue declined.** Q1 2026 $193.4M → Q2 2026 $180.1M. For a company priced at >20x sales, a sequential decline in the first two quarters as a public company undermines the growth narrative that supports the valuation.
- **The competitive moat belongs to the other side.** Nvidia's CUDA software ecosystem, not Cerebras's hardware, is where switching costs actually live. Reports in October 2026 that OpenAI elected Nvidia chips sent the stock down ~20% in a week — the market is correctly pricing the possibility that Cerebras is a *second source*, and second sources have no pricing power. That is precisely the 14% gross margin.

Moat verdict: **None**, with a Narrow rating earnable only if gross margin returns above 40% and concentration falls below ~30%.

---

## 2. Financial Quality Score — **2 / 10**

| Metric | 2022 | 2023 | 2024 | 2025 | Q2 2026 (ann.) |
|---|---|---|---|---|---|
| Revenue | $24.6M | $78.7M | $290.3M | $510.0M | ~$720M |
| YoY growth | — | +220% | +269% | +76% | +74% |
| Gross margin | 11.7% | 33.5% | 42.3% | 39.0% | **14.2%** |
| Operating income | -$178.8M | -$133.9M | -$101.6M | **-$145.3M** | -$477M (Q2) |
| Free cash flow | -$174.9M | -$85.6M | +$428.5M* | **-$392.8M** | negative |
| Owner earnings | -$176.2M | -$123.2M | -$493.5M | **-$110.5M** | negative |

*2024's positive FCF is an artifact: +$443M of working capital inflow (customer prepayments) against a -$482M net loss. Not operating cash generation.

**Critical accounting caveat:** FY2025 net income of **+$237.8M** is *not* a profit. Operating income was **-$145.3M**; the positive net figure comes from ~$390M of non-operating fair-value gains (warrant/derivative re-marks around the IPO). Similarly, the -$482M 2024 net loss was inflated by fair-value losses. **Neither year's net income is economically meaningful.** Ignore the reported 235x P/E — the denominator is not earnings. Properly measured, owner earnings have been negative in all four years.

**Cash conversion is poor:** FCF/net income is meaningless here; on an owner-earnings basis the business consumed ~$110M in 2025 and its capex is running at 75% of revenue ($382.7M in 2025) because it builds its own inference data centers. That converts a capital-light chip story into a capital-intensive compute-hosting story.

**Balance sheet — the one genuine strength.** Post-IPO, at June 30, 2026: cash and short-term investments **$8.61B**, total debt **$1.49B** ($824M of it short-term), equity **$9.15B**. Net cash of roughly **$6–7B**. This gives a multi-year runway and removes solvency risk. Accumulated deficit is -$1.37B.

**Score: 2/10** — one point for real, verified hyper-growth; one point for the fortress cash position. Zero for margins, FCF, capital intensity, or earnings quality.

---

## 3. Valuation Analysis

**Multiples (at $96.36, ~226.5M shares):**
- EV / FY2025 revenue: 15.8 / 0.51 = **31x**
- EV / annualized Q2 2026 revenue (~$720M): **~22x**
- EV / FY2026E revenue (~$770M): **~21x**
- Peer median P/E 37.7x vs CBRS's (meaningless) 235x — and on EV/sales, established semiconductor peers trade at 5–12x
- FCF yield: **negative**
- Dividend: none. Buybacks: immaterial ($38M in 2025).

**Reverse DCF — what does $15.8B of EV require?**
Discounting at 10% over ten years with a 20x terminal multiple, an investor today needs roughly **$2.0B of year-10 free cash flow** to justify the price. At a generous 25% steady-state FCF margin, that means **~$8B of revenue by 2036** — an 11x increase, or a **~27% revenue CAGR for a full decade**, with margins well above anything Cerebras has ever posted. That is not impossible given a reported $24.6B backlog (including a $10B OpenAI agreement through 2028), but the backlog is largely contingent/non-binding and its largest piece is now in question.

**Scenario-weighted intrinsic value:**

| Scenario | Prob. | 2031 revenue | FCF margin | Multiple | Value/Share |
|---|---|---|---|---|---|
| Bull — becomes #2 inference platform | 30% | $5.0B | 20% | 25x | ~$114 |
| Base — solid niche, pricing pressure | 45% | $3.0B | 15% | 20x | ~$49 |
| Bear — Nvidia/second source, stalls | 25% | $1.0B | 5% | 3x sales | ~$26 |

**Probability-weighted intrinsic value ≈ $63/share.** Adding the $6B net cash at full value.

**Verdict on price: ~$96 is roughly 50% above my central intrinsic value, and ~2x my margin-of-safety buy price of ~$45.** Note that even the *bull* case barely exceeds today's price — meaning an investor is being paid nothing for the risk of being wrong. That is the definition of an inadequate margin of safety.

---

## 4. Management Quality Assessment — **Incomplete, leaning favorable on execution, neutral on capital allocation**

- **Founder-led:** CEO Andrew Feldman co-founded the company in 2015 and has run it for a decade. Deep technical conviction — the wafer-scale bet looked reckless in 2015 and is now validated as an engineering matter. That earns credit.
- **Insider ownership** is likely substantial post-IPO, but I could not verify the precise post-IPO split within this data set — treat as an open item.
- **Capital allocation is the concern, not the strength.** Spending $383M of capex on owned data centers against $510M of revenue, with negative owner earnings, is a defensible land-grab in a capacity-constrained market but is precisely the kind of vertical integration that destroys returns if demand disappoints. Debt of $1.49B alongside a fresh IPO raise is also aggressive for a company with no profits. The $38M buyback in 2025 — while burning cash — is not a signal of discipline.
- **Governance risk:** the scale and nature of the UAE-related contracts, and the political/export-control dimension of Middle East AI compute, put revenue partly in the hands of policy rather than customers.
- **Transparency:** the FY2025 net income of +$238M presented against a -$145M operating loss is a fair-value artifact, legal but obscuring. Watch for how prominently this is disclosed.

**Assessment: competent operators, unproven capital allocators, no track record of earning a return on invested capital.** ROIC as reported (45.8% in 2025) is not trustworthy — it is distorted by negative equity and non-operating gains. On invested capital that includes the new $8.6B cash pile, returns are deeply negative.

---

## 5. Investment Verdict: **SELL / AVOID**

*For a Buffett-style mandate, this fails on nearly every test that matters:*

1. **Outside the circle of competence** — rapid technological obsolescence, a competitor with a vastly stronger ecosystem, and revenue that depends on a handful of sovereign and frontier-lab capital-spending decisions. Buffett's own rule: if you can't predict the business in ten years, don't value it.
2. **No demonstrated moat** — 14% gross margin in the most recent quarter is dispositive evidence of absent pricing power.
3. **No margin of safety** — intrinsic value ~$63 versus a $96 price. The bull case is required just to break even.
4. **Negative owner earnings and negative free cash flow** with capital intensity rising, not falling.

**The honest counterpoint:** this is not a fraud or a zero. The cash pile (~$6–7B net, ~28% of market cap) is real, revenue is genuinely growing ~74% YoY, $24.6B of reported backlog exists, and the technology is differentiated. That is why the verdict is **Sell/Avoid, not Strong Sell.**

**What would change my mind — the specific triggers to monitor:**
- Gross margin recovering above 40% for two consecutive quarters (proves pricing power)
- G42/MBZUAI concentration falling below 30% of revenue with US/European hyperscaler wins
- Free cash flow turning positive *excluding* customer prepayments
- Price below ~$45–50/share (a 25–30% discount to my $63 intrinsic value)
- Evidence the $10B OpenAI agreement is binding and expanding rather than migrating to Nvidia

On the last point: if the backlog genuinely converts, my base case is too low and the bull case is the right frame. But I will not pay today's price to find out. Patience costs nothing; being early on an overvalued AI infrastructure story costs a great deal.

---

## 6. Key Risks to the Value Thesis

**Risks to the downside (why I would not own it):**
1. **Nvidia competition** — the single largest risk. If CUDA-adjacent inference offerings win on total cost of ownership, Cerebras becomes a niche second source and the 14% gross margin becomes structural.
2. **Customer concentration** — 86% of 2025 revenue from two UAE-linked entities. Loss or delay of one contract is catastrophic. Export-control or geopolitical disruption to Gulf AI investment is a live, non-diversifiable risk.
3. **Lockup overhang** — staggered lockup expirations continue through November 9, 2026, releasing up to ~194M additional shares. Supply pressure persists into year-end.
4. **Capital intensity** — capex at 75% of revenue. If growth slows, the owned-data-center strategy becomes stranded capital.
5. **Debt** — $1.49B total, $824M current. Servicing $824M of near-term maturities while burning cash is manageable given the cash pile, but it constrains flexibility.
6. **Competition from hyperscalers' own silicon** (TPUs, Trainium, MTIA) — the largest buyers are also building substitutes.

**Risks to the upside (what would make my Sell wrong):**
1. Backlog conversion — $24.6B of contracted/indicated demand, if real and binding, implies revenue far above my base case by 2028.
2. Sovereign AI as a durable, large, non-US-hyperscaler market that Nvidia cannot fully serve.
3. Operating leverage once the data-center buildout matures — capex intensity could fall sharply, flipping FCF positive quickly.
4. A takeout or strategic partnership at a premium (the technology has clear strategic value).

---

### Data caveats (stated for transparency)
- FY2025 net income (+$237.8M) and EBITDA (+$279.3M) are inflated by non-operating fair-value gains; operating income was -$145.3M. Analysis uses operating figures.
- Q2 2026 revenue is reported as $180.1M in the income statement but $209.9M in the earnings calendar — a material discrepancy I could not resolve. I used the income statement; if $209.9M is correct, growth is meaningfully better and my base case should rise somewhat, though not enough to change the verdict at $96.
- FY2025 annual balance sheet shows equity of -$579M while the quarter-end Dec-2025 row shows +$1.35B (preferred stock mezzanine classification differences). The June 30, 2026 post-IPO figures ($8.61B cash, $9.15B equity) are the reliable ones.
- Peer valuation data limited to P/E median (37.7x); no peer EV/sales data was available from the feed.
