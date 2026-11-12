# Fin Risk Analyst

- Symbol: EQX
- Elapsed: 73.3s

---
## EQX — Equinox Gold Corp. | Financial Risk Assessment
*As of Nov 12, 2026 (latest market data). Gold/silver producer — Brazil, US, Mexico, Canada. Market cap ≈ $12.1B; price $10.39.*

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (recently re-rated from Sub-Investment Grade)**

The single most important fact in this file is a balance-sheet transformation that happened *inside* the last four quarters. Total debt has fallen from **$1,552M (FY25) → $583M (Q2'26) → $510M (Q3'26)**, against $527.9M of unrestricted cash, i.e. the company is now in a **net cash position (~–$16M)**. Management reports net cash of **$164M** excluding the 2023 convertible notes redeemed after quarter-end, plus **$1.2B total liquidity** ($528M cash + $635M undrawn revolvers).

This is not cosmetic: FY2025 leverage was 1.17x net debt/EBITDA and interest expense had more than doubled YoY ($95M → $182M) on the Greenstone build + Orla combination. Twelve months later, coverage has gone from thin (2.4x) to comfortable with a net cash cushion.

- Refinancing cliff: **largely removed.** The 4.75% converts due Oct 2028 ($172.5M) were called for redemption in Sept 2026. Remaining $512M is predominantly term/bank debt against a $1.2B liquidity stack — near-term maturity wall is not a solvency issue.
- Credit rating: **no public issuer rating found in available sources (data gap).** Fundamentally the profile now screens as BB+/BBB– — low leverage, positive FCF, dividend initiated and raised 50%. An upgrade path is plausible but unverified.

**Caveat:** the improvement is ~70% operating (AISC down 4% QoQ to $2,091/oz, realized gold $4,157/oz) and ~30% shareholder-funded (Orla merger issued ~400M shares). Leverage is now low *because gold is near record highs* — that is a cyclical, not structural, safety margin.

---

### 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | Q3'26 (latest) | Read |
|---|---|---|---|---|---|
| Total debt | $945M | $1,408M | $1,552M | **$510M** | ↓↓ deleveraging |
| Net debt | $753M | $1,169M | $1,145M | **–$16M** | net cash |
| Net debt / EBITDA | 2.59x | 1.23x | **1.17x** | **≈0.0x** | very strong |
| Debt / equity | — | 0.41x | **0.27x** | **0.05x** | very strong |
| Debt / assets | — | 0.21x | **0.15x** | **0.03x** | very strong |
| Interest coverage (EBIT/int.) | 1.24x | 7.6x | **2.41x** | **≈9.2x** (TTM) | recovered |
| Current ratio | 1.74 | 1.14 | **1.56** | **0.93** | ⚠ deteriorated |
| Quick ratio | — | — | 1.27 | **0.51** | ⚠ inventory-heavy |
| Altman Z-Score | — | — | **1.198 (Distress)** | ~1.84 est. (grey) | model caveat below |
| Piotroski F-Score | — | — | **6 / 9 (Moderate)** | n/a | fails on dilution |
| FCF (annual) | –$164.8M | –$39.9M | **–$6.7M** | TTM **≈+$126M** | chronic thin FCF |
| FCF yield | — | — | **–0.1%** | **≈1.0–1.2%** | ⚠ weak |

**Altman Z caveat:** the tool's 1.198 "Distress" reading is an artifact of using *book* equity and a 2025 balance sheet pre-merger. Recomputing at Q3'26 with market capitalization: X1 = –0.01, X2 = 0.09, X3 = 0.07, X4 = 2.19 (mkt cap $12.1B / liabilities $5.54B), X5 = 0.18 → **Z ≈ 1.84 (grey zone, borderline)**. X1 and X5 are structurally low for any capital-intensive miner with $13.1B of PP&E; the Z-score is a poor discriminator here. **I do not treat it as a going-concern signal.**

---

### 3. Market Risk Profile — **HIGH**

| Metric | 3-Year | 1-Year |
|---|---|---|
| Annualised volatility | **58.5%** | **65.0%** |
| Beta vs SPY | 0.91 | **2.21** |
| Max drawdown | **–53.9%** | –54.4% (manual: $18.88 → $8.61) |
| Sharpe (rf=0) | 0.712 | **–0.408** |

