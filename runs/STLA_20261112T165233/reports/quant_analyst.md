# Quant Analyst

- Symbol: STLA
- Elapsed: 53.1s

---
# STLA — Quantitative Factor & Risk Assessment
**As of 2026-11-12 | Price $3.93 | Mkt cap $11.35B | EV $37.7B | Consumer Cyclical / Auto Manufacturers (NL)**

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/B 0.19 · EV/EBITDA 5.9x · P/E 196.5x · P/FCF −1.01 · Div yld 19.6% | 1 of 3 on P/B (TSLA 16.7) | **Mixed / Value Trap** |
| **Momentum** | −63.5% 1-yr; 12-1 momentum −22.7% (tool) | 3 of 3 | **Strong negative** |
| **Quality** | ROE 0.3%, ROIC 0.78%, GP/Assets 5.9%, F-Score 5/9 | 3 of 3 (TM ROE 9.7%) | **Weak** |
| **Low Vol** | Vol 53.97% ann., beta 1.02, max DD −61.6% | 3 of 3 | **Strong negative** |
| **Earnings Revision** | Tool: +15.4% "upgrade" — **invalid** (see below) | n/a | **Negative (adjusted)** |

**Value — nuance matters.** P/B of 0.19 (BVPS $21.24 vs $3.93) is genuine deep-asset territory, and the $37.7B EV against FY2026 EBITDA of €6.4B looks cheap. But two offsets kill the headline: (a) **P/FCF −1.01** — operating cash flow was **−€6.8B** in FY2026 and −€5.5B in FY2025, so there is no cash-based valuation support; (b) **EV/EBITDA 5.9x is a ~48% premium to Toyota's 4.0x** despite Toyota earning a 9.7% ROE and STLA 0.3%. On the one multiple that is currency-consistent and forward-looking, STLA is **not cheap**. The 19.6% dividend yield against negative FCF is a cut waiting to happen, not income.

**Quality — unambiguously poor and deteriorating fast.** ROIC collapsed 20.6% (FY23) → 4.6% (FY24) → **−22.2%** (FY25) → 0.8% (FY26). Gross profit/assets fell from ~$0.19 to 0.059, and gross profit itself went *negative* in FY2025 (−€4.2B). F-Score 5/9 masks two zeros that matter: **F2 (positive operating cash flow) = 0** and **F4 (accruals quality) = 0**.

**Earnings Revision — the tool's signal is an artifact; the real signal is negative.** The +15.42% "upgrade" compares FY2030 consensus EPS (2.145) to FY2029 (1.858) — two *different fiscal years four years apart*, not the same forward period three months apart. That is a growth curve, not revision momentum. The true evidence: FY2026 consensus was **€0.479** and actual reported EPS came in at **€0.02** — a ~96% miss. Coverage is **3–5 analysts** (drift risk, low statistical power). Adjusted correctly, revisions are **downward**.

---

## 2. Price Statistics

| Metric | 252d | 120d | Read |
|---|---|---|---|
| Annualised return | −80.1% | −85.9% | Compounded actual 1-yr: **−63.5%** ($10.76→$3.93); tool annualises arithmetically, so treat as directional |
| Annualised volatility | 53.97% | 48.56% | ~1.8× a typical auto OEM — extreme |
| Beta vs SPY | 1.016 | 0.975 | **Unreliable** |
| R² vs SPY | 0.074 | 0.078 | **Only 7% of variance explained** |
| Alpha (annualised) | −118.7% | −131.9% | Large and significant, but event-driven |
| Sharpe | −1.711 | −1.781 | Deeply negative |
| Sortino | −3.14 | −3.583 | Downside dev. ≫ total dev. — crash-dominated |
| Max drawdown | −61.6% | −44.2% | Peak-to-now from $14.78 (Sep-24): **−73.4%** |

**The beta of 1.02 is a statistical fiction for risk-management purposes.** With R² = 0.074, STLA's returns are ~93% idiosyncratic. Market-hedging the position will not work. Correlations: SPY 0.27, Toyota 0.28, Tesla 0.17 — no sector read-through, no diversification substitute.

Note a minor internal inconsistency: the standalone volatility tool reports Sharpe −1.921 vs −1.711 from the Sharpe/Sortino function on the same 252d window. Immaterial to the conclusion but worth flagging as feed noise.

**Event concentration:** the 1-yr alpha is driven by a handful of gap days — notably **2026-02-06 (−23.7% on 93M shares, 5× normal volume)** and **2026-10-28 (+10.0% on 120M shares)**. Excluding outliers would materially change alpha; the estimate is *not* robust to single observations. n=252 is adequate in count but effectively far smaller in independent information.

---

## 3. Composite Quant Signal: **SELL**

*(Strong Sell is defensible; I hold at Sell solely because of the 0.19× book asset floor and the possibility of a violent mean-reversion squeeze from this depressed level.)*

STLA is the textbook **value-trap configuration**: top-quintile on a single static value metric (P/B), **bottom-quintile on every dynamic factor** — momentum, quality, low-vol, and true revision momentum. The framework's high-conviction case requires value + momentum + quality together; STLA has one of three, and that one is contradicted by the cash flow statement. Value without quality and without a catalyst is a falling knife, and the −63.5% trailing year confirms the market is repricing solvency, not mispricing assets.

---

## 4. Key Quant Risk Flags

1. **Cash burn is the dominant risk, and the accruals ratio hides it.** FY2026 accruals ratio of 0.0327 screens "ok" only because it is scaled by a ~€200B asset base; in absolute terms it is **−€7.0B of operating cash flow against +€0.19B of net income**. Do not let the benign ratio reassure you.
2. **Dividend sustainability — high risk.** 19.6% yield with negative FCF and a €0.02 EPS. Model a cut; the yield is not a return, it is a distress signal.
3. **Data-integrity flag on FY2025 gross profit.** FY2025 COGS (€157.7B) *exceeds* revenue (€153.5B), producing −€4.2B gross profit. At that magnitude this is more likely a mixed-currency or cost-line error than economic reality. **Verify against the 20-F before relying on the FY2025 loss figure** (−€22.4B net income). All quality scores inherit this uncertainty.
4. **Peer benchmarking is compromised.** Toyota's P/E of 0.07 and P/B of 0.01 are JPY/USD currency mismatches — unusable. Only EV/EBITDA (TM 4.0x) and dividend yield are reliable comps; Tesla is not an economically comparable business. **True auto-peer multiples (GM, Ford, Renault, VW) were not retrievable** — the "sector rank" column is therefore an estimate over a 3-name sub-industry, not a rigorous cross-sectional z-score.
5. **Momentum-reversal / squeeze risk (two-sided).** At P/B 0.19 with heavy volume spikes, upside gaps of 10%+ occur on no fundamental news. A short position carries real squeeze risk; a long position carries trend and solvency risk. Position sizing should reflect both.
6. **Factor crowding: low.** STLA is abandoned by momentum and quality screens — the opposite of crowded. Any re-rating would come from a genuine trough in the estimate ladder, not flows.
7. **Liquidity: not a concern.** Daily volume 15–60M shares, $11B+ market cap. Execution is fine.

**What would flip the signal:** two consecutive quarters of *positive* operating cash flow plus stabilization of the FY2027 EPS estimate (currently €0.93 with a 0.39–1.52 range — that dispersion is the market admitting it has no idea). Until then, the numbers do not support the cheapness story.
