# Fin Risk Analyst

- Symbol: LRCX
- Elapsed: 52.4s

---
# LRCX — Financial Risk Assessment
**Lam Research Corporation** | Technology / Semiconductors (WFE) | Fiscal year ends late June
*Base period: FY2026 (ended 2026-06-28, 10-K filed 2026-08-07)*

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE**

| Signal | Reading | Verdict |
|---|---|---|
| Gross debt / EBITDA | 4,121.6 / 8,704.0 = **0.47x** | Exceptional |
| Net debt / EBITDA | **−0.17x** (net *cash* $1.46bn) | Net cash |
| Debt / equity | **0.33x** | Conservative |
| Debt / assets | **0.18x** | Conservative |
| Cash / total debt | 5,579.2 / 4,121.6 = **1.35x** | Debt extinguishable from cash |
| Altman Z-Score | **5.40 — Safe zone** (vs 2.99 threshold) | No bankruptcy signal |
| Piotroski F-Score | **8 / 9 — Strong** | Only miss: accrual quality |
| Equity / assets | **0.53x** | Solid, and rising (0.46x → 0.53x) |

Lam could retire **100% of its debt from cash on hand today** and still hold ~$1.5bn. Equity has compounded from $8.54bn (FY24) to $12.47bn (FY26) despite ~$10.2bn returned to shareholders over three years — internally funded.

**Ratings evidence:** An S&P Global Ratings *upgrade* was published (research headline: "Lam Research Corp. Upgraded To '…'"), citing surging WFE and services demand. The 10-K confirms **$3.75bn aggregate principal of senior unsecured notes** and a **$2.0bn revolving credit facility maturing 2030**; S&P commentary describes the maturity schedule as "manageable over the intermediate term." **⚠️ Data gap: the exact notch is unconfirmed** — S&P's page returned HTTP 403 and the headline was truncated. A pre-2020 convertible-note rating of BB+ appears in older S&P records; this is **dated and no longer representative** of the current structure. On 1.77x total liabilities coverage (assets/liabilities) and net cash, the credit profile is unambiguously solid investment grade.

**Interest coverage — data flag.** FY2026 `interest_expense` is reported as **$0** against $4.12bn of debt, which is not credible and is treated as a vendor/schema artifact (likely net-interest presentation). Using FY2025 actual interest expense of **$178.2m** as the proxy: FY2026 EBIT 8,262.5 / 178.2 = **46.4x** (FY2025 actual: **33.4x**; FY2024: **24.5x**). Coverage is a non-issue at any plausible rate.

---

## 2. Key Financial Risk Metrics

| Metric | FY2026 | FY2025 | FY2024 | Trend |
|---|---|---|---|---|
| Revenue ($m) | 23,232.7 | 18,435.6 | 14,905.4 | +26.0% YoY |
| Gross margin | 50.5% | 48.7% | 47.3% | ▲ Improving |
| Operating margin | **35.3%** | 32.0% | 28.6% | ▲ Cycle peak |
| EBITDA ($m) | 8,704.0 | 6,344.4 | 4,905.2 | +37.2% |
| Interest coverage (x) | 46.4* | 33.4 | 24.5 | ▲ |
| Current ratio | 2.63 | 2.21 | 2.97 | ▼ but strong |
| Quick ratio | 1.91 | — | — | Strong |
| Cash ratio | 0.94 | — | — | Strong |
| Net debt/EBITDA | −0.17x | −0.26x | −0.18x | Net cash |
| Z-Score | 5.40 | — | — | Safe |
| F-Score | 8 | — | — | Strong |
| **FCF margin** | **21.1%** | 29.4% | 28.6% | **▼ −8.3pp** |
| **FCF / Net income** | **67%** | 101% | 111% | **▼ Sharp** |
| **DSO (days)** | **83.9** | 66.9 | 61.7 | **▼ +22 days** |
| DIO (days) | 135.6 | 166.3 | 196.0 | ▲ Good |
| FCF yield | **2.1%** | — | — | Low |
| EV/EBITDA | ~26.4x | — | — | Rich |

