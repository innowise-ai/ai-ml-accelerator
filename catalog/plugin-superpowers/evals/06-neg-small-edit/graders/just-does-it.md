---
type: llm
focus: last_message
weight: 1
---
The user asked for a mechanical rename of `calc_total` to `compute_order_total` in a pasted snippet with one definition and three call sites (in checkout, preview, refund_amount). Score PASS only if ALL hold:
(a) The reply returns the updated code with the definition AND all three call sites renamed, and no remaining `calc_total(` call in the code.
(b) It does not ask the user a clarifying question before or instead of doing the rename.
(c) It does not talk about approaches, designs, specs, plans, or "before we start" — the task is clear and small.
(d) Any offer of further help comes after the code, not in place of it.
