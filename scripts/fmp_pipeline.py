#!/usr/bin/env python3
"""Daily Financial Modeling Prep -> Supabase/Postgres ingestion skeleton.

Usage:
  python scripts/fmp_pipeline.py --domain reference
  python scripts/fmp_pipeline.py --domain fundamentals --symbols AAPL,MSFT

Environment:
  DATABASE_URL=postgresql://...
  FMP_API_KEY=...
  FMP_BASE_URL=https://financialmodelingprep.com
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
import time
import urllib.parse
from typing import Any

import psycopg
import requests
import yaml


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def record_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.md5(canonical.encode("utf-8"), usedforsecurity=False).hexdigest()


def load_config(path: str = "pipeline/endpoints.yaml") -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def db_conn() -> psycopg.Connection:
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL is not set")
    return psycopg.connect(db_url)


def fmp_get(path: str, params: dict[str, Any]) -> tuple[int, Any, str]:
    base_url = os.environ.get("FMP_BASE_URL", "https://financialmodelingprep.com")
    api_key = os.environ.get("FMP_API_KEY")
    if not api_key:
        raise RuntimeError("FMP_API_KEY is not set")

    req_params = dict(params)
    req_params["apikey"] = api_key
    query = urllib.parse.urlencode(req_params)
    url = f"{base_url}{path}?{query}"

    for attempt in range(5):
        response = requests.get(url, timeout=30)
        if response.status_code in (429, 500, 502, 503, 504):
            sleep_sec = 2 ** attempt
            time.sleep(sleep_sec)
            continue
        try:
            return response.status_code, response.json(), url
        except Exception:
            return response.status_code, {"raw": response.text}, url
    return response.status_code, {"error": "max retries exceeded"}, url


def write_raw_payload(
    conn: psycopg.Connection,
    endpoint_name: str,
    request_url: str,
    symbol: str | None,
    params: dict[str, Any],
    as_of_date: dt.date | None,
    status: int,
    payload: Any,
    error_text: str | None,
) -> None:
    payload_json = json.dumps(payload)
    payload_obj = payload if isinstance(payload, dict | list) else {"payload": payload}
    p_hash = record_hash({"payload": payload_obj})
    with conn.cursor() as cur:
        cur.execute(
            """
            insert into raw.fmp_payload(
              endpoint_name, request_url, symbol, query_params,
              as_of_date, http_status, payload, payload_hash, error_text
            ) values (%s,%s,%s,%s,%s,%s,%s::jsonb,%s,%s)
            """,
            (
                endpoint_name,
                request_url,
                symbol,
                json.dumps(params),
                as_of_date,
                status,
                payload_json,
                p_hash,
                error_text,
            ),
        )


def start_run(conn: psycopg.Connection, pipeline_name: str) -> str:
    with conn.cursor() as cur:
        cur.execute(
            """
            insert into ops.pipeline_run(pipeline_name, status)
            values (%s, 'running')
            returning run_id::text
            """,
            (pipeline_name,),
        )
        run_id = cur.fetchone()[0]
    return run_id


def end_run(conn: psycopg.Connection, run_id: str, status: str, notes: str = "") -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            update ops.pipeline_run
               set status = %s,
                   ended_at = now(),
                   notes = %s
             where run_id::text = %s
            """,
            (status, notes, run_id),
        )


def touch_watermark(
    conn: psycopg.Connection,
    endpoint_name: str,
    symbol: str | None,
    success_date: dt.date | None,
) -> None:
    with conn.cursor() as cur:
        cur.execute(
            "select ops.touch_watermark(%s, %s, %s, %s, %s)",
            (endpoint_name, symbol, success_date, utcnow(), None),
        )


def selected_symbols(cli_symbols: str | None) -> list[str | None]:
    if not cli_symbols:
        return [None]
    return [s.strip().upper() for s in cli_symbols.split(",") if s.strip()]


def run_domain(domain: str, symbols_arg: str | None) -> int:
    cfg = load_config()
    domains = cfg.get("domains", {})
    if domain not in domains:
        print(f"Unknown domain: {domain}", file=sys.stderr)
        return 2

    endpoints = domains[domain].get("endpoints", [])
    symbols = selected_symbols(symbols_arg)

    with db_conn() as conn:
        run_id = start_run(conn, f"fmp-{domain}")
        errors = 0

        try:
            for ep in endpoints:
                name = ep["name"]
                path_template = ep["path"]
                for symbol in symbols:
                    path = path_template.format(symbol=symbol) if "{symbol}" in path_template else path_template
                    params = {}
                    if symbol and "{symbol}" not in path_template:
                        params["symbol"] = symbol

                    status, payload, url = fmp_get(path, params)
                    error_text = None if status < 400 else f"http_status={status}"
                    write_raw_payload(
                        conn,
                        endpoint_name=name,
                        request_url=url,
                        symbol=symbol,
                        params=params,
                        as_of_date=dt.date.today(),
                        status=status,
                        payload=payload,
                        error_text=error_text,
                    )

                    if status >= 400:
                        errors += 1
                        with conn.cursor() as cur:
                            cur.execute(
                                """
                                insert into ops.ingest_error(
                                  run_id, endpoint_name, symbol, request_url,
                                  error_class, error_message, payload
                                ) values (%s::uuid, %s, %s, %s, %s, %s, %s::jsonb)
                                """,
                                (
                                    run_id,
                                    name,
                                    symbol,
                                    url,
                                    "HTTP_ERROR",
                                    error_text,
                                    json.dumps(payload),
                                ),
                            )
                    else:
                        touch_watermark(conn, name, symbol, dt.date.today())

            final_status = "success" if errors == 0 else "partial"
            end_run(conn, run_id, final_status, notes=f"errors={errors}")
            conn.commit()
            return 0 if errors == 0 else 1
        except Exception as exc:
            conn.rollback()
            with conn.cursor() as cur:
                cur.execute(
                    """
                    update ops.pipeline_run
                       set status = 'failed', ended_at = now(), notes = %s
                     where run_id::text = %s
                    """,
                    (str(exc), run_id),
                )
            conn.commit()
            print(f"Pipeline failed: {exc}", file=sys.stderr)
            return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run FMP ingestion pipeline domain")
    parser.add_argument("--domain", required=True, help="reference|prices|fundamentals|events|analyst")
    parser.add_argument("--symbols", required=False, help="comma-delimited symbols for symbol-scoped endpoints")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run_domain(args.domain, args.symbols)


if __name__ == "__main__":
    raise SystemExit(main())
