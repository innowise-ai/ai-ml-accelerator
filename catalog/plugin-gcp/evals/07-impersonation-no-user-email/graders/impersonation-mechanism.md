---
type: regex
target: last_message
pattern: '--impersonate-service-account|auth/impersonate_service_account'
flags: i
---
Impersonation is configured with `--impersonate-service-account=` (or `gcloud config set auth/impersonate_service_account`), not by pointing GOOGLE_APPLICATION_CREDENTIALS at a key file.
