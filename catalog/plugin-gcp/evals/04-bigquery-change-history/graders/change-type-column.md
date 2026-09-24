---
type: regex
target: last_message
pattern: '_CHANGE_TYPE'
---
The pseudo-column `_CHANGE_TYPE` (INSERT / UPDATE / DELETE) is how the consumer tells the change kinds apart; without it the result cannot drive an incremental replica.
