---
type: llm
focus: last_message
---
PASS if the answer explains that CLI-level impersonation (`gcloud config set auth/impersonate_service_account` or `--impersonate-service-account`) does not automatically propagate into a library that builds its own credentials, and that the fix is to explicitly construct an impersonated-credentials object from the base ADC and pass it into the connector's credentials parameter.

FAIL if the answer only tells the user to set the CLI impersonation flag/config and stops there, without addressing that the connector needs the credentials object passed in explicitly.
