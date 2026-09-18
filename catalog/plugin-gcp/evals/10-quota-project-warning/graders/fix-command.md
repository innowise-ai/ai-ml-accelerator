---
type: regex
target: last_message
pattern: 'application-default set-quota-project'
flags: i
---
The direct fix is `gcloud auth application-default set-quota-project <PROJECT_ID>`.
