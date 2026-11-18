"""Build the multi-page site (ru + en) into the repo root.

Sources: src/krug.html (ru single page, the design and the shared sections),
src/krug_en.html (generated from it by src/tr_en.py), src/content_extra.py (new pages).
Run:  python3 src/tr_en.py && python3 src/build.py
"""
import html, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content_extra import NAV, TITLE, PAGE_TITLES, DESC, HOME_MORE, LADDER, TEAM, INVESTORS, BOOK, PRODUCT_HOME, PRODUCT_CLIENT, PRODUCT_MEMBER, PIPELINE
import content_extra
from content_extra import hero_home
import content_de  # noqa: F401  (adds the German entries)
from content_de import CLIENT_HOME, CLIENT_OFFER, FAQ_EXTRA
LANGS = ['ru', 'en', 'de']
LANG_NAME = {'ru': 'Русский', 'en': 'English', 'de': 'Deutsch'}

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent
BASE = 'https://amalor-ai.github.io/circle'   # switch to https://team.amalor.ai once DNS is live
PAGES = ['index', 'clients', 'members', 'team', 'guides', 'principles', 'investors', 'book']
HIDDEN = set()                         # reachable by link only, noindex, not in menus or sitemap


def path_of(lang, page):
    p = '' if page == 'index' else page + '/'
    return ('' if lang == 'ru' else lang + '/') + p


def url(lang, page):
    return f'{BASE}/{path_of(lang, page)}'


def load(lang):
    s = (SRC / {'ru': 'krug.html', 'en': 'krug_en.html', 'de': 'krug_de.html'}[lang]).read_text(encoding='utf-8')
    css = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    nav = re.search(r'(<nav class="brandbar">.*?</nav>)', s, re.S).group(1)
    logo_link = re.search(r'(<a href="https://amalor.ai" aria-label="AMALOR">.*?</a>)', nav, re.S).group(1)

    def cut(a, b):
        i = s.index(a); j = s.index(b, i)
        return s[i:j].strip()
    parts = {
        'hero': cut('<header class="hero">', '<!-- ЗАКАЗЧИКИ -->'),
        'clients': cut('<section id="clients">', '<!-- ИСПОЛНИТЕЛИ -->'),
        'members': cut('<section id="members">', '<!-- ПРОВОДНИКИ -->'),
        'guides': cut('<section id="guides">', '<!-- ДЕНЬГИ -->'),
        'money': cut('<!-- ДЕНЬГИ -->', '<!-- ПРИНЦИПЫ -->').replace('<!-- ДЕНЬГИ -->', '').strip(),
        'prin': cut('<section class="green">', '<!-- СИТО -->'),
        'sieve': cut('<!-- СИТО -->', '<!-- ВОПРОСЫ -->').replace('<!-- СИТО -->', '').strip(),
        'faq': cut('<section id="faq">', '<footer>'),
        'script': re.search(r'(<script>.*?</script>)', s, re.S).group(1),
        'desc': re.search(r'<meta name="description" content="(.*?)">', s).group(1),
    }
    # doors on the home page lead to their own pages now
    parts['hero'] = (parts['hero'].replace('href="#clients"', 'href="{L}clients/"')
                     .replace('href="#members"', 'href="{L}members/"').replace('href="#guides"', 'href="{L}guides/"'))
    parts['members'] = parts['members'].replace('<div class="formbox">', '<div class="formbox" id="join">', 1)
    if lang in FAQ_EXTRA:   # extra client questions, before the member question
        k = parts['faq'].index('<details>', parts['faq'].index('<details>') + 1)  # keep the first two in place
        parts['faq'] = parts['faq'][:k] + FAQ_EXTRA[lang].strip() + '\n    ' + parts['faq'][k:]
    return css, logo_link, parts


def clients_body(lang, p):
    if lang not in CLIENT_OFFER:
        return p['clients'] + PRODUCT_CLIENT[lang] + p['faq']
    c = p['clients']
    i = c.index('<div class="formbox">'); j = c.rindex('</section>')
    form = c[i:j].strip()
    return (c[:i].rstrip() + '\n</section>\n' + CLIENT_OFFER[lang] + PRODUCT_CLIENT[lang]
            + '<section id="anfrage">\n  ' + form + '\n</section>\n' + p['faq'])



