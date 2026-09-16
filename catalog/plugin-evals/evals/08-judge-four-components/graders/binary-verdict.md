---
type: llm
weight: 3
---

Ordinal outputs cannot be calibrated against human labels, so the verdict has to be binary.

Pass if the judge prompt's output is a two-valued verdict (Pass/Fail, or an equivalent pair such as
true/false or violation/no-violation) with both values explicitly defined.

Fail if the prompt asks for a 1-5 or 1-10 rating, a letter grade, a percentage, a confidence score
used as the verdict, or any scale the user would have to threshold themselves.
