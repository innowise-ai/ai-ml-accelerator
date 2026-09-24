---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, bigquery, sql]
---
We keep a replica of one BigQuery table in an external system. Right now we copy the whole table every night, which has got expensive. I need to pull only what changed in a time window — and it has to include updates and deletes, not just new rows. What does BigQuery offer for this, what do I have to turn on beforehand, and what does the query look like?
