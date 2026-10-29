# Fin Risk Analyst

- Symbol: SKHY
- Elapsed: 65.4s

---
## SK hynix Inc. (SKHY) — Financial Risk Assessment

**Company:** SK hynix Inc. — Technology / Semiconductors (DRAM, NAND, HBM). Korea-domiciled; SEC-registered Nasdaq ADR (listing 2026-07-10). Reporting currency **KRW**; market prices **USD**. Market cap ≈ US$1.169T. 

**Data caveats up front (material):**
- **Equity price history for the ADR exists only since 2026-07-10 (~76 trading days).** All market-risk statistics below are computed on that ~3.5-month window, not 3 years. A true 3-year maximum drawdown for SKHY is **not available** from the data.
- The `calculate_fcf_yield` tool returned **2,133%** — this is a units error (KRW free cash flow ÷ USD market cap). Corrected figures are given below.
- Q2-2026 net income (KRW 93.8T) **exceeds** operating income (KRW 60.5T) by KRW 33T, and Q2 capex (KRW 10.7T) looks inconsistent with reported H1 capex increases. Treat Q2-2026 as containing one-offs / vendor-data noise. Core ratios below are anchored to **FY2025 audited annuals**.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (high quality)**

| Agency | Rating | Outlook |
|---|---|---|
| Moody's | **A3** | Stable |
| S&P Global | **A-** (upgraded from BBB+) | Positive |
| Fitch | **BBB+** (upgraded Apr-2026) | Stable |

The balance sheet transformed in 24 months. Gross debt fell from **KRW 32.5T (2023) → 24.8T (2025) → 21.1T (Q2-2026)** while equity rose from KRW 53.5T to **KRW 262.7T** (retained earnings plus the ~$26.5B Nasdaq raise). Net position is now **net cash of roughly KRW 66T** (cash + ST investments KRW 87.1T vs. total debt KRW 21.1T). Debt/assets is 6.0%.

**Conclusion: no credit deterioration, no covenant or refinancing risk.** Near-term maturities (KRW 5.9T short-term debt) are covered ~15× by cash.

---

### 2. Key Financial Risk Metrics

| Metric | FY2023 (trough) | FY2024 | FY2025 | H1/Q2-2026 |
|---|---|---|---|---|
| Revenue (KRW T) | 32.8 | 66.2 | 97.1 | 131.9 (H1) |
| Operating margin | **-23.6%** | 35.5% | 48.6% | 74.3% (H1) |
| EBITDA (KRW T) | 3.5 | 37.8 | 65.3 | ~120 (H1) |
| Debt / Equity | 0.61 | 0.34 | **0.21** | **0.08** |
| Net debt / EBITDA | 7.1× | 0.4× | **net cash** | **net cash** |
| Interest coverage (EBIT/int.) | **neg.** | 18.6× | **51.1×** | >200× |
| Current ratio | 1.45 | 1.69 | **1.86** | 2.59 |
| Quick ratio | 0.81 | 1.16 | **1.48** | 2.29 |
| Cash ratio | 0.42 | 0.57 | 0.94 | 1.44 |
| **Altman Z-Score** | — | — | **3.89 (Safe)** | — |
| **Piotroski F-Score** | — | — | **8 / 9 (Strong)** | — |
| FCF (KRW T) | **-4.0** | 13.1 | 24.8 | 73.5 (H1) |
| FCF margin | -12.4% | 19.8% | 25.5% | 55.7% (H1) |

Z-score components: X1 0.18, X2 0.61, X3 0.29, X4 2.18 (book equity basis — understated vs. market), X5 0.55. Only F-score miss is **F9 asset-turnover improvement** — expected, since the asset base is growing faster than revenue (capex ramp).

**FCF sustainability:** FY2025 FCF yield ≈ **1.5%** on market cap (KRW 24.8T ÷ ~KRW 1,650T); on annualised H1-2026 FCF (~KRW 147T) the yield is **~8–9%**. Capex is the swing factor: FY2025 capex KRW 28.6T = **29.4% of revenue**, and H1-2026 capex reportedly rose **+73% YoY**. FCF margin is strongly improving, but it is improving *because* margins are at cycle-peak, not because capital intensity is falling.

---

### 3. Market Risk Profile — **HIGH (structural), aggravated by short sample**

| Metric | Value | Note |
|---|---|---|
| Annualised volatility | **101.8%** | 365-day window, ~76 obs. |
| Beta vs SPY | **3.46** | vs. company-reported 2.39 |
| Max drawdown | **-34.6%** | Occurred within ~6 weeks of listing |
| Sharpe ratio | 0.42 | 0% risk-free assumption |
| Sortino | n/a | Not returned by tool |

Context: the ADR printed **199.87 → 126.77 (-37%)** between 9-Sep and 29-Jul-2026, then recovered to 164.70. Beta of 3.46 vs SPY means a **-20% market drawdown implies roughly -60% to -70% in SKHY**. Volatility near 100% is consistent with a leveraged, cyclical memory pure-play, but the short window probably *overstates* true long-run vol modestly while *understating* tail risk (no full cycle in the sample).

