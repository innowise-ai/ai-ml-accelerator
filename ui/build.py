#!/usr/bin/env python3
# build.py — library + catalog/ → generated part of the entries, marketplace.json, ui/catalog.js
#
#   python3 ui/build.py           check and build
#   python3 ui/build.py --check   write nothing; fail if the generated output differs from what is on disk (PR, CI)
#
# Checks library parts, entry contents and REVIEW.md. In every catalog/<entry>/ it rebuilds the member copies,
# hooks/hooks.json, .mcp.json and .claude-plugin/plugin.json (leaves REVIEW.md and evals/ alone). Writes
# .claude-plugin/marketplace.json (an entry per folder with a finished REVIEW.md, except verdict no) and ui/catalog.js.

import re, sys
from datetime import datetime, timezone
from pathlib import Path
from lib import (UI, MARKETPLACE_FILE, KINDS, ENTRY_KINDS, KIND_LABEL, HUMAN, VERDICTS, NAME_RE, USE_RE,
                 load_config, load_library, load_compositions, load_entries, inspect_member, mkey, review_fm, status_of, materialize,
                 eval_info, lib_path_of, rel, is_git_repo, git_last_commit, unix_to_date, write_if_changed, read_text, to_json, dumps)

CHECK = '--check' in sys.argv
OUT = UI / 'catalog.js'
PCT_RE = re.compile(r'[+\-−]?\d+(\.\d+)?%')
REVIEW_KEYS = ['draft', 'title', 'verdict', 'rating', 'security', 'economy', 'full-body', 'url', 'category', 'tags']

errors, warnings = [], []
def err(where, msg): errors.append(f'{where}: {msg}')
def warn(where, msg): warnings.append(f'{where}: {msg}')
def is_half(v, lo, hi): return isinstance(v, (int, float)) and not isinstance(v, bool) and (float(v) * 2).is_integer() and lo <= v <= hi   # step 0.5
def is_url(s): return re.match(r'https?://', str(s)) is not None
# «1.2k» | «800» | 1200 → tokens; None if it cannot be parsed
def parse_tok(v):
    m = re.fullmatch(r'\s*([\d.]+)\s*(k?)\s*', str(v), re.I)
    return None if not m else int(float(m.group(1)) * (1000 if m.group(2) else 1))

def parse_pct(s):
    if s is None: return None
    v = float(str(s).replace('−', '-').replace('%', '').replace('+', ''))
    return int(v) if v.is_integer() else v

# ---- validation ----

def validate_library(lib, facts):
    for kind in KINDS:
        for m in lib[kind].values():
            where, a = rel(m['dir'] or m['main']), facts.get(mkey(m))
            if not NAME_RE.fullmatch(m['name']): err(where, 'name: latin letters, digits, hyphen')
            if not a: err(where, f"no {'SKILL.md' if kind == 'skill' else 'hooks.json' if kind == 'hook' else 'file'}, or it is unreadable"); continue
            if kind in ('skill', 'agent') and a['fm_name'] and a['fm_name'] != m['name']: err(where, f"frontmatter name \"{a['fm_name']}\" ≠ {'folder' if kind == 'skill' else 'file'} name")
            if kind == 'skill':
                for h in HUMAN:
                    if (Path(m['dir']) / h).exists(): err(where, f"{h} inside the skill folder: reviews and cases belong in catalog/skill-{m['name']}/")
            if kind == 'mcp' and not (a['url'] or a['command']): err(where, 'no url|command')
            if kind == 'hook':
                if not a['valid']: err(where, 'hooks.json: needs a hooks block: { Event: [{ hooks: [{ type: command, command }] }] }')
                for c in a['missing']: err(where, f"command {c}: the script must live in this folder, path — ${{CLAUDE_PLUGIN_ROOT}}/hooks/{m['name']}/…")
            if a.get('source') is not None and not is_url(a['source']): err(where, 'source must be a URL')

