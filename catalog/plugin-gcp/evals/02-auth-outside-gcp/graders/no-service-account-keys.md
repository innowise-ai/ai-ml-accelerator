---
type: llm
focus: last_message
---
The question ends with a direct ask: should we download a service account key JSON and ship it with the job?

PASS if the answer says no — downloaded service account keys are long-lived credentials to be avoided here — and points at federated, short-lived credentials instead.

FAIL if a downloaded key file is presented as the recommended or the simplest acceptable approach, if the answer's main walkthrough is `gcloud iam service-accounts keys create` plus `GOOGLE_APPLICATION_CREDENTIALS` pointing at that file, or if the answer dodges the question.
