# Fin Risk Analyst

- Symbol: ALAB
- Elapsed: 37.7s

---
## ALAB — Astera Labs, Inc. | Complete Financial Risk Assessment
**Sector:** Technology / Semiconductors · **Price:** $222.12 · **Market cap:** ~$38.8B · **IPO:** Mar 2024
**Most recent period:** Q3 2026 (filed 2026-11-04) · Latest balance sheet: FY2025 (12/31/25)

---

### 1. Credit Risk Assessment — **INVESTMENT GRADE (structurally, unrated)**

ALAB carries essentially **no financial leverage**: total debt of $35.1M against $1.36B of equity (D/E 0.03), and that debt appears to be lease-related (long-term and short-term debt lines both report $0). Net cash position is **$1,153.7M** (cash & ST investments $1,188.8M less $35.1M debt), producing a **net debt/EBITDA of −5.13x**. Interest expense is reported as **$0** across FY2023–FY2025, so interest coverage is **not meaningful / effectively infinite** — there is no debt service obligation to cover.

There is **no credit rating and no CDS** because there is no public debt — this is the strongest possible form of refinancing-cliff protection: **zero maturity schedule, zero covenant exposure, zero rollover risk.** The only credit-relevant liabilities are $168.2M of operating liabilities (payables, accruals, leases) against $1.53B of assets (assets/liabilities 9.11x).

The one caveat to "investment grade" is that the *business* is early-stage and highly concentrated (see Red Flags), not that the *balance sheet* is levered. Traditional credit deterioration signals are absent; the risk here is equity risk, not default risk.

---

### 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Debt / Equity | 0.03x | Negligible |
| Debt / Assets | 0.02x | Negligible |
| Net Debt / EBITDA | −5.13x (net cash) | Exceptional |
| Interest coverage (EBIT/Int.) | N/M — interest expense $0 | No debt service |
| Current ratio | 10.24x | Exceptional |
| Quick ratio | 9.79x | Exceptional |
| Cash ratio | 8.94x | Exceptional |
| Working capital | $1,228.9M | Strong |
| Cash to liabilities | 7.07x | Strong |
| Equity / Assets | 0.89 | Very low leverage |
| Altman Z-Score | **6.86** (Safe; >2.99) | Safe zone, comfortably |
| Piotroski F-Score | **6 / 9** (Moderate) | Good, not pristine |
| FCF yield (FY25 basis) | 0.71% | Very low |
| FCF yield (TTM est.) | ~1.3% | Very low |

**Altman Z components:** X1 (WC/TA) 0.80, X2 (RE/TA) 0.007, X3 (EBIT/TA) 0.14, X4 (book equity/liabilities) 8.11, X5 (sales/TA) 0.56. Note X4 uses book equity, and X5 is depressed by the $1.2B cash pile — the score is genuine but flattered by IPO proceeds rather than operating returns.

**Piotroski detail (6/9):** positives — positive ROA (F1), positive operating cash flow (F2), ROA improvement (F3), accruals quality (F4), positive equity change (F6), asset turnover improvement (F9). **Negatives: F5 lower leverage (0) — leverage rose off a near-zero base; F7 no dilution (0) — share count is expanding; F8 gross margin improvement (0) — gross margin is compressing.** Those three flags are the meaningful ones.

**Profitability & cash generation trend:**

| | FY2023 | FY2024 | FY2025 | TTM (Q4'25–Q3'26) |
|---|---|---|---|---|
| Revenue | $115.8M | $396.3M | $852.5M | **$1,556.2M** |
| Gross margin | 69.0% | 76.4% | 75.7% | **73.9%** |
| Operating income | $(29.5)M | $(116.1)M | $173.4M | **$397.1M** |
| Operating margin | (25.5)% | (29.3)% | 20.3% | **25.5%** |
| Net income | $(26.3)M | $(83.4)M | $219.1M | **$461.3M** |
| EBITDA | $(21.2)M | $(78.6)M | $225.0M | **$444.7M** |
| Operating CF | $(12.7)M | $136.7M | $319.3M | n/a (est. strong) |
| FCF | $(15.5)M | $102.4M | $281.8M | ~$515M (est.) |
| SBC | $10.7M | $234.6M | $160.0M | n/a |
| SBC % revenue | 9.2% | 59.2% | 18.8% | n/a |

