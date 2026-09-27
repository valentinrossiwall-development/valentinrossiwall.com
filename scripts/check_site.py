"""Dependency-free checks for static pages, local links, metadata and sitemap."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://valentinrossiwall.com/'
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.stack, self.ids, self.refs = path, [], set(), []
        self.h1 = self.main = 0
        self.title = self.description = self.canonical = None
        self.schema = []
        self.capture = None
        self.buffer = ''
        self.feed(path.read_text())
        self.close()
        if self.stack:
            errors.append(f'{path.name}: unclosed tags {self.stack}')

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path.name}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        for key in ['href', 'src']:
            if key in attrs: self.refs.append(attrs[key])
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = attrs.get('content')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        if tag == 'title' or (tag == 'script' and attrs.get('type') == 'application/ld+json'):
            self.capture, self.buffer = tag, ''

    def handle_data(self, data):
        if self.capture: self.buffer += data

    def handle_endtag(self, tag):
        if self.capture == tag:
            if tag == 'title': self.title = self.buffer
            else:
                try: self.schema.append(json.loads(self.buffer))
                except ValueError as ex: errors.append(f'{self.path.name}: JSON-LD {ex}')
            self.capture = None
        if not self.stack or self.stack[-1] != tag:
            errors.append(f'{self.path.name}: unexpected closing tag {tag}')
        else: self.stack.pop()

pages = {p.resolve(): Page(p) for p in ROOT.rglob('*.html') if '.git' not in p.parts}
for path, page in pages.items():
    if page.h1 != 1 or page.main != 1:
        errors.append(f'{path.name}: expected exactly one h1 and main')
    if not page.title or not page.canonical:
        errors.append(f'{path.name}: missing title or canonical')
    alias = path.name == 'unternehmertum.html'
    if not alias and (not page.description or not page.schema):
        errors.append(f'{path.name}: missing description or JSON-LD')
    expected = BASE + ('' if path.name == 'index.html' else path.relative_to(ROOT).as_posix())
    if not alias and page.canonical != expected:
        errors.append(f'{path.name}: incorrect canonical')
    for ref in page.refs:
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc: continue
        target = (ROOT / unquote(parsed.path.lstrip('/')) if parsed.path.startswith('/') else path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if target.is_dir(): target /= 'index.html'
        if not target.exists(): errors.append(f'{path.name}: broken link {ref}')
        if parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f'{path.name}: missing fragment {ref}')

sitemap = ET.parse(ROOT / 'sitemap.xml')
locations = [el.text for el in sitemap.findall('.//{*}loc')]
for loc in locations:
    if not loc.startswith(BASE): errors.append(f'Noncanonical sitemap URL: {loc}')
    target = (ROOT / (urlsplit(loc).path.lstrip('/') or 'index.html')).resolve()
    if target not in pages: errors.append(f'Missing sitemap page: {loc}')
for path, page in pages.items():
    if path.name not in ['unternehmertum.html'] and page.canonical not in locations:
        errors.append(f'{path.name}: missing from sitemap')
if BASE + 'sitemap.xml' not in (ROOT / 'robots.txt').read_text():
    errors.append('robots.txt: missing canonical sitemap')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'OK: {len(pages)} HTML pages, local links and fragments, JSON-LD, metadata, {len(locations)} sitemap URLs.')
