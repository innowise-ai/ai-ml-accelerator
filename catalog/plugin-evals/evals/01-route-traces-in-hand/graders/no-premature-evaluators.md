---
type: llm
weight: 2
---

Building evaluators before error analysis is the failure this plugin exists to prevent. Evaluators
written first measure generic qualities ("helpfulness", "coherence") instead of real failure modes.

Pass if the answer does not instruct the user to build an LLM judge, a scorer, a metric suite, a
regression test set, or a metrics dashboard before the trace review has happened. Mentioning that
these come *later*, after failure modes are known, is fine and does not fail this grader.

Fail if any of those artifacts is presented as something to build now, in parallel, or as step one
or two of the plan.
