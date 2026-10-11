"""
Hyperparameter snapshots: what configuration produced each research run.

- snapshot.py builds a content-addressed snapshot from live module state.
- capture.py writes one per run to runs/<id>/config.json.
- ingest.py stores snapshots and run links in the `hparams` schema.
- backfill.py reconstructs snapshots for runs that predate capture.

CLI: ``python -m equity_mcp.hparams --help``.
"""
