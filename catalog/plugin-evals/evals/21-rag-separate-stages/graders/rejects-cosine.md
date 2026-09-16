---
type: llm
weight: 2
---

Cosine similarity between an answer and a reference measures wording overlap. An answer can be
close to the reference and wrong, or far from it and right.

Pass if the answer states that cosine similarity (or embedding distance / ROUGE / BERTScore) is not
a valid measure of generation quality here, and points to binary evaluators grounded in observed
failure modes instead.

Fail if cosine similarity is retained in any primary role, or is replaced by another surface
similarity metric.
