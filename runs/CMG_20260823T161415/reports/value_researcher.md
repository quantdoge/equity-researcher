# value_researcher

_2026-08-23T08:18:13+00:00_

# Value Analysis — Chipotle Mexican Grill (CMG)

**Researcher note on data access:** The session `fmp_call` limit was reached before I could hit the `quote`/current, `company/profile-symbol`, and `company/peers` endpoints. Where those are material I say so and cite the source I used instead. All FMP figures below carry tool + endpoint. I did not compute (or transform) any derived metric; everything cited is a field fetched from FMP or a web corroboration.

---

## 1. Business Quality & Moat Assessment

**Rating: Narrow-to-Moderate brand moat (not wide, thinning).**

Evidence:
- **Pricing / brand power is being tested.** Full-year 2025 comparable-restaurant sales declined **–1.7%**, the first annual same-store decline since 2016 (web: Chipotle Q4/2025 press release, Chipo IR 2026-02-03). Q4-2025 comp sales **–2.5%**, Q2-2025 **–4.0%** with transactions down ~4.9% (web: PR Newswire / Restaurant Dive). This is a day-to-day brand losing traffic to value-focused fast food — the opposite of durable pricing power.
- **No network effects, trivial switching costs.** A burrito is substitutable. The moat rests on brand intangible + efficient scale (a broad fresh-food supply chain and ~3,700-store base), not on lock-in.
- **Reputational wobble:** portion-size skimping allegations (CEO confirmed ~10% of stores in 2024, Forbes) and an earlier food-safety history (2015 E. coli) show the brand intangible/trust moat is breachable.
- **Returns on capital are real but typical of an asset-heavy grower:** ROIC ~18–19% (see §2) is above a reasonable WACC, so the capital engine works — that is the strongest "moat" evidence — but gross margin is slipping (see §2), which says pricing power is *softening*, not widening.

**Verdict:** Brands moat is Narrow and, on a 5-year look-back, has **narrowed** (2021-2024 saw 40-50x earnings and strong pricing; 2025 saw the first same-store decline since 2016). This is not a Coke or a Visa. It is a good fast-food consumer brand with a defensible but porous moat.

---

## 2. Financial Quality Score

**Score: 6.5 / 10** — outstanding profitability metrics, but deteriorating momentum and a capital-hungry lease-loaded balance sheet.

| Metric | Value | Source (tool / endpoint) |
|---|---|---|
| Return on equity | **54.3%** FY2025; **53.3%** TTM | statements / key-metrics, key-metrics-ttm |
| ROIC (return on invested capital) | **19.0%** FY2025; **18.2%** TTM; 17.6% FY2024; 16.3% FY2023 | statements / key-metrics |
| Return on assets | 17.1% FY2025 | statements / key-metrics |
| Gross margin | **25.4%** FY2025; **24.1%** TTM (was 26.7% FY2024) | statements / metrics-ratios, metrics-ratios-ttm |
| Net margin | **12.9%** FY2025; **11.4%** TTM | statements / metrics-ratios, metrics-ratios-ttm |
| EBITDA margin | **19.9%** FY2025; **18.3%** TTM | statements / metrics-ratios |
| Owner earnings | $314M Q4-2025; $603M Q1-2026; **$640M Q2-2026** (≈ $2.1B annualized); $0.496/share (Q2-2026) | statements / owner-earnings |
| Free cash flow / operating cash flow | **0.68x** (FCF consumed by heavy capex) | statements / key-metrics-ttm |
| Free cash flow yield | **3.3%** TTM | statements / key-metrics-ttm |
| FCF per share | $1.22 TTM | statements / key-metrics-ttm |
| Capex / D&A | **2.0x** TTM; ~1.8x FY2025 | statements / key-metrics-ttm |
| Balance sheet / leverage | Net debt **$9.50B** FY2025; debt/equity 3.48x FY2025; **netDebt/EBITDA 2.28x TTM** | statements / balance-sheet-statement, key-metrics-ttm |

**Notes you should calibrate against:**
- **The leverage is not as scary as it looks.** FMP classifies ~$4.77B of *operating lease obligations* (`capitalLeaseObligationsNonCurrent`, FY2025) as debt — that is real-estate leases for stores, standard for a leased-asset restaurant model, not borrowings. Core interest-bearing debt is essentially zero (`longTermDebt` ~$4.77B is leases; `interestExpense` = 0 in the FY2025 income statement). ROIC≥18% on this basis comfortably exceeds WACC.
- **Margins are rolling backward:** gross 26.7% → 24.1% and net 13.6% → 11.4% over 2024→TTM. This is the single most important negative-trend datum in the set.
- **No dividends** (dividend payout 0) — Chip returns cash via buybacks (weighted average shares fell from 1.377B FY2023 to 1.337B FY2025).

---

## 3. Intrinsic Value (FMP DCF — fetched, not derived)

