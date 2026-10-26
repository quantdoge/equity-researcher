# Quant Analyst

- Symbol: CCI
- Elapsed: 65.9s

---
## CCI (Crown Castle Inc.) — Quantitative Factor & Risk Report
**Sector:** Real Estate / REIT – Specialty (towers & fiber) · **Price $88.17** · **Mkt cap $38.5B** · **EV ~$67.9B** · **Div yield 4.81%**
**As-of window:** ~Oct 2025 – Oct 2026 (252 trading days); fundamentals FY2025A (filed 2026-02-23)

### 1. Factor Scores Table

Sector ranks computed against a **5-name specialty-REIT / comm-infrastructure comp set** (CCI, AMT, SBAC, DLR, EQIX). ⚠️ The platform's `rank_universe_by_factor` **ignored the supplied universe** and ranked the default mega-cap top-25 (AAPL/META/NVDA…), so I rebuilt ranks from direct peer calls. n=5 is coarse — treat percentiles as ±1 slot.

| Factor | Score (raw) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 86.6 · EV/EBITDA 24.5 · P/FCF **13.4** · P/B n/a (BVPS **–$3.74**) | **3 / 5** (~40th pct) | Neutral / mixed |
| **Momentum** | 12-1 return **–14.0%** (AMT –1.2, SBAC –11.4, EQIX –0.4, DLR +2.6) | **5 / 5** (bottom quintile) | **Bearish** |
| **Quality** | ROE **–27.2%** · GP/Assets **0.089** · Accruals **–0.083** · F-score **4/9** | **4 / 5** (~20th pct) | **Bearish** |
| **Low Vol** | σ 38.2% · β 0.047 (broken) · MaxDD **–28.2%** vs peers –14% to –16% | **4 / 5** (2nd highest vol) | **Bearish** |
| **Earnings Revision** | Forward EPS est. **+5.4%** (3.43 vs 3.26) | 2 / 2 (AMT +12.3%) | Mild positive — **low confidence** |

**Value — the one genuine positive, but it's an artifact-rich signal.** CCI's P/FCF of 13.4x is *far* the cheapest in the group (SBAC 18.9, AMT 23.6, DLR 25.2). Conversely P/E 86.6x is the most expensive and P/B is undefined because shareholders' equity is **negative**. On EV/EBITDA (24.5x trailing) it is the priciest of the five; on 2027E EBITDA of $3.04B it is ~22.3x — essentially in line with AMT (21.75x). **Verdict: not expensive on cash flow, not cheap on EBITDA — a true neutral.**

**Quality rank is distorted but directionally right.** Accruals of –8.3% appear excellent, but that is driven by the ~$2.6B fiber impairment flow-through, not clean earnings. ROE is negative purely because equity is negative; ROA 1.41% and ROIC 7.44% are the honest measures, and both are below AMT. F-score 4/9 (profitability 4/4, but leverage, dilution, margin and turnover all fail). Recovering from –9.97% ROIC in 2024, but below the 6.7–6.9% of 2022-23 on a shrinking asset base.

**Momentum is the cleanest signal.** –14.0% on 12-1, worst of the five comps, with the tower cohort broadly negative — this is both stock-specific and sector momentum drag. No reversal precursor visible.

**Revision signal should be discounted.** The tool compares the FY**2030** estimate ($3.43, only **5 analysts**, range 3.37–3.50) against $3.255 — a value that is coincidentally identical to the FY**2029** estimate, suggesting a period-mismatch artifact rather than a true 3-month revision. Countervailing hard evidence: **consensus price targets have collapsed** — UBS $127 (Dec-25) → KeyBanc $115 (Jan-26) → BMO $91 (Feb) → Goldman $95 (Jun) → Barclays $84 → Morgan Stanley $85 → BMO $93 (Oct-26). Median ≈ **$93 vs price $88.17 → ~5% upside**. Ratings cluster at Equal-Weight/Neutral. I read this as **flat-to-negative revision momentum**, not the reported upgrade.

### 2. Price Statistics

| Metric | Value | Assessment |
|---|---|---|
| Annualised return (252d) | **+14.53%** | Decent absolute |
| Annualised volatility | **38.66%** (38.22% alt calc) | Very high — ~2x a typical REIT |
| **Sharpe (rf=0)** | **0.376** | Weak; at rf≈4% → **~0.27** |
| **Sortino (rf=0)** | **0.629** | Poor downside capture; Sortino/Sharpe 1.67 |
| Max drawdown | **–28.19%** | vs AMT –15.7%, DLR –15.0%, EQIX –14.2% |
| Alpha (ann., vs SPY) | **+13.54%** | **Statistically meaningless** |
| **Beta (vs SPY)** | **0.047**, R² **0.0003** | **Broken — do not use** |

