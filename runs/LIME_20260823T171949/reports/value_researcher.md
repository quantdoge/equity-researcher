# value_researcher

_2026-08-23T09:26:46+00:00_

# LIME (Neutron Holdings, Inc.) — Buffett-Style Value Report

## Data-Basis & Coverage Warning (read first)

LIME is a **recently public company (IPO 2026-07-01; profile-symbol `company/profile-symbol`)**. Because FMP's financial-statement endpoints (`income-statement`, `balance-sheet-statement`, `cashflow-statement`, `key-metrics`, `enterprise-values`, `owner-earnings`) all return **`not_found`** for LIME, **all income/cash-flow/balance-sheet figures below are sourced from the S-1 registration and post-IPO earnings disclosures as reported by third parties (SEC.gov, Dealroom, MostlyMetrics, Yahoo Finance, Investor's Business Daily, Seeking Alpha, Micromobility Industries).** None are FMP-retrieved. I flag this plainly: **FMP has zero financials for this name; every financial figure is web-sourced, not a pulled dataset.** The only FMP-retrieved data points are identity/market-cap/price (profile-symbol) and peers (company-tool).

---

## 1. Business Quality & Economic Moat: **Narrow, and uncertain**

| Evidence (all S-1/web-sourced) | Assessment |
|---|---|
| ~1B lifetime rides; ~19M riders in 2025; ~230 cities, 29 countries; ~27% global share, 37% U.S. share, ~3x nearest operator | **Scale leader — real, but leadership of a young category** |
| Marketing <2% of revenue; MAU +21%; average fleet +18% with revenue/vehicle/day (RVD) +5% | A *supply-side* local network effect — denser supply increases rider reliability |
| RFP win rate ~90%, permit renewal >95% (including Paris 2023 exit and Madrid 2024 revocation) | Permits are the true moat *and* the existential throttle |
| Vertically integrated hardware/software, swappable batteries, per-fleet-unit ops | Potential **intangible/cost-advantage moat** — but execution-dependent |
| Subscription mix rose 20%→28% of revenue; subscription riders ~6x trip frequency | **Modest switching-cost build** (app + prepaid pass nexus) |

**Verdict:** Lime's *only* structural advantage is **regulatory scarcity** (city permits) plus local density effects. These are real but **not proprietary economics** — the vehicles are commoditized, capital-intensive hardware; riders have near-zero single-trip switching cost; and the franchise can be revoked by a public vote (Paris) or city order (Madrid), destroying city-specific fleet value overnight. This is closer to a **capital-intensive, permit-regulated rental utility** than a software-moat compounder. On the Buffett test — *durable pricing power + returns on invested capital reliably above cost of capital* — Lime has **not yet earned it**. Moat rating: **Narrow, contestable, and city-concession-dependent.**

---

## 2. Financial Quality / Balance Sheet

**Growth & efficiency (2023–2025, S-1):**
- **Revenue:** $522.0M (2023) → $686.6M (2024) → $886.7M (2025), +29% YoY (FMP not available; Disney via SEC/Sources).
- **Gross margin 39.0%** ($345.4M GP, slipped from 40.9%); **Adjusted gross margin ~52%** (ex-fleet Depreciation, $467.2M adj GP) — the ~13pt gap *is* fleet wear.
- **Adjusted EBITDA:** $99.8M→$153.4M→$218.1M (+42% in 2025); **FY2026 guidance $265–285M**.
- **Operating income flipped positive:** −$24.6M (2023) → +$47.0M (2024) → **+$70.4M (2025)**. The core operating business is now cash-generative.
- **Net income is misleading:** net losses −$122.4M (2023), −$33.9M (2024), −$59.3M (2025) despite rising op-income. The 2025 §93M "other expense" line was largely a **non-cash mark-to-market charge (~$84M) on 2021 convertible-notes fair value** — it disappears when notes convert at IPO. Interest expense is modest (~$20M). **This is why is not, on its own, the operative margin signal.**
- **Free cash flow:** +$103.8M in 2025 (3rd consecutive year), but **2016 Q1 FCF was −$79.2M** (capital expenditure front-loaded into a seasonally weak quarter). FCF is *volatile and capex-hungry*, not dependable owner earnings.
- **Q2 2026 (post-IPO):** Revenue $304M (+24%), Adjusted EBITDA ≈$84M, but **net income of ~$295M was inflated by one-time IPO-related items (a tax benefit) and the CFO cited diluted EPS ($4.43-$4.73) that is not recurring.** Underlying GAAP operating profitability is thin.

