# Fin Risk Analyst

- Symbol: CRWV
- Elapsed: 69.4s

---
# CRWV — CoreWeave, Inc. | Complete Financial Risk Assessment
**Data as of Q3 2026 (period ended 30-Sep-2026), last price $58.33 (12-Nov-2026), market cap ≈ $32.1B**

---

## 1. Credit Risk Assessment — **SUB-INVESTMENT GRADE (deep junk), trending toward Distress**

CoreWeave is a levered AI-infrastructure lessor whose credit profile is driven by a single mechanical fact: **its asset base is funded ~72% by debt, its equity cushion is 4.4% of assets, and it does not yet earn an operating profit.**

| Signal | Reading | Interpretation |
|---|---|---|
| S&P credit rating | **B+** (junk) | 5 notches below IG; Fitch rates notes RR4 (average recovery) |
| Bond yields (9.625%/9.75% notes, 2031) | **~15–15.8% YTM** | Spread of roughly 1,100bp → loose LGD-based math implies **~15–20% annualised default probability**, i.e. a coin-flip-plus cumulative PD by 2031 |
| CDS | Spiked to records Oct-2026 | Credit market pricing distress, not growth |
| Altman Z (FY2025) | **−0.144 → Distress zone** | My recomputation on Q3-26 TTM data gives **Z ≈ −0.12** (book equity). Even substituting *market* cap for X4 lifts Z only to **≈0.08** — still far below the 1.81 distress threshold |
| Piotroski F-Score | **5/9** (Moderate) | Fails on negative ROA (F1) and continued dilution (F7) |

**Interest coverage is the core failure point.** TTM EBIT is **−$76M** against **$2,410M** of interest — coverage ≈ **0.0x (technically negative)**. Debt service is met from *new debt*, not from earnings. EBITDA/interest of **2.2x** looks survivable in isolation, but EBITDA is a poor proxy here because D&A is 49% of revenue: the fleet must be replaced almost as fast as it is depreciated. On a maintenance-adjusted basis, **(EBITDA − capex)/interest = −9.2x**.

**Refinancing/liquidity structure is the acute risk:**
- Short-term debt **$10.57B** vs cash **$5.59B** → current-portion shortfall of ~$5.0B
- Total current liabilities **$24.4B** vs current assets **$10.8B** → **working capital −$13.6B**
- Known paper: 9.25% 2030 ($2.0B), 9.0% 2031 ($1.75B), 9.625% 2031, 9.75% 2031 ($1.0B, priced Apr-2026), plus 2031/2032 converts (~$7.5B fair value at Jun-26)
- Debt has grown **+$36.4B in nine months** (Dec-25 $29.8B → Sep-26 $66.2B), i.e. ~$4B/month of new issuance. **This is a business that must refinance continuously; a closed capital market is an existential event, not an inconvenience.**

---

## 2. Key Financial Risk Metrics Table

| Metric | FY2023 | FY2024 | FY2025 | **TTM Q3-26** | Assessment |
|---|---|---|---|---|---|
| Revenue ($M) | 229 | 1,915 | 5,131 | **9,886** | +93% YoY; Q3-26 +168% YoY |
| EBITDA ($M) | (427) | 480 | 2,468 | **5,333** | 54% margin |
| EBIT ($M) | (530) | (383) | 14 | **(76)** | **Negative — no operating profit** |
| Net income ($M) | (594) | (863) | (1,167) | **(2,527)** | Loss widening in dollars |
| Interest expense ($M) | 28 | 361 | 1,229 | **2,410** | **24% of revenue** |
| **Interest coverage (EBIT/int.)** | n.m. | n.m. | **−0.04x** | **−0.03x** | **Critical** |
| EBITDA / interest | n.m. | 1.3x | 2.0x | **2.2x** | Thin for B+ |
| Total debt ($M) | 2,000 | 10,620 | 29,822 | **66,219** | +122% in 9M26 |
| Net debt ($M) | 1,783 | 9,259 | 25,876 | **60,692** | |
| **Net debt / EBITDA** | n.m. | 19.3x | **10.5x** | **11.4x** | Extremely high; rising |
| **Debt / equity** | n.m. | n.m. | **8.9x** | **16.5x** | Equity is a rounding error |
| Total liab. / equity | n.m. | n.m. | 13.8x | **21.7x** | |
| Equity / assets | −12.0% | −2.3% | 6.8% | **4.4%** | **A 4.4% asset writedown = negative equity** |
| Current ratio | 0.50 | 0.39 | 0.46 | **0.44** | Below 1 since inception |
| Quick ratio | 0.50 | 0.39 | 0.46 | **0.44** | No inventory to liquidate |
| Cash ratio | 0.22 | 0.27 | 0.24 | **0.23** | |
| Working capital ($M) | (496) | (3,046) | (8,952) | **(13,583)** | Structural deficit |
| Operating cash flow ($M) | 1,833 | 2,749 | 3,058 | **7,197** | Genuinely strong |
| Capex ($M) | (2,943) | (8,702) | (10,309) | **(27,618)** | 2.8x revenue growth spend |
| **Free cash flow ($M)** | (1,110) | (5,953) | (7,251) | **(20,421)** | |
| **FCF yield** | — | — | **−22.6%** (FY25) / **−63.6%** (TTM) | | Cash incinerator |
| Altman Z | — | — | **−0.14** Distress | **≈ −0.12** | Distress zone |
| Piotroski F | — | — | **5/9** | — | Moderate |

