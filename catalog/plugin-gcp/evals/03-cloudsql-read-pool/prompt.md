---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, cloud-sql, gcloud]
---
We have a PostgreSQL primary on Cloud SQL and the read traffic from our dashboards spikes unpredictably through the day. I want one load-balanced group of read nodes that grows and shrinks on CPU by itself — not a pile of individual read replicas I have to add and remove by hand. Give me the `gcloud` command to create it, and tell me what edition this needs and what the node limits are.