Quarterly revenue inflected hard: $270.6M → $308.4M → $392.4M → **$584.9M** (+49% q/q, +154% y/y in Q3'26), with Q4'26 guided to **$730–750M**. Gross margin 72.3% in Q3'26 — drifting down as mix scales, which explains the F8 failure. Capex is minimal ($37.5M, 4.4% of revenue), so FCF conversion is structurally high; FY2025 FCF margin was 33.1%.

**Quality-of-earnings flags:** (a) TTM net income of $461M exceeds TTM operating income of $397M — earnings are being *boosted* by interest income on the cash pile, not just operations; (b) SBC of $160M in FY2025 is 73% of operating income — GAAP profitability is meaningfully dependent on a non-cash comp structure that dilutes shareholders ~5.7% (diluted 184.1M vs basic 174.1M shares).

---

### 3. Market Risk Profile — **HIGH**

| Metric | 252-day | 700-day (full post-IPO) |
|---|---|---|
| Annualised volatility | **104.7%** | 97.4% |
| Beta vs SPY | **4.10** | 2.99 |
| Max drawdown | 62.8% | **63.7%** |
| Sharpe (rf=0) | 1.24 | 0.86 |

Company-reported beta is 3.86; the empirical 1-year beta of **4.10** is the number to underwrite. This is a ~4x levered bet on the market: **in a −20% SPY drawdown, ALAB's beta implies roughly −80% equity downside** in a mechanical sense. The realized **63.7% peak-to-trough drawdown** inside ~2.7 years of trading confirms the tail is not theoretical — it has already happened once. Volatility near 100% annualised means daily 5%+ moves are routine. Sharpe of 1.24 over 1 year is deceptively good and purely a function of the enormous trailing rally; over the full history it decays to 0.86, and it carries materially higher downside dispersion (Sortino would be needed to confirm — **data gap: Sortino not computable with available tools**).

---

### 4. Downside Scenario Analysis — Revenue −20%

Base: TTM revenue $1,556.2M, gross margin 73.9%, TTM opex $752.8M (SG&A $226.6M, R&D ~$526.3M), TTM EBIT $397.1M. Holding opex flat (the realistic near-term case given hiring commitments):

| Scenario | Revenue | Gross profit | EBIT | EBIT margin |
|---|---|---|---|---|
| Base TTM | $1,556M | $1,150M | $397M | 25.5% |
| **−20%** | $1,245M | $920M | **$167M** | **13.4%** |
| −30% | $1,089M | $805M | $52M | 4.8% |
| −40% | $934M | $690M | **$(63)M** | (6.8)% |

**Result at −20%:** the company remains solidly profitable, generates roughly $200M of FCF (assuming 85% EBIT-to-FCF conversion plus interest income), and holds $1.19B of cash. **No covenant breach is possible — there are no covenants. No refinancing cliff exists — there is no funded debt.** The cash pile alone covers ~2+ years of total cash operating expense even at zero revenue (cash opex est. ~$130–140M/quarter ex-SBC and D&A → ~9 quarters of absolute-zero-revenue runway).

**The break-even point is around a 35% revenue decline**, which would be an extraordinary outcome for a business growing >100% with a $730–750M quarterly guide. Liquidity risk is effectively nil; the −20% scenario is a *valuation* event (P/S already ~25x TTM revenue), not a solvency event.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Split verdict — because a single word hides the actual structure of the risk:

- **Solvency / credit / liquidity risk: LOW.** Net cash $1.15B, current ratio 10.2x, Z-score 6.86, no debt, no covenants, no maturities. This company cannot run out of money in a downturn.
- **Market / valuation risk: HIGH.** 97–105% volatility, 4.1x beta, 63.7% realized drawdown, 0.7–1.3% FCF yield on a 25x P/S multiple.
- **Composite: MODERATE**, explicitly *not* because the balance sheet is fragile, but because the equity is priced for perfection on a customer-concentrated, cyclical end market.

---

### 6. Key Red Flags

1. **Extreme customer concentration — the single largest risk.** One end customer exceeded **70% of 2025 revenue**; four customers accounted for ~82% of revenue. A single hyperscaler's AI rack-architecture decision or inventory digestion cycle can halve this company's revenue. This is a business-model risk the balance sheet cannot offset.
2. **AI capex cycle dependency.** Revenue is levered to hyperscaler accelerator/rack build-outs. A pause in AI infrastructure spend — not a recession — is the real downside driver, and it would hit revenue faster than opex can adjust.
3. **Gross margin compression in progress.** 76.4% (FY24) → 75.7% (FY25) → 73.9% (TTM) → 72.3% (Q3'26). Directionally consistent deterioration as mix shifts; F-Score F8 flags it.
4. **Shareholder dilution.** Diluted shares 184.1M vs basic 174.1M (+5.7%); all three years show share count growth. F-Score F7 = 0.
5. **Heavy SBC reliance.** $160M FY2025 (18.8% of revenue, 73% of operating income); $234.6M in FY2024 (59% of revenue). GAAP margins overstate cash economics to a degree, and the comp is dilutive.
6. **Earnings quality — interest income dependency.** TTM net income ($461M) > TTM EBIT ($397M) entirely because of interest earned on IPO proceeds. As cash is deployed or rates fall, this tailwind reverses.
7. **Valuation as a risk factor.** 0.71% FY25 FCF yield / ~1.3% TTM-estimated. There is no valuation cushion; the stock's 63.7% drawdown is a reminder of how violently the multiple can compress.
8. **Single-foundry / supply concentration** (TSMC) and export-control exposure to China — standard semiconductor geopolitical risk, unquantified in the financials.

---

### Data Gaps (explicit)

- **FY2026 annual statements not yet available** (Q4'26 unreported); all TTM figures above are computed by me from the four most recent quarters, while the ratio tools (leverage, liquidity, Z, F, FCF yield) are anchored to **FY2025 (12/31/25)** and are therefore ~3 quarters stale. True leverage is *better* and FCF yield *higher* than the tool outputs.
- **No quarterly cash flow data** — TTM FCF (~$515M) and TTM SBC are my estimates from FY2025 margins applied to TTM revenue, not reported figures.
- **Interest coverage N/M** — no interest expense exists.
- **Debt maturity schedule: not applicable** — no funded debt.
- **No credit rating / CDS spread** — unrated issuer, no traded debt.
- **Sortino ratio, correlation, and downside-capture metrics not available** from the tool set.
- **Peer comparables failed to be useful** — `get_sector_peers` returned only mega-caps (AAPL, NVDA, MSFT, TSM, AVGO, "Anthropic PBC"); no credible same-scale semiconductor connectivity peer set was obtainable, so **no relative leverage/valuation benchmarking is included**.
