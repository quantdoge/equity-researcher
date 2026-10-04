# Quant Analyst

- Symbol: MS
- Elapsed: 72.3s

---
All data gathered. I have everything needed — writing the full quant report now.

---

# Quant Factor Report — Morgan Stanley (MS)
**Sector:** Financial Services (Capital Markets) | **Price:** $190.31 | **Mkt Cap:** ~$300B | **Data as of:** latest close

## 1. Factor Scores

| Factor | Score | Sector Rank (vs. money-center bank peers)¹ | Signal |
|--------|-------|--------------------------------------------|--------|
| Value | P/E 18.66, P/B 2.69, EV/EBITDA 8.97, P/FCF 6.58, DivY 2.18% | Below median (P/E & P/B premium to GS 17.6/2.3, JPM 16.6/2.6, BAC 14.1/1.3) | **Neutral** |
| Momentum | 12-1 mo return: **–0.69%** | Bottom half (negative vs. strong bank-benchmark momentum) | **Weak/Neutral** |
| Quality | ROE 14.97%, GP/assets 4.62%, Accruals –2.26%, F-Score 7/9 | Top half (ROE improving 4 yrs: 10.9→9.1→12.7→15.0) | **Positive** |
| Low Vol | Vol 29.9%, Beta vs SPY 1.45, MaxDD –18.8% | Bottom decile — high-beta, high-vol name | **Negative** |
| Earnings Revision | Consensus FY29 EPS $16.38 vs. prior $14.88 → **+10.1% upgrade** | Top decile | **Strong Positive** |

¹ *Caveat:* the sector-peer API returned index funds, not financial stocks. Ranks are estimated against a manually composed money-center bank set (GS, JPM, BAC, C, WFC) — indicative, not a full cross-sectional screen.

**Valuation nuance:** Trailing P/E (18.7) looks rich vs. peers, but consensus growth makes forward multiples cheap: **FY27E 13.9x, FY28E 12.8x, FY29E 11.6x** on EPS of 13.69/14.88/16.38. The value case rests entirely on the delivery of those upgrades.

## 2. Price Statistics (252-day window vs. SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **–11.0%** |
| Beta | **1.46** (R² = 0.41) |
| Sharpe | 0.31–0.42 (rfr = 0) |
| Sortino | 0.45 |
| Annualised return / vol | +9.4% / 29.9% |
| Max drawdown | –18.8% |
| Peer correlation (252d) | GS 0.86 · C 0.75 · JPM 0.66 · BAC 0.66 · WFC 0.54 |

Only 41% of MS variance is explained by the market — substantial idiosyncratic risk. Negative alpha with a 1.46 beta means the stock has *underperformed* its risk level: it delivered equity-like downside with inferior compensation.

## 3. Composite Quant Signal: **BUY** (leaning cautious)

**Bull case:** Earnings revisions are the single most predictive factor in our framework and they are decisively positive (+10.1%, among the strongest signals scored). ROE has compounded from 9.1% to 15.0% over three years, accruals are negative (clean earnings), F-Score 7, and forward P/E of ~12–13x on a 15% ROE franchise is not demanding. Sell-side targets ($215–$260, mean ~$235 ≈ +24% vs. price) cluster well above spot even after Wells Fargo's trim to $223.

**Bear case:** 12-1 momentum is *negative* while most large-cap financials rode 2025 strength; the alpha/beta profile is unambiguously poor (high beta, negative alpha, Sharpe < 0.5); valuation is a premium to peers on trailing metrics. Historically, negative momentum + negative alpha is a combination that argues for patience or a smaller position.

**Net:** The revision momentum and forward valuation outweigh flat momentum and rich trailing optics. **Buy, moderate conviction** — this is a *revision-driven* buy, not a momentum or value buy, so sizing should reflect that the price catalyst is entirely contingent on EPS upgrade delivery.

## 4. Key Quant Risk Flags

- ⚠️ **Momentum reversal risk:** 12-1 return –0.7% with stock ~7% below July highs (~$210); no positive price confirmation of the EPS story yet.
- ⚠️ **Factor crowding / idiosyncratic concentration:** 0.86 correlation with GS — the two bulge-bracket names trade as one factor; any capital-markets de-rating hits both. R² of 0.41 means ~60% of risk is idiosyncratic (trading revenues, WM flows).
- ⚠️ **High-beta exposure:** β 1.46 — MS is a ~1.5x S&P amplifier; in a tape drawdown the stock will overshoot to the downside (recent –18.8% DD demonstrates).
- ⚠️ **Value-trap risk if revisions revert:** P/FCF 6.58 and EV/EBITDA 8.97 are ratios that flatter bank FCF volatility; trailing P/E premium to all large peers leaves little cushion if FY26 execution slips.
- ℹ️ **Statistical note:** Earnings-revision signal computed on only 4 analysts for the 2029 period — meaningful but thin coverage; treat the +10% magnitude with appropriate haircut.

**Bottom line:** Strong revisions + improving quality against negative momentum and a weak risk-adjusted return profile → **Buy (moderate conviction)**, sized knowing the trade is an earnings-revision bet with 1.5x market beta.