---

### 4. Downside Scenario — Revenue -20% (and a full 2023-style cycle)

**Downside economics are brutal at the margin.** Observed incremental gross margin 2023→2024 was ~97%: revenue +KRW 33.4T produced gross profit +KRW 32.4T. Costs are overwhelmingly fixed (FY2025 D&A KRW 13.9T + SG&A KRW 1.9T). That cuts both ways:

**Scenario A — Revenue -20% from FY2025 base (KRW 97.1T → 77.7T):**
- Gross profit ≈ 58.7 - ~18.5 = **~KRW 40T** (gross margin ~52%)
- EBIT ≈ **~KRW 28T**; EBITDA ≈ **~KRW 42T**
- Interest coverage ≈ **30×+**; net cash **widens** (capex would be cut)
- **Verdict: fully absorbed. No credit event conceivable.**

**Scenario B — full 2023 replay: revenue -50% (→ KRW 48.6T):**
- Gross profit ≈ KRW 8–11T; EBIT ≈ **-3T to -5T**; EBITDA still **+KRW 9–11T** (D&A)
- Interest coverage on EBITDA ≈ **60×** vs. KRW 0.9T interest
- Cash burn pre-dividend ≈ KRW 5T/yr if capex is slashed → **net cash of KRW 66T funds >10 years**
- **Verdict: survivable with no external financing.** Contrast 2023, when the same shock produced a KRW 9.1T net loss, negative FCF and net debt of 7.1× EBITDA. The company is structurally hedged to the *next* downturn.

**Breakeven revenue** (EBIT = 0): roughly **KRW 16T/yr** at current cost structure — about **6% of the 2026 annualised run-rate**. Caveat: this is a *cost* breakeven, not a *price* breakeven. Memory ASPs can fall 50–70% with volume flat, and the true risk is a simultaneous price collapse + inventory write-down (FY2023 gross margin went to -1.6%), not a volume decline. Note inventory has already built from KRW 13.3T to **KRW 18.0T** (+35%) in H1-2026.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Split the rating:
- **Solvency / credit / liquidity risk: LOW.** Net cash, 51× coverage, A-/A3/BBB+ ratings with positive momentum, Z-score 3.89, F-score 8, no refinancing cliff.
- **Earnings & market risk: HIGH.** 100% volatility, 3.46 beta, 29% capex intensity at cycle-peak revenue, single-product-cycle dependence (HBM/AI), and a demonstrated capacity for a swing of KRW 52T in operating income in 24 months (2023 -7.7T → 2025 +47.2T).

The balance sheet can survive any plausible downturn. The **equity** cannot be assumed to — that is where the risk sits.

---

### 6. Key Red Flags

1. **Cycle-peak earnings base.** FY2025–H1'26 margins (48.6% → 74.3% operating) are unprecedented and not a sustainable run-rate. Any ratio computed off this base flatters the company. 2023 is the calibration point: revenue -50%, operating margin -23.6%, net loss KRW 9.1T.
2. **Capex escalation vs. cycle timing.** Capex 29.4% of FY2025 revenue and +73% YoY in H1-2026. History says memory capex peaks coincide with margin peaks — the classic setup for post-cycle FCF disappointment. Watch the FCF margin trend for the first derivative turn.
3. **Customer/product concentration.** HBM/AI-driven (reported ~56% HBM share); revenue geared to a handful of hyperscalers/Nvidia. A single AI-capex pause passes through almost 1:1 to gross profit given ~97% marginal contribution.
4. **Inventory build.** +KRW 4.7T (+35%) in one half — the leading indicator of the last two downcycles.
5. **Severe equity tail risk.** Beta 3.46, vol ~102%, -34.6% max drawdown in the first 6 weeks of trading. Position sizing, not credit analysis, is the binding constraint here.
6. **Data integrity issues.** (a) FCF-yield tool output invalid (2,133% — KRW/USD mismatch); (b) Q2-2026 net income > operating income by KRW 33T, suggesting a one-off gain or vendor error — *unverified*; (c) Q2-2026 capex (KRW 10.7T) inconsistent with reported H1 capex growth; (d) **no 3-year price history for the ADR**, so long-horizon drawdown/Sortino unavailable; (e) no peer multiple screen or CDS spread data obtained.
7. **Geopolitical / FX.** Korea-listed, USD-traded ADR: won translation, US export controls on China fabs, and semiconductor tariff exposure are unpriced in the financials.

**Bottom line:** credit-quality risk is negligible — this is now an A-/A3 net-cash issuer that can self-fund through a repeat of its worst historical downturn. The investment risk is **entirely valuation-and-cycle risk on a 3.5-beta, 100%-vol equity priced off peak memory margins.**
