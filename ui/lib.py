# lib.py — shared by build.py and eval.py.
#
# Repository layout:
#   lib/{skills/<name>/, agents/<name>.md, hooks/<name>/, mcp/<name>.json}   library: artifacts, added by a human or an agent
#   lib/plugins/<name>.json      bundle contents: {"skills": [...], "agents": [...], "mcp": [...], "hooks": [...]} — names from the library
#   catalog/<kind>-<name>/       catalog entry = a full plugin: it is what gets installed and what gets run through eval:
#       REVIEW.md, evals/            written by a human
#       .claude-plugin/ skills/ agents/ hooks/ .mcp.json   built by build.py and eval.py from the library per the contents
#       kind ∈ skill | agent | mcp | hook (a single part, contents by name) | plugin (contents from plugins/<name>.json)
#   .claude-plugin/marketplace.json   written by build: one entry per catalog/ folder that has a REVIEW.md, source "./catalog/<entry>"
#   config.json                  marketplace, repo_url, session model, verdicts
#   ui/                          the page, the generated catalog.js, these scripts

import hashlib, json, math, os, re, shutil, subprocess
from datetime import datetime, timezone
from pathlib import Path

UI = Path(__file__).resolve().parent
REPO = UI.parent
CONFIG = REPO / 'config.json'
MARKETPLACE_FILE = REPO / '.claude-plugin' / 'marketplace.json'
CATALOG = REPO / 'catalog'
PLUGINS = REPO / 'lib' / 'plugins'
CACHE = UI / '.cache'

KINDS = ['skill', 'agent', 'mcp', 'hook']                                          # kinds of library parts
LIB_DIR = {'skill': 'lib/skills', 'agent': 'lib/agents', 'mcp': 'lib/mcp', 'hook': 'lib/hooks'}
COMP_KEY = {'skill': 'skills', 'agent': 'agents', 'mcp': 'mcp', 'hook': 'hooks'}   # keys in plugins/<name>.json
ENTRY_KINDS = KINDS + ['plugin']
KIND_LABEL = {'skill': 'Skills', 'agent': 'Agents', 'mcp': 'MCP servers', 'hook': 'Hooks', 'plugin': 'Plugins'}
HUMAN = ['REVIEW.md', 'evals']                                                      # in the entry folder, written by a human
GENERATED = ['.claude-plugin', 'skills', 'agents', 'hooks', '.mcp.json']            # in the entry folder, written by build
VERDICTS = ['must-have', 'stack', 'task', 'taste', 'no']
NAME_RE = re.compile(r'[a-z0-9][a-z0-9._-]*')


def read_json(file, dflt=None):
    try: return json.loads(Path(file).read_text('utf-8'))
    except Exception: return dflt
def read_text(file):
    try: return Path(file).read_text('utf-8')
    except Exception: return None
def load_config(): return read_json(CONFIG)
def sha1(b): return hashlib.sha1(b).hexdigest()
def rel(p): return os.path.relpath(p, REPO)
def list_dir(d, pred):
    try: return sorted(e.name for e in os.scandir(d) if not e.name.startswith('.') and pred(e))
    except OSError: return []
def nn(v, dflt): return dflt if v is None else v
def jslen(s): return len(s.encode('utf-16-le')) // 2          # string length as in JS

# JSON like JSON.stringify: whole floats without ".0", non-ASCII as is
def _js(v):
    if isinstance(v, float) and v.is_integer(): return int(v)
    if isinstance(v, dict): return {k: _js(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)): return [_js(x) for x in v]
    return v
def to_json(v, indent=2): return json.dumps(_js(v), indent=indent, ensure_ascii=False)
def dumps(v): return to_json(v) + '\n'

# ---- frontmatter ----

