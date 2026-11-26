# Macro Researcher

- Symbol: ORCL
- Elapsed: 55.1s

---
## 1. Macro Environment Summary — **Risk-Off within a Reflationary Regime (bifurcated market)**

As of 25-Nov-2026, the US is running a **late-cycle reflation with a hawkish, arguably still-behind-the-curve Fed**, and the long end is repricing violently:

- **The Fed reversed course.** Policy was eased from 4.33% (mid-2025) to 3.63% by Apr-2026 and held through Aug-2026. It has since **hiked twice** — effective Fed Funds 3.75% (Sep-2026) → **3.88% (Oct-2026)**, target range 3.75–4.00%. The Oct-28 FOMC held, but minutes show "nearly all" officials favour a quarter-point hike on **9-Dec-2026**; FedWatch odds ~97% (→ 4.00–4.25%). Cook (20-Nov) and Waller have explicitly called for hikes.
- **Growth is too strong to justify cuts.** Real GDP Q3-2026 = $24,665B, **+2.3% YoY and ~+4.3% QoQ annualised** (Q2 +2.2%, Q1 +2.5%). Unemployment has *fallen* to **4.1%** (Oct-2026) from 4.5% a year ago. Nominal PCE is growing **+6.4% YoY** — an economy that does not need easing.
- **Inflation re-accelerated after the Fed's cuts.** CPI **3.82% YoY** (Oct-2026), up from a mid-2026 trough; the last four months annualise near 4.5%. Critically, **10Y breakevens are *falling*** — 2.12% today vs 2.40% on 10-Sep-2026. So the bond sell-off is **not** inflation-expectation-driven; it is **real-yield / term-premium driven** (10Y real ≈ **3.0%**).
- **Curve is bear-steepening:** 2Y 4.74% / 5Y 4.93% / 10Y **5.13%** / 30Y 5.47%; 2s10s +39bp (no inversion). The 10Y at 5.13% is above Fed Funds by 125bp — the market is pricing *more* tightening and a fiscal term premium, not relief.
- **Credit is two markets.** Broad US HY OAS is **3.72%** (25-Nov-2026) — historically tight, i.e. the system is *not* in a credit crisis. But AI-capex borrowers are being repriced as distressed: **Oracle 5Y CDS hit a record 356bp**, its new bonds priced at up to 8.65%, its paper trades near **9%**, and CoreWeave's spread implies a 68% five-year default probability. **This is a sector-specific credit event inside an otherwise calm market.**

**Regime call: transitional/risk-off for long-duration, levered equities.** Rising real yields + a hiking Fed + a firm dollar are the dominant macro forces, and they hit exactly one kind of company: high-beta, debt-funded, long-dated-cash-flow growth stories.

## 2. Key Macro Variables

| Variable | Latest | Date | Direction (12m) | Regime read |
|---|---|---|---|---|
| Real GDP growth | +2.3% YoY / ~+4.3% QoQ saar | Q3-2026 | Re-accelerating | Too hot for cuts |
| CPI YoY | 3.82% | Oct-2026 | Re-accelerating H2 | Sticky |
| 10Y breakeven | 2.12% | 25-Nov-2026 | Falling (from 2.40%) | Expectations *anchored* |
| Fed Funds (effective) | 3.88% (target 3.75–4.00%) | Oct-2026 | Hiking; +25bp priced Dec-9 | Hawkish |
| 2Y / 10Y / 30Y | 4.74% / 5.13% / 5.47% | 26-Nov-2026 | Bear-steepening | Term premium |
| 10Y real yield | ~3.01% | 26-Nov-2026 | **Rising fast (+40–50bp in ~6 wks)** | The key variable |
| US HY OAS | 3.72% | 24-Nov-2026 | Tight/stable | Broad credit calm |
| ORCL 5Y CDS | ~356bp (record) | Nov-2026 | Blowing out | Idiosyncratic stress |
| Broad USD index | 123.60 | 20-Nov-2026 | +3.0% since Jun, +4.7% since 10-Sep | Headwind |
| Unemployment | 4.1% | Oct-2026 | Falling | Tight labour |

## 3. Company-Specific Macro Impact — Oracle

Oracle is no longer a classic software compounder on macro exposure; since the OCI buildout it has become **a levered, rate-sensitive infrastructure financier wearing a software multiple** — ~$125–130B of debt, FY26 capex up ~162% to ~$56B, a $45–50B capital-raise programme (including $10B equity at an 11% discount and $10B of bonds at 8.65%), and $11.4B of customer prepayments flattering operating cash flow. Beta is **1.78**.

