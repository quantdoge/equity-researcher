# Portfolio Strategist

- Symbol: AMD
- Elapsed: 52.5s

---
# AMD — PORTFOLIO CONSTRUCTION RECOMMENDATION

**Price $446.23 (20-Nov-2026) | Mkt cap ~$730B | Final Action: PASS**

---

## 0. Data Integrity Corrections (read before the table)

Four inputs the desk is relying on do not survive independent verification:

| Claim used by agents | Verified | Impact |
|---|---|---|
| Beta 2.49 | **3.56 vs SPY** (252d); 77.5% annualized vol | Risk budgeting was understated by ~43% |
| "+250% YTD / +72% YoY" | **12-1 momentum = +7.0%**; $459.61 (1-Sep) → $446.23 (20-Nov) = **−3%** | The "crowded momentum unwind" framing is wrong — there is no momentum left to unwind |
| P/E ~96x | **168x** trailing (FY25 EPS); **EV/EBITDA 99.5x; P/FCF 108x** | Premium to peer median **+511%** |
| Street median PT $650 | Confirmed — **but every target pre-dates the 19-Nov short report** | Targets are stale, not corroborating |

Also: **the Quant Analyst submitted an empty report.** One of twelve inputs is missing; I have not imputed it.

---

## 1. Agent Conviction Summary

| Agent | View | Conviction | Key Finding |
|---|---|---|---|
| **Growth** | BUY | High (long-only bias) | 2027 guide >+80%; 25x FY27E; 7/7 beats; 5 hyperscalers in production |
| **Value** | SELL / AVOID | **High** | Base IV $280–305, *bull* $420 — **both below spot**; 0.92% FCF yield |
| **Sector** | Attractive sector, **late cycle** | Med-High | AMD is the only name slower *and* less profitable than peer median yet on the highest multiple |
| **Macro** | UNFAVOURABLE | **High** | 10Y real ~2.91%, Fed hiking, HY OAS +89bp — pure multiple-compression regime |
| **Geo Legal** | HIGH risk | **High** | 40–50% odds of formal inquiry; 22.4% China; 50%-ownership rule returns 10-Jan-27 |
| **Nonfin Risk** | HIGH risk | **High** | 3 securities investigations in 24hrs; CEO sold >$320M, **zero insider buying** |
| **Fin Risk** | LOW credit / HIGH market | **High** | Net cash $6.1B, A1, Altman Z 3.74 — solvency is not the risk; *price* is |
| **Short** | SHORT (valuation) | Medium | **Explicitly clears AMD of fraud** (Beneish −2.76, DSO 98→67). $85B OpenAI warrant = equity-for-revenue |
| **ESG** | Average, deteriorating | Medium | Governance 6.5/10; fails export-control controversy screen; Dec hearing is live |
| **Alt Data** | NEUTRAL, bearish skew | **Low** | Product search −25% to −85% YoY; consensus already **above** company guide |
| **Quant** | — | — | **NO REPORT SUBMITTED** |

---

## 2. Consensus Assessment: **SPLIT on direction — HIGH consensus on risk**

**Where all eleven agents agree (this is the finding that matters):** the *business* is excellent. Growth, Value, Short, Fin Risk and ESG independently confirm it — revenue +45%, Data Center +97%, GM 480bp→462bp→445bp→461bp→495bp→**54%**, credit flawless, no accounting manipulation. The Short Analyst went hunting for fraud and found none.

**Where they split:** price. Growth says 25x FY27E is cheap; Value says the *bull* case is $420, i.e. 6% below spot.

