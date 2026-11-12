---
type: llm
focus: last_message
weight: 1
---
The user gave a fairly complete spec (FastAPI, Postgres, three endpoints, Docker Compose) and said "Implement this." Score PASS only if ALL hold:
(a) The reply restates the shape of the request in its own words — it mentions FastAPI or Postgres AND refers to the endpoints/behaviour (create, redirect, stats).
(b) It does NOT re-ask anything the spec already decided (framework, database, endpoint list, code length, redirect status).
(c) It ends with EITHER exactly one question about something the spec leaves open that would change the build (e.g. who may create links / auth, expiry, duplicate URLs, custom aliases, abuse) OR a short design (a few lines) plus an explicit request for approval. Either ending is acceptable.
(d) It does not contain the implementation (no route handlers, models, migrations, or Dockerfile/compose content).
