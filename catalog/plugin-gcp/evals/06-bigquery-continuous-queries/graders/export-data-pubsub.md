---
type: regex
target: last_message
pattern: 'EXPORT\s+DATA'
flags: i
---
A continuous query exports to Pub/Sub with an `EXPORT DATA OPTIONS (format = 'CLOUD_PUBSUB', uri = ...)` statement.
