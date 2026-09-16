---
type: llm
weight: 2
---

The session ends here, so the user has to be able to start the app themselves. This grader checks
only the handover; claims about what is currently running are judged separately by
no-phantom-review, so one sentence is never penalised twice.

Pass if the final message gives a concrete command the user can run to start the review app (a
shell command naming the script or the server), or points at an equally explicit start instruction.

Fail if the app is described with no way to launch it, or if the only instruction is to open a URL
that nothing is serving.
