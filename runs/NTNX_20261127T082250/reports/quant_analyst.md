# Quant Analyst

- Symbol: NTNX
- Elapsed: 64.7s

---
## NTNX — Quantitative Factor & Risk Report
**Price $46.30 (25-Nov-2026) | Mkt cap ~$13.5B | EV ~$12.7B | Technology / Software-Infrastructure**

**Critical data caveat up front:** on 25-Nov-2026 NTNX fell **-15.2%** on ~5.4x normal volume (FQ1 results beat — EPS $0.73 vs ~$0.61, revenue +15% — but FY guidance was soft and the CEO announced his departure). Every trailing score below therefore straddles a major event; the momentum/revision scores are **stale as of the break**.

---

### 1. Factor Scores

| Factor | Score /10 | Sector Rank (of 5 infra comps) | Signal |
|---|---|---|---|
| **Value** | 5.5 | 2nd | Neutral-positive |
| **Momentum** | 3.0 | n/a (peer momentum unavailable) | **Negative — trend broken** |
| **Quality** | 4.5 | 3rd | Neutral |
| **Low Vol** | 3.0 | 3rd | Negative (absolute) |
| **Earnings Revision** | 4.0 | n/a | Deteriorating ex-post |

**Peer set used (n=5):** NTNX, PSTG, CSCO, ANET, DELL. The API's sector list returned only mega-caps (AAPL/MSFT/NVDA), so ranks are against a hand-built infra/storage comparable group — **small-n, indicative only**. PSTG (beta 0.131) and DELL (beta 2.82, vol 92.7%) returned implausible risk stats and were down-weighted.

#### Value — 5.5/10 (rank 2/5)
| Metric | NTNX | CSCO | ANET | DELL | PSTG |
|---|---|---|---|---|---|
| P/FCF | **16.1x** (1st) | 29.4x | 49.2x | 23.8x | n/a |
| EV/EBITDA | 31.7x (3rd) | 19.4x | 45.9x | 18.8x | n/a |
| P/E | 8.97x ⚠️ *artifact* | 28.3x | 59.6x | 34.2x | n/a |

- **Do not screen on the 8.97x P/E.** Net income $1.507B vs EBIT $330M implies ~$1.2B of non-operating income (a deferred-tax valuation-allowance release). **Normalized P/E ≈ 53x** (pre-tax $321M taxed at 21% → EPS ~$0.87).
- Forward multiples are the honest lens: **FY27E 19.2x, FY28E 17.1x, FY29E 14.0x**; EV/FY27E EBITDA **12.1x**; EV/Sales FY27E 4.0x.
- Reported FCF yield 6.2% (P/FCF 16.1x) — but see SBC flag: **SBC-adjusted FCF $483M → true yield 3.6%, P/adj-FCF 28x.**

#### Momentum — 3.0/10 ⚠️
Tool 12-1 score: **+10.4%** ("positive"). That score excludes the last 21 trading days — i.e. it excludes the entire break:

| Window | Return |
|---|---|
| 1 month | **-36.3%** |
| 3 months | **-30.3%** |
| 6 months | -0.5% |
| 12 months | **-21.2%** |
| Last day | -15.2% |

- Peak $72.74 (27-Oct-26) → $46.30 = **-36.3%**; peak $83.07 (19-May-25) → **-44.3%**.
- 12-1 momentum is positive only on paper and **will mechanically flip negative** at the next recalculation. Classic momentum-reversal setup: sharp break on volume after a leadership change.

#### Quality — 4.5/10 (rank 3/5)
| Metric | Value | Rank |
|---|---|---|
| Gross profit / assets (Novy-Marx) | **0.488** | **2/5** (best-in-class) |
| Accruals ratio | **+0.116** | **5/5 (worst)** |
| ROIC FY26 | 12.6% | — |
| ROE | 214% (meaningless — equity $703M vs $3.71B accumulated deficit) | — |
| Piotroski F-Score | **6/9** (Moderate) | — |
| Interest coverage (EBIT/int.) | 36.7x | Strong |

- Gross margin 86.8%; **GAAP operating margin 9.8%, ex-SBC 22.3%**. Profitability is structurally SBC-dependent.
- The **+0.116 accruals flag is mechanical, not deterioration**: net income was inflated by the tax benefit while OCF is cash-real. FY23–FY25 accruals were −0.21, −0.37, −0.19 (OCF consistently >> net income — historically *high* earnings quality). This is why F-Score's accruals component scored 0.
- ROIC series sign-flips (−33% → −23% → +21.9% → +12.6%) because invested capital is near zero/negative — **trend is not interpretable**.

