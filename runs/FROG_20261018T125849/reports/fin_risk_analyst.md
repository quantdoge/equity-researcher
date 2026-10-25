# Fin Risk Analyst

- Symbol: FROG
- Elapsed: 123.1s

---
## Financial Risk Assessment — JFrog Ltd. (FROG)

**Snapshot:** $84.31/share, ~$10.2B market cap, ~121.8M diluted shares. Software – Application (DevOps/Artifactory). Fiscal data through FY2025 annual (Dec-2025) plus quarterly detail through **Q2 FY2026 (Jun-2026)**.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (net-cash, effectively AAA-style balance sheet)**

FROG has essentially **no credit risk in the conventional sense**. The balance sheet is net cash and the company has no funded debt burden.

| Item (FY2025 / latest) | Value |
|---|---|
| Total debt | $19.1M (ST $5.8M + LT $6.7M — consistent with finance leases) |
| Cash & ST investments | $705.1M |
| **Net cash** | **~$686M** (6.9% of market cap; ~$5.63/share) |
| Debt/Equity | 0.02 |
| Debt/Assets | 0.01 |
| Interest expense | $0 — **interest coverage is N/A because there is no interest to cover** (a strength, not a gap) |
| Debt maturity schedule | **No refinancing cliff.** Total debt < 1 quarter of FCF |
| Cash/liabilities | 1.55 |

**No covenant risk.** With zero meaningful leverage and $176M TTM operating cash flow, there is no plausible covenant-breach or refinancing scenario. This company could survive a multi-year downturn on existing liquidity alone.

⚠️ **Tool artifact to disregard:** `net_debt_to_ebitda: 16.52` is a **sign artifact** — net debt is *negative* (−$686M) and EBITDA is *negative* (−$18M TTM). It carries no information. Similarly, the reported **Altman Z-Score of 1.353 ("Distress") is structurally misleading** here: X2 (retained earnings/assets = −0.32) is negative only because of accumulated GAAP losses funded by stock comp, and X3 is negative on GAAP EBIT. Re-running the model with market cap in X4 (10,211.6 / 453.9 = 22.5) gives **Z ≈ 13.7 — deep safe zone**. Z-score should not be used to assess this issuer.

---

