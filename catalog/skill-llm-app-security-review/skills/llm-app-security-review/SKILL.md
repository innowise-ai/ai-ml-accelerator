---
name: llm-app-security-review
description: >
  Reviews the code of an LLM-powered application (prompts, RAG pipelines, tool
  calling, agents) for security problems and returns a fixed-format report
  mapped to the OWASP Top 10 for LLM Applications (2025). Use when someone asks
  to security-review, audit, threat-model or check for prompt injection in code
  that calls an LLM, or shares a snippet of such code and asks whether it is safe.
---

# LLM Application Security Review

Review what the code actually does. Do not give generic advice and do not invent findings.

## Scope

Applies to code that builds prompts, calls a model API, retrieves documents, executes tools or handles model output.

Does not apply to a plain web application with no LLM, to model training safety, or to content moderation policy.

## Procedure

1. Map the data flow. List where untrusted text enters (user input, retrieved documents, web pages, tool results, file contents, other agents), where it is placed in a prompt, what the model can do (tools, code execution, network access, writes), and where model output goes (UI, database, shell, generated code, other services).
2. Walk all ten categories below in order. For each one, either record a finding or write one line saying why it does not apply to the code shown.
3. For every finding quote the exact line or snippet, state the concrete attack, and give the smallest fix that closes it.
4. List what could not be judged from the code given: deployment, IAM, network rules, vendor settings, data sources that are not shown.

## Categories (OWASP Top 10 for LLM Applications, 2025)

- LLM01 Prompt Injection: untrusted text concatenated into instructions, retrieved or tool-returned text treated as instructions, no delimiting or privilege separation.
- LLM02 Sensitive Information Disclosure: secrets, personal data or other users' data placed in prompts, logs or responses.
- LLM03 Supply Chain: unpinned or unverified models, datasets, plugins, MCP servers and packages; models loaded with unsafe deserialization.
- LLM04 Data and Model Poisoning: unreviewed data flowing into fine-tuning, embeddings or retrieval stores.
- LLM05 Improper Output Handling: model output passed to eval, exec, a shell, SQL, HTML or URLs without validation or escaping.
- LLM06 Excessive Agency: tools with broader permissions than the task needs, destructive actions without human confirmation, tool arguments taken from the model unchecked.
- LLM07 System Prompt Leakage: secrets, credentials or access rules stored in the system prompt and relied on as a control.
- LLM08 Vector and Embedding Weaknesses: missing per-tenant access control on retrieval, shared indexes, unfiltered ingestion.
- LLM09 Misinformation: model answers shown as fact without grounding, citations or a fallback where errors are costly.
- LLM10 Unbounded Consumption: no max token limits, rate limits, timeouts, loop or recursion caps, or per-user budgets.

## Severity

- Critical: an attacker with ordinary user access can reach code execution, other users' data, or destructive actions.
- High: untrusted text can steer tool use or leak secrets, but a precondition is needed.
- Medium: a weakness that raises the impact of another flaw, or abuse limited to the attacker's own session.
- Low: hardening and hygiene.

## Output format

Use exactly these sections, in this order:

```
## Verdict
One sentence: safe to ship, ship after fixes, or do not ship, and the single biggest reason.

## Data flow
Untrusted inputs, model capabilities, output sinks. Three short lines.

## Findings
### [SEVERITY] Short title (LLMxx)
- Where: quoted line or snippet
- Attack: one concrete scenario
- Fix: smallest change that closes it

## Checked, no issue
LLMxx: one line each

## Not reviewed
What the code given does not show.
```

Order findings from most to least severe. A category with no finding goes under "Checked, no issue".

## Rules

- Quote the code. A finding without a quoted location is not allowed.
- No generic advice such as "validate inputs" without naming the input and the check.
- Do not rewrite the whole application; propose the minimal fix for each finding.
- Never claim a control exists if it is not visible in the code; put it under "Not reviewed".
- Do not run or execute the code under review.
