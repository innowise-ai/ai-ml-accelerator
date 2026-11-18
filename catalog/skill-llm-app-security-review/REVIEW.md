---
url: https://github.com/innowise-ai/ai-ml-accelerator/tree/main/lib/skills/llm-app-security-review
title: "LLM app security review"
verdict: task
rating: 3
security: 5
---
## Summary
For the moment you review or ship an LLM feature (RAG, tool calling, agents): the base model already finds the main holes, the skill adds a strict report with the vulnerable line quoted, a severity per finding and a list of what the code does not show. Worth it as a review template, not as a better detector

## Examples
- "Review this support bot before we ship it" (model output goes straight into `db.execute`, key and password hardcoded) => without it, finds the same flaws (SQL execution, hardcoded key and password, injection) in free format, rewrites the whole function and ends with an offer to draft more instead of listing what it did not review (2 of 3 runs); with it, quotes the offending lines, rates each finding and lists what was not reviewed
- "Threat-model this multi-tenant Q&A endpoint" (tenant check runs only on the sources list, after generation) => both arms catch the late filter; the base answers quote the filter line in 2 of 3 runs, with the skill all 3 runs do, in the fixed report format
- Triage agent where customer ticket text can drive `refundOrder` and `deleteUser` => both find the chain; with the skill it is rated Critical, but its "Checked, no issue" line for LLM09 says staff review the output, while the loop runs every tool call at once
- "Review this Express login handler for SQL injection" and "explain prompt injection" => the skill stays silent, as it should

## Notes
Eval: 6 cases x 3 runs, Sonnet as the agent, Opus as the judge, $5.65 for the whole run. With the skill 0.94 against 0.82 without it, mean uplift +0.12: +0.28, +0.17, +0.24 and +0.04 on the four review cases, 0 on the two negative ones. The uplift comes from format, quoted evidence and the "Not reviewed" list, not from finding more flaws
Weak spots: the rule to dismiss every unflagged category in one line makes it write reassuring sentences about controls the code does not show (case 02, LLM09: the judge flagged 3 of 3 runs, 2 of them fairly); walking all ten categories also pulls in speculative findings on code it cannot see. A possible fix is to list only categories verified from visible code and move the rest to "Not reviewed"
no-invented was the strictest grader: it failed the with-skill runs in case 02 (3 of 3), 03 (1 of 3) and 04 (2 of 3). Some of those are real slips, like the reassuring LLM09 line in 02, others look borderline. Only the judge votes were stored, not its reasoning, so per-case numbers are indicative
SKILL.md is about 4.3 KB (roughly 1.1k tokens per activation), no scripts, no network
