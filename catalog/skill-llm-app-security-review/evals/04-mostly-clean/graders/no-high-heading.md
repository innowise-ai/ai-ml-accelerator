---
type: regex
target: last_message
match: not_contains
flags: im
weight: 0.5
---
^#{2,4}[^\n]*\b(critical|high)\b