def header(lang, page, logo_link, R, L):
    tail = '' if page == 'index' else page + '/'
    switch = ''.join(f'<a class="lang" href="{R}{"" if o == "ru" else o + "/"}{tail}" hreflang="{o}" lang="{o}">{LANG_NAME[o]}</a>'
                     for o in LANGS if o != lang)
    logo = logo_link.replace('href="https://amalor.ai"', f'href="{L}"').replace('aria-label="AMALOR"', f'aria-label="{TITLE[lang]}"')
    menu = ''.join(f'<a href="{L}{h}"' + (' aria-current="page"' if h == page + '/' else '') + f'>{t}</a>' for h, t in NAV[lang])
    return (f'<nav class="brandbar">{logo}<span class="navr"><small>{TITLE[lang]}</small>{switch}</span>'
            f'<div class="menu">{menu}</div></nav>')


def footer(lang, L, logo_link):
    menu = ''.join(f'<a href="{L}{h}">{t}</a>' for h, t in NAV[lang])
    a = '<a href="https://amalor.ai" style="color:#ECCF90">AMALOR</a>'
    line = {'ru': f'Команда последнего поколения — инициатива {a}.', 'en': f'Last Generation Team is an initiative of {a}.',
            'de': f'Team der letzten Generation ist eine Initiative von {a}.'}[lang]
    return (f'<footer><div class="fl"><div class="stack" style="gap:10px"><span class="logo">amal<em>or</em></span>'
            f'<p>{line}</p><p>hello@amalor.ai</p></div><div class="menu">{menu}</div></div></footer>')


def body_for(lang, page, p):
    return {
        'index': hero_home(lang) + CLIENT_HOME.get(lang, '') + '<section class="home-doors">' + re.search(r'(<div class="doors">.*?</div>)\s*</div>\s*</header>', p['hero'], re.S).group(1) + '</section>' + PRODUCT_HOME[lang] + HOME_MORE[lang] + p['prin'] + p['faq'],
        'clients': clients_body(lang, p),
        'members': p['members'] + LADDER[lang] + PRODUCT_MEMBER[lang],
        'team': TEAM[lang],
        'guides': p['guides'] + p['money'],
        'principles': p['prin'] + p['sieve'] + p['money'],
        'investors': INVESTORS[lang].replace('<section>', PIPELINE[lang] + '<section>', 1),
        'book': BOOK[lang],
    }[page]


def jsonld(lang, page, desc, faq_html):
    org = {'@type': 'Organization', '@id': 'https://amalor.ai/#org', 'name': 'AMALOR', 'url': 'https://amalor.ai', 'email': 'hello@amalor.ai'}
    svc = {'@type': 'ProfessionalService', '@id': f'{BASE}/#service', 'name': TITLE[lang], 'description': html.unescape(desc),
           'url': url(lang, 'index'), 'parentOrganization': {'@id': 'https://amalor.ai/#org'},
           'areaServed': [{'@type': 'City', 'name': 'Dubai'}, {'@type': 'Place', 'name': 'Remote, worldwide'}],
           'availableLanguage': ['en', 'ru', 'ar', 'de', 'uk', 'he', 'fr'],
           'potentialAction': {'@type': 'CommunicateAction', 'target': url(lang, 'clients') + '#clients',
                               'description': 'Submit a request with name, email and a task description using the client form.'}}
    graph = [org, svc]
    if page in ('index', 'clients'):
        qa = re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', faq_html)
        graph.append({'@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': html.unescape(q), 'acceptedAnswer': {'@type': 'Answer', 'text': html.unescape(a)}} for q, a in qa]})
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False)