_FM = re.compile(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', re.S)

def _unquote(s):
    m = re.fullmatch(r'(["\'])(.*)\1', s, re.S)
    if not m: return s
    return re.sub(r'\\(["\\])', r'\1', m.group(2)) if m.group(1) == '"' else m.group(2)
def _scalar(s):
    v = _unquote(s.strip())
    if v in ('', 'null', '~'): return None
    if v == 'true': return True
    if v == 'false': return False
    if re.fullmatch(r'-?\d+', v): return int(v)
    if re.fullmatch(r'-?\d+\.\d+', v): return float(v)
    return v
def _inline_list(s): return [x for x in (_scalar(p) for p in s[1:-1].split(',')) if x is not None]

# Top-level YAML frontmatter keys: `key: value`, quotes, `[a, b]`, block lists `- x`, block scalars > and |,
# multi-line plain scalars. Nested maps are skipped (value None). typed=False — everything as strings (SKILL.md, agents).
def parse_frontmatter(text, typed=False):
    m = _FM.match(text or '')
    if not m: return None
    lines = re.split(r'\r?\n', m.group(1))
    out, i = {}, 0
    while i < len(lines):
        kv = re.match(r'([A-Za-z0-9_-]+):\s*(.*)$', lines[i])
        if not kv: i += 1; continue
        key, val = kv.group(1), kv.group(2).strip()
        if val[:1] not in ('"', "'"): val = re.sub(r'(^|\s)#.*$', '', val).strip()      # YAML comment
        cont, j = [], i + 1
        while j < len(lines):
            if re.match(r'\s+\S', lines[j]): cont.append(lines[j].strip()); j += 1
            elif lines[j].strip() == '' and j + 1 < len(lines) and re.match(r'\s+\S', lines[j + 1]): j += 1
            else: break
        i = j
        is_list = bool(cont) and all(re.match(r'-\s+', l) for l in cont)
        looks_map = bool(cont) and not is_list and all(re.match(r'[A-Za-z0-9_-]+:(\s|$)', l) for l in cont)
        if is_list and val == '': val = [(_scalar(x) if typed else _unquote(x)) for x in (re.sub(r'^-\s+', '', l) for l in cont)]
        elif re.fullmatch(r'\[.*\]', val) and not cont: val = _inline_list(val) if typed else [_unquote(x.strip()) for x in val[1:-1].split(',')]
        elif re.fullmatch(r'[>|][+-]?', val): val = ' '.join(cont)
        elif cont and looks_map and val == '': val = None
        elif cont: val = ' '.join(x for x in [val, *cont] if x)
        if isinstance(val, str): val = _scalar(re.sub(r'\s+', ' ', val)) if typed else re.sub(r'\s+', ' ', _unquote(val)).strip()
        out[key] = val
    return out
def strip_frontmatter(text): return _FM.sub('', text, count=1)

# REVIEW.md: typed frontmatter (None if there is none), the body and its `## Heading` sections.
# use — the "## Summary" section (the "Why" table column and the plugin description); with no headings — the first paragraph, the rest as one unnamed section.
USE_RE = re.compile(r'summary', re.I)
def _para(t): return re.sub(r'\s+', ' ', re.split(r'\n\s*\n', t.strip(), maxsplit=1)[0]).strip() if t.strip() else ''
def parse_review(text):
    if text is None: return None
    body = strip_frontmatter(text).strip()
    sections, cur = [], {'title': '', 'text': ''}
    for line in body.split('\n'):
        m = re.match(r'##\s+(.+?)\s*$', line)
        if m: cur = {'title': m.group(1), 'text': ''}; sections.append(cur)
        else: cur['text'] += line + '\n'
    if not sections and cur['text'].strip():                      # old format: first paragraph and everything else
        parts = re.split(r'\n\s*\n', body, maxsplit=1)
        sections = [{'title': '', 'text': parts[1]}] if len(parts) > 1 else []
    use = next((x for x in sections if USE_RE.fullmatch(x['title'])), None)
    use_text = re.sub(r'\s+', ' ', use['text']).strip() if use else _para(body)
    return {'fm': parse_frontmatter(text, typed=True), 'body': body, 'use': use_text, 'first_paragraph': _para(use['text']) if use else use_text,
            'sections': [{'title': x['title'], 'text': x['text'].strip()} for x in sections if x is not use and x['text'].strip()]}

# ---- library ----

# all parts: {kind: {name: m}}; m = {kind, name, dir|None, main}
def load_library():
    lib = {k: {} for k in KINDS}
    S, A, M, H = (REPO / LIB_DIR[k] for k in KINDS)
    for n in list_dir(S, lambda e: e.is_dir()): lib['skill'][n] = dict(kind='skill', name=n, dir=S / n, main=S / n / 'SKILL.md')
    for f in list_dir(A, lambda e: e.is_file() and e.name.endswith('.md')): lib['agent'][f[:-3]] = dict(kind='agent', name=f[:-3], dir=None, main=A / f)
    for n in list_dir(H, lambda e: e.is_dir()): lib['hook'][n] = dict(kind='hook', name=n, dir=H / n, main=H / n / 'hooks.json')
    for f in list_dir(M, lambda e: e.is_file() and e.name.endswith('.json')): lib['mcp'][f[:-5]] = dict(kind='mcp', name=f[:-5], dir=None, main=M / f)
    return lib
def mkey(m): return (m['kind'], m['name'])

# plugins/<name>.json → {name, file, raw, comp: {skill: [...], agent: [...], mcp: [...], hook: [...]}}
def load_compositions():
    out = {}
    for f in list_dir(PLUGINS, lambda e: e.is_file() and e.name.endswith('.json')):
        raw = read_json(PLUGINS / f)
        comp = {k: [str(x) for x in raw[COMP_KEY[k]]] if isinstance(raw.get(COMP_KEY[k]), list) else [] for k in KINDS} if isinstance(raw, dict) else None
        out[f[:-5]] = dict(name=f[:-5], file=PLUGINS / f, raw=raw, comp=comp)
    return out
# contents of an entry by its kind: a single part, or a bundle from plugins/<name>.json
def composition_of(kind, name, comps):
    if kind == 'plugin': return (comps.get(name) or {}).get('comp')
    return {k: [name] if k == kind else [] for k in KINDS}
def comp_members(comp, lib):
    return [lib[k].get(n) or dict(kind=k, name=n, missing=True) for k in KINDS for n in (comp or {}).get(k, [])]

# ---- catalog entries ----

def parse_entry_name(s):
    m = re.fullmatch(r'(skill|agent|mcp|hook|plugin)-([a-z0-9][a-z0-9._-]*)', s)
    return dict(kind=m.group(1), name=m.group(2)) if m else None
# path to a part or a bundle → {kind, name}: lib/skills/docx, lib/agents/x.md, lib/mcp/x.json, lib/hooks/x, lib/plugins/x.json; catalog/<kind>-<name> is accepted too
def parse_lib_path(s):
    p = os.path.relpath(os.path.abspath(os.path.join(REPO, s)), REPO).split(os.sep)
    if p[0] == 'catalog': return parse_entry_name(p[1] if len(p) > 1 else '')
    if p[0] != 'lib' or len(p) < 3: return None
    kind = {'skills': 'skill', 'agents': 'agent', 'mcp': 'mcp', 'hooks': 'hook', 'plugins': 'plugin'}.get(p[1])
    return dict(kind=kind, name=re.sub(r'\.(md|json)$', '', p[2])) if kind else None
def lib_path_of(kind, name):
    if kind == 'plugin': return f'lib/plugins/{name}.json'
    return f"{LIB_DIR[kind]}/{name}{'.md' if kind == 'agent' else '.json' if kind == 'mcp' else ''}"
def entry_dir(id): return CATALOG / id

# catalog/<kind>-<name>/ → {id, kind, name, dir, where, review, comp, members}
def load_entries(lib, comps):
    out = []
    for id in list_dir(CATALOG, lambda e: e.is_dir()):
        p, d = parse_entry_name(id), entry_dir(id)
        comp = composition_of(p['kind'], p['name'], comps) if p else None
        out.append(dict(id=id, kind=p['kind'] if p else None, name=p['name'] if p else id, dir=d, where=rel(d),
                        review=parse_review(read_text(d / 'REVIEW.md')), comp=comp, members=comp_members(comp, lib) if comp else []))
    return out
def review_fm(e): return (e['review'] or {}).get('fm') or {}
# status: no REVIEW.md or draft: true → draft; verdict no → rejected; otherwise reviewed
def status_of(e):
    if not e['review'] or review_fm(e).get('draft') is True: return 'draft'
    return 'rejected' if review_fm(e).get('verdict') == 'no' else 'reviewed'

# ---- hashes ----

def hash_path(p, skip_top=()):
    p = Path(p)
    if not p.exists(): return None
    if p.is_file(): return sha1(p.read_bytes())
    h = hashlib.sha1()
    def walk(d, r):
        for e in sorted(os.scandir(d), key=lambda e: e.name):
            if e.name == '.DS_Store' or (not r and e.name in skip_top): continue
            rr = f'{r}/{e.name}' if r else e.name
            if e.is_dir(): walk(e.path, rr)
            else: h.update(f'{rr}\0'.encode()); h.update(f'{sha1(Path(e.path).read_bytes())}\n'.encode())
    walk(p, '')
    return h.hexdigest()
def tokens(chars): return math.floor(chars / 4 + 0.5)

# ---- facts about a part ----

def hook_events(frag): return list(((frag or {}).get('hooks') or {}).keys())
def hook_commands(frag): return [h.get('command') or '' for entries in ((frag or {}).get('hooks') or {}).values() for e in entries for h in (e.get('hooks') or [])]

def inspect_member(m):
    if m.get('missing') or not Path(m['main']).exists(): return None
    if m['kind'] in ('skill', 'agent'):
        text = read_text(m['main']) or ''
        fm = parse_frontmatter(text) or {}
        desc = fm['description'] if isinstance(fm.get('description'), str) else ''
        fm_name = fm['name'] if isinstance(fm.get('name'), str) else None
        out = dict(description=desc, fm_name=fm_name, tokens_meta=tokens(jslen(str(fm.get('name') or m['name'])) + jslen(desc)), tokens_body=tokens(jslen(text)))
        if m['kind'] == 'skill':
            size = files = 0; scripts = False
            for root, _, names in os.walk(m['dir']):
                for f in names:
                    rr = os.path.relpath(os.path.join(root, f), m['dir'])
                    if f == '.DS_Store' or rr == 'SKILL.md': continue
                    files += 1; size += os.path.getsize(os.path.join(root, f)); scripts = scripts or rr.startswith('scripts/')
            out.update(tokens_dir=tokens(size), files=files + 1, has_scripts=scripts)
        else:
            tools = fm.get('tools')
            out['tools'] = [t.strip() for t in tools.split(',') if t.strip()] if isinstance(tools, str) else None
            out['model'] = fm['model'] if isinstance(fm.get('model'), str) else None
        return out
    frag = read_json(m['main'])
    if not frag: return None
    if m['kind'] == 'mcp':
        return dict(type=frag.get('type') or ('http' if frag.get('url') else 'stdio'), url=frag.get('url'), command=frag.get('command'), args=frag.get('args'),
                    headers=frag.get('headers'), env_required=nn(frag.get('env_required'), []), source=frag.get('source'), tokens_meta=None)
    scripts = sorted(f for f in os.listdir(m['dir']) if f != 'hooks.json' and not f.startswith('.'))
    commands = hook_commands(frag)
    found = [re.search(r'\$\{CLAUDE_PLUGIN_ROOT\}/hooks/([^/\s"\']+)/([^\s"\']+)', c) for c in commands]
    missing = [x.group(0) for x in found if x and (x.group(1) != m['name'] or not (Path(m['dir']) / x.group(2)).exists())]
    return dict(events=hook_events(frag), commands=commands, scripts=scripts, missing=missing, valid=isinstance(frag.get('hooks'), dict) and len(commands) > 0,
                source=frag.get('source'), tokens_meta=0)

# ---- building an entry: catalog/<entry>/ as a full plugin ----

def mcp_server_of(frag): return {k: v for k, v in frag.items() if k not in ('env_required', 'source')}
def hooks_block_of(frag, root=None):
    fix = lambda h: h if root is None else {**h, 'command': str(h.get('command') or '').replace('${CLAUDE_PLUGIN_ROOT}', root)}
    return {ev: [{**e, 'hooks': [fix(h) for h in (e.get('hooks') or [])]} for e in entries] for ev, entries in (frag.get('hooks') or {}).items()}
def merge_hook_blocks(blocks):
    out = {}
    for b in blocks:
        for ev, entries in b.items(): out.setdefault(ev, []).extend(entries)
    return out
def _copy_tree(src, dst, skip_top=()):
    shutil.copytree(src, dst, ignore=lambda d, names: [n for n in names if n == '.DS_Store' or (os.fspath(d) == os.fspath(src) and n in skip_top)])
def _rm(p):
    if p.is_dir() and not p.is_symlink(): shutil.rmtree(p)
    elif p.exists() or p.is_symlink(): p.unlink()

# Build the generated part of an entry from the library. dry=True — only report whether there are differences.
# Returns the number of replaced GENERATED items. Does not touch REVIEW.md or evals/.
def materialize(e, cfg, dry=False):
    stage = CACHE / 'stage' / e['id']
    shutil.rmtree(stage, ignore_errors=True); stage.mkdir(parents=True)
    hooks, mcps = [], []
    for m in e['members']:
        if m.get('missing'): continue
        if m['kind'] == 'skill': _copy_tree(m['dir'], stage / 'skills' / m['name'], HUMAN)
        elif m['kind'] == 'agent': (stage / 'agents').mkdir(exist_ok=True); shutil.copy(m['main'], stage / 'agents' / f"{m['name']}.md")
        elif m['kind'] == 'hook': _copy_tree(m['dir'], stage / 'hooks' / m['name'], ['hooks.json']); hooks.append(read_json(m['main'], {}))
        elif m['kind'] == 'mcp': mcps.append((m['name'], read_json(m['main'], {})))
    if hooks: (stage / 'hooks' / 'hooks.json').write_text(dumps({'hooks': merge_hook_blocks([hooks_block_of(h) for h in hooks])}), 'utf-8')
    if mcps: (stage / '.mcp.json').write_text(dumps({'mcpServers': {n: mcp_server_of(f) for n, f in mcps}}), 'utf-8')
    description = review_fm(e).get('title') or (e['review'] or {}).get('use') or f"{e['kind']} {e['name']} (ai-context-builder)"
    manifest = {'name': e['name'], 'description': description}
    if (cfg.get('marketplace') or {}).get('owner'): manifest['author'] = cfg['marketplace']['owner']
    (stage / '.claude-plugin').mkdir(); (stage / '.claude-plugin' / 'plugin.json').write_text(dumps(manifest), 'utf-8')
    changed = 0
    for g in GENERATED:
        src, dst = stage / g, Path(e['dir']) / g
        if src.exists() == dst.exists() and (not src.exists() or hash_path(src) == hash_path(dst)): continue
        changed += 1
        if dry: continue
        _rm(dst)
        if src.is_dir(): shutil.copytree(src, dst)
        elif src.exists(): shutil.copy(src, dst)
    shutil.rmtree(stage, ignore_errors=True)
    return changed

# REVIEW.md template for a new entry: template/REVIEW.md, draft: true until a human fills it in
def review_template(e):
    return (REPO / 'template' / 'REVIEW.md').read_text('utf-8').replace('{what}', ', '.join(f"{m['kind']}/{m['name']}" for m in e['members']))

# ---- evals ----

def eval_info(d):
    E = Path(d) / 'evals'
    cases = [n for n in list_dir(E, lambda e: e.is_dir()) if n != 'results' and ((E / n / 'prompt.md').exists() or (E / n / 'case.yaml').exists())]
    runs = [n for n in list_dir(E / 'results', lambda e: e.is_dir()) if (E / 'results' / n / 'aggregate-result.json').exists()]
    latest = None
    if runs:
        R = E / 'results' / runs[-1]
        j = read_json(R / 'aggregate-result.json') or {}
        A = j.get('aggregates') or {}
        ag = lambda c: c.get('aggregates') or {}
        latest = dict(score=A.get('overallScore'), delta=A.get('meanDelta'), pass_rate=A.get('overallPassRate'), cases=A.get('casesTotal'), passed=A.get('casesPassed'),
                      cost_usd=j.get('costUsd'), version=j.get('claudeVersion'), at=(j.get('startedAt') or runs[-1])[:10], partial=bool(j.get('partial')),
                      report=rel(R / 'report.html') if (R / 'report.html').exists() else None, dir=rel(R),
                      per_case=[dict(name=c.get('name'), score=ag(c).get('score'), without=ag(c).get('scoreWithout'), delta=ag(c).get('delta')) for c in j.get('cases') or []])
    return dict(cases=cases, runs=len(runs), latest=latest)
# run command: the plugin's MCP servers do not start in eval without explicit permission
def eval_flags(e):
    mcps = [m for m in e['members'] if m['kind'] == 'mcp']
    return ['--allow-real-servers', '--allow-tools', *(f"mcp__plugin_{e['name']}_{m['name']}__*" for m in mcps)] if mcps else []

# ---- git ----

_git_ok = None
def is_git_repo():
    global _git_ok
    if _git_ok is None:
        try: _git_ok = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], cwd=REPO, capture_output=True).returncode == 0
        except OSError: _git_ok = False
    return _git_ok
def git_last_commit(paths, exclude=()):
    if not is_git_repo() or not paths: return None
    try:
        r = subprocess.run(['git', 'log', '-1', '--format=%ct', '--', *map(rel, paths), *(f':(exclude){rel(p)}' for p in exclude)], cwd=REPO, capture_output=True, text=True, check=True)
        return int(r.stdout.strip()) if r.stdout.strip() else None
    except Exception: return None
def unix_to_date(ts): return None if ts is None else datetime.fromtimestamp(ts, timezone.utc).strftime('%Y-%m-%d')

def write_if_changed(file, content):
    file, b = Path(file), content if isinstance(content, bytes) else content.encode('utf-8')
    if file.exists() and file.read_bytes() == b: return False
    file.parent.mkdir(parents=True, exist_ok=True); file.write_bytes(b)
    return True
