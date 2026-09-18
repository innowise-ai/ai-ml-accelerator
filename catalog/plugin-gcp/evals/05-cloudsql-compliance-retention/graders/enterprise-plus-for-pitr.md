---
type: regex
target: last_message
pattern: 'ENTERPRISE_PLUS|Enterprise[ _-]Plus'
flags: i
---
30 days of PITR rules out the Enterprise edition, whose PITR log retention tops out at 7 days; only Enterprise Plus reaches 35 days. The create command therefore needs `--edition=ENTERPRISE_PLUS`, and getting this wrong means provisioning an instance that cannot meet the requirement.
