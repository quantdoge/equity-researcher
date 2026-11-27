# Quant Analyst

- Symbol: LRCX
- Elapsed: 76.2s

---
## LRCX — Quantitative Factor Report
*As of last close 2026-09-01: $289.89. Fiscal year ends late June.*

---

### ⚠️ DATA INTEGRITY WARNING — read before using the scores

Three vendor tools returned values that conflict materially with the raw OHLCV series. I verified each against the price file:

| Metric | Vendor tool | Re-derived from raw OHLCV | Verdict |
|---|---|---|---|
| 12-1 momentum | **−22.51%** | **≈ +201%** (Aug-25 $97.76 → Aug-26 $294.30) | Vendor wrong |
| Trailing 12M return | −0.43% | **+191.4%** | Vendor wrong |
| Annualised alpha | **−31.19%** | **≈ +127%** (realised 191% vs β·SPY 64%) | Vendor wrong (sign) |
| Sharpe | −0.006 | **≈ +2.5** | Vendor wrong |
| Max drawdown | −57.66% | **−41.8%** (close basis); −42.9% intraday | Vendor overstated |
| Current price | $185.01 | **$289.89** | Conflict — see below |

**Root cause:** the vendor's price feed for LRCX ends at **$185.01**, while the OHLCV file ends at **$289.89**. That 36% gap propagates through every price-dependent tool. Confirmation: vendor P/E 32.12 ÷ EPS $5.76 = exactly $185.01 — the EPS ties out perfectly, so only the price level is in dispute. Momentum works fine on peers (MU = +4.53%), so this is LRCX-specific.

**Consequence:** every multiple below is shown *as-computed* and then **restated at the $289.89 close**. The restated column is what the market is actually paying.

---

### 1. Factor Scores

| Factor | Score / Raw Inputs | Sector Rank (of 5 semis) | Signal |
|---|---|---|---|
| **Value** | P/E 32.1 **(50.3 restated)**; EV/EBITDA 26.6 **(41.8)**; P/FCF 47.7 **(74.7)**; P/B 18.7 **(29.3)**; div yield 0.64% | **4th** as-computed / **5th** restated | **Negative** |
| **Momentum (12-1)** | **+201%** (vendor −22.5% invalid) | **1st** (MU +4.5%) | **Strong Positive** |
| **Quality** | ROE 58.3%; ROIC 49.4%; GP/Assets 0.498; Piotroski **8/9**; accruals **+5.98%** | **3rd** | **Positive, accruals-capped** |
| **Low Vol** | Vol 75.2%; β 3.29; R² 0.49 | **5th** | **Strong Negative** |
| **Earnings Revision** | +19.24% — **artefact, see note** | n/a | **Unusable** |

**Value detail** — peers: MU 8.1x P/E / 6.0x EV/EBITDA (cheapest); NVDA 30.5x; **LRCX 32.1x (50.3x restated)**; AVGO 63.1x / 43.5x. LRCX is expensive in absolute terms and cheap only against AVGO. On the restated 50x trailing / 30x FY27E, value is bottom-quintile.

**Quality detail** — the tool's `"low"` label is triggered *solely* by accruals (5.98% vs the 0.05 threshold) and contradicts its own profitability inputs. Fundamental quality is genuinely elite and **improving** every year:
- ROIC: 31.5% → 40.4% → **49.4%** (FY24→FY26)
- Gross margin: 47.3% → 48.7% → **50.5%**
- Operating margin: 28.6% → 32.0% → **35.3%**
- Diluted EPS: $2.90 → $4.15 → **$5.76** (+38.8% YoY); revenue +26.0% to $23.23B

F-Score 8/9, with the single miss being the accruals test (F4=0) — same finding as the quality tool. ROE is flattered by a thin book (BVPS $9.89, P/B 29x restated).

**Earnings revision — DISCARD.** The tool reports +19.24%, but its `prior_eps_estimate` of **15.657 is numerically identical to the FY2030 consensus (15.65732)**. It compared FY2031 ($18.67) against FY2030 ($15.66) — i.e. it measured *one year of growth*, not a revision of the same period. No genuine revision signal exists here. Separately, the far-dated estimates are thin (6–7 analysts for FY2030/31 vs 21 for FY2027) and should be discounted heavily. Only FY2027E **$9.66** (21 analysts) is high-confidence.

