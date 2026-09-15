---
type: regex
target: last_message
pattern: 'keep\s*=\s*\(\s*[''"]messages[''"]\s*,\s*20\s*\)'
flags: i
---
How many of the last messages to keep is set by the `keep=("messages", 20)` parameter; the old `messages_to_keep=` is marked deprecated.
