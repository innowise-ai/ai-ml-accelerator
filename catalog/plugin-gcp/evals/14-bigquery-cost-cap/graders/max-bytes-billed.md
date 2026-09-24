---
type: regex
target: last_message
pattern: 'maximum_bytes_billed|maximumBytesBilled'
flags: i
---
`maximum_bytes_billed` (or the `--maximum_bytes_billed` `bq` flag) makes the query fail rather than run past a set byte threshold — this is the actual hard cap, distinct from just estimating cost with a dry run.
