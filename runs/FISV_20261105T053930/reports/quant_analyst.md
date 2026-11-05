# Quant Analyst

- Symbol: FISV
- Elapsed: 92.5s

---
## FISV (Fiserv, Inc.) — Quantitative Factor Report
Price $62.05 | Mkt cap $33.0B | EV $62.4B | FY end 2025-12-31 | Data as of 2026-02-20

**⚠ Data-integrity caveat up front:** the return-based risk tools do not reconcile with the OHLC tape. The `momentum` tool reports −16.42% 12-1, `alpha` −5.21%, `Sharpe` +0.32 — but the raw price record shows $234.43 (2025-02-20) → $62.05, a **−73.5% one-year return**. The 504-day readings *do* tie to the tape (vol 52.4%, max DD −74.7%), so I treat the 504-day stats and my own tape-derived returns as governing, and report tool values alongside. With R² = 0.016, the alpha/beta regression is statistically meaningless regardless.

### 1. Factor Scores

Peer set = payments/fintech (FISV, GPN, PYPL, MA, V); rank 1 = best of 5. The `get_sector_peers` feed returns mega-cap hardware/semis (AAPL, NVDA, MSFT), which are not valid comparables — I discarded it and built the peer group manually.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| Value | 9.0/10 | **1 / 5** | **Strong Buy** |
| Momentum | 1.0/10 | 5 / 5 | **Strong Sell** |
| Quality | 5.0/10 | 3 / 5 | Neutral |
| Low Vol | 2.0/10 | 5 / 5 | Sell |
| Earnings Revision | 2.0/10 | 5 / 5 | Sell (see warning) |

**Value (raw):** P/E 9.79 · P/B 1.32 · EV/EBITDA 6.97 · P/FCF 7.92 · FCF yield 12.6% · EV/EBIT 10.8x. Cheapest of the group on all three multiples (GPN 16.5/10.6/11.3; PYPL 11.1/7.5/10.5; MA 40.7/29.8/36.8; V 35.4/27.8/37.7). Forward P/E 8.5x on FY26E $7.27, 7.8x FY27E $7.96.

**Momentum (verified from tape):** 12-1 −72.2% · 12m −73.5% · 6m −55.7% · 3m +3.8% · YTD −7.6% · −73.9% from the 2025-03-03 high. The only positive is a +6.8% bounce off the 2026-02-03 low ($58.12).

**Quality:** ROE 13.5%, ROIC 10.4% (down from 11.2% in FY24), ROA 4.3%, GP/assets 15.7% (vs MA 60.6%, V 39.1%, PYPL 19.3%), accruals **−3.22%** (2nd best of 5; cash conversion strong: OCF $6.06B vs NI $3.48B), Piotroski **F-score 5/9** — leverage up (F5=0), no positive equity change (F6=0), gross margin down (F8=0), asset turnover down (F9=0). Revenue growth decelerating: +7.1% (FY24) → +3.6% (FY25); gross margin 60.8% → 59.4%; **EBIT −3.0% y/y while reported NI rose 11%** — EPS is being carried by a 5.7% share-count reduction, not operations. That is the central quality flaw.

**Earnings Revision — tool output rejected:** the model returns "+22.59%, upgrade," but it is comparing the **FY2030** estimate ($13.19) to the **FY2029** estimate ($10.76) — two different fiscal years, not a 3-month revision. That is a growth rate, not revision momentum. Actual evidence is bearish: FY26 consensus $7.27 vs FY25 $8.56 = **−15.1%**, and every price target in the sample was cut ($65→60, $65→59, $60→54, $52→50, $53→48, $53→51, $50→48). Revisions are unambiguously **down**.

### 2. Price Statistics

| Metric | 252d | 504d | Note |
|---|---|---|---|
| Beta vs SPY | 0.42 | 0.57 | 5y profile beta 0.80 — declining |
| Alpha (ann.) | −5.21% | n/a | Not credible; R² = 0.016 |
| R² vs SPY | 0.016 | — | 98.4% idiosyncratic |
| Annualised vol | 43.5% | **52.4%** | Very high for payments |
| Sharpe | 0.32 | **−0.97** | 252d figure inconsistent with −73.5% return |
| Sortino | 0.50 | n/a | Same caveat |
| Max drawdown | −33.1% | **−74.7%** | Verified: $237.79 → $58.12 |

Beta is a trap here: 0.42 looks defensive, but with 52% vol and R² of 0.016 it is a **low-beta, high-idiosyncratic-risk** profile — the market explains essentially none of the risk.

### 3. Composite Quant Signal: **SELL** (composite 3.8/10)
Weights: Momentum 25%, Value 20%, Quality 20%, Revision 20%, Low Vol 15%.
`0.20(9.0) + 0.25(1.0) + 0.20(5.0) + 0.20(2.0) + 0.15(2.0) = 3.75`

This is a textbook **value-trap configuration**: cheapest decile valuation, worst-decile momentum and revisions, compressing margins, rising leverage. The cheapness is the market pricing in a permanently lower earnings base, not a mispricing. A value-only screen would say Buy — the other four factors veto it. Upgrade trigger: two consecutive quarters of stabilising/raising FY consensus and a reclaim of the 2025-10-29 gap ($70.60).

### 4. Key Quant Risk Flags

1. **Gap-risk / non-stationary vol.** Four single-day crashes in 12 months: −18.5% (2025-04-24), −16.2% (2025-05-15), −13.9% (2025-07-23), **−44.1% (2025-10-29 on 103.5M shares, ~19x ADV)**. Return distributions are fat-tailed and event-driven; stop-losses and vol targeting are structurally ineffective. Realised vol is a poor guide to future vol — regime shifts, not noise.
2. **Leverage.** Net debt ≈ **$29.4B** (EV $62.4B − mkt cap $33.0B) = **3.3x EBITDA**; interest expense $1.53B, **+23.7% y/y**; EBIT/interest 3.8x, EBITDA/interest 5.8x. F-score leverage and equity-change flags both fail. Cheap equity + rising interest cost + decelerating revenue is a refinancing-risk compound.
3. **Squeeze risk on the
