---
type: regex
target: last_message
pattern: 'bigquery\.jobUser'
flags: i
---
`roles/bigquery.jobUser` is the commonly missed half of read-only access — without it, `dataViewer` alone cannot run a query job.
