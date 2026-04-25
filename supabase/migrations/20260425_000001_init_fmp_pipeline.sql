-- FMP + Supabase baseline data platform
create extension if not exists pgcrypto;

create schema if not exists ref;
create schema if not exists raw;
create schema if not exists core;
create schema if not exists ops;

create table if not exists ref.symbol (
  symbol text primary key,
  name text,
  exchange text,
  asset_type text,
  currency text,
  country text,
  is_active boolean not null default true,
  first_seen_at timestamptz not null default now(),
  last_seen_at timestamptz not null default now()
);

create table if not exists ref.company (
  symbol text primary key references ref.symbol(symbol) on delete cascade,
  cik text,
  isin text,
  cusip text,
  sector text,
  industry text,
  ipo_date date,
  description text,
  website text,
  updated_at timestamptz not null default now()
);

create table if not exists ref.symbol_change (
  old_symbol text not null,
  new_symbol text not null,
  change_date date not null,
  reason text,
  created_at timestamptz not null default now(),
  primary key (old_symbol, new_symbol, change_date)
);

create table if not exists raw.fmp_payload (
  id bigint generated always as identity primary key,
  endpoint_name text not null,
  request_url text not null,
  symbol text,
  query_params jsonb not null default '{}'::jsonb,
  as_of_date date,
  fetched_at timestamptz not null default now(),
  http_status integer not null,
  payload jsonb not null,
  payload_hash text,
  error_text text
);

create index if not exists idx_raw_fmp_endpoint_fetched
  on raw.fmp_payload(endpoint_name, fetched_at desc);

create index if not exists idx_raw_fmp_symbol_endpoint_fetched
  on raw.fmp_payload(symbol, endpoint_name, fetched_at desc);

create table if not exists core.price_daily (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  date date not null,
  open numeric(18, 6),
  high numeric(18, 6),
  low numeric(18, 6),
  close numeric(18, 6),
  adj_close numeric(18, 6),
  volume bigint,
  source_updated_at timestamptz,
  ingested_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, date)
);

create index if not exists idx_price_daily_symbol_date_desc
  on core.price_daily(symbol, date desc);

create table if not exists core.income_statement (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  period_end date not null,
  period_type text not null check (period_type in ('annual', 'quarter')),
  reported_currency text,
  filing_date date,
  accepted_date timestamptz,
  revenue numeric,
  gross_profit numeric,
  operating_income numeric,
  net_income numeric,
  eps numeric,
  eps_diluted numeric,
  source_updated_at timestamptz,
  ingested_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, period_end, period_type)
);

create table if not exists core.balance_sheet (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  period_end date not null,
  period_type text not null check (period_type in ('annual', 'quarter')),
  reported_currency text,
  filing_date date,
  accepted_date timestamptz,
  total_assets numeric,
  total_liabilities numeric,
  total_equity numeric,
  cash_and_short_term_investments numeric,
  total_debt numeric,
  source_updated_at timestamptz,
  ingested_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, period_end, period_type)
);

create table if not exists core.cash_flow (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  period_end date not null,
  period_type text not null check (period_type in ('annual', 'quarter')),
  reported_currency text,
  filing_date date,
  accepted_date timestamptz,
  operating_cash_flow numeric,
  capital_expenditure numeric,
  free_cash_flow numeric,
  source_updated_at timestamptz,
  ingested_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, period_end, period_type)
);

create table if not exists core.earnings_calendar (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  event_date date not null,
  time_of_day text,
  eps_estimate numeric,
  eps_actual numeric,
  revenue_estimate numeric,
  revenue_actual numeric,
  updated_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, event_date)
);

create table if not exists core.dividends (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  ex_date date not null,
  payment_date date,
  record_date date,
  declaration_date date,
  dividend numeric,
  adjusted_dividend numeric,
  frequency text,
  updated_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, ex_date)
);

create table if not exists core.splits (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  split_date date not null,
  numerator integer,
  denominator integer,
  ratio numeric,
  updated_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, split_date)
);

create table if not exists core.analyst_estimates (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  period_end date not null,
  period_type text not null,
  eps_estimate numeric,
  revenue_estimate numeric,
  num_analysts integer,
  updated_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, period_end, period_type)
);

create table if not exists core.price_targets (
  symbol text not null references ref.symbol(symbol) on delete cascade,
  published_date date not null,
  analyst_name text not null,
  rating text,
  target_price numeric,
  previous_target_price numeric,
  publisher text not null,
  updated_at timestamptz not null default now(),
  record_hash text,
  primary key (symbol, published_date, analyst_name, publisher)
);

create table if not exists ops.pipeline_run (
  run_id uuid primary key default gen_random_uuid(),
  pipeline_name text not null,
  started_at timestamptz not null default now(),
  ended_at timestamptz,
  status text not null check (status in ('running', 'success', 'failed', 'partial')),
  rows_inserted bigint not null default 0,
  rows_updated bigint not null default 0,
  error_count integer not null default 0,
  notes text
);

create table if not exists ops.endpoint_watermark (
  endpoint_name text not null,
  symbol text,
  last_success_cursor text,
  last_success_date date,
  last_success_ts timestamptz,
  updated_at timestamptz not null default now(),
  primary key (endpoint_name, symbol)
);

create table if not exists ops.ingest_error (
  id bigint generated always as identity primary key,
  run_id uuid references ops.pipeline_run(run_id) on delete set null,
  endpoint_name text not null,
  symbol text,
  request_url text,
  error_class text,
  error_message text,
  payload jsonb,
  created_at timestamptz not null default now()
);

create or replace function ops.touch_watermark(
  p_endpoint_name text,
  p_symbol text,
  p_last_success_date date,
  p_last_success_ts timestamptz,
  p_last_success_cursor text default null
)
returns void
language sql
as $$
  insert into ops.endpoint_watermark(
    endpoint_name,
    symbol,
    last_success_cursor,
    last_success_date,
    last_success_ts,
    updated_at
  ) values (
    p_endpoint_name,
    p_symbol,
    p_last_success_cursor,
    p_last_success_date,
    p_last_success_ts,
    now()
  )
  on conflict(endpoint_name, symbol)
  do update set
    last_success_cursor = excluded.last_success_cursor,
    last_success_date = excluded.last_success_date,
    last_success_ts = excluded.last_success_ts,
    updated_at = now();
$$;

create or replace view ops.v_freshness as
select
  endpoint_name,
  symbol,
  last_success_date,
  last_success_ts,
  now() - coalesce(last_success_ts, updated_at) as staleness
from ops.endpoint_watermark;
