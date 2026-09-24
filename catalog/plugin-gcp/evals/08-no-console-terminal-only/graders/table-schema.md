---
type: regex
target: last_message
pattern: 'bq\s+show[^\n]*--schema|bq\s+show\s+[^\n]*\.[^\n]*'
flags: i
---
Reading a table's schema from the shell is `bq show --schema dataset.table` (or `bq show` on the table).
