---
type: llm
weight: 1
---

Unstructured generation ("ask an LLM for 50 test queries") produces repetitive happy-path inputs.
The plugin's method is dimension-based: named axes of variation, combined into tuples, each tuple
turned into a query.

Pass if the answer describes generating the test inputs along explicit named dimensions / axes of
variation / structured combinations, rather than simply prompting a model for a list of example
queries.

Fail if the synthetic-data step is described only as "have the LLM write some representative
queries" with no structure.
