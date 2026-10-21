# Value Researcher

- Symbol: DVA
- Elapsed: 131.7s

---
# DaVita Inc. (DVA) — Value Investment Analysis
**Price: $175.35 (Oct 20, 2026) | Market cap ≈ $11.4B | Net debt ≈ $10.1B | EV ≈ $21.5B**
*(Shares ≈ 64.8M basic, Q2'26. Note: several data-feed multiples in my source files use stale 88M share counts and a $15.4B market cap — all figures below are recomputed on current shares. Next catalyst: Q3'26 results, Oct 29, 2026.)*

---

## 1. Business Quality Assessment — Moat: NARROW

DaVita is one of two scaled US dialysis providers (with Fresenius), operating ~2,700 US centers treating roughly 200,000 ESRD patients, plus home dialysis, inpatient acute contracts (~850 hospitals), its own lab, and international centers in ~10 countries.

**Sources of moat:**
- **Efficient scale / local density**: dialysis is a geographically local, three-times-weekly, non-deferrable service. Center density drives labor, lab, and supply-route economics; new entrants cannot replicate a two-player network at equal cost.
- **Switching costs**: ESRD patients are clinically enmeshed with a care team; transfer rates are low.
- **Intangible assets**: physician joint-venture relationships, state CON requirements in some markets, payer network contracts, and a 30-year operating/billing capability under a highly complex regulatory regime.
- **Confirmed by returns**: ROIC of 12.4% (2025), 14.8% (2024), 11.6% (2023), 9.5% (2022) — consistently above my ~8% WACC estimate, and *improving*. That is genuine moat evidence.

**Why not Wide:** DaVita has **no pricing power**. Medicare sets the ESRD Prospective Payment System rate, and government-linked revenue (Medicare + Medicare Advantage) is roughly 80%+ of the total. Management itself said on the Q2'26 call that the CY2027 proposed base-rate update "once again tracks below the cost trends for the industry." A business whose price is administered by a single payer and whose costs inflate at market rates has a structurally capped return, not a compounding franchise. Both the moat and the ROIC spread narrowed in 2025–26: gross margin fell from 32.9% (2024) to 27.0% (2025) as phosphate binders moved into the bundle (DaVita now bears the drug cost risk) and commercial mix eroded with the lapsing of enhanced ACA subsidies. At best, ROIC treads water.

**Moat trend: stable-to-slightly-narrowing.** Policy, not competition, is the moat's boundary.

---

## 2. Financial Quality Score: 6 / 10

