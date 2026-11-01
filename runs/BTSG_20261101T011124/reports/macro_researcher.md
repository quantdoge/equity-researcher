# Macro Researcher

- Symbol: BTSG
- Elapsed: 64.1s

---
I have enough to write. Note two data gaps: the `fetch_yield_curve` tool returned nulls for all tenors (I computed spreads directly from DGS2/DGS10), and I could not confirm BrightSpring's exact net-debt figure — I've flagged leverage as an estimate.

---

# BTSG — Macroeconomic Impact Assessment
**BrightSpring Health Services, Inc.** | Healthcare — Home & Community-Based Services / Pharmacy
As of data through **30 Oct 2026** | Price $66.89 | Mkt cap $13.2bn | Beta 1.85

## 1. Macro Environment Summary — **Transitional, hawkish tilt ("reflation with a bear steepener")**

The US economy is in an unusual and uncomfortable configuration: **growth is solid, the labor market is tight, and inflation is re-accelerating — so the Fed has resumed hiking.** The FOMC raised the target range 25bp to **3.75–4.00% on 16 September 2026**, the first hike of the cycle, after holding at 3.50–3.75% from February through August. This is a regime change from the 2024–25 easing path (EFFR peaked at 5.33% in 2023–24, fell to 3.63% by Feb 2026, now back to 3.75%).

The bond market has responded with a **bear steepening**: the 10Y sits at **4.98%** (29 Oct), up ~60bp from 4.44% on 30 June, while the 2Y rose ~47bp to 4.61% — a 2s10s spread of about **+37bp**, steepened from +20bp in June. Part of the 2026 move is a global bond sell-off pushing the 10Y through 5%, i.e. term premium and supply, not just Fed expectations.

Critically, **credit markets have not yet corroborated the rate stress.** HY OAS is **326bp** (29 Oct) — still in the bottom decile historically — but it has **widened ~65bp from the 260bp cycle tight on 28 August**. That is a small but real deterioration in risk appetite.

**Stance: risk-on in equities and credit, risk-off in duration.** For a levered, high-multiple, long-duration healthcare equity, that is the wrong combination.

## 2. Key Macro Variables

