# Quant Analyst

- Symbol: JPM
- Elapsed: 124.8s

---
`rank_universe_by_factor` is dead both ways (schema demands a string, validator demands a list) — noting the gap and moving on. I have everything needed from direct peer ratios. Writing the report now.

---

# JPMorgan Chase (JPM) — Quantitative Factor Report
**As of 2026-08-14 | US Money Center Bank | Mkt Cap ≈ $919B (profile ref. price $343.06; latest tape $362.84)**

*Note on reference prices:* valuation multiples below are computed off the profile's $343.06 snapshot; mark-to-tape $362.84 would scale P/E to ≈18.1 and P/B to ≈2.79.

## 1. Factor Scores

| Factor | Score | Signal | Peer Context (JPM / BAC / WFC / C) |
|--------|-------|--------|--------------------------------------|
| Value | **Neutral (−)** | Rich on every book-based metric | P/E 17.1 (14.8/13.1/19.2); **P/B 2.64 (1.41/1.46/1.17)**; EV/EBITDA 5.2 (neg/7.5/12.0); P/FCF −6.5 (bank FCF artifact); DY 1.79% |
| Momentum | **+7.45%** (12–1m, 252d) | Positive, moderate | 2nd of 4 banks (BAC +7.6%, WFC +0.5%, C −6.7%) |
| Quality | **Low / deteriorating** | Negative trend, high absolute level | ROE 15.7% (down from 17.0%); ROIC 5.6% (down 4yr avg 6.1%); gross profit/assets 3.8%; **accruals 0.046, up 4 straight yrs (−.019→.009→.025→.046)**; Piotroski **4/9 (Weak)**; peers: BAC 6/9, WFC 4/9 |
| Low Vol | **Vol 22.4%, β 0.77, maxDD −15.5%** | Positive | Sub-1.0 beta is genuine for a mega-cap; moderate vol |
| Earnings Revision | **+8.5% upgrade** (fwd-year EPS 27.26 vs 25.14 prior) | Strong positive | Consensus ladder $20.20 (25A) → 24.77 (26E) → 25.14 (27E) → 27.26 (28E), all rising; targets raised across street (UBS $400, WF $390, DB Buy $375, RBC $370, Truist $352) |

## 2. Price Statistics (252 trading days vs SPY; 0% rf)

| Metric | Value |
|--------|-------|
| Alpha (annualised) | **+1.35%** — positive but low-confidence (R² = 0.20) |
| Beta vs SPY | **0.77** |
| R² vs market | **0.20** (only 20% of variance explained → alpha/beta estimates noisy) |
| Sharpe | **0.545** (0.73 per vol-tool approx) |
| Sortino | **0.773** |
| Ann. return / vol | +12.3% / 22.5% |
| Max drawdown | **−15.5%** (Jan-2026 peak ~$331 → Mar-2026 trough $280) |
| Peer correlation (1y) | BAC 0.80, WFC 0.74, C 0.70, MS 0.66, GS 0.63 — high sector co-movement |

## 3. Composite Quant Signal: **BUY** (not Strong Buy)

Two factors are outright negative/neutral (Quality trend, Value), three positive (Momentum, Low-Vol, Earnings Revision). The revision story is the strongest input: consensus EPS rising every reported year + a wall of raised price targets above spot. But this is an expensive, quality-premium stock whose earnings-quality metrics are deteriorating even as the tape runs to records — that caps conviction.

## 4. Key Quant Risk Flags

1. **Momentum-reversal risk:** 12–1 momentum (+7.5%) lagged a +23% run over the last ~8 weeks to all-time highs. The 12–1 signal only just caught up; extended momentum + crowded bank complex = mean-reversion pullback risk.
2. **Earnings-quality deterioration:** accruals ratio 0.046 and rising for the 4th consecutive year; F-score 4/9 (negative op. cash flow, no ROA improvement, no deleveraging). If the accrual build is real (not bank CF accounting noise), reported profitability is running ahead of cash conversion — the single most likely source of a downgrade surprise.
3. **Factor crowding:** 0.70–0.80 correlation with money-center peers; JPM's low-beta protection evaporates in a rates/credit-shock episode. Alpha (+1.35%) is not statistically distinguishable from 0 at R² = 0.20 — do not underwrite alpha.
4. **Valuation premium:** P/B 2.64 vs ~1.2–1.5 for peers means JPM carries the full quality premium; the value factor offers no margin of safety. Negative P/FCF (FCF model artifact for banks) — treat as uninformative, not a signal.
5. **Statistical caveats:** alpha/beta estimated on 252 obs with R²=0.20; earnings-revision tool compares different forward periods (2028E vs 2027E), so the +8.5% is directional. Peer universe ranks unavailable (`rank_universe_by_factor` tool broken — schema/validator conflict); sector ranking above is computed directly from peer ratios, not a full-universe quintile.

**Bottom line:** The numbers support a Buy on momentum + revisions + low beta, but not a Strong Buy — the market already prices the premium, and the accruals/Piotroski deterioration is a real canary. Anyone long here is short future earnings quality surprises.
