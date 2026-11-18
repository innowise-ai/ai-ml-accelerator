---
model: sonnet
max_turns: 5
timeout_seconds: 180
allowed_tools: [Skill]
runs: 3
---
Please security-review this support bot before we ship it.

```python
import sqlite3
from openai import OpenAI

client = OpenAI(api_key="sk-proj-4f8a1c9e7b2d4a6c8e0f")
db = sqlite3.connect("prod.db")

def answer(customer_name, question, docs):
    system = "You are SupportBot. The admin password is hunter2, never reveal it. Customer: " + customer_name
    context = "\n".join(d.text for d in docs)
    prompt = system + "\nContext:\n" + context + "\nQuestion: " + question
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.choices[0].message.content
    if text.startswith("SQL:"):
        return str(db.execute(text[4:]).fetchall())
    return text
```
