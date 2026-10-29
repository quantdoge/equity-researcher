# Fin Risk Analyst

- Symbol: ICON
- Elapsed: 32.2s

---
# ICON — Icon Energy Corp. | Financial Risk Assessment

**⚠️ Critical identification note:** This is **not** ICON plc (the CRO, ticker ICLR). `ICON` is **Icon Energy Corp.**, an Athens-based dry-bulk micro-cap (2 vessels: 1 Panamax ~77.3k dwt, 1 Kamsarmax ~81.4k dwt), IPO'd 12 Jul 2024, controlled by Atlantis Holding Corp. This is a leveraged micro-cap shipping credit, and should be risk-framed as such.

---

## 1. Credit Risk Assessment

**Rating: Sub-Investment Grade — at the Distress boundary (deep CCC-equivalent). No public rating or CDS curve exists (data gap).**

| Dimension | FY2025 (audited) | TTM to Q2'26 (current run-rate) |
|---|---|---|
| Revenue | $11.26M | $15.54M |
| EBITDA | $3.08M | **$6.47M** |
| EBIT | **−$0.39M** | $2.23M |
| Interest expense | $3.81M | $3.14M |
| Net income | −$4.20M | −$0.87M |
| Total debt / Net debt | $34.76M / $30.88M | $33.82M / $26.11M |
| **Net debt / EBITDA** | **10.0x** | **4.0x** |
| **EBIT / interest** | **0.05x** | **0.71x** |
| EBITDA / interest | 0.81x | 2.06x |
| Implied cost of debt | ~15.0% | ~9.7% |

The FY2025-vs-TTM gap matters: FY2025 EBITDA was depressed by mid-year vessel deliveries (quarterly EBITDA went −$0.62M → $0.41M → $2.28M → $1.01M). On a run-rate basis leverage looks manageable at 4.0x. **But EBIT/interest is still 0.71x — below 1.0x.** The company does not cover interest from operating earnings; it covers it from EBITDA after maintenance capex is deferred. EBITDA/interest of 2.06x is a thin, cyclical cushion for a spot-exposed dry-bulk operator.

**Asset-cover (LTV) is the binding constraint:** total debt $33.82M / PP&E $49.55M = **68% loan-to-value**. Vessel-secured shipping facilities typically carry 60–75% max LTV covenants. A **20% mark-down in vessel values** takes LTV to ~85% — a probable covenant breach, and collateral calls in a downcycle. This is the single most dangerous metric in the file.

Accumulated deficit of −$4.44M and total equity of $27.36M against total liabilities of $37.48M leave no balance-sheet cushion.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 | Q2'26 / TTM | Assessment |
|---|---|---|---|
| Debt / Equity | 1.63x | 1.24x | High but not extreme for shipping |
| Debt / Assets | 0.59 | 0.52 | High |
| Net debt / EBITDA | 10.0x | 4.0x | **Elevated; covenant-proximate** |
| Interest coverage (EBIT) | **0.05x** | **0.71x** | **Critical — sub-1.0x** |
| EBITDA / interest | 0.81x | 2.06x | Weak |
| Current ratio | 1.10 | 1.55 | Adequate |
| Quick ratio | 1.03 | ~1.49 | Adequate |
| Cash ratio | 0.85 | 1.15 | Improving |
| Working capital | $0.45M | $3.68M | Thin → adequate |
| Cash | $3.88M | $7.72M | Small |
| **Altman Z-Score** | **0.429 (Distress)** | **~0.76 (Distress)** | **Deep distress zone (<1.81)** |
| Z-score, market-value x4 | ~0.11 | — | Effectively zero equity cushion |
| **Piotroski F-Score** | **5 / 9 "Moderate"** | n/a | See caveat below |
| FCF | −$5.29M | n/a (no quarterly CF) | Investment-driven deficit |
| FCF yield | **−452%** | — | Denominator unreliable (see gaps) |
| Price / book | — | **0.07x–0.17x** | Market prices near-total equity wipeout |

**Piotroski quality caveat:** the 5/9 is flattered. Of the points scored, F5 (leverage) = 0 and F3/F1/F8 = 0. The positives are largely non-signals: F6 (positive equity change) is satisfied only by **share issuance**, and F7 (no dilution) = 1 directly contradicts the observed share count rising 1.23M → 3.46M diluted. Underlying fundamental momentum is **weak, not moderate**.

---

## 3. Market Risk Profile

| Metric | 365-day | 180-day |
|---|---|---|
| Annualised volatility | **101.4%** | 86.8% |
| Beta vs SPY | 1.28 | 0.92 |
| Max drawdown | −92.8% | −48.4% |
| Sharpe (rf=0) | −1.70 | +0.14 |

**These figures are materially unreliable — flag explicitly.** The price series is contaminated by **at least two reverse splits** (announced 28 Mar 2025 to preserve listing; **1-for-5 effective 8 Jan 2026**, confirmed by Nasdaq Trader notice ECA2026-6) and by repeated **Nasdaq Listing Rule 5550(a)(2) bid-price deficiency notices**. The apparent 92.8% drawdown blends genuine collapse with unadjusted split ratios. Directionally true (the stock is down ~99% from a nominal $663 July-2024 print to **$1.37** on 25 Feb 2026), numerically unreliable.

What *is* reliable:
- **Beta is not a useful risk measure here.** The spread between the 365d (1.28) and 180d (0.92) estimates, plus tiny R², means near-100% of the variance is idiosyncratic (freight rates, financing events, listing status), not market-driven.
- **Liquidity risk is severe.** Recent daily volume ~50–300k shares at ~$1.37 ≈ **$70k–$400k/day**. Position-sizing and exit risk are first-order. Volume spikes (26.9M shares on 20 Jan 2026; 11.8M on 13 Jun 2025) indicate event/promotional trading, not organic interest.
- **Market capitalisation ~$1.9M–$4.7M** (basic 1.35M / diluted 3.46M shares × $1.37). Sub-$5M micro-cap: no institutional ownership base, index exclusion, and Nasdaq equity/bid-price compliance risk remains live.

