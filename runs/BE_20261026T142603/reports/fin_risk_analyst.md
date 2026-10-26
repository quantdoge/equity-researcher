# Fin Risk Analyst

- Symbol: BE
- Elapsed: 100.2s

---
## BLOOM ENERGY CORPORATION (BE) — Financial Risk Assessment
**As of 26 Oct 2026 | Price $200.41 | Market cap $59.2B**

---

### ⚠️ Data-Vintage Warning (material)
All pre-built ratio tools (leverage, liquidity, Z-score, F-score, FCF yield) key off **FY2025 year-end (31 Dec 2025)**. Q3 2026 results were filed **22 Oct 2026** and show a transformed company (revenue +138% YoY). I therefore **recomputed every metric on a TTM Q4'25–Q3'26 basis** using statement data. The stale tool outputs (e.g. net debt/EBITDA 26.8x, interest coverage 1.35x, Z-score 0.15, F-score 4/9) **materially overstate current credit risk** and are shown only for contrast.

---

### 1. Key Financial Risk Metrics

| Metric | Tool (FY2025) | **Recomputed TTM Q3'26** | Read |
|---|---|---|---|
| Revenue | $2.02B | **$3.83B** | +138% YoY in Q3 |
| EBITDA | $20M | **$616M** (16.1%) | Turning point |
| Net income | –$88M | **+$518M** (13.5%) | Now profitable |
| Gross margin | 29.0% | **32.3%** | Expanding |
| Debt / equity | 3.77x | **1.42x** | Deleveraging |
| **Net debt / EBITDA** | 26.8x | **0.48x** | Very low |
| Gross debt / EBITDA | — | **4.51x** | Moderate |
| Debt / assets | 0.68 | **0.42** | Improving |
| **Interest coverage (EBIT/int.)** | 1.35x | **15.9x** (EBITDA/int. 17.3x) | Strong |
| Current / quick / cash ratio | 5.98 / 4.95 / 3.93 | **3.74 / 3.07 / 1.79** | Ample |
| Net debt | $538M | **$295M** vs $2.49B cash | Negative-risk |
| **Altman Z (book equity)** | 0.148 (Distress) | **1.08** (still "distress") | ⚠️ artifact |
| **Altman Z (market-cap x4)** | — | **≈8.5 (Safe)** | See note |
| **Piotroski F-score** | 4/9 (Weak) | **~7/9 est.** | Improving |
| FCF (TTM) | $57M | **$440M** | But see §5 |
| **FCF yield** | 0.12% | **0.74%** | Extremely thin |
| EV/Sales · EV/EBITDA · P/E | — | **15.5x · 96.6x · 114x** | 🔴 See §2 |

**Z-score note (important):** The distress reading is driven entirely by **negative retained earnings (–$3.47B)** and thin book equity ($1.96B), not by cash-flow insolvency. The book-equity variant the tool uses understates x4 by ~30x. On a market-cap basis (x4 = 12.9x) Z ≈ 8.5, deep in the safe zone. **Altman is structurally unreliable for BE** — a company with $3.5B of cumulative historical losses now generating $616M EBITDA. I weight it near zero here.

---

### 2. Credit Risk Assessment: **INVESTMENT GRADE (on current metrics) — formally unrated**
Leverage (0.48x net), coverage (17.3x EBITDA/interest), liquidity ($2.49B cash, 3.74x current ratio) and the maturity wall all point to a solidly investment-grade profile. **Caveat: this is a one-year transformation** — in FY2023 BE burned $456M of FCF with negative EBITDA. A formal rating would likely lag at **BB/BB+** given earnings volatility. Rating agency opinions and CDS spreads are **not available in our data — gap flagged.**

**Maturity profile (from filings):** essentially **no maturities before mid-2029** — ~$2.2B **0% convertible notes due Nov 2030** and 3.00% green converts due Jun 2029, post the 2025 exchange. **No refinancing cliff.** Zero coupon also means interest expense is falling ($10.6M/qtr → $7.5M/qtr), self-reinforcing coverage.

---

### 3. Market Risk Profile: 🔴 **CRITICAL — this is where the risk lives**

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility | **110.2%** | ~7x market; daily ~7% swings |
| Beta vs SPY | **4.23** (measured) / 3.78 (profile) | A 10% market drop implies ~42% |
| Max drawdown (1y) | **–52.65%** | Already halved once in last 12 months |
| Sharpe (0% rf) | 0.881 | Good, but rf 4.65–4.99% (per yield curve) erodes it; return is momentum, not quality |
| Short interest | 20.98M sh / **7.1%** of float (~$4.2B) | Two-way squeeze risk |
| Diluted vs basic shares | 324.3M vs 294.8M | ~10% convert/RSU overhang |

