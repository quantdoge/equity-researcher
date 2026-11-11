# Quant Analyst

- Symbol: ONON
- Elapsed: 33.0s

---
# ONON (On Holding AG) — Quantitative Factor Report

**Data as of:** latest available; price $34.70 · Market cap ~$11.6B · Sector: Consumer Cyclical / Apparel–Footwear · Reporting currency CHF, listed USD (note FX mismatch in cross-currency ratios).

⚠️ **Peer caveat:** `get_sector_peers` returned broad Consumer-Cyclical mega-caps (AMZN, TSLA, HD, BABA…), *not* footwear comps. Apparel-specific peer multiples were unavailable, so sector ranks below are **estimated** against the Consumer-Cyclical distribution and should be treated as directional, not precise. Sample of annual periods (4–5) and revision history is small.

---

## 1. Factor Scores Table

| Factor | Score (0–100) | Est. Sector Rank | Signal |
|--------|:---:|:---:|--------|
| **Value** | 18 | Bottom quintile (~85th most expensive) | **Bearish** — P/E 56.9×, EV/EBITDA 31.4×, P/FCF 45.8×, P/B 7.1× |
| **Momentum** | 32 | 4th quintile | **Bearish** — 12-1 return **−6.5%**, negative |
| **Quality** | 55 | Middle | **Neutral/Mixed** — ROIC 17.0%, GP/Assets 0.67, accruals −0.042 (clean); but ROE fell 17.4%→12.5%, F-score 7 |
| **Low Vol** | 12 | Bottom quintile | **Strongly Bearish** — 49.4% ann. vol, β 1.22 (SPY) / 2.08 (FMP), max DD **−45.9%** |
| **Earnings Revision** | 62 | Top-tercile | **Mildly Bullish** — +22.9% revision, *but* for FY2029 (long-dated, only 10 analysts) — low confidence |

**Quality detail:** 2025 revenue +30% YoY ($3.01B) yet net income *fell* to $203.7M from $242.3M and diluted EPS dropped to $0.61 from $0.71 — **margin compression despite top-line growth** is the key fundamental red flag. Piotroski F-score 7 (of 9) = moderate; accruals consistently negative (earnings backed by cash) save for 2022.

---

## 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|--------|-------|
| Alpha (annualised) | **−38.0%** |
| Beta (vs SPY) | 1.22 (R² = 0.126) |
| Annualised return | −19.9% |
| Annualised volatility | 50.0% |
| Sharpe ratio | **−0.40** |
| Sortino ratio | **−0.46** |
| Max drawdown | −45.9% |

**Interpretation:** Deeply negative alpha with a low R² (12.6%) — most return variance is **idiosyncratic, not market-driven**, so beta understates true risk (FMP's own beta is 2.08). Both Sharpe and Sortino are negative, meaning the stock has *destroyed* risk-adjusted value over the trailing year: it underperformed cash on both a total- and downside-risk basis.

---

## 3. Valuation & Growth Bridge

| Metric | Value |
|--------|-------|
| Trailing P/E | 56.9× |
| Forward P/E (FY26E EPS $1.456) | **23.8×** |
| Forward P/E (FY27E $1.725) | 20.1× |
| EV/EBITDA | 31.4× |
| Revenue growth (FY25) | +30.0% |
| Consensus revenue (FY26E) | $3.56B (~+18%) |
| Analyst PT range (recent) | $33–$60; median ~$40 |

Valuation only normalises on aggressive multi-year growth estimates. At $34.70 the stock trades ~5% below the ~$40 median analyst target — thin margin of safety given the earnings-quality drag.

---

## 4. Composite Quant Signal: **SELL** (leaning; low-conviction)

The factor stack is dominated by negatives: bottom-quintile **value**, negative **momentum**, bottom-quintile **low-vol** (i.e., extreme realized risk), and **−38% alpha** with negative Sharpe/Sortino. Offsets are real but softer: top-tercile **Earnings Revision** (+22.9%, though long-dated and thin coverage) and solid **ROIC (17%)** with clean accruals and strong gross margins. Net: no factor provides a risk-adjusted reason to own it at 56.9× trailing earnings while EPS is *declining* year-over-year. **Composite signal: Sell**, upgraded to at best Neutral only if FY26 EPS revisions hold and momentum inflects.

---

## 5. Key Quant Risk Flags

- **Momentum reversal / negative trend** — 12-1 return −6.5%, underperforming; trend not yet repaired.
- **Extreme volatility & drawdown** — 50% annualised vol, β up to 2.08, −46% max drawdown; position-sizing risk is severe.
- **Earnings-quality divergence** — revenue +30% but EPS −14% YoY; margin compression undercuts the "growth" narrative.
- **Alpha decay / idiosyncratic risk** — low R² (0.13) means weak diversification benefit; this is a single-name bet, not market exposure.
- **Valuation fragility** — 56.9× trailing P/E and 45.8× P/FCF leave no cushion; a growth scare de-rates hard.
- **Revision signal reliability** — the +22.9% upgrade is on FY**2029** with only 10 analysts; low sample → statistically weak. Near-term FY26 revision direction unconfirmed.
- **FX / ADR** — CHF reporting vs USD listing distorts cross-currency multiples.

*Sample-size note: 4 annual financial periods and a 252-day price window; revision estimate based on n=10 analysts. Treat factor z-scores as directional.*
