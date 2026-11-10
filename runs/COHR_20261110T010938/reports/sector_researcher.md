# Sector Researcher

- Symbol: COHR
- Elapsed: 50.7s

---
## Sector Brief: COHR (Coherent Corp.) — Optical Transceivers & Photonics Components

**Data note:** The platform tags COHR as "Technology / Hardware, Equipment & Parts," which spans Apple to Oracle and is analytically useless. I built a purpose-made peer set of US-listed optical/photonics competitors: **LITE, FN, MTSI, CIEN, AAOI**. All figures are from pulled financials; FYs are misaligned (COHR/June, FN/June, LITE/June, MTSI/Sept-Oct, CIEN/Nov, AAOI/Dec).

---

### 1. Sector Overview

The optical transceiver and photonics component sector (~$15–20B/yr revenue base in 2025) sits at the physical layer of the AI data centre build-out: every GPU-to-GPU fibre link requires a transceiver at each end, and the unit count scales with cluster size, not just bandwidth. The sector is in an acute **capacity-constrained upcycle** — 800G modules have been on allocation since 2025 with 30–50 week lead times, and the 800G→1.6T node transition is being pulled forward, with 800G+1.6T forecast at ~$14.6B in 2026, or ~64% of total module revenue. The binding constraint is **not assembly but the laser chip** — high-power InP EMLs and silicon-photonics engines — which take 18–24 months to add capacity, creating a genuine scarcity rent available only to vertically integrated chip owners. Structure is a barbell: a fragmented, price-competitive module-assembly layer (Coherent, Lumentum, AAOI, plus Chinese vendors Innolight/Eoptolink) and an oligopolistic InP/EML chip layer (Coherent, Lumentum, Broadcom, Mitsubishi) — top-3 concentration is roughly 50%+ in chips but under 40% in merchant modules (estimates). This is a **semiconductor-cycle business wearing a networking costume**: high beta (COHR 2.23, AAOI 3.99), violent drawdowns (−43% for COHR in the month to early November), and demand that is a derivative of six hyperscaler capex budgets.

**Porter's Five Forces (net: moderately attractive, cyclical):** Rivalry **high** at module level / moderate in chips. Buyer power **high and structurally rising** — a handful of hyperscalers and NVIDIA negotiate node-by-node price deflation. Supplier power **high** (InP epi, coherent DSPs from Broadcom/Marvell, lithography lead times). New entry threat **low** in chips (capital intensity, 18–24mo build) but **high** in assembly. Substitution threat **moderate rising** — copper DAC/AEC for sub-2m reach, and co-packaged optics (CPO) as a structural threat that would move value from pluggables to switch vendors over 3–5 years.

---

### 2. Key Tailwinds

- **Accelerating content-per-GPU and node transitions.** Each 400G→800G→1.6T step roughly doubles ASP per port while cost declines lag, and cluster transceiver counts are exploding (~200k+ transceivers for a single 100k-GPU cluster). Sector AI-segment growth is running **30–40%/yr**, and COHR's own FY27 pro forma guide is **>60%**.
- **Scarcity pricing is now being converted into contracted backlog.** COHR's **$20B five-year PhotonLink agreement** is the sector's clearest evidence that chip-level scarcity is migrating into multi-year take-or-pay contracts — a structural change from the historical spot-pricing model, ramping toward **$250M/quarter by end-2027**.
- **Operating leverage is inflecting hard across the group.** COHR gross margin went **30.9% (FY24) → 35.4% (FY25) → 37.5% (FY26) → 39.1% (Q1 FY27)**; operating margin **2.6% → 9.5% → 12.7% → 15.9%**. LITE went from **18.5% → 41.7%** GM over two years. Capacity utilisation is effectively full, so incremental revenue drops through at very high margins.

### 3. Key Headwinds

