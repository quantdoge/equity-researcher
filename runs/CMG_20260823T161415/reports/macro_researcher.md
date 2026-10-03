# macro_researcher

_2026-08-23T08:18:07+00:00_

# Macro Environment Research — CMG (Chipotle Mexican Grill)
**Prepared by:** Macroeconomy Researcher | **Data as of:** ~Aug 21, 2026

---

## 1. Current Macro Regime

The environment is **transitional**. Policy rates have already been cut substantially from their 2023–24 peak but are now **on hold**; inflation is still **elevated above the 2% target** and only grinding lower; growth is positive but consumer-led and increasingly K-shaped (upper-income resilient, lower-income squeezed). This is a "higher-for-slightly-longer, sticky inflation" regime — not a recession regime, not a stimulative regime.

**Monetary policy (sources: Federal Reserve FOMC minutes via web; J.P. Morgan, Morgan Stanley, iShares):**
- Fed funds target range: **3.50%–3.75%**, unchanged at the July 2026 meeting (web_search: Federal Reserve FOMC minutes 6/17/2026; Yahoo/J.P. Morgan).
- The Fed has made **no rate cuts in 2026 to date**. Markets price only ~36% odds of a single 2026 cut; Morgan Stanley notes markets even price a possible hike; the Fed minutes carry some rate cuts toward late-2026/2027.
- **Inflation message:** "elevated inflationary pressures" cited as the reason the Fed is waiting rather than cutting (Schwab/CNBC).

**Inflation (FMP + web):**
- CPI index: **326.031 (Dec-2025)**, 325.063 (Nov-2025), 324.245 (Sep-2025) — `fmp_call(economics/economics-indicators, name=CPI)`.
- _Year-over-year CPI: **3.4% in July 2026**, down from 3.5% in June 2026; core ~2.5% (web: CNBC, Trading Economics, NY Fed). Food at-home inflation ~2.98% y/y, energy +14.7% (JEC Senate).
- Monthly CPI in July: +0.1% m/m (CNBC) — decelerating but **sticky above target**.

