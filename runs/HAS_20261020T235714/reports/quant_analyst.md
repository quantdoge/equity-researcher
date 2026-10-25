# Quant Analyst

- Symbol: HAS
- Elapsed: 60.7s

---
# Hasbro, Inc. (HAS) — Quantitative Factor Report

**Price:** $109.52 | **Market cap:** ~$15.4B | **Sector:** Consumer Cyclical / Leisure | **Beta (long-run, FMP):** 0.44

> **Data-integrity note up front:** the OHLCV series I pulled ends **2025-12-31 at $80.17**, while the "current" price used by the valuation tools is **$109.52**. The stock has therefore appreciated an additional **+36.6%** after the history window, which means every trailing return/momentum figure below **understates** realized momentum. Price targets are dated mid-2026 (posted on ~$81–93).

---

## 1. Factor Scores Table

Scores are 0–100 percentile-style composites on the raw factor outputs. **Sector ranks are LOW CONFIDENCE** — see caveat below.

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | 30 | Bottom ~30% | **Bearish** — P/E −47.6 (TTM loss), P/B **27.2x** on a collapsed book ($4.03/sh BVPS); partly offset by EV/EBITDA 14.9x, P/FCF 18.5x, 2.56% yield |
| **Momentum (12-1)** | 78 | Top ~20% | **Bullish** — +10.1% 12-1 return *in-sample*; full-window return ~+31.7% (Dec-24 $60.86 → Dec-25 $80.17), plus a further +36.6% to $109.52. Trend is unambiguously up |
| **Quality** | 45 | Mid/low | **Neutral (barbell)** — gross profit/assets **0.540** (strong, Novy-Marx), accruals **−0.219** (conservative, high earnings quality), but ROE **−57%**, ROIC **0.28%** (from 15.0% in FY24), Piotroski F **4/9** (weak) |
| **Low Vol** | 40 | Mid | **Neutral/mixed** — beta **0.66** is genuinely low, but absolute vol **34.6%** is high and max DD **27.3%**. Low beta, high total risk = idiosyncratic, not defensive |
| **Earnings Revision** | 62 | Top ~35% | **Mildly bullish, but statistically weak** — FY2030 EPS revised 7.35 → 7.73 (**+5.17%**) on **n = 1 analyst** |

**Forward valuation check (the real value argument):** FY2027E EPS $6.46 (8 analysts) → **17.0x**; FY2028E $7.23 → **15.1x**; FY2030E $7.73 → **14.2x** at $109.52. On consensus forward numbers HAS is a *market-multiple* stock, not an expensive one — the negative trailing P/E is an impairment artifact.

---

## 2. Price Statistics (252-day window vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **38.44%** |
| Annualised volatility | **34.58–34.78%** |
| Beta vs SPY | **0.665** (0.661 in the vol calc) |
| Alpha (annualised, OLS) | **+29.28%** |
| R² | **0.063** ⚠️ |
| Sharpe ratio | **1.105** (vol-tool: 1.135) |
| Sortino ratio | **2.024** |
| Max drawdown | **−27.31%** |

**Read:** A Sharpe >1.0 with a Sortino >2.0 is objectively good risk-adjusted performance, and the low 0.66 beta means it was earned with sub-market systematic exposure. **But the R² of 0.063 is the single most important number in this report** — the market factor explains only ~6% of HAS's return variance. The "+29% alpha" is therefore a *point estimate with an enormous standard error*; it is not evidence of durable skill-driven excess return, it is evidence that HAS did something idiosyncratic and positive in this window. Do not extrapolate.

Underlying drawdown path: peak $64.93 (20-Feb-25) → trough $46.57 (09-Apr-25) ≈ **−28.3%**, driven by the tariff/trade shock. Recovery to $80.17 by year-end, then to $109.52. This is a high-amplitude trader's stock, not a compounder's stock.

---

## 3. Composite Quant Signal

### **NEUTRAL (with a positive momentum/estimate-revision tilt)**

Factor votes: 1 bullish (momentum), 1 mildly bullish (revisions), 2 neutral (quality, low-vol), 1 bearish (value). No factor reaches the top quintile on a *clean* basis, and the one top-quintile reading (momentum) is a trailing, crowded, and now-extended signal. That is not a Strong Buy configuration. It is also clearly not a Sell — the tape, the forward multiple (15–17x) and the direction of estimates all point the right way.

**Why not Buy:** the quality pillar does not confirm the momentum. A stock at 27x book with a sub-1% ROIC, an F-score of 4, and negative GAAP earnings is a *narrative recovery*, and this framework requires the numbers to confirm the story. They only half do.

---

## 4. Key Quant Risk Flags

1. **Alpha is statistically hollow (R² = 0.063).** The 29% annualized alpha is not separable from noise. Treat the excess return as unverified. Low explanatory power also means SPY-based beta hedging will *not* protect this position — the risk is 94% company-specific.
2. **Book equity is nearly destroyed.** BVPS $4.03 with P/B at 27.2x and ROE −57%. Any further goodwill/intangibles impairment mechanically re-rates the P/B and re-breaks the trailing P/E. This is the balance-sheet tail risk.
3. **Earnings-revision signal is noise.** +5.17% rests on **one analyst's FY2030 number** — five years out, single contributor. Statistically meaningless; I assign it weight only because it agrees with the tape, not because it is significant.
4. **Momentum reversal / crowding risk — the highest-probability near-term risk.** The stock has run $60 → $110. The **mean of the 5 most recent price targets is $105** (90 / 120 / 95 / 110 / 110), i.e. **~4% *below* the current price**. Street targets are now *behind* the tape — the classic setup for a momentum reversal. Note also mixed target directionality: Wells Fargo raised (85→90), UBS raised (→120), but DA Davidson (100→95) and Jefferies (120→110) both *cut*.
5. **High absolute volatility despite low beta (34.6% vs beta 0.66).** Volatility is idiosyncratic and event-driven; toys are a Q4-concentrated seasonal business, so the earnings-date gap risk is structurally large.
6. **Dividend coverage.** 2.56% yield against negative GAAP EPS. It is covered by operating cash flow ($893M OCF vs $322M net loss), but not by earnings — vulnerable to any cash-flow wobble.
7. **Sector rank caveat.** The peer set returned is mega-cap Consumer Cyclical (AMZN, TSLA, HD, BABA, MCD…), **not** toy/leisure comps. Mattel, Spin Master, JAKKS and similar direct comparables were unavailable, so all "sector rank" percentiles above are against a loosely related universe and should be read as directionally indicative only, not as rigorous cross-sectional z-scores.

**Liquidity:** not a concern — $15.4B cap, ~1.5M ADV, tight spreads.

---

## Bottom line for the memo

HAS screens as a **high-momentum, low-beta, low-quality, low-value recovery name**. Sharpe 1.11 / Sortino 2.02 look excellent but are built on a return series the market barely explains (R² 0.06), so I would not bank the alpha. The forward multiple (15–17x on FY27–28 consensus) is the strongest quantitative support for the long case; the 27x book, 0.28% ROIC and F-score of 4 are the strongest case against. With price targets now at or below spot, **avoid adding on momentum** — the quantitative edge here has been largely realized.
