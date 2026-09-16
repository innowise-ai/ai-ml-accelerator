---
type: llm
weight: 3
---

`judge_prompt.md` quotes examples labelled t000-t003. `evaluate.py` scores the judge over every row
of `labeled.csv`, which contains those same four ids. The judge is being graded partly on examples
it was handed the answers to.

Pass if the answer identifies this overlap specifically — that the few-shot examples in the prompt
also appear in the data the judge is measured on — and states that it inflates the alignment score.

Fail if leakage is not raised at all, or if it is mentioned only as a generic caution ("watch out
for leakage in general") without connecting it to these files.
