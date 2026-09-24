---
type: regex
target: last_message
pattern: 'enable_change_history\s*=\s*TRUE'
flags: i
---
`CHANGES` only works once the table option is switched on: `ALTER TABLE ... SET OPTIONS (enable_change_history = TRUE)`. This is the "what do I have to turn on beforehand" half of the question and is easy to miss from memory.
