# Quant Analyst

- Symbol: TTWO
- Elapsed: 62.6s

---
## TTWO — Take-Two Interactive Software, Inc.
**Quantitative Factor & Risk Report** | Sector: Technology / Electronic Gaming & Multimedia | Price ref. $213.76 (30-Apr-2026) | Mkt cap ≈ $39.6B

---

### 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 8 / 100 | Bottom decile (3rd of 3 gaming peers) | **Strongly negative** |
| **Momentum** | 15 / 100 | 3rd of 3 | **Negative** |
| **Quality** | 40 / 100 | 2nd of 3 | **Mixed / weak** |
| **Low Vol** | 65 / 100 | 2nd of 3 (1st on absolute beta) | **Positive (relative)** |
| **Earnings Revision** | 25 / 100 | n/a — thin coverage | **Downgrade (low confidence)** |
| **Composite** | **26.9 / 100** | — | **Sell** |

**Value — score 8.** P/E is not meaningful (negative earnings, −128x). P/B **10.94x**, EV/EBITDA **31.7x**, P/FCF **83.3x**. Every usable multiple sits in the most expensive bucket of the peer set. Against RBLX (P/FCF 26.3x) TTWO is ~3.2x more expensive on cash flow despite both having negative GAAP earnings. EA's multiples are null (take-private deal) and NTDOY's ADR ratios are clearly corrupted (P/E 0.14x) — **excluded as unreliable**, which thins the comparison set to two names.

**Momentum — score 15.** 12-1 month momentum **−14.04%** (252d, excl. last 21d). 3-month momentum **+2.88%** — a genuine short-term bounce off the March low, but it is a reversal inside a downtrend, not a trend. Price $213.76 sits **−19.3% below** the 52-week high of $264.79 (15-Oct-2025) and **+13.9% above** the low of $187.63 (27-Mar-2026). Three distribution days on 5–9M volume (8-Aug-25 −4%, 7-Nov-25 −8.1%, **30-Jan-26 −7.9% on 9.1M shares vs ~1.5M average**) mark repeated institutional exits.

**Quality — score 40.** The composite tool flags "low," but the components disagree and the detail matters:
- ROE **−8.49%**, ROA −3.18%, ROIC **−1.68%** — all negative, though ROIC has improved sharply from −12.43% (FY24) → −11.84% (FY25) → **−1.68% (FY26)**.
- Gross profit/assets **0.406** — solidly above the ~0.30 Novy-Marx threshold, essentially tied with RBLX (0.400).
- Accruals ratio **−9.83%** (NI −$298.2M vs OCF **+$624.3M**). Negative accruals = conservative, cash-backed earnings; the GAAP loss is driven by non-cash amortization of acquired intangibles, not cash burn.
- **Piotroski F-Score 7/9** ("Moderate"). Failures are F1 (negative ROA) and F7 (share count rising — dilution from M&A, not distress).

**Low Vol — score 65.** 252d vol **35.79%**, 504d vol **31.02%**, beta vs SPY **0.50–0.54**, max drawdown **27.7%**. Absolute beta is genuinely low. Within gaming, RBLX runs 75.2% vol / beta 1.76 / −51.6% drawdown, so TTWO is far safer. **Caveat: EA is not a valid comp** — 6.2% vol, beta −0.01, 3.3% max drawdown, Sharpe 1.60 reflect a stock pinned to a merger price, not a real risk profile.

**Earnings Revision — score 25 (LOW CONFIDENCE).** Tool reports **−19.35%** (current $9.46 vs prior $11.73) → "downgrade." **I do not trust this number.** The tool compared FY**2031** EPS ($9.46, only **4 analysts**) against FY**2030** ($11.73, 3 analysts) — different fiscal years, not a like-for-like revision, and the 2031 revenue estimate ($10.12B) is *below* 2030 ($10.26B), which is implausible. The reliable part of the estimate stack is the near-dated curve, which is *rising*: FY26 $3.91 (16 analysts) → FY27 $7.06 (11) → FY28 $10.12 (13). I have no same-period prior vintage, so the true revision direction is **unverified**; the Jan-30 gap-down suggests guidance was cut, but I cannot confirm with this data.

---

### 2. Price Statistics

