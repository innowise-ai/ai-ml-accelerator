---
type: llm
focus: last_message
---
PASS if the answer also checks that the project/resource identifier being called matches the one the role was actually granted on, and that the relevant API is enabled in that project.

FAIL if the answer never considers a project/resource mismatch as a possible cause.
