---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, cloud-sql, backups, compliance]
---
I am provisioning a new Cloud SQL for PostgreSQL instance in us-central1 for a regulated workload. Compliance has given us three requirements:

- point-in-time recovery going back 30 days;
- backups kept for three years, and immutable — nobody may delete or alter them before that, including an administrator whose account has been compromised;
- those backups restorable into a separate project.

Give me the `gcloud sql instances create` command, and explain how the three-year immutable requirement is actually met — I don't believe instance-level automated backups can do it. What are the retention ceilings I'm working against?