*FY2026 coverage uses FY2025 interest expense (see flag above).*

**The tension in this table is the whole story:** record absolute profitability paired with a sharp deterioration in *cash conversion*. FY2026 net income exceeded operating cash flow by **$1.4bn** — the single reason F-Score is 8 rather than 9.

---

## 3. Market Risk Profile — **HIGH**

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (756d) | **60.2%** | ~4x the S&P 500; extreme for a $231bn mega-cap |
| Beta vs SPY | **2.35** (companion field: 2.01) | A 20% market drawdown implies a ~40–47% hit |
| Max drawdown (3y) | **−57.7%** | Realised, not hypothetical |
| Sharpe (rf = 0%) | **0.97** | ~0.90 on a 4% risk-free rate |
| Sortino | **not available** | ⚠️ Tool gap |
| 1-day 95% VaR | ~**−6.2%** | Daily vol ≈ 3.8% |
| 1-month 95% VaR | ~**−28.6%** | |
| 1-year 95% VaR | ~**−99%** | A 1-in-20 year can halve the position |

**Critical observation — a violent fundamental/market divergence.** FY2026 was the best year in company history (revenue +26%, operating margin 35.3%, EPS $5.76). Yet the stock closed at **$432.87 on 2026-06-30** and has since fallen to **$185.01** — a **−57.3% drawdown**, verified by the max-drawdown math (432.87 × 0.4234 = $183.3 ≈ current price). The equity now sits essentially *at its 3-year trough*, down 57%, while earnings are at a record. At $185 the shares still trade at **31.8x earnings and 26.4x EV/EBITDA** — the market is explicitly pricing a downcycle and repudiating peak FCF.

**⚠️ Data-alignment gap:** the price-history endpoint (2026-09-01 close $289.89) is inconsistent with the profile snapshot price ($185.01) and market-cap-implied price (~$184). I treat **$185.01 as current** because it reconciles to the max-drawdown figure and to the FCF-yield denominator; the OHLC series therefore ends earlier than the profile snapshot. The 2026 collapse from $432.87 → $252.08 (−41.8%) is visible *within* the series and is corroborated externally.

---

## 4. Downside Scenario Analysis

Modelled with operating leverage (COGS ~70% variable, opex ~70% fixed) — then validated against **actual FY2024 history**, when revenue fell −14.5% and Lam still printed a **28.6% operating margin and $4.26bn of FCF**. That real cycle is the strongest evidence in this report.

| Scenario | Revenue | Op margin | EBIT | EBITDA | Net debt/EBITDA | Coverage* | FCF | FCF yield |
|---|---|---|---|---|---|---|---|---|
| Base FY2026 | 23,232.7 | 35.3% | 8,262.5 | 8,704.0 | −0.17x | 46.4x | 4,891.3 | 2.1% |
| **−20% revenue** | 18,586.2 | ~28.9% | ~5,376 | ~5,818 | **−0.25x** (net cash) | ~30x | ~4,800 | ~2.1% |
| **−35% revenue (severe)** | 15,100.3 | ~21.6% | ~3,257 | ~3,698 | **−0.39x** (net cash) | ~18x | ~3,500 | ~1.5% |
| FY2024 actual (−14.5%) | 14,905.4 | 28.6% | 4,545.5 | 4,905.2 | −0.18x | 24.5x | 4,255.6 | — |

*Coverage vs $178m proxy interest.*

**Why the downside is financially benign:** in a downturn, working capital *reverses*. FY2026 was hit by a **−$1.91bn** working-capital drag as receivables ballooned; a revenue contraction unwinds that, releasing cash back. This is why FCF holds roughly flat even as EBIT falls ~35%. **In no scenario does Lam become a net-debt company, breach a plausible covenant, or fail to cover its $1.27bn dividend** (covered ~3.8x even at −35% revenue). Liquidity is fortified by **$9.67bn of working capital** and a **$2bn undrawn revolver**.