**FCF sustainability verdict: not sustainable on a stand-alone basis.** Operating cash flow is real and scaling (+$7.2B TTM), but capex is 2.8x OCF. FCF has deteriorated every single year (−$1.1B → −$6.0B → −$7.3B → −$20.4B) and the **FCF deficit is growing faster than revenue**. Self-funded cash runway = **$5.59B cash ÷ ~$5.1B quarterly burn ≈ 1.1 quarters.** Solvency is a function of capital-markets access, full stop.

---

## 3. Market Risk Profile — **Extreme**

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (252d) | **102.3%** | Roughly 6x a typical large-cap; in the top decile of listed equities |
| Beta vs SPY (252d daily) | **3.49** | A 10% market drawdown implies ~35% CRWV drawdown |
| Beta (vendor, longer window) | **7.67** | ⚠️ Discrepancy vs 3.49 — see data gaps; either reading is extreme |
| Max drawdown (252d) | **−68.4%** | Peak-to-trough Oct-25 $153.20 → Nov-26 $40.58 = **−73.5%** |
| Sharpe ratio | **−0.047** | Negative risk-adjusted return; no compensation for the vol taken |
| Sortino ratio | **Not available** | ⚠️ Data gap — cannot be computed from provided tooling |
| Current price vs peak | **−62%** | $58.33 vs $153.20 |
| Most recent stress | **−55.8% in one month** (6-Oct $91.72 → 5-Nov $40.58), then **+43% in one day** (11-Nov) | Earnings/binary-event risk |

This is a **high-beta, high-idiosyncratic-risk instrument with negative realised risk-adjusted returns**. Vol of 102% plus a 3.5–7.7 beta means CRWV is effectively a levered call option on AI capex sentiment *and* on high-yield credit spreads simultaneously. Note the Oct-2026 drawdown was explicitly credit-driven (bond yields >15%), which demonstrates the correlation the downside case depends on: **equity and credit deteriorate together.**

---

## 4. Downside Scenario Analysis — Revenue −20%

Base: FY2026 guidance midpoint **$13.15B**; −20% → **$10.52B**. A 20% revenue decline for CRWV almost certainly means **contract cancellations or repricing by concentrated hyperscaler counterparties**, so margin must compress, not hold.

| Line item | Base (FY26E) | Stress (−20% rev) | Mechanism |
|---|---|---|---|
| Revenue | 13,150 | **10,520** | Backlog haircut / cancellation |
| Gross margin | ~67% | **~60%** | Fixed power/real-estate costs deleverage |
| EBITDA margin | ~54% | **~35%** | ~95% decremental margin on lost revenue |
| EBITDA | ~7,100 | **~3,680** | |
| D&A (fixed, fleet-linked) | ~5,400 | **~5,400** | Does not flex with revenue |
| EBIT | ~1,700 | **(1,720)** | Deep operating loss |
| Interest expense | ~3,000 | **~3,400** | Higher debt + wider spreads on refi |
| **EBITDA / interest** | 2.4x | **1.08x** | **At/below likely covenant thresholds** |
| Net debt / EBITDA | ~8.5x | **~17x** | |
| Capex (if cut 50%) | 30,000 | 15,000 | Contractually committed minimums limit cuts |
| FCF | ~(20,000) | **~(13,000)** | Still massively negative |
| Equity ($M) | 4,025 | **→ negative** | |

**Three transmission channels matter more than the P&L:**

1. **Equity wipeout on a 4.4% writedown.** Assets $91.5B vs equity $4.0B. A GPU-fleet impairment of only ~$4B — trivial for hardware facing a 2–3 year obsolescence cycle in a demand air-pocket — produces **negative book equity and a technical covenant event** across asset-backed facilities. This is the single most dangerous asymmetry in the capital structure.
2. **Covenant breach → acceleration.** At EBITDA/interest of ~1.1x and net leverage ~17x, debt-service and leverage covenants on the asset-backed/term facilities come under immediate pressure. With $10.6B already in the current portion and $24.4B of current liabilities vs $5.6B cash, an acceleration is un-survivable without emergency equity or asset sales.
3. **Reflexivity.** Falling revenue → falling equity → wider spreads → higher interest → deeper losses. The 15% bond yield already prices much of this; the equity at $32B market cap is pricing recovery-value optionality, not earnings.

