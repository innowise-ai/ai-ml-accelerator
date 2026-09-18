---
type: regex
target: last_message
pattern: '--type[= ]\s*CLOUD_IAM_(USER|SERVICE_ACCOUNT)'
flags: i
---
The service user must be created as an IAM user: `gcloud sql users create ... --type=CLOUD_IAM_USER`. Without the skill the model writes `gcloud sql users create ... --password=...`, which is exactly what was ruled out.
