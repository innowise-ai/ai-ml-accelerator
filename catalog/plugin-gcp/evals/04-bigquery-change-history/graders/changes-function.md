---
type: regex
target: last_message
pattern: 'CHANGES\s*\(\s*TABLE'
flags: i
---
Updates and deletes require the `CHANGES` table-valued function — `CHANGES(TABLE `dataset.table`, start, end)`. `APPENDS` returns appended rows only and would silently miss the updates and deletes the question asks for.
