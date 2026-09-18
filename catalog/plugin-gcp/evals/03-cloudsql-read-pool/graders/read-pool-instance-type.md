---
type: regex
target: last_message
pattern: '--instance-type[= ]\s*READ_POOL_INSTANCE'
flags: i
---
A load-balanced group of read nodes is a read pool, created with `--instance-type=READ_POOL_INSTANCE`. From memory the model offers ordinary read replicas, which are individual single-node instances and are exactly what was ruled out.
