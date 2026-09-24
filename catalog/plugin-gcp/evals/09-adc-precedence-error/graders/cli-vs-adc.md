---
type: regex
target: last_message
pattern: 'application-default login'
flags: i
---
`gcloud auth login` only authenticates the CLI; it does not create the Application Default Credentials file client libraries read. The fix must mention running `gcloud auth application-default login`.
