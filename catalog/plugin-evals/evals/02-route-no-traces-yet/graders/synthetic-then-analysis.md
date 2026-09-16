---
type: llm
weight: 3
---

With no traces, the only way to get material for error analysis is to manufacture inputs and run
them through the pipeline. The order matters: generate inputs, run them, then analyse the traces.

Pass if the answer proposes generating synthetic test inputs (or otherwise manufacturing traffic)
as an early step, AND explicitly places error analysis on the resulting traces after it. Both
elements must be present and the order must be that way round.

Fail if error analysis is never mentioned, if evaluators are built directly from the synthetic
inputs with no trace review in between, or if the answer says to wait for real users before doing
anything.
