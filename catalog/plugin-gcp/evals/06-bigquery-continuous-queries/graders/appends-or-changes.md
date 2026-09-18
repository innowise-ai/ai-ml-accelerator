---
type: regex
target: last_message
pattern: '(APPENDS|CHANGES)\s*\(\s*TABLE'
flags: i
---
A continuous query must name the earliest data to process through `APPENDS` (or `CHANGES`) in the FROM clause — this is what makes the query unbounded rather than a one-shot scan.
