# Short Analyst

- Symbol: FDXF
- Elapsed: 111.9s

---
I now have enough to write. Two important findings changed my conclusion materially: the forensic scores are largely artifacts of carve-out accounting, and the LTL cycle has genuinely turned.

---

# FORENSIC SHORT ANALYSIS — FDXF (FedEx Freight Holding Company)

**Price $126.04 | Mkt cap $18.84bn | Net debt $6.11bn | EV $24.96bn**
**Spin-off from FedEx completed June 1, 2026. FY ends May 31.**

---

## 1. Earnings Quality Assessment

**Rating: MEDIUM-HIGH (quality of earnings is fine; quality of the *business* is not)**

This is the most important and counter-consensus finding in this report. Every mechanical forensic score screams fraud. On inspection, **most of that signal is an artifact of carve-out accounting, not manipulation.**

| Metric | Reported | Verdict |
|---|---|---|
| Beneish M-Score | **6.577** ("likely manipulator") | **Rejected — 4 of 8 inputs corrupted** |
| Accruals ratio | **+0.0709** (warning) | Artifact of one-off AR step-up |
| Cash conversion | **25.5%** | Normalizes to **~184%** |
| FCF conversion | **−32.4%** | Normalizes to positive |
| Earnings quality score | **25/100** | Not representative |
| Piotroski F-Score | **3/9** (weak) | Distorted by spin mechanics |
| Altman Z | **1.674** (distress) | Book-equity artifact |

**Why the M-Score must be discarded.** Decomposing it:

- **DSRI 8.97** — receivables/revenue went from 1.49% to 13.3%. Beneish reads this as channel stuffing. In reality, DSO is now **48.6 days** — squarely normal for an LTL carrier (peers run 40–50 days). The *prior* year was the anomaly: as part of FedEx, freight customer receivables were collected through FedEx's centralized AR and settled intercompany. Standalone AR is structurally new. **No channel stuffing.**
- **GMI 0.311** — driven by `cost_of_revenue = 0` in the FY2026 data. Data gap.
- **AQI 6.474** — driven by `ppe_net` going 4,132 → 0. Data gap, not a $4bn asset disappearance.
- **DEPI 0.091** — same corrupted D&A/PPE pairing.
- **SGI 0.99, SGAI 1.00** — neutral.
- **LVGI 2.048** — **this one is real and adverse** (debt/assets 28.5% → 92.5%).
- **TATA 0.0709** — real, but see below.

Adjusting FY2026 cash flow for the one-off ~$1,040m receivable build (the single largest component of the −$1,413m working capital swing), normalized OCF is **~$1,207m against $655m net income — 184% cash conversion.** That is high-quality earnings by any standard. There is **no accounting fraud thesis here.** Anyone pitching FDXF as a "Beneish 6.6 = manipulator" short has not read the carve-out.

---

## 2. Key Red Flags Found

1. **Negative book equity.** Total equity **−$497m**; liabilities $7,381m exceed assets $6,884m. Retained earnings −$509m. Debt loaded on at distribution: total debt **$1,433m → $6,365m** (+$4.9bn).
2. **Leverage into a cyclical.** Net debt/EBITDA **4.4x** (FY26). 4.4x on *trough* EBITDA with a negative equity cushion means no balance-sheet room to absorb a second leg down.
3. **Four consecutive years of revenue decline.** 10,084 → 9,424 → 8,887 → 8,795 (−12.8% cumulative, −4.5% CAGR).
4. **Operating leverage is brutal.** Operating income 1,894 → 1,753 → 1,339 → 540. Margin 18.8% → 18.6% → 15.1% → **6.1% GAAP / 10.7% adj.** A 13% revenue decline destroyed 71% of operating income.
5. **Self-serving margin target vs. delivery.** Pre-spin pitch was **"$8.7bn revenue and a 12% operating margin."** FY26 delivered $8.795bn revenue and **10.7% adjusted** operating margin. Guidance met on the top line, missed on the bottom.
6. **FedEx retains up to 19.9%** (~29.8m shares ≈ **$3.8bn**), and FDXF is now a *competitor* to FedEx's own operations. FedEx has every incentive to exit — a defined, dated technical overhang on a ~120m-share float.
7. **Data transparency is poor.** Duplicate quarter-ends, sign-flipped interest expense, missing COGS/PPE, a "gross margin" of 44.2% in Q1 FY27 versus 28–35% historically (evidently cost reclassification, since SG&A is reported as zero). Operating margin is the only trustworthy line.

**Rejected red flags (checked, came back clean):** receivable days (48.6, normal); inventory (LTL carries none); insider selling (the 25 Form 4s cluster on the June 3 and July 1 post-spin dates and are consistent with required holdings/grant reports — **I could not confirm net selling and will not assert it**); auditor changes (none found).

---

## 3. Beneish & Accruals Analysis

As detailed above: **M-Score 6.577 is not usable.** Only LVGI (2.05) and TATA (0.071) carry genuine information, and both say the same thing — **the balance sheet was re-levered at the spin and FY26 cash flow absorbed a one-time receivable build.**

