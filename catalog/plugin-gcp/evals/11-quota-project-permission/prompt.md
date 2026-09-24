---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, auth, iam, quota-project]
---
Before `gcloud auth application-default set-quota-project` will actually succeed, what IAM permission or role does my own user account need on the target project?