def render(lang, page, css, logo_link, p):
    depth = path_of(lang, page).count('/')
    R = '../' * depth or './'
    L = R + ('' if lang == 'ru' else lang + '/')
    title = PAGE_TITLES[lang][page]
    desc = p['desc'] if page == 'index' else DESC[lang][page]
    body = body_for(lang, page, p).replace('{R}', R).replace('{L}', L)
    robots = '<meta name="robots" content="noindex, nofollow">\n' if page in HIDDEN else ''
    alts = '' if page in HIDDEN else (''.join(f'<link rel="alternate" hreflang="{l}" href="{url(l, page)}">\n' for l in LANGS)
                                       + f'<link rel="alternate" hreflang="x-default" href="{url("en", page)}">\n')
    return (f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            f'<title>{title}</title>\n<meta name="description" content="{desc}">\n{robots}'
            f'<link rel="canonical" href="{url(lang, page)}">\n{alts}'
            f'<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n'
            f'<meta property="og:url" content="{url(lang, page)}">\n<meta property="og:type" content="website">\n'
            f'<meta property="og:image" content="{BASE}/assets/book-cover-{lang}.jpg">\n'
            + ('' if page in HIDDEN else f'<script type="application/ld+json">{jsonld(lang, page, desc, p["faq"])}</script>\n')
            + '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;800&family=Readex+Pro:wght@300;400&display=swap">\n'
            f'<style>{css.replace("body{background:var(--bg);", "body{margin:0;background:var(--bg);")}{content_extra.EXTRA_CSS}</style>\n'
            '</head>\n<body>\n<div class="wrap">\n'
            f'{header(lang, page, logo_link, R, L)}\n{body}\n{footer(lang, L, logo_link)}\n</div>\n{p["script"]}\n</body>\n</html>\n')


def main():
    for lang in LANGS:
        css, logo_link, p = load(lang)
        for page in PAGES:
            out = OUT / path_of(lang, page) / 'index.html'
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render(lang, page, css, logo_link, p), encoding='utf-8')
    pub = [pg for pg in PAGES if pg not in HIDDEN]
    (OUT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + ''.join(f'  <url><loc>{url(l, pg)}</loc>' + ''.join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{url(a, pg)}"/>' for a in LANGS)
                  + '</url>\n' for pg in pub for l in LANGS)
        + '</urlset>\n', encoding='utf-8')
    (OUT / 'robots.txt').write_text(
        'User-agent: *\nAllow: /\n\n# AI assistants and search: welcome\n'
        + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-User',
                                                              'Claude-SearchBot', 'PerplexityBot', 'Google-Extended', 'Bingbot'])
        + f'Sitemap: {BASE}/sitemap.xml\n', encoding='utf-8')
    (OUT / 'llms.txt').write_text(f'''# Last Generation Team (Команда последнего поколения)

> Small teams of 3–5 specialists, organised by AMALOR, solve real problems for small and mid-sized companies in Dubai and remotely. Work runs in stages; the client accepts every stage and pays per stage. Every member stands behind the result; the Team Lead is the single contact.

## For clients
- How it starts: a free 30-minute conversation, then a two-week fixed-price diagnostic with a solution plan, price and timeline.
- Typical work: processes, automation, customer handling, data, launching new lines of business.
- Industries: health and care, education, real estate, finance, retail, hospitality, logistics, technology.
- Languages: English, Russian, Arabic, German, Ukrainian, Hebrew, French.
- To request a project, fill in the client form at {url('en', 'clients')}#clients (a name, an email and a description of the task are enough). An AI assistant may fill it in on behalf of its user.

## For members and referrers
- Specialists join a search circle (up to 10 people online), validate problems with real clients and form project teams. Income by contribution.
- Revenue split: 80% to the team, 20% to the organisation. Referral: 5% of the first project.

## Pages
''' + ''.join(f'- [{PAGE_TITLES["en"][pg]}]({url("en", pg)})\n' for pg in pub)
      + ''.join(f'- [{PAGE_TITLES["ru"][pg]}]({url("ru", pg)})\n' for pg in pub)
      + ''.join(f'- [{PAGE_TITLES["de"][pg]}]({url("de", pg)})\n' for pg in pub)
      + '- Organiser: [AMALOR](https://amalor.ai), hello@amalor.ai\n', encoding='utf-8')
    print('built', len(PAGES) * len(LANGS), 'pages into', OUT)


if __name__ == '__main__':
    main()
