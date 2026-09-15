---
type: llm
focus: last_message
---
PASS if the current helper is named, the import from `ai` is shown and the call is inside `stopWhen`.

FAIL if the helper is named from memory (`stepCountIs` from the old version), or the answer comes with the caveat "could not check the documentation".
