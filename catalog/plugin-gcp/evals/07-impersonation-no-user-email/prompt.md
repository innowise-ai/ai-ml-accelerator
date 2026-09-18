---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, auth, iam, impersonation]
---
Our Python batch job has to run as a service account, `batch-runner@my-project.iam.gserviceaccount.com`. It runs in a container on a jump host inside Google Cloud, so there is no interactive browser login, and the security team has forbidden downloading service account key files. There is no human user email we can attach roles to for this workload.

I set the impersonation up and the client library now fails with a permission error when it tries to get a token for the service account. What is the correct way to do this, and what am I most likely missing?
