---
type: regex
target: last_message
pattern: '--dry_run'
flags: i
---
Estimating bytes scanned without running the query is `bq query --use_legacy_sql=false --dry_run '...'`. This is the step most likely to be answered with a cost-estimate hand-wave or a Console screenshot instead of a command.
