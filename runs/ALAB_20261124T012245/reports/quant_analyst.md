# Quant Analyst

- Symbol: ALAB
- Elapsed: 41.6s

---
## ALAB (Astera Labs) — Quantitative Factor Report

**Sector:** Technology / Semiconductors · Mkt cap ~$21.3B (see integrity flag) · Price used in vendor ratios: $222.12; last OHLCV close $118.83 (2026-02-27)

### 1. Factor Scores

| Factor | Score | Sector Rank (n=9 semis) | Signal |
|---|---|---|---|
| **Value** | P/E 182.1 · EV/EBITDA 172.1 · P/FCF 141.5 · P/B 29.3 | **9/9 (bottom)** | **Strong Sell (factor)** |
| **Momentum** | 12-1 return **−19.3%** (vendor); **+125.8%** recomputed from OHLCV | 4/8 ex-corrupt peers | **Conflicting / Neutral** |
| **Quality** | ROE 16.1%, GP/Assets 0.421, accruals −6.5%, ROIC 12.4%, F-score 6/9 | **3/9 (top tercile)** | **Buy** |
| **Low Vol** | Ann. vol 104.7%, β 4.10, max DD −62.8% | **9/9 (worst)** | **Strong Sell (factor)** |
| **Earnings Revision** | Forward EPS revised **+24.5%** over 3 months | 1 of 9 positive | **Buy — low confidence** |

Peer detail (value, valid names only): MU 9.5x → NVDA 33.7x → ASML 56.0x → AVGO 65.7x → AMD 171.1x → **ALAB 182.1x** (INTC negative/n.m.). ALAB is the most expensive positive-earnings semiconductor in the comp set.

Quality detail — GP/Assets: NVDA 0.742 → **ALAB 0.421** → ASML 0.341 → TSM 0.288 → AVGO 0.253 → AMD 0.223 → INTC 0.087. Accruals: TSM −7.3% → **ALAB −6.5%** → ASML −6.0% → AMD −4.4%. Negative accruals (NI $219M vs OCF $319M) = high earnings quality; cash conversion 146% of net income.

Revision detail: FY2030 EPS $17.33 vs $13.92 three months prior (+24.5%), FY2026 $4.34, FY2027 $7.16. Implied P/E at $118.83: **27.4x FY26, 16.6x FY27** — the value factor's 182x is a trailing artifact; forward growth (2025→26 EPS +144%, 2026→27 +65%) is where the multiple lives.

### 2. Price Statistics (252d, vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+90.77%** |
| Beta | **4.118** (profile beta 3.859) |
| R² | 0.397 — **60% idiosyncratic** |
| Annualised vol | 104.7% (Sharpe tool: 106.2%) |
| Sharpe (0% rf) | **1.219** |
| Sortino | **1.970** |
| Annualised return (vendor) | +129.4% |
| Max drawdown | **−62.84%** (OHLCV-window recompute: −52.8% close-to-close, 251.88 → 118.83) |
| Correlations | AMD 0.70, INTC 0.68, MU 0.65, SPY 0.63, AVGO 0.62, NVDA 0.52 |

Sharpe 1.22 / Sortino 1.97 looks respectable in isolation, but it is a *return-per-unit-of-104%-vol* number: the equity curve is one of the most volatile in the semiconductor universe. Alpha is **not statistically significant** — with residual vol ~82% and ~1 year of data, the t-stat on alpha is ≈1.1 (needs >2.0). Beta of 4.1 with R² under 0.40 means ALAB is a levered, largely stock-specific AI-connectivity bet, not a diversified tech exposure.

### 3. Composite Quant Signal: **NEUTRAL** (high-risk, growth-dependent)

- **Quality (+)** top-tercile GP/Assets and negative accruals; genuinely high earnings quality.
- **Growth/Revisions (+)** triple-digit EPS growth, +24.5% revision, forward P/E 27x — not 182x.
- **Value (−)** worst in sector on every trailing multiple.
- **Low-vol (−)** worst in sector: 105% vol, β 4.1, −63% max drawdown.
- **Momentum (?)**

Net: quality and revisions are fighting a 105%-vol, β 4.1, sector-worst-valuation profile. Not attractive on a factor basis, not a Sell on fundamentals. Neutral, with a **sell-biased risk overlay**.

### 4. Key Quant Risk Flags

1. **⚠️ DATA INTEGRITY — read before using any multiple.** The vendor profile price ($222.12) and the OHLCV series (last close **$118.83**, 2026-02-27) disagree by 47%. The $222.12 anchor matches ALAB's early-October 2025 level, so trailing multiples are likely computed on a stale price. Rescaled to $118.83: P/E **~97x**, P/B **~15.7x**, EV/EBITDA **~92x**, P/FCF **~76x** — still the most expensive name in the group, but half the reported figures. Market cap should be ~**$21.3B** (179.6M shares × $118.83), not $38.8B.
2. **Momentum signal conflict** — the vendor's −19.3% 12-1 momentum cannot be reproduced from the price file: from 2025-03-03 ($67.68) / 2025-02-28 ($74.35) to the 21-day-prior close of $167.90 (2026-01-28) the return is **+126%**. Either way, the *trend* is broken: −37% from the 2026-01-16 high ($187.67) in six weeks, including a −31% two-day collapse on 2026-02-10→12 (182.86 → 126.58) on 16.4M and 11.4M shares — textbook institutional distribution/high-volume reversal.
3. **Momentum-reversal / factor crowding** — β 4.1 and 0.63–0.70 correlation to AMD/MU/INTC means ALAB is a high-beta proxy for the AI-semi trade; it will amplify any sector de-rating roughly 4x.
4. **Sample-size caveats** — IPO'd 2024-03-20, so <2 years of history: beta, alpha, Sharpe and max drawdown all rest on a single 252-day window (n≈252, t-stat on alpha ≈1.1, **not significant**). The revision score is worse: it compares **FY2030** consensus with only **5 analysts** covering that out-year — I would not trade on it.
5. **Volatility/event risk** — 105% annualised vol, 6%+ average daily true range, and repeated single-day moves >12% around prints. Position sizing must assume −50%+ drawdowns are normal.
6. **Liquidity: NOT a flag** — ~3–6M shares/day (~$600–700M notional), liquid enough for institutional size.

**Bottom line:** quality is real, valuation is extreme, and the risk factor is the worst in the sector. The quant case is **Neutral at best — not a factor buy**, and the only statistically robust statement in this book is "very high volatility, very high beta, beta-adjusted nothing new." Excluded from ranking: TSM and SKHY value metrics (vendor P/E 1.1 and 0.02 — ADR/local-currency unit error, not usable).
