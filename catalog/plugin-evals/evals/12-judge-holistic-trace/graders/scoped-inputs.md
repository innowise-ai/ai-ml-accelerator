---
type: llm
weight: 2
---

Each judge gets what its decision needs and no more: the retrieval check needs the query and the
retrieved articles, the tool-call check needs the conversation plus the call and its result, the
reply check needs the retrieved policy and the reply.

Pass if the answer assigns different, narrower inputs to at least two of its judges rather than
handing every judge the full trace.

Fail if all judges are fed the whole trace, or if what goes into each is never addressed.
