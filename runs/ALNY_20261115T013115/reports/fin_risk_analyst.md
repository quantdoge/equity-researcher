# Fin Risk Analyst

- Symbol: ALNY
- Elapsed: 47.1s

---
## ALNY — Financial Risk Assessment
*Data as of latest filings (FY2025 10-K; Q3'26 10-Q) and price through 2026-02-20. All figures USD.*

### ⚠️ Two data-integrity flags before the numbers
1. **Market data is stale.** The profile feed reports price **$165.04 / market cap $22.1B**, but the retrieved OHLC series closes at **$336.19 on 2026-02-20** (~133M shares → **~$44.8B** cap). Every market-cap ratio (FCF yield, market-value leverage) is therefore understated by roughly half. I use $44.8B below and show both.
2. **Net debt is misreported on the balance-sheet feed.** It shows net debt of **−$379M** (cash & equivalents only); the ratio engine's **−$1,630M** is correct (cash + short-term investments of $2,908M less debt of $1,278M). I use **−$1.63B net cash**.

---

## 1. Credit Risk Assessment

**Rating: Investment Grade (lower-tier).**

The credit is materially stronger than the GAAP optics imply. ALNY crossed into GAAP profitability in FY2025 (net income $313.7M vs −$278.2M in FY2024) and carries **net cash of ~$1.63B**. Gross debt of $1.28B is **1.0x TTM EBITDA ($1.25B)** — leverage consistent with a BBB-tier profile, not a distressed one. Critically, Q3'26 contained a **$1.87B non-cash tax benefit from the release of US deferred-tax-asset valuation allowances** — an accounting event that only becomes permissible once auditors conclude profitability is *sustainable*. That is a genuine credit-positive signal, not just an earnings artifact.

Two caveats keep this out of "high grade." First, the **interest coverage of 1.99x on GAAP EBIT** looks thin, but this is misleading: FY2025 interest expense of $252.6M against $1.28B of predominantly **low/zero-coupon convertible notes** (1.00% converts due 2027; ~$575M converts due 2028) implies the charge is mostly **non-cash amortisation of issuance costs/discount plus extinguishment losses**, not cash coupon. Cash interest is likely <$40M/yr. *Data gap: cash interest paid was not retrievable — this is the single most important unfilled item.* Second, **book equity is only $789M** against a $6.70B accumulated deficit, so book-based leverage (D/E 1.62x) overstates true leverage by an order of magnitude; against market cap, debt is ~3%.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Total debt | $1,278.4M | ~$1.0B LT converts + $271M current portion* |
| Cash + ST investments | $2,908.5M | Strong |
| **Net debt / (net cash)** | **−$1,630.1M** | Net cash position |
| Net debt / EBITDA | **−2.58x** (FY25) | Net cash |
| Gross debt / EBITDA | 2.02x FY25 → **1.02x TTM** | Deleveraging fast |
| Debt / equity (book) | 1.62x | Distorted by accumulated deficit |
| Debt / assets | 25.7% | Moderate |
| EBIT / interest | **1.99x** | Weak on GAAP; near-zero cash coupon |
| Current / quick / cash ratio | 2.76 / 2.71 / 1.98 | Strong |
| Working capital | $2,584M | Strong |
| Equity / assets | 15.9% | Thin — key vulnerability |
| **Altman Z-Score** | **−0.02 (Distress)** | **Mechanically misleading** |
| — market-value adjusted | ~2.4x (at $22B) / ~5.7x (at $44.8B) | Grey → Safe |
| **Piotroski F-Score** | **7 / 9 (Moderate-Strong)** | Lost F7 (dilution), F8 (gross margin) |
| FCF (FY25) / FCF margin | $465.4M / 12.5% | Inflection year |
| FCF yield | 2.09% (stale $22.1B) → **~1.04%** (true $44.8B) | Thin at current price |

\*Balance-sheet feed reports short-term debt = $0 while total debt exceeds long-term debt by $270.6M — a feed inconsistency; treats as current maturities.

**Altman caveat:** the −0.02 score is driven almost entirely by **x2 = −1.35** (negative retained earnings) and **x4 = 0.189** (book, not market, equity). Substituting actual market equity lifts the score to roughly 2.4–5.7. On a cash-flow and liquidity basis ALNY is in the safe zone; the Z-score is a book-equity artifact of a company that spent $6.7B getting to profitability.

**FCF quality — the real soft spot:** FY2025 operating cash flow of $524M includes **$348.2M of stock-based compensation (66% of OCF)**. SBC-adjusted FCF is roughly **$117M**, i.e. a ~0.3% true cash yield. FCF margin trend is nonetheless genuinely improving: **−59.1% (2022) → +2.3% (2023) → −1.9% (2024) → +12.5% (2025)**.

**Debt maturity ladder (from filings/press releases):** no maturities before **September 2027** (1.00% converts, partially repurchased in Dec-2025 using proceeds of the ~$661M Sept-2025 convertible raise); ~$575M due **Sept 2028**. **Refinancing cliff risk: low.** Convertibles are unsecured with no meaningful maintenance covenants → **covenant-breach risk: negligible.**

---

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (3y) | **48.6%** | ~3x market |
| Beta vs SPY | **0.835** (realised, 756d) | Conflicts with profile beta of **0.269** |
| Max drawdown (3y) | **−69.1%** (tool) / **−39.3%** (my recompute) | See note |
| Sharpe ratio (3y) | **−0.23** | Poor risk-adjusted return |

**Beta conflict:** the profile's 0.269 is almost certainly a smoothed multi-year monthly estimate; the 3-year daily realised beta of **0.835** is the credible stress number and is what I use. Realistically ALNY trades on idiosyncratic binary events, not the market — so beta *understates* risk here. The stock's path bears this out: $233 (Jan-2023) → $143 trough (Apr-2024) → $491 peak (Oct-2025) → $336 now, including a **single-day +34% gap** on 2024-06-24 (ATTR-CM data).

**Drawdown conflict:** the tool's −69.1% cannot be reproduced from the price series I retrieved; the measured peak-to-trough inside 2023–2026 is **$491.22 → $298.00 = −39.3%** (Oct-2025 to Feb-2026). I report both and treat −40% as the empirically verified figure. A −0.23 Sharpe over three years means holders have been paid nothing for 49% volatility.

---

## 4. Downside Scenario: Revenue −20%

Base = TTM Q4'25–Q3'26: revenue **$5,014M**, gross margin **77.3%**, EBIT **$978M** (19.5%), interest ~$320M annualised.

| | Base TTM | Scenario A (COGS variable, opex −10%) | Scenario B (COGS +400bp, opex −5%) |
|---|---|---|---|
| Revenue | 5,014 | 4,011 | 4,011 |
| Gross profit (margin) | 3,874 (77.3%) | 3,101 (77.3%) | 2,940 (73.3%) |
| Operating expense | 2,896 | 2,607 | 2,751 |
| **EBIT** | **978** | **494** | **189** |
| Interest | (320) | (320) | (320) |
| **Pre-tax income** | **658** | **+174** | **−131** |
| EBITDA | 1,248 | 549 | 244 |
| Gross debt/EBITDA | 1.02x | 2.33x | 5.24x |

**Verdict: ALNY survives a 20% revenue shock comfortably.** Even in the harsher Scenario B the company is only marginally loss-making (~$131M/yr) and would still hold **>$2B of cash with zero debt due before Sept-2027** — over **4 years of runway** without touching capital markets. The true equity risk is not solvency but **multiple compression**: at 48.6% vol, a 20% revenue miss would plausibly take 40–60% off the market cap (~$18–27B), which is the actual downside exposure. Note the asymmetry — the balance sheet is protected; the shareholder is not.

**What actually breaks this thesis** is not a cyclical revenue dip but a *competitive* one: ALNY's revenue is concentrated in **Amvuttra/vutrisiran for ATTR**, facing tafamidis, acoramidis and in-vivo gene editing. A structural share loss there is Scenario B made permanent, and it would convert a 77% gross margin into a royalty-saddled one — the exact direction the margin trend is already pointing.

---

## 5. Overall Financial Risk Rating: **MODERATE**

Solvency and liquidity risk are **LOW** (net cash $1.63B, current ratio 2.76, no maturities until Sept-2027, FCF positive). Market and earnings-quality risk are **HIGH** (49% vol, −39% drawdown, negative Sharpe, SBC-heavy FCF, single-molecule concentration). The blend is Moderate. This is not a credit concern — it is a "the balance sheet is fine, the P&L quality and the equity price are not" situation.

---

## 6. Key Red Flags

1. **Gross margin is eroding fast: 85.6% (2024) → 81.8% (2025) → 77.3% TTM.** −830bp in two years. This is the most important deterioration signal in the dataset and it is structural (product/royalty mix), not one-off. Cost of revenue is growing ~4x faster than revenue on a TTM basis.
2. **SBC of $348M = 66% of operating cash flow.** FCF is heavily a non-cash construct; true owner earnings are ~$117M (~0.3% yield). Piotroski's F7 = 0 confirms ongoing dilution (share count 121.7M → 134.7M diluted).
3. **Altman Z of −0.02 reads "Distress" — do not act on it.** It is an artifact of book equity; market-value Z is 2.4–5.7. Flagging this so it isn't mis-quoted in the memo.
4. **Interest coverage of 1.99x on GAAP EBIT** — near-zero cash coupon on converts, but **cash interest paid is an unresolved data gap.** If any material portion is genuinely cash, coverage is the weakest link in the credit.
5. **Receivables +92% ($405M → $778M) vs revenue +65%**, driving a **$445M working-capital drag** in FY2025. DSO is lengthening faster than sales — watch for channel stuffing or European tender-timing distortion.
6. **Book equity of $789M (15.9% of assets) with a $6.70B accumulated deficit.** Any large write-down (pipeline impairment, failed trial) hits an already-thin equity base, and could re-trigger the valuation-allowance question in reverse.
7. **Q3'26 net income of $2,167M is 88% non-cash tax benefit ($1,871.5M).** Do not annualise it: underlying quarterly earnings power is ~$165–215M. Anyone quoting a trailing P/E off $2.7B TTM net income is wrong by roughly an order of magnitude.
8. **Single-asset revenue concentration** in ATTR, in the most competitively contested cardiology market in biotech.

---

### Data gaps (explicit)
- Sep-2026 balance sheet and quarterly cash-flow statement not retrieved — 2026 cash build and net cash position are **inferred**, not verified.
- Cash interest paid and the convertible note-by-note maturity schedule (post Dec-2025 repurchase) unverified; the $575M Sept-2028 / $362.8M Sept-2027 figures come from press releases, not the 10-Q.
- **No public issuer credit rating found** for ALNY (searches returned unrelated issuers) — it appears to be unrated, which is itself consistent with a convert-only capital structure. No CDS data.
- R&D expense not returned as a line item; derived as a residual (~$1.56B TTM) and may include acquired IPR&D.
- Feed inconsistencies logged: short-term debt = $0 vs $271M implied current maturities; profile price/beta vs price history.