| Metric (TTM to Q2'26 / FY) | Value |
|---|---|
| Revenue TTM | $14.0B (+6–7% YoY) |
| Revenue CAGR 2021–25 | 3.4% (accelerating: +5.6%, +6.5%) |
| Operating margin | 14.7% (2025); 16.3% (2024); 13.2% (2023); 11.5% (2022) |
| Gross margin | 27.0% (2025) vs 32.9% (2024) — **warning** |
| EBITDA TTM | $2.76B |
| Net income TTM (GAAP) | $847M; adj. EPS 2026E ≈ $14.65 |
| Operating cash flow TTM | $2.19B |
| Capex TTM | $583M (≈4% of revenue — genuinely low-intensity) |
| Free cash flow TTM | $1.61B (≈14% FCF yield) |
| Owner earnings (NI + D&A − capex, 2025) | $886M |
| Net debt / EBITDA | ≈3.7x |
| Total equity | $1.08B (vs $17.7B assets) |
| Dividend | None historically; ~$150M paid in Q2'26 (see note) |

**Positives:** Revenue is remarkably predictable (non-discretionary, recurring, volume-linked); capex is far below depreciation ($583M vs $715M), so reported FCF overstates normalized cash generation but is still robust; FCF conversion is strong in every year sampled.

**Negatives:** The balance sheet is the weak link. $10.8B of debt against $1.08B of book equity, negative retained earnings (heavy buybacks), and ~$560M of annual interest expense. Gross margin compression of ~600bp in a single year shows how quickly a policy change transmits to the P&L. ROE of 64% is a leverage artifact, not quality. Score docked for leverage, payer concentration, and margin volatility.

*Note on the dividend:* `get_dividends` returned no data, but the Q2'26 cash flow statement shows −$149.9M "dividends paid" (first in company history). Per-share amount and structure unverified — I have not credited it in valuation.

---

## 3. Valuation Analysis

**Current multiples (my recomputation, current share count):**

| Multiple | DVA | Comment |
|---|---|---|
| EV / EBITDA (TTM) | **7.8x** | vs. 12–14x historically (2019–21) |
| EV / EBIT (TTM) | 10.2x | |
| P/E — 2026E adjusted EPS $14.65 | **12.0x** | guidance reiterated at Q2 |
| P/E — TTM GAAP EPS $11.38 | 15.4x | |
| P/FCF (TTM) | 7.1x | flattered by capex < D&A |
| FCF yield / FCF-to-EV | ~14% / 7.5% | |
| Sector-peer median P/E | 31.7x | DVA at a 42% discount |

**Normalization (critical step):** I do not underwrite $1.6B of FCF as permanent. Maintenance capex for a mature center base is closer to D&A (~$700M), and GAAP earnings carry ~$250–300M of genuine drag from wound-down risk-based care (IKC) and impairments. My normalized owner-earnings figure is **$1.05–1.15B**, growing 3–4%.

**Intrinsic value (equity DCF on normalized owner earnings, 9.5% cost of equity, 4% growth for 10 years, 2.5% terminal; cross-checked on multiples):**

| Scenario | Assumptions | Value/share |
|---|---|---|
| Bear | CY2027 rate below cost trend + binder bundling squeezes EBIT 5–8%; refinancing at ~6.5% adds $100M interest; volumes flat | **$150** |
| Base | OE ~$1.1B, modest growth, leverage held at 3.5x, buybacks continue | **$215** |
| Bull | Rate update recovers, commercial mix stabilizes, 2%+ treatment growth by 2029 realized | **$270** |

Cross-checks: 8.5x EV/EBITDA = $224; 13x adjusted EPS = $190; 10x EV/EBIT = $170.

**Base intrinsic value ≈ $215. At $175 the stock trades ~19% below base case — inside fair value, but short of the 25–30% margin of safety I require.** Note the stock is 25% off its early-August high (~$247) following the Q2 revenue-per-treatment decline and a fresh ~6% drop on Oct 20 on heavy volume, cause unconfirmed. *(The built-in DCF tool returned a broken discounting series — PV of a $1.8B annual stream shown as $184M — so all DCF figures above are my own arithmetic.)*

---

## 4. Management Quality Assessment

**Positive.** CEO Javier Rodríguez (since 2015, career insider) and CFO Joel Ackerman have executed well operationally: volume growth is accelerating on improved mortality, guidance has been reiterated, and capital allocation has been aggressively per-share oriented. Diluted shares fell from 122.6M (2020) to **66.1M (Q2'26) — a 46% reduction** — through $1.6B (2021), $0.8B (2022), $0.3B (2023), $1.4B (2024), $1.8B (2025) and ~$0.76B in H1'26 of repurchases. That is exemplary per-share discipline, and net debt has actually fallen (~$14.3B → $10.1B) even while buying back stock — real deleveraging plus shrinkage.

**Negative.** The buybacks were partly debt-funded, leaving equity of just $1.08B; and 2026 repurchases occurred at $180–235/share (13–16x adjusted earnings), i.e. buying back stock at prices above today's quote while carrying 3.7x leverage. Empire-building is absent — DaVita has been exiting risk-based care rather than expanding it, which I respect — but the balance sheet leaves little room for a policy error. Insider ownership: **not retrieved (data gap)**; I infer alignment from behavior, not from filings.

Management grade: **B+ / good operators, aggressive but rational allocators, thin margin for error.**

---

## 5. Investment Verdict: **HOLD** (Buy below $160; trim above $250)

DaVita is a genuinely decent business — duopoly scale, recurring non-discretionary revenue, 12%+ ROIC, low capex, and a management team compounding per-share value — trading at 7.8x EBITDA and 12x adjusted earnings. That is not expensive.

But it is not the bargain the headline 14% FCF yield implies: normalized free cash flow is materially lower than reported, the gross margin just fell 600bp on a policy change, ~80% of revenue is priced by a single payer, $10.1B of net debt sits atop $1.08B of equity, and GAAP earnings are roughly half of "adjusted" earnings. My base-case intrinsic value of ~$215 offers only a ~19% discount — **fairly priced, not cheap**. Per my discipline, a fair price is not a buy. I would be a willing buyer of a full position at **≤$160** (25%+ discount to base case, ~11x adjusted EPS) and would add aggressively in the $130s, where the bear case is largely paid for.

---

## 6. Key Risks to the Value Thesis

1. **Reimbursement (dominant risk).** CY2027 ESRD PPS base-rate update is tracking below industry cost trends; the final rule (due imminently) plus phosphate-binder bundling could compress operating income by 5–10%. There is no ability to raise price in response.
2. **Commercial mix erosion.** Expiration of enhanced ACA subsidies is already reducing commercially insured (higher-paying) mix and revenue per treatment — the proximate cause of the August 2026 selloff and a continuing headwind.
3. **Leverage and refinancing.** 3.7x net debt/EBITDA with $560M of interest; a refinancing at 6%+ instead of legacy ~4.5% coupons would permanently reduce owner earnings. Equity cushion is ~$1.1B.
4. **GLP-1 structural threat.** Broad GLP-1 adoption may reduce the incident ESRD population over a 5–10 year horizon — a slow-burn threat to terminal value that is difficult to size and easy to ignore.
5. **Capital allocation at the wrong price.** Continued repurchases above intrinsic value, funded with debt, would destroy the very per-share compounding that makes the equity attractive.
6. **Margin structure.** Drug/supply and labor inflation against fixed, administered rates; the 2025 gross-margin decline shows limited pass-through.
7. **Legal/regulatory.** Historical DOJ kickback and charity-premium-assistance matters; False Claims Act exposure is a recurring tail risk in this sector.
8. **Near-term event risk.** Q3'26 results on Oct 29, 2026, nine days from this analysis, plus an unexplained 6% single-day decline on Oct 20 of unknown cause — I would not establish a position into that print.

*Data gaps disclosed: insider ownership, precise dividend terms, and the cause of the Oct 20 decline were not obtainable within budget; peer comparison uses a broad healthcare-sector median rather than pure dialysis comparables.*
