# Quant Analyst

- Symbol: BE
- Elapsed: 58.8s

---
# Bloom Energy (BE) — Quantitative Factor Analysis & Risk Statistics

**Price:** $142.45 (last close 2026-11-20) | **Mkt cap:** ~$34.3B (240.4M dil. sh.) — *profile reports $42.1B, implying ~295M fully diluted shares, i.e. ~23% convertible/option overhang not in the diluted count* | **Sector:** Industrials / Electrical Equipment & Parts

---

## 1. Factor Scores

| Factor | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **2** | 4 of 4 (ETN/VRT/GEV/BE); bottom decile of 50 largest Industrials | **Strong Sell** — P/E −385x (EPS −$0.37), P/B 43.2x (BVPS $3.30), EV/EBITDA 1,735x, P/FCF 599x. Every multiple is 10–80× peer levels (VRT 16.5× P/B, GEV 15.7×, ETN 6.2×; EV/EBITDA 21–50×). No value support at any price. |
| **Momentum** | **40** | 1 of 4 measured (**but all four negative**) | **Neutral / Deteriorating** — see conflict note below |
| **Quality** | **30** | 3–4 of 4 | **Sell** — ROE −11.2%, ROIC 1.92% (vs WACC; uneconomic), GP/assets 0.134 (VRT 0.304, GEV 0.120), Piotroski F-score **4/9 (Weak)**. Offsets: accruals −0.046 (high earnings quality — cash exceeds earnings), gross margin up 29.0% vs 27.5%, op. income positive for first time (+$72.8M on $2.02B revenue, +37% y/y). |
| **Low Vol** | **3** | 4 of 4 (worst) | **Strong Sell** — 113.1% annualised vol (VRT 71%), beta **4.16–4.47**, max drawdown 58.8%. A 10% market decline implies ≈−42% for BE. |
| **Earnings Revision** | **75 (low confidence)** | 1 of 4 measured | **Buy, weakly** — FY2030 consensus EPS revised **+22.98%** (13.5 vs 11.0) in 3 months. Caution: the revision window is a **far-dated FY2030 estimate**, not near-term; near-term PTs are mixed-to-down (Jefferies, JPM, Roth, BTIG, Wells Fargo all cut in Oct-26). Median of 20 PTs = **$262** (+84% vs spot), latest BMO $230 (Nov-19). Targets are stale vs the November collapse. |

**Composite Quant Signal: SELL** (high-dispersion name; not a Strong Sell only because revision momentum and PT upside are positive)

---

## 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Annualised return | +42.1% (arithmetic; 12-mo price change +52.6%) | −128.5% (deep negative, i.e. severe decline) |
| Annualised vol | 113.4% | 109.6% |
| **Alpha vs SPY** | **+45.4%** (t ≈ 0.5 — **not significant**) | **−72.9%** |
| **Beta vs SPY** | **4.16** (t ≈ 11 — highly significant) | **4.47** (stable) |
| R² | 0.311 | 0.368 |
| **Sharpe** | **0.372** (alt calc 0.53) | **−1.173** |
| **Sortino** | **0.643** | **−2.013** |
| Max drawdown | **−58.8%** | — |

**Interpretation:** Beta is stable (~4.2–4.5) and statistically robust; **alpha is not** — it flips from +45% to −73% when the window is halved. All the excess return was earned between late 2025 (~$90) and the June-2026 peak (~$346 close; $351.28 intraday); the last 6 months have more than reversed the excess return. With 1 year of data the annual Sharpe standard error is ≈1.0, so **Sharpe 0.37 is statistically indistinguishable from zero** (t≈0.36). Sortino > Sharpe indicates modest positive skew, but the 126-day Sortino of −2.01 shows the downside regime is now dominant.

**Momentum conflict (disclosed, not resolved):** the vendor 12-1 score is **−18.2%**, but raw closes give **+133%** for the same 12-1 window (93.38 → 217.77 on 2026-10-22) and **+52.6%** for the trailing 12 months. The vendor score is consistent with a ~1-month window: BE fell **−34.6% in the last 21 trading days** and **−15.3% on 2026-11-20 alone** on 28.7M shares (capitulation volume). I weight the *direction* of the vendor score (cross-sectionally consistent across all names) as the usable signal: momentum has rolled over hard. Current price sits 0.9% above the drawdown low ($140.69) with no support beneath.

---

## 3. Key Quant Risk Flags

1. **Negative recent alpha / regime break** — the +45% full-year alpha is entirely historical; trailing 6-month alpha −72.9%. Do not size on the 1-year alpha.
2. **Beta leverage trap** — beta 4.16–4.47 with R² only 0.31 (69% idiosyncratic). Position sizing must use *total* vol (113%), not market beta.
3. **Factor crowding confirmed** — BE correlation 0.58–0.62 to VRT/GEV/ETN, which are 0.68–0.80 correlated to each other. This is one crowded AI/data-centre power trade, not four independent names; the whole cohort de-rated together (VRT −32%, GEV −22%, ETN −19% momentum). Diversification across these names is largely illusory.
4. **Valuation with no floor** — EV/EBITDA 1,735x and P/FCF 599x mean multiples are not a support; the entire thesis rests on FY2027–30 estimates ($5.33 → $13.54 EPS). FY2027 revenue consensus of $7.27B implies ~90% two-year growth vs FY2025's $2.02B — an extremely aggressive extrapolation.
5. **Dilution** — shares 185.9M (FY22) → 240.4M (FY25), ~9%/yr; F-score flags dilution (F7 = 0). Fully diluted count may be ~295M, ~23% above the 240M used in the market-cap calc, understating per-share multiples.
6. **Estimate-revision sample weakness** — 13 analysts on a 4-year-forward period; that is not an actionable revision signal. Revision breadth on near-term PTs is actually negative.
7. **Liquidity: not a constraint** — ~10–15M shares/day (~$1.5–2B notional); no liquidity risk. *(Short interest unavailable — a probable additional risk given a 60% drawdown from a crowded theme.)*

**Bottom line:** Bottom-quintile on value, quality, and low-vol; momentum decaying with a broken trend; only far-dated estimate revisions are positive. The statistically defensible statement is that BE offers **no reliable risk-adjusted edge at current levels** — 12-month Sharpe 0.37 (insignificant), 6-month Sharpe −1.17, and a beta that turns any market wobble into a 4× loss.
