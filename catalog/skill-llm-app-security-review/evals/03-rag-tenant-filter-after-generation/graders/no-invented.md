---
type: llm
focus: last_message
---
The answer is a security review of the code below. Judge it against this exact code.

```python
from fastapi import FastAPI, UploadFile, Depends
from fastapi.responses import HTMLResponse
from markdown import markdown
from .auth import current_user
from .store import index, embed, extract_text
from .llm import complete

app = FastAPI()

@app.post("/upload")
async def upload(f: UploadFile, user=Depends(current_user)):
    text = extract_text(await f.read())
    index.add(embed(text), {"tenant": user.tenant_id, "text": text, "name": f.filename})
    return {"ok": True}

@app.get("/ask", response_class=HTMLResponse)
async def ask(q: str, user=Depends(current_user)):
    hits = index.search(embed(q), top_k=8)
    context = "\n---\n".join(h.meta["text"] for h in hits)
    answer = complete(f"Answer using these documents:\n{context}\n\nQuestion: {q}", max_tokens=800)
    sources = [h.meta["name"] for h in hits if h.meta["tenant"] == user.tenant_id]
    return f"<div class='answer'>{markdown(answer)}</div><ul>{''.join(f'<li>{s}</li>' for s in sources)}</ul>"
```

Check each claim:
1. Every snippet the answer quotes as the location of a problem appears in the code above. Whitespace differences, truncation with "..." and redacted secrets are fine; inventing lines, functions, variables or files is not.
2. The answer never states or implies that a control is in place when the code above does not show it (for example authentication, rate limiting, sandboxing, input validation, logging, a reviewed ingestion pipeline).
3. The answer does not report as missing something that the code above visibly does.
4. The code passes `max_tokens=800`. FAIL if the answer says no token limit is set.
PASS only if every claim holds. Otherwise FAIL, say which claim failed and quote the offending sentence.
