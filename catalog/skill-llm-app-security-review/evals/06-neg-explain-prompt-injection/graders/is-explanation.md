---
type: llm
focus: last_message
---
Check each claim:
1. The answer is a short explanation of about two paragraphs (no more than roughly 250 words of body text).
2. It explains that prompt injection is untrusted text being treated by a model as instructions, and mentions indirect injection (instructions hidden in documents, web pages, tool results or similar) or gives a concrete example.
3. It is not formatted as a security review report: no verdict, no severity-labelled findings, no review of code that was never provided.
PASS only if all three hold.
