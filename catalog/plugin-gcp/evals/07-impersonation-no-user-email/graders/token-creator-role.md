---
type: regex
target: last_message
pattern: 'roles/iam\.serviceAccountTokenCreator|Service Account Token Creator'
flags: i
---
The permission error on impersonation is almost always the caller lacking `roles/iam.serviceAccountTokenCreator` ON the target service account. This is the "what am I missing" half of the question and the single most common impersonation failure.
