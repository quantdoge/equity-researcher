# Fin Risk Analyst

- Symbol: MU
- Elapsed: 80.3s

---
## MICRON TECHNOLOGY (MU) — FINANCIAL RISK ASSESSMENT

**Data as of:** FY2026 10-K (period end 2026-09-03, filed 2026-10-09); price $788.43, market cap $892.0B; 3-yr market-risk window vs SPY.

---

### ⚠️ Data Integrity Caveat (read first)
Several inputs are anomalous and I flag them rather than silently accepting them:
- FY2026 revenue of **$133.2B is 3.56x FY2025's $37.4B**, and Q4 alone ($54.2B) is **4.0x Q1** ($13.6B). A single-year 256% revenue ramp with Q4 gross margin of **86.7%** has no precedent in memory-industry history (prior peak: 45.2% in FY2022).
- `net_debt` is inconsistent between tools: **−$38.3B** (leverage tool, = cash $43.4B − total debt $5.2B) vs **−$33.2B** (balance-sheet field). Both imply net cash; I use the conservative $33.2B in ratios and note the $5.1B gap as unexplained.
- **Gaps:** no Sortino ratio, no CDS spreads, no debt-maturity schedule or covenant terms, no customer-concentration disclosure, no segment margin detail.

Treat conclusions below as directionally valid (the balance sheet is unambiguous) but **verify margins and revenue against the primary 10-K** before relying on absolute earnings figures.

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE** (lowest IG tier)

| Agency | Rating | Outlook |
|---|---|---|
| S&P | BBB− | Stable |
| Fitch | BBB | — |
| Moody's | Baa2 (upgraded from Baa3) | Stable |

The balance sheet is effectively net-cash and near-impossible to impair: **net cash $33–38B**, total debt **$5.18B**, D/E **0.04**, debt/assets **0.03**, interest expense collapsed to **$106M** (from $477M in FY2025) giving coverage of **937x**. Debt could be retired **8.4x over** out of cash. Short-term debt is **$0** — there is **no refinancing cliff**.

Critically, the ratings sit at BBB-family despite net cash *because of cycle risk* — that is the correct read, and it is confirmed by history: FY2023 coverage was **−14.1x** (EBIT −$5.75B) and FY2024 was only **2.2x**. Current coverage is a peak-cycle artifact, not a structural attribute.

---

### 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|---|
| Revenue ($B) | 133.19 | 37.38 | 25.11 | 15.54 | +256% YoY; −49.5% in FY23 |
| Gross margin | 80.7% | 39.8% | 22.4% | **−9.1%** | Cycle range 90 pts |
| Operating margin | 74.6% | 26.4% | 5.2% | −37.0% | See §4 |
| Debt/Equity | 0.04 | 0.28 | 0.31 | 0.32 | Very strong |
| Net debt/EBITDA | **−0.35x** | 0.30x | 0.77x | 2.33x | Net cash |
| Interest coverage | 937x | 21.3x | 2.2x | **−14.1x** | Through-cycle: thin to negative |
| Current / Quick / Cash ratio | 3.31 / 2.94 / 1.58 | — | — | — | Exceptional |
| Working capital ($B) | 63.59 | 17.39 | 15.12 | 16.48 | — |
| **Altman Z-Score** | **5.13 (Safe)** | — | — | — | Book-equity basis |
| **Piotroski F-Score** | **8 / 9 (Strong)** | — | — | — | Only miss: F7 dilution |
| FCF ($B) | 58.96 | 1.67 | 0.12 | −6.12 | FCF margin 44.3% vs −39.4% |
| FCF yield | 6.55% | — | — | — | On $892B cap |
| EV/EBITDA | 7.8x | — | — | — | On peak EBITDA |
| EV/Sales | 6.4x | — | — | — | Rich for memory |
| DSO / DIO | 99 days / 147 days | 90 / 135 | 96 / 166 | — | WC absorbing $6.1B |
| ROE | 88.3% | — | — | — | Peak artifact |

Peer context: SK hynix runs D/E 0.21, net cash, coverage 51x — MU is **materially less levered than its closest memory comparable**. NVDA Z-score 6.75.

---

### 3. Market Risk Profile — **HIGH**

| Metric | Value |
|---|---|
| Annualised volatility (3y) | **72.7%** (vs market ~16%) |
| Beta vs SPY | **2.50** (profile field: 2.37) |
| Max drawdown (3y) | **45.9%** |
| Sharpe (0% rf) | 1.77 |
| Sortino | *not available — gap* |
| Implied 1-month 95% VaR | **≈ −34.5%** (≈$308B of market cap) |
| Implied 1-year 95% VaR | ≈ −120% → i.e. total-loss tail |

A 2.5 beta means a 20% market drawdown mechanically implies ~50% on MU. Realized 3-yr drawdown of 45.9% materially **understates** forward risk given that vol is 4.5x the market. The 1.77 Sharpe is not "quality" — it is the arithmetic of a vertical run-up; risk-adjusted quality here is deceptive.

