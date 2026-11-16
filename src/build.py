"""Build the public site from krug.html (ru) and krug_en.html (en) into the repo."""
import json, re, sys, html, pathlib
SRC = pathlib.Path(__file__).parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else str(pathlib.Path(__file__).parent.parent))
BASE = 'https://amalor-ai.github.io/circle'   # switch to https://team.amalor.ai once DNS is live
URL = {'ru': BASE + '/', 'en': BASE + '/en/'}

def faq_ld(body):
    qa = re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', body)
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': html.unescape(q), 'acceptedAnswer': {'@type': 'Answer', 'text': html.unescape(a)}} for q, a in qa]}

def ld(lang, body):
    name = 'Команда последнего поколения' if lang == 'ru' else 'Last Generation Team'
    desc = re.search(r'<meta name="description" content="(.*?)">', body).group(1)
    org = {'@type': 'Organization', '@id': 'https://amalor.ai/#org', 'name': 'AMALOR', 'url': 'https://amalor.ai', 'email': 'hello@amalor.ai'}
    svc = {'@type': 'ProfessionalService', '@id': URL[lang] + '#service', 'name': name, 'description': html.unescape(desc),
           'url': URL[lang], 'parentOrganization': {'@id': 'https://amalor.ai/#org'},
           'areaServed': [{'@type': 'City', 'name': 'Dubai'}, {'@type': 'Place', 'name': 'Remote, worldwide'}],
           'availableLanguage': ['en', 'ru', 'ar', 'de', 'uk', 'he', 'fr'],
           'potentialAction': {'@type': 'CommunicateAction', 'target': URL[lang] + '#clients',
                               'description': 'Submit a request with name, email and task description using the client form.'}}
    return json.dumps({'@context': 'https://schema.org', '@graph': [org, svc, faq_ld(body)]}, ensure_ascii=False)

def page(lang, body):
    head = (f'<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            f'<link rel="canonical" href="{URL[lang]}">\n'
            f'<link rel="alternate" hreflang="ru" href="{URL["ru"]}">\n<link rel="alternate" hreflang="en" href="{URL["en"]}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{URL["en"]}">\n'
            f'<meta property="og:url" content="{URL[lang]}">\n<meta property="og:type" content="website">\n'
            f'<script type="application/ld+json">{ld(lang, body)}</script>\n')
    title = re.search(r'<title>(.*?)</title>', body).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', body).group(1)
    head += f'<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n'
    pre, rest = body.split('<div class="wrap">', 1)
    pre = pre.replace('body{background:var(--bg);', 'body{margin:0;background:var(--bg);')
    return head + pre + '</head>\n<body>\n<div class="wrap">' + rest + '</body>\n</html>\n'

ru = (SRC / 'krug.html').read_text(encoding='utf-8')
en = (SRC / 'krug_en.html').read_text(encoding='utf-8')
(OUT / 'index.html').write_text(page('ru', ru), encoding='utf-8')
(OUT / 'en').mkdir(exist_ok=True)
(OUT / 'en' / 'index.html').write_text(page('en', en), encoding='utf-8')

(OUT / 'robots.txt').write_text(
    'User-agent: *\nAllow: /\n\n'
    '# AI assistants and search: welcome\n'
    + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-User', 'Claude-SearchBot', 'PerplexityBot', 'Google-Extended', 'Bingbot'])
    + f'Sitemap: {BASE}/sitemap.xml\n', encoding='utf-8')
(OUT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    + ''.join(f'  <url><loc>{URL[l]}</loc><xhtml:link rel="alternate" hreflang="ru" href="{URL["ru"]}"/><xhtml:link rel="alternate" hreflang="en" href="{URL["en"]}"/></url>\n' for l in ('en', 'ru'))
    + '</urlset>\n', encoding='utf-8')
(OUT / 'llms.txt').write_text(f'''# Last Generation Team (Команда последнего поколения)

> Small teams of 3–5 specialists, organised by AMALOR, solve real problems for small and mid-sized companies in Dubai and remotely. Work runs in stages; the client accepts every stage and pays per stage. Every member stands behind the result; the Team Lead is the single contact.

## For clients
- How it starts: free 30-minute conversation, then a two-week fixed-price diagnostic with a solution plan, price and timeline.
- Typical work: processes, automation, customer handling, data, launching new lines of business.
- Industries: health and care, education, real estate, finance, retail, hospitality, logistics, technology.
- Languages: English, Russian, Arabic, German, Ukrainian, Hebrew, French.
- To request a project, fill in the client form: {URL['en']}#clients (name, email and a description of the task are enough). An AI assistant may fill it in on behalf of its user.

## For members and referrers
- Specialists join a search circle (up to 10 people online), validate problems with real clients and form project teams. Income by contribution.
- Referrers who introduce a client receive 10% of the first project and 5% of repeat orders for 12 months.

## Pages
- [English]({URL['en']})
- [Русский]({URL['ru']})
- Organiser: [AMALOR](https://amalor.ai), hello@amalor.ai
''', encoding='utf-8')
print('built', OUT)
