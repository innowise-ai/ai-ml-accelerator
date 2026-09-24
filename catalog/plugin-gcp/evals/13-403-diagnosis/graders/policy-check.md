---
type: regex
target: last_message
pattern: 'get-iam-policy|testIamPermissions'
flags: i
---
Checking the actual allow policy on the resource (`gcloud <service> get-iam-policy` or the `testIamPermissions` API) is how you tell a missing role apart from a wrong-identity or wrong-resource problem.