Macro backdrop: 10Y at **5.13%**, 2s10s **+39bp (not inverted)** — no recession signal, but a 5%+ discount rate is hostile to a 6.4x-sales cyclical whose value sits in out-year AI capex expectations.

---

### 4. Downside Scenario Analysis — Revenue −20% (FY2026 cost structure)

Fixed/variable split: D&A $9.50B is fixed inside COGS; variable COGS ≈ 12.1% of revenue; opex $8.16B (SG&A + R&D), largely fixed.

| Scenario | Rev ($B) | GM | EBIT ($B) | Coverage | FCF | Verdict |
|---|---|---|---|---|---|---|
| **Base FY26** | 133.2 | 80.7% | 99.3 | 937x | +$59.0B | — |
| **A: −20% volume only** | 106.6 | 78.9% | 76.0 | 716x | ~+$40B | Trivial |
| **B: −20% + ASP deflation (17pt GM hit, FY2019 analog)** | 106.6 | 63.5% | 59.5 | **561x** | ~+$28B | Trivial |
| **C: −50% revenue, GM→20% (FY2023 magnitude)** | 66.6 | 20% | 5.2 | 49x | ≈ −$6B | Covenant-safe; cash covers ~7 yrs |
| **D: −60%, COGS→100% of revenue (true FY2023 form)** | 53.3 | 0% | **−8.2** | −77x | ≈ −$10.5B/yr | **$43.4B cash = ~4 yrs runway; no solvency event** |

**The decisive finding: no revenue scenario inside historical precedent threatens solvency.** Debt is $5.2B against $43.4B cash — the company can fund four years of depression-level losses without external capital. Credit risk is genuinely low.

**But the equity math is brutal.** Normalizing EBITDA to $40B (still 2.2x FY2025) at 7x → EV $280B + $38B net cash = **$318B equity, −64%**. Normalizing to $25B at 6x → **−79%**. The market is paying 6.4x *peak* sales for a business that lost $5.8B three years ago.

**Structural margin headwind not in consensus:** capex of **$30.7B vs D&A of only $9.5B** means PP&E ($63.3B) is compounding. Future D&A could triple toward $20–25B, mechanically cutting EBIT by **$12–15B annually at flat revenue** — a pure accounting drag that arrives regardless of pricing.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Decomposed, because a single label hides the real picture:

| Risk bucket | Rating | Driver |
|---|---|---|
| Credit / solvency | **LOW** | Net cash $38B, 0.04 D/E, 937x coverage, no maturity wall, IG ratings |
| Liquidity | **LOW** | Current 3.31, quick 2.94, cash ratio 1.58, $63.6B WC |
| Earnings durability | **HIGH / CRITICAL** | 80.7% GM has no precedent; 90-pt cycle range; D&A ramp |
| Market / equity risk | **HIGH** | 72.7% vol, 2.5 beta, 6.4x EV/Sales on peak EPS |

**Bottom line: this is a solvency-safe, equity-fragile business.** MU would survive a prolonged downturn comfortably — the balance sheet was rebuilt precisely to do so — but shareholders bear the full amplitude of the memory cycle at a valuation that presupposes the cycle does not turn. For a credit/liquidity mandate: no action warranted. For a market-risk mandate: position sizing, not credit analysis, is the binding constraint.

---

### 6. Key Red Flags

1. **Peak-cycle margin fragility (primary).** 80.7% gross / 74.6% operating margin is 35–90 points above every historical observation. Mean reversion is a question of *when*, not *if*, and every credit metric in §2 deteriorates mechanically when it occurs.
2. **Demonstrated negative coverage.** FY2023 delivered −14x interest coverage and −$6.1B FCF. The business can destroy cash at scale; the current cushion is new, not battle-tested across a second downcycle.
3. **Sequential growth deceleration.** QoQ revenue growth: **+75%, +74%, +31%** — momentum halving. Simultaneously DSO at 99 days and DIO at 147 days with a **$6.1B working-capital drag**. In memory, receivables/inventory build plus decelerating growth is the canonical late-cycle tell.
4. **Capex/D&A mismatch.** $30.7B capex vs $9.5B depreciation → a multi-year D&A step-up that compresses future margins independent of demand.
5. **Valuation at 6.4x EV/Sales, 7.8x peak EBITDA, 10.5x peak EPS.** Peaks earnings rarely deserve peak multiples; the combination implies 60–80% downside on normalization.
6. **Equity volatility 72.7% / beta 2.50 / 45.9% realized drawdown** — tail risk is structural, not event-driven.
7. **Data gaps to close before sizing:** FY26 revenue and margin figures are anomalous and unverified; net-debt field discrepancy of $5.1B; no covenant schedule, revolver capacity, debt maturity ladder, CDS, Sortino, or customer-concentration disclosure. Customer concentration in AI datacenter demand is the single most important unquantified exposure — it drives both the revenue ramp and its reversal.
