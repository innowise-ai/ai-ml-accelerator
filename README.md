# ai-context-builder

A catalog of vetted context for Claude Code (later for Codex too). Four kinds: skills, MCP servers, hooks, agents, plus bundles of them — plugins. Everything lives in `lib/`. In `catalog/` — reviews: `REVIEW.md` (a human review with notes) and `evals/` (cases that check this skill, MCP or bundle).

To install, it is enough to open `ui/index.html`: a table with verdict, rating, security, token cost and eval result; you tick the entries and get the install commands and the text for the agent window.

![The catalog in ui/index.html: entries with verdict, rating, security, token cost and eval; the basket on the right builds the install commands](docs/catalog.png)


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


## What's in it

| Category | Name | Eval | Review |
|---|---|---|---|
| skill | caveman | – | ✅ |
| skill | claude-api | 1 case · Δ +0.50 | ✅ |
| skill | docx | – | ✅ |
| skill | mcp-builder | – |  |
| skill | skill-creator | – | ✅ |
| mcp | context7 | 2 cases · Δ +0.58 | ✅ |
| mcp | github | – | ✅ |
| hook | notify-done | – | ✅ |
| agent | – | – |  |
| plugin | base | – |  |
| plugin | evals | 32 cases · last run incomplete (16 of 32) |  |
| plugin | langchain | – |  |
| plugin | qdrant | – |  |

A plugin is a bundle of parts from `lib/`, so its members are not repeated as rows of their own. ✅ means a finished `REVIEW.md`; only those entries reach `ui/index.html` and the marketplace.

<details>
<summary><b>plugin/base</b> – empty for now</summary>

A placeholder for the bundle every project starts from. Nothing in it yet.

</details>

<details>
<summary><b>plugin/evals</b> – 8 skills from <a href="https://github.com/ai-evals-course/evals-skills">ai-evals-course/evals-skills</a></summary>

| Category | Name | Eval | Review |
|---|---|---|---|
| skill | evals-start | – |  |
| skill | eval-audit | – |  |
| skill | error-discovery | – |  |
| skill | write-judge-prompt | – |  |
| skill | validate-evaluator | – |  |
| skill | generate-synthetic-data | – |  |
| skill | evaluate-rag | – |  |
| skill | build-review-interface | – |  |

</details>

<details>
<summary><b>plugin/langchain</b> – 22 skills from <a href="https://github.com/langchain-ai/langchain-skills">langchain-ai/langchain-skills</a></summary>

| Category | Name | Eval | Review |
|---|---|---|---|
| skill | deep-agents-core | – |  |
| skill | deep-agents-memory | – |  |
| skill | deep-agents-orchestration | – |  |
| skill | deepagents-python-quickstart | – |  |
| skill | deepagents-typescript-quickstart | – |  |
| skill | ecosystem-primer | – |  |
| skill | eval-engineering | – |  |
| skill | langchain-dependencies | – |  |
| skill | langchain-fundamentals | – |  |
| skill | langchain-middleware | – |  |
| skill | langchain-python-quickstart | – |  |
| skill | langchain-rag | – |  |
| skill | langchain-typescript-quickstart | – |  |
| skill | langgraph-cli | – |  |
| skill | langgraph-fundamentals | – |  |
| skill | langgraph-human-in-the-loop | – |  |
| skill | langgraph-persistence | – |  |
| skill | langgraph-python-quickstart | – |  |
| skill | langgraph-typescript-quickstart | – |  |
| skill | langsmith-online-eval-engineering | – |  |
| skill | managed-deep-agents | – |  |
| skill | swarm | – |  |

</details>

<details>
<summary><b>plugin/qdrant</b> – 12 skills from <a href="https://github.com/qdrant/skills">qdrant/skills</a></summary>

| Category | Name | Eval | Review |
|---|---|---|---|
| skill | qdrant-clients-sdk | – |  |
| skill | qdrant-deployment-options | – |  |
| skill | qdrant-edge | – |  |
| skill | qdrant-migration-tool | – |  |
| skill | qdrant-model-migration | – |  |
| skill | qdrant-monitoring | – |  |
| skill | qdrant-multitenancy | – |  |
| skill | qdrant-performance-optimization | – |  |
| skill | qdrant-scaling | – |  |
| skill | qdrant-search-quality | – |  |
| skill | qdrant-sizing | – |  |
| skill | qdrant-version-upgrade | – |  |

</details>

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
