---
type: regex
target: last_message
pattern: 'retention lock|immutab|air[- ]gapped'
flags: i
---
"Not deletable by a compromised administrator" is retention lock plus air-gapped immutable vaults held in a separate project — not merely a longer retention number.