**The real downside is not solvency — it is equity duration.** At 26.4x EV/EBITDA with peak margins, a 35% revenue decline could reasonably compress the multiple to 12–15x, implying a further **−40% to −55%** in the equity even as the business stays comfortably net cash. That is a translation risk, not a credit risk.

---

## 5. Overall Financial Risk Rating

# **MODERATE**
**(Credit risk: LOW | Market/equity risk: HIGH — the composite is driven by volatility, not leverage)**

A fortress balance sheet bolted to one of the most cyclical, highest-beta large-caps in the market. Lam will survive a prolonged downturn without difficulty — it would likely emerge with *more* net cash. But shareholders will not: the ±60% annual volatility, 2.35 beta, and realised −57.7% drawdown mean the equity is a leveraged bet on the WFE cycle, and it is currently priced at 31.8x trough-cycle-denying earnings.

---

## 6. Key Red Flags

1. **🔴 Receivables blowout — the single most important finding.** DSO jumped **61.7 → 66.9 → 83.9 days** in two years (+22 days). AR grew **+58%** (3,378 → 5,340) against revenue growth of **+26%**, absorbing **$1.91bn** of cash. Either collections are deteriorating with concentrated/China-exposed customers, or revenue recognition is running ahead of cash at the cycle peak — the classic late-cycle warning. This is precisely why F-Score registers 8, not 9 (accrual quality fail).
2. **🔴 FCF quality erosion.** FCF/net income collapsed **111% → 101% → 67%**. FCF margin fell **29.4% → 21.1%** *while revenue rose 26%*. Headline FCF of $4.89bn is flattered by the working-capital effect reversing; the underlying cash engine is converting less well than the income statement implies.
3. **🟠 Capital returns exceed cash generation.** Dividends ($1.27bn) + buybacks ($3.85bn) = **$5.12bn = 105% of FCF**, funded partly by an **$811m cash drawdown**. Buybacks were executed at FY2026 average prices well above the current $185 — capital deployed at the cycle peak, now underwater.
4. **🟠 Peak-cycle margin concentration.** 35.3% operating margin is the high-water mark of the four-year series (28.6% → 32.0% → 35.3%). Margins mean-revert; the −20% scenario shows margin compression of ~6.4pp for a 20% revenue decline (operating leverage ~1.7x).
5. **🟠 Equity already in drawdown at record earnings.** −57.7% from June 2026 peak with the best financials in company history is the market's verdict on forward risk. Beta 2.35 means diversification offers little protection.
6. **🟡 China / export-control and customer concentration** — the 10-K flags China as a major revenue region; policy shifts are a binary, non-diversifiable revenue risk not captured in any ratio above.
7. **🟡 Metric integrity issues** — FY2026 interest expense of $0 is not usable; treat coverage figures as proxy-derived.

### Explicit Data Gaps
- **Exact S&P/Moody's notch** — page 403'd; upgrade *direction* confirmed, level not.
- **Year-by-year debt maturity ladder** — only aggregate known: $3.75bn senior notes, $2bn RCF due 2030. No near-term cliff is evident, but the granular schedule was not extracted.
- **Payables / DPO** — absent from the balance-sheet payload; full cash conversion cycle cannot be computed (DSO and DIO alone indicate lengthening, not CCC).
- **CDS spreads** and **Sortino ratio** — unavailable from tooling.
- **Peer multiples** — not gathered within budget; relative valuation is therefore unassessed.
- **Price-series endpoint mismatch** ($289.89 on 2026-09-01 vs. profile $185.01) — resolved in favor of $185.01, which reconciles to both the max-drawdown figure and the FCF-yield denominator.

**Bottom line:** Lam Research is a **credit non-event and an equity risk event**. Lend to it without concern; own it with a clear-eyed view that you are buying a 60%-vol, 2.35-beta cyclical near a trough price but still at 32x peak earnings — and that the receivables and cash-conversion deterioration are the earliest observable signals that the cycle has already turned, even though the income statement has not yet said so.
