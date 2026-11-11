# Quant Analyst

- Symbol: FSLR
- Elapsed: 48.5s

---
# FSLR — Quantitative Factor & Risk Assessment
*First Solar, Inc. | Energy / Solar | Price $180.98 | Mkt Cap $19.45B | Employees 7,900*

## 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 12.7 · EV/EBITDA 7.9 · P/FCF 16.4 · P/B 2.04 | **1 of 4** (vs XOM/CVX/COP) | **Strongly positive** |
| **Momentum (12-1)** | **−19.8%** | 3–4 of 4 (est.; peer data n/m) | **Negative** |
| **Quality** | ROE 16.0% · ROIC 15.9% · GP/Assets 0.159 · Accruals −0.040 | **2 of 4** | Mixed-positive |
| **Low Vol** | σ 53.1% · β 1.44 | **4 of 4** (worst) | **Strongly negative** |
| **Earnings Revision** | **−10.3%** (2030E: $34.01 → $30.51) | n/m | **Negative** |

**Value detail.** Cheapest name in the Energy cohort on 2 of 3 multiples — lowest P/E (12.7 vs 21.4–31.9), lowest P/FCF (16.4 vs 23.5–30.0), second-lowest EV/EBITDA (7.9 vs COP's 7.3). FCF yield ≈ **6.1%**; EV $17.1B sits *below* market cap of $19.5B — a net-cash balance sheet.

**Quality detail.** ROE of 16.0% is the highest in the cohort; GP/Assets 0.159 is mid-pack (CVX 0.173). Piotroski **F-Score 7/9 (Moderate)** — fails only on share dilution (F7) and gross-margin improvement (F8). Accruals ratio −3.97% (cash earnings *exceed* reported income — good quality, though a −11.1% reading in 2022 shows volatility). Multi-year ROIC trajectory: −0.5% (2022) → 11.7% → 16.0% → 15.9% — a genuine structural improvement, now plateauing.

**Revision detail — flag.** The tool compares a 2030 current estimate ($30.51) against a prior of $34.01. That prior figure is *identical* to the current 2029 consensus ($34.011), which strongly suggests a **period-mismatch artifact** rather than a true 90-day cut for the same forward year. Treat the −10.3% magnitude as unreliable. The direction is nonetheless corroborated by the term structure: consensus 2030 EPS ($30.51) is **below** 2029 ($34.01), i.e., the out-year is being modelled as an earnings decline — unusual and a genuine yellow flag. Coverage is deep (25 analysts).

## 2. Price Statistics

| Metric | 252d (1Y) | 504d (2Y) |
|---|---|---|
| Annualised return | −12.4% | n/a |
| Alpha vs SPY (annualised) | **−34.3%** | **−1.9%** |
| Beta vs SPY | 1.451 | 1.507 |
| R² | 0.155 | 0.120 |
| Sharpe (rf = 0%) | −0.233 | +0.464 |
| Sortino | −0.345 | n/a |
| Annualised volatility | 53.2% | 55.3% |
| Max drawdown | **−47.2%** | −47.2% |

**Interpretation.** The two horizons tell one consistent story: FSLR's returns are **almost entirely idiosyncratic**. R² of 0.12–0.16 means only ~13–15% of variance is explained by the market — alpha and beta estimates here have wide standard errors and should be read as directional, not precise. The beta (1.45–1.51) is nonetheless stable across windows and well above the company-reported 1.71 vs. the peer group's ~0.8–0.9. Sharpe is negative over 1Y and only 0.46 over 2Y — poor compensation for 53–55% volatility. Sortino (−0.345) is *worse* than Sharpe, meaning downside deviation dominates: losses are fatter than gains. The −47.2% max drawdown is unmitigated over both windows — i.e., it has not been recovered.

**Peer correlation (252d) is the standout finding:**

| | FSLR | XOM | CVX | COP | SPY |
|---|---|---|---|---|---|
| **FSLR** | 1.00 | **−0.20** | **−0.22** | **−0.21** | 0.39 |

FSLR is *negatively* correlated with every large-cap Energy peer — it is not an energy stock in factor terms; it trades on solar policy, tariffs, and module pricing. Note also that XOM/CVX/COP show **negative correlation to SPY (−0.36 to −0.38)**, which is economically implausible and almost certainly a data/sample artifact. I therefore discount the absolute correlation levels, but the *relative* pattern (FSLR decorrelated from oil majors) is robust.

## 3. Composite Quant Signal: **NEUTRAL** (negative tilt)

Value and quality are genuinely attractive — top-quartile cheap on cash-flow multiples with a net-cash balance sheet and improving ROIC. But the three forward-looking factors all point down: **negative 12-1 momentum, negative estimate revisions, and bottom-quartile volatility with a negative 1-year Sharpe and −34% alpha.** Under a standard equal-weight multi-factor score, cheapness does not offset that combination. Not a Sell — the balance sheet and FCF yield provide a valuation floor and there is no distress signal (F-Score 7, accruals negative). But this fails the "top quintile on value, momentum AND quality" test: momentum is bottom-quintile.

## 4. Key Quant Risk Flags

1. **Momentum reversal risk — highest priority.** 12-1 momentum is −19.8%, but the trailing 63-day return is **+5.0%**. That divergence (a stock turning up inside a one-year downtrend) is the classic setup for either a genuine reversal *or* a dead-cat bounce. With β 1.45, a failed bounce carries outsized downside. Position sizing, not conviction, is the right response.
2. **Negative alpha is the core problem.** −34.3% over 1Y and still −1.9% over 2Y despite a 53% vol and 1.5 beta. Investors have been paid nothing for taking enormous risk. Until alpha turns positive on a 1Y window, the cheapness is a value trap candidate, not a catalyst.
3. **Factor crowding is *not* a risk here — the opposite.** Correlation to Energy peers is negative (−0.20 to −0.22) and R² to the market is only 0.12–0.16. This is an idiosyncratic, policy-driven single-name bet (tariffs, IRA/45X credits, trade policy). It offers genuine diversification against an Energy book but cannot be hedged with an XLE short.
4. **Downside deviation dominates** — Sortino (−0.345) worse than Sharpe (−0.233); 47% peak-to-trough drawdown unrecovered.
5. **Data-quality caveats:** (a) the EPS revision series has an apparent forward-period mismatch — treat the −10.3% as direction-only; (b) analyst coverage thins with horizon (25–30 analysts on 2027–2028, but the out-year 2030 estimate implies an EPS *decline* vs. 2029, suggesting limited agreement at the tail; (c) 2025 revenue consensus ($5.11B) exceeds 2026 ($4.79B) — an inconsistent term structure worth verifying against guidance; (d) the SPY/oil-major negative correlation implies sample or alignment error; (e) 252d ≈ 1 regime — **statistical significance is limited**, and the alpha/beta figures should carry wide confidence bands given R² near 0.13.
6. **Liquidity:** no constraint — $19.5B cap and index membership imply deep trading. Not a risk.

**Recommendation for the memo:** Quant stance is **Neutral / size-down**. The value-plus-quality case is real and measurable; the momentum, revision, and risk-adjusted-return evidence is uniformly negative. The trade is a *catalyst-dependent* value position, not a quant buy. Re-underwrite if 12-1 momentum crosses zero or if 2026–2027 consensus EPS revises upward — those are the two conditions that would flip this to Buy.
