---
type: llm
weight: 3
---

MMLU and HumanEval have fixed ground truth. Error analysis over traces, failure-mode taxonomies and
LLM-judge calibration are machinery for evaluating a product with no ground truth, and none of it
applies here.

Pass if the answer does not prescribe error analysis on traces, building a failure-mode taxonomy,
writing an LLM-as-judge, or judge validation with TPR/TNR as part of this task. A brief closing note
that product-specific evals are a different exercise, if the user later needs them, does not fail
this grader.

Fail if any of that methodology is presented as a step in the benchmark work.