Valuation is the dominant risk: **96.6x EV/EBITDA and 15.5x sales** on a 4.2-beta industrial. The equity is priced for flawless continued hyper-growth in AI data-center power. **Asymmetry is severe: balance sheet cannot fail, equity can.**

---

### 4. Downside Scenario Analysis (revenue –20% / –35%)

| | Base TTM | **–20% rev** | **–35% rev** |
|---|---|---|---|
| Revenue | $3,830M | $3,064M | $2,489M |
| Gross margin | 32.3% | 22–25% | ~18% |
| Gross profit | $1,238M | $674–766M | $448M |
| Opex (~fixed) | $671M | ~$637M | ~$620M |
| **Operating income** | $567M | **+$37M to +$129M** | **–$172M** |
| EBITDA | $616M | $91–183M | **–$118M** |
| Net debt/EBITDA | 0.48x | 1.6–3.2x | ~n.m. |
| **Interest coverage** | 15.9x | **1.0–3.6x** | **negative** |
| FCF | +$440M | –$100M to +$150M | ~–$300M |
| Cash runway ($2.49B) | — | no issue | **>6 yrs** (and capex cuttable) |
| Implied equity value @25x EBITDA | — | ~$54/sh (**–73%**) | impaired |

**Conclusion:** Even in a –35% revenue shock, BE **does not breach covenants, does not face a refinancing wall, and has over six years of cash runway.** Solvency risk is genuinely low. **However, the equity would be decimated** because the current price embeds ~96x EBITDA — a de-rating to 25x on –20% revenue implies a ~70%+ decline. This is an **equity-duration risk, not a credit risk.**

---

### 5. FCF Sustainability: **the weakest link**
- TTM FCF $440M looks strong but is **flattered by a $234M working-capital release in Q4'25**.
- **Q3 2026 FCF was –$181M despite net income of +$250M** — a WC drag of –$356M, inventory up $185M QoQ to $928M, capex $153M/qtr.
- **9M 2026 FCF = just $41.7M on $3.05B revenue (1.4% margin).** Cash conversion is deteriorating as growth accelerates.
- History is wildly volatile: –$456M (2023) → +$33M (2024) → +$57M (2025) → +$440M (TTM).
- **FCF yield of 0.74% is the single clearest valuation-based warning in the dataset.**

---

### 6. Overall Financial Risk Rating: **HIGH**
**Decomposed:** Balance-sheet / solvency risk = **Low**. Liquidity risk = **Low**. Refinancing risk = **Low**. Market / equity-valuation risk = **Critical**. Weighted composite for an equity investor = **HIGH**. A credit investor would see this as Moderate.

### 7. Key Red Flags
1. 🔴 **Valuation risk** — 96.6x EV/EBITDA, 15.5x sales, 114x P/E against a 4.23 beta and 110% volatility; 52.7% drawdown already occurred in the last year.
2. 🔴 **Cash conversion breakdown** — Q3'26 FCF –$181M on record profit; 9M'26 FCF $42M; inventory and receivables absorbing all earnings.
3. 🟠 **Dilution** — basic shares 240.4M → 294.8M in nine months (**+23%**); $2.2B of 2030 converts with a strike near ~$195 are **in the money** at $200, plus a 10% diluted overhang.
4. 🟠 **End-market concentration** — growth is AI data-center driven (+138% YoY); an AI capex pause is the primary downside driver and would hit a 96x multiple violently.
5. 🟠 **Earnings durability unproven** — FY2023 EBITDA was **–$135M**; only one year of genuine profitability exists.
6. 🟡 **Accumulated deficit –$3.47B**, equity/assets just 29.9%, book-to-market 3.3% — no cushion in book terms.
7. 🟡 **7.1% short interest** (~$4.2B) amplifies moves in both directions.

### 8. Explicit Data Gaps
- **No credit rating or CDS spread** available — credit assessment is purely fundamentals-derived.
- **Debt maturity schedule** derived from press releases/8-Ks, not a full maturity table; ~$121M of total debt is unexplained by ST+LT lines (likely finance leases/project debt).
- **No peer comparables** — the sector-peer tool returned mega-caps (CAT, GE, RTX, GEV) that are not meaningful comps for an early-stage fuel-cell manufacturer; **no clean peer multiple benchmarking possible.**
- **No covenant detail** (convert indentures), no revolver availability disclosure.
- Z-score and F-score recomputations for TTM are **my derivations**, not tool-native outputs.
