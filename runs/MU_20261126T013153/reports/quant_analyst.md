# Quant Analyst

- Symbol: MU
- Elapsed: 34.2s

---
Data collection complete. The price series reconciles exactly with the profile ($601.25 on 2026-11-25), which lets me verify the factor outputs — and three of them fail that check.

# Micron Technology (MU) — Quantitative Factor Report
**As of 2026-11-25 | Price $601.25 | Mkt cap $687B | Sector: Technology / Semiconductors**

## ⚠️ Data Integrity Warnings (read before the table)

Three tool outputs are unusable and I have overridden or flagged them:

1. **Earnings revision score is spurious.** The tool compared FY2031 consensus (`eps_estimate = 0`, an unpopulated field with 8 analysts) against FY2030 ($207.52) and produced "−100% downgrade." That is a null-value artifact, not a revision. **Revision momentum is unmeasurable** — no 3-months-prior estimate snapshot is available.
2. **Momentum score contradicts the price tape.** Tool reports 12-1 momentum of **+4.53%**; raw closes give **+168%** (Nov-25-25 $224.28 → $928.76 at the 21-day cutoff) and **−35.3%** over the last month. The price series is the internally consistent one (it reconciles to market cap and P/B), so I report both and trust the tape.
3. **TSM value data is corrupt** (P/E 1.03, EV/EBITDA −0.11). Excluded from peer medians. Also note FY2027–FY2031 estimates imply >2× revenue growth and a 73% net margin — treat as low-reliability.

## 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 8.09, EV/EBITDA 5.96, P/FCF 11.66, P/B 4.97 | **1 of 4** (86% P/E discount to peer median 63.1x) | **Strong positive** |
| **Momentum** | 12-1 +4.53% (tool) vs. **+168% raw 12M**; 1M −35.3%, 3M −35.5% | 3 of 5 | **Deteriorating / reversal** |
| **Quality** | ROE 61.4%, ROIC 69.2%, GP/assets 0.549, accruals −0.024, F-score 8/9 | **2 of 5** (behind NVDA only) | **Strong positive** |
| **Low Vol** | Ann. vol 78–92%, beta 3.25–3.53 | **5 of 5 (worst)** | **Strong negative** |
| **Earnings Revision** | Unmeasurable (tool artifact) | n/a | **Inconclusive** |

**Value detail:** MU is the cheapest name in the semi peer group by a wide margin — 8.1x earnings vs. NVDA 30.5x, AVGO 63.1x, AMD 153.2x. Top quintile.

**Quality detail:** The ROIC path (−9.9% → 2.2% → 14.1% → 69.2%) is textbook memory-cycle expansion. Quality is real but **peak-cycle**, not structural. Negative accruals (−0.024) confirm cash conversion — earnings are cash-backed, the only F-score miss is share dilution.

**Revision detail:** These are deep-future periods, exactly where the tool's EPS estimates are least reliable.

## 2. Price Statistics

| Metric | 504-day | 252-day |
|--------|---------|---------|
| Alpha (annualised) | **+99.25%** | — |
| Beta vs SPY | **3.249** | 3.526 |
| R² | **0.331** | — |
| Sharpe | **1.795** | 1.025 |
| Sortino | **2.904** | — |
| Ann. return | 141.6% | — |
| Ann. volatility | 78.9% | 91.8% |
| **Max drawdown** | **−51.0%** | −51.0% |

**Interpretation:** Alpha and Sharpe look outstanding on a 2-year window purely because it captures a 5.5× run from $181 to a $1,227 peak. **R² of 0.33 is the tell** — two-thirds of MU's variance is idiosyncratic, so this is a high-conviction single-thesis bet, not a diversifying holding. Beta of 3.25 means a 10% market decline implies a ~32% drawdown.

**The trend has broken.** From the $1,227 June-2026 close, MU is **−51%**, including **−35% in the last month alone** ($928.76 → $601.25). The 252-day Sharpe (1.025) collapsing versus the 504-day (1.795) is the signature of a live momentum crash.

## 3. Composite Quant Signal

### **NEUTRAL** (composite z ≈ 0.0), with a negative tactical skew

A mechanical equal-weight average of the five factors says **Buy**: MU wins on value (1/4) and quality (2/5). I am not endorsing that, because both factors are **cycle-peak artifacts** — an 8x P/E on record memory earnings is the classic value-trap setup, and ROIC of 69% is unsustainable in a commoditised industry. Against that, low-vol ranks dead last and momentum is in acute reversal.

The honest read: **valuation and quality are genuinely exceptional, but the price action says the market is already discounting the cycle turn.** Fair value on trailing numbers, negative risk-adjusted momentum. Not a buy until momentum stabilises; not a sell given the balance-sheet strength and F-score of 8.

## 4. Key Quant Risk Flags

- **🔴 Momentum reversal in progress.** −51% from peak, −35% in one month. Bleeding-edge of a cycle de-rating. Do not average down on the value signal alone.
- **🔴 Extreme volatility / factor crowding.** 79–92% annualised vol, beta 3.25. Correlations: TSM 0.70, AMD 0.69, SPY 0.61. This is a crowded AI-memory trade unwinding — MU has the **highest correlation to peers** in the group, so diversification within semis is illusory.
- **🔴 Low-vol factor bottom quintile** — disqualifies MU from any risk-managed or min-vol mandate.
- **🟠 Valuation may be a trap.** 8.1x P/E on peak EPS. Normalising EPS toward mid-cycle ROIC (14%) implies a far higher effective multiple.
- **🟠 Analyst targets are stale and worthless.** Range $1,250 (GS, Neutral) to $3,000 (D.A. Davidson) — posted at $1,030–1,100 vs. $601 now. 5x dispersion signals analyst confusion, not conviction.
- **🟠 Sample-size caveat.** The 504-day regression uses one cycle (n≈2 years); beta and alpha estimates are not stable through a memory downturn. FY2029–2031 consensus rests on 6–9 analysts and is statistically thin.

**Bottom line:** Cheap and high-quality on trailing data; broken and high-risk on the tape. Neutral — the numbers support owning MU *after* momentum stabilises, not during a −51% drawdown with 3.25 beta.