**Conflict resolution:**
1. **Short vs Value** — resolved in Value's favour on severity but *narrowed* by Short. The bear case is a **multiple/durability** bear case, not an integrity one. That bounds the downside tail (no restatement) but does not shrink the central estimate.
2. **Growth vs Value** — **Value takes precedence**, because Growth's own data contains the disconfirming fact: FY2028 consensus revenue range is **$106.7B–$207.2B**, a 2× spread. You cannot capitalize a 25x FY27E multiple on a number with that dispersion. Growth's PEG of 0.62 is an artifact of a 2030 estimate ($242.7B, 5.3× TTM) that no agent can underwrite.
3. **Risk agents (Macro + Geo + Nonfin + Fin-Risk/valuation) all line up negative, unhedged, and dated.** Four independent domains, four HIGH ratings, one shared catalyst calendar.

**Net: 6 of 10 substantive agents negative, 1 positive, 3 neutral. The bull case is single-threaded and depends entirely on forward estimates landing.**

---

## 3. Position Sizing Recommendation: **0.0% now → 1.5–2.0% on triggers**

**The risk-equivalent math is the whole argument.** At 77.5% vol vs ~16% for the index:

> **A 2% AMD position contributes the same portfolio risk as a ~9.7% S&P position.** A 1% position = **4.8% S&P-equivalent risk.**

This is not a small-cap-style "1% lottery ticket." One percent of AMD is nearly five percent of index-risk.

**Kelly check (for calibration, not for action):** probability-weighted scenarios (Bull 25% → $900; Base 30% → $620; Bear 30% → $340; Severe 15% → $180) give EV ≈ **$540, +21%**. Full Kelly on σ=0.775 = edge/variance ≈ 0.33 → ~33%. Applying ¼-Kelly → ~8%, then haircutting for (a) 2× revenue dispersion, (b) a binary hearing two weeks out, (c) 0.81 correlation to QQQ → **practical ceiling 2%**. Kelly says the *edge* is real; it does not say own it *today*, ahead of an unresolvable event.

---

## 4. Portfolio Fit Analysis

**Correlation (252d) — the key table:**

| | AMD | TSM | MU | AVGO | NVDA | QQQ |
|---|---|---|---|---|---|---|
| AMD | 1.00 | **0.74** | **0.67** | **0.63** | 0.50 | **0.81** |

- **AMD is more correlated to QQQ (0.81) than to any semiconductor.** It is not a diversifying sector bet — it is a **levered Nasdaq instrument** (beta 3.56). Adding it does not add sector alpha; it adds index beta at 3.6×.
- **Correlation to NVDA is only 0.50** — AMD is *not* a cheap NVDA substitute. If the book already owns NVDA/AVGO/MU/TSM, AMD stacks a fourth correlated AI-capex leg.
- **Factor tilts added:** high beta (+), high valuation (−), momentum (weak, +7%), negative quality (ROIC 5.47% reported, 0.92% FCF yield), large size (0). It dilutes any quality or low-vol tilt.

**The relative-value verdict — the most actionable portfolio point:**
> If the mandate wants AI-semiconductor exposure, **AMD is currently the worst risk-adjusted way to get it.** NVDA trades at ~14.6× trailing with 74.8% GM and 56% net margin; MU at ~8.3× with 80.7% GM. AMD trades at **168× trailing / 99.5× EV-EBITDA / 0.92% FCF yield / 53.7% GM.** Same cycle, same geopolitics, one-third the profitability, twenty times the multiple.

**Sector concentration test:** before any initiation, confirm total AI-capex-cluster exposure (NVDA + AVGO + MU + TSM + AMD + hyperscalers) is below **25%** of NAV. Given 0.63–0.74 pairwise correlations, a 2% AMD adds meaningfully to cluster VaR.

---

## 5. Entry Strategy: **Scale in on catalysts — do not buy ahead of 1-Dec/December hearing**

Three tranches, each condition-gated. **Tranche 1 fires only *after* the December congressional hearing passes without AMD being named or subpoenaed.**