| Model | Intrinsic value / share | Source |
|---|---|---|
| **DCF, unlevered (dcf-advanced)** | **$26.89** | deductedCashFlow / dcf-advanced |
| **DCF, levered (dcf-levered)** | **$24.17** | discountedCashFlow / dcf-levered |

FMP's own DCF therefore puts intrinsic value in the **~$24–27/share** range. I add no human adjustment headroom on top of these, per my mandate to avoid hand-built DCFs.

---

## 4. Margin of Safety vs Current Price

- Current share price: **≈ $36.90** — FMP; noted in the DCF endpoints' `Stock Price` field (36.9), corroborated by web (CNN 🔎$36.90; macrotrends $36.90; Morningstar market cap $46.7B / ~1.27B shares). I could **not** directly reach the `quote` endpoint this session (call limit), so treat this as web-corroborated rather than a live quote.
- Mark-to-intrinsic gap (FMP DCF basis):
  - vs advanced unlevered DCF counter: price is **+37%** above	intrinsic.
  - vs levered DCF: **+53%** above intrinsic.

**There is no margin of safety.** In fact the price embeds an ~27-35% *premium* over the FCO intrinsic estimate — the wrong side of the bargain for a Buffett-style buyer who only buys at a 20–30% discount to value.

---

## 5. Valuation Multiple vs History / Peers

| Metric | Current | Historical | Source |
|---|---|---|---|
| P/E | **32.2x** FY2025; **33.2x** TTM | 53.8x FY2024; 51.4x FY2023 | statements / metrics-ratios, metrics-ratios-ttm |
| EV/EBITDA | **23.1x** TTM (24.8x FY2025) | 37.2x FY2024; 34.1x FY2023 | statements / key-metrics |
| Price/FCF | 30.2x TTM | 54.6x FY2024 | statements / metrics-ratios |

- The stock has **de-rated dramatically** from its 2021–2024 bubble (40–50x earnings) to ~33x now. Web corroboration: macrotrends current PE ~33x vs 10-yr avg ~80x; value investing.io EV/EBITDA ~18.6x. Note: the 10-yr *average* is flattered by bubble years, so "cheap vs average" is a weak point in isolation.
- I could **not** fetch the `company/peers` endpoint (call limit); peer-calibrated multiples (McD, Y(N), etc.) are a **data gap**. From web only: Chipotle's EV/EBITDA runs ~1.5–2x & peers (e.g., research-gate note it is "much higher than others", ~42x in 2024). Not enough to conclude a discount — only that it historically commanded vast multiples.

Even after the multiple collapse, the market price sits decidedly above FMP's capped DCF intrinsic value.

---

## 6. Investment Verdict

**Sell / Avoid for value (Hold/no-action if you already own at historical cost).**

The operator is a genuinely high-ROIC consumer brand (ROE ~53%, ROIC ~19%, no real debt, ~ any-owner earnings ~$2.1B). But:
1. The **moat is narrowing** — first same-store comp decline since 2016, negative traffic, portion-size/food-safety fractures.
2. **Margins are compressing** (net margin 12.9%→11.4% TTM) while capex/D&A runs ~2x (growth capital eating FOCF).
3. The **market price is ~35% above** FMP's own DCF intrinsic value ($24–27 vs $36.90). There is no margin of safety; there is negative edge.

A lovely business bought at a full (or premium) price is not a Warren-Buffett buy. That is precisely the case here.

---

## 7. Key Risks to the Value Thesis / Open Data

- **Narrow moat thesis, correctly** — the outcome rests on it. If comp sales ever re-accelerate and gross margin recovers above 26%, the DCF case brightens materially; my "Sell" is a function of both price *and* the 2025 traffic break.
- **Live price gap:** `quote`/current not fetched — confirm $36.90 before acting; material (±$1 changes the safety margin by ~3 points).
- **Peer multiples not fetched** — request `company/peers` for McD vs Yum vs Shake Shack to size the 23x EV/EBITDA premium.
- **FMP counts operating leases as debt** (~$4.77B) — the `netDebt`, `debtToEquity (~3.5x)`, and `netDebtToEBITDA` figures are inflated versus conventional interest-debt treatment. Rebase on interest-bearing-debt-only if you want a cleaner leverage read.
- **Share-count basis (~1.2–1.4B shares)** — FMP's per-share DCF and EPS are computed on FMP's own count; confirm against the actual 10-K share count before treating $26.89/’24.17 as per-real-share intrinsic values.
- **Legacy/ownership** — insider selling was flagged (former CEO Niccol, who left to Starbucks in Aug-2024, replaced by former COO Scot Boatwright confirmed Nov-2024). No FMP insider-ownership figures were fetched this session → for the quant_engineer: pull and compute insider-ownership % and buyback-or-bulge trend over the FY2023–26 statements.

**Recommended follow-ups for quant_engineer (FMP does not return these):** (a) 5-year ROIC series — I only have FY2023–25 here; (b) FCF/net-income conversion trend (the income-meg + incomeConversion fields are proxies); (c) insider-ownership % and money; (d) a margin trend (gross/operating) enforcing the 2024→TTM compression.
