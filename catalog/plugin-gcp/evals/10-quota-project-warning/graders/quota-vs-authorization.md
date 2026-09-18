---
type: llm
focus: last_message
---
PASS if the answer explains a quota project is the project billed and rate-limited for API usage, and distinguishes it from the project that owns the resource being accessed or from IAM authorization on that resource.

FAIL if the answer conflates the quota project with IAM permissions, or claims it controls what the caller is allowed to do rather than who is billed/metered for usage.
