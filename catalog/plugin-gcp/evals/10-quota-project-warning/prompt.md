---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, auth, adc, quota-project]
---
When I run `gcloud auth application-default login`, gcloud prints a warning that it could not automatically determine a quota project and that some APIs may not work. What is a quota project, why couldn't gcloud set one for me, and what actually breaks in my application if I just ignore the warning?
