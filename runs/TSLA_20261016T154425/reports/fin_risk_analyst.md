# Fin Risk Analyst

- Symbol: TSLA
- Elapsed: 170.8s

---
The web search timed out — I'll flag the credit-rating gap rather than retry and burn budget. I now have 5 quarters of forward data showing continued margin compression into 2026. I have sufficient data to write the assessment.

---

# Tesla, Inc. (TSLA) — Financial Risk Assessment

**Date of analysis basis:** FY2025 annuals (period end 2025-12-31) + Q1/Q2 2026 interim data; price $359.71, market cap ≈ $1.42T. Sector: Consumer Cyclical / Auto Manufacturers.

---

## 1. Credit Risk Assessment: **Investment Grade (low-end)** — on fundamentals, with caveats

Tesla holds **net cash of ≈$35.7B** ($44.1B cash & short-term investments vs. only $8.4B total debt), so it is a **net-creditor**, not a net-debtor. This is the dominant credit fact: bankruptcy/solvency risk from the balance sheet is minimal. Leverage is extremely low (D/E 0.10x; debt/assets 6%).

However, the **EBITDA/earnings trajectory is deteriorating sharply** — this is the credit story that matters:
- EBITDA: $17.5B (FY22) → $14.8B (FY23) → $14.7B (FY24) → **$11.8B (FY25)**
- Operating income: $13.7B (FY22) → **$4.4B (FY25)** — down ~68% in three years
- Q2'26 operating margin hit just **1.4%**, and Q1'26 4.2% — the price-war/cycle compression continues into 2026.

