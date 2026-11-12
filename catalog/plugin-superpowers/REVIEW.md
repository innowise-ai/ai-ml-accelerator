---
title: Superpowers
url: https://github.com/obra/superpowers
verdict: taste
rating: 4
security: 3
economy: +3%
category: workflow
tags: [brainstorming, tdd, debugging, planning]
---
## Summary
For people who want Claude to stop and ask before it starts building. On a vague request like "build me X", it asks one clear question first instead of writing a whole app. It also comes with skills for debugging, TDD, planning and code review.

## Examples
- "Build me a habit tracker app" - without the plugin it writes the whole app into files straight away. With it, it asks one question ("what do you want it to help you with?"), says how the answer changes what gets built, and offers "or I can just start".
- Flask app pasted in + "Add user accounts to this" - without the plugin it starts coding right away. With it, it asks about the parts that change the build (who the accounts are for, what should need a login), using the routes from the pasted code.
- A detailed spec (FastAPI + Postgres, three endpoints) + "Implement this." => no difference. The brainstorming skill did not fire in any of 3 runs, and both versions wrote the whole service without checking anything first.
- Simple tasks ("rename this function", "list vs tuple?") => it just answers, the same as without it. No unnecessary questions.

## Notes
Only the brainstorming flow was tested. The other 14 skills (TDD, debugging, plans, code review, etc.) are not covered by these evals.

It changes how Claude works in every session. A hook adds the using-superpowers rules at the start of every session, so it pushes Claude to use skills all the time. That is a matter of taste: some people like the "ask, plan, then build" style, others find it slow.