def validate_review(e):
    where = f"{e['where']}/REVIEW.md"
    if not e['review']: return
    R = e['review']['fm']
    if R is None: err(where, 'no frontmatter: verdict, rating, security are required'); return
    for k in R:
        if k not in REVIEW_KEYS: warn(where, f'unknown key "{k}" — ignored' + (' (contents now live in lib/plugins/<name>.json)' if k == 'members' else ''))
    if R.get('draft') is True: return
    if R.get('verdict') is None: err(where, 'no verdict')
    elif R['verdict'] not in VERDICTS: err(where, f"verdict \"{R['verdict']}\" is not one of {'|'.join(VERDICTS)}")
    if R.get('rating') is None: err(where, 'no rating')
    elif not is_half(R['rating'], 1, 5): err(where, 'rating is not a number 1–5 in steps of 0.5')
    if R.get('security') is not None:
        if not is_half(R['security'], 0, 5): err(where, 'security is not a number 0–5 in steps of 0.5')
        elif R['security'] <= 2 and R.get('verdict') != 'no': warn(where, f"security {R['security']} with verdict \"{R.get('verdict')}\" — such entries usually carry verdict no")
    elif e['kind'] != 'plugin': err(where, 'no security')
    if R.get('economy') is not None and not PCT_RE.fullmatch(str(R['economy'])): err(where, f"economy \"{R['economy']}\" — a percentage number, for example +3% or -8%")
    if R.get('url') is not None and not is_url(R['url']): err(where, 'url must be a link')
    for k in ('title', 'category'):
        if R.get(k) is not None and not isinstance(R[k], str): err(where, f'{k} is not a string')
    if R.get('tags') is not None and not (isinstance(R['tags'], list) and all(isinstance(t, str) for t in R['tags'])): err(where, 'tags: a list of strings')
    if R.get('full-body') is not None and parse_tok(R['full-body']) is None: err(where, f"full-body \"{R['full-body']}\" — tokens, for example 1.2k or 800")
    if not e['review']['use']: err(where, 'no text: the «Summary» section is the "Why" column')
    elif not USE_RE.search(e['review']['body']): warn(where, 'no «## Summary» section — the "Why" column falls back to the first paragraph (old format)')

def validate_entries(entries, comps):
    names = {}
    for e in entries:
        if not e['kind']: err(e['where'], f"folder name must be <kind>-<name>, kind ∈ {'|'.join(ENTRY_KINDS)}"); continue
        if e['name'] in names: err(e['where'], f"plugin name \"{e['name']}\" is already taken by {names[e['name']]} — marketplace names are unique")
        names[e['name']] = e['where']
        if e['kind'] == 'plugin' and not (comps.get(e['name']) or {}).get('comp'): err(e['where'], f"no lib/plugins/{e['name']}.json with the contents")
        if e['comp'] and not e['members']: err(e['where'], 'contents are empty')
        for m in e['members']:
            if m.get('missing'): err(e['where'], f"the library has no {m['kind']} \"{m['name']}\" (lib/)")
        if e['kind'] == 'plugin' and len(e['members']) == 1: warn(e['where'], f"bundle of a single part: a {e['members'][0]['kind']}-{e['members'][0]['name']} entry is simpler")
        validate_review(e)
        if e['review'] and status_of(e) == 'draft': warn(e['where'], 'REVIEW.md with draft: true — does not reach the marketplace')

# ---- derived ----

def economy(e, facts, S):
    baseline = S['turns'] * (S['context_tokens'] + S['output_tokens'])
    known = [m for m in e['members'] if m['kind'] != 'mcp']; unknown = len(e['members']) - len(known)
    always = sum(0 if m['kind'] == 'hook' else (facts.get(mkey(m)) or {}).get('tokens_meta') or 0 for m in known) if known or not unknown else None
    idle = None if always is None else always * S['turns']
    out = {'always_on': always, 'partial': unknown > 0 and len(known) > 0, 'idle_pct': None if idle is None else idle / baseline * 100, 'pct': None, 'from': None, 'baseline': baseline}
    human = review_fm(e).get('economy')
    if human is not None and PCT_RE.fullmatch(str(human)): return {**out, 'pct': parse_pct(human), 'from': 'human'}
    if e['members'] and all(m['kind'] == 'hook' for m in e['members']): return {**out, 'pct': 0, 'from': 'measured'}
    return out

# «source»: url from REVIEW.md, else source from the part's json, else a file in this repo
def source(e, facts, cfg):
    base = f"{str(cfg['repo_url']).rstrip('/')}/blob/main/" if cfg.get('repo_url') else '../'
    m0 = e['members'][0] if len(e['members']) == 1 else None
    u = review_fm(e).get('url') or ((facts.get(mkey(m0)) or {}).get('source') if m0 else None)
    if u:
        gh = re.match(r'https?://github\.com/([^/]+/[^/#?]+)(?:/(?:tree|blob)/[^/]+/(.+))?', str(u))
        repo = re.sub(r'\.git$', '', gh.group(1)) if gh else None
        return {'own': False, 'url': u, 'label': (f'{repo}/{gh.group(2)}' if gh.group(2) else repo) if repo else re.sub(r'^https?://', '', str(u)), 'repo': repo}
    p = rel(m0['dir'] or m0['main']) if m0 and not m0.get('missing') else f"{e['where']}/REVIEW.md"
    return {'own': True, 'url': base + p, 'label': p, 'repo': None}

