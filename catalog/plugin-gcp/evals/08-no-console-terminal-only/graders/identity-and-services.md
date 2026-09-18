---
type: regex
target: last_message
pattern: 'gcloud\s+auth\s+list|gcloud\s+config\s+(list|get-value)'
flags: i
---
Steps 1 and 2 are `gcloud auth list` / `gcloud config list` for the active identity and project, and `gcloud services list --enabled` for the API.
