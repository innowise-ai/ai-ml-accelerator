---
type: llm
weight: 3
---

Faithfulness asks whether the answer is supported by what was retrieved, not whether it is true.
A model that answers from memory happens to be right this time and will be wrong the next, with no
way to tell the cases apart.

Pass if the answer says the eval made the wrong call, and that ungrounded content counts as a
hallucination in a RAG setting even when the fact is correct.

Fail if the pass is endorsed because the answer was factually right, or if the distinction between
correctness and grounding is never drawn.
