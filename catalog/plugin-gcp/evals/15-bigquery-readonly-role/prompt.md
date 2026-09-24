---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, bigquery, iam]
---
I need to grant a service account read-only query access to BigQuery — it should be able to run SELECT queries but have no write, delete, or admin rights anywhere. Which role or roles do I actually need to grant?
