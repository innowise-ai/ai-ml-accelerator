---
url: https://github.com/anthropics/skills/tree/main/skills/skill-creator
title: Creating and evaluating Agent Skills
verdict: task
rating: 4
security: 3
economy: +31%
---
## Summary
When you write or edit an Agent Skill: interview, draft, running evals with subagents, picking a description.

## Examples
- "Make a skill for X" => first four questions (what it can do, which phrases trigger it, output format, are tests needed), then a draft and test prompts, instead of a SKILL.md by guesswork
- The skill does not trigger on the right requests => `scripts/run_loop.py` splits the requests 60/40 into train and held-out, runs each 3 times, edits the description for up to 5 iterations and returns `best_description` by held-out

## Notes
The most expensive activation among the "For a task" ones: +31% per session, the description tuning loop is 20 requests × 3 runs × up to 5 iterations.
The scripts write to ~/.claude/commands and /tmp.
