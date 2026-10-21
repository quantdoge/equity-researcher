# Fin Risk Analyst

- Symbol: GM
- Elapsed: 114.6s

---
# General Motors (GM) — Complete Financial Risk Assessment
**As of: FY2025 audited (Dec-2025) + Q3 2026 (period ended 30-Sep-2026). Last price $77.09 (20-Oct-2026), market cap ≈ $67bn.**

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (BBB), but weakening at the industrial level**

- **S&P: 'BBB' long-term, stable outlook** — affirmed for GM (Jan-2025) and for **GM Financial (BBB, stable, affirmed 24-Nov-2025)**. *Moody's/Fitch ratings and CDS spreads not retrieved (data gap).*
- The investment-grade rating rests on **liquidity and captive-finance structure, not on earnings quality**. FY2025 GAAP operating income collapsed to **$2.91bn (1.57% margin)** from $12.78bn (6.82%) — a **77% decline** — driven by a **Q4-2025 operating loss of −$3.65bn** (negative gross profit of −$1.12bn) from a **~$7.2bn EV charge** plus tariff costs of $3.5–4.5bn gross.
- **Critical structural adjustment:** consolidated debt of **$130.3bn** is ~85–90% **GM Financial** (captive, ABS-funded, matched against earning assets and self-liquidating). Consolidated net debt/EBITDA of **5.57x is not a meaningful measure of industrial leverage** — it mechanically penalizes a finance book. On an estimated automotive-only basis, GM carries roughly **$16–17bn gross automotive debt against ~$28bn cash — i.e. approximately net cash**, with automotive EBIT-adjusted guided to **$14.5–15.5bn for FY2026** (~1.2x gross debt/EBIT). ⚠️ *The segment split is an estimate; I could not retrieve the 10-Q segment debt table (SEC returned 403).*
- **Earnings quality is the real credit concern:** FY2026 **EBIT-adjusted guidance of $14.5–15.5bn** vs **TTM GAAP operating income of only ~$4.3bn** implies a **~$10bn GAAP/adjusted gap**. A rating supported by adjusted numbers with a 70% GAAP haircut is fragile if charges recur (EV, Cruise, warranties, tariffs).
- **Verdict:** BBB is defensible today because of the balance-sheet structure, but the **trend of coverage and equity is negative** (see §2). A 20% volume shock would put GAAP EBIT near zero (see §4) — the path to a downgrade is a *sustained* negative-FCF, charge-heavy year, not a single bad quarter.

---

