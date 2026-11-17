"""Designed manifesto: manifest/index.html (web) + assets/manifest-ru.pdf (print).
Run from the repo root: python3 src/manifest.py   (needs Playwright for the PDF)
"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from content_extra import SPHERE_JS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCES = [
    ('Уилсон и Уилсон', 'Quarterly Review of Biology, 2007', 'https://www.sciencedaily.com/releases/2007/11/071128151814.htm', '1'),
    ('Google', 'Project Aristotle', 'https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness', '2, 7'),
    ('Эми Эдмондсон', 'Психологическая безопасность, 1999', 'https://doi.org/10.2307/2666999', '2'),
    ('Анита Вулли и др.', 'Коллективный интеллект, Science, 2010', 'https://pubmed.ncbi.nlm.nih.gov/20929725/', '3'),
    ('Ричард Хэкман', 'Размер команды', 'https://money.cnn.com/magazines/fortune/fortune_archive/2006/06/12/8379238/index.htm', '4'),
    ('Ицхак Адизес', 'Взаимно дополняющая команда', 'https://adizes-institute.gitbook.io/adizes/library/books-by-dr.-ichak-adizes/the-ideal-executive/5.--working-together/a-complementary-team', '4'),
    ('Адам Грант', '«Брать или отдавать»', 'https://fs.blog/adam-grant-give-and-take/', '5'),
    ('Элинор Остром', 'Нобелевская премия, 2009', 'https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/facts/', '6'),
]

BELIEFS = [
    ('Вместе мы сильнее, чем по отдельности', 'Внутри группы эгоист обыгрывает альтруиста, но группа альтруистов обыгрывает группу эгоистов — так это сформулировали биологи Уилсон и Уилсон. Мы выбираем быть такой группой.'),
    ('Мы отвечаем друг за друга', 'Застрял один — это задача всех. Сказать «мне тяжело» безопасно. Google изучил 180 своих команд и нашёл именно это на первом месте.'),
    ('Мы равные за одним столом', 'Каждый голос весит одинаково. Ум группы зависит не от самого умного в ней, а от того, как равномерно все говорят и слышат друг друга.'),
    ('Маленькая команда из разных людей', 'Ядро — три–пять человек, и сила одного закрывает слабость другого. Под задачу к ним подключаются специалисты из круга, а выросшая команда делится, а не разрастается.'),
    ('Вклад виден всем', 'Признание — за то, что ты дал, а не за должность. Дающие выигрывают там, где их отдачу видят и защищают.'),
    ('Мы сами управляем общим', 'Команда сама договаривается о правилах, сама следит за ними и сама их улучшает. Так сообщества живут долго.'),
    ('Польза людям — мерило задачи', 'Мы берём только то, что действительно нужно, никому не вредит и за что готовы платить. Каждая задача проходит через сито из семи вопросов.'),
]

SUPPORT = [
    ('Организатор (AMALOR)', 'продажи, договоры, гарантию, метод', '10–20% проекта, долю за сборку продукта'),
    ('Проводники', 'знакомство с тем, у кого есть задача', '10% первого проекта'),
    ('Инвесторы и фонды', 'деньги, опыт, наставничество', 'команды с первым клиентом, долю в продуктах, измеримый социальный эффект'),
    ('Государство и его программы', 'гранты, софинансирование, заказы', 'занятость специалистов, новые компании, интеграцию приезжих'),
    ('Технологические компании и вендоры ИИ', 'кредиты, лицензии и облако на пилот, экспертов', 'новые продукты на своей платформе, подготовленных специалистов, клиентов'),
    ('Общественные организации', 'гранты, своих людей, каналы', 'работающую модель занятости с балансом работы и жизни'),
    ('Сообщества, диаспоры, университеты', 'людей, доверие, методы', 'работу для своих, данные о том, как малые команды работают на деле'),
]

RHYTHM = [
    ('Пн', '30 мин', 'Круг', 'Цель одной фразой. Каждый по очереди называет свою главную задачу и где нужна помощь.'),
    ('Вт–Чт', 'без встреч', 'Работа', 'Короткий отчёт в чате: что сделал, где застрял. Застрявшему помогают.'),
    ('Пт', '45 мин', 'Демо и раунд признания', 'Что сделали и узнали. Каждый называет ценное, что сделал другой.'),
    ('6 недель', '90 мин', 'Большая ретро и пауза', 'Продолжаем, меняем курс или расходимся — решаем вместе.'),
    ('Квартал', '', 'Большой круг', 'Команда подтверждает роли и лидера по сделанному, а не по симпатии.'),
]

CIRCLES = '''<svg viewBox="0 0 760 600" class="rings" role="img" aria-label="Команда в центре, вокруг — ради кого работа и круг поддержки">
<ellipse cx="380" cy="300" rx="350" ry="270" fill="#EFE7D3" stroke="#C9B48A" stroke-dasharray="3 6"/>
<ellipse cx="380" cy="300" rx="225" ry="178" fill="#F7F1E3" stroke="#C9B48A"/>
<ellipse cx="380" cy="300" rx="112" ry="88" fill="#0B3F3C" stroke="#C99A45" stroke-width="3"/>
<text x="380" y="62" class="rl">КРУГ ПОДДЕРЖКИ</text>
<text x="380" y="150" class="rl">РАДИ КОГО РАБОТА</text>
<text x="380" y="292" class="core">Команда</text>
<text x="380" y="316" class="core-s">3–5 человек + ИИ</text>
<text x="380" y="338" class="core-g">почёт · 80% дохода</text>
<g class="it"><text x="210" y="305">Заказчики</text><text x="548" y="305">Пользователи</text><text x="380" y="438">Общество</text>
<text x="128" y="196">Организатор</text><text x="632" y="196">Проводники</text>
<text x="88" y="296">Инвесторы</text><text x="88" y="316">и фонды</text><text x="672" y="305">Государство</text>
<text x="128" y="414">Общественные</text><text x="128" y="434">организации</text>
<text x="632" y="414">Технологические</text><text x="632" y="434">компании</text>
<text x="380" y="530">Сообщества и университеты</text></g>
</svg>'''

TENT = '''<svg class="tent" viewBox="0 0 600 340" role="img" aria-label="Над открытым шатром висит сеть связей; под ним команда за круглым столом">
<defs>
 <linearGradient id="tg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7E7B0"/><stop offset=".4" stop-color="#E2BF74"/><stop offset=".75" stop-color="#C99A45"/><stop offset="1" stop-color="#EDCD82"/></linearGradient>
 <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4D2" stop-opacity=".5"/><stop offset=".35" stop-color="#FFF4D2" stop-opacity=".7"/><stop offset="1" stop-color="#FFF4D2" stop-opacity=".9"/></linearGradient>
 <radialGradient id="tl" cx="50%" cy="78%" r="42%"><stop offset="0" stop-color="#FFE9B0" stop-opacity=".6"/><stop offset=".55" stop-color="#ECCF90" stop-opacity=".14"/><stop offset="1" stop-color="#ECCF90" stop-opacity="0"/></radialGradient>
 <linearGradient id="tab" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7E7B0"/><stop offset="1" stop-color="#C99A45"/></linearGradient>
</defs>
<rect x="80" y="60" width="440" height="270" fill="url(#tl)"/>
<path d="M300 0 L300 250" stroke="url(#beam)" stroke-width="2.2"/><path d="M300 0 L300 250" stroke="#6FB7E6" stroke-width=".9" opacity=".8"/><circle cx="300" cy="248" r="22" fill="#FFF4D2" opacity=".18"/>
<ellipse cx="300" cy="312" rx="230" ry="16" fill="#000" opacity=".2"/>
<g fill="none" stroke="url(#tg)" stroke-linecap="round" stroke-linejoin="round">
 <path d="M168 132 L168 300 M432 132 L432 300" stroke-width="1.6" opacity=".45"/>
 <path d="M70 160 C150 150 230 120 300 64 C370 120 450 150 530 160" stroke-width="3"/>
 <path d="M70 160 C88 172 104 172 118 164 C134 174 150 174 164 166 C180 176 196 176 210 168 C226 177 242 177 256 170 C270 178 286 178 300 171 C314 178 330 178 344 170 C358 177 374 177 390 168 C404 176 420 176 436 166 C450 174 466 174 482 164 C496 172 512 172 530 160" stroke-width="1.8" opacity=".9"/>
 <path d="M300 64 C268 108 236 134 210 150 M300 64 C332 108 364 134 390 150 M300 64 C285 110 270 140 256 160 M300 64 C315 110 330 140 344 160" stroke-width="1" opacity=".5"/>
 <path d="M86 166 L86 304 M514 166 L514 304" stroke-width="2.6"/>
 <path d="M70 160 L34 306 M530 160 L566 306" stroke-width="1" opacity=".5" stroke-dasharray="3 5"/>
</g>
<circle cx="300" cy="62" r="4" fill="url(#tg)"/>
<g fill="url(#tg)">
 <path transform="translate(244 262)" opacity=".85" d="M-18 0 C-21 -28 -15 -50 -5 -60 C0 -67 10 -68 13 -60 C15 -54 11 -50 12 -43 C19 -32 22 -14 20 0 Z"/>
 <path transform="translate(356 262)" opacity=".85" d="M18 0 C21 -28 15 -50 5 -60 C0 -67 -10 -68 -13 -60 C-15 -54 -11 -50 -12 -43 C-19 -32 -22 -14 -20 0 Z"/>
 <path transform="translate(300 252)" opacity=".75" d="M-17 0 C-20 -30 -13 -54 0 -63 C13 -54 20 -30 17 0 Z"/>
</g>
<ellipse cx="300" cy="266" rx="92" ry="20" fill="url(#tab)" opacity=".95"/>
<ellipse cx="300" cy="264" rx="84" ry="15" fill="#FFF4D2" opacity=".35"/>
<path d="M208 268 C210 282 250 290 300 290 C350 290 390 282 392 268" fill="none" stroke="#B98A34" stroke-width="5" opacity=".85"/>
<g fill="url(#tg)">
 <path transform="translate(206 296)" d="M-18 0 C-21 -28 -15 -50 -5 -60 C0 -67 10 -68 13 -60 C15 -54 11 -50 12 -43 C19 -32 22 -14 20 0 Z"/>
 <path transform="translate(394 296)" d="M18 0 C21 -28 15 -50 5 -60 C0 -67 -10 -68 -13 -60 C-15 -54 -11 -50 -12 -43 C-19 -32 -22 -14 -20 0 Z"/>
</g>
<path d="M120 306 L480 306" stroke="url(#tg)" stroke-width="1.2" opacity=".55"/>
</svg>'''

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;')

def build_html(for_pdf=False):
    font = '../assets/fonts/Manrope.ttf'
    beliefs = ''.join(f'<li><span class="n">{i+1}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for i, (t, d) in enumerate(BELIEFS))
    support = ''.join(f'<tr><th>{esc(a)}</th><td>{esc(b)}</td><td>{esc(c)}</td></tr>' for a, b, c in SUPPORT)
    rhythm = ''.join(f'<li><div class="when"><b>{w}</b><span>{d}</span></div><div><h4>{esc(t)}</h4><p>{esc(p)}</p></div></li>' for w, d, t, p in RHYTHM)
    sources = ''.join(f'<li><b>{esc(a)}</b>, <a href="{u}">{esc(t)}</a><span>принцип {n}</span></li>' for a, t, u, n in SOURCES)
    web_bar = '' if for_pdf else '''<nav class="topbar"><a href="../" class="home">← amalor · Команда последнего поколения</a><a class="dl" href="../assets/manifest-ru.pdf" download>Скачать PDF</a></nav>'''
    return f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Манифест · Команда последнего поколения</title>
<meta name="description" content="Манифест команды последнего поколения: в центре — команда, которая делает работу; вокруг — те, ради кого работа, и круг поддержки. Почёт и 80% дохода — тем, кто делает.">
<link rel="icon" href="../assets/favicon.svg">
<style>
@font-face{{font-family:"Manrope";src:url("{font}") format("truetype");font-weight:200 800;font-display:swap}}
:root{{--bg:#FBF7EE;--paper:#FFFDF8;--ink:#0B2F2D;--soft:#4A6563;--line:#E4DAC4;--deep:#083C3A;--brand:#0E6B64;--gold:#C99A45;--gold2:#ECCF90;
--gg:linear-gradient(135deg,#F7E7B0,#E2BF74,#C99A45,#EDCD82)}}
*{{box-sizing:border-box}}
html,body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Manrope",system-ui,sans-serif;font-size:17px;line-height:1.6;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
a{{color:var(--brand)}}
h1,h2,h3,h4{{margin:0;line-height:1.15;text-wrap:balance}}
p{{margin:0}}
.sheet{{position:relative;max-width:900px;margin:0 auto;padding:72px 64px}}
.eyebrow{{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:14px}}
h2{{font-size:40px;font-weight:800;letter-spacing:-.02em;margin-bottom:18px}}
.lead{{font-size:20px;color:var(--soft);max-width:60ch}}
/* topbar (web only) */
.topbar{{position:sticky;top:0;z-index:5;display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 24px;background:rgba(8,60,58,.94);backdrop-filter:blur(6px)}}
.topbar a{{color:#C9E4E2;text-decoration:none;font-weight:600;font-size:15px}}
.topbar .dl{{background:var(--gg);color:#1B1405;padding:8px 16px;border-radius:999px}}
/* cover */
.cover{{background:radial-gradient(ellipse 60% 50% at 50% 42%,rgba(27,156,147,.45),rgba(27,156,147,0) 70%),var(--deep);color:#fff;min-height:100vh;display:flex;flex-direction:column;justify-content:space-between;padding:56px 64px}}
.cover .brand{{font-size:15px;letter-spacing:.3em;text-transform:uppercase;color:var(--gold2);font-weight:600}}
.cover .sphere{{display:block;width:min(340px,70%);aspect-ratio:1/1;margin:0 auto -70px;position:relative;z-index:1}}.cover .tent{{display:block;width:min(560px,96%);height:auto;margin:0 auto}}
.cover h1{{font-size:64px;font-weight:800;letter-spacing:-.03em;line-height:1}}
.cover .kind{{font-size:22px;color:var(--gold2);font-weight:600;margin-top:12px;letter-spacing:.04em}}
.cover .q{{font-style:italic;color:#9DC3BF;font-size:16px;margin-top:22px;max-width:46ch}}
/* intro */
.intro .big{{font-size:28px;line-height:1.35;font-weight:600;letter-spacing:-.01em}}
.intro .cols{{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:28px;color:var(--soft)}}
.intro .center{{margin-top:34px;padding:26px 30px;border-radius:18px;background:var(--deep);color:#fff;font-size:20px;line-height:1.45}}
.intro .center b{{color:var(--gold2)}}
/* beliefs */
.beliefs ol{{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.beliefs li{{position:relative;background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:22px 22px 22px 70px;break-inside:avoid}}
.beliefs li:last-child{{grid-column:1/-1}}
.beliefs .n{{position:absolute;left:20px;top:20px;width:36px;height:36px;border-radius:50%;background:var(--gg);display:grid;place-items:center;font-weight:800;color:#1B1405}}
.beliefs h3{{font-size:19px;margin-bottom:6px}}
.beliefs p{{font-size:15px;color:var(--soft)}}
/* circles */
.rings{{width:100%;height:auto;margin:22px 0 8px}}
.rings .rl{{font-size:14px;letter-spacing:.2em;font-weight:700;fill:#8C7440;text-anchor:middle}}
.rings .core{{font-size:26px;font-weight:800;fill:#F7E7B0;text-anchor:middle}}
.rings .core-s{{font-size:14px;fill:#C9E4E2;text-anchor:middle}}
.rings .core-g{{font-size:14px;font-weight:700;fill:#ECCF90;text-anchor:middle}}
.rings .it text{{font-size:15px;fill:#0B2F2D;text-anchor:middle;font-weight:500}}
table{{width:100%;border-collapse:collapse;font-size:14.5px;margin-top:18px}}
th,td{{text-align:left;vertical-align:top;padding:11px 12px;border-bottom:1px solid var(--line)}}
thead th{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);border-bottom:2px solid var(--gold2)}}
tbody th{{font-weight:700;width:30%}}
tr{{break-inside:avoid}}
.note{{font-size:13px;color:var(--soft);margin-top:12px}}
/* honor */
.honor{{background:var(--deep);color:#fff}}
.honor h2{{color:#fff}} .honor .lead{{color:#C9E4E2}}
.split{{margin-top:30px;display:flex;flex-direction:column;gap:22px}}
.split .case b{{display:block;font-size:15px;color:#C9E4E2;margin-bottom:8px;font-weight:600}}
.bar{{display:flex;gap:4px;height:58px;border-radius:12px;overflow:hidden;font-weight:700}}
.bar div{{display:flex;align-items:center;justify-content:center;background:rgba(201,228,226,.14);color:#C9E4E2;font-size:15px;white-space:nowrap}}
.bar .team{{background:var(--gg);color:#0B2F2D;justify-content:flex-start;padding-left:22px;font-size:20px}}
.big4{{margin-top:36px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}
.big4 div{{border-top:1px solid rgba(201,228,226,.25);padding-top:14px}}
.big4 h4{{color:var(--gold2);font-size:19px;margin-bottom:6px}}
.big4 p{{font-size:14px;color:#A9CBC7}}
/* rhythm */
.rhythm ol{{list-style:none;margin:26px 0 0;padding:0;position:relative}}
.rhythm ol::before{{content:"";position:absolute;left:83px;top:10px;bottom:10px;width:2px;background:var(--line)}}
.rhythm li{{display:grid;grid-template-columns:100px 1fr;gap:26px;padding:12px 0;break-inside:avoid;position:relative}}
.rhythm li::before{{content:"";position:absolute;left:77px;top:22px;width:14px;height:14px;border-radius:50%;background:var(--gg);box-shadow:0 0 0 4px var(--bg)}}
.rhythm .when{{text-align:right;padding-right:28px}}
.rhythm .when b{{display:block;font-size:17px}} .rhythm .when span{{font-size:13px;color:var(--soft)}}
.rhythm h4{{font-size:18px;margin-bottom:2px}} .rhythm p{{color:var(--soft);font-size:15.5px}}
.pact{{margin-top:22px;padding:20px 24px;border-left:4px solid var(--gold);background:var(--paper);border-radius:0 14px 14px 0;font-size:15.5px}}
/* product path */
.path{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:28px;counter-reset:s}}
.path div{{position:relative;background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:18px}}
.path div:last-child{{background:var(--gg);border-color:transparent}}
.path i{{font-style:normal;font-size:12px;letter-spacing:.16em;color:var(--gold);font-weight:800}}
.path div:last-child i{{color:#5B4314}}
.path h4{{font-size:19px;margin:6px 0 4px}} .path p{{font-size:14px;color:var(--soft)}} .path div:last-child p{{color:#3A2C0C}}
.owners{{margin-top:22px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}
.owners div{{font-size:14.5px;color:var(--soft)}} .owners b{{display:block;color:var(--ink);font-size:16px}}
/* invitation */
.invite{{background:radial-gradient(ellipse 60% 60% at 80% 20%,rgba(27,156,147,.4),rgba(27,156,147,0) 70%),var(--deep);color:#fff}}
.invite h2{{color:#fff}}
.inv{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:24px}}
.inv div{{border:1px solid rgba(236,207,144,.3);border-radius:16px;padding:20px;break-inside:avoid}}
.inv h4{{color:var(--gold2);font-size:18px;margin-bottom:8px}} .inv p{{color:#C9E4E2;font-size:15px}}
.closing{{margin-top:44px;text-align:center}}
.closing p{{font-size:30px;font-weight:800;line-height:1.25;letter-spacing:-.01em}}
.closing span{{display:block;margin-top:14px;color:var(--gold2);font-weight:600}}
/* sources */
.src p{{color:var(--soft)}}
.src ul{{list-style:none;padding:0;margin:20px 0 0;columns:2;column-gap:28px}}
.src li{{break-inside:avoid;padding:8px 0;border-bottom:1px solid var(--line);font-size:14.5px}}
.src li span{{display:block;font-size:12px;color:var(--soft)}}
footer.end{{text-align:center;font-size:13px;color:var(--soft);padding:26px}}
@media (max-width:720px){{.sheet,.cover{{padding:44px 20px}}.cover h1{{font-size:42px}}h2{{font-size:30px}}
 .intro .cols,.beliefs ol,.inv{{grid-template-columns:1fr}}.big4,.path,.owners{{grid-template-columns:1fr 1fr}}.src ul{{columns:1}}
 .intro .big{{font-size:22px}}.rings .it text{{font-size:17px}}.bar .team{{font-size:15px;padding-left:12px}}
 table,thead,tbody,tr,th,td{{display:block}}thead{{display:none}}tbody th{{width:auto;border:0;padding-bottom:0}}td{{border:0;padding-top:2px}}tr{{border-bottom:1px solid var(--line);padding:6px 0}}}}
/* blue thread */
.bar{{box-shadow:0 0 0 1.5px #6FB7E6}}.topbar .dl{{box-shadow:0 0 0 1.5px #6FB7E6}}
.big4 div{{border:1px solid rgba(111,183,230,.55);border-radius:14px;padding:14px}}
.beliefs .n{{box-shadow:0 0 0 1.5px #6FB7E6}}.path div:last-child{{box-shadow:0 0 0 1.5px #6FB7E6}}
.intro .center{{box-shadow:inset 0 0 0 1.5px #6FB7E6}}
@page{{size:A4;margin:0}}
@media print{{.topbar{{display:none}}.cover,.page{{height:297mm;overflow:hidden}}.page{{break-before:page}}.sheet{{max-width:none;padding:22mm 20mm}}
 footer.end{{display:none}}.beliefs ol{{gap:10px;margin-top:18px}}.beliefs li{{padding:14px 16px 14px 60px}}.beliefs .n{{left:16px;top:14px;width:32px;height:32px}}
 .beliefs h3{{font-size:16.5px}}.beliefs p{{font-size:13.5px;line-height:1.5}}.intro .big{{font-size:32px}}.intro .cols{{font-size:18px}}
 .path{{margin-top:36px}}.path div{{padding:22px;min-height:170px}}.owners{{margin-top:34px}}.product .lead{{font-size:21px}}}}
</style></head><body>
{web_bar}
<section class="cover">
  <div class="brand">amalor</div>
  <canvas id="sphere" class="sphere" aria-hidden="true"></canvas>{TENT}
  <div><h1>Команда последнего<br>поколения</h1><div class="kind">Манифест</div>
  <p class="q">«Связку тростника не сломать разом. По одной тростинке её переломит и ребёнок»</p></div>
</section>

<section class="sheet intro page">
  <div class="eyebrow">Связка тростника</div>
  <p class="big">Мы живём во время, когда один человек с ноутбуком и искусственным интеллектом может больше, чем целый отдел двадцать лет назад. И всё же один он уязвим.</p>
  <div class="cols"><p>Один продаёт часы, один выгорает, один не дотягивается до большой задачи.</p>
  <p>Мы собираем таких людей в связки. Три, четыре, пять специалистов — и рядом с ними их ИИ-агенты. Они берут задачу, которая нужна людям, и доводят её до результата, этап за этапом, отвечая друг за друга.</p></div>
  <div class="center"><b>Это и есть команда последнего поколения.</b> Она в центре всего, что мы делаем. Всё остальное — заказчики, инвесторы, партнёры, организатор — стоит вокруг неё кругами. И почёт с достойной оплатой полагаются тем, кто делает работу.</div>
</section>

<section class="sheet beliefs page">
  <div class="eyebrow">Во что мы верим</div>
  <h2>Семь убеждений</h2>
  <p class="lead">Каждое мы проверяем делом, и каждое независимо подтверждают те, кто изучает людей и команды.</p>
  <ol>{beliefs}</ol>
</section>

<section class="sheet circles page">
  <div class="eyebrow">Круги</div>
  <h2>В центре — команда. Все круги служат ей</h2>
  <p class="lead">Вокруг команды два круга: те, ради кого работа, и те, кто помогает ей сложиться, работать и расти.</p>
  {CIRCLES}
</section>

<section class="sheet circles page">
  <div class="eyebrow">Круг поддержки</div>
  <h2>Кто помогает и что получает</h2>
  <p class="lead">Каждый в круге поддержки вносит своё и получает то, что ему важно, — не всегда деньги.</p>
  <table><thead><tr><th>Круг поддержки</th><th>Вносит</th><th>Получает</th></tr></thead><tbody>{support}</tbody></table>
</section>

<section class="sheet honor page">
  <div class="eyebrow">Почёт и достойная оплата</div>
  <h2>80 центов из каждого доллара — команде. Всегда</h2>
  <p class="lead">Это не щедрость, а структура: круги существуют, чтобы служить центру, а не кормиться от него. Пример — проект на $100 000.</p>
  <div class="split">
    <div class="case"><b>Заказчика привёл проводник</b><div class="bar"><div class="team" style="flex:80">Команда · $80 000</div><div style="flex:10">$10 000</div><div style="flex:10">$10 000</div></div></div>
    <div class="case"><b>Заказчика нашли мы сами</b><div class="bar"><div class="team" style="flex:80">Команда · $80 000</div><div style="flex:20">$20 000</div></div></div>
    <p class="note" style="color:#A9CBC7">Серые доли — организатор (продажи, договор, юрист, гарантия) и проводник (знакомство). Без проводника его доля уходит организатору, доля команды не меняется. В команде из четырёх это по $20 000 каждому за проект: доход команды делится поровну. Команда сама себя собирает и сама подтверждает свой состав.</p>
  </div>
  <div class="big4">
    <div><h4>Признание</h4><p>Каждую неделю каждый вслух называет ценное, что сделал другой.</p></div>
    <div><h4>Голос</h4><p>Команда сама решает, как работать, и сама подтверждает своих лидеров.</p></div>
    <div><h4>Доля в будущем</h4><p>Если решение вырастет в продукт, те, кто его сделал, — его совладельцы.</p></div>
    <div><h4>Имя</h4><p>Результат подписан именами тех, кто его сделал.</p></div>
  </div>
</section>

<section class="sheet rhythm page">
  <div class="eyebrow">Как живёт команда</div>
  <h2>Три часа встреч в неделю</h2>
  <p class="lead">Этого хватает, чтобы быть командой, и можно совмещать с основной работой.</p>
  <ol>{rhythm}</ol>
  <p class="pact"><b>Договор команды.</b> В первый день команда подписывает его: отвечаем вместе, о товарищах говорим ценное, решаем по согласию, в споре сначала пересказываем позицию другого. Перечитываем на каждой большой ретро.</p>
</section>

<section class="sheet product page">
  <div class="eyebrow">От задачи к продукту</div>
  <h2>Из подрядчика — в совладельцы</h2>
  <p class="lead">Иногда задача одной компании оказывается задачей целой отрасли. Тогда решение становится продуктом.</p>
  <div class="path"><div><i>01</i><h4>Проблема</h4><p>Важная людям задача одного заказчика. Решаем по этапам, с приёмкой.</p></div>
  <div><i>02</i><h4>Пилот</h4><p>Проверяем у других компаний той же отрасли.</p></div>
  <div><i>03</i><h4>Проект</h4><p>Решение становится продуктом: лицензии для отрасли.</p></div>
  <div><i>04</i><h4>Стартап</h4><p>Инвесторы входят, когда спрос уже доказан.</p></div></div>
  <div class="owners"><div><b>Команда</b>доля за труд — больше всего у тех, кто сделал основную работу</div><div><b>Заказчик-партнёр</b>бесплатная лицензия и доход от лицензий, проданных другим</div><div><b>Организатор</b>доля за сборку и запуск</div><div><b>Инвестор</b>доля за деньги на рост</div></div>
  <p class="note">Размеры долей и права на решение закрепим с юристом до первого такого продукта.</p>
</section>

<section class="sheet invite page">
  <div class="eyebrow">Приглашение</div>
  <h2>Каждому кругу — своё слово</h2>
  <div class="inv">
    <div><h4>Если ты специалист</h4><p>и устал продавать свои часы в одиночку — приходи в центр. Здесь тебя подхватят, когда тяжело, заплатят достойно и назовут по имени за то, что ты сделал.</p></div>
    <div><h4>Если у вас есть задача</h4><p>приносите её. Сплочённая команда проведёт её по этапам, а платите вы только за принятое. А если задача нужна целой отрасли, вы можете стать совладельцем продукта.</p></div>
    <div><h4>Если вы знаете, у кого есть задача</h4><p>познакомьте нас. Одно знакомство может дать работу целой команде, а вам — 10% первого проекта.</p></div>
    <div><h4>Если вы инвестор, фонд, компания или государство</h4><p>станьте кругом поддержки. Вы вкладываете не в идею, а в людей, которые уже доказали, что умеют работать вместе и что их работа нужна.</p></div>
  </div>
  <div class="closing"><p>По одной тростинке мы ломаемся.<br>Вместе — нет.</p><span>hello@amalor.ai · amalor-ai.github.io/circle</span></div>
</section>

<section class="sheet src page">
  <div class="eyebrow">Исток и источники</div>
  <h2>Откуда эти мысли</h2>
  <p>Идея команды выросла из текстов Бааль Сулама («Поручительство», «Мир»), Рабаша (статьи о группе, в том числе «Цель общества») и Михаэля Лайтмана о связи между людьми. К тем же выводам независимо пришли современные исследователи:</p>
  <ul>{sources}</ul>
</section>
<footer class="end">Команда последнего поколения · AMALOR · 2026</footer>
{SPHERE_JS}
</body></html>'''

def main():
    os.makedirs(os.path.join(ROOT, 'manifest'), exist_ok=True)
    open(os.path.join(ROOT, 'manifest', 'index.html'), 'w', encoding='utf-8').write(build_html(False))
    tmp = os.path.join(ROOT, 'manifest', '_print.html')
    open(tmp, 'w', encoding='utf-8').write(build_html(True))
    js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:794,height:1123}}}});
await p.emulateMedia({{reducedMotion:'reduce'}});await p.goto('file://{tmp}');await p.waitForTimeout(800);
await p.pdf({{path:'{os.path.join(ROOT,'assets','manifest-ru.pdf')}',format:'A4',printBackground:true,preferCSSPageSize:true}});await b.close()}})()"""
    subprocess.run(['node', '-e', js], check=True)
    os.remove(tmp)
    print('manifest page + PDF written')

if __name__ == '__main__':
    main()
