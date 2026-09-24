---
type: regex
target: last_message
pattern: 'dry.?run'
flags: i
---
A dry run (`--dry_run` in `bq`, or `job_config.dry_run = True` in a client library) reports bytes processed without executing or billing for the query.
