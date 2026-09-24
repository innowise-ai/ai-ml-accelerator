---
runs: 1
max_turns: 10
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, bigquery, cli, gcloud]
---
I have no access to the Cloud Console at all — I work over SSH on a locked-down jump host, there is no browser, and my role does not render the BigQuery UI anyway. Everything has to happen in the shell.

Walk me through it, entirely with commands:
1. confirm which identity and which project I am actually operating as;
2. check whether the BigQuery API is enabled on that project;
3. list the datasets, then read the schema of one table;
4. find out how many bytes a query would scan **before** I run it — I am not allowed to run an expensive query by accident;
5. see which IAM roles I actually hold on the project, since I cannot look at the permissions page.

Do not tell me to open the Console for any step.
