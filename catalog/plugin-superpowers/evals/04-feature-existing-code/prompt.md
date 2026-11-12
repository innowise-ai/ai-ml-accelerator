---
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
runs: 3
---
Here's our team's notes service (`app.py`):

```python
from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)
DB = "notes.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.get("/notes")
def list_notes():
    rows = get_db().execute(
        "SELECT id, title, body, created_at FROM notes ORDER BY created_at DESC"
    ).fetchall()
    return jsonify([dict(r) for r in rows])

@app.post("/notes")
def create_note():
    data = request.get_json()
    db = get_db()
    cur = db.execute("INSERT INTO notes (title, body) VALUES (?, ?)", (data["title"], data["body"]))
    db.commit()
    return jsonify({"id": cur.lastrowid}), 201

@app.delete("/notes/<int:note_id>")
def delete_note(note_id):
    db = get_db()
    db.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    db.commit()
    return "", 204
```

Add user accounts to this.
