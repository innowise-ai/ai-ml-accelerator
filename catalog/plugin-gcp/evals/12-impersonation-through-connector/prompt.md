---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, auth, impersonation, cloud-sql]
---
Our developers authenticate as themselves and impersonate a service account for everything — no downloaded keys. Now I need the Cloud SQL Python Connector to connect as that impersonated service account instead of my own user identity, and the connector fetches its own credentials internally rather than taking a token I hand it manually. How do I actually make impersonation apply to a library that manages its own credential fetching, rather than just setting `--impersonate-service-account` on the CLI?
