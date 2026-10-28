# Value Researcher

- Symbol: CLS
- Elapsed: 29.2s

---
# Celestica Inc. (CLS) — Value Investment Analysis

**Price $277.63 (27-Feb-2026) | Market cap ≈$32.3B | Net debt $320M | EV ≈$32.6B**

*Note: the automated DCF tool returned a unit-mangled result (WACC read as 1000%), so all valuation work below is built manually from reported financials.*

---

## 1. Business Quality Assessment

**Moat Rating: NARROW (and narrower than the recent numbers imply)**

Celestica is an electronics manufacturing services (EMS) provider, not a technology owner. It builds other companies' products — switches, routers, servers, storage, plus aerospace/defense, industrial and healthtech hardware. In 2025, 88% of revenue was cost of goods. This is a scale-and-execution business.

What has genuinely changed since 2021 is a mix shift toward design-led programs (HPS — hyperscaler hardware platforms) where Celestica co-designs the product rather than just assembling it. That is a real, defensible improvement:

| Evidence | 2021 | 2025 |
|---|---|---|
| Revenue | $5.63B | $12.39B |
| Gross margin | 8.64% | 12.06% |
| Operating margin | 2.98% | 8.64% |
| ROIC | ~n/m | 34.2% |

A 566bp operating-margin expansion on 2.2× revenue is not luck — it reflects design wins and pricing mix. That is the strongest argument *for* a moat.

**But applying the five moat sources honestly:**
- **Switching costs — narrow, real, temporary.** Re-qualifying a manufacturing partner for an 800G/1.6T switch program takes 12–18 months of joint engineering. Customers don't churn mid-program. But they *do* dual-source by design and re-bid each generation, and hyperscalers hold all the pricing leverage.
- **Cost advantage — weak.** Scale purchasing and low-cost footprint (Mexico, Thailand, Romania) are matched by Foxconn, Jabil, Sanmina, Fabrinet and Wiwynn. No structural advantage.
- **Intangible assets — modest.** Engineering talent, certifications, program IP. Valuable, but not a brand or a patent wall.
- **Network effects / efficient scale — none.**

**Verdict:** Narrow moat, resting on switching costs that reset every product generation, in an industry with a 30-year record of margin mean-reversion. Critically, gross margin of 12% is likely **peak-of-cycle** for an EMS business (Jabil ~9%, Foxconn ~6–7%). A 200bp normalization on $15B of revenue would erase roughly 40% of current net income. That is not a moat; that is a favourable product cycle.

**Customer concentration risk is severe.** The client base is a handful of hyperscalers; the top few customers are almost certainly each >10% of revenue. One insourcing decision or one AI-capex digestion year is an existential-level revenue event.

---

## 2. Financial Quality Score: **6 / 10**

| Metric | 2025 | 2024 | 2023 | 2022 |
|---|---|---|---|---|
| Revenue growth | +28.5% | +21.2% | +9.8% | +28.7% |
| Gross margin | 12.1% | 10.7% | 9.5% | 9.0% |
| Operating margin | 8.6% | 6.2% | 4.3% | 4.0% |
| Net income | $832.5M | $428.0M | $244.4M | $180.1M |
| Diluted EPS | $7.29 | $3.61 | $2.03 | $1.46 |
| Operating cash flow | $659.5M | $473.9M | $326.2M | $211.1M |
| Capex | $201.2M | $170.9M | $125.1M | $109.0M |
| **Free cash flow** | **$458.3M** | **$303.0M** | **$201.1M** | **$102.1M** |
| **FCF / Net income** | **55%** | **71%** | **82%** | **57%** |
| ROIC | 34.2% | 22.3% | 13.2% | 11.7% |
| ROE | 37.6% | 22.6% | 13.8% | 10.7% |

**Strengths:** Exceptional returns on capital (ROIC 34%), a repaired balance sheet (net debt/EBITDA just **0.26×**, current ratio 1.44, and retained earnings finally swung from a cumulative deficit of –$1,075M in 2022 to +$408M in 2025), and owner earnings of ~$807M.

**The problem — cash conversion.** Earnings are compounding faster than cash. FCF/net income averaged 66% over four years and only 55% in 2025. The cause is structural, not temporary: growth consumes working capital.

- Receivables: $2,077M → $2,633M (**+$556M**)
- Inventory: $1,760M → $2,184M (**+$423M**)
- Cash conversion cycle ≈ 65 days (DSO ~78, DIO ~73, DPO ~85)

Every dollar of incremental EMS revenue must be financed with receivables and inventory. This is the defining financial fact about Celestica, and it is why the stock trades at **38× earnings but 70× free cash flow.**

**Why not higher:** revenue predictability is poor (the 2000s–2010s history includes years of value destruction and a lost decade), margin stability has only four quarters-of-improvement of evidence, and FCF conversion is mediocre. **Why not lower:** the ROIC profile and balance sheet are genuinely excellent.

---

## 3. Valuation Analysis

**Current multiples at $277.63:**

| Multiple | CLS | Comment |
|---|---|---|
| P/E (trailing) | 38.1× | vs. peer median 44.5× (sector = semis/large-cap tech, a poor comp set) |
| EV/EBITDA | 26.9× | |
| P/FCF | 70.4× | FCF yield **1.43%** |
| EV/Sales | 2.63× | Historically 0.5–0.8× |
| P/B | 14.6× | |

