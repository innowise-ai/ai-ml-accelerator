---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, bigquery, cost]
---
I'm about to run a query against a multi-terabyte BigQuery table and I'm not confident about the cost. How do I find out how many bytes it will actually process before running it, and how do I put a hard cap in place so a mistake can't blow the budget?
