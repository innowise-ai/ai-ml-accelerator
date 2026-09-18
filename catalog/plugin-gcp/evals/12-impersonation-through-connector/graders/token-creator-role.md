---
type: regex
target: last_message
pattern: 'serviceAccountTokenCreator'
flags: i
---
The impersonating principal still needs `roles/iam.serviceAccountTokenCreator` on the target service account regardless of which layer performs the impersonation.
