"""Build the preserved Markdown into a portable, searchable static website."""
import html
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit, unquote
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
OUT.mkdir(exist_ok=True)
parser = MarkdownIt('commonmark', {'html': True}).enable('table')
pages = sorted(p for p in ROOT.rglob('*.md') if p.parts[len(ROOT.parts)] not in ('.git', '_site', 'site'))
known = {p.relative_to(ROOT).as_posix() for p in pages}
search = []

def escaped(value):
    return html.escape(str(value), quote=True)

def convert_link(value, current):
    url = urlsplit(value)
    if url.scheme or url.netloc or not url.path:
        return value
    target = os.path.normpath(os.path.join(os.path.dirname(current), unquote(url.path))).replace('\\', '/')
    if target in known:
        return url.path[:-3] + '.html' + ('?' + url.query if url.query else '') + ('#' + url.fragment if url.fragment else '')
    # Original sources and metadata stay directly accessible in the archive repository.
    if target.startswith(('source/', 'metadata/')):
        return 'https://github.com/erika-archive/erika-wiki/blob/main/' + target
    return value

for path in pages:
    relative = path.relative_to(ROOT).as_posix()
    prefix = '../' * relative.count('/')
    soup = BeautifulSoup(parser.render(path.read_text(encoding='utf-8')), 'html.parser')
    title = soup.h1.get_text() if soup.h1 else path.stem
    used = {tag['id'] for tag in soup.find_all(id=True)}
    toc = []
    for heading in soup.find_all(re.compile('^h[1-6]$')):
        anchor = re.sub(r'[^\w\- ]', '', heading.get_text().lower()).replace(' ', '-') or 'section'
        original = anchor
        suffix = 1
        while anchor in used:
            anchor = f'{original}-{suffix}'; suffix += 1
        if not heading.get('id'):
            heading['id'] = anchor; used.add(anchor)
        if heading.name in ('h2', 'h3'):
            toc.append(f'<a href="#{escaped(heading["id"])}">{escaped(heading.get_text())}</a>')
    for tag in soup.find_all(['a', 'img']):
        attribute = 'href' if tag.name == 'a' else 'src'
        if tag.get(attribute):
            tag[attribute] = convert_link(tag[attribute], relative)
    search.append({'title': title, 'url': relative[:-3] + '.html', 'text': soup.get_text(' ', strip=True)})
    navigation = [('docs/Main_Page.html', 'Wiki 首页'), ('INDEX.html', '全部文档'), ('categories/Category_Supported_Devices--1975.html', '支持的芯片'), ('categories/Category_ERIKA_internals--2129.html', 'ERIKA 内核'), ('categories/Category_RT-Druid--2304.html', 'RT-Druid'), ('ASSETS.html', '图片与资源'), ('ARCHIVE.html', '归档说明'), ('NOTICE.html', '署名与许可')]
    nav = ''.join(f'<a href="{prefix}{url}">{label}</a>' for url, label in navigation)
    document = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escaped(title)} · ERIKA Archive</title><link rel="stylesheet" href="{prefix}site.css"><script src="{prefix}site.js" defer></script></head>
<body data-root="{prefix}"><header><a class="brand" href="{prefix}index.html"><span class="logo">E</span> ERIKA <span class="muted">/ Archive</span></a><a href="https://github.com/erika-archive/erika-wiki">GitHub ↗</a></header>
<div class="layout"><aside class="sidebar"><div class="eyebrow">DOCUMENTATION</div><label for="search">搜索归档 / Search</label><input id="search" type="search" placeholder="芯片、配置、API…" autocomplete="off"><p id="search-status" role="status" aria-live="polite"></p><div id="results"></div><nav>{nav}</nav><div class="archive-note">非官方历史归档<br>204 篇正文 · 690 个原始资源<br>Snapshot · November 2026</div></aside>
<main><div class="eyebrow">ERIKA ENTERPRISE & RT-DRUID</div><article>{soup}</article><footer>Unofficial historical archive. Original authorship and rights notices retained. <a href="{prefix}NOTICE.html">Attribution & licensing</a> · <a href="https://github.com/erika-archive/erika-wiki/blob/main/{relative}">View Markdown source</a></footer></main><aside class="toc"><div class="eyebrow">ON THIS PAGE</div>{''.join(toc)}</aside></div></body></html>'''
    target = OUT / (relative[:-3] + '.html')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(document, encoding='utf-8')

shutil.copytree(ROOT / 'assets', OUT / 'assets', dirs_exist_ok=True)
shutil.copyfile(ROOT / 'LICENSE-GFDL-1.2.txt', OUT / 'LICENSE-GFDL-1.2.txt')
for name in ('site.css', 'site.js'):
    shutil.copyfile(ROOT / 'site' / name, OUT / name)
(OUT / 'search.json').write_text(json.dumps(search, ensure_ascii=False), encoding='utf-8')
(OUT / 'index.html').write_text((OUT / 'README.html').read_text(encoding='utf-8'), encoding='utf-8')
(OUT / '.nojekyll').touch()
print(f'Built {len(pages)} searchable pages and copied original local resources.')
