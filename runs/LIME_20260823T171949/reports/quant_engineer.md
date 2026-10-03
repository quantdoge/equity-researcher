# quant_engineer

_2026-08-23T10:44:43+00:00_

**External inputs (web/S-1-cited, supplied in the request — NOT FMP; FMP has no statements for this Jul-2026 IPO, confirmed by empty prior calls in this workspace):** price $41.06; market cap $2,628.904932M; IPO $25.00 (7/1/26); ref $34.30; revenue 2023/24/25/26E = $522.0 / $686.6 / $886.7 / $1,070.0M; adj EBITDA 2025 $218.1M, 2026E $275M; 2025 FCF $103.8M; shares 65.0M (assumed); net debt ≈ $0 (assumed). All figures below computed by quant_engineer in Python; $M throughout.

1. **Price change** — (41.06/25.00 − 1) = **+64.24%**; (41.06/34.30 − 1) = **+19.71%**.

2. **Revenue CAGR** — 2023→2025: (886.7/522.0)^(1/2) − 1 = **+30.33%**; 2023→2026E: (1,070/522)^(1/3) − 1 = **+27.03%**.

3. **Adj EBITDA margin** — 2025: 218.1/886.7 = **24.59%**; 2026E: 275/1,070 = **25.70%**.

4. **Rule of 40 (2025)** — revenue growth (886.7/686.6 − 1) = 29.14% + FCF margin (103.8/886.7) = 11.71% → **40.85**.

5. **Implied serviceable market** (2025 rev ÷ share) — 27%: 886.7/0.27 = **$3,284.1M**; 25%: 886.7/0.25 = **$3,546.8M**; 29%: 886.7/0.29 = **$3,057.6M**.

6. **Multiples** (market cap = EV = $2,628.904932M):
   - P/S trailing 2025 = 2,628.9/886.7 = **2.96x**
   - P/S forward 2026E = 2,628.9/1,070 = **2.46x**
   - EV/adj EBITDA 2025 = 2,628.9/218.1 = **12.05x**
   - EV/adj EBITDA 2026E = 2,628.9/275 = **9.56x**
   - P/FCF 2025 = 2,628.9/103.8 = **25.33x**
   - EV/Revenue 2025 = 2,628.9/886.7 = **2.96x** (identical to P/S trailing by the EV≈mkt-cap assumption)

7. **DCF sensitivity** — 10-yr horizon, terminal growth g = 3.5%. Growth path (yrs 1–10): +25.0%, 22.61%, 20.22%, 17.83%, 15.44%, 13.06%, 10.67%, 8.28%, 5.89%, 3.50% (linear step −2.389pp/yr). Year-1 FCF = base × 1.25 (the +25% applies **in** yr 1, per "growth starts +25% in yr1"). End-of-year discounting; TV = FCF₁₀ × 1.035/(WACC − 0.035), discounted 10 yrs. Intrinsic value = [Σ FCFₜ/(1+WACC)ᵗ + PV(TV)] ÷ 65.0M shares. FCF path, base A: 129.8, 159.1, 191.3, 225.4, 260.2, 294.1, 325.5, 352.5, 373.2, 386.3 (base B = 2.0998× each).

| WACC | Base A ($103.8M): value = PV(FCF)+PV(TV) | IV/share | vs $41.06 | Base B ($218M): value | IV/share | vs $41.06 |
|---|---|---|---|---|---|---|
| 10.0% | $1,513.3M + $2,371.4M = $3,884.7M | **$59.76** | **+45.6%** | $3,178.2M + $4,980.4M = $8,158.6M | **$125.52** | **+205.7%** |
| 11.5% | $1,401.8M + $1,682.7M = $3,084.5M | **$47.45** | **+15.6%** | $2,944.1M + $3,534.0M = $6,478.0M | **$99.66** | **+142.7%** |
| 13.0% | $1,301.7M + $1,239.8M = $2,541.4M | **$39.10** | **−4.8%** | $2,733.7M + $2,603.7M = $5,337.4M | **$82.11** | **+100.0%** |

8. **Exit-multiple check** (undiscounted spot check on FY2026E adj EBITDA × multiple ÷ 65M shares):

| Multiple | EV ($M) | Implied price | vs $41.06 |
|---|---|---|---|
| 10x | 2,750.0 | **$42.31** | **+3.0%** |
| 15x | 4,125.0 | **$63.46** | **+54.6%** |
| 20x | 5,500.0 | **$84.62** | **+106.1%** |

**Flags & caveats**
- **65.0M shares is an assumption** and is internally inconsistent with the given inputs: $41.06 × 65M = $2,668.9M ≠ given market cap $2,628.9M, which implies **64.03M** shares. Using 65M spreads the same value over ~1.5% more shares, so every per-share figure (items 7–8) is ~1.5% conservative vs the implied count. Item 6 multiples are share-count-independent.
- **Net debt ≈ $0 assumed** → EV = market cap; DCF present value is taken directly as equity value (no net-debt bridge). No dilution (options/RSUs) modeled; share count held at 65M for 10 years.
- **Interpretation choice in item 7:** Year-1 FCF = base × 1.25. Under the alternative reading (Year-1 FCF = base, +25% first applied in yr 2, declining to +3.5% by yr 10 over 9 steps), IVs are: Base A **$51.82 / $41.05 / $33.75** and Base B **$108.83 / $86.22 / $70.88** at 10%/11.5%/13% — notably, A at 11.5% ≈ exactly the current price ($41.05 vs $41.06).
- **Base B uses adj EBITDA ($218M) as an FCF base**, i.e., assumes ~100% EBITDA→FCF conversion; its values are ~2.1× Base A by construction (identical growth/discount path). "FCF" and "adj EBITDA" are company-defined non-GAAP figures.
- Terminal value is 49–61% of total DCF value across cells (highest at low WACC), so results are highly sensitive to the 3.5% terminal growth and WACC choices. Item 8 applies the multiple to **current** 2026E EBITDA undiscounted (a spot valuation check, not a future exit).
- Prior run context: FMP statements for LIME return no data (`data/lime_income_q.json` etc. are empty stubs), so no FMP figure is used anywhere above — every number traces to the external inputs plus the script.

**Reproduce:** `lime_valuation.py` in the run workspace (also `scripts/2456992fa122.py` / `scripts/316152305b1e.py` for the executed runs). Re-running it prints every table above.
