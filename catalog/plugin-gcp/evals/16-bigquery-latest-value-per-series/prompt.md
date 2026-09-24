---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, bigquery, sql, time-series]
---
I have a long-format telemetry table in BigQuery: `(device_id, metric_name, ts, value)`. For each device and metric, I need the single most recent reading — not an aggregate like `MAX(value)`, the actual latest row including its timestamp. What's the right way to write that query so it doesn't do a full table scan?
