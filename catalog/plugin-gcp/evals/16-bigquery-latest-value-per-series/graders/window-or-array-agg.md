---
type: regex
target: last_message
pattern: 'ROW_NUMBER|QUALIFY|ARRAY_AGG'
flags: i
---
Getting the latest full row per group (not just an aggregated value) requires a window-function pattern — `QUALIFY ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ts DESC) = 1` or `ARRAY_AGG(... ORDER BY ts DESC LIMIT 1)[OFFSET(0)]` — plain `MAX(value)` cannot return the associated row.