**Upside offset worth stating:** backlog of **$132.5B** (up 138% YoY, ~10x TTM revenue) and 4.6GW of contracted power provide real contractual visibility. A 20% revenue shock is therefore a *contract-cancellation* scenario, not a *demand-softness* scenario — less likely, but far more damaging when it happens.

---

## 5. Overall Financial Risk Rating: **CRITICAL**

| Dimension | Rating |
|---|---|
| Credit risk | **High** (B+, 15% bond yields, Z-score distress) |
| Liquidity risk | **Critical** (0.44 current ratio, −$13.6B WC, 1.1-quarter self-funded runway) |
| Leverage risk | **Critical** (11.4x net debt/EBITDA, 16.5x D/E, 4.4% equity/assets) |
| Market risk | **Critical** (102% vol, 3.5–7.7 beta, −74% drawdown) |
| FCF sustainability | **Critical** (−$20.4B TTM FCF, deteriorating every year) |
| Covenant/refinancing risk | **High–Critical** ($10.6B current maturities vs $5.6B cash) |
| Counterparty/concentration risk | **High** (see below) |

**Conclusion:** CRWV is a **solvent-on-paper, cash-flow-insolvent** enterprise whose survival depends on uninterrupted access to high-yield capital at 9–15% coupons. It is not investable on a credit basis. Equity holders retain value only under the assumption that the $132.5B backlog converts at current pricing *and* that capital markets stay open through a multi-year, tens-of-billions capex cycle. The equity is best modelled as a levered option on that joint condition, not as a going-concern earnings stream.

---

## 6. Key Red Flags

1. **Negative EBIT against $2.4B TTM interest expense — interest coverage of ~0.0x.** The company cannot service debt from operations by any conventional measure.
2. **Equity is 4.4% of assets ($4.0B vs $91.5B).** A ~4% asset writedown produces negative book equity. GPU obsolescence risk makes this a live, not theoretical, scenario.
3. **FCF deficit is accelerating: −$1.1B → −$6.0B → −$7.3B → −$20.4B.** The gap is widening faster than revenue is growing.
4. **$10.6B short-term debt and $24.4B current liabilities against $5.6B cash.** Near-term refinancing cliff requiring continuous issuance (~$4B/month of new debt added in 9M26).
5. **Bond yields of ~15–15.8% and S&P B+.** The credit market is pricing a material probability of default; CDS at records. This is the market's own risk assessment and should be weighted heavily.
6. **Customer concentration.** Microsoft was **67% of FY2025 revenue** (declining since). Backlog counterparties include loss-making AI labs (e.g. OpenAI) — revenue contracted with unprofitable counterparties carries its own credit risk that does not appear on CRWV's balance sheet.
7. **Serial dilution.** Shares outstanding 192M (2023) → 435M (FY25) → **559M diluted (Q3-26)**, +29% in nine months. Piotroski F7 failed. Per-share value is being structurally diluted to fund capex.
8. **Altman Z in distress zone under both book and market equity.** Z ≈ −0.12 (book) / ≈ +0.08 (market cap) vs a 1.81 distress threshold — no reasonable input choice avoids the distress classification.
9. **Business-model inertia.** Capex is largely committed against customer contracts and power obligations (4.6GW), limiting the ability to cut spend quickly in a downturn — the classic failure mode of over-levered infrastructure builders.
10. **Extreme market fragility.** −74% drawdown, 102% vol, and a −56%/one-month, +43%/one-day sequence. Position sizing, not fundamentals, may dominate realised returns.

---

## Data Gaps & Caveats (explicit)

- **Q3-2026 D&A is blank in the income statement** (EBITDA field shows $220M with D&A = 0); I substituted the cash-flow-statement D&A of **$1,889M**, giving EBITDA ≈ $2,096M. All TTM figures depend on this reconstruction.
- **Total debt does not reconcile to short- + long-term debt.** Q3-26: $66.2B total vs $46.9B reported ST+LTD (gap ~$19.3B); FY25 gap ~$8.0B corresponds to convertible notes. The composition of the $19.3B residual (converts, leases, ABS) is unverified — flag for the analyst.
- **Beta conflict:** 3.49 (my 252d daily calc vs SPY) vs **7.67** (vendor field). Both are extreme; I have not reconciled the window/frequency difference.
- **No Sortino ratio** and **no 3-year drawdown** — CRWV IPO'd 28-Mar-2025, so >~1.6 years of trading history does not exist. True 3Y vol/max-DD/Sharpe are not computable.
- **No covenant detail** (thresholds, headroom, springing liens) and **no year-by-year maturity schedule** obtained; maturity characterisation relies on public note terms, not the full debt footnote.
- **No valid peer comparison.** The sector-peer tool returned mega-cap Technology names (AAPL, NVDA, MSFT, AVGO) rather than neocloud/GPU-lessor comparables; no meaningful leverage or coverage benchmarking was possible.
- FY2026 guidance ($13.0–13.3B revenue) is company guidance, not audited actuals; the downside scenario is built on it and is therefore indicative.
