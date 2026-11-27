# Fin Risk Analyst

- Symbol: HPQ
- Elapsed: 92.6s

---
I have what I need. Two important data-quality findings before the analysis.

---

# HP Inc. (HPQ) — Financial Risk Assessment
**Price $31.15 | Market cap $28.09B | Fiscal year ends Oct 31 | Rating date: Nov 2026**

## ⚠️ Data Integrity Note (read first)
The FY2026 **annual income statement** in the feed is corrupted — it contains **Q4-only** figures mislabelled as annual. Evidence: revenue $16.0B vs $55.3B prior year (impossible), `interest_expense = 0` on $9.3B of debt, net income $769M which exactly equals Q4 net income, and diluted EPS $0.84 = Q4 EPS. The **cash flow statement annual row is clean** (each line equals the sum of four quarters: OCF 932+1,735+926+383 = $3,976M ✓; capex $791M ✓; FCF $3,185M ✓). FY2026 revenue of **$60.5B (+9.5% YoY)** and FCF of **$3.3B** are confirmed by HP's own release.

**Consequence:** the tool-computed `net_debt/EBITDA` of 2.83x and `interest_coverage` of null are artifacts of the bad row. I have rebuilt leverage and coverage from quarterly data below. Altman Z and F-Score also ingest the bad row and are only directionally usable.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade (low BBB)**

Agencies (verified, HP investor site): **Moody's Baa2 / S&P BBB / Fitch BBB+ — all Stable outlook.**

| Metric (FY2026, rebuilt) | Value | Read |
|---|---|---|
| Revenue | $60.5B (+9.5%) | Growth confirmed |
| EBITDA | ~$4.05B | Flat vs FY25 $4.09B |
| EBIT / op income | ~$3.11B | Down 14% YoY |
| **Net debt / EBITDA** | **~1.2x** | Strong for IG |
| Gross debt / EBITDA | 2.29x | Comfortable |
| **Interest coverage (EBIT/int.)** | **~7.6x** (FY25: 6.3x) | Adequate IG |
| EBITDA / interest | ~9.9x | |
| Total debt | $9,275M (FY25: $10,882M) | **−15% YoY** |
| Net debt | $4,881M (FY25: $7,192M) | **−32% YoY** |
| Cash | $4,394M | Covers ST debt **3.3x** |
| Total equity | $527M (FY25: −$346M) | Now positive, barely |
| **Tangible book equity** | **−$8,197M** | ⚠️ Entire equity is goodwill |

The deleveraging is genuine and the credit metrics are solidly investment grade. **But the equity cushion is illusory**: $527M of book equity against $8,724M of goodwill/intangibles means tangible book value is deeply negative. In any liquidation or severe impairment scenario, common equity absorbs the first dollar and is wiped out. This is why HPQ sits at the *low* end of the BBB band despite 1.2x net leverage.

**Altman Z-Score 0.226 ("distress") — I judge this a false signal, but not a harmless one.** The score is destroyed by two mechanical artifacts: x2 (retained earnings) = 0 because buybacks have depleted accumulated earnings, and x1 = −0.143 from a *deliberate* negative-working-capital model. Re-computing x4 on market cap instead of book ($28.1B/$47.0B = 0.60) lifts Z only to **~0.58** — still "distress." So even the corrected score fails, because the model cannot handle supplier-financed balance sheets. **Do not read this as bankruptcy risk; do read it as confirmation that book equity provides no protection.**

**Piotroski F-Score 6/9 (moderate).** Points lost on ROA deterioration, gross margin deterioration, and asset turnover deterioration — all three inputs are directionally correct and match the operating-margin compression I document below.

---

## 2. Key Financial Risk Metrics

| Category | Metric | Value | Assessment |
|---|---|---|---|
| **Leverage** | Net debt/EBITDA | ~1.2x | Low |
| | Debt/equity (book) | 17.6x | Meaningless — artifact of $527M book equity |
| | Debt/equity (market) | 0.33x | Low |
| | Net debt / market cap | 17.4% | Low |
| | Debt/assets | 19.5% | Moderate |
| **Coverage** | EBIT/interest | ~7.6x | Adequate |
| | EBITDA/interest | ~9.9x | Adequate |
| **Liquidity** | Current ratio | **0.81** | ⚠️ Below 1.0 |
| | Quick ratio | **0.46** | ⚠️ Weak |
| | Cash ratio | 0.12 | ⚠️ Thin |
| | Working capital | **−$6,796M** | Structural, flat YoY (FY25 −$6,805M) |
| | Cash / current liabilities | 12.5% | Relies on revolver + supplier terms |
| **Solvency scores** | Altman Z | 0.23 → ~0.58 mkt-adj | Distress zone; structural artifact |
| | Piotroski F | 6/9 | Moderate |
| **Returns** | ROA | 5.1% | |
| | Operating margin | ~5.1% (FY25 6.6%, FY24 7.1%) | ⚠️ Compressing |
| | Asset turnover (x5) | 0.34 | Low |
| **FCF** | FCF | $3,185M ($3.3B co. basis) | |
| | FCF yield | **11.1%** | Strong |
| | FCF margin | 5.3% | |
| | EV/EBITDA | ~8.1x | |

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (3y) | **42.8%** | Very high for hardware; implies ~$13 stock-price range at 1σ |
| Beta vs SPY (3y daily) | **0.97** | Profile beta 1.21 (longer window) — I report both; divergence is material |
| Max drawdown (3y) | **−51.2%** | Peak $35.93 (Nov 2024) → trough $17.52 (Feb 2026); **verified against price history** |
| Sharpe ratio | **0.18** | Poor risk-adjusted return |
| Current price vs trough | **+77.8%** | Sharp V-recovery; last day +11.5% on FY26 results + dividend increase |