**Growth (source: `fmp_call(economics/economics-indicators, name=GDP) + web):**
- FMP GDP point: **$31,422.5** (2025-10-01); **only a single point returned**, so growth cannot be de-annualized from FMP data alone.
- Qualitative: U.S. retail & food services sales +5.0% y/y in July 2026 but −0.6% m/m (U.S. Bank via web). TD Economics characterizes 2026 consumer spending as solid but "K-shaped."

---

## 2. Yield Curve Shape & Signal

**Treasury rates (2026-08-21, `fmp_call(economics/treasury-rates)`):**

| Maturity | Yield (%) |
|---|---|
| 3-mo | 3.88 |
| 1-yr | 4.03 |
| 2-yr | 4.24 |
| 3-yr | 4.31 |
| 5-yr | 4.43 |
| 10-yr | 4.74 |
| 20-yr | 5.25 |
| 30-yr | 5.27 |

**Shape:** Upward-sloping everywhere — **no inversion**. The front end (3-mo 3.88% vs 10-yr 4.74%) is **+0.86 pts**; 2s10s is ~+0.50%. The 10s30s (4.74%→5.27%) is steep, and the 20-year sits only 2 bp under the 30-year.

**What it signals:**
- The positively sloped 3-mo→10-yr curve is **not** flashing the classic recession signal (historically a negative 3m-10y spread precedes downturns). Near-term downturn risk from the curve itself is muted.
- The sharply higher 30-yr/20-yr (−5.25/5.27%) vs the 10-yr indicates **large term-premium repricing** — investors demand meaningful long-duration compensation, consistent with elevated long-run inflation fear and heavy fiscal supply. This is the key macro watch for long-duration assets.

---

## 3. Company-Specific Macro Impact (CMG)

**Consumer discretionary spending power — NEGATIVE bias.** 
- CMG is fast-casual ($8.79 avg entrée; typical meal $10–15), sitting between QSR and casual. Consumers are **pulling back in discretionary categories, most pronounced among low-income households** (McKinsey State of the US Consumer, May 2026); Q2 2026 household debt reached 79% of disposable personal income (NRA). 
- Mitigant: CM cites its core customer tilting **higher-income**, which is more resilient; but CMG has still seen **transaction/traffic softness** (Q1 2026 comp sales +0.5%; Q2 2026 records show comp sales +2.2% but the + signs breakdown: +1.2% check / +1.0% transactions). Traffic weakness is the discretionary-squeeze signal.

**Labor costs — NEGATIVE.** 
- Restaurant labor shrink has drifted up (industry fast-casual labor ~27–32% sales; CMG is lower). CMG **Q1 2026 labor = 26.1%** of revenue, up from 25.0% a year earlier; **H1 2026 = 25.5%** vs 24.8% (company releases via web). Minimum-wage increases / state wage floors keep pushing on the line.

**Food / commodity costs — NEGATIVE.** CMG **H1 2026 food & packaging = 29.6%** of revenue, up from 29.0% (company via Pulse 2.0). Chipotle cites beef, dairy, and avocado as cost drivers (avocados ~19% y/y at one point in 2024; beef up ~1.9% per coverage). Hikes fatten a -2% menu price per newspaper cover. Energy inflation at +14.7% (JEC) pressures store/commodity chain costs.

**Interest-rate sensitivity — LOW/NEUTRAL.** CMG is **low-leverage** with minimal refinancing exposure; it is not a rate-sensitive business like a REIT or utility. The main channel is **valuation discount rate**: CMG is a long-duration growth asset, so a higher-for-longer curve compresses its multiple — a persist, though soft comps already do.

**Currency / trade — NEUTRAL-to-minimal.** CMG derives effectively all revenue from North America; international (Canada, UK/Europe, Middle East, Mexico) is a small share. USD strength has only marginal translation/trans fee effect. Not a primary driver.

| Variable | Direction for CMG |
|---|---|
| CPI decelerating but >3% (sticky) | Negative (labor+food margin, pricing power fading) |
| Fed on hold @3.5–3.75 | Neutral-to-negative (discount rate) |
| Yield curve steepening long-end | Negative (long-duration multiple, but CM is low-beta) |
| Discretionary pullback, low-income soft | Negative (traffic/transactions) |
| Higher-income tilt of CMG base | Shelfier tailwind → less downside |
| Real wage growth / energy relief | Conditional tailwind if sustained |
| USD strength | Negligible (domestic-heavy) |

---

## 4. Macro Tailwinds & Headwinds (12–24 months)

**Headwinds**
1. Sticky, above-target inflation (~3.4% headline) keeping the Fed restrictive; if it re-accelerates, cuts keep slipping and long yields stay elevated → margin + multiple compression.
2. Labor cost creep (state minimum wages) — structural and compounding.
3. Food/avocado/beef-input inflation is running ahead of menu-price pass-through (CM only guiding ~+2% price) → restaurant margin.
4. Ongoing low-income discretionary contraction; CM's bathroom/transactions look flat-to-down despite price/mix growth.

**Tailwinds**
1. If the Fed delivers a late-2026/2027 cut (markets now place meaningful probability; minutes flag late-2026/Q1-2027 cuts), the front-end curve steps lower — supports restaurant-values and consumer funding conditions.
2. Real wage growth as headline inflation decelerates is restoring discretionary purchasing power for intact cohorts.
3. CMG itself is **outpacing** its own (Q2 revenue +9.3% y/y; raised full-year comp-sales guidance) despite industry headwinds — an idiosyn macroeconomic offset as modest.

---

## 5. Data Gaps & Next Steps

- **GDP growth rate:** FMP `economics-indicators` (name=GDP) returned a **single** point ($21,422B, 2025-10-01); no growth % was retrievable. Need quant_engineer to compute from a multi-quarter series or pull a separate GDP-growth series.
- **CPI y/y from CMGs data:** FMP returned only 3 index points (Sep/Nov/Dec-2025) — insufficient for y/y calc without retrieving a fuller range. I used web-sourced y/y (3.4% July 2026).
- **Market risk premium:** FMP `economics/market-risk-premium` returned the full 192-country file (US row present) but the US figure could not be isolated inline; I used Damodaran's July 2026 estimated **4.42% ERP** instead. Quant_engine should pull the US row from `data/economics_market-risk-premium.json`.
- **Unemployment / labor-force utilization:** `economics-indicators` rejected "Unemployment Rate"/"Real GDP" (invalid identifier). Gaps: CLS); used web context (NRA: eating-and-drinking employment only +0.5% vs Feb 2020). Quant_engine or a different series needed.
- **FX / USD index:** no USD-dollar series pulled for this report; CMG's currency exposure is small, but a DXY/USD series would quantify the minor effect if required.
- **Forecast series:** SPF/consensus (CPI 3.5% avg 2026, 2.9% 2027 per Philadelphia Fed) is web-based, not FMP.

---

**Net macro rating: Neutral-to-unfavourable** — a in a sticky-inflation, higher-for-longer-rate regime with a K-shaped consumer squeezing discretionary categories, but partially offset by CMG's higher-income skew, minimal leverage, and positive idiosyncratic momentum. The **clearest macro scenario that could surprise to the downside**: a renewed food/energy cost shock re-accelerates CPI (energy already +14.7% y/y), forcing the Fed to postpone cuts into 2027 while long-dated yields (20/30y at 5.25/5.27%) push higher — squeezing both CMG restaurant margin and its long-duration valuation multiple.

Every FMP figure is attributed above to `fmp_call(economics/…)`; all policy/inflation/labor/CMG-specific figures are web-sourced and flagged as such. Where no figure was retrievable, I have said so rather than estimating.
