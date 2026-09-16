---
type: llm
weight: 2
---

The fixture's judge bundles tone, accuracy, completeness and customer satisfaction into one
"helpfulness" verdict. A verdict like that cannot be acted on: it does not say what broke.

Pass if the answer flags that the judge evaluates several dimensions at once / is holistic / is not
tied to one specific failure mode, AND recommends splitting it into separate judges, one per
failure mode.

Fail if the holistic framing is not raised, or if the recommendation is merely to add more detail
to the single rubric while keeping one combined verdict.