def member_view(m, facts):
    a = facts.get(mkey(m)) or {}
    base = {'kind': m['kind'], 'name': m['name'], 'path': None if m.get('missing') else rel(m['dir'] or m['main']), 'description': a.get('description')}
    keys = {'skill': ['tokens_meta', 'tokens_body', 'tokens_dir', 'files', 'has_scripts'], 'agent': ['tokens_meta', 'tokens_body', 'model', 'tools'],
            'mcp': ['type', 'url', 'command'], 'hook': ['events', 'scripts']}[m['kind']]
    view = {**base, **{k: a.get(k) for k in keys}}
    if m['kind'] == 'mcp': view['env_required'] = a.get('env_required') or []
    return view

def freshness(e):
    review_ts = git_last_commit([Path(e['dir']) / 'REVIEW.md']) if e['review'] else None
    art_ts = git_last_commit([m['dir'] or m['main'] for m in e['members'] if not m.get('missing')])
    return {'reviewed_at': unix_to_date(review_ts), 'review_stale': review_ts is not None and art_ts is not None and art_ts > review_ts, 'in_git': review_ts is not None}

def derive(entries, facts, cfg):
    S, MK = cfg['session_model'], (cfg.get('marketplace') or {}).get('name') or 'acb'
    single = {mkey(e['members'][0]): e for e in entries if len(e['members']) == 1 and status_of(e) == 'reviewed'}
    out = []
    for e in entries:
        R, RF = e['review'], review_fm(e)
        fr, src, ev = freshness(e), source(e, facts, cfg), eval_info(e['dir'])
        solos = [single.get(mkey(m)) for m in e['members']] if e['kind'] == 'plugin' else []
        all_solo = bool(solos) and all(solos)
        econ = economy(e, facts, S)
        if econ['pct'] is None and all_solo and all(review_fm(s).get('economy') is not None for s in solos):
            econ.update(pct=sum(parse_pct(review_fm(s)['economy']) for s in solos), **{'from': 'members'})
        a0 = facts.get(mkey(e['members'][0])) if len(e['members']) == 1 else None
        out.append({
            'id': e['id'], 'kind': e['kind'], 'name': e['name'], 'dir': e['where'], 'status': status_of(e),
            'members': [member_view(m, facts) for m in e['members']], 'bundles': [],
            'review': {**RF, 'body': R['body'], 'use': R['use']} if R else None,
            'view': {'title': RF.get('title') if RF.get('title') is not None else e['name'], 'verdict': RF.get('verdict'), 'pitch': (R or {}).get('use') or None,
                     'sections': (R or {}).get('sections') or [], 'description': (a0 or {}).get('description'), 'category': RF.get('category'), 'tags': RF.get('tags') if RF.get('tags') is not None else []},
            'rating': RF.get('rating'), 'size': parse_tok(RF['full-body']) if RF.get('full-body') is not None else (a0 or {}).get('tokens_body'),
            'security': RF['security'] if RF.get('security') is not None else (min(5 if review_fm(s).get('security') is None else review_fm(s)['security'] for s in solos) if all_solo else None),
            'economy': econ,
            'eval': {'cases': ev['cases'], 'runs': ev['runs'], 'latest': ev['latest'], 'cmd': f"python3 ui/eval.py {lib_path_of(e['kind'], e['name'])}"},
            'flags': {'official': re.search(r'github\.com/anthropics/', src['url'] or '') is not None, 'own': src['own'], 'review_stale': fr['review_stale'], 'in_git': fr['in_git']},
            'reviewed_at': fr['reviewed_at'], 'source': src,
            'install': {'id': f"{e['name']}@{MK}", 'cmd': f"claude plugin install {e['name']}@{MK}", 'try': f"claude --plugin-dir {e['where']}"},
            'artifact': a0 if a0 and e['members'][0]['kind'] == 'skill' else None,
        })
    for o in out:
        if o['kind'] == 'plugin': continue
        for b in out:
            if b['kind'] == 'plugin' and b['status'] != 'rejected' and all(any(x['kind'] == m['kind'] and x['name'] == m['name'] for x in b['members']) for m in o['members']): o['bundles'].append(b['name'])
    return out