**Balance sheet quality (post-IPO):**
- Pre-IPO liabilities ~$821M: **$115M conventional Senior Secured term loan (10%**, due Sept 2026) repaid from IPO proceeds; **~$706M of convertible notes (2020+2021) automato- convert to common stock.** Post-IPO chart shows **"current $114,622 thousand term loan"** — the company **cleared essentially all long-term debt**. New **$200M JPMorgan revolver placed, mainly undrawn (cushion for negative-FCF winter quarters).**
- Net leverage is now low-to-negative; **the crisis-era capital structure is mostly gone.** The caveat: this "deleveraging" came from **equity conversion**, so the share count ran up ~46M from conversions and favorites converting (e.g., Sapphire ~15.2%, Uber 21.9% post-IPO, Fidelity 10.3%).
- Internal-rail: **the business is profitable at operating/EBITDA level; the balance sheet is now cleanish; the open question is reinvestment.**

**Quality integer score: 6/10 — real turnaround and now net-debt-light, but (a) earnings are heavily **one-time/non-cash inflated**, (b) gross margin fell, (c) FCF is capex-front-loaded and quarter-volatile, and (d) owner-earnings remain a small fraction of reported EBITDA.**

---

## 3. Intrinsic Value Estimate (method & assumptions)

FMP's discountedCashFlow endpoints produce **no output for LIME** (no underlying statement data); **DCF must be custom. Everything below is a **methodology and input**; the final number requires the quant-engineer (see **COMPUTE REQUESTS§**).

**Assumption framework the quant should drive:**
- **Base:** 2026 guidance Revenue $1.04–1.10B; Adjusted EBITDA $265–285M; CapEx $180–185M (all cited).
- **Owner-earnings proxy:** Because Adjusted EBITDA *adds back fleet depreciation* — the single largest *real* replacement cost — true owner earnings for a value buyer must be **Adjusted EBITDA − fleet-replacement capex − working-capital** ≈ closer to the ~$100M-level 2025 reported FCF than to $200M+ EBITDA. This is the central discount in any DCF.
- **Growth:** Company is compounding revenue ~25–30%; the DCF should assume a fade to mid-single-digit terminal growth (category + share gain is real but capped by city permit conversion rates and the fact that supply is bought, not built free).
- **WACC:** ~10–13% (small specialty company, thin margins, high reinvestment beta; **confirmation pending** from available risk metrics).

**Useful anchors already cited (not my computation):** at the $25 IPO price, from the "Demand/leverag" sourcing the company valued **EV ~5.5–1.9x trailing sales, ~1.2x next-year sales, and ~1.6x next-year Adj-EBITDA**, positioned between Uber (~2.8x sales) and Lyft (~1.1x). *At the IPO price the name was cheap against soft comps.* The current price has since risen materially (see §4).

**Bottom-line (directional, not a computed internal value):** A fair intrinsic range likely sits **below the current market price when measured on owner earnings net of fleet capex**, and *at-or-modestly-above* it only if you accept the non-GAAP Adjusted-EBITDA-and-growth re-rating the market did plus-IPO. The cheapness captured at IPO has largely been **arbitraged by the post-IPO rally.**

---

## 4. Margin-of-Safety Verdict

**Could expensive / No margin enough in a value frame.**

