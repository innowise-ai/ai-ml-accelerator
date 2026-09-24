---
type: llm
focus: last_message
---
PASS if the answer states a concrete consequence of ignoring the warning, such as API calls failing with a quota-project-not-set error, or usage being billed/rate-limited against an unintended or absent project.

FAIL if the answer says nothing will break, or is vague ("might cause issues") with no concrete failure mode named.
