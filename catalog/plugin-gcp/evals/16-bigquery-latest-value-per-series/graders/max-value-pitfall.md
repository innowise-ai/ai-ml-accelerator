---
type: llm
focus: last_message
---
PASS if the answer explicitly explains why `MAX(value)` is wrong here: it returns the largest value ever recorded, not the most recent one, and loses the associated timestamp and other columns of that row.

FAIL if the answer proposes `MAX(value)` grouped by device/metric as sufficient, or never addresses the difference between "latest" and "maximum".
