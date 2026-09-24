---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, auth, iam, troubleshooting]
---
I'm getting a 403 PERMISSION_DENIED calling a Google Cloud API from my service. Before I start granting more IAM roles and hoping it goes away, how do I systematically figure out whether the problem is the wrong identity, a missing role, or the wrong project/resource?