**Critical data-integrity flag on beta/alpha.** A beta of 0.047 with R² = 0.0003 is not economically possible for a $38.5B REIT: the company profile and every third-party source put CCI's beta at **~0.96**. The R² implies the market explains *0.03%* of CCI's variance, so the +13.54% "alpha" is pure regression noise (t-stat ≈ 0) — it must **not** be cited as evidence of outperformance. The defect is systematic across the feed (AMT returns a **negative** beta of –0.162, which is equally impossible), pointing to a date-alignment failure between the stock and benchmark series. **Recommendation: re-estimate on monthly returns or 2-year weekly windows before using beta for cost of equity or hedging.** For risk purposes use **β ≈ 0.96**, which with 38.7% vol implies only ~15% of total risk is market-driven — i.e. ~85% is idiosyncratic/single-name, consistent with the 28% drawdown occurring with essentially no market beta.

Sanity check on volatility: 38.2% is high but *is* corroborated by peer data (SBAC 39.6%), so I accept the vol figure. Only the beta/alpha/correlation estimates are unreliable.

### 3. Composite Quant Signal: **NEUTRAL** (Sell tilt)

| Factor | Weight | Score (quintile) | Contribution |
|---|---|---|---|
| Value | 30% | 3/5 | 0.0 |
| Momentum | 25% | 5/5 (worst) | **–1.0** |
| Quality | 20% | 4/5 | –0.6 |
| Low Vol | 15% | 4/5 | –0.5 |
| Revision | 10% | weak positive | +0.2 |
| **Composite** | | | **≈ –0.3σ** |

Four of five factors sit below the sector median, which on a mechanical screen argues Sell. I stop at **Neutral** for two reasons: (a) the value and quality scores are *structurally corrupted* by the fiber divestiture — 2025 revenue fell 35% YoY ($6.57B → $4.27B), net income turned positive but remains depressed at $444M, equity is negative, so any P/E/ROE/book-based z-score is measuring accounting transition, not economics; and (b) the stock is genuinely **not expensive on cash flow** (P/FCF 13.4x cheapest in group, 4.81% yield ~65% covered by FCF) and EV/EBITDA on 2027E is in line with AMT. A Sell needs expensive-or-deteriorating; CCI is *cheap-but-broken-momentum*. **Upgrade trigger:** 12-1 momentum back above –5% with FY2027 EPS revisions positive. **Downgrade trigger:** any further consensus target cuts below $85, or 2027E EBITDA revised below $2.9B.

### 4. Key Quant Risk Flags

1. **Beta/alpha estimate is invalid (highest priority).** β = 0.047, R² = 0.0003, and a sister-stock negative beta confirm a data-alignment bug. The reported +13.5% alpha is noise. Do not feed this into any risk model.
2. **Momentum reversal / continuation risk.** Bottom-quintile 12-1 (–14.0%), worst in the tower cohort, and the *loss* is recent (momentum worse than the 252-day total return implies). No bottoming pattern; expect continuation absent a catalyst.
3. **Idiosyncratic risk concentration, not factor crowding.** With β≈0.96 explaining ~15% of variance, CCI is a **single-name bet on tower leasing + leverage**, not a market proxy. Max drawdown 28.2% is ~1.8x peers — position sizing should reflect this, not the group beta.
4. **Rate/duration sensitivity.** 4.81% dividend yield + $67.9B EV against $959M annual interest expense → highly levered, duration-sensitive; the 38% vol is largely a rate/long-duration artifact. Peer correlations with AMT/SBAC are the crowding vector to monitor.
5. **Fundamental distortion window.** Negative book value (–$3.74/sh), P/E 86.6x on transitional earnings, F-score 4/9, ROE –27.2%. Factor models are **mis-specified on CCI for 2025-26**; use P/FFO and AFFO payout, not P/E or P/B. Confirm the go-forward tower-only EBITDA base before trusting any multiple.
6. **Estimate-revision signal is unreliable.** FY2030, n=5 analysts, and a suspected period-mismatch (prior value equals the FY2029 consensus). Weight the *negative* price-target trajectory instead.
7. **Liquidity: not a flag.** ~3M shares/day, $38.5B cap — no capacity constraints.

**Sample-size caveats:** sector ranks rest on n=5 comps (percentile resolution ±1 slot); the beta regression has effectively zero explanatory power (R²=0.0003) and is unusable; the revision signal uses 5 analyst estimates on a period 4 years out. Only volatility, drawdown, momentum and the raw multiple cross-section are statistically trustworthy here.