Accruals of +0.071 clear the 0.05 warning threshold, but 100% of the excess is the AR step-up. Strip it and accruals are negative. **Conclusion: earnings manipulation probability LOW.**

---

## 4. Competitive Threat Assessment

This is where the real bear case lives, and it is stronger than the accounting case.

- **Share loss into a recovery.** The LTL cycle has turned: ODFL reported **August 2026 revenue per day +12.4%**, and over twelve months **ODFL +39.5%, XPO +50.1%, ArcBest +74.8%.** Over the same window **FDXF is down ~16% from its first-day close.** Most damning: FDXF's Q1 FY27 revenue grew **+3.1%** while the industry leader grew ~12% per day. Growing at a quarter of the market rate in an upcycle is a mix/share problem, not a macro problem.
- **Amazon LTL entry** is the genuine secular threat to the LTL oligopoly — a full-scale network launched through Amazon Freight. The #1 carrier has the most volume to lose.
- **Structural margin erosion is real:** gross margin 36.1% → 34.7% → 31.1%, and the 18.8%→10.7% operating margin slide is far worse than the revenue decline justifies. Some is cycle; some looks like permanent dis-synergy from losing FedEx procurement, IT and network density. **Transition Services Agreement costs roll off over roughly 12–24 months and are not yet fully in the run-rate.**
- **Counterweight (bull):** LTL remains a rational oligopoly with high barriers; FDXF is the largest player with the densest network, and Q1 FY27's 10.4% operating margin already shows sequential improvement. The 12% target is not fantasy.

---

## 5. Management Red Flags

No fraud-grade flags. Concerning but not disqualifying: (a) promotional pre-spin margin framing that FY26 did not deliver; (b) the spin was structured to extract $4.9bn of debt while leaving the equity account negative — standard sponsor playbook, and it transfers cyclical risk to public holders; (c) reporting transparency is weak. Governance includes a staggered board and no written-consent rights — mildly shareholder-unfriendly but standard for a fresh spin.

---

## 6. Short Thesis Summary

**The bear case is real but it is a *valuation and structure* case, not a fraud case.**

At $126.04, FDXF trades at **17.9x EV/EBITDA** on FY26 and FY27E, **27x FY27E EPS** (consensus $4.67), and **23x FY28E** — for a business with ~10% operating margins, four straight years of revenue decline, **negative book equity**, and **4.4x net leverage**. The correct LTL comp set (XPO, SAIA, ArcBest at roughly 11–14x) says a 10%-margin trucker does not deserve 18x. Only ODFL, at 25%+ margins, earns a premium multiple.

**Fair value: 14–16x FY27E EBITDA of $1,398m → EV $19.6–22.4bn → equity $13.5–16.3bn → $90–109/share.** Base case **~$100 (−21%)**.

Consensus is also a hockey stick: EBITDA **$1.40bn → $2.01bn by FY30 (+45%)** covered by only 3–8 analysts, all initiated post-IPO. Note the internal inconsistency — FY27E net income of $698m is not reconcilable with $1,398m EBITDA less ~$460m D&A less ~$220m of *new* interest. **Consensus FY27 EPS looks 15–25% too high.**

**The bull case, stated fairly:** the cycle *has* turned, Q1 beat ($1.49 adj vs $1.38), the stock popped 16%, and analysts are upgrading. If margins recover to 15% on $9.5bn revenue, EBITDA is ~$1.88bn and 15x supports **~$148**. A high multiple on trough EBITDA is the classic cyclical-bottoming signature, and a standalone #1 LTL asset carries strategic/takeout value. **If volume recovery accelerates, this short is wrong quickly.**

**Tactical caveat:** shorting one day after a 16% earnings beat into an upgrade cycle is poor entry. The trade wants a bounce that stalls, or evidence in the next 1–2 quarters that the +3% growth gap versus ODFL persists.

---

## 7. Contrarian Rating

### **SHORT** (moderate conviction — not Strong Short)

| | |
|---|---|
| **Fraud/manipulation risk** | **Low.** Beneish/Piotroski/Altman signals are carve-out artifacts. Do not market this as an accounting short. |
| **Valuation risk** | **High.** 18x trough EBITDA for a levered, shrinking, 10%-margin carrier. |
| **Balance-sheet risk** | **Elevated.** −$497m equity, 4.4x net leverage, no cushion. |
| **Structural risk** | **High.** TSA dis-synergies ahead; Amazon LTL; demonstrated share loss vs. ODFL. |
| **Technical risk** | **High, near-term.** FedEx's 19.9% (~$3.8bn) overhang; but also post-beat momentum *against* the short. |

**Reflexively bearish verdict I am explicitly rejecting:** treating the 6.577 M-Score as proof of manipulation. A rigorous reading shows cash conversion of 184%, normal receivable days, and no revenue-recognition games. **The short case is that FDXF is a mediocre, over-levered, no-growth business wearing a premium multiple — not that it is lying.**

**What would break the thesis:** operating margin sustained above 13% with revenue growth converging to the ~10% LTL industry rate, or net leverage below 3.0x.

**What would confirm it:** another quarter of ~3% growth against a double-digit market, TSA expiry disclosure revealing stranded costs, a FedEx secondary offering, or net leverage drifting above 5x into a softening freight market.