- **Two beta measurements disagree materially** (0.91 3-yr vs 2.21 1-yr; vendor profile says 2.49). The recent reading is the credible one: the stock is now a high-beta gold-price proxy. Plan on **~2x market sensitivity**.
- Drawdown path is brutal and recent: peak **$18.88 (Feb 25, 2026)** → trough **$8.61 (Jul 17, 2026) = –54%**, a full retrace, then a rally to $13.98 and a slide back to **$10.39 (–45% off the high, +21% off the low)**. Around the current price the stock is a coin flip in either direction on 30-day horizons.
- Volatility of 65% means a 1-in-20 monthly move is **±30%**. Risk sizing must reflect that this is a levered bet on the gold price, not a diversified equity.
- Silver lining for long-horizon holders: 3-yr Sharpe 0.71, price $4.68 (Jan '24) → $10.39 (**+122%**).

---

### 4. Downside Scenario — Revenue –20% (gold price $4,157 → ~$3,330/oz)

Using Q3'26 run-rate economics (~1.0 Moz/yr, AISC **$2,091/oz**, cash cost $1,654/oz, revenue Q3 $1,029M, adjusted EBITDA $533M):

| Line item | Base (Q3'26 annualised) | Gold –20% | Gold –40% |
|---|---|---|---|
| Realized gold | $4,157/oz | $3,326/oz | $2,494/oz |
| Revenue | ~$4.1B | ~$3.3B | ~$2.5B |
| Margin over AISC | ~$2,066/oz | ~$1,235/oz | ~$403/oz |
| Adjusted EBITDA | ~$2.13B | **~$1.05–1.15B (–48%)** | **~$0.3B** |
| EBIT (after ~$640M D&A) | ~$1.4B | **~$450–500M** | **negative** |
| Interest coverage | ~9x | **~4x** | **< 1x (covenant stress)** |
| Net debt / EBITDA | negative (net cash) | negative / <0.5x | ~1.7x |

**Conclusion:** a 20% revenue shock is comfortably survivable — EBITDA covers interest ~4x, the balance sheet stays in net cash, the dividend ($0.09/yr) and buyback are fundable, and no covenant is remotely threatened. **The genuine break point is a ~40% gold decline (≈$2,450/oz)**, below the ~$2,200/oz all-in breakeven where FCF turns negative and coverage breaks. Note that reserves/resources, not the balance sheet, become the constraint at that level — and the model above assumes volumes hold; a grade or throughput miss at Valentine/Greenstone compounds the price shock.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Credit risk is genuinely **low** today (net cash, ~4x through a 20% price shock, no maturity wall). Market risk is **high** (65% vol, 2.2 beta, –54% drawdown in 2026). Liquidity is **adequate but deteriorating in character** (current ratio 1.56 → 0.93; working capital collapsed), and FCF quality is **weak-to-poor** across the cycle.

That mix nets to Moderate — not because solvency is in question, but because **the equity's risk is dominated by gold price and by capex-driven FCF dilution, not by the capital structure.**

---

### 6. Key Red Flags

1. **FCF is chronically negative-to-marginal.** FY22 –$501M, FY23 –$165M, FY24 –$40M, FY25 –$7M; TTM ≈ +$126M on a $12.1B market cap (**~1% FCF yield**). Capex ($640M–$700M/yr) still consumes nearly all operating cash flow, and South Railroad (first gold H1 2028) adds another call on capital. The deleveraging was funded by gold prices, not free cash flow.
2. **Massive dilution.** Diluted/weighted shares: 630M (FY25) → 1,041M (Q3'26) — **~65% increase** from the Orla combination. Piotroski F7 (no dilution) fails. Per-share value accretion is unproven.
3. **Earnings inflection already visible.** Sequential net income: $310M (Q1'26) → $231M (Q2'26) → **$62.5M (Q3'26)**, even as revenue hit a record $1.03B. Cost of revenue jumped to **66% of revenue** (vs 49% in Q1). Reported net income ($62.5M) is only 12% of *adjusted* ($199.3M) — the gap is large and unexplained in the extract.
4. **Liquidity quality, not quantity.** Current ratio fell below 1.0x (0.93) and quick ratio to 0.51 — the company is relying on revolver access ($635M undrawn) rather than working capital.
5. **Jurisdictional/operational concentration.** Mexico (Camino Rojo, Los Filos history of blockades), Nicaragua, Brazil, plus Canadian ramp-ups (Valentine, Greenstone, Musselwhite integration). Any single-asset suspension hits a 1.0 Moz base.
6. **CEO transition mid-integration** — Darren Hall retired Oct 31, 2026; Jason Simpson assumed the role Nov 1, 2026, two months into a transformational merger.

### Data Gaps (flagged explicitly)
- **No credit rating or CDS data available** — credit assessment is ratio-based only.
- **Internal inconsistency in FY2025 net income** (+$225.3M per income statement vs –$19.2M in the cash-flow statement) and a **Q4'25 revenue stub of $136.7M** that is inconsistent with FY25 revenue of $1,849.1M. TTM figures should be treated as approximate; I have leaned on FY2025 annual and 9M'26 actuals.
- **Market cap conflict:** vendor market cap $12.14B implies ~1.17B shares vs ~1.04B diluted reported; the FCF-yield tool used a stale $6.55B cap (its –0.1% FCF yield is wrong; true figure ~+1%). I used ~$12B throughout.
- FY2024 EBIT/EBITDA fields (EBIT $725M vs operating income $238M) are internally inconsistent — prior-year margin trends are unreliable.
