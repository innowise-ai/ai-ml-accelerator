---
type: regex
target: last_message
pattern: 'cloudsql\.iam_authentication\s*=\s*on'
flags: i
---
"No database passwords" requires IAM database authentication, which is off by default and has to be switched on at create time with `--database-flags=cloudsql.iam_authentication=on`.
