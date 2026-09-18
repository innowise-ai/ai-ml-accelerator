---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, auth, iam]
---
We run a nightly batch job on an AWS EC2 instance. It needs to read objects from a Google Cloud Storage bucket and append rows to BigQuery. How should that job authenticate to Google Cloud? Explain the mechanism and what has to be set up on the Google Cloud side. And tell me straight: should we be downloading a service account key JSON and shipping it with the job?
