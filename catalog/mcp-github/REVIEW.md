---
verdict: must-have
rating: 5
security: 3.5
economy: +3%
full-body: 600
---
## Summary
When the project is on GitHub: the agent opens PRs and issues itself, reads reviews and the logs of failed Actions

## Examples
- "Open a PR from this branch and reply to the reviewer" => `create_pull_request` and `add_reply_to_pull_request_comment` straight from the session, without gh CLI and without the web
- CI failed => `get_job_logs` with `failed_only: true` returns the logs of every failed job of one run, instead of copy-paste from Actions or switching to browser using tools

## Notes
I use it constantly
Schemas of ~40 tools ≈ 18k tok, but Claude Code loads them deferred: ≈ 600 tok of names in the context, the schema is pulled in on call
The token goes only to the official GitHub server, where the code already lives anyway