## 2. Key Financial Risk Metrics

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | Latest (TTM Q3'26) | Read |
|---|---|---|---|---|---|---|
| Revenue ($bn) | 156.7 | 171.8 | 187.4 | 185.0 | ~186.9 | Flat top line |
| Operating margin | 8.0% | 5.4% | 6.8% | **1.6%** | ~2.3% | Severe compression |
| EBIT ($bn) | 12.58 | 11.31 | 9.37 | 3.84 | 4.41 | −65% in 2 yrs |
| Interest expense ($m) | 987 | 911 | 846 | 727 | ~645 | Rising with debt |
| **Interest coverage (op. income/interest)** | 12.7x | 12.4x | 15.1x | **4.0x** | ~6.7x | Recovering, still thin |
| Total debt ($bn) | 115.7 | 122.6 | 130.7 | **130.3** | 127.7 (Q2'26) | +$12bn in 2 yrs |
| Net debt / EBITDA (consolidated) | 4.04x | 4.47x | 5.09x | **5.57x** | n/a | Deteriorating; captive-distorted |
| Debt / equity | 1.60x | 1.80x | 1.99x | **2.06x** | ~1.98x | Leverage up, equity down |
| Equity / assets | 27.4% | 25.0% | 23.4% | **22.5%** | 22.3% | 5pts of erosion |
| Current ratio | 1.10 | 1.08 | 1.13 | 1.17 | **1.09** | Thin; re-deteriorated |
| Quick ratio | — | — | — | 1.01 | ~0.94 | Inventory-dependent |
| Cash | 31.3 | 26.5 | 27.1 | 27.7 | **27.8** | Stable, but ~flat |
| Working capital ($bn) | 9.28 | 7.17 | 12.28 | 15.43 | **9.54** | −$5.9bn in 9 months |
| **Altman Z-Score** | — | — | — | **1.199 (Distress)** | — | *Not valid for captive finance* |
| **Piotroski F-Score** | — | — | — | **4 / 9 (Weak)** | — | Fails leverage, ROA, margins, turnover |
| FCF ($bn) | −5.14 | −3.68 | −5.98 | **+11.07** | ~+12.7 | See quality caveat below |
| Shareholders' equity ($bn) | 72.3 | 68.3 | 65.6 | **63.2** | 64.5 | Retained earnings falling |

**Interpretation / adjustments:**
- **Z-Score of 1.199 is not actionable.** It is driven by low x4 (book, not market, equity), x1 (working capital), and x5 (asset turnover of 0.66 — structurally low for a balance-sheet-heavy lender). I report it because it is in the toolchain, but the **Piotroski 4/9 is the more credible warning**: no leverage improvement, no ROA improvement, no gross-margin improvement, no asset-turnover improvement, and negative equity change.
- **FCF quality is the key misread risk.** FY2025 FCF of $11.07bn was produced by a **+$9.06bn working-capital inflow** against a −$3.3bn net loss in Q4. **FCF ex-working-capital ≈ $2.0bn.** GM generated **negative cumulative FCF of −$14.8bn across FY2022–FY2024**, so FY2025's positive print is a one-off WC swing, not a trend. Meanwhile GM repurchased **$24bn of stock over FY2023–FY2025** while running negative cumulative FCF — funded by balance-sheet cash. FY2025 capex also fell to $15.8bn from $26.1bn in FY2024, which flatters FCF and raises a **underinvestment/capex-deferral** question.
- **Liquidity is adequate but not improving:** $27.8bn consolidated cash, plus GM Financial **available liquidity of $28.0bn at 30-Sep-2026** (its Q1'26 figure was $35.0bn — a **$7bn decline in two quarters** worth monitoring). Automotives historically supplement this with an undrawn revolver (~$16bn, reportedly subject to a minimum-liquidity condition, not covenant-heavy). *Revolver terms unverified — data gap.*
- ⚠️ **Data defect:** the Q3-2026 balance sheet returned `total_debt = 0` and `net_debt = −$23.2bn` (positive net cash). That is a feed error; I use Q2-2026 ($127.7bn debt) and FY2025 ($130.3bn).

---

## 3. Market Risk Profile

| Metric | Value | Context |
|---|---|---|
| Annualised volatility (756d) | **35.9%** | Very high for a large cap — cyclical + tariff/policy beta |
| Beta vs SPY (756d) | **0.93** | ⚠️ Conflicts with profile field of **1.4**; different window/frequency. Use ~0.9–1.4 range |
| Max drawdown (3y) | **−29.1%** | Consistent with observed 13-month range |
| Sharpe (rf = 0%) | **0.80** | Adequate risk-adjusted return, but rate-free assumption understates risk |
| 13-month close range | **$54.88 → $90.11** | 64% trough-to-peak round trip |
| Peak-to-current (Jul-2026 $90.11 → $77.09) | **−14.4%** | Guidance disappointment |
| Single-day event risk | **−6.8% on 20-Oct-2026** | Earnings-day gap; 24.6m shares on 2.5x normal volume |

**Read:** GM is a **high-volatility, event-driven cyclical** whose risk is concentrated in quarterly print dates and trade-policy headlines, not in steady drift. Vol of ~36% versus a beta near 1.0 means the volatility is **idiosyncratic (tariff/EV/segment-specific), not market-driven** — it will not be hedged well by index exposure. The stock has fully retraced its 2025 lows and then given back ~14% from the July 2026 peak; there is real drawdown asymmetry (see §4 tail).

---

## 4. Downside Scenario Analysis — Revenue −20% ($185bn → ~$148bn)

Assumed contribution margin ~15% on lost revenue, $2bn of fixed-cost self-help, tariffs unchanged, no new charges.

| Line item | Base (FY2025 / TTM) | −20% revenue stress | Δ |
|---|---|---|---|
| Revenue | $185.0bn | $148.0bn | −$37.0bn |
| Gross profit | $20.1bn | ~$8.0bn | −$12.1bn |
| SG&A + fixed cost | $8.7bn | ~$6.7bn (cut) | −$2.0bn |
| **GAAP operating income** | **$2.9bn** | **≈ −$1.1bn (loss)** | **−$4.0bn** |
| Interest expense (industrial) | $0.73bn | $0.73bn | — |
| **Interest coverage** | 4.0x | **negative — 0.0x** | Breach territory |
| Net debt / EBITDA (consolidated) | 5.6x | ~9–10x | Downgrade trigger |
| Net debt / EBITDA (automotive est.) | ~net cash | ~1.5–2.0x net debt | Still manageable |
| Cash (start $27.8bn) | — | ~$21–23bn after burn | Survivable |
| Liquidity incl. facilities | ~$45–50bn auto + $28bn GMF | ~$60–70bn | No refinancing cliff |

**Scenario conclusions:**
1. **GAAP EBIT goes negative on a 20% revenue drop — the industrial business has no earnings cushion.** On adjusted EBIT ($14.5–15.5bn guidance) the same shock leaves ~$8–9bn, still positive: **the survival case depends entirely on which earnings measure you believe.** With a $10bn GAAP/adjusted gap, the honest answer is that GAAP earnings are already near zero-optionality.
2. **A 20% volume shock is a GM Financial problem before it is an automotive problem.** Lower originations, rising delinquencies, and falling used-vehicle residuals hit the lease book and GMF's ~$112bn of wholesale/ABS funding. **The true tail risk is an ABS-market seizure** (as in 2020), which would force GM to draw revolvers and push consolidated leverage to the ~9–10x range. GMF's $28bn liquidity is the buffer; its decline from $35bn in two quarters is the leading indicator to watch.
3. **Tariffs are a permanent P&L tax, not a shock.** $3.0–4.5bn of annual gross tariff cost against $2.9bn of GAAP operating income means tariff relief — not volume — is the largest single swing factor in the credit.

---

## 5. Overall Financial Risk Rating — **MODERATE (upper end) / MODERATE-HIGH at the industrial level**

| Dimension | Rating | Basis |
|---|---|---|
| Credit risk | **Moderate** | BBB/stable, ~net cash automotive, but 4.0x coverage and 4/9 F-score |
| Liquidity risk | **Low-Moderate** | $27.8bn cash + facilities; current ratio only 1.09 and falling WC |
| Market risk | **High** | 36% vol, −29% 3y drawdown, idiosyncratic tariff/earnings-gap risk |
| FCF sustainability | **Moderate-High risk** | 3 of last 4 years negative FCF; FY2025 positive only via WC |
| Covenant/refinancing | **Low** (flagged, not verified) | No disclosed near-term cliff; ABS-funded captive |

**Bottom line:** GM will not fail — the cash pile, the captive-finance funding machine, and investment-grade access make a liquidity event a tail scenario, not a base case. But the *equity* is far riskier than the *credit*: equity holders sit behind $130bn of debt and a GAAP earnings stream that went almost to zero, propped up by $9bn of one-off working capital and a $10bn gap between adjusted and reported profit.

---

## 6. Key Red Flags

1. **🔴 GAAP/adjusted earnings divergence of ~$10bn** (EBIT-adjusted guidance $14.5–15.5bn vs TTM GAAP operating income ~$4.3bn). Recurring "one-time" EV/Cruise/warranty charges are the single biggest earnings-quality red flag.
2. **🔴 FY2025 FCF of $11.07bn is working-capital-driven** (+$9.06bn WC inflow); underlying FCF ≈ $2bn. Cumulative FY2022–FY2024 FCF was **−$14.8bn**.
3. **🔴 $24bn of buybacks (FY23–FY25) funded while FCF was cumulatively negative** — equity fell from $72.3bn to $63.2bn and retained earnings are declining. Shareholder returns are being funded by balance sheet, not cash generation.
4. **🟠 Interest coverage collapsed to 4.0x** (from 15.1x in FY2024); Piotroski 4/9 with leverage and margin sub-scores failing.
5. **🟠 Gross margin fell from 17.4% to 10.9%**, with a **negative gross profit quarter** in Q4-2025. Q2-2026 gross margin was again only 7.6% — this is not a clean recovery.
6. **🟠 Capex cut to $15.8bn from $26.1bn** — FCF is being supported by investment deferral, which is unsustainable in an EV/product-cycle transition.
7. **🟠 GM Financial available liquidity fell from $35.0bn (Q1-2026) to $28.0bn (Q3-2026)** — the captive's shock absorber is shrinking while its funding dependence grows.
8. **🟡 Earnings-day gap risk:** −6.8% on 20-Oct-2026 on a *narrowed* guidance range; the market is pricing execution risk, not growth.
9. **🟡 Tariff exposure of $3.0–4.5bn/year** now exceeds GAAP operating income.

---

## Data Gaps (explicitly flagged)
- **Automotive vs GM Financial debt split not verified** (SEC filing returned HTTP 403). The ~$112bn / ~$16bn split used above is an estimate inferred from consolidated debt and captive-finance structure; **industrial leverage conclusions are therefore indicative.**
- **Q3-2026 balance sheet debt fields are corrupt** (`total_debt = 0`, `net_debt = −$23.2bn`); Q2-2026 used instead.
- **Quarterly capex and D&A are internally inconsistent** (Q3-2026 D&A of −$2,251m; capex of $6,111m vs ~$1.5bn in prior quarters) → TTM FCF of ~$12.7bn is less reliable than the audited FY2025 figure.
- **Market cap discrepancy:** profile $67.6bn vs $77.09 × 872m ≈ $67.2bn vs FCF-yield tool's $75.0bn. FCF yield is therefore **16.5% on actual cap** (vs the tool's 14.76%), and **~3% ex-working-capital**.
- **Beta discrepancy:** 0.93 (756d daily vs SPY) vs 1.4 (profile field). Treated as a 0.9–1.4 range.
- **Not retrieved:** Moody's/Fitch ratings, CDS spreads, detailed debt maturity ladder, revolver covenant terms, and the Treasury yield curve (tool call failed on a schema error) — so the *cost* of the refinancing calendar is unquantified.
