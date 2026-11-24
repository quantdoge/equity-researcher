# Value Researcher

- Symbol: CRWV
- Elapsed: 148.2s

---
# CoreWeave, Inc. (CRWV) — Value Investment Analysis

**Price:** $48.33 (close 2026‑11‑23) | **Market cap:** ~$27.0B | **Net debt:** $60.7B | **EV:** ~$87.6B
**52‑week range:** ~$39.28 – $187 (‑74% from June 2025 peak) | **Div yield:** none
*Note: the ratio tool's P/E/P-B used a stale 435M share count; I use the Q3'26 weighted 559M shares throughout.*

---

## 1. Business Quality Assessment

**Moat rating: NONE.**

CoreWeave rents GPU compute — overwhelmingly NVIDIA GPUs — to AI labs and hyperscalers from leased data‑center shells. It is an **equipment lessor**, not a software business, despite the "Software – Infrastructure" classification.

| Moat source | Assessment |
|---|---|
| Intangible assets | None. They buy the same NVIDIA silicon at the same price as Microsoft, Oracle, Amazon, and Google. No proprietary chip, no proprietary model. |
| Cost advantage | **Negative.** They lease the shells and scramble for power in the most competitive land/power market in decades. Hyperscalers own their shells and have captive power. |
| Switching costs | Modest. Multi‑year take‑or‑pay contracts do bind customers mid‑training‑run — the one real positive — but this cuts *against* CRWV on price: fixed‑price contracts mean the customer captures all upside from a longer GPU life or falling hardware costs. |
| Network effects | None. |
| Efficient scale | None. 4.6 GW of contracted power across many third‑party providers; capital is perfectly mobile into this asset class. |
| Customer concentration | Extreme. Microsoft has been >60% of revenue; OpenAI is now the marginal contract. A single counterparty renegotiation is existential. |

