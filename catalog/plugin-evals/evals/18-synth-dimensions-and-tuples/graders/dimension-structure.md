---
type: llm
weight: 3
---

Unstructured generation produces generic, repetitive, happy-path examples. The structure is: named
axes of variation, each with an enumerated set of values.

Pass if the answer defines named dimensions (however labelled — axes, factors, variables) each with
an explicit list of possible values, and builds the test inputs from combinations of them. Around
three dimensions is the expected starting point; more is acceptable if justified.

Fail if the answer is a flat list of example queries with no stated axes behind it, or if
"dimensions" are named but never given value sets or combined.