| Macro variable | Impact | Transmission channel |
|---|---|---|
| **Real 10Y yield / term premium (5.13% nominal, ~3.0% real)** | **Strongly negative** | Two hits: (a) discount rate on FY30-weighted cash flows — at $103.88 ORCL trades ~14x FY27 guided EPS and ~5.4x its FY30 EPS target, i.e. ~85% of value sits beyond year 3, so +100bp on the discount rate is worth roughly −15–20% of equity value; (b) direct cost of capital — marginal debt at 8.65–9.0% versus a project IRR that is falling as AI pricing normalises |
| **Fed hiking cycle (Dec-9 hike ~97% priced)** | **Negative** | Removes the "cuts will bail out the buildout" narrative; raises short-rate reset cost on floating/revolver debt; extends the window in which ORCL must fund at punitive spreads |
| **Credit conditions (HY OAS 3.72%, but ORCL CDS 356bp)** | **Strongly negative** | ORCL is a price-taker in a market that has singled it out. Record CDS + $10B equity raise at an 11% discount = the two things equity holders fear most: rising funding cost *and* dilution. Any downgrade into BBB-/high-yield territory would force index-driven selling |
| **Nominal GDP / enterprise IT budgets (+6.4% nominal PCE, +4.3% GDP)** | **Positive** | Backlog/RPO conversion and triple-digit OCI growth are real; strong nominal demand supports multi-year contract pricing |
| **CPI 3.82% / build-cost inflation** | **Negative (net)** | ORCL's inputs are physical and cyclically scarce — GPUs, power, land, electrical equipment, construction labour. Sticky 3.8% services inflation and hardware tariffs inflate cost-per-MW faster than multi-year cloud contracts can reprice |
| **USD strength (123.6, +4.7% since 10-Sep)** | **Negative** | Roughly 40–45% of revenue is non-US; a 5% dollar move is a ~2pt revenue translation headwind, and it raises the local-currency price of USD-denominated OCI contracts for EM/European customers |
| **Unemployment 4.1% / tight labour** | **Mildly negative** | Wage pressure on cloud engineers and, more importantly, corroborates "no cuts" |
| **Fiscal deficit / term premium; government demand** | **Mixed → negative net** | ORCL is a large federal contractor (demand positive), but deficit-driven term premium is the single biggest destroyer of its equity value |
| **Equity risk appetite (beta 1.78)** | **Negative** | The AI-complex is in active de-rating: NVDA −38% from its 6-Oct peak ($239→$149), ORCL −68% from its Sep-2025 peak. MSFT, which self-funds its buildout, is **+19% since 1-May** — the market is paying for cash flow and punishing leverage |

**The evidence the shock is macro-mechanical, not just company-specific:** ORCL fell from $170.60 (1-May-2026) to $103.88 — **−39%** — while MSFT rose 19% and NVDA fell 25% over the identical window. ORCL is down **−46% YTD 2026** and **−68%** from its 10-Sep-2025 close of $323.43. The dispersion between levered (ORCL, CoreWeave, Nebius) and self-funded (MSFT, GOOGL) AI exposure is precisely the signature of a rising-real-rate, rising-term-premium regime.

## 4. Macro Risk Rating: **UNFAVOURABLE**

This is close to the worst feasible macro mix for Oracle specifically: **rising real yields** (maximum damage to long-duration, levered equity), a **Fed still hiking** (denying the pivot that would compress its spread), **sticky cost inflation** on physical build inputs, and a **firming dollar**. The one genuinely supportive force — strong nominal growth and a huge AI backlog — accrues to revenue and backlog, not to free cash flow, and the market is currently capitalising cash flow. The offsetting comfort is valuation: at 14x FY27 EPS and 5.4x FY30 targets, a great deal of the funding risk is now priced, and a December funding update plus $11.4B of customer prepayments provide near-term liquidity.

## 5. The Scenario That Would Materially Surprise — **Bear: "The December Credit Accident" (~30% probability)**

The consensus expects the AI-credit scare to stay contained because broad HY spreads are 3.72%. **The surprise is a self-reinforcing funding spiral triggered by policy.**

Sequence: the Fed hikes 25bp on **9-Dec-2026** *and* the SEP dots show a higher terminal rate for 2027 (inflation at 3.8% and GDP at 4.3% give hawks the votes). The 10Y breaks 5.40% and heads for 5.60–5.75% as term premium compounds; the 10Y real yield goes to ~3.4%. Simultaneously, ORCL's December fiscal-Q2 update shows capex guidance rising again while operating cash flow ex-prepayments stagnates. The ratings agencies move to negative outlook. ORCL CDS takes out 500bp, its 9% bonds trade to 10.5%, and the equity loses the "software multiple" floor entirely — the stock trades as a levered infrastructure SPV at 8–10x earnings, i.e. **$70–80 (−25% to −33%)**. Because ORCL is a bellwether, that print forces a mark-to-market across the whole AI-credit complex (CoreWeave, Nebius, and the private-credit warehouses behind them), which is where the systemic risk actually lives — not in the IG index.

The skew is genuinely two-sided: the mirror-image bull case (inflation rolls over as shelter/tariff base effects lap in H1-2027, the December hike proves to be the last, real yields fall ~60bp and ORCL's spread compresses) is worth **+50–70%** to $160–175. But the *distribution* is asymmetric in the wrong direction right now, because the macro variable that matters most to Oracle — the real 10-year yield — is moving against it with momentum, and the company must refinance into that market.

**Data gaps to note:** FRED's real-time policy path beyond the December meeting, ORCL's exact debt maturity ladder and floating-rate share, and the precise non-US revenue split are not in the retrieved data; the debt, capex and funding figures above are drawn from press coverage dated 24–25-Nov-2026 rather than filings. CPI for Oct-2025 is a missing observation in the FRED pull (YoY computed on the reported 3.82% series value).
