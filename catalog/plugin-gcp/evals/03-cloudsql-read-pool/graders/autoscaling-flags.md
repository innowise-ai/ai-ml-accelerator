---
type: regex
target: last_message
pattern: '--auto-scale-(min|max)-node-count'
flags: i
---
"Grows and shrinks by itself" is read pool autoscaling, configured with `--auto-scale-min-node-count` / `--auto-scale-max-node-count`. A fixed `--node-count` alone does not answer the request.
