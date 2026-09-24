---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, bigquery, streaming]
---
As rows land in a BigQuery table I want BigQuery itself to transform them and push them onto a Pub/Sub topic continuously — not a scheduled query every five minutes, and I would rather not stand up a Dataflow job. Show me what the SQL looks like, and tell me what has to be in place for this to keep running in production for months rather than dying on us.
