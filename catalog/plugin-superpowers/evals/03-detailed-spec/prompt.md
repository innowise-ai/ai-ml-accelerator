---
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
runs: 3
---
Here's the spec for our internal URL shortener:

- FastAPI service, Postgres for storage.
- `POST /links` takes `{"url": "..."}` and returns a 7-character base62 short code.
- `GET /{code}` 302-redirects to the original URL; 404 if the code is unknown.
- `GET /links/{code}/stats` returns the click count and `created_at`.
- It runs in our existing Docker Compose setup.

Implement this.