---

### 2. Price Statistics

| Statistic | Vendor | Re-derived | Note |
|---|---|---|---|
| Beta vs SPY | 3.29–3.31 | ~3.3 | **Coherent — accept.** 3–4x amplification on SPY down-days |
| R² vs SPY | 0.49 | — | Half the variance is idiosyncratic |
| Annualised vol | 75.2% | ~73% (monthly) | **Accept**, but regime-driven (see below) |
| Alpha (annualised) | −31.19% | **≈ +127%** | Vendor sign is wrong |
| Sharpe | −0.006 | **≈ +2.5** | Return input corrupted |
| Sortino | −0.009 | **Not reproducible** | Needs full daily downside series |
| Max drawdown | −57.66% | **−41.8%** | Peak $432.87 (6/30/26) → trough $252.08 (7/29/26) |
| Current vs peak | — | **−33.0%** off high | $289.89 vs $432.87 |

**Volatility caveat:** the 75% vol is real but is a *regime break*, not a stable characteristic. From Aug-24 to Aug-25 the stock traced a normal ~35–40% vol path ($81→$99). From Sep-25 onward monthly returns swung from +38% to −32%. Beta 3.3 on a 75% vol name is a **balance-sheet-sized risk**, not a stock-specific one.

---

### 3. Composite Quant Signal: **NEUTRAL**

Two strongly positive factors (Momentum, Quality) offset by two strongly negative (Value, Low-Vol), with the fifth unusable.

- **Bull case:** the sector's #1 momentum name (+201% 12-1) paired with genuinely expanding, top-tier returns on capital (ROIC 49.4%, rising 3 straight years), F-Score 8, and EPS +39% YoY. Quality and momentum are the two best-documented return premia, and LRCX screens top-tercile on both.
- **Bear case:** you pay 50x trailing / 30x forward for it, and the price has already fallen 33% from its June peak. On any composite that includes value or risk-weighting, LRCX is bottom-quintile. The momentum is *decaying* — 12-1 is positive only because of gains booked six months ago.

I do not upgrade to Buy because the momentum strength is stale and the low-vol score is disqualifying for a risk-parity or vol-targeted sleeve. I do not downgrade to Sell because the operating quality is verifiable and improving, which is the harder thing to fake.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** The +201% 12-1 reading is entirely backward-looking. The stock is −33% from the 6/30 peak and −8.7% over the last 21 sessions. The 12-1 signal is now being *paid for* by a broken short-term trend. This is the textbook setup for momentum crash.
2. **Factor crowding — HIGH.** LRCX shares the crowded "AI-capex semiconductor" trade with NVDA/AVGO/MU. Beta 3.3 means the whole complex is one macro print away from a synchronized drawdown.
3. **Valuation fragility.** At the restated 289.89 close: 50x trailing earnings, 42x EV/EBITDA, 75x P/FCF. P/FCF is the standout warning — free cash flow conversion lags reported earnings (accruals +5.98%), so 75x cash flow is a demanding ask.
4. **Earnings quality — MODERATE.** Accruals ratio +5.98% exceeds the 5% flag; net income is running ahead of operating cash flow. Both the quality factor and the F-Score independently caught this. Not a red flag on its own, but it weakens the "high quality" case and is the item I would interrogate first in the financials.
5. **Liquidity — LOW RISK.** ~$300 price, 4–22M shares/day, ~$365B market cap. No capacity constraint.
6. **Sample-size / data caveats.** 252-day window only (~1 year); the vol/beta estimates straddle an abnormal regime and are unstable. Analyst coverage on FY2030–31 estimates is 6–7 names — statistically thin. **The vendor momentum, alpha, Sharpe, Sortino and max-drawdown figures for LRCX should not be used in the memo; use the re-derived values.** I recommend confirming the true current price ($185 vs $290) before publishing any multiple, as this single input moves the P/E by 18 points.