- **Hyperscaler capex digestion risk is the dominant swing factor.** The whole group just sold off violently (COHR −43% in a month, AAOI −16% in a day, LITE −13%) on AI-buildup concerns *despite* earnings beats — proof that the sector trades on capex sentiment, not reported fundamentals. Order books can gap down quickly.
- **Module-level price deflation and customer concentration.** COHR sells high-volume modules at market-clearing prices rather than scarcity prices (unlike Lumentum's narrower, chip-scarce mix) — hence its structurally lower gross margin. A handful of hyperscalers dictate pricing at each node transition, and Chinese vendors (Innolight, Eoptolink) continue taking module share on cost.
- **Capital intensity and working capital.** The industry is adding InP and module capacity simultaneously (18–24 month lead times), which pressures free cash flow exactly as revenue ramps — COHR's inventory is the metric bears are watching. Overbuild risk in 2028 is real if two or three capacity expansions land into a capex pause. Secondary: China revenue exposure and export-control/tariff risk.

---

### 4. Peer Comparison Table

| Company | Mkt Cap | Latest FY Rev | Rev Growth (latest FY) | Gross Margin | Operating Margin | P/S (trailing) | Beta |
|---|---|---|---|---|---|---|---|
| **COHR** | $44.3B | $7.12B (FY26, Jun) | **+22.5%** | 37.5% (Q1FY27: 39.1%) | 12.7% (Q1FY27: 15.9%) | **6.2x** (~3.9x FY27E) | 2.23 |
| LITE | $54.0B | $3.01B (FY26, Jun) | **+83.2%** | 41.7% | 17.4% | 17.9x | 1.65 |
| FN | $13.1B | $4.64B (FY26, Jun) | +35.7% | 12.0% | 10.0% | **2.8x** | 1.37 |
| MTSI | $17.6B | $1.33B (FY26, Oct) | +37.3% | **58.0%** | **23.0%** | 13.2x | 1.83 |
| CIEN | $38.2B | $4.77B (FY25, Nov) | +18.8% | 42.0% | 6.5% | 8.0x | 1.34 |
| AAOI | $4.4B | $0.46B (FY25, Dec) | +82.8% | 30.0% | −12.0% | 9.7x | 3.99 |
| **Peer median** | — | — | **+36.5%** | **39.6%** | **11.4%** | 8.9x | 1.74 |

*Caveats: trailing P/S mixes June–December FY ends and is distorted by growth rates (LITE/MTSI carry scarcity-premium multiples). EV multiples unavailable — debt was not pulled, so COHR's P/S flatters it slightly versus levered peers.*

**Read-through:** On *trailing* numbers COHR is a laggard on growth (22.5% vs 36.5% median) and roughly median on margin. But its latest quarter (Q1 FY27) is the tell: **+16% QoQ, ~+56% YoY pro forma, 39.1% GM, 15.9% OM** — that puts it at ~1.6x the peer median growth rate on a forward basis, with margins above peer median. At ~3.9x FY27E revenue, COHR is the **cheapest scaled asset in the group** (FN is cheaper on P/S but is a 12%-gross-margin contract manufacturer with no scarcity rent; LITE trades at ~4.5x COHR's multiple on far less revenue). Share-gain dynamic: **LITE and AAOI are gaining on growth rate; COHR is gaining on absolute scale (+~$2.4B of revenue in one year) and margin; CIEN is the relative loser** (18.8% growth, 6.5% OM — a telco-gear business, not an AI-pure-play).

---

### 5. COHR's Competitive Position: **STRONG** (with one structural caveat)

- **Scale leadership:** $7.1B FY26 revenue and ~$9.5B annualised run-rate — 1.5–2.3x LITE and ~5x AAOI. Sole US-listed player with merchant scale across lasers, optical components, *and* finished modules, plus 51,000 employees and a genuinely broad end-market mix (industrial, semiconductor, life sciences) that dampens datacom cyclicality versus pure-plays.
- **Vertical integration into the chokepoint:** InP/EML and silicon-photonics capability in-house means COHR captures chip-level scarcity rent, unlike Fabrinet (assembly only, 12% GM) — the single biggest reason to prefer it to FN on quality despite FN's cheaper multiple.
- **Margin trajectory is best-in-group improving:** +660bp GM and +1,330bp OM in two years, and management guides a first **$3B quarter by end-FY27** and **$4B quarter in FY28**.
- **Caveat:** it monetises scarcity only partially — the module business sells volume at market prices, so its 37–39% gross margin structurally trails LITE (41.7%) and MTSI (58.0%). Its defensibility is capacity, not pricing power. Coherent is the highest-quality *scale* asset here, not the highest-margin one.

---

### 6. Sector Rating: **ATTRACTIVE** (cyclically hot, high-volatility)

Demand is running ahead of supply in a market growing 30%+ with a hard 18–24 month supply constraint on the value-capturing input, contracted backlog is now multi-year, and group operating margins are still expanding — the classic signature of the *middle* of an upcycle, not the end. I stop short of a stronger rating for two reasons: **(1)** the sector's demand is a second derivative of six capex budgets, and the last thirty days demonstrated a 40%+ drawdown on sentiment alone with no fundamental deterioration; **(2)** capacity is being added industry-wide against a 2028 timeline that could coincide with an AI capex digestion. Positioning implication: COHR is the best risk-adjusted expression of the theme — scale, vertical integration, the cheapest forward sales multiple among scaled peers, and margin catch-up still in progress — but it should be sized as a **high-beta cyclical derivative (β 2.23), not a defensive compounder**, and the inventory/working-capital line is the key early-warning indicator to monitor each quarter.

**Gaps:** no EV/EBITDA, no forward EPS consensus, and no live monthly datacom module pricing data were available through these tools; hyperscaler capex guidance was inferred from news flow rather than primary filings.
