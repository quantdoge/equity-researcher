# Quant Analyst

- Symbol: SITM
- Elapsed: 125.3s

---
## SITM — Quantitative Factor Report
**SiTime Corp | Technology / Semiconductors | Price $378.29 (24-Nov-2026) | Mkt cap ~$9.44B (24.97M diluted sh) | Net cash ~$804M (8.5% of cap)**

**Peer set note:** The tool's default sector peers were mega-caps (AAPL, NVDA, MSFT, TSM, AVGO…), which are not valid comparables for an $11B timing-chip maker. I built a custom 6-name analog/mixed-signal set — **SITM, MPWR, ADI, TXN, MCHP, ON** — and rank within it. Ranks are therefore "x of 6," which is coarse; treat as ordinal, not quintile.

### 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|
| Value | 5 | 6 / 6 | **Very expensive** (P/E, EV/EBITDA n.m. on losses; P/FCF 272x) |
| Momentum | 10 | 6 / 6 | **Negative** (tool 12-1: −34.5%; 6-mo −48.1%) |
| Quality | 18 | 6 / 6 | **Weak** (ROE −3.7%, GP/assets 13.5%) — but F-Score 7 |
| Low Vol | 0 | 6 / 6 | **Very high risk** (vol 98%, beta 3.47, DD 60.6%) |
| Earnings Revision | 55 | 3 / 6 | **Upgrade** (+20.2%) — mid-pack, thin coverage |

**Factor detail**

- **Value:** P/E −219.9 (n.m.), P/B 8.17 (rank 4/6 — 3rd cheapest on book), EV/EBITDA −4,084 (n.m.), **P/FCF 272.2x (worst of 6)**; peers P/FCF 17.9–90.7. No dividend. Trailing P/S ≈ 28.9x. Loss-making status makes P/E and EV/EBITDA non-informative — the binding metric is P/FCF and P/S, both at the extreme.
- **Momentum:** Tool output −34.49% (negative). **Caveat:** that figure is inconsistent with the raw tape — the tool's realized history behaves like ~6-month momentum. Computed from the price series: 12-month total return **+35.3%** (279.61 → 378.29); 12-1 momentum **+83.9%** (252.76 → 464.70); 6-month **−48.1%**; 3-month **−34.9%**; 1-month **−18.6%**. All peers were measured on the same tool basis, so the *relative* rank (6/6) is valid; the absolute level is not.
- **Quality:** ROE −3.71% (6/6; peers 1.6%–30.7%), gross profit/assets 0.1352 (6/6; peers 0.158–0.367), accruals ratio **−0.1005 (2/6 — positive quality signal**, only ON better). **Piotroski F-Score 7/9 "Moderate"** — the one genuinely constructive quality datapoint. Fails on F1 (negative ROA) and F7 (dilution: shares 23.12M → 24.97M, +8.0%; ~$499M equity raise lifted equity to $1.156B despite a −$42.9M loss).
- **Low Vol:** annualised vol 97.97% (worst of 6; peers 48%–71%), beta 3.472 (worst), max drawdown 60.62% (worst; peers 23%–55%). Sharpe 0.354 is mid-pack only because of the 2026 up-leg.
- **Earnings Revision:** +20.23% (FY2028 EPS $21.81 vs $18.14 three months prior), 3 analysts — **upgrade**, but rank 3/6: TXN +36.9%, ON +32.1%, MCHP +20.0%, ADI +8.8%, MPWR +7.2%. **Not a standout.** Peer comparison is also horizon-mismatched (peers' forward periods are 2030; SITM's is 2028).

### 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (annualised, vs SPY) | **+3.56%** |
| Beta (vs SPY) | **3.49** (R² 0.3245) |
| Sharpe (252d) | **0.411** |
| Sortino (252d) | **0.758** |
| Annualised return (tool) | 40.84% |
| Annualised vol | 97.97% – 99.33% |
| Max drawdown | **−60.62%** |
| Drawdown from 11-May-26 close peak ($901.48) | **−58.0%** |
| 52-wk low ($243.68, 21-Nov-25) | price is +55.2% above |

**Correlations (252d):** SPY 0.567, MPWR 0.660, ADI 0.638, TXN 0.575, ON 0.570 — materially *below* the peer-to-peer cluster (0.74–0.87). Only 32% of variance is market-explained; ~68% is idiosyncratic. Beta of 3.5 means SPY −10% implies roughly −35% on SITM.

### 3. Composite Quant Signal

**SELL** (composite 18/100; weights: momentum 25%, value 20%, quality 20%, revision 20%, low-vol 15%)

Bottom-ranked on four of five factors. The single offsetting input — positive estimate revisions — is mid-pack versus peers and rests on 3 analysts projecting a far-out year. Alpha is positive but economically trivial against 98% vol and is statistically indistinguishable from zero (R² 0.32; no t-stat recoverable from the tool).

### 4. Key Quant Risk Flags

1. **Momentum crash in progress.** A 2026 momentum leader (≈3.2x from the Nov-25 low to the May-26 peak) now −58% off that peak and −48% in six months. Classic high-beta reversal signature; 12-1 momentum still reads +84%, so there is substantial unrealized-gain supply overhead.
2. **Factor crowding / beta amplification.** Beta 3.47 in a crowded high-beta semi trade; 11/5 intraday ranged $335–$398 (−15% swing) on 3.0M shares (6x normal). Gap risk, not liquidity risk — ADTV ≈ $180M is ample.
3. **Estimate credibility.** FY2025 consensus EPS was $2.84 vs actual **−$1.72** — a wide miss. FY2026E revenue of $906M implies **+177% y/y** on FY2025's $326.7M. The revision signal is built on a 3-analyst FY2028 number; **sample too small for significance**.
4. **GAAP vs non-GAAP gap.** SBC $103.5M = 31.7% of revenue. FCF +$34.7M, but **FCF ex-SBC ≈ −$68.8M**. The "profitability" narrative is SBC-adjusted only.
5. **Dilution.** Shares +8.0% y/y with ~$499M raised; Piotroski F7 = 0. Continued ATM issuance would erode per-share upside.
6. **Stale analyst targets.** Median $820 / mean $747 across 10 notes, but posted at $417–$797 when the stock was far higher; the two most recent are $370 (MS, 9/17) and $425 (Seaport, 11/6). Implied upside is not a usable factor input.

**Data gaps:** sector rank is a 6-name custom set (not a full industry cross-section); revision comparison is horizon-mismatched; market-cap discrepancy between profile ($11.43B) and computed ($9.44B) — I used the diluted-share figure; alpha's standard error was not returned, so significance cannot be confirmed.
