# Quant Analyst

- Symbol: TEVA
- Elapsed: 58.0s

---
# TEVA — Quantitative Factor & Risk Report
**Teva Pharmaceutical Industries (NASDAQ: TEVA)** · Healthcare / Drug Mfrs – Specialty & Generic · Price $34.22 (last close 2026‑02‑20) · Mkt cap ≈$39.8B at that price

---

## 1. Factor Scores Table

Sector ranks are computed cross‑sectionally against 7 large‑cap pharma peers from the Healthcare universe (JNJ, ABBV, MRK, AMGN, GILD, NVS, LLY). Rank 1 = best of 8.

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 32.4 · EV/EBITDA 18.9 · P/FCF 39.7 · P/B 5.8 | **6 / 8** (P/E 6th, EV/EBITDA 6th, P/FCF 7th) | **Negative** — bottom‑quartile. Cheap vs nothing here; peer median P/E ≈24.6, EV/EBITDA ≈16.8. Only LLY/ABBV more expensive. |
| **Momentum (12‑1)** | **+7.91%** | **3 / 8** | **Positive** — top tercile. Peers: ABBV +14.6, GILD +13.6, **TEVA +7.9**, MRK +7.8, AMGN +5.7, LLY +5.5, JNJ +1.2, NVS −0.4 |
| **Quality** | ROE 17.8% · GP/Assets **0.219** · Accruals −0.006 · Piotroski **8/9** | **7 / 8** (GP/A last, ROE 7th, accruals 5th) | **Negative on level, strongly positive on trend** |
| **Low Vol** | Ann. vol **36.8%** · β 0.649 (252d) | **8 / 8** (highest vol of peer set) | **Negative** — no defensive cushion |
| **Earnings Revision** | **+9.7%** (2030E EPS 4.13 vs 3.76 3m prior) | **3 / 7** | **Positive but low confidence** (see caveats) |

**Factor detail**

- **Value is the weakest pillar.** TEVA pays nothing for cash flow: P/FCF 39.7 vs NVS 16.9, GILD 22.5. Generic‑drug economics (high COGS, litigation overhang) have not been rewarded with a discount it can compound out of.
- **Quality is bifurcated.** The level is poor — gross profit/assets of 0.219 is dead last in the peer group (LLY 0.481, GILD 0.393, NVS 0.387) because COGS consumes 51.8% of revenue. But the *trajectory* is textbook turnaround:

  | FY | Revenue | Gross margin | ROIC | ROE | Net income |
  |---|---|---|---|---|---|
  | 2022 | — | — | −7.28% | −28.45% | −$2,446m |
  | 2023 | $15,845m | 48.2% | +1.53% | −6.88% | −$559m |
  | 2024 | $16,544m | 48.7% | −1.27% | −28.65% | −$1,639m |
  | **2025** | **$17,258m** | **51.8%** | **+8.53%** | **+17.82%** | **+$1,410m** |

  Piotroski F‑Score **8/9** (only fail: share count rose — 1,131m → 1,163m diluted). Accruals ratio −0.006 → clean, cash‑backed earnings (OCF $1,649m > NI $1,410m).

---

## 2. Price & Risk Statistics

| Metric | 504‑day (2y) | 252‑day (1y) |
|---|---|---|
| Annualised return | **+63.41%** | — |
| Volatility | 37.99% | 36.83% |
| **Sharpe** | **1.669** | 0.649 (approx.) |
| **Sortino** | **2.983** | — |
| Beta vs SPY | 0.717 | 0.649 |
| Alpha (annualised, OLS) | **+52.17%** | — |
| R² vs SPY | **0.0597** | — |
| Max drawdown | **−21.79%** | −17.61% |

**Read‑through:** Sortino 2.98 vs Sharpe 1.67 means almost all the return came from upside capture with limited downside deviation — the drawdown profile (−21.8% worst 2y) is remarkably contained for a stock compounding at 63% annualised. Alpha of +52%/yr with beta 0.72 is a huge idiosyncratic (turnaround re‑rating) return, not market beta.

---

## 3. Composite Quant Signal

