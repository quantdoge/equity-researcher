# equity-researcher

Equity Research Team formed by a system of AI agents- data engineering agent, quantitative analyst agent, long-only equity analyst agent, short-only equity analyst agent, credit analyst agent, economist agent, risk analyst agent, head of researcher agent.

## FMP -> Supabase continuous data pipeline

This repo now includes a production-ready starter for ingesting Financial Modeling Prep (FMP) data into Supabase/Postgres on a continuous schedule.

### Included components

- **Supabase SQL migration** with schemas and tables:
  - `ref`: symbols and company metadata
  - `raw`: immutable raw API payloads
  - `core`: normalized market/fundamental/event/analyst tables
  - `ops`: pipeline runs, endpoint watermarks, ingestion errors
- **Endpoint contract config** in `pipeline/endpoints.yaml`
- **Python ingestion skeleton** in `scripts/fmp_pipeline.py`
- **GitHub Actions workflow** in `.github/workflows/daily-fmp-pipeline.yml`

### Setup

1. Apply SQL migration to your Supabase project:
   - `supabase/migrations/20260425_000001_init_fmp_pipeline.sql`
2. Add GitHub repository secrets:
   - `DATABASE_URL` (Supabase Postgres connection string)
   - `FMP_API_KEY` (Financial Modeling Prep API key)
3. Install Python dependencies:
   - `pip install -r requirements.txt`

### Local run examples

```bash
python scripts/fmp_pipeline.py --domain reference
python scripts/fmp_pipeline.py --domain fundamentals --symbols AAPL,MSFT
python scripts/fmp_pipeline.py --domain prices --symbols AAPL
```

### Scheduling strategy

- `reference`: daily universe refresh
- `fundamentals`: daily statement refresh
- `events`: every 4 hours during weekdays
- `prices`: EOD weekday refresh
- `analyst`: daily analyst estimate/target refresh

You can adjust cadences and endpoint paths in `pipeline/endpoints.yaml`.

### Notes

- The pipeline always writes raw API responses to `raw.fmp_payload` before transforms.
- `ops.endpoint_watermark` enables incremental loads per endpoint/symbol.
- The starter script focuses on durable ingestion plumbing; you can add table-specific transform/upsert jobs as the next step.
