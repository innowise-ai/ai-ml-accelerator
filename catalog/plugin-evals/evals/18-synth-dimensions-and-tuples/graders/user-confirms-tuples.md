---
type: llm
weight: 3
---

The user knows which combinations occur in their business and which are fiction. That check happens
on the tuples, before effort goes into writing queries.

Pass if the answer presents the combinations to the user for review/confirmation before generating
the final queries, and says why the user's judgement is needed at that point.

Fail if queries are produced in one pass with no checkpoint, or if the only invitation is a closing
"let me know if you want changes" after everything is already written.