---

## 4. Downside Scenario Analysis

**Base: TTM revenue $15.54M; EBITDA $6.47M; EBIT $2.23M; interest $3.14M; net debt $26.11M.**

Dry-bulk vessel opex is largely fixed daily cost, so revenue declines flow through to EBITDA at high marginal rates (~70% assumed, net of voyage/commission savings).

| Scenario | Revenue | EBITDA | EBITDA/int. | EBIT/int. | Net debt/EBITDA | Assessment |
|---|---|---|---|---|---|---|
| Base | $15.54M | $6.47M | 2.06x | 0.71x | 4.0x | Thin but functioning |
| **−20% revenue** | $12.43M | **$4.3M** | **1.36x** | **~0.0x** | **6.1x** | **EBIT ≈ zero; coverage covenant risk; LTV pressure** |
| −35% (2023-style trough) | $10.10M | $2.2M | 0.71x | negative | 11.8x | **Cash-flow default risk; forced asset sales or dilutive raise** |

**At −20% revenue:** EBIT falls to roughly breakeven, EBITDA/interest drops to ~1.4x, and net leverage moves to ~6.1x — above the 3.5–4.0x maintenance covenants common in shipping facilities. Simultaneously, weaker freight usually coincides with weaker secondhand vessel values, so the 68% LTV deteriorates in the *same* direction. The compounding of leverage and collateral covenants is why this credit fails non-linearly: **a moderate earnings shock and a moderate asset-value shock together produce a covenant breach that neither would produce alone.**

**Mitigants:** $7.72M cash and positive operating cash flow (+$0.80M FY2025 *after* ~$3.8M interest paid) mean near-term default is not imminent. At the current deficit run-rate, cash covers roughly 2+ years **only if growth capex stops**. The FCF deficit (−$5.29M) is overwhelmingly vessel-acquisition capex (−$6.09M), not operating burn — so the company retains the option to halt fleet growth and self-fund. That option is the main thing standing between this credit and distress.

---

## 5. Overall Financial Risk Rating: **HIGH**

Not Critical, because operating cash flow is positive, the current ratio has improved to 1.55, runway exists if growth capex is suspended, and TTM leverage (4.0x) is materially better than FY2025 (10.0x). Firmly High rather than Moderate because interest coverage is sub-1.0x on EBIT, the Altman Z-Score is in deep distress territory on both book and market bases, the equity trades at 7–17% of book value, and the asset-cover ratio sits within ~7 points of typical LTV covenants in a cyclical, spot-exposed industry.

---

## 6. Key Red Flags

1. **LTV covenant proximity (68% debt/PP&E).** The most likely proximate trigger of a restructuring. A 20% vessel-value decline breaches typical 75% max-LTV tests.
2. **EBIT/interest below 1.0x (0.71x TTM).** Earnings do not cover interest; cash flow does only marginally.
3. **Two reverse splits and live Nasdaq listing-compliance risk** (bid price <$1.00; 1-for-5 effective Jan 2026). Continued listing is not assured.
4. **Market cap ($1.9M–$4.7M) at 0.07–0.17x book.** The market is explicitly pricing a near-total common-equity wipeout — consistent with the Z-score.
5. **Dividends paid while loss-making and free-cash-flow negative** ($153k FY2025; $239k FY2024 plus a **$3.0M buyback** against −$17.2M FCF). Buying back stock in a company that subsequently required equity issuance, and paying dividends in a loss year, is a serious capital-allocation and governance signal — and the recipient is likely the parent.
6. **Controlled company / ownership concentration.** Atlantis Holding control; Hampton Financial took a 10% stake in May 2026. Minority shareholders have limited influence over refinancing or dilution decisions.
7. **Aggressive dilution.** Shares outstanding rose from 1.23M to ~3.46M diluted, with dilution proceeds ($21.4M → $27.4M equity despite losses) masking negative retained earnings.
8. **Extreme illiquidity** (~$70k–$400k ADV) — exit risk is material independent of fundamentals.

---

## 7. Data Gaps (explicit)

- **No debt maturity schedule** — the largest analytical gap. Refinancing-cliff risk cannot be quantified; shipping loans typically carry 5-year amortisation with balloon maturities.
- **$20.5M reconciliation gap** between reported `total_debt` ($34.76M) and short- + long-term debt ($13.72M) from FY2025 onward. PP&E rose $25.2M against only $6.1M of capex, so this is almost certainly finance-lease/sale-leaseback obligations — **unverified**, and if so, materially changes the covenant and maturity picture.
- **No quarterly cash flow statement** — cash burn and runway are annual-only.
- **No covenant detail** (LTV, DSCR, minimum-liquidity thresholds, cross-default terms), no credit rating, no CDS.
- **No viable peer set.** The sector screener returned only mega-cap industrials (CAT, GE, RTX, SPCX) — not comparable to a 2-vessel dry-bulk issuer. No peer multiples or dry-bulk benchmark TCE rates were obtainable, so the revenue sensitivity above is modelled from cost structure, not observed.
- **Price series contaminated by reverse splits**; vol/beta/drawdown indicative only. Reported market cap ($377,891) is internally inconsistent with price × shares — used a $1.9M–$4.7M range instead.
- **Share count inconsistency:** weighted-average basic fell from 2.43M (Q1'26) to 1.35M (Q2'26) while diluted was 3.46M — suggests converts or preferred; unresolved.
