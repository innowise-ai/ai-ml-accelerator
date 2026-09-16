---
type: llm
weight: 2
---

The purpose of this pass is finding out what kinds of failure exist, not how often each occurs.
Sampling for frequency estimation at this stage gives a batch of near-duplicates.

Pass if the answer states that the goal is discovering distinct failure modes / maximising coverage
and diversity, explicitly not estimating how common any failure is.

Fail if the sample is justified as representative of the population, or as a basis for measuring
failure rates.
