---
type: llm
focus: last_message
---
Check: the answer identifies that `customer_name` and/or the retrieved `docs` text is concatenated straight into the prompt, and gives a concrete attack that names the input and what the attacker gets (for example, a document or customer name containing instructions that make the model reveal the password, or reply with "SQL: ..." so that the query runs on prod.db).
PASS if both the injected input and a concrete outcome are named. FAIL if prompt injection is mentioned only generically ("an attacker could inject malicious input") without naming the input and the consequence.
