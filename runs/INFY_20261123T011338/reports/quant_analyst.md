# Quant Analyst

- Symbol: INFY
- Elapsed: 59.7s

---
## INFY — Quantitative Factor & Risk Scorecard
**Price $12.03 (close 2026‑11‑20) · Mkt cap ~$48.1B · 3.996B sh · Technology / IT Services · ADR (India)**

### 1. Factor Scores

| Factor | Score (−2…+2) | Sector Rank | Signal |
|---|---|---|---|
| Value | **+0.5** | 2 of 5 (IT‑svcs peer set) | Attractive (mild) |
| Momentum | **−1.5** | 5 of 5 (worst) | Negative |
| Quality | **+1.5** | 1 of 5 (best) | Strong |
| Low Vol | **+0.3** | 1 of 5 (lowest vol) | Positive — *unreliable, see flags* |
| Earnings Revision | **+0.2** | 3 of 4 valid | Mild upgrade |

**Value (raw):** P/E 14.49, EV/EBITDA 8.87, P/FCF 12.88, P/B 4.89 vs ACN 16.31/9.78/11.76, CTSH 12.73/6.88/10.94, IBM 20.09/15.37/17.59 (WIT excluded — its P/E of 0.16 and negative EV/EBITDA are data errors). INFY sits below peer-median on P/E and EV/EBITDA, marginally above on P/FCF. **Sector rank 2/4 on multiples.**

**Momentum (raw):** 12‑1 month −0.49% (tool) → **bottom of peer group** (ACN +40.8%, CTSH +19.7%, WIT +7.7%, IBM +6.9%). Price‑verified recomputation from the OHLC series gives a *worse* reading: 12.93 (10‑22‑26) vs 16.39 (11‑20‑25) = **−21.1%**. Six‑month momentum +14.2% (tool) / **−1.6%** (recomputed, 12.22 → 12.03) — the tool's positive 6‑month figure does not reconcile with the raw tape and should not be relied on.

**Quality (raw):** ROE 33.67% (best of 5), gross‑profit/assets 0.370 (best of 5, Novy‑Marx), accruals −4.41% (earnings backed by cash; 2nd best after ACN −5.43%). ROIC 37.8% (4‑yr 33.0–37.8%, stable/high). Piotroski F‑Score **6/9** — strengths: positive ROA, positive OCF, ROA improvement, clean accruals, no dilution, rising asset turnover; **failures: leverage up (F5), equity change negative (F6), gross margin not improving (F8)**.

**Low Vol:** 40.25% annualised vol vs ACN 53.5%, CTSH 45.9%, WIT 48.3%, IBM 51.9% — lowest of the set. Beta vs SPY −0.084 (profile 0.131).

**Earnings Revision:** FY2030 EPS 0.91289 vs 0.88629 three months prior = **+3.0% (upgrade)**, but only **14 analysts** on the far‑dated year (vs 31 on FY29). Peer revisions: ACN +12.1%, WIT +6.5%, INFY +3.0%, CTSH −7.5%. Long‑run EPS path 0.744 (FY25) → 0.762 → 0.803 → 0.840 → 0.886 → 0.913 = **~4.2% CAGR**; revenue 19.13B → 23.59B (~4.3% CAGR). Thin growth, mildly improving.

### 2. Price Statistics (252d, vs SPY, rf = 0)

| Metric | Value | Note |
|---|---|---|
| Alpha (ann.) | **−12.4%** | t ≈ −1.9; **not significant** (R² = 0.001) |
| Beta | **−0.084** | R² 0.001 → estimate is economically meaningless |
| Ann. volatility | **40.25%** | high absolute risk |
| Sharpe (1y) | **−0.121** (tool) | restated ≈ **−0.61** on actual −24.4% total return |
| Sortino (1y) | **−0.193** (tool) | restated ≈ −0.8 (more downside vol than total vol) |
| Max drawdown | 28.75% (tool) / **−44% to −47%** (recomputed: 18.35–19.35 peak → 10.27 trough) | |
| 52‑wk range (close) | 10.26 – 19.35 | price at **19th percentile** of range, +17.2% off low |
| 6‑mo Sharpe / Sortino | 1.17 / 2.14 (tool) | **discard** — implies +48% ann. return vs −1.6% actual |

Correlation (252d): INFY–ACN 0.77, INFY–CTSH 0.77, INFY–IBM 0.47, INFY–WIT 0.42. High co‑movement with US IT services but near‑zero measured market beta — internally inconsistent.

### 3. Composite Quant Signal: **NEUTRAL** (Quality/Value buy vs Momentum sell)
Weighted composite ≈ **+1.0** on a −8…+8 scale: top‑quintile **quality** (ROE 33.7%, ROIC 37.8%, negative accruals) and 2nd‑of‑5 **value** are offset by **bottom‑of‑peer momentum** (−21% 12‑1) and a **non‑significant, strongly negative alpha** (−12.4%). Positive 3‑month price action (+14% off the June low, two analyst PT raises in late Oct 2026: BMO $12→$13, TD Cowen $9→$11) hints at trend inflection, but this is unconfirmed — once momentum turns positive this flips to Buy. This is the classic **quality‑value + negative‑momentum = value‑trap risk** profile.

### 4. Key Quant Risk Flags
1. **Momentum reversal / value‑trap risk** — worst 12‑1 momentum in the peer set (−21% recomputed), 19th percentile of 52‑wk range.
2. **Data‑integrity flag (material):** β ≈ 0 with R² = 0.001 and 40% vol is mathematically implausible for an ADR with 0.77 correlation to ACN — ADR/local session misalignment. **Do not feed this beta into a cost of equity.** Reported dividend yield 8.79% is also implausible against P/E 14.49 and EPS 0.762 (~60% payout implies ~3.8%); treat as artifact. The 2025‑12‑19 intraday print of $28.71 (open $18.26, 118M shares) is a bad tick.
3. **Reconciled vs. tool stats diverge materially** (return −4.8% vs −26.6% actual; max DD 28.8% vs ~−45%). Use the price‑verified figures above.
4. **Estimate fragility:** revision signal rests on a +3.0% move in FY2030 EPS from only 14 analysts; peer CTSH is being cut −7.5%, signalling sector‑wide estimate risk.
5. **Margin/leverage deterioration** — F‑score 6 with negative equity change, rising leverage and flat gross margin.
6. **Liquidity is NOT a concern** (~$200M+ daily traded value); the risk is ADR‑to‑ordinary‑share basis and INR translation, not slippage.
