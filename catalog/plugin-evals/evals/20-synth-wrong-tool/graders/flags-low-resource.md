---
type: llm
weight: 3
---

Synthetic generation degrades in languages and dialects that are thinly represented in training
data: the output is grammatical but does not sound like the users it is meant to imitate.

Pass if the answer warns that model-generated Belarusian is likely to be unrepresentative of real
user language, and treats that as a reason not to build the eval set this way.

Fail if 100 queries are produced with no such warning, or if the language is treated as an
incidental translation detail.