**The decisive test — does the asset earn its cost of capital?** Build economics are roughly **$44M of capex per active MW** ($75.7B net PP&E / 1.7 GW) against **~$8.6–9.2M of revenue per MW per year** (Q3'26: $3.66B on ~1.6GW avg). Over a 6‑year GPU life, a MW generates ~$52M of cumulative revenue and, at a 62% adjusted‑EBITDA margin, **~$32M of EBITDA against $44M of investment.** That is a negative lifetime return on capital. Stretch the useful life to 8 years and it's ~2% annualized.

This is why reported ROIC is **‑0.14% (2025), +3.17% (2024), ‑1.0% (2023)** — never once above any plausible WACC. The moat has not widened; it has narrowed as hyperscalers brought their own capacity online and NVIDIA began allocating directly.

**Circle of competence: this business fails it.** Its value rests on two unknowables — the *economic* useful life of a GPU (architecturally superseded in 18–24 months; they are already deploying Vera Rubin against GB200 fleets) and the future spot price of compute. I cannot forecast either with the confidence a 20–30% margin of safety demands.

## 2. Financial Quality Score: **2 / 10**

| Metric | 2023 | 2024 | 2025 | 9M 2026 |
|---|---|---|---|---|
| Revenue | $229M | $1,915M | $5,131M | $8,314M |
| Gross margin | 70% | 74% | 72% | 68% |
| GAAP operating income | $(14)M | $324M | $(46)M | $14M |
| **D&A as % of revenue** | 45% | 45% | **48%** | **53%** |
| Net income | $(594)M | $(863)M | $(1,167)M | $(2,075)M |
| Interest expense | $28M | $361M | $1,229M | $2,022M |
| Capex | $2.9B | $8.7B | $10.3B | $23.6B |
| **Free cash flow** | $(1.1)B | $(6.0)B | **$(7.3)B** | **$(17.9)B** |
| Total debt | $2.0B | $10.6B | $29.8B | **$66.2B** |
| Equity | $(597)M | $(414)M | $3,335M | $4,025M |

The revenue trajectory is genuinely extraordinary (+168% YoY in Q3'26; FY26 guide $13.0–13.3B, exit‑2026 ARR $20–21B, backlog $132.5B). Everything else is alarming:

- **FCF conversion is catastrophically negative** — the single most important Buffett metric, and it is the worst I have seen at this scale: ‑$17.9B in nine months.
- **Depreciation, not growth, is the story.** D&A has climbed from 45% to 53% of revenue and, because PP&E is still young (much of it pre‑revenue CIP), it is converging *toward* ~78–83% of revenue at steady state (0.20x asset turnover ÷ 6‑year life). The 62% adjusted‑EBITDA margin is a headline that ignores the ~80 points of depreciation this asset class eventually carries. **GAAP operating margins should be expected to deteriorate as the fleet ages, not improve.**
- **Leverage is at the edge.** Liabilities of $87.5B against $4.0B of equity: **94% debt‑to‑capital.** Interest alone is ~24% of revenue and Q4'26 guidance is $1.05–1.15B *in one quarter* (~$4.2B annualized). EBITDA covers interest ~2.0–2.6x — sub‑investment‑grade metrics with equity‑like volatility.
- **Financing dependence is now the business model:** $4.2B of converts, a 35M‑share ATM, $2.6B DDTL 5.5 (explicitly *short‑duration*), and reliance on ~$9B of customer prepayments in a single quarter. CDS spreads near **1,000bps** imply the credit market prices a ~35–40% five‑year default probability. When credit and equity disagree at 94% leverage, credit is usually right.
- **Cash conversion:** operating cash flow of $3.06B in 2025 flattered by $632M of working‑capital inflow and $2.45B of non‑cash D&A. It is entirely consumed — and then some — by capex.

Revenue growth: 10/10. Everything that determines whether the business is *worth* anything: 0/10.

## 3. Valuation Analysis

| Metric | Value | Comment |
|---|---|---|
| P/S (FY26E) | 2.0x | Deceptively cheap — but debt‑funded |
| **EV/Sales (FY26E)** | **6.7x** | The honest number |
| EV/adj. EBITDA (FY26E ~$8.2B) | 10.7x | On an EBITDA that overstates cash by ~$8B/yr |
| EV/adj. EBITDA (exit‑run‑rate ~$12.7B) | 6.9x | The bull anchor |
| P/B | 6.7x | For a ~0% ROIC asset base |
| P/FCF | negative | No meaningful multiple |
| Peer median P/E | 27.4x | Not a valid comparison (CRWV loss‑making) |

**Intrinsic value — I will not use a DCF built on trailing FCF (it is negative and meaningless).** Instead I value the *cash the assets can actually throw off* after the depreciation that funds their own replacement:

- **2027E:** revenue ~$26B, adjusted EBITDA ~$15.5B, D&A ~$9–10B → **EBITDA less maintenance capex ≈ $6B.**
- At 12–15x that figure (appropriate for a levered, cyclical, no‑moat lessor): EV of **$72–90B**, less $60.7B net debt (and rising) → **equity of $11–29B, or $20–52/share.**
- **Base case intrinsic value: ~$25–30/share** (EV ~$75B). Requires the 2027 ramp to land on schedule *and* no refinancing shock.
- **Bull case (~$55–65):** assumes asset productivity improves ~2x and Rubin extends useful life to 8 years, letting steady‑state D&A fall to ~60% of revenue.
- **Bear case: $0.** Equity is a levered call option; a single customer renegotiation, a failed DDTL rollover, or GPU price deflation wipes it out.

At $48.33 the market is paying **full price for the bull case** with the bear case still live. There is no margin of safety — there is negative margin of safety. The reverse‑DCF implied by an $87.6B EV requires ~$8.8B of perpetual owner earnings, which requires revenue well above $50B at a depreciation burden the current asset productivity cannot support.

## 4. Management Quality Assessment

**Founder‑led but not owner‑operator disciplined in the Buffett sense.**

- **Positives:** Michael Intrator and co‑founders built this from a crypto miner in 2017 into the reference AI cloud — exceptional execution and salesmanship. Winning 9 of 10 leading foundation model labs, a $132.5B backlog, and NVIDIA backstop/equity support is real operating achievement. First‑mover speed in deploying new architectures (first Vera Rubin NVL72 production workloads) is a genuine capability.
- **Negatives:** Capital allocation is **growth at any price**, funded with 94% debt and an ATM equity program — the opposite of conservatism. The company reports "adjusted operating income" that excludes both D&A and SBC ($160M/qtr), i.e., it guides investors to a metric that ignores the dominant cost of its own assets. DDTL 5.5, explicitly designed for "shorter‑duration customer contracts," signals the matching of short‑lived assets to long‑dated obligations is under strain. Dividends: none; buybacks: none; dilution: ongoing.
- **Insider ownership and post‑IPO selling:** not verifiable from the data available to me — **flagged as a gap.** I would want the Form 4 record before trusting management's alignment.

## 5. Investment Verdict: **SELL / AVOID**

This is the archetype of what Buffett avoids: a capital‑devouring, commodity, hyper‑competitive, heavily levered business whose economics depend on the kindness of both the capital markets and a single dominant customer — at a price that already discounts the good outcome.

It is a spectacular *growth* story and a poor *business*. Revenue has compounded from $16M to $13B+ in four years while cumulative free cash flow over the same span is roughly **‑$26B**. Growth is being purchased with balance‑sheet capacity, and the bill (interest at ~$4B/yr today, materially more in 2027 on $100B+ of debt) is now consuming ~24% of every revenue dollar.

- **Not a buy at any price I can defend.** At $48.33 my base‑case intrinsic value is ~$25–30, and the bear case is zero.
- I would need the price near **$15–20** — a genuine 40%+ discount to base‑case IV — *plus* evidence that depreciation is stabilizing as a share of revenue, *plus* a visible path to positive levered FCF, before this enters the circle of competence as a speculative position.
- For a value portfolio: **zero weight.** Capital is better deployed in moated businesses with FCF conversion >80%; this one converts FCF at ~‑140%.

*The sell‑side is split almost comically — D.A. Davidson at $45, Rosenblatt at $160 — which is itself the tell: nobody, bull or bear, can actually forecast this business. That is not an investment; it is a macro bet on AI compute scarcity, expressed with leverage.*

## 6. Key Risks to the Value Thesis (i.e., how I could be wrong)

1. **GPU useful lives are longer than I assume.** If Rubin‑class assets hold economic value 8–10 years rather than 5–6, steady‑state D&A falls to ~50–60% of revenue, operating margins turn solidly positive, and the equity is worth multiples of today's price. *This is the single load‑bearing assumption in my bear case.*
2
