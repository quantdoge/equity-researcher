# Fin Risk Analyst

- Symbol: TSEM
- Elapsed: 108.9s

---
# TSEM — Tower Semiconductor Ltd. | Financial Risk Assessment

**Snapshot:** Price $133.42 (last close in feed: $128.47, 2026‑02‑20) · Market cap ~$15.1B · Net cash · FY2025 revenue $1,566.1M · Semiconductors (analog/mixed‑signal foundry), Israel
**Data vintage:** Financial statements through **FY2025** (20‑F filed 2026‑04‑30). Price/market metrics through 2026‑02‑20. Treasury curve snapshot dated 2026‑11‑17. See Data Gaps.

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE**

Tower is effectively an **unlevered, net‑cash balance sheet**. Total debt of $161.5M (ST $28.1M / LT $133.4M) against $1,151.9M of cash and short‑term investments = **net cash of ~$990M**, or ‑1.82x net debt/EBITDA. Debt is only **4.9% of assets** and **6% of equity**; equity funds 87% of the balance sheet (assets/liabilities 7.95x).

There is **no interest‑service constraint to monitor**: FY2025 interest expense was $0 (FY2024: $5.9M, implying ~31.6x EBIT coverage). Cash covers *all* debt **7.1x**, so there is no refinancing cliff — even if every maturity were called tomorrow it is self‑funded. Altman Z‑Score of **5.41 ("Safe")** is ~1.8x the safety threshold, and that score is *understated*: x2 is zero because the data feed shows retained earnings of $0 for FY2025 (FY2024: $675.5M). Restating x2 at ~0.20 lifts Z to **~5.7**.

The one credit‑quality soft spot is **cash generation, not solvency**: FCF was **‑$41.1M** in FY2025 (first negative year in five), and Piotroski is a middling **6/9**.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|
| Revenue ($M) | 1,566.1 | 1,436.1 | 1,422.7 | +9.0% y/y; 4‑yr CAGR only 1.9% |
| Gross margin | 23.2% | 23.6% | 24.8% | **Deteriorating 4 straight yrs** (27.8% FY22) |
| EBITDA ($M) | 543.5 | 451.3 | 847.3* | *FY23 inflated by ~$353M Intel break fee |
| EBIT ($M) | 240.4 | 185.0 | 589.3* | FY23 normalized EBIT ≈ $194M |
| Debt/Equity | 0.06 | 0.07 | 0.10 | Very low, deleveraging |
| Net debt/EBITDA | **‑1.82x** | ‑0.20x | ‑0.03x | Net cash |
| Interest coverage | n/m ($0 int.) | 31.6x | 132.6x | Non‑binding |
| Current ratio | **6.48** | 6.17 | 6.17 | Exceptional |
| Quick ratio | 5.51 | 5.23 | 5.15 | Inventory‑light risk |
| Cash ratio | 4.37 | 4.27 | 4.46 | — |
| Working capital ($M) | 1,445.9 | 1,475.2 | 1,432.3 | — |
| Altman Z | **5.41 Safe** (~5.7 adj.) | — | — | Insolvency risk negligible |
| Piotroski F | **6/9 Moderate** | — | — | Fails: ROA trend, dilution, GM trend |
| OCF ($M) | 395.5 | 448.7 | 676.6 | Down 42% from FY23 peak |
| Capex ($M) | 436.6 | 436.2 | 444.5 | 27.9% of revenue — structural |
| **FCF ($M)** | **‑41.1** | 12.5 | 232.1 | 5‑yr: 107→163→232→13→**‑41** |
| FCF yield / margin | ‑0.27% / ‑2.6% | — | — | Negative |

**Read‑through:** the leverage and liquidity columns are flawless; the **FCF and margin columns are the deterioration trend**. Cash conversion of earnings remains strong (OCF/NI = 1.79x, D&A‑heavy), so this is a **deliberate capex ramp** (PP&E $1,294M → $1,581M, +$287M), not working‑capital leakage — though WC was a $137M drag in FY2025 vs $50M in FY2024.

---

## 3. Market Risk Profile — **ELEVATED**

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (3y, 756d) | **70.2%** | ~4x a typical large cap; top‑decile tail risk |
| Beta vs SPY (3y regression) | **2.16** | Profile beta 0.949 → **conflict, see gaps** |
| Max drawdown (tool, 3y window) | **‑58.7%** | Visible series also shows ‑48% Feb→Apr 2025 |
| Sharpe (rf = 0%) | 1.12 | **Overstated** — at 4.74% 2Y yields excess Sharpe is materially lower |
| Sortino | n/a | Not provided |
| 14‑month price move | ~$51 → $128 (+150%) | Re‑rating, not earnings‑led (EPS $1.87 → $1.94) |

At **2.16 beta**, a 20% index drawdown mechanically implies a ~40%+ hit to TSEM before any idiosyncratic move. Valuation is the real risk vector: **68.8x P/E, 26.0x EV/EBITDA (net‑cash EV ≈ $14.2B), 9.7x sales, 5.2x book** — while FCF is negative. The stock is priced on a photonics/AI‑capacity narrative; multiple compression, not default, is the loss channel.

