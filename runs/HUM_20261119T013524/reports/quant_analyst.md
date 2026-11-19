# Quant Analyst

- Symbol: HUM
- Elapsed: 60.2s

---
I now have the correct picture. **"Today" is 2026-11-18, HUM = $385.78** — the tool outputs are consistent with this; my first OHLCV pull simply ended at the Feb-2026 bottom. Crucially, HUM bottomed at **$173.73 (2026-02-11)** and rallied **+122%** to $461.25 before breaking down 13% on 2026-11-18. That changes every momentum and risk conclusion.

# HUM (Humana Inc.) — Quantitative Factor Report
**As of 2026-11-18 | Price $385.78 | Mkt cap $46.6B | EV $55.3B | Healthcare / Managed Care**

## 1. Factor Scores

| Factor | Score / Raw | Sector Rank (5 peer group) | Signal |
|---|---|---|---|
| **Value** | P/E 39.2 · P/B 2.63 · EV/EBITDA 19.0 · P/FCF **124.3** · FCF yld 0.8% · Div 0.92% | **5 / 5** | **Strong negative** |
| **Momentum** | 12-1 = **+84.5%**; 12-mo +66.9%; 1-mo −9.5%; −16.4% off peak | **1 / 5** | Positive, but **decelerating** |
| **Quality** | ROE 6.7% · ROIC 4.74% · GP/A 38.7% · Accruals +0.55% · F-Score 6 | **4 / 5** | **Negative** |
| **Low Vol** | Ann. vol **44.1%** · Beta 0.545 (R² 0.032) | **5 / 5** | **Strong negative** |
| **Earnings Revision** | FY30E EPS **−5.11%** (38.05 vs 40.10); n=4 analysts | **5 / 5** | **Downgrade** |

*Peer group = the 5 managed-care names in sector (UNH, ELV, CI, CVS, HUM). Peer multiples: P/E CI 12.9 / ELV 16.0 / UNH 26.5 / **HUM 39.2** / CVS 58.5. EV/EBITDA CI 8.5 / ELV 11.7 / UNH 16.0 / CVS 17.5 / **HUM 19.0** — HUM is the most expensive plan on both.*

**Note on momentum:** the `momentum_score` tool returns +14.11%, which does not reconcile with the raw tape. My own 12-1 computation (close[t−21] / close[t−252] − 1 = 426.47 / 231.09 − 1) gives **+84.5%**. Direction agrees; the tool understates magnitude. Likely the tool's window truncates at the Feb-2026 trough.

## 2. Price Statistics

| Metric | Value | Assessment |
|---|---|---|
| Alpha (ann., vs SPY) | **+103.7%** | **Not significant** — SE ≈ ±43%, t ≈ 2.4; R² = 0.032 |
| Beta | **0.545** | 95% CI ≈ 0.10–1.00 — effectively unestimated |
| R² / corr to SPY | 0.032 / 0.178 | 97% of variance is idiosyncratic |
| Sharpe | **2.39** (tool) / **1.52** (my 252d calc: 66.9% ÷ 44.1%) | Flattered by one-time re-rating |
| Sortino | **3.76** | Same caveat |
| Ann. volatility | **44.1%** | ~1.5–1.7× sector normal |
| Max drawdown | Tool 16.4% = peak-to-current ($461.25→$385.78). **True trailing-252d = −29.8%** ($231.09→$162.12); **full-period = −47.2%** ($306.91 Sep-25 → $162.12 Mar-26) | Tool's figure is a point-in-time drawdown, **not** max DD |

The tool's `annualised_return_pct` of 106.32% appears to be a *cumulative* window return mislabeled as annualized (385.78/186.98 ≈ +106%). Use the reconstructed figures above.

## 3. Composite Quant Signal: **SELL**

Four of five factors are negative, and the lone positive (momentum) is now reversing. The +122% since February is a **compression of a distressed multiple off a near-death low**, not a repeatable return stream: ROIC has fallen 13.14% → 5.67% → **4.74%** (2022→2025) while the stock re-rated to 39× earnings and **124× free cash flow**. FCF collapsed $2.98B → $2.39B → **$0.375B**, including a −$1.80B working-capital drain.

The bull case rests on analyst estimates HUM must compound 4× in two years (FY26E $9.54 → FY28E $37.81) — i.e. ¥20.5× FY27E and 10.2× FY28E if delivered. The FY30 revision was cut 5.11%, and 11 of 15 FY26 estimates' worth of coverage thins to just 4 analysts by FY30. That is a thin, low-conviction consensus.

## 4. Key Quant Risk Flags

1. **Momentum reversal underway (highest priority).** −13.0% on 2026-11-18 on 4.16M shares (~2.5× ADV) — a high-volume distribution day breaking a 9-month uptrend. 12-1 momentum is a backward-looking +84.5% that mechanically excludes this. Off −16.4% from the Nov-16 peak.
2. **Alpha and beta are statistically meaningless.** R² = 0.032 over n=252. Do not size a hedge or risk budget on beta 0.545. The reported +103.7% alpha is one idiosyncratic event, not skill-persistent.
3. **Value trap risk on FCF.** 124× P/FCF with FCF yield 0.8% and net debt/EBITDA ≈ 3.0× ($8.74B/$2.91B). Earnings quality is acceptable (accruals +0.55%) but cash conversion is the problem, not accounting.
4. **Negative estimate revision, tiny sample.** −5.11% on 4 analysts — directionally bearish but **not statistically robust**; treat as a weak signal.
5. **NOT factor-crowded** — the one genuinely favourable structural point. Correlation to UNH 0.63, ELV 0.53, CVS 0.45, CI 0.38, SPY 0.18. Low crowding means the risk is single-name idiosyncratic, not a factor unwind.
6. **Liquidity: adequate.** ~$600–800M daily dollar volume in recent sessions; no liquidity penalty.

**Sample-size caveats:** price statistics n=252 trading days (adequate for vol, inadequate for alpha/beta given R²). FY2030 revision score rests on 4 analysts. Peer ranking on 5 names is directional only — CVS's 58.5× P/E reflects depressed earnings, not richness, and inflates HUM's relative value rank.