The –15% "discount to peer median" the screening tool reports is meaningless here: CLS is being compared to NVIDIA, Apple and Microsoft. The correct comps are Fabrinet, Jabil, Sanmina, Foxconn — which trade at roughly 15–25× earnings, not 38×.

**Manual DCF (owner earnings basis).** I normalize FY2026 owner earnings to ~$1.00B (net income ≈$1.09B at 7% net margin on ~$15.5B revenue, + D&A $220M – maintenance capex $180M – SBC ~$90M). $1.00B is a fair starting base — more generous than trailing FCF of $458M, because it assumes working-capital drag eases as growth decelerates.

*Base case* — 20% growth yrs 1–3, fading to 15%/13%/10%/7%/5%/5%, 10% discount rate, 3% terminal:
→ PV of years 1–10 ≈ $12.6B + PV of terminal ≈ $17.0B = EV $29.6B → **equity ≈ $29.3B → $252/share**

*Conservative case* — 15% fading to 5% by year 7:
→ PV of years 1–10 ≈ $11.1B + terminal PV $14.6B = EV $25.7B → **equity ≈ $25.4B → $219/share**

*Aggressive case* — AI capex compounds at 25%+ for five years: intrinsic value rises into the $330–350 range.

**My intrinsic value estimate: ~$245/share (range $200–$330).**

**Verdict: the stock trades at roughly a 13% PREMIUM to intrinsic value.** The market is pricing in the aggressive case — sustained ~20%+ owner-earnings growth for five-plus years in a business with no structural moat and brutal customer concentration.

**Margin of safety:** none. My buy threshold — a 25% discount to $245 — is **≈$185/share, 33% below today's price.**

*Street context: analyst targets sit at $375–$520 (median ~$420), with notes posted at prices of $263–$366. The sell-side is extrapolating the AI cycle; I decline to capitalize cyclical peak margins at a growth multiple.*

---

## 4. Management Quality Assessment

**Rating: Good — arguably the best thing about this investment.**

- **CEO Rob Mionis (since 2015)** has executed one of the genuine turnarounds in contract manufacturing: revenue +120%, operating margin nearly tripled, ROIC from low-teens to 34%. That is operational excellence, not financial engineering.
- **Capital allocation is disciplined.** No dividend. Buybacks of $153M (2025), $152M (2024), $36M (2023), $35M (2022) — steady and funded from cash flow, not debt. Share count fell from 126.7M to 116.2M (~2%/yr).
- **No empire building.** Goodwill and intangibles *declined* from $715M (2021) to $598M (2025) — there is no rolling M&A program masking organic weakness. This is rare and commendable.
- **Balance sheet conservatism:** net debt/EBITDA of 0.26× despite tripling capex.

**Criticism:** buybacks have been executed into a rising stock (roughly $30s to $300), which is the least efficient use of the capital; and absolute repurchase dollars are trivial relative to a $32B market cap (~0.5%/yr net share reduction). Insider ownership data was not available to me — an honest gap I would want to close before committing capital.

---

## 5. Investment Verdict: **HOLD** (avoid new capital at $277)

| Test | Result |
|---|---|
| Within circle of competence? | Partially — the business model is understandable, but the durability of AI-driven demand is not something I can underwrite |
| Durable moat? | **Narrow**, cycle-dependent |
| Consistently high ROIC? | Yes — 34%, but only recently and not yet proven through a downturn |
| FCF conversion >80%? | **No — 55%** |
| Margin of safety? | **No — trading ~13% above intrinsic value** |

**Reasoning:** This is a good business with a good CEO that has become a great stock. Those are different things. At 38× earnings, 27× EBITDA and 70× free cash flow, the market has already paid for the successful execution and then some. Buffett's rule is that a wonderful business at a fair price beats a fair business at a wonderful price — but Celestica is a *narrow-moat* business at a *wonderful* price. That fails both legs of the test.

I would be an interested buyer at **$185 or below** (~25% discount to intrinsic value), which is roughly 24× normalized earnings and a 4% FCF yield on a fully-unwound working-capital base. Until then: **Hold if owned, do not initiate.**

---

## 6. Key Risks to the Value Thesis

1. **Margin mean-reversion (highest probability).** 12.1% gross and 8.6% operating margins are peak-of-cycle for an EMS provider. A 200bp GM normalization on $15B of revenue = ~$300M of gross profit, roughly 40% of net income. This is the single largest threat to both earnings and the multiple.
2. **Customer concentration / insourcing.** A handful of hyperscalers dominate revenue. Any one shifting volume to a captive line, a second source, or pausing a program is a step-function revenue event.
3. **AI capex digestion.** Celestica's growth is levered to hyperscaler capital spending. Capex cycles in this industry have never been linear, and the stock's own history shows the violence of the reaction: **–46% in Q1–Q2 2025** ($123 → $66) and **–20% in January 2026 alone** ($345 → $277), on no fundamental change.
4. **Working-capital cash drain.** Growth requires financing receivables and inventory. If growth stalls, the FCF picture improves — but if it stalls *and* margins compress simultaneously, the 70× P/FCF multiple has no support.
5. **Valuation compression.** At 26.9× EV/EBITDA, a de-rating to a still-generous 18× would cost ~33% of the share price with zero change in earnings.
6. **Beta of 1.46 and extreme drawdown behaviour** warrant position sizing at no more than 2–3% of a portfolio even for a buyer at the right price.

**Bottom line:** Quality business, good management, excellent current returns on capital — but no durable moat, poor cash conversion, and a price that already discounts the bull case. **Hold; buy only on a substantial de-rating toward $185.**
