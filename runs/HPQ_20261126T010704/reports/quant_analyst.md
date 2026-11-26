# Quant Analyst

- Symbol: HPQ
- Elapsed: 34.3s

---
# HPQ — Quantitative Factor Report

**⚠️ Data-integrity flag up front:** three independent feeds disagree materially. I computed price statistics directly from the raw OHLC series (my own returns), which is the only verifiable source.

| Source | Price | 52-wk return | Vol | Beta |
|---|---|---|---|---|
| Raw OHLC (verified, 2026-02-20 close) | **$17.90** | **−44.1%** | ~40% (my calc) | — |
| `calculate_sharpe_sortino` / `alpha_beta` tools | — | **+84.8%** | 52.1% | 0.49 |
| Valuation/profile tools | $31.15 | — | — | 1.21 |

The regression's R² is 0.023 (252d) / 0.057 (504d) — implausibly low for HPQ vs SPY, so the reported **alpha of +80.7% and Sharpe of 1.63 are not usable**. Analyst price targets posted at $25–$32 through Aug 2026 confirm the stock has since fallen to ~$17.90, not recovered to $31. **I have used $17.90 and my own return calculations throughout.** FY2026 income statement is also garbled (revenue $16.0bn vs $55.3bn FY25 and $59.8bn consensus; net income $769m in the P&L vs $2,425m in the cash flow), which corrupts the reported quality/ROIC/F-score inputs.

## 1. Factor Scores

| Factor | Score (raw) | Rank in hardware comp group* | Signal |
|---|---|---|---|
| **Value** | P/FCF **5.2x** (adj. to $17.90), EV/EBITDA **12.3x**, fwd P/E **5.5x** (FY26E $3.25), div yield **6.7%**; P/B 54.7x, GAAP P/E 21.3x | 1 of 3 (DELL P/FCF 23.8, HPE 15.3) | **Strong Buy** |
| **Momentum** | 12-1 return **−41.3%** ($32.00 → $18.80); 52-wk total **−44.1%** | 3 of 3 (DELL +5.5%, HPE +8.6%) | **Strong Sell** |
| **Quality** | Normalized FY25 GP/assets **23.3%** (vs DELL 22.4%, HPE 20.0%); accruals **−6.7%** (good); F-score **6/9**; ROIC 8.6%–34% (period-dependent, unreliable); ROE 145.9% = book-equity artifact, ignore | 1 of 3 on GP/assets | **Neutral** |
| **Low Vol** | Realized vol **~40%** (tool: 51.2%), beta **~1.1–1.2** (profile 1.21); max DD **−44.8%** | 3 of 3 | **Strong Sell** |
| **Earnings Revision** | FY29E EPS +5.23% vs 3mo prior; PTs raised May–Aug'26 (Bernstein $27→32, Evercore $25→32, Barclays $19→23) | n/a | **Mild Buy** |

\* Only DELL/HPE/AAPL are true Computer-Hardware comparables; the sector peer endpoint returns mega-cap semis (NVDA, TSM, AVGO) that are not meaningful for HPQ. **This is a 3-name rank, not a sector quintile — no statistical significance.**

## 2. Price Statistics (52 weeks, computed from raw OHLC)

| Metric | Value | Note |
|---|---|---|
| Return (price) | **−44.1%** | $32.00 → $17.90 |
| 12-1 momentum | **−41.3%** | excludes last 21 trading days |
| Annualized vol | **~40%** (est.) | vs SPY ~15%; tool reported 51.2% |
| Max drawdown | **−44.8%** | peak $32.00 → trough $17.66 (19-Feb-26) |
| Beta | **~1.21** (profile); regression 0.49/0.76 | R² 0.02–0.06 → **regression beta unreliable** |
| Alpha | **Large negative**, roughly −50 to −60pp | tool's +80.7% is spurious (R²≈0) |
| Sharpe | **≈ −1.1** (est.) | tool: +1.63 |
| Sortino | **≈ −1.5** (est.) | downside dev ~30%; tool: +3.14 |

**Correlation:** HPQ–DELL 0.38, HPQ–HPE 0.27, HPQ–AAPL 0.16. HPQ is substantially idiosyncratic — it has not tracked its own hardware peers, consistent with company-specific (PC/print demand, tariff, capital-return) drivers.

## 3. Composite Quant Signal: **NEUTRAL (with Sell bias)**

Value is genuinely extreme — 5x FCF, 5.5x forward EPS, ~6.7% dividend yield, cheapest of its hardware peers — but it is the *only* supportive factor. Momentum is bottom-decile (−41% 12-1), volatility and drawdown are worst-in-class, and estimate revisions are positive only in a thin sample (FY29E n=1 analyst). This is the classic **value-trap configuration**: cheap for a reason, with no price confirmation. The cross-sectional pattern (top-quintile value + bottom-quintile momentum + bottom-quintile low-vol) has historically been a poor near-term combination. Upgrade trigger: momentum inflection plus sustained positive revisions.

## 4. Key Quant Risk Flags

- **Stale/broken price feed** in valuation and risk tools (price $31.15 vs actual $17.90) — any multiple computed off that price is ~74% too high. Recompute P/E, P/B, P/FCF, EV/EBITDA, and yield at $17.90.
- **Garbled FY2026 P&L** (revenue $16.0bn) — quality factor, ROIC series, and F-score inputs are contaminated; gross-profit/assets of 5.89% is an artifact, normalized figure is ~23%.
- **Negative momentum / downtrend persistence** — still making lower lows into Feb 2026; no technical base.
- **Capital-return sustainability:** dividends $1.095bn + buybacks $1.225bn = $2.32bn vs FCF $3.19bn (**73% of FCF**). A 6.7% yield on a de-rating hardware name is at risk if FCF rolls over.
- **Thin book equity** ($0.57/sh, P/B 54.7x) makes ROE and any book-based value/quality metric meaningless; leverage metrics distorted.
- **Factor crowding: low.** HPQ's correlation to DELL/HPE is only 0.27–0.38, so crowding risk is minimal — but so is any diversification benefit within a hardware sleeve.
- **Sample-size caveats:** revision score rests on 1 analyst (FY29); peer rankings rest on 3 names; regression alphas/betas statistically insignificant (R² 0.02–0.06). Treat the +80.7% alpha and 1.63 Sharpe from the toolkit as rejected, not confirmed.
