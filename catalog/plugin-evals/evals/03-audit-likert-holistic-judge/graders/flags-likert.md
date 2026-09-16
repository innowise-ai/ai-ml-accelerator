---
type: llm
weight: 2
---

`evals/judge_prompt.txt` asks for a 1-5 rating. Ordinal scales cannot be calibrated: annotators
disagree on the boundary between a 3 and a 4 and the judge inherits that noise.

Pass if the answer flags the 1-5 scale as a problem AND recommends a binary pass/fail decision
instead (or explicitly defines a threshold that converts the scale into a binary decision with a
stated cut-off).

Fail if the scale is not mentioned, is treated as acceptable, or the only advice is to describe the
1-5 anchors more precisely.
