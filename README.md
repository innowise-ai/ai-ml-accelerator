# ai-context-builder

A catalog of vetted context for Claude Code (later for Codex too). Four kinds: skills, MCP servers, hooks, agents, plus bundles of them — plugins. Everything lives in `lib/`. In `catalog/` — reviews: `REVIEW.md` (a human review with notes) and `evals/` (cases that check this skill, MCP or bundle).

To install, it is enough to open `ui/index.html`: a table with verdict, rating, security, token cost and eval result; you tick the entries and get the install commands and the text for the agent window.

## Run

```bash
# Prompt for the agent:
Clone https://github.com/innowise-ai/ai-ml-accelerator, run the commands from the Readme "##Run" below

# Or by hand:
git clone https://github.com/innowise-ai/ai-ml-accelerator && cd ai-ml-accelerator
python3 ui/build.py && open ui/index.html        # catalog: tick entries → install commands

# Install without the catalog:
claude plugin marketplace add innowise-ai/ai-ml-accelerator
claude plugin install <name>@acb
```

## Layout

```
lib/                              library — added by a human
  skills/<name>/SKILL.md
  agents/<name>.md
  mcp/<name>.json
  hooks/<name>/hooks.json + scripts
  plugins/<name>.json             {"skills": [], "agents": [], "mcp": [], "hooks": []}

catalog/<kind>-<name>/            entry = ready-made plugin
  REVIEW.md                       written by a human
  evals/<case>/                   written by a human: prompt.md, graders/
  evals/results/<ts>/report.html  eval run
  .claude-plugin/plugin.json      automatic
  skills/ agents/ hooks/ .mcp.json  automatic

template/                         templates for REVIEW.md and evals/
.claude-plugin/marketplace.json   built by build: one entry per catalog/ folder with a finished REVIEW.md

ui/
  index.html                      catalog
  catalog.js                      data for index.html, built by build
  build.py                        check lib/ and catalog/, build marketplace.json and catalog.js
  eval.py                         build an entry in catalog/, create cases, run claude plugin eval
```

## Commands

```
python3 ui/build.py && open ui/index.html   view the catalog
python3 ui/eval.py <path in lib> [--init]   build an entry in catalog/, create cases (--init), run eval
python3 ui/build.py [--check]               build marketplace.json and catalog.js; --check for CI
```

How to add an entry — see [CONTRIBUTING.md](CONTRIBUTING.md).
