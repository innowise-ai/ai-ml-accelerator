---
type: llm
weight: 3
---

Building evaluators before failure modes are known is the single named prohibition for this state.

Pass if no evaluator, LLM judge, scorer, metric suite, golden dataset or dashboard is scheduled
before the trace review is complete. Listing them as later steps that depend on the review's output
is correct and passes.

Fail if any of those is placed first or second, or is scheduled to run in parallel with the review
"to save time".
