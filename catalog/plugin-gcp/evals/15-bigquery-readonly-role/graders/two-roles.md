---
type: llm
focus: last_message
---
PASS if the answer grants both `roles/bigquery.dataViewer` (read table/view data) AND `roles/bigquery.jobUser` (permission to run query jobs in the project) — `dataViewer` alone lets you read data but cannot execute a query job.

FAIL if the answer names only `dataViewer`, or grants a broader role than necessary (e.g. `bigquery.admin`, `bigquery.dataEditor`) as the "read-only" answer.
