---
runs: 1
max_turns: 8
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
tags: [gcp, auth, adc]
---
I ran `gcloud auth login` and it printed "You are now logged in". My Python app still throws `google.auth.exceptions.DefaultCredentialsError: Could not automatically determine credentials`. I also have an old `GOOGLE_APPLICATION_CREDENTIALS` environment variable set from a previous project, pointing at a key file that no longer exists on disk. Walk me through why this is failing and how to fix it so it doesn't happen again.
