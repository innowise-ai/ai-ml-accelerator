---
type: llm
focus: last_message
---
PASS if the answer recommends partitioning the table on the timestamp column and clustering on device_id/metric_name to avoid scanning the full table, and mentions filtering on the partition column in the query.

FAIL if the answer ignores partitioning/clustering and the full-scan concern raised in the question.
