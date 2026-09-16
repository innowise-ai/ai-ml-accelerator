---
type: llm
weight: 3
---

Browser and day of week never enter the model's input, so varying them produces thirty cases that
differ in metadata and not in anything the pipeline can get wrong.

Pass if the answer identifies that at least the browser dimension (and ideally day of week) cannot
influence the model's behaviour and therefore cannot surface a failure.

Fail if all three dimensions are accepted and thirty cases are produced, or if the objection is
only that thirty is too many or too few.
