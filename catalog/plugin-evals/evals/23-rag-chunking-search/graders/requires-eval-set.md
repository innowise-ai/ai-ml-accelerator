---
type: llm
weight: 2
---

A sweep needs something to score against: queries paired with the chunks that actually answer them.

Pass if the answer states that a retrieval evaluation set (queries with known relevant chunks) is
needed for the comparison, or explains how to build one if it does not exist.

Fail if the sweep is described with no mention of what the configurations are scored against.
