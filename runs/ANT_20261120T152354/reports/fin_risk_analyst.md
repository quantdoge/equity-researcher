# Fin Risk Analyst

- Symbol: ANT
- Elapsed: 72.2s

---
## Financial Risk Assessment — ANT (Anthropic PBC)

**Critical framing note:** ANT listed on Nasdaq on **2026-11-19**, so the tool's ratio set is built on FY2025 (12/31/25) audited statements that are *already superseded* by S-1 interim disclosures through Q3 2026. I report both, and treat FY2025 GAAP figures with heavy skepticism — the reported $42.0B FY2025 net loss and $80.7B H1-2026 net loss are dominated by **non-cash convertible-note fair-value marks** ($6.2B principal carried at $130.5B fair value), not operating deterioration.

---

### 1. Credit Risk Assessment — **Sub-Investment Grade (unrated; ~BB-/B+ equivalent)**

| Segment of the capital structure | Assessment |
|---|---|
| Near-term (0–18m) | Effectively strong: **$212.7B pro-forma cash** (post-IPO + concurrent placement) + **$14.8B revolver available** ($15B facility, expanded Sept-2026 from $3.25B, matures 2031) vs **$70.7B** of commitments due in 12 months → **3.2x coverage** |
| Long-dated (2030+) | Structurally weak: **$900.9B** purchase commitments/leases (≈all compute, extending to **2045**), of which **$451.6B** falls due through 2030 and **~$117B/yr** thereafter |

**No agency rating or CDS spread was available for ANT** — explicit data gap (likely unrated/new issue). Debt is de minimis on a principal basis ($6.2B converts + finance leases), so traditional leverage is not the risk; **off-balance-sheet compute commitments are the true leverage**. Key analytical anchor: Anthropic needs **~$160B of annual revenue** to cover fixed commitments (~$117B/yr) plus non-compute costs, versus an **$81B run-rate** (Oct-2026).

**Covenant/structural risk:** the **$125.2B Broadcom 2026 lease** sits in SPVs with parent guarantee, equipment collateral, **cross-default**, and $2.5B escrow; certain uncured defaults accelerate a substantial portion of amounts owed. A reported **$42B Broadcom loan** to Anthropic further concentrates counterparty/financing linkage.

---

### 2. Key Financial Risk Metrics

| Metric | FY2025 (tool) | Latest (2026 interim, S-1) | Read |
|---|---|---|---|
| Revenue | $4.585B (+1,088% YoY) | H1 $16.3B; **Q3 $17.0B** | Hyper-growth, but ~$81B is a 28-day usage run-rate, **not** contracted |
| Gross margin | **-59.8%** (COGS $7.33B vs rev $4.59B) | Compute 48% of revenue in Q2-26 (from 177%) | FY25 sold inference below cost |
| Operating income | -$8.06B (incl. $1.5B copyright settlement) | -$693M H1; **+$1.6B adj. op. income** | Inflection, but recent |
| EBITDA | Reported -$41.9B = net income (artifact). **Computed ≈ -$8.02B** | 3Q adj. EBITDA ~$2.6B (~$10.5B ann.) | Reported EBITDA field is unusable |
| Interest coverage | **N/A** — interest expense $0 (no cash coupon) | Low cash interest; income from cash is a *revenue* item | Coverage meaningless; converts are equity-like |
| Debt / Equity | **-2.02** (negative equity) | Lease liabilities to build materially | Ratio not interpretable |
| Debt / Assets | **1.69** (liabilities $45.4B > assets $24.7B) | Structurally negative | **Book insolvency**, FV-mark driven |
| Net debt / EBITDA | -0.51 (EBITDA negative) | Net cash-like position post-IPO | Not meaningful |
| Current ratio / Quick / Cash | **8.43 / 8.43 / 7.20**; WC +$20.9B | Cash $131.8B at 9/30/26 | Liquidity is genuinely ample |
| Altman Z-Score | **-7.64 (Distress)** | x4 negative on book equity | **Distorted — do not use** (see below) |
| Piotroski F-Score | **4 / 9 (Weak)** | — | Fails ROA, op CF, equity change, no-dilution |
| FCF yield | **-1.76%** (FCF -$2.77B / ~$156.8B mcap) | 9M FCF ~$3.4B; **ex-interest-income ~$1.0B** | FCF quality poor |

**Why Z-score is misleading:** Z = -7.64 is driven almost entirely by negative book equity (X2 -2.11, X4 -0.46), which exists *because* the Amazon convertible notes are marked to a $130.5B fair value with offsetting losses. On a market-cap basis X4 would be strongly positive. I flag the score but do not weight it. Similarly FY2025 "leverage improvement" (F5 = 1) is a book-accounting artifact.

---

### 3. Market Risk Profile — **NOT MEASURABLE (material data gap)**

