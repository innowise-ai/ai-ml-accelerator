---
type: regex
target: last_message
pattern: 'get-iam-policy'
flags: i
---
Finding your own roles without the permissions page means reading the project allow policy: `gcloud projects get-iam-policy PROJECT_ID`, usually flattened and filtered down to your own principal.
