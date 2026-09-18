---
type: llm
focus: last_message
---
PASS if the first diagnostic step is confirming which identity the code is actually authenticated as (e.g. via the tokeninfo endpoint, `google.auth.default()`, or the metadata server), before assuming the role grants themselves are wrong.

FAIL if the answer jumps straight to "grant more roles" without first confirming the calling identity.
