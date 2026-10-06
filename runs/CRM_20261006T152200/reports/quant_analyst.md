# Quant Analyst

- Symbol: CRM
- Elapsed: 160.5s

---
Analysis complete. All data gathered — the custom-universe rank tool has a recurring schema bug (string rejected / list rejected), so I'm noting that gap and anchoring sector ranks on direct software-peer factor values instead.

---

# QUANT FACTOR REPORT — CRM (Salesforce, Inc.)

**Universe & data notes:** CRM is a ~$187B mega-cap (Microsoft-family software; sector: Technology). It falls **outside the 25-symbol ranked research universe** used by the factor screens (universe = top 25 by market cap), so formal cross-sectional quintile ranks are **not computable** — flagged as a data gap. Sector ranks below are anchored on direct computations for the two closest software comps (ORCL, ADBE) plus the mega-cap screen where available. All price stats use a 252-trading-day window vs SPY.

## 1. Factor Scores

| Factor | Raw Value | Software-Peer Rank (3 comps) | Signal |
|--------|-----------|------------------------------|--------|
| **Value** | P/E 29.2 · P/B 3.7 · EV/EBITDA 17.1 · P/FCF 15.1 (FCF yield 6.6%) | **3rd / 3** (worst P/E & EV/EBITDA; ADBE 14.3/10.4, ORCL 24.9/17.0) | **Weak** |
| **Momentum** | 12–1 month return **+57.3%** (252d lookback, excl. last 21d) | Highest raw level in peer set, but stale (see §2) | **Positive — reversal risk HIGH** |
| **Quality** | ROE 12.6% · Gross profit/assets 0.287 · Accruals −0.067 · Piotroski **7/9** | **3rd / 3** on ROE (ADBE 61.3%, ORCL 39.7%) | **Weak** (tool signal: "low") |
| **Low Vol** | Ann. vol **51.4%** · Max drawdown −43.3% | Worst of comps (very high vol) | **Negative** |
| **Earnings Revision** | Consensus EPS FY2031 $21.15 → **$25.37 (+19.95%)** | Strong directional upgrade | **Buy** |

Component detail: Piotroski F=7/9 (profitability 4/4, efficiency 2/2, leverage/liquidity 1/3 — leverage increased, equity issuance). Negative accruals on CRM (−0.067), ADBE (−0.098), ORCL (−0.057) mean bookkeeping is *not* inflating earnings quality — that is the one genuinely healthy input. Earnings revision is +19.95% but on a **5-year-forward horizon with only 10 analysts covering FY2031** — treat as directionally bullish, not precise.

## 2. Price Statistics (252d, vs SPY, rƒ = 0%)

| Stat | Value | Read |
|------|-------|------|
| Alpha (annualised) | **−12.75%** | Negative, but R² = 0.007 → **not statistically meaningful** |
| Beta vs SPY | **0.32** | Appears low-vol, but regression explains <1% of variance → unreliable |
| Sharpe / Sortino | **−0.137 / −0.264** | Both negative — poor trailing risk-adjusted return |
| Annualised return / vol | **−7.1% / 51.4%** | Negative drift, very high vol |
| Max drawdown | **−43.3%** | Severe |
| Peer correlations | MSFT 0.46 · AAPL 0.10 · NVDA 0.07 | Decoupled from mega-cap peers → idiosyncratic |

**Critical reconciliation — stale momentum signal:** 12–1 momentum says +57.3%, but the full-window return is −7.1% and Sharpe is negative. Reconciling the two implies the **most recent ~21 trading days fell ≈ −41%** — consistent with the 43.3% max drawdown. The headline momentum is almost entirely a pre-crash artifact. (Caveat: a ~40% one-month drawdown in a mega-cap is anomalous vs real-world tape — flagging as a data-consistency item to verify.)

## 3. Composite Quant Signal: **NEUTRAL**

- **Supports Buy:** +20% EPS estimate revision, Piotroski 7/9, 6.6% FCF yield, clean negative accruals.
- **Supports Sell:** Bottom-of-peer value & quality, negative Sharpe/Sortino/alpha, 43% max drawdown, and a stale momentum factor that contradicted itself in the last month.
- The framework rewards stocks that score top-quintile on value **and** momentum **and** quality. CRM scores in the bottom third on two of three, and its one strong factor (momentum) is reversing. On a strict trailing risk-adjusted reading it would be **Sell**; the bullish case rests entirely on forward-looking revisions, so the composite lands at **Neutral**, tilt negative.

## 4. Key Quant Risk Flags

1. **Momentum reversal — HIGH, #1 risk.** +57.3% 12–1 momentum vs ≈ −41% implied last-21-trading-days and a −43.3% max drawdown. Any factor model long on CRM's momentum is stale.
2. **Cross-sectional rank gap.** CRM is outside the ranked 25-cap universe; within the computable software peer set it is last on P/E (29.2 vs ADBE 14.3 / ORCL 24.9) and last on ROE (12.6% vs 61.3% / 39.7%). No top-quintile claim is supportable.
3. **Benchmark decoupling, not low beta.** Beta 0.32 with R² = 0.007: the −12.75% alpha and low beta are statistical noise, not risk signals. Peer correlations (0.07–0.46) confirm idiosyncratic, not market-driven, behavior.
4. **Revision-horizon noise.** The +19.95% upgrade targets FY2031, 5 years forward, 10 analysts — small sample; likely overstated precision (estimate range $24.9–$25.8 is deceptively tight).
5. **Small-window inference.** The recent-crash read rests on ~21 daily observations — sufficient to flag, insufficient to model regime change without confirmation.

**Bottom line:** Neither a quant short nor a quant long. Neutral composite driven by a bullish revisions signal against bottom-of-peer value/quality and a momentum factor that has already reversed. Do not express a position on the stale +57% momentum; re-screen after the revision trend or valuation multiple improves.
