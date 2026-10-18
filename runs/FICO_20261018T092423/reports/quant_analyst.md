# Quant Analyst

- Symbol: FICO
- Elapsed: 53.7s

---
# FICO — Quantitative Factor & Risk Report
**As of latest close 2026-04-15: $1,030.81 | Mkt cap ≈ $25.3B (24.56M diluted sh) | EV ≈ $28.3B**

⚠️ **Data integrity note:** the valuation-ratio tool returned a stale price of $771.19 (implying $18.9B cap). I recompute all multiples at the $1,030.81 close using its reported FY-end share count, EBITDA, and net debt ($2.94B). Short-window betas are also unstable (see §2) — read them as "no measurable market sensitivity," not as low risk.

## 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| Value | **−0.2** (neutral) | ~40th pct | Neutral — 35.0x trailing P/E, 26.9x EV/EBITDA, but 24.1x FY26E / 21.0x FY27E on +45% EPS growth (PEG ≈ 0.54) |
| Momentum | **−2.0** | Bottom decile | **Strongly negative** — 12-1m −25.8%, 6-1m −14.5% |
| Quality | **+1.8** | Top decile | **Strong** — ROIC 69.6%, ROA 34.9%, GP/assets 0.876, accruals −0.068, Piotroski 7/9 |
| Low Vol | **−2.0** | Bottom decile | **Severe** — 68.6% vol (252d), 90.3% (63d), max DD 64.4% |
| Earnings Revision | **−0.3 (unverified)** | n/a | Tool reported +19.0%, but period-mismatched — see below |

**Composite Quant Signal: NEUTRAL (−0.54).** High-quality business, poor price factors, unverified revisions. A price-only composite would score **Sell**.

### Factor detail
- **Value:** trailing multiples are inflated by a depressed FY25 base (EPS $29.49). Forward multiples are the correct lens and are attractive *if* FY26 consensus holds: revenue $2.54B (+27%), EBITDA $1.44B, EPS $42.80 (+45%). EV/EBITDA falls 26.9x → 19.6x. No P/B — **book value per share is −$71.08**.
- **Quality — the composite tool is wrong.** It scored "low" solely because ROE = −37.3%, which is an arithmetic artifact of **negative shareholders' equity** from sustained buybacks (ROE has been −47% to −62% for four years while ROIC rose 48.9% → 69.6%). On the metrics that are not distorted — ROIC, ROA, gross profit/assets, accruals (negative = high earnings quality) — FICO is top-decile. Piotroski 7/9, docking exactly the two items driven by negative equity and leverage (F5, F6).
- **Earnings Revision — do not use the reported +19.0%.** The tool compared the FY2030 estimate ($62.78) against the FY2029 estimate ($52.76): a horizon mismatch, and the 2030 figure rests on **1 analyst**. Nearer term, FY26 consensus is unusually tight (13 analysts, $42.32–$43.42, ~2.6% band) and implies +45% growth, but I cannot verify the 3-month *direction* of change. **Revision momentum is genuinely unresolved.** Dispersion explodes further out (FY28: $32.34 low vs $70.20 high) — the analyst community has no consensus on the post-2026 path.

## 2. Price Statistics

| Metric | 252d | 126d | 63d |
|---|---|---|---|
| Alpha (ann., vs SPY) | **−80.7%** | −51.8% | — |
| Beta | 0.37 | −0.13 | −0.42 |
| R² | **0.005** | 0.0004 | — |
| Ann. volatility | 68.6% | 76.8% | **90.3%** |
| Sharpe | −0.92 (−1.10) | −1.19 | −1.64 |
| Sortino | −0.97 | −1.23 | — |
| Ann. return | −63.5% | −91.7% | — |
| Max drawdown | **−64.4%** | — | −56.9% |

**Statistical caveat — critical:** R² of 0.005/0.0004 means the beta and alpha estimates are **not statistically distinguishable from noise**. All 12-month return variation is idiosyncratic, not market-driven. Sharpes assume a 0% risk-free rate, which overstates the negative ratios modestly. Negative Sortino worse than negative Sharpe confirms losses are large *and* downside-clustered. Max drawdown of −64% (peak ~$2,550 → trough $909 on 2026-04-10) exceeds the annualized vol, indicating a gap-driven, event-based decline rather than drift.

## 3. What the tape says (verified)
Price path is real, not a split artifact: $1,512 (Oct 1) → **+18% to $1,785 (Oct 2)** on the direct-to-lender FICO score pricing model, then a grinding −40% decline to ~$1,030. Sharp gaps: −16.7% on 2026-04-10 (1.09M sh, 3x ADV), −9.4% on 2026-03-11. The driver is structural, not cyclical: the mortgage-score distribution monopoly is being contested (VantageScore / industry shakeup). That is a **regime break in the Scores segment**, which is not something a momentum model can see but which explains why value and momentum disagree.

## 4. Key Quant Risk Flags
1. **Structural/regulatory risk to the Scores moat** — the single largest risk, and it invalidates the 4-year quality trend as a forward predictor.
2. **Momentum reversal + factor crowding** — the former high-multiple momentum favorite is now unwinding; vol has *risen* (68.6% → 90.3%) as price fell, the classic signature of a crowded long de-grossing.
3. **Beta is unmeasurable (R² ≈ 0)** — FICO offers no diversification benefit; SPY-hedged positions will not offset it.
4. **Negative book equity** — no P/B or book-value floor; ROE is unusable. Do not feed this name into a naive quality screen; it will be misclassified as low quality.
5. **Estimate dispersion widening with horizon** (FY28 range $32–$70) — forward multiples I quote carry wide error bars.
6. **Vendor data staleness** (price off by 25%) — any third-party screen run on the stale $771 print understates multiples; flag for replication.
7. **Liquidity is adequate** (~$350M/day notional) but gap risk in a 1.0M-share down day is material; size positions to the gap, not to ADV.

**Bottom line:** a top-decile quality asset in a bottom-decile price regime, priced at a discount only if consensus growth survives a genuine competitive threat. Sample sizes here are adequate in days (252) but degenerate in explanatory power (R² ≈ 0) — I would not underwrite the negative alpha as skill/lack of skill, only as realized outcome. **Neutral; would upgrade on two consecutive positive FY26/FY27 revision cycles, downgrade to Sell on another close below $909.**
