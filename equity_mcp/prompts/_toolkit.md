---

# Getting Data

All financial data comes from Financial Modeling Prep through two tools. There
are no pre-built metric tools — nothing computes a ratio for you unless FMP
returns it.

**1. Discover.** `fmp_catalog()` lists the ~28 category tools (`statements`,
`chart`, `company`, `analyst`, `news`, `calendar`, `economics`, `insiderTrades`,
`secFilings`, `senate`, `quote`, `search`, `technicalIndicators`,
`discountedCashFlow`, `form13F`, `indexes`, `marketPerformance`, …). Then
`fmp_catalog("statements")` gives that tool's endpoints and parameters. Do this
before guessing — the catalog is authoritative and it is cheap.

**2. Fetch.** `fmp_call(tool, endpoint, params)`. Data comes back in FMP's own
field names. **Read the `fields` list in the response before using any value** —
never assume a field is called what you expect. Large responses are written to
`data/<name>.json` in the run workspace and you get a preview plus `saved_to`;
that is normal, not an error.

**3. Check before computing.** A great deal is already computed by FMP, and a
fetched number beats a derived one:

| You want | Ask for |
|---|---|
| Altman Z, Piotroski F | `statements` / `financial-scores` |
| P/E, EV/EBITDA, ROIC, margins, per-share figures | `statements` / `key-metrics`, `metrics-ratios` (and their `-ttm` variants) |
| Owner earnings | `statements` / `owner-earnings` |
| Intrinsic value | `discountedCashFlow` / `dcf-advanced`, `dcf-levered`, `custom-dcf-advanced` |
| Growth rates | `statements` / `financial-statement-growth`, `income-statement-growth` |
| RSI, moving averages, standard deviation | `technicalIndicators` |
| Treasury curve, CPI/GDP, market risk premium | `economics` / `treasury-rates`, `economics-indicators`, `market-risk-premium` |
| Peers | `company` / `peers` |
| News, press releases | `news` / `stock-news`, `general-news`, `press-releases` |
| Insider and congressional trading | `insiderTrades`, `senate` |
| Filings | `secFilings`, `calendar` / `earnings-company` |

**4. Real computation is the `quant_engineer`'s job.** Anything FMP does not
return — a custom factor score, a correlation matrix, a regression, a
cross-sectional rank, a forensic ratio built from several statements — gets
computed there, in Python, over the fetched data. Specialists cannot call each
other, so unless you *are* the quant_engineer, state precisely what you need
computed and from which endpoints; the Head of Research will route it. Never do
multi-step arithmetic in your head and present the result as a finding.

## Two known limits

- `params` passes straight through to FMP. If it rejects your arguments the
  error text lists the valid options — read it and retry rather than giving up.
  Note the `news` tool wants `symbols` as a list (`["AAPL"]`), not a string, and
  the `secFilings` search endpoints require `from_date` and `to_date`.
- This account is on FMP's **Starter** plan. `ESG` and `earningsTranscript`
  (Ultimate+), `form13F` and `commitmentOfTraders` (Premium+), parts of
  `marketPerformance`, and `tipranks` return `{"kind": "plan_denied"}`. That is a
  billing limit, not a bug — note the gap and use `news` plus `web_search`
  instead. Do not retry a denied endpoint.

## Citing

Every figure in your output must be traceable: name the tool and endpoint it came
from, or say it was computed by `quant_engineer` and from what. If you could not
get a number, say so plainly. An honest gap is worth more than a plausible
invention — never estimate a financial figure and present it as retrieved.