### **NEUTRAL → HOLD** (momentum‑positive tilt; not a factor‑model Buy)

Weighting the framework: Value 6/8, Quality 7/8, Low‑Vol 8/8, Momentum 3/8, Revision 3/7.

- **Three of five factors rank in the bottom quartile.** Under a strict multi‑factor screen TEVA does *not* qualify — it is neither cheap, nor high‑quality on levels, nor defensive.
- The **only** genuine factor support is momentum + a strong Piotroski/ROIC inflection, i.e. this is a **turnaround‑momentum trade, not a value or quality holding**. That is a narrower, more fragile thesis than a top‑quintile‑on‑three‑factors name.
- Risk‑adjusted performance is excellent (Sharpe 1.67, Sortino 2.98) which argues *against* a Sell — money is being made with controlled drawdowns.

---

## 4. Key Quant Risk Flags

1. **⚠️ Alpha is not statistically reliable.** R² = 0.0597 — the market explains only ~6% of TEVA's variance. A 52% annualised alpha on an R² of 0.06 carries a standard error so wide the point estimate is essentially uninformative. Do not quote the alpha as an established skill premium; it is an unmodelled idiosyncratic re‑rating. Beta estimates are correspondingly unstable (0.65 over 252d vs 0.72 over 504d vs 0.842 from the profile feed).

2. **⚠️ Momentum reversal / near‑term overbought.** The 12‑1 score of +7.91% badly understates what has actually happened: TEVA closed **$20.06 on 2025‑10‑01 and $34.22 on 2026‑02‑20 (+70.6% in ~4.7 months)**, including a +9.1% move in the last 21 trading days alone. The 12‑1 metric is depressed by a sharp mid‑2025 drawdown. Translation: the stock is **short‑term extended**, and the 12‑1 factor reading is stale/artificially low. A pullback toward the $30–31 breakout shelf would be the normal mean‑reversion path.

3. **⚠️ Highest volatility in the peer group.** 36.8% annualised vol is 60%+ above JNJ (22.5%) and above LLY (33.9%). There is **no low‑vol factor support** — this cannot serve as a defensive healthcare position, and beta‑to‑SPY understates true risk because the risk is idiosyncratic.

4. **⚠️ Estimate revision signal is low quality.** The revision metric compares the **FY2030** consensus (EPS $4.13 vs $3.76) with **only 2 analysts** contributing (5 on revenue). A +9.7% "upgrade" from a two‑analyst far‑forward number is statistically fragile and is not comparable to peers with deeper coverage. More importantly, the near‑term curve is **non‑monotonic**: FY2025E $2.63 → **FY2026E $2.07 (an implied −21% decline)** → FY2027E $3.13 → FY2028E $3.50. The forward year is a step *down*, which is the opposite of a clean upward‑revision staircase. (Consensus is non‑GAAP; FY2025 GAAP diluted EPS was $1.21.)

5. **⚠️ Data integrity flag.** Pricing feeds disagree: valuation ratios were computed off **$39.23** while the OHLC series closes at **$34.22** on 2026‑02‑20 (~15% gap, presumably differing effective dates). On $34.22 the multiples would be roughly P/E 28.3, P/B 5.0, P/FCF 34.7 — still mid‑to‑bottom of the peer group on value, so the ranking conclusion is unchanged, but quote multiples only with the price explicitly stated.

6. **Liquidity: not a concern.** ~8–19m shares/day, $45.9B market cap, $59.5B EV. Factor crowding is low — TEVA is under‑owned in quant long books precisely because it fails quality screens, which is arguably why the momentum leg has run so far.

---

**Bottom line:** A high‑conviction *price* story (Sharpe 1.67, Sortino 2.98, Piotroski 8, ROIC −1.3% → +8.5%) sitting on a *low‑conviction factor* foundation (bottom‑quartile value, quality level and low‑vol). **Neutral/Hold** — factor‑model support is insufficient for a Buy, and the risk‑adjusted return record is too strong for a Sell. Verdict hinges on whether FY2027–28 EPS recovery (the far‑forward upgrade) survives scrutiny, not on any current factor reading.
