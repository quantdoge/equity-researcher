# Quant Analyst

- Symbol: FDXF
- Elapsed: 41.9s

---
# FDXF — FedEx Freight Holding Co. | Quantitative Factor Report

**Critical data caveat up front:** FDXF is a June 2026 spin-off from FedEx. Genuine trading history is only **~105 sessions (2026-06-01 → 2026-10-30)**. The three pre-separation prints (May 27–29: $135→$185→$160 on 6k–15k shares) are thin indicative markings and must be discarded. Every "252-day" statistic below is therefore computed on **~107 observations, not 252**, and includes stub-distortion. Treat all risk metrics as **directionally indicative only — statistically insignificant.** Current price: **$126.04**.

---

## 1. Factor Scores

The scoring tools return raw values; I map each to a 0–100 percentile read and rank against the only valid peer set (FedEx `FDX`, UPS — the 3-name Integrated Freight & Logistics bucket). Full-sector quintile ranking was *not* run, so "rank" = rank of 3.

| Factor | Raw Value | Score (0–100) | Sector Rank (of 3) | Signal |
|---|---|---|---|---|
| **Value** | P/E 28.8; EV/EBITDA 18.0; P/FCF −88.9 (neg FCF); P/B n/m (neg equity) | 10 | **3rd** (worst) | **Expensive** — trades at ~1.9× UPS/FDX EV/EBITDA despite *worse* fundamentals |
| **Momentum** | 12-1 return **−27.1%** vs UPS −17.2%, FDX −7.6% | 5 | **3rd** (worst) | **Negative** — down ~35% from June high ($194); persistent downtrend |
| **Quality** | ROIC 9.2% (from 49%→35%→9.2%); accruals 7.1% (>5% = poor); Piotroski F **3/9** | 25 | **3rd** | **Low/Weak** — collapsing profitability, cash conversion worsening |
| **Low Volatility** | Ann. vol 64.8%; beta −0.20; R² 0.0015; max DD 42.7% | 15 | **3rd** (highest vol) | **High risk** — worst vol in group |
| **Earnings Revision** | 2030 EPS $7.64 vs $6.58 3mo prior = **+16.1%** | 55 | 2nd | **Weak upgrade** — long-dated, 3 analysts, low signal quality |

**Peer multiple check (why Value is the standout negative):**

| | FDXF | UPS | FDX |
|---|---|---|---|
| P/E | **28.8** | 16.5 | 16.9 |
| EV/EBITDA | **18.0** | 9.6 | 9.4 |
| P/FCF | **neg (−88.9)** | 19.3 | 14.6 |
| Div yield | 0% | 6.1% | 1.7% |
| ROIC | 9.2% | 17.5% | 8.9% |

FDXF pays a ~90% EV/EBITDA premium to both peers while earning peer-level ROIIC and burning cash. LTL pure-plays (e.g. ODFL) do command higher multiples, but not on **EBITDA falling 44% in two years** ($2,483M→$1,863M→$1,390M).

---

## 2. Price Statistics (vs SPY, ~107 obs — low confidence)

| Metric | Value | Read |
|---|---|---|
| Alpha (annualized) | **−21.1%** | Not significant (R² 0.0015) |
| Beta | **−0.20** | Economically implausible for a cyclicals trucker; **R² 0.0015 means beta is statistically meaningless** |
| Annualized volatility | 64.8% | Inflated by 3 stub sessions; true vol likely ~40–50% |
| Sharpe | **−0.336** | Negative — no risk-adjusted reward |
| Sortino | **−0.635** | Negative downside-adjusted return |
| Annualized return | −21.8% | Over the ~5-month life |
| Max drawdown | **−42.7%** | Peak $194 (Jun 9) → $108 (Oct 27) |

Note: the company profile's `beta = −7.34` is a **data error** and should be disregarded. The R² of 0.15% means returns are essentially uncorrelated to the market — idiosyncratic spin-off trading, not factor-driven.

**Fundamental trajectory (annual, $M):**
- Revenue: 9,424 → 8,887 → **8,795**
- Operating income: 1,753 → 1,339 → **540** (−69% in 2yrs)
- Net income: 1,574 → 1,079 → **655**
- Diluted EPS: 12.54 → 8.88 → **4.38**
- Equity: **negative** (BVPS −$3.32) → ROE −131.8% is an artifact of the leveraged spin-off, not a valid profitability read

---

## 3. Composite Quant Signal: **SELL**

Four of five factors rank **last of peer set**; the lone positive (revision) is long‑dated and thin. On factor logic alone this scores in the bottom quintile. I stop short of "Strong Sell" only because (a) the sample is too short for statistical confidence, and (b) the stock is already −35% from its high, raising near-term mean-reversion/capitulation risk on the developing long-range EPS recovery (FY27 $4.67 → FY30 $7.64 consensus). The **quality and value signals are unambiguously negative**, so the burden of proof is on the bulls.

---

## 4. Key Quant Risk Flags

1. **Statistical insignificance (top risk):** ~105 trading days vs. 252 assumed; 3 stub prints contaminate vol/beta/alpha/Sharpe. Do not size positions off these risk metrics.
2. **Value trap / premium mismatch:** 18× EV/EBITDA on EBITDA down 44% — de-rating risk if LTL recovery slips; peers trade at ~9.5×.
3. **Negative FCF & weak accruals:** P/FCF −88.9 (≈ −$212M FCF) with 7.1% accruals → earnings not converting to cash; F-score 3/9.
4. **Negative equity / ROE distortion:** ROE/Methods screens will misread this name; use ROA (9.5%) and ROIC (9.2%) instead.
5. **Momentum-reversal / thin-float overhang:** post-spinoff supply and low liquidity (sub-$1M/day on many sessions) amplify drawdowns — 42.7% peak-to-trough already realized.
6. **Earnings-revision quality:** +16% "upgrade" is a 4-years-out, 2–3 analyst estimate — negligible predictive weight for a 12-month horizon.

**Bottom line:** On clean factor ranks, FDXF is **expensive, deteriorating, high-volatility, and in negative momentum** — a bottom-quintile quant profile. Signal: **Sell**, with an explicit small-sample health warning on all price-derived statistics.