- `calculate_price_volatility` **failed**: FMP `historical-price-eod/dividend-adjusted` endpoint unavailable on the current subscription. One retry is not worthwhile; annualised vol, beta, Sharpe/Sortino and 3-yr max drawdown are **unavailable**.
- Available price history is **2 trading days**: IPO 2026-11-19 close **$97.17** → 2026-11-20 close **$86.12** = **-11.4% in one session**; from IPO-day intraday high $115.10 to $86.12 = **-25.2% in 48 hours**. Last price $86.31.
- **Profile beta of 0.00 is a placeholder, not a measurement.** Treat sensitivity to AI-capex sentiment as high and unhedged.
- Rate backdrop: UST 2Y 4.74% / 5Y 4.93% / 10Y 5.13% / 30Y 5.47%, 2s10s **+39bp (no inversion)** — a ~5%+ long discount rate against cash flows back-loaded to 2031–2045 is a direct valuation and lease-discounting headwind.
- Market cap data conflict: profile reports **$1.129T**, while the FCF tool used **~$156.8B** (≈1.82B diluted shares × $86). I use ~$157B and flag the $1.13T figure as an error.

---

### 4. Downside Scenario — revenue -20%

Modelled off 3Q-2026 economics (revenue $17.0B/qtr; compute+infra ~$9.9B/qtr; non-compute costs ~27% of revenue; adj. EBITDA ~$2.6B/qtr).

| Line | Base (3Q26) | Rev -20%, compute **fixed** | Rev -20%, compute **variable** |
|---|---|---|---|
| Revenue | $17.0B | $13.6B | $13.6B |
| Compute & infra | $9.9B | $9.9B | $9.9B |
| Other costs (27%) | $4.6B | $3.7B | $3.7B |
| **Adj. EBITDA / qtr** | **$2.6B** | **~$0.0B** | **~$0.0B** |
| Annualised | $10.5B | **~$0** | **~$0** |

**The key asymmetry: a 20% revenue shortfall erases ~100% of EBITDA**, because compute is contracted 12–18 months forward and owed whether used or not. That is the single most important fact in this assessment.

**Cumulative liquidity test (through 2030, external analysis):** $451.6B of commitments due by 2030 vs $227.5B total liquidity (cash $212.7B + revolver $14.8B). If revenue is held **flat at the $81B run-rate** and all fixed commitments are honoured, ~$200B of the $212.7B is consumed by 2030, leaving **~$12B** (and that assumes no cost cuts, no new capital, no interest income). At $120B revenue, ~$133B would remain. **Mitigant:** $186.2B of the $900.9B is terminable or conditional (only $4.2B of it within 12 months) — a genuine escape valve, but concentrated where counterparties have least protection.

Balance-sheet stress: a further 20% revenue decline plus continued FV marks would deepen negative book equity (already -$20.7B) and could push the SPV lease structures toward cross-default if covenants are financial as well as structural (**covenant package not disclosed in available data — gap**).

---

### 5. Overall Financial Risk Rating: **HIGH**

Not "Critical," because near-term default risk is genuinely remote: 3.2x coverage of 12-month commitments, $14.8B undrawn revolver, positive operating cash flow ($6.6B 9M-26), and adjusted operating profitability already reached. But **High** for equity holders and long-dated creditors because: (a) fixed commitments are ~11x current run-rate revenue and extend to 2045; (b) 90%+ of revenue is uncontracted usage-based spend that can churn; (c) book equity is negative and reported earnings are uninformative; (d) there is no price history from which to estimate tail risk.

---

### 6. Key Red Flags

1. **$900.9B commitments vs $212.7B liquidity** = 4.2x; $451.6B due by 2030; ~$117B/yr fixed 2031–35 against an $81B revenue run-rate.
2. **Negative gross margin in FY2025 (-59.8%)** — revenue $4.59B against compute COGS $7.33B; unit economics only recently crossed positive.
3. **Negative book equity -$20.7B, debt/assets 1.69, Altman Z -7.64 (distress), Piotroski F 4 (weak)** — every screening model will flag this as impaired.
4. **FCF quality is thin:** 3Q-2026 FCF was positive *only* because of $1.2B of interest income on IPO cash; ex-interest FCF ≈ **-$1.0B**. FY2025 OCF of -$2.64B was flattered by +$3.27B working-capital inflow → underlying burn ≈ **-$5.9B**.
5. **Revenue durability:** $81B run-rate annualises the last 28 days of usage; only **$13.8B RPO** ($10.4B within 12 months). The majority of revenue is cancellable.
6. **EBITDA will overstate cash flow as Broadcom finance leases ramp** — rent paid in cash, booked as amortisation + interest; large lease liability builds despite "almost no debt today."
7. **Dilution overhang:** converts at $130.5B fair value on $6.2B principal; share count 1.53B → 1.82B; SBC $1.16B and rising. Piotroski F7 (no dilution) fails.
8. **Post-IPO price action is poor and unmeasurable:** -11.4% on day two, -25% from IPO-day high; beta/vol/max-drawdown/Sharpe **unavailable** due to vendor endpoint limitation.

### Data Gaps (explicit)
- No volatility/beta/Sharpe/drawdown statistics — tool endpoint unavailable on subscription; 2 trading days of history only.
- No credit rating or CDS spread.
- No contractual debt maturity ladder or financial covenant package (only commitment schedule, from secondary summaries).
- Tool financials stop at FY2025; all 2026 figures are from S-1 summaries (secondary sources), not tool-derived.
- Market cap inconsistent ($1.129T profile vs ~$156.8B tool basis).
- Reported EBITDA, net debt, and D/E fields are unreliable for this entity (FV marks, negative equity); computed proxies used instead.