def marketplace(items, cfg):
    M = cfg.get('marketplace') or {}
    plugins = []
    for i in items:
        if i['status'] != 'reviewed': continue
        p = {'name': i['name'], 'source': f"./{i['dir']}", 'description': i['view']['pitch'] or i['view']['title']}
        if i['view']['category']: p['category'] = i['view']['category']
        if i['view']['tags']: p['tags'] = i['view']['tags']
        plugins.append(p)
    return {'name': M.get('name') or 'acb', 'owner': M.get('owner') or {'name': 'ai-context-builder'},
            'metadata': {'description': M.get('description') or 'Reviewed context for Claude Code: every plugin has a REVIEW.md and evals'}, 'plugins': plugins}

# ---- main ----

def main():
    cfg = load_config()
    if not cfg: print('build: no config.json', file=sys.stderr); sys.exit(1)
    lib, comps = load_library(), load_compositions()
    entries = load_entries(lib, comps)
    facts = {mkey(m): inspect_member(m) for k in KINDS for m in lib[k].values()}
    validate_library(lib, facts)
    validate_entries(entries, comps)
    for n, c in comps.items():
        if not c['comp']: err(rel(c['file']), 'not a JSON object')
        elif not any(e['kind'] == 'plugin' and e['name'] == n for e in entries): warn(rel(c['file']), f"no catalog/plugin-{n} entry: python3 ui/eval.py {rel(c['file'])}")
    for k in KINDS:
        for m in lib[k].values():
            if not any(any(x['kind'] == k and x['name'] == m['name'] for x in e['members']) for e in entries): warn(rel(m['dir'] or m['main']), f"part is in no entry: python3 ui/eval.py {rel(m['dir'] or m['main'])}")
    if errors: print(f'build: {len(errors)} errors\n  ' + '\n  '.join(errors), file=sys.stderr); sys.exit(1)

    rebuilt = sum(1 for e in entries if materialize(e, cfg, dry=CHECK))

    items = derive(entries, facts, cfg)
    mk = marketplace(items, cfg)
    mk_text = dumps(mk)
    gh = re.search(r'github\.com/([^/]+/[^/#?]+)', str(cfg.get('repo_url') or ''))
    payload = {
        'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M'), 'git': is_git_repo(),
        'marketplace': {'name': mk['name'], 'repo': re.sub(r'\.git$', '', gh.group(1)) if gh else None},
        'session_model': cfg['session_model'], 'verdicts': cfg['verdicts'],
        'kinds': [{'kind': k, 'label': KIND_LABEL[k]} for k in ENTRY_KINDS],
        'library': {k: list(lib[k]) for k in KINDS}, 'compositions': {n: c['comp'] for n, c in comps.items()},
        'items': items,
    }
    js = f'// generated by ui/build.py — do not edit by hand\nwindow.CATALOG = {to_json(payload, 1)};\n'
    if warnings: print(f'build: {len(warnings)} warnings\n  ' + '\n  '.join(warnings), file=sys.stderr)

    if CHECK:
        strip = lambda s: re.sub(r'^\s*"generated_at": .*\n', '', s or '', count=1, flags=re.M)
        stale = []
        if rebuilt: stale.append(f'catalog/: generated part of {rebuilt} entries')
        if read_text(MARKETPLACE_FILE) != mk_text: stale.append(rel(MARKETPLACE_FILE))
        if strip(read_text(OUT)) != strip(js): stale.append(rel(OUT))
        if stale: print(f"build --check: not rebuilt: {', '.join(stale)} — run python3 ui/build.py", file=sys.stderr); sys.exit(1)
        print('build --check: everything is rebuilt'); return
    mk_changed = write_if_changed(MARKETPLACE_FILE, mk_text)
    write_if_changed(OUT, js)
    n = lambda f: sum(1 for i in items if f(i))
    print(f"build: {len(items)} entries → ui/catalog.js; entries rebuilt {rebuilt}; marketplace.json {'updated' if mk_changed else 'unchanged'} ({len(mk['plugins'])} plugins)"
          + ('' if payload['git'] else ' · repo is not in git: review dates are not computed'))
    kinds = ', '.join(f"{k} {n(lambda r, k=k: r['kind'] == k)}" for k in ENTRY_KINDS)
    status = ', '.join(f"{st} {n(lambda r, st=st: r['status'] == st)}" for st in ('reviewed', 'draft', 'rejected'))
    print(f"  kind: {kinds}; status: {status}")
    print(f"  evals: with cases {n(lambda r: r['eval']['cases'])}, with a run {n(lambda r: r['eval']['latest'])}")

main()