| Metric | 252-day | 504-day |
|---|---|---|
| Annualised return | — | **−2.11%** |
| Annualised volatility | 35.79% | 31.02% / 31.23% |
| Beta vs SPY | **0.501** | **0.535** |
| Alpha vs SPY (annualised) | **−8.55%** | **−11.13%** |
| R² vs SPY | **0.041** | **0.048** |
| Sharpe (rf = 0%) | −0.066 | **−0.068** |
| Sortino (rf = 0%) | — | **−0.096** |
| Max drawdown | −26.41% | **−27.68%** |

**Critical caveat on alpha:** R² of **0.048** means the market explains under 5% of TTWO's return variance. The annualised alpha standard error at this residual dispersion and sample size is roughly **±21%**, giving a **t-stat of about −0.5**. The −11.1% alpha is therefore **statistically indistinguishable from zero** — do not cite it as evidence of value destruction. Equally, do not let a bull case cite a low beta as "defensive quality" when the low beta simply reflects 95% idiosyncratic, event-driven variance (GTA VI launch timing). The company-reported 5-year monthly beta of **0.929** (vs my 0.535 daily estimate) shows how unstable this parameter is.

Sortino (−0.096) is worse than Sharpe (−0.068): downside deviation exceeds total-volatility-adjusted expectation, i.e. the return distribution is **left-skewed** — losses are larger and more frequent than gains of equal size. That is the opposite of the convex, lottery-like payoff you want in a game publisher ahead of a flagship release.

---

### 3. Composite Quant Signal

> ### **SELL** — composite 26.9 / 100

Weighting (Value 20%, Momentum 25%, Quality 25%, Low Vol 10%, Revision 20%): 1.6 + 3.75 + 10.0 + 6.5 + 5.0 = **26.9**.

The bull case is entirely a single-name, forward-looking catalyst (FY27 EPS stepping from $3.91 to $7.06 on a major release slate) plus genuine cash-generation quality (negative accruals, +$624M OCF, ROIC inflecting from −12% to −2%). None of that is a *current* factor score. On every measurable cross-sectional factor the stock is expensive, in a downtrend, unprofitable on a GAAP basis, and beta-adjusted unproductive (negative Sharpe and Sortino over two years). A quantitative screen does not get to underwrite a launch date.

**What would flip this:** two consecutive positive same-period revision prints on FY27/FY28 EPS; 12-1 momentum crossing above zero; EV/EBITDA compressing under ~18x on FY27 EBITDA ($2.62B estimate implies ~15x at current EV — the closest thing to a valuation support level here).

---

### 4. Key Quant Risk Flags

1. **Estimate-revision data is methodologically broken.** The −19.35% print compares FY2031 to FY2030 estimates backed by 3–4 analysts. Any model consuming this score for TTWO is consuming noise. Coverage depth (3–5 analysts at the long end vs 16–17 near-dated) means the out-year estimates carry **no statistical significance**.
2. **Alpha and beta are statistically meaningless (R² 0.048).** Single-factor market models do not describe this stock. Event risk (launch slippage, delay announcements) dominates — and 27.7% max drawdown is the realized cost of that.
3. **Negative skew / fat left tail.** Sortino < Sharpe over both windows. Downside gaps are violent and volume-confirmed (three >7% single-day drops in 12 months). Position sizing should assume gap risk, not continuous risk.
4. **Momentum reversal risk cuts both ways.** The +2.88% 3-month reading against −14.04% 12-1 means the stock is at an inflection. If the bounce holds, momentum could flip positive within a quarter — this is the one factor with genuine upside optionality.
5. **Value factor is structurally uninformative here.** Negative GAAP earnings make P/E undefined; the meaningful metrics (EV/EBITDA 31.7x, P/FCF 83.3x) say expensive. Do not let "P/E is n/a" be read as "no valuation risk."
6. **Peer set is unusable for true cross-sectional ranking.** The sector tool returns mega-cap semis (AAPL, NVDA, MSFT) that share no economics with a game publisher; EA is merger-pinned; NTDOY's ADR ratios are corrupted. All ranks above are **3-name gaming-peer estimates, not quintile percentiles** — treat them as directional only.
7. **Liquidity is not a concern.** ~1.5–2.0M ADV ≈ $350–400M/day. No crowding or liquidity flag.

*Data gaps, stated plainly: no same-period prior estimate vintage (true revision direction unverified); no valid peer multiples for EA/NTDOY; sector rank is a 3-name approximation.*
