---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, cloud-sql, gcloud]
---
I am standing up a new PostgreSQL instance on Cloud SQL in us-central1 for a production service. Give me the `gcloud sql instances create` command, and then the command that creates the database user the service will authenticate as. Constraints: we do not want to manage database passwords at all, every connection must be encrypted, and we need to be able to restore to an arbitrary point in time. Show the exact flags.
