---
type: llm
weight: 3
---

The user asked a specific, answerable question about public benchmarks.

Pass if the answer gives concrete guidance on running MMLU and HumanEval: how to execute them (a
harness or equivalent), what to hold constant across the two models (prompt format, shot count,
decoding settings), and what to report (for example pass@k for HumanEval, accuracy for MMLU, with
some acknowledgement of run-to-run variance).

Fail if the answer redirects to building product-specific evals instead of answering, or stays so
general that the user could not start the run.