#### Low Vol — 3.0/10 (rank 3/5)
Vol 47.8% annualized (2nd lowest of 5, but **bottom tercile vs the broad universe**); beta 1.011 (2nd lowest); max DD −38.0%; Sharpe 0.64 (4th of 5). Absolute risk is high; it is only "low vol" relative to ANET/DELL/PSTG.

#### Earnings Revision — 4.0/10 (reading 7/10 stale, 2/10 live)
- Tool reading: **+21.7%** (FY2029 EPS $3.297 vs $2.709 prior) — "upgrade." **But it rests on 3 analysts, three fiscal years out** — statistically fragile, and it predates the guide.
- Live evidence is the opposite: **BofA downgraded to Neutral** (PT $62) and targets were cut across the board on 25-Nov: $90→$75 (Needham), $90→$70 (Rosenblatt), →$67 (Piper). Pre-crash targets $85–100; post-crash median **~$68.5** vs $46.30 (**-24% cut**). Revision direction has inflected **negative**.

---

### 2. Price Statistics (252d, vs SPY)

| Metric | Value | Interpretation |
|---|---|---|
| Annualized alpha | **+18.5%** | **Statistically insignificant** (t ≈ 0.4) |
| Beta | **1.016** (SE ≈ 0.19, t ≈ 5.5) | Market-level |
| R² | **0.116** | **88% idiosyncratic** — beta is a poor risk control |
| Sharpe | 0.635 | Mediocre |
| Sortino | 0.831 | Downside dev ≈ 76% of total vol |
| Annualized vol | **47.76%** | High absolute risk |
| Max drawdown (252d) | **-37.96%** | -44.3% from May-25 peak |
| Realized 12m return | **-21.2%** | vs tool "29.93% ann." — **inconsistent, flagged** |

- **Alpha is not usable as evidence of skill/excess return**: with 47% residual vol, one year of data gives an alpha standard error of ~44%. You would need ~6 years of this dispersion to establish significance.
- The tool's +29.93% annualized return conflicts with the actual price series (58.77 → 46.30). Treat Sharpe/Sortino as **indicative only**; internal data inconsistency.

---

### 3. Composite Quant Signal: **NEUTRAL (Hold) — negative tactical bias**
**Composite 4.1/10** (Value 20% × 5.5, Momentum 20% × 3.0, Quality 25% × 4.5, Low Vol 15% × 3.0, Revision 20% × 4.0).

The factor stack is genuinely contradictory: **best-in-class gross profitability (0.49) and cheapest P/FCF in the group** against **worst-in-group accruals, a broken trend, and a just-downgraded estimate path**. Forward valuation (19x FY27, 12x FY27 EBITDA, 14x FY29) is not demanding for a ~25% grower — but the numbers that made this a "cheap" screen (8.97x P/E, 6.2% FCF yield) are both **optically flattered** by a tax benefit and by SBC. Not a Sell (real cash generation, net debt only ~0.98x ex-SBC EBITDA, high gross margins), not a Buy until revision momentum stabilizes.

### 4. Key Quant Risk Flags
1. **Momentum reversal risk — HIGH.** -36% in three weeks on 5.4x volume; the +10.4% momentum score is stale by exactly the month that matters. Mechanical downgrade to negative at next rebalance.
2. **Event / leadership binary risk.** CEO exit announced alongside a soft guide. Not modeled by any factor in the stack — idiosyncratic, high-variance.
3. **Valuation optical illusion.** P/E 8.97x ≈ unfiltered tax benefit. Any screen ranking NTNX as a deep-value name is wrong by ~6x on earnings multiple.
4. **SBC dilution undermines FCF quality.** SBC $358M = 12.5% of revenue; FY26 buybacks $484M reduced diluted shares by only ~0.5% (294.1M → 292.7M). Economic FCF ≈ $483M, not $841M.
5. **Thin-sample estimate revision.** The +21.7% figure = 3 analysts, FY2029. Low confidence; superseded by the 25-Nov target cuts.
6. **Factor crowding / comparability.** n=5 peer ranks; PSTG and DELL risk inputs are corrupt (beta 0.13 / 2.82). No peer momentum or peer revision data available — those ranks are genuinely missing, not zero.
7. **Book equity instability.** $703M equity, $3.71B accumulated deficit → ROE, P/B (19.3x), and ROIC are all non-comparable across time; F-Score components 8 and 9 (gross margin, asset turnover) both failed.
8. **Liquidity — not a concern.** ~2.5M shares/day average; the 13.6M spike is event-driven and readily absorbed.
