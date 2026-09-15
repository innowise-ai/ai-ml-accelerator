---
url: https://github.com/anthropics/skills/tree/main/skills/docx
title: "Word documents: creating and editing"
verdict: task
rating: 5
security: 5
economy: +1%
---
## Summary
When you need to fix up a .docx (touch up a CV, produce a solid report with tables)

## Examples
- "Make the edits to the contract as tracked changes" => the edit is easy to insert without `<w:ins>`/`<w:del>`, and in accepted view it is invisible; `validate.py --original doc.docx --author "<name>"` shows every untracked one
- "Add langchain to my stack at my last job" => Without the skill everything would shift and you would have to fix it by hand

## Notes
For .docx there are no alternatives, install for the duration of work with documents
security: 5 - official Anthropic plugin