---
type: llm
focus: last_message
---
Check: the answer identifies that `/upload` extracts and indexes user-uploaded files with no review or sanitization, and that this lets an attacker plant instructions or false content that later reaches the prompt (indirect prompt injection and/or data poisoning), ideally noting that with the shared index this affects other tenants.
PASS if the upload path is named as an injection or poisoning source. FAIL if uploads are not discussed as an attack path.
