---
url: https://github.com/anthropics/skills/tree/main/skills/claude-api
title: "Claude API: models, SDK, migrations"
verdict: stack
rating: 5
security: 4.5
economy: +3%
---
## Summary
When the project calls the Claude API: current model ids and prices, adaptive thinking, caching, tool use, model migrations. Pays off in any code on the Anthropic SDK

## Examples
- "A script on the Anthropic SDK: Opus 5 with server-side web search, no more than 3 searches" => without it, from memory puts the outdated `web_search_20250305`; with it, the current `web_search_20260209`, `claude-opus-5`, `max_uses: 3` — the code runs as is
- With the skill it picks a more current model (not sonnet-3.5; it fairly puts the latest sonnet-5)

## Notes
The most expensive to activate: SKILL.md ≈ 22k tokens on every activation, so only into projects that really write code on the Anthropic SDK
security: 4.5 - official Anthropic plugin, but it can go to the network and take credential tokens; 
