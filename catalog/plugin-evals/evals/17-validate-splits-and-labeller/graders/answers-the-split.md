---
type: llm
weight: 2
---

The question asked still deserves an answer.

Pass if the answer gives a concrete three-way split: a small training slice as the source of
few-shot examples, a dev portion for iteration, and a held-out test portion for the final
measurement, with the training slice clearly the smallest of the three.

Fail if only two splits are described, if no proportions or relative sizes are given, or if the
split question is displaced entirely by the labelling critique.
