# Quant Analyst

- Symbol: CRDO
- Elapsed: 65.6s

---
## CRDO — Credo Technology Group Holding (Semiconductors, KY-domiciled/San Jose HQ, $18.77B cap, $99.86 last close 2026‑11‑20)

**Data-integrity note up front:** the factor engine's 252‑day windows do not reconcile with the raw price file. Verified from OHLCV: peak close $302.52 (2026‑06‑22) → $99.86 (2026‑11‑20) = **−67.0%**, which exactly matches the tool's reported max drawdown, implying the "252‑day" window is effectively ~5 months. I report tool outputs as system-of-record but attach my own verified arithmetic wherever the two diverge materially.

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | Trl P/E **39.8x**, EV/EBITDA **34.1x**, P/FCF **46.2x**, ROE 22.9%. Fwd P/E ~**15.9x** FY27E ($6.30), ~**10.3x** FY28E ($9.67) | ~60th pct of semis comp set (3rd cheapest of 5 on P/E & P/FCF, 4th of 5 on EV/EBITDA) | **Neutral** (trailing rich, forward cheap) |
| **Momentum** | 12‑1 ret **−44.6%**; 63d **−33.1%**; verified −45.4% (6m), −56.8% (3m), −30.6% YTD, **−67% off June peak** | Bottom decile | **Strong Sell** |
| **Quality** | ROE 22.9% (vs 7.7% FY25, −5.3% FY24), GP/assets **39.6%**, accruals **0.35%** (clean), ROIC **21.3%** (5.5%→−6.7% prior), Piotroski **7/9** | Top quartile vs own history; mid vs mega-cap semis (ROE 4th of 5) | **Buy** |
| **Low Vol** | Ann. vol **103.4%**, beta **3.53** (profile: 3.29), max DD **−67.0%**, SR‑approx 0.24 | Worst in comp set by a wide margin | **Strong Sell** |
| **Earnings Revision** | −**1.07%** on FY2031 EPS ($13.45 vs $13.60) — **only 2 analysts → not significant**. Sell-side PTs cut Sept–Oct (Stifel $350→$310, Mizuho $290→$245, Evercore $325→$292) after June–July raises | Median PT **$282.50** (n=12) vs $99.86 → **+183% implied** | **Neutral** (statistically insignificant) |

F‑score detail (7/9): loses points on accruals‑quality (F4) and **share dilution (F7)**; gains on ROA improvement, leverage reduction, margin and turnover improvement.

### 2. Price Statistics (verified where possible)
- **Alpha (annualised, vs SPY): +12.26%**
- **Beta: 3.55** (R² **0.27** → 73% of variance is idiosyncratic, not market)
- **Sharpe 0.281 / Sortino 0.455** (252d) — but **Sharpe −1.88 / Sortino −2.75** on 126d → sharp regime deterioration
- **Ann. vol 103–104%**; **Max drawdown −67.0%** (verified $302.52 → $99.86)
- Realised: +40.8% since Jan‑2025 ($70.93) but **−25.9% trailing 12m**; implied return math from the −67% drawdown over ~5 months annualises to roughly **−90%**, so the tool's +29.3% "annualised return" is an artifact of a mismatched window — treat return figures as unreliable, vol/drawdown as reliable.
- Fundamental growth support: rev est $1.33B FY26 → $2.50B FY27 (+88%) → $3.86B FY28 (+54%); EPS $3.31 → $6.30 → $9.67.

### 3. Composite Quant Signal: **NEUTRAL (negative tactical tilt)**
A textbook factor conflict: top-quartile **Quality** (21% ROIC, 0.35% accruals, F=7, 88% forward growth at 16x forward EPS) collides with bottom-decile **Momentum** and the worst **Low-Vol** profile in the peer group. Value is neutral (cheap forward, expensive trailing). In a momentum/vol-gated process this screens out; in a quality-at-a-reasonable-price process it screens in. Score-weighted across the five factors: **Neutral**, roughly −0.2σ.

### 4. Key Quant Risk Flags
1. **Momentum reversal risk — highest.** −67% drawdown with no base formation; 3m, 6m and 12‑1 all negative. Historically the worst regime for trend strategies.
2. **Beta 3.55 / vol 103%.** A 10% SPY drawdown mechanically implies ~35% CRDO downside; R² of 0.27 means the residual is pure stock-specific gap risk (earnings-day moves of −16% to +29% are in the sample).
3. **Earnings-revision signal is unusable** — 2 analysts on the long-dated estimate; the −1.07% is inside noise. Near-term FY27 consensus range is tight ($6.05–$6.48, n=12), suggesting high conviction but also high estimate fragility if AI-connectivity orders slip.
4. **Dilution** (F7 = 0) despite strong organic cash conversion — recurring SBC-driven share growth.
5. **Comparables caveat:** the sector peer set is mega-cap (NVDA $3.0T, AVGO $1.45T, TSM, AMD, MU) vs an $18.8B small-cap; multiples are not size-adjusted, and TSM's ratios returned corrupted values (P/E 0.96, EV/EBITDA −0.15) — excluded from ranking.
6. **Liquidity is NOT a flag**: ~7–13M shares/day (~$0.7–1.3B) is ample.
7. **Data vintage risk:** price targets run to Oct‑2026 while several inputs are anchored earlier — the +183% implied upside is likely stale and should not be traded on without re-basing the target set.