---

## 4. Downside Scenario: Revenue ‑20%

Model: variable COGS ≈ 57.4% of revenue (FY25 COGS less $303M D&A), D&A $303M and opex (~$86M non‑SG&A + $83M SG&A) held fixed.

| | Base FY25 | Revenue ‑20% | Revenue ‑35% |
|---|---|---|---|
| Revenue | 1,566.1 | 1,252.9 | 1,017.9 |
| Gross profit | 363.9 | ~230.6 | ~130.5 |
| EBIT | 240.4 | **~61** (‑75%) | **~44** (‑82%) |
| EBITDA | 543.5 | ~364 (‑33%) | ~347 |
| Net income | 220.5 | ~55 | ~40 |
| OCF | 395.5 | ~340 | ~325 |
| Capex (held) | 436.6 | 436.6 | 436.6 |
| **FCF** | ‑41.1 | **~‑100** | ~‑110 |
| Cash | 1,151.9 | ~1,050 | ~1,040 |
| Net cash | 990.4 | ~890 | ~880 |

**Conclusion: the balance sheet survives any plausible downturn.** At ‑35% revenue the company still holds ~$880M net cash and positive EBIT — cash runway on a ‑$110M burn exceeds 8 years, and capex is discretionary (27.9% of revenue is eminently deferrable, which cuts the burn to near zero).

**Two caveats to that comfort:**
- **Operating leverage is brutal at the EBIT line** (‑20% revenue → ‑75% EBIT) — this is a fixed‑cost foundry. My model holds D&A fixed; in reality **under‑absorption/idle‑plant charges hit COGS**, so EBITDA would fall more than the ‑33% shown. A −20% revenue scenario with utilization collapse could push EBIT to roughly breakeven.
- **Debt capacity is not free.** If management funded the announced capex program with debt at 5.13% (10Y), $1.5B of new borrowings would cost ~$77M — *above* downside EBIT of $61M. To keep 2.0x coverage in the ‑20% case, debt cannot exceed roughly **$550M**. Leverage room exists but is not unlimited at these rates.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Deliberately split:
- **Credit / solvency / liquidity risk: LOW.** Net cash, 6.5x current ratio, Z‑score 5.4, no maturity wall, no covenant exposure, interest coverage non‑binding.
- **Market / valuation / FCF risk: HIGH.** 70% vol, 2.16 beta, ‑59% historical drawdown, negative FCF, 26x EV/EBITDA on decelerating margins.
- Blended = **Moderate** — the equity is risky, the company is not.

---

## 6. Key Red Flags

1. **FCF has gone negative (‑$41M) after a 5‑year decay** ($232M → $13M → ‑$41M). Capex has consumed 28% of revenue while gross margin fell 460bp since FY2022. Growth is being bought, not earned — yet.
2. **Gross margin erosion despite 9% revenue growth** — mix/pricing or start‑up costs on new capacity. A foundry with 23% GM has thin cushion for a cyclical downturn.
3. **Capex escalating beyond the model:** post‑period disclosures reference a **~$920M capex plan**, full ownership of Fab 7 (March 2026), and authorization for **convertible debt/bonds**. This is the single most important forward risk: it converts a pristine net‑cash story into a levered one, and FCF likely stays negative through the build.
4. **Piotroski 6/9 with dilution and margin flags** — share count rose 2.2% y/y; no buyback or dividend offsets.
5. **Valuation risk dominates credit risk.** 68.8x earnings, 26x EV/EBITDA with *negative* trailing FCF. Downside is a de‑rating of 40‑60%, exactly the historical drawdown magnitude.
6. **FY2023 was flattered by the ~$353M Intel termination fee** — any 3‑year trend chart (EBITDA, ROA, margins) overstates underlying improvement and must be normalized.

**Watch items (not yet red):** utilization/under‑absorption disclosures, capex funding mix (debt vs cash), and photonics/SiPh revenue concentration.

---

### Data Gaps & Caveats
- **Net debt discrepancy:** leverage tool reports **‑$990.4M** (total debt − cash & ST investments); balance‑sheet `net_debt` field shows **‑$73.9M**. I used ‑$990.4M. The gap implies the BS field may net only a subset of debt.
- **Retained earnings = $0** in the FY2025 balance sheet feed (FY2024: $675.5M) — depresses Altman x2; adjusted Z shown.
- **Beta conflict:** tool 3y regression **2.16** vs profile **0.949**. Material — I report both and lean conservative (2.16) for stress purposes.
- **No debt maturity schedule**, no credit rating, no CDS spread available → refinancing cliff assessed via aggregate ST/LT split only.
- **No Sortino ratio**; Sharpe uses 0% risk‑free (overstates quality at ~4.7% T‑bills).
- **Statement data ends FY2025** while price data ends 2026‑02‑20 and the yield curve snapshot is dated 2026‑11‑17 — snapshots are asynchronous. Web results dated mid/late 2026 (Q3 2026 record quarter, ~$2B annualized revenue guidance, $920M capex) are **not reflected in the audited financials used above** and would, if confirmed, raise forward revenue but also extend the negative‑FCF period.
