---
type: llm
weight: 3
---

Placing the critique first forces the judge to articulate its assessment before committing to a
decision. Emitting the verdict first lets it decide and then rationalise.

Pass if the judge's required output puts a free-text critique / reasoning / justification field
BEFORE the verdict field — in the JSON schema key order, in the stated output template, or in an
explicit instruction to write the critique first.

Fail if the verdict comes first, if the two are unordered, or if no critique is required at all.
