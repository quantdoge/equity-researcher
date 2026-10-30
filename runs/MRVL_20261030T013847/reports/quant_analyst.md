# Quant Analyst

- Symbol: MRVL
- Elapsed: 53.2s

---
# MRVL — Quantitative Factor Report
**Price $218.34 | Mkt cap $191.2B | Semiconductors | Data as of 2026-10-29**

---

## 1. Factor Scores

| Factor | Score / Raw | Sector Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | P/E 71.1, EV/EBITDA 42.3, P/FCF 136.0, P/B 13.3 | **3 / 5** (~50th pct) | Neutral |
| **Momentum (12-1)** | **+27.06%** | **1 / 5** (top) | Strong Positive |
| **Quality** | ROE 18.7%, GP/A 0.188, Accruals +4.13% | **5 / 5** (bottom) | Negative |
| **Low Vol** | Vol 87.7%, Beta 3.40, MaxDD −48.35% | **5 / 5** (bottom) | Strong Negative |
| **Earnings Revision** | +53.0% (see caveat) | **1 / 5** (top) | Positive — *low confidence* |

**Peer raw data (semis comp set)**

| | P/E | EV/EBITDA | P/FCF | ROE | GP/A | Accruals | Vol | Beta | 12-1 Mom | Rev. |
|---|---|---|---|---|---|---|---|---|---|---|
| **MRVL** | 71.1 | 42.3 | 136.0 | 18.7 | 0.188 | **+4.1%** | **87.7%** | **3.40** | **+27.1%** | **+53.0%** |
| NVDA | 43.6 | 35.9 | 54.2 | 76.3 | 0.742 | +8.4% | 37.9% | 1.91 | +9.0% | +3.9% |
| AVGO | 72.3 | 49.6 | 62.2 | 28.5 | 0.253 | −2.6% | 44.7% | 2.08 | −13.2% | +4.6% |
| AMD | 213.7 | 126.5 | 137.6 | 6.9 | 0.223 | −4.4% | 71.8% | 3.41 | +11.5% | +39.4% |
| MU | 12.6 | 9.5 | 18.1 | 61.4 | 0.549 | −2.4% | 84.2% | 3.33 | +14.4% | +22.7% |

MRVL is the **only name in the group with positive accruals** and the **worst gross-profit-to-assets**. It is mid-pack on value (cheaper than AVGO/AMD on EV/EBITDA, far more expensive than MU/NVDA).

## 2. Price Statistics (252 trading days)

| Metric | Value |
|---|---|
| Annualised return | **+176.59%** |
| Annualised volatility | 89.19% (calc) / 87.66% (vol tool — consistent) |
| Beta vs SPY | **3.416** (R² = 0.253) |
| Alpha (annualised) | **+106.0%** — t ≈ 21, statistically significant *in-sample* |
| Sharpe | **1.98** |
| Sortino | **3.24** |
| Max drawdown | **−48.35%** (peak close $316.28 on 2026‑06‑04 → $163.36 on 2026‑07‑29) |
| Drawdown from June peak to today | **−31.0%** |
| Last 21 trading days | **−17.3%** ($264.15 → $218.34) |
| ADV | ~20–40M sh (~$5–8B/day) — no liquidity issue |

Alpha is real but **conditional on a 3.4-beta AI-semiconductor melt-up**; 75% of return variance is idiosyncratic, so the intercept absorbs sector beta rather than skill.

## 3. Composite Quant Signal: **NEUTRAL**

Two top-ranked factors (momentum #1, revisions #1) offset by two bottom-ranked (quality #5, low-vol #5) and mid-pack value. This is a **high-beta momentum/revision vehicle, not a quality or value holding.** The 12-1 momentum is a lagging read: the stock has already broken down −17.3% in the last month, so the momentum factor is pointing at a door the price has already walked through.

Cross-sectional composite (equal-weight z-scores): **≈ 0.0** → Neutral. A momentum-tilted long is defensible only with tight stop discipline; it does not qualify as a core factor position.

## 4. Key Quant Risk Flags

1. **Momentum reversal in progress** — 12-1 = +27% but 1-month = −17.3%, −31% off the June peak. Classic momentum-crash signature (long-duration crowded winner unwinding). Highest-priority flag.
2. **Earnings-revision score is contaminated — treat +53% as low confidence.** The tool measured the **FY2031** estimate (5 years out, only **10 analysts**) vs 3 months prior. Near-term FY2026/FY2027 consensus is extremely tight (EPS $2.845 ±0.025; $4.215 ±0.055), meaning **near-term revision momentum is effectively flat/unknown**. The +53% is a long-horizon forecast extrapolation, not a revision cycle.
3. **Quality deterioration** — ROIC **7.01%** vs ROE 18.66% (ROE levelled up by leverage/intangibles); accruals flipped from −12.7% (FY25) to **+4.13%** (FY26); Piotroski **F-score 6** with F4 (accruals) = 0, F5 (leverage) = 0, **F7 (dilution) = 0** — 869.7M diluted shares rising. Cash conversion weak: NI $2.67B vs OCF $1.75B.
4. **Factor crowding / correlation** — 0.54 with AVGO, 0.57 AMD, 0.55 MU, 0.50 SPY. Adds no diversification to a semis book; at beta 3.4 it is a leveraged sector bet.
5. **Valuation requires heroic extrapolation** — 136x P/FCF. The consensus path needs revenue to go from $8.2B (FY26) to **$75.0B (FY31)** and EPS from $2.84 to $28.26. Forward P/E ladder: 51.8x FY27, 30.0x FY28, 17.6x FY29. Any AI-capex deceleration compresses the multiple before the earnings arrive.
6. **Stale analyst targets** — 10 targets raised Oct 7, 2026 at $280–287 (median ~$350); price is now $218.34. Upside implied ~+60%, but the notes predate the −24% move and are not fresh information.

**Sample-size caveats:** cross-sectional ranks use n=5 peers — directional only, not statistically robust. Regression n=252 with adequate power, but R²=0.25 means beta/alpha estimates are unstable and the alpha is not separable from sector factor exposure. Peer-level earnings-revision comparison is apples-to-oranges because each peer's tool call resolved to a different forward year (FY30–FY31).

**Verdict:** Neutral. The statistically defensible statement is that MRVL is the peer group's best momentum and worst quality/low-vol name, priced for flawless long-horizon execution, currently in a momentum drawdown. I would not add on the momentum factor alone; a re-entry case requires the accruals/ROIC deterioration to reverse and the 1-month return series to stabilise.
