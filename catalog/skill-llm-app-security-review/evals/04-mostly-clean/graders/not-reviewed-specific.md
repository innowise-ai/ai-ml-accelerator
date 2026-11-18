---
type: llm
focus: last_message
---
Check: the answer has a section or list of things it could not judge from the code, and it names at least two specific items tied to this code, such as: the `confirm()` implementation; whether `TOOL_IMPL` functions scope data to `user`; what `ARG_SCHEMAS` actually validate; how `store` isolates tenants or what is ingested into it; the `TOOL_DEFS` contents; rate limiting or deployment.
PASS if at least two specific items are named. FAIL if the list is missing or only generic ("other parts of the system").
