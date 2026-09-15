---
type: regex
target: last_message
pattern: 'trigger\s*=\s*[\(\[\{]\s*[''"]tokens[''"]\s*[,:]\s*4_?000'
flags: i
---
In the current documentation the summarization threshold is set by the `trigger=("tokens", 4000)` parameter; the old `max_tokens_before_summary=` is marked deprecated.