- At IPO, Lime priced at **$25/share, post-IPO mixed $1.63B (~$1.8B annum fully diluted; ~65.1M shares)** (Yahoo/Sources).
- Now FMP profile shows **$41.06/share, $2.63B** **market cap (FMP `company/profile`)** — roughly **+64% above IPO price** and ~2x the bottom-of-its range. FMP-verified; arithmetic re-derived below.
- The market has effectively pívoted from the **cheap-IPO thesis (~1.5–7x leverage)** to a **full-growth re-rating on Adjusted EBITDA delivered**, even though the recur-ring owner-earnings leg is only ~the 2015 FCF $104M (~1/2 of a $219M EBITDA on a $2.6B cap).
- If Q1 FCF can flip −$79M and GAAP net income is propped by one-time items, an investors paying $2.6B is **forecasting the depreciation-add-back to become mostly-cash and the fleet spend ($180–185M/yr) to tail lower.** That is not now objectively measurable; it's **a tested-discipline wager**, not a margin of safety.
- Even with a clean balance sheet post-IPO and real operating EBITDA, **value-investing discipline requires a ~20–30% discount to intrinsic**; current price offers **none**, and the macro-sector (permit), pre-/post category) is ****heads-risky****.

**Verdict: AVOID / NOT A BUY.** The right owner-earnings LOB is not obvious, but at $2.6B* this is a *speculative asset priced for flawless execution* rather than an equity into which a margin-of-safety framework fits. The IPO printed value for early holders; much of it is now **concedes to the market.** For an existing holder, **Hold / trimmed.**

**Overall rating: NAVOID (speculative; structures not Buy).** Business real, capital heavy, cash-generative at EBITDA, but the price has removed the cheap-original thesis.

---

## 5. COMPUTE REQUESTS (route to quant_engineer)

I cannot derive ratios/ers values myself (no arithmetic/ratios). Please compute over the S-1/disclosure figures I've cited:

1. **`COMPUTE_REQUEST: current market multiples`** — Given market cap $2,628,904,932 (FMP profile), Adjusted EBITDA FY2026 $265–285M (guidance), TTM revenue from f'24 Q2→25Q2 and FY26 $1.04–1.10B, compute current **EV/Adj EBITDA, P/Sales-trailing, P/Sales-forward, P/FCF(2025 $103.8M), P/Owner-earnings.**
2. **`COMPUTE_REQUEST: price move`** — % move from IPO $25 to current $41.06; % move from Q2-report ~$34.3 (IBD) to current; confirm the multiple-compression.
3. **`COMPUTE_REQUEST: owner-earnings DCF sensitivity`** — 10-year DCF on Adá base with two earnings bases (OwnerFCF≈$100M starting; Adjusted-EBITDA≈$219M starting), revenue fade 25%→terminal 4%, WACC 10–13%, cap-ex tail $180M a year, terminal exit. Report intrinsic/per-share at each base, and % discount/(premium) to $41.06.
4. **`COMPUTE_REQUEST: reinvestment-rate test`** — incremental capex ($180–185M) vs incremental Adjusted EBITDA and FCF 2025→2026, to assess return on reinvested fleet capital.

---

**Key Risks to the Value Thesis** (each cited below against the data above):
- **Permit concentration & political exit risk:** Paris and Madrid exits show cities can remove the franchise at a vote/order — access scarcity, not property.
- **GAAP-quality:** Adhesion EBITDA adds back dep, net income is one-time-inflated; **Adjusted-company growth could mask true owner earnings.**
- **Capex treadmill:** $180–185M/yr fleet spend with −FCF winter quarters; the Lo Ro is upkeep-dependent, not self-financing.
- **Uber dependency** (~21.9% equity, ~14.3% revenue via in-app channel).
- **Fleet/litigation/insurance risk:** battery cells have caught fire; theft/vandalism (incl. organized retail crime case); insurance bill +$19.1M/yr; contingent-worker reclassification risk (France, Switzerland, Spain).
- **Depreciation change going public (straight-line, 2025)** — a timing-friendly estimate change that will flatter post-IPO margins.

**Follow-on question worth a dedicated pass:** the *quant* return on the owner-earnings-level DCF (Request 3). If its answer is **≤$31–33/share** — i.e. a 20–30% discount vs the $41 close — that's the visible no-bed for this whole thesis.
