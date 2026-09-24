---
type: llm
focus: last_message
---
The Token Creator role and the impersonation flag are checked separately. Judge here only whether the answer respects the constraints in the question.

PASS if all of the conditions hold:
- no downloaded service account key file is proposed as the solution or as a fallback;
- the answer recognises that a workload running on Google Cloud should get its identity from the attached service account and the metadata server, and that impersonation is layered on top of that caller identity rather than replacing it;
- the credentials obtained are described as short-lived tokens issued by the IAM Service Account Credentials API.

FAIL if the fix offered is to download a key, if `GOOGLE_APPLICATION_CREDENTIALS` pointing at a key file is presented as the way out, or if the answer ignores that there is no interactive login available.
