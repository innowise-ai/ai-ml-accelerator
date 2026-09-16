---
type: llm
weight: 2
---

A judge prompt needs four parts: the task and criterion, explicit Pass and Fail definitions,
labelled few-shot examples, and an enforced output format.

Pass if all four are present: (a) a statement of what this judge evaluates, (b) separate written
definitions of what counts as Pass and what counts as Fail, (c) at least two concrete labelled
examples with their verdicts, (d) a specified output structure.

Fail if any one of the four is missing — most commonly the few-shot examples, or Pass/Fail
definitions collapsed into a single sentence of criteria.