| Tranche | Size | Trigger |
|---|---|---|
| **T1** | 0.75% | December hearing concludes clean **AND** price holds >$420 (above the 5-Nov capitulation low of $402.10) |
| **T2** | 0.75% | Price <$380 (**21× FY27E** — Growth's own stated upgrade trigger) **or** Q4 print (2-Feb-27) confirms ≥$17.0B rev and ≥54% GM |
| **T3** | 0.50% | Two consecutive quarters of sequential decline in both inventory days and DSO, with FY28 estimates *raised* (Short Analyst's cover condition) |

If price runs to $600+ before any trigger fires, **do not chase** — that is 90% of the stale $650 median and far above Value's $420 bull case.

---

## 6. Risk Management Rules

**Stop-loss (fundamental, not price — 77.5% vol makes a 15–20% price stop pure noise; daily σ ≈ 4.9%):**
- **Hard price stop: $400** — a decisive close below the 5-Nov capitulation low ($402.10) fails the technical thesis.
- **Fundamental stop (immediate):** any 10-Q/8-K disclosing a **BIS subpoena, government inquiry, or formal SEC investigation** → exit the full position same session, no averaging down.
- **Fundamental stop:** Q4 revenue below **$16.5B** (low end of guide) or GAAP gross margin below **52%**.

**Thesis invalidation conditions:**
1. Hyperscaler 2027 capex guidance cut below **~$950B** (from ~$1.2–1.3T) — Macro's transmission channel.
2. FY2028 revenue consensus cut **>10%** (currently $137.2B, range $106.7–207.2B — the 2× spread *is* the thesis risk).
3. Inventory days cross **180** (currently 165 — the pattern that preceded the 2022–23 −66%).
4. HY OAS gaps above **5.0%** (currently 3.52%, +89bp in 11 weeks) — Macro's single best tell.
5. OpenAI fails to fund its 1GW MI450 tranche, or the warrant is disclosed as a **contra-revenue charge** ≥10% of FY27 revenue.

**Trim trigger:** $585–600 (≈90% of the $650 stale median, and 40%+ above Value's *bull* case). Trim 50% there; do not hold for $650.

**Governance red flag to monitor:** any 10b5-1 plan *amendment* by Lisa Su within 90 days of the 19-Nov report. Executive PSUs adding a compliance metric in the 2027 proxy would be the single clearest positive governance signal.

---

## 7. Final Portfolio Action: **PASS**

**For a new position: PASS.** Not because AMD is a bad business — it is a very good one, and the Short Analyst's forensic work explicitly clears it of fraud. Pass because:
1. **Negative margin of safety.** Value's base IV is $280–305 and its *bull* case is $420; both sit below $446. There is no price at which the downside is protected.
2. **The catalyst calendar is adverse and imminent** — a December congressional hearing and three open securities investigations arrive *before* the 2-Feb-27 earnings print. I do not need to own a 77.5%-vol, 3.56-beta name through a binary unresolvable event to express a thesis I can enter after it, cheaper and better-informed.
3. **77.5% vol + 0.81 QQQ correlation** means even a "small" position is a large directional bet on the Nasdaq and on hyperscaler capex financing.
4. **Superior substitutes exist in the same trade** — NVDA at 14.6× and MU at 8.3× offer the same cycle with real cash flow.

**For an existing holder: REDUCE to ≤1.0%** (≈4.8% S&P-equivalent risk) immediately, ahead of the December hearing, and hold the residual against the rules in §6.

**Re-entry is live and specific** — the three tranches in §5 cap the eventual position at **2.0%**, contingent on catalyst clearance or a move to 21× FY27E. The watchlist entry is *not* "AMD is down 32%"; it is **"the regulatory overhang has resolved, or the price is below $380."** Neither is true today.

---

*Data gaps carried forward: Quant Analyst report absent; no forward-estimate verification of the FY27E/FY29E EPS series that the entire 25× multiple rests on; the 4-agent bull case is unverifiable against a FY2028 range whose 2× spread no agent could narrow; peer-multiple tool returned only 8 peers with no forward multiples; debt maturity ladder and CDS unavailable (immaterial at 0.07× D/E).*
