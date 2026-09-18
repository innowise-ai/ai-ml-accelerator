---
type: regex
target: last_message
pattern: 'workload\s+identity\s+federation'
flags: i
---
For code running outside Google Cloud the recommended mechanism is Workload Identity Federation: the external token (here an AWS IAM role) is exchanged for a short-lived Google Cloud access token.
