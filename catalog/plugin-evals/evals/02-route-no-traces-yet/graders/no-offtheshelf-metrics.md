---
type: llm
weight: 2
---

Generic academic metrics are the standard wrong answer for a pre-launch team: they produce a number
without ever defining what failure means for this product.

Pass if the answer does not propose ROUGE, BLEU, BERTScore, embedding/cosine similarity, perplexity,
or a generic "hallucination / toxicity / coherence score" as the evaluation approach. Naming one to
explain why it is a poor fit is fine and does not fail this grader.

Fail if any of them is recommended as a metric to adopt, including as a "quick baseline while we
wait for real data".