The interest coverage ratio (12.9x per tool; ~16.6x on EBIT/interest basis) looks comfortable, but it is flattered by a tiny interest-expense base; the more relevant cushion is **net interest income on the cash pile (~$2B/yr at current rates)**, which is propping up net income (Q2'26: $1.11B net income vs. $0.40B operating income).

**Indicative rating:** S&P **BBB** / Moody's **Baa3** (low investment grade). Note: my web verification of the current rating timed out — **treat rating as unverified this session**, though BBB/Baa3 is consistent with the ratios.

---

## 2. Key Financial Risk Metrics (FY2025)

| Metric | Value | Assessment |
|---|---|---|
| Debt / Equity | 0.10x | Very low — strong |
| Net debt / EBITDA | **−3.03x** (net cash) | Strong |
| Debt / Assets | 6% | Strong |
| Interest coverage | 12.9x | Strong (see flattery note above) |
| Current ratio | 2.16 | Strong |
| Quick ratio | 1.77 | Strong |
| Cash ratio | 1.39 | Very strong |
| Working capital | $36.9B | Strong |
| Cash & ST investments | $44.1B | Strong |
| **Altman Z-Score** | **2.445 (grey zone)** | ⚠️ Book-value based |
| **Piotroski F-Score** | **5/9 (moderate)** | ⚠️ Deteriorating |
| Gross margin | 18.0% (FY25) vs 25.6% (FY22) | Negative trend |
| FCF / FCF yield | $6.2B / **0.49%** | Extremely rich valuation |
| Revenue growth | −3.0% YoY (FY25); flat-to-down since FY23 | Negative trend |

**Altman nuance:** x4 uses *book* equity (not market cap). With market cap ≈ $1.42T vs. book equity $82.9B, a market-capitalization-based x4 would push the Z-score into the safe zone (≈8+). The 2.445 grey-zone reading is therefore **conservative** — but it still flags that profit generation (x3 = 4.1% EBIT/assets) and asset turnover are weak relative to the balance sheet.

**Piotroski detail (5/9):** Passing on positive ROA, positive OCF, accruals quality, equity growth, and gross-margin improvement; **failing** on ROA improvement, leverage reduction, dilution (SBC), and asset turnover — i.e., the score is being held up by cash flow while profitability and efficiency erode.

---

## 3. Market Risk Profile (3-year window, SPY benchmark)

| Metric | Value | Reading |
|---|---|---|
| Annualised volatility | **59.1%** | Extreme (3–4x the market) |
| Beta vs. SPY | **2.28** | Very high systematic risk |
| Max drawdown (3Y) | **−53.8%** | Severe tail risk |
| Sharpe (approx., 0% RFR) | 0.67 | Mediocre risk-adjusted return for the risk taken |

Tesla is one of the highest-beta mega-caps in the market. A 10% market drawdown maps to roughly a **20%+ stock decline** on beta alone, and realized downside (max DD −54% in the last 3 years) has been much worse than beta implies. Nearly **$1.42T of equity value** is priced on an FCF yield of ~0.5%, meaning the market is capitalizing ~$230B of annual FCF to justify today's price — the equity carries enormous **de-rating risk** if growth narratives (robotaxi, Optimus) disappoint. If the stock fell to a still-generous 2% FCF yield, that implies ~65% downside — the *stock* (not the company) is the tail risk here.

---

## 4. Downside Scenario: Revenue −20%

Model: FY25 baseline ($94.8B revenue, 18.0% GM, ~$12.7B fixed opex) shocked to $75.8B revenue; COGS partially variable (assume GM compresses to 13–15% on pricing pressure); opex held fixed.

| Line | FY25 Base | −20% Scenario (mid) |
|---|---|---|
| Revenue | $94.8B | $75.8B |
| Gross profit | $17.1B | ~$10.6B (14% GM) |
| Operating income | $4.4B (4.6% margin) | **−$2.1B (operating loss)** |
| Net interest income (cash at ~5%) | ~+$1.9B | ~+$1.9B |
| Net income | $3.8B | **~breakeven / small loss** |
| FCF | $6.2B | **−$10 to −$12B** (after ~$9B capex) |
| Interest coverage | 12.9x | **negative** (EBIT < 0) |
| Cash balance after 3 yrs of shock | — | **≈ $10–15B, still positive** |

**Verdict:** A 20% revenue shock pushes Tesla to an **operating and free-cash-flow loss**, but the **balance sheet absorbs it**: $44B cash vs. $8.4B debt means no refinancing cliff, no covenant breach risk, and roughly **3+ years of cash runway** even under sustained losses with unchanged capex. This is the signature of a *low credit risk / high profit-cycle risk* company. A deeper (40%+) demand collapse would be the true stress boundary — likely still survivable via capex cuts, but it would trigger rating downgrades toward high-yield territory.

---

## 5. Overall Financial Risk Rating: **Moderate**

| Dimension | Risk | Rationale |
|---|---|---|
| Credit risk | **Low** | Net cash $36B, D/E 0.10x, interest coverage ~13x |
| Liquidity risk | **Low** | CR 2.16, cash ratio 1.39, no near-term debt wall ($1.6B ST debt vs. $44B cash) |
| Profitability trend | **High** | Op margin 13.6%→4.6% in 3 yrs; Q2'26 1.4% |
| Market/valuation risk | **Critical** | β 2.28, vol 59%, FCF yield 0.49% — priced for perfection |

Net: **strong fortress balance sheet; deteriorating earnings power; extreme equity valuation and market risk.** Solvency is not the question — earnings sustainability and the stock's price are.

---

## 6. Key Red Flags

1. **Structural margin collapse** — gross margin 25.6% (FY22) → 18.0% (FY25); operating margin down ~68% over 3 years; Q2'26 op margin 1.4%. Price competition in EVs is chronic, not cyclical.
2. **Revenue growth has stalled and turned negative** ($96.8B FY23 → $94.8B FY25; −3% YoY) — the growth engine that underpins the valuation is not currently producing.
3. **Negative Piotroski signals** — failing leverage-reduction, ROA-improvement, no-dilution, and asset-turnover tests; SBC dilution of ~9% of shares over the period.
4. **FCF yield 0.49% on $1.42T market cap** — valuation implies multi-hundred-billion-dollar future FCF; any narrative stumble invites a −50%+ drawdown (already seen in 3Y max DD).
5. **Earnings quality** — net income is increasingly dependent on interest income from the cash pile and likely regulatory credits, masking weak core auto economics.
6. **Key-man/organizational risk** — CEO Elon Musk carries outsized strategic importance; not captured in ratios but a real tail risk (flagged as qualitative).
7. **Rate environment** — 10Y UST at ~4.99% (2s10s +34bps, no inversion) means the equity risk premium demanded on a 0.49% FCF-yield stock is extreme; duration-sensitive.

---

## 7. Data Gaps / Caveats

- **Credit rating unverified** (web search timed out); BBB/Baa3 noted as indicative only.
- **Peer comparison** (Toyota, GM, Ford leverage/margin benchmarks) not computed — only this ticker's data was available.
- Altman Z uses book equity; **market-cap-adjusted Z is far higher** — do not read the 2.445 as distress.
- Sortino ratio, exact debt-maturity schedule, and credit-facility/covenant details not available from tools; Q2'26 balance sheet (cash position) not pulled — cash assumed near FY25 levels.
- Beta reported 1.92 (profile) vs. 2.28 (computed, 3Y vs SPY); I use the computed 3-year figure.

**Bottom line:** Tesla is **financially solvent and liquid** (net cash ~$36B, low leverage, strong liquidity ratios) — the credit story is investment-grade. The risk is not bankruptcy; it is **earnings erosion (margins near trough) + an extreme valuation on a 2.28-beta stock**. Overall financial risk: **Moderate** — with the balance sheet and the market price pointing in opposite directions.