### 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | TTM (Q2'26) | Assessment |
|---|---|---|---|---|---|
| Revenue ($M) | 349.9 | 428.5 | 531.8 | 600.0 | +28.7% YoY (Q2'26) — strong |
| Gross margin | 78.0% | 77.1% | 76.8% | 77.9% | Stable, inflecting up |
| Operating margin | −21.5% | −20.8% | −16.9% | −11.2% | Improving but still GAAP loss |
| Net income ($M) | −61.3 | −69.2 | −71.8 | −44.1 | **Loss every year since IPO** |
| FCF ($M) | 72.2 | 107.8 | 142.3 | 169.7 | +57% 2-yr; FCF margin 28.3% |
| **SBC ($M)** | 95.2 | 131.1 | 156.7 | **161.0** | **95% of FCF** |
| **FCF ex-SBC ($M)** | **−23.0** | **−23.3** | **−14.4** | **+8.7** | ≈ breakeven on true economics |
| Current / Quick / Cash ratio | — | — | 2.09 / 2.09 / 1.73 | — | Strong |
| Working capital | — | — | $443M | — | Strong |
| Altman Z (book) | — | — | 1.353 "Distress" | — | **Not meaningful** (see above) |
| Altman Z (mkt-cap X4) | — | — | 13.68 | — | Safe |
| **Piotroski F-Score** | — | — | **5 / 9 (Moderate)** | — | Docked for dilution (F7=0) and gross-margin erosion (F8=0) |
| FCF yield (reported) | — | — | 1.45% | **1.66%** | Thin |
| **FCF yield ex-SBC** | — | — | negative | **~0.09%** | **No cash return to shareholders** |
| EV / TTM revenue | — | — | — | **~15.9x** | No valuation cushion |

Liquidity verdict: **current ratio 2.09, cash ratio 1.73, cash runway effectively infinite** (FCF-generative, no debt). Liquidity risk is the lowest of any risk category here.

---

### 3. Market Risk Profile — **HIGH**

| Metric | 750-day window | 252-day window |
|---|---|---|
| Annualised volatility | **59.8%** | **75.8%** |
| Beta vs SPY | 1.276 | 1.36 (profile: 1.24) |
| Max drawdown | **−49.6%** | −42.2% |
| Sharpe (0% rf) | 1.17 | 0.99 |

Volatility has *risen* into the most recent year (76% vs 60%), meaning the stock is currently in a higher-risk regime than its 3-year average. A ~1.3 beta plus ~60–75% idiosyncratic vol implies that in a 20% market drawdown, beta alone implies ~−26%, and realized drawdowns of **40–50% are demonstrably recurrent** (observed twice). Risk-adjusted returns look respectable (Sharpe ~1.0–1.2) but that Sharpe is compensation for extreme variance, not evidence of a defensive profile — and it is measured against a 0% risk-free assumption, which overstates it in a positive-rate world.

---

### 4. Downside Scenario Analysis — Revenue −20%

Base case: TTM revenue $600M, 77.9% GM, opex $534M (89% of revenue), FCF $170M.

| Scenario | Revenue | Gross Profit | Operating Income | Reported FCF | FCF ex-SBC | Cash (FY25) | Solvency |
|---|---|---|---|---|---|---|---|
| **Base** | $600M | $467M | −$67M | +$170M | +$9M | $705M | — |
| **−20%, 8% opex cut** | $480M | $374M | −$118M | **+$76M** | −$72M | $705M | **No distress** |
| **−20%, no cost action** | $480M | $374M | −$160M | +$9M | −$152M | $705M | **No distress** |
| **−35% severe, 15% cuts** | $390M | $304M | −$150M | ~+$60M | −$120M | $705M | **No distress** |

**Key finding: cash solvency never comes into question.** Reported FCF is unusually resilient to a revenue shock because ~27% of revenue ($161M) is stock-based comp — a non-cash add-back. Even in the harshest modeled case the company remains cash-generative and sits on $705M+ of cash with $19M of debt. **Cash runway exceeds 10 years in every scenario, and there is no scenario in the modeled range that requires external financing.**

**The risk is transferred entirely to the equity, not the balance sheet.** In the −20% case, *true* shareholder economics (FCF net of SBC) swing from roughly breakeven to a −$72M to −$152M annual deficit, while ~5–6% annual dilution continues and the market's 15.9x EV/revenue multiple would almost certainly compress. A plausible outcome is **40–55% equity downside with zero credit event** — i.e., the risk here is valuation and dilution, not default.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Split verdict — the single most important thing to understand about FROG's risk profile is that its two risk dimensions point in opposite directions:

- **Balance-sheet / credit risk: LOW (effectively zero).** Net cash $686M, D/E 0.02, no maturities, no covenants, positive operating cash flow, current ratio 2.09.
- **Earnings-quality risk: HIGH.** Reported FCF of $170M is 95% funded by SBC; on a fully-loaded basis the company has generated roughly **$9M of true FCF on a $10.2B market cap (0.09% yield)**. GAAP operating losses have persisted every year since IPO, and the F-Score of 5 reflects dilution (F7=0) and gross-margin erosion (F8=0).
- **Market risk: HIGH.** 60–76% annualized vol, beta 1.24–1.36, two 40–50% drawdowns in three years.

Net: **Moderate financial risk** — no solvency threat whatsoever, but no margin of safety for equity holders and a proven capacity for halving in a drawdown.

---

### 6. Key Red Flags

1. **FCF quality — the dominant issue.** SBC of $161M TTM vs FCF of $170M. "FCF margin of 28%" is a stock-comp illusion. FCF ex-SBC ≈ **$8.7M**, and FCF ex-SBC yield ≈ **0.09%**. Compare to 1.66% headline FCF yield — a ~19x overstatement of true cash return.
2. **Persistent dilution.** Diluted shares: 99.2M (FY22) → 116.2M (FY25) → **121.8M (Q2'26)**. ~+5.5%/yr, ~23% cumulative since 2022. Every year of FCF generation is partly offset by share issuance; note the F-Score explicitly zeros out on "no dilution."
3. **No valuation cushion.** EV/TTM revenue ~15.9x, EV/FCF ex-SBC >1,000x. Downside protection rests entirely on future growth delivery, not current cash generation.
4. **Recurrent large drawdowns.** −49.6% (3-yr) and −42.2% (1-yr) max drawdowns; volatility accelerating (60% → 76%), suggesting the stock has recently become *more* fragile, not less.
5. **Goodwill & intangibles $411M = 46% of equity** — impairment risk if acquisitions underperform.
6. **GAAP unprofitability on a growing top line** — revenue +28.7% YoY but operating margin still −11.2%; operating leverage is improving (−20.0% → −8.1% YoY in Q2'26) but breakeven remains 3–5 quarters away at best.
7. **Mild gross-margin erosion** from 78.0% (FY23) to 76.8% (FY25), though recovering to 77.9% in Q2'26 — watch for mix/cloud-hosting cost pressure.

### Data Gaps (explicit)
- **No meaningful peer benchmarking.** The provided sector peer list returned mega-cap semiconductors/consumer electronics (NVDA, AAPL, MSFT, TSM, AVGO, MU, SKHY, AMD) — not valid comparables for a mid-cap DevOps software company. No software-application peer multiples available in this run.
- **No credit rating or CDS spread** — not applicable; FROG carries no rated debt, so these are structurally absent rather than missing.
- **Balance sheet is only available annually through FY2025.** Q2'26 cash/investments is inferred (likely ~$780–790M after ~$91M of H1'26 FCF and a small $2.0M buyback) rather than reported. FY2025 figures are used for all liquidity/leverage ratios.
- **Interest coverage is genuinely N/A** (zero interest expense), not an extraction failure.
- Beta/volatility are window-dependent (1.24 profile, 1.276 at 750d, 1.36 at 252d); treat ~1.3 as the working assumption.
