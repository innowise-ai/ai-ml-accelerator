---
type: llm
weight: 3
---

Presence of a fixed-format token is decidable by string matching. An LLM judge for it is strictly
worse: nondeterministic, paid per call, and capable of being wrong about something exact.

Pass if the answer's primary recommendation is a deterministic code-based check (regex, pattern
match, parser, assertion) rather than an LLM judge, and it gives at least one reason why code is
the right tool here.

Fail if an LLM judge is the primary deliverable, even a good one, or if the code check is offered
only as an afterthought to a judge that was written anyway.