**Key insight:** volatility (42.8%) is nearly double what a ~1.0 beta implies. Almost all of HPQ's risk is **idiosyncratic, not market-driven** — driven by tariff/trade shocks, memory-cost inflation, PC demand cycles, and print-supplies erosion. Beta materially understates drawdown exposure: a 51% loss occurred while the market was broadly rising. Risk models relying on beta will understate HPQ's downside by a wide margin.

---

## 4. Downside Scenario Analysis — Revenue −20%

Applying a ~19.5% gross margin and ~10% variable opex on the ~$6.0B opex base:

| | Base FY26 | −20% Revenue | −30% + margin compression |
|---|---|---|---|
| Revenue | $60.5B | $48.4B | $42.4B |
| EBITDA | $4.05B | **~$2.35B** | **~$1.2B** |
| EBIT | $3.11B | ~$1.41B | ~$0.35B |
| **Net debt/EBITDA** | 1.2x | **~2.1x** | **~4.1x** |
| **Interest coverage** | 7.6x | **~3.4x** | **~0.9x** |
| FCF (post-WC release) | $3.19B | ~$1.5–2.0B | ~$0.5–1.0B |
| Dividend ($1.1B) covered? | 2.9x | ~1.5x | **At risk** |
| Buyback ($1.2B) | Funded | **Suspended** | Suspended |

**Verdict:** HPQ **survives a 20% revenue decline without covenant breach.** Net leverage peaks ~2.1x, coverage holds ~3.4x, and $4.4B of cash plus an inventory release ($12.3B, a natural shock absorber in a downturn) bridges the gap. The dividend stays covered. The *severe* case (−30% with margin compression) pushes leverage to ~4.1x and coverage toward 1x — that is where a downgrade to BBB−/Ba1 and a dividend cut become live. Notably, inventory-heavy balance sheets are self-correcting in a downturn via working-capital release, which is HPQ's most important hidden liquidity source.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Not "Low," because the balance sheet has no equity loss-absorption capacity and liquidity ratios sit below 1.0. Not "High," because leverage is genuinely low, coverage is ~7.5x, FCF is $3.2B, debt is falling fast, and the company is investment grade. The risk is concentrated in **balance-sheet fragility and margin trajectory**, not in solvency.

## 6. Key Red Flags

1. **Negative tangible book equity (−$8.2B).** Total equity of $527M is entirely goodwill. Zero residual cushion beneath $47.0B of liabilities.
2. **Inventory +44% YoY to $12.3B** while revenue grew 9.5%. Inventory days stretched from ~70 to ~90. This is a $3.8B cash-absorption and obsolescence exposure — particularly acute given memory/component cost inflation. **Single largest new risk on the balance sheet.**
3. **Negative operating leverage.** Revenue +9.5% but operating income **−14%** and net income −4%. Growth is being bought, not earned. Operating margin has fallen three straight years (7.1% → 6.6% → ~5.1%).
4. **Liquidity below 1.0.** Current ratio 0.81, quick 0.46, working capital −$6.8B. Structural and stable, but it means HPQ is dependent on uninterrupted supplier financing and revolver access — a tail risk that amplifies exactly when credit markets tighten.
5. **Capital return consumes 73% of FCF** ($2.32B of $3.19B). This is what keeps equity near zero. A policy choice, but it removes the buffer that would otherwise exist.
6. **Refinancing cost headwind.** 10Y UST at 5.13%, 30Y at 5.47% (curve normally sloped, +39bp 2s10s — *no* recession signal). HPQ's implied coupon is ~4.4%; refinancing $9.3B at ~5.3–5.6% adds ~$90–110M/yr of interest, trimming coverage from ~7.6x to ~7.0x. Manageable, but the direction is negative.
7. **Risk metrics understate the tail.** 42.8% vol vs 0.97 beta; 51% realized drawdown during a rising market; Sharpe 0.18. Position sizing based on beta would materially misprice this.

## 7. Explicit Data Gaps

- **Debt maturity schedule by year: unavailable.** ST debt $1,320M / LT $7,955M is known, but I cannot identify a 2027–2029 refinancing wall. Cash covers ST debt 3.3x, which limits near-term concern.
- **Revolver capacity and covenant thresholds: unavailable.** Cannot test headroom against leverage or coverage covenants.
- **CDS spreads: unavailable.** No market-implied default signal.
- **Q4 FY2026 interest expense: unavailable** (`interest_expense = 0` on both annual and implied Q4 rows). Coverage is estimated from 9M actuals + run-rate.
- **Peer comparables: not usable.** The peer tool returned AAPL/MSFT/NVDA/TSM/AVGO — mega-cap semis and software, not PC/print hardware. True comps (DELL, 2354.TW Lenovo, XRX, Canon) were not returned.
- **Altman Z and Piotroski F computed on contaminated FY2026 income statement** — treat as indicative only; I rebuilt all leverage/coverage/FCF figures independently.