| Variable | Latest | Prior / Reference | Direction | Source |
|---|---|---|---|---|
| Real GDP growth (q/q ann.) | **+3.4%** (Q3'26) | +2.2% (Q2'26); +0.2% (Q4'25) | Accelerating | BEA via FRED (GDPC1) |
| Real GDP (y/y) | **+2.07%** (Q3'26) | — | Solid | GDPC1 |
| CPI (y/y) | **+3.72%** (Sep'26) | +3.35% (Aug); +3.29% (Mar) | **Re-accelerating** | BLS (CPI series) |
| CPI (3-mo annualized) | **~4.6%** (Jul–Sep'26) | — | Above target | Calculated |
| Fed Funds (EFFR) | **3.75%** (Sep'26) | 3.63% (Feb–Aug'26) | **Hiking** | FRED FEDFUNDS |
| Fed target range | **3.75–4.00%** | 3.50–3.75% | +25bp on 16 Sep'26 | Fed |
| 10Y Treasury | **4.98%** (29 Oct'26) | 4.44% (30 Jun'26) | +54bp | FRED DGS10 |
| 2Y Treasury | **4.61%** (29 Oct'26) | 4.14% (30 Jun'26) | +47bp | FRED DGS2 |
| 2s10s spread | **+37bp** | +20bp (Jun); inverted 2023–24 | Bear steepening | Calculated |
| Unemployment | **4.2%** (Sep'26) | 4.0% (Jan'25); 4.5% peak (Nov'25) | Full employment | FRED UNRATE |
| HY OAS | **326bp** (29 Oct'26) | 260bp (28 Aug'26) | Widening off tights | FRED BAMLH0A0HYM2 |
| Broad USD index | **121.3** (23 Oct'26) | 117.9 (9 Sep'26) | +2.9% in 7 wks | FRED DTWEXBGS |

*Gaps: the yield-curve endpoint returned nulls for 5Y/30Y, so I derived the 2s10s from the DGS series directly. The PCE series available is nominal consumption levels, not the price deflator, so I have relied on CPI for the inflation read.*

## 3. Company-Specific Macro Impact

BrightSpring's revenue is ~**88% Pharmacy Solutions** (institutional/specialty drug distribution to skilled nursing, senior living and managed-care populations) and ~**12% Provider Services** (home health, hospice, personal care, rehab) — but the Provider segment carries a materially higher margin, so it punches far above its revenue weight in EBITDA. FY2026 guidance (raised 30 Oct): revenue **$15.9–16.1bn** (+17–19.5%), Adj EBITDA **$850–860m** (+37.6–39.3%). Q3: revenue $4.21bn (+26%), Adj EBITDA $228m (+42%), Adj EPS $0.54 (+80%).

| Macro variable | Impact | Reasoning |
|---|---|---|
| **Fed hiking / floating-rate debt** | **Negative** | The $2.55bn Term Loan B (refinanced Dec 2024 at –75bp, maturing **Feb 2031**) is floating-rate. Each +25bp of policy rate costs roughly **$6.4m/yr** pre-tax — ~0.7% of FY26 EBITDA. Real but digestible. No refinancing wall until 2031 — the maturity profile is genuinely a strength, not a risk. |
| **10Y at ~5.0% (discount rate)** | **Clearly negative** | At ~$13.2bn market cap plus roughly $3bn net debt, EV ≈ $16.3bn on $855m mid-point EBITDA ≈ **19x EV/EBITDA**. That is a long-duration asset. A 100bp move in the 10Y plausibly compresses 1.5–2.5 turns of multiple, i.e. **$2–3.5bn of EV, or 15–25% of the equity** — far larger than the interest-cost effect. This is the dominant monetary transmission channel for BTSG. |
| **Real GDP +3.4% / unemployment 4.2%** | **Neutral to mildly positive** | Demand is non-cyclical — Medicare/Medicaid enrollment and aging demographics (~3%/yr 65+ growth) drive volume, not the business cycle. Solid GDP is mildly helpful for commercial/managed-care volumes, but BTSG will not outperform because GDP is strong. Note beta of **1.85 is *financial* beta (leverage + multiple), not fundamental beta** — revenue is defensive, the equity is not. |
| **Wage inflation (~4%)** | **Negative, contained** | Labor-intensive: 23,500 employees, with home health aides and nurses the scarce input. At 4.2% unemployment, wage pressure persists — but this hits Provider Services (~12% of revenue) hardest, and management is offsetting with AI/automation that is showing early margin gains. Pharmacy, being 88% of revenue, is less labor-sensitive per dollar. |
| **CPI +3.7% / drug price inflation** | **Mixed** | Inflation *inflates* pharmacy revenue (pass-through of higher drug costs) but compresses gross margin %; gross profit dollars generally still rise. High medical inflation, however, is precisely what drives **Medicaid and Medicare rate pressure** — the second-order policy effect is negative. |
| **USD +2.9%, tariffs** | **Neutral** | Effectively **zero FX exposure** — essentially 100% US revenue, so dollar strength is irrelevant to the P&L. Tariffs on imported pharmaceuticals are an indirect COGS channel only, partly contractually passed through. Not a thesis driver. |
| **Medicaid / fiscal policy (H.R.1)** | **Strongly negative, 2027-weighted** | The largest macro variable for this company, and it is *fiscal*, not monetary. The 2025 reconciliation law reduces federal Medicaid spending by ~**$911bn (–14%)** over ten years, with work requirements, provider-tax limits and state trigger mechanisms. States are now legislating FY2027 budgets against that backdrop. Home- and community-based services (HCBS) and personal care — BTSG's Provider core — are "optional" benefits and therefore the most exposed line item. This arrives *after* the current beat-and-raise cycle, so the market is not yet pricing it. |
| **Credit conditions (HY OAS 326bp)** | **Positive but deteriorating** | Spreads remain near cycle tights and BTSG has no 2026–2028 maturities, so access to capital is not a near-term constraint. But the 65bp widening since August is the leading indicator to watch — a levered issuer's equity re-rates fast when spreads normalise. |

**The key insight:** BrightSpring is a **defensive revenue stream wrapped in a levered, long-duration balance sheet.** Macro risk reaches it almost entirely through (a) the discount rate applied to a 19x multiple and (b) government reimbursement budgets — not through the business cycle. That is the opposite of the usual cyclical exposure profile, and it means the *Fed and state legislatures* matter far more than GDP.

## 4. Macro Risk Rating: **NEUTRAL (with a negative skew)**

**Justification:** Operationally, the backdrop is supportive — full employment, +3.4% GDP, tight credit spreads, non-cyclical demand, no debt maturities until 2031, and a company beating and raising (+11% on 30 Oct alone; +67% YTD as of mid-October). Nothing in the *real* economy threatens the revenue line.

But the *financial* environment is actively hostile to the multiple: the Fed is **hiking** into 3.7% CPI with 3-month momentum near 4.6%, the 10Y is at 5% and bear-steepening, and spreads have begun to widen. For a 19x-EV/EBITDA, 1.85-beta, floating-rate borrower, that is a persistent de-rating force. Add a $911bn Medicaid contraction landing in FY2027 budgets and the skew is clearly to the downside — hence Neutral, not Favourable.

## 5. Scenario That Could Materially Surprise — **BEAR: the Fed is not done**

**The setup:** CPI momentum is running ~4.6% annualized over the last three months. If Q4 core prints stay above 3.5% y/y, the September hike is the first of several, the 10Y clears 5.25–5.50% on term premium, and HY OAS normalises from 326bp toward 450bp.

**The transmission to BTSG:**
- Multiple de-rates from ~19x to ~15x → EV falls ~$3.4bn, **equity −25% to −30% on unchanged EBITDA**;
- Floating-rate interest cost rises another ~$13m/yr at +50bp, and;
- This collides with state FY2027 Medicaid HCBS cuts, which hit Provider Services' high-margin revenue right as the multiple compresses.

**Why it's underappreciated:** the sell side is anchored on the beat-and-raise (revenue +26%, EBITDA +42%); the stock's −6.4% slide from $62.36 to $58.36 between 22 and 27 October while the 10Y held at 5% shows the equity is already rate-sensitive, and the 65bp spread widening since late August is an early, ignored warning. This is a rare case where the macro surprise arrives via **the discount rate and a state budget**, not via the economy.

**Bull offset (less likely, higher magnitude):** if Q4 shelter disinflation pulls CPI back toward 2.5% and the Fed signals the hike was a one-off, the 10Y at 4.30% plus 22x on raised FY27 guidance gives **+30–35%**.
