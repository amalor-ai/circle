"""2026-11-19: one site for the whole model.

- The client page takes over the sales page that was on www.amalor.ai/de/eigene-software/ (that address now
  redirects here): own software -> startup -> industry customers -> cooperative.
- The path everywhere: Diagnostic -> Own software -> Startup -> Industry customers -> Cooperative.
- No "circle" any more (Kreis / круг / circle): network, sessions.
- No location: the teams work remotely; what matters is the language.

Imported by build.py after content_extra and content_de, so it overrides them.
"""
from content_extra import CIRCLES_TXT, PRODUCT_HOME, INVESTORS

BOOKING = {'de': 'https://www.amalor.ai/de/termin/'}
PHONE = '+491636304313'
WA = {'de': 'https://wa.me/491636304313?text=Hallo%20Herr%20Mikhalev%2C%20',
      'en': 'https://wa.me/491636304313?text=Hello%20Igor%2C%20',
      'ru': 'https://wa.me/491636304313?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%2C%20%D0%98%D0%B3%D0%BE%D1%80%D1%8C%2C%20'}
LINKEDIN = 'https://www.linkedin.com/in/igor-mi'

# ---------- the path on the home page ----------
PATH = {
    'de': (['Diagnose', 'Eigene Software', 'Startup', 'Kunden der Branche', 'Genossenschaft'],
           'Jeder Schritt baut auf dem vorigen auf, keiner ist Pflicht. Im Startup halten Auftraggeber und Team Anteile nach '
           'ihrem Beitrag. Wird die Lösung zum Standard der Branche, kann eine Genossenschaft der Unternehmen Mehrheitseigentümerin '
           'werden – Gründer und Team behalten ihre Anteile.'),
    'en': (['Diagnostic', 'Your own software', 'Startup', 'Industry customers', 'Cooperative'],
           'Each step builds on the one before, none is required. In the startup, the client and the team hold shares according '
           'to their contribution. If the solution becomes the industry standard, a cooperative of the companies can become its '
           'majority owner – the founders and the team keep their shares.'),
    'ru': (['Диагностика', 'Своё ПО', 'Стартап', 'Клиенты отрасли', 'Кооператив'],
           'Каждый шаг опирается на предыдущий, ни один не обязателен. В стартапе у заказчика и команды доли по вкладу. Если '
           'решение становится стандартом отрасли, его основным владельцем может стать кооператив компаний отрасли — основатели '
           'и команда сохраняют свои доли.'),
}
LEGEND = {'de': ('Netzwerk der Unterstützung', 'Verbindungen zwischen den Teams'),
          'en': ('network of support', 'links between the teams'),
          'ru': ('сеть поддержки', 'связи между командами')}
for _l in CIRCLES_TXT:
    CIRCLES_TXT[_l]['path'], CIRCLES_TXT[_l]['path_note'] = PATH[_l]
    CIRCLES_TXT[_l]['support'], CIRCLES_TXT[_l]['links'] = LEGEND[_l]

# ---------- "from a task to a product": the cooperative as the last step ----------
_COOP_TILE = {'de': '<li><b>Genossenschaft</b><span>die Branche wird Mitbesitzerin</span></li>',
              'en': '<li><b>Cooperative</b><span>the industry becomes a co-owner</span></li>',
              'ru': '<li><b>Кооператив</b><span>отрасль становится совладельцем</span></li>'}
_INV_OLD = {'de': '<div><b>Investoren</b><span>steigen ein, wenn das Produkt Nachfrage bewiesen hat</span></div>',
            'en': '<div><b>Investors</b><span>join once the product has proven demand</span></div>',
            'ru': '<div><b>Инвесторы</b><span>входят, когда продукт доказал спрос</span></div>'}
_INV_NEW = {'de': '<div><b>Investoren</b><span>steigen ein, wenn das Produkt Nachfrage bewiesen hat; Ausstieg über die Genossenschaft</span></div>',
            'en': '<div><b>Investors</b><span>join once the product has proven demand; exit through the cooperative</span></div>',
            'ru': '<div><b>Инвесторы</b><span>входят, когда продукт доказал спрос; выход — через кооператив</span></div>'}
for _l in PRODUCT_HOME:
    s = PRODUCT_HOME[_l]
    assert '</ol>' in s and _INV_OLD[_l] in s, _l
    PRODUCT_HOME[_l] = s.replace('</ol>', '  ' + _COOP_TILE[_l] + '\n  </ol>', 1).replace(_INV_OLD[_l], _INV_NEW[_l])

# ---------- investors: the exit ----------
_EXIT = {
    'de': ('<li><b>Daten</b>', '<li><b>Ein klarer Ausstieg</b><span>Wird ein Produkt zum Standard seiner Branche, kann die '
           'Genossenschaft der Unternehmen die Anteile übernehmen – ein Exit, der zur Idee passt.</span></li>\n    <li><b>Daten</b>'),
    'en': ('<li><b>Data</b>', '<li><b>A clear exit</b><span>When a product becomes the standard of its industry, the companies’ '
           'cooperative can take over the shares – an exit that fits the idea.</span></li>\n    <li><b>Data</b>'),
    'ru': ('<li><b>Данные</b>', '<li><b>Понятный выход</b><span>Когда продукт становится стандартом отрасли, кооператив компаний '
           'может выкупить доли — выход, который соответствует самой идее.</span></li>\n    <li><b>Данные</b>'),
}
for _l, (a, b) in _EXIT.items():
    assert a in INVESTORS[_l], _l
    INVESTORS[_l] = INVESTORS[_l].replace(a, b, 1)


# ---------- the client page ----------
T = {
'de': dict(
    eyebrow='Für Auftraggeber',
    h1='Ihre eigene Software. <span class="gold">Gebaut von Menschen, denen sie mitgehört.</span>',
    lead='Ein festes Team aus 3–5 Fachleuten plus KI baut Software, Automatisierung und neue Abläufe für Ihr Unternehmen. '
         'Bezahlt wird nur, was Sie abgenommen haben. Und hat Ihre ganze Branche dieselbe Aufgabe, wird aus Ihrer Lösung ein Produkt – '
         'mit Ihnen als Mitgründer.',
    cta1='Gespräch vereinbaren', cta2='So läuft es ab',
    byline='80 % des Budgets beim Team · 0 € für nicht abgenommene Etappen · 2 Wochen Diagnose zum Festpreis',
    w_eyebrow='Die Idee', w_h2='Software, an deren Erfolg alle Beteiligten teilhaben',
    w_lead='Gute Software entsteht dort, wo die Menschen, die sie bauen, mit dem Ergebnis verbunden sind. Darum gehen 80 % Ihres '
           'Budgets direkt an das Team – und wer möchte, wird gemeinsam mit dem Team Miteigentümer der Lösung.',
    c1='Sicherheit für Sie', c1s='was Sie bekommen',
    c1l=['Ein fester Preis für jede Etappe, vorab vereinbart.', 'Bezahlt wird, was Sie abgenommen haben.',
         'Ein Vertrag und eine feste Ansprechperson.', 'Fällt jemand aus, sorgt AMALOR für Ersatz.'],
    c2='Ein Team, das bleibt', c2s='was das Team antreibt',
    c2l=['80 % des Budgets für die Menschen, die Ihre Lösung bauen.', 'Ein Anteil an der Lösung, wenn daraus ein Produkt wird.',
         'Der eigene Name am Ergebnis.', 'Dasselbe Team betreut und entwickelt Ihre Lösung weiter.'],
    rule='<b>Gemeinsames Eigentum verbindet.</b> Wer an einer Lösung beteiligt ist, denkt über die Abnahme hinaus – an die Menschen, '
         'die sie täglich nutzen, und an die nächste Version.',
    a_eyebrow='So arbeiten wir', a_h2='Erst verstehen, dann bauen – Etappe für Etappe',
    a_lead='Nach jedem Schritt entscheiden Sie neu: weiter, anpassen oder aufhören.',
    steps=[('kostenlos', 'Gespräch', '30 Minuten. Wir hören zu, verstehen Ihr Anliegen und sagen offen, ob wir helfen können.'),
           ('ca. 2 Wochen', 'Diagnose', 'Festpreis. Lösungsplan, Etappen mit Abnahmekriterien, Preis und Termin.'),
           ('Festpreis je Etappe', 'Erste Version', 'Das Team baut die erste nutzbare Lösung für Ihr Unternehmen. Jeden Freitag sichtbare Ergebnisse.'),
           ('laufend', 'Betrieb', 'Dasselbe Team betreut und entwickelt weiter – zum Monatspreis.')],
    g_eyebrow='Zwei Wege',
    v_eyebrow='Die Vision', v_h2='Zuerst die beste Software für Ihr Unternehmen. Dann für Ihre Branche.',
    v_lead='Unternehmen einer Branche unterscheiden sich in ihrem Angebot, nicht in ihrer Verwaltungssoftware. Darum lohnt es sich, '
           'solche Software gemeinsam zu bauen. So ist DATEV entstanden: Steuerberater haben ihre Software zusammen aufgebaut und '
           'besitzen sie bis heute als Genossenschaft. Wer den ersten Schritt geht, prägt den Standard für alle. Jeder Schritt baut auf '
           'dem vorigen auf, keiner ist Pflicht.',
    vsteps=[('Diagnose', 'zwei Wochen, Festpreis'), ('Eigene Software', 'für Ihr Unternehmen gebaut, im echten Einsatz bewährt'),
            ('Startup', 'Sie und das Team gründen gemeinsam – mit eigenem Namen'),
            ('Kunden der Branche', 'andere Unternehmen nutzen die Lösung, Daten streng getrennt'),
            ('Genossenschaft', 'die Branche wird Mitbesitzerin der Software')],
    o_h3='Wenn die Branche einsteigt',
    owners=[('Unternehmen der Branche', 'zeichnen Anteile an der Genossenschaft: Stimmrecht und günstigere Lizenzen'),
            ('Genossenschaft', 'wird Mehrheitseigentümerin des Startups – die Software gehört denen, die sie täglich nutzen'),
            ('Sie als Gründer', 'behalten Gründeranteile, die kostenlose Nutzung und einen Sitz im Aufsichtsrat'),
            ('Das Team', 'behält seine Anteile und entwickelt die Software weiter')],
    v_rule='<b>Wer an alle denkt, bekommt das Beste.</b> Der erste Auftraggeber setzt den Standard seiner Branche – und bekommt die '
           'Lösung, die genau für ihn gebaut wurde.',
    p_eyebrow='Passt das zu Ihnen?', p_h2='Besonders passend, wenn zwei dieser Punkte auf Sie zutreffen',
    p_list=['Sie wünschen sich Software, die genau zu Ihren Abläufen passt.',
            'Wichtige Arbeit läuft noch über Excel, E-Mail oder Papier – und Sie möchten Ihrem Team diese Zeit zurückgeben.',
            'Sie denken über eigene Software nach und möchten das Risiko klein halten.',
            'Andere Unternehmen Ihrer Branche haben dasselbe Anliegen – und Sie sind offen, gemeinsam etwas aufzubauen.'],
    p_note='Die übrigen 20 % des Budgets sind die Garantie von AMALOR: ein Vertrag, Auswahl und Ersatz der Leute, Methode, '
           'Qualitätskontrolle, Werkzeuge. <a href="{L}principles/">Das Modell im Detail →</a>',
    k_eyebrow='Kontakt', k_h2='Ein Gespräch genügt, um zu sehen, ob es passt',
    k_lead='Erzählen Sie, was Sie bewegt und was Ihnen heute Zeit kostet. 30 Minuten, kostenlos und unverbindlich. Antwort innerhalb '
           'eines Werktags – auf Deutsch, Englisch oder Russisch.',
    k_btn=['Termin buchen', 'WhatsApp', 'Anrufen', 'LinkedIn'], k_form='Oder beschreiben Sie Ihre Aufgabe direkt hier:'),
'en': dict(
    eyebrow='For clients',
    h1='Your own software. <span class="gold">Built by people who co-own it.</span>',
    lead='A fixed team of 3–5 specialists plus AI builds software, automation and new workflows for your company. You only pay for '
         'what you have accepted. And if your whole industry has the same problem, your solution becomes a product – with you as a '
         'co-founder.',
    cta1='Talk to us', cta2='How it works',
    byline='80% of the budget goes to the team · nothing for stages you have not accepted · 2-week diagnostic at a fixed price',
    w_eyebrow='The familiar problem', w_h2='Why software projects so often cost too much and disappoint',
    w_lead='When you order software from a development firm, you pay for the whole machine: sales, project management, offices and '
           'margin. The people who build your software work for their employer – their salary is the same whether your solution '
           'succeeds or not.',
    c1='Classic contract', c1s='with a service provider',
    c1l=['Your budget funds the provider’s overhead.', 'The developers work for their employer, not for your result.',
         'Billing by the hour: more effort means more revenue.', 'After the project the team moves on to the next client.'],
    c2='With us', c2s='built by a team that stays',
    c2l=['80% of your budget goes to the people who build your solution.', 'You only pay for what you have accepted.',
         'If someone drops out, AMALOR provides a replacement.', 'As a partner, you and the team become co-founders of the solution.'],
    rule='<b>Ownership is the strongest motivation.</b> Whoever holds a share in the solution wants it to really work – not just '
         'to get the project invoiced.',
    a_eyebrow='How we work', a_h2='Understand first, then build – stage by stage',
    a_lead='After every step you decide again: continue, adjust or stop.',
    steps=[('free', 'Conversation', '30 minutes. We understand your problem and tell you honestly whether we can help.'),
           ('about 2 weeks', 'Diagnostic', 'Fixed price. Solution plan, stages with acceptance criteria, price and timeline.'),
           ('fixed price per stage', 'First version', 'The team builds the first usable solution for your company. Visible results every Friday.'),
           ('ongoing', 'Operation', 'The same team supports and develops it further – for a monthly fee.')],
    g_eyebrow='Two paths',
    v_eyebrow='The vision', v_h2='First the best software for your company. Then for your industry.',
    v_lead='Companies in one industry compete in their business, not in their software. That is how DATEV began: German tax advisers '
           'built their software together and still own it as a cooperative. Whoever builds first sets the standard. Each step '
           'builds on the one before, none is required.',
    vsteps=[('Diagnostic', 'two weeks, fixed price'), ('Your own software', 'built for your company, proven in real use'),
            ('Startup', 'you and the team found it together – under its own name'),
            ('Industry customers', 'other companies use the solution, data strictly separated'),
            ('Cooperative', 'the industry becomes a co-owner of the software')],
    o_h3='When the industry joins',
    owners=[('Companies in the industry', 'buy shares in the cooperative: a vote and lower licence prices'),
            ('The cooperative', 'becomes the majority owner of the startup – the software belongs to the industry, not to a corporation'),
            ('You as the founder', 'keep founder shares, free use and a seat on the supervisory board'),
            ('The team', 'keeps its shares and keeps developing the software')],
    v_rule='<b>Whoever thinks of everyone gets the best.</b> The first client sets the standard of its industry – and gets the '
           'solution built exactly for it.',
    p_eyebrow='Is this for you?', p_h2='Companies gain most when two of these points apply',
    p_list=['Your industry software does not fit your processes, costs too much or is too rigid.',
            'Important work still runs on Excel, email or paper.',
            'You have thought about your own software, but the risk put you off.',
            'Other companies in your industry struggle with the same problem.'],
    p_note='The remaining 20% of the budget is the AMALOR guarantee: one contract, selecting and replacing people, method, quality '
           'control, tools. <a href="{L}principles/">The model in detail →</a>',
    k_eyebrow='Contact', k_h2='One conversation is enough to see whether it fits',
    k_lead='Tell us what costs you time or money today. 30 minutes, free and without obligation. We reply within one working day – '
           'in English, German or Russian.',
    k_btn=['', 'WhatsApp', 'Call', 'LinkedIn'], k_form='Or describe your task right here:'),
'ru': dict(
    eyebrow='Заказчикам',
    h1='Своё ПО для вашей компании. <span class="gold">Его строят люди, которые им совладеют.</span>',
    lead='Постоянная команда из 3–5 специалистов и ИИ создаёт софт, автоматизацию и новые процессы для вашей компании. Платите только '
         'за то, что приняли. А если у всей вашей отрасли та же проблема, ваше решение становится продуктом — и вы его сооснователь.',
    cta1='Обсудить задачу', cta2='Как это устроено',
    byline='80% бюджета — команде · 0 за непринятые этапы · 2 недели диагностики по фиксированной цене',
    w_eyebrow='Знакомая проблема', w_h2='Почему проекты по разработке ПО так часто дороги и разочаровывают',
    w_lead='Заказывая софт у компании-разработчика, вы оплачиваете весь аппарат: продажи, проектное управление, офисы и маржу. Люди, '
           'которые пишут ваше ПО, работают на своего работодателя — их зарплата одинакова, удастся ваше решение или нет.',
    c1='Обычный заказ', c1s='у подрядчика',
    c1l=['Ваш бюджет содержит аппарат подрядчика.', 'Разработчики работают на работодателя, а не на ваш результат.',
         'Оплата по часам: больше работы — больше выручки.', 'После проекта команда уходит к следующему клиенту.'],
    c2='С нами', c2s='строит команда, которая остаётся',
    c2l=['80% вашего бюджета получают люди, которые создают решение.', 'Вы платите только за то, что приняли.',
         'Если кто-то выбывает, AMALOR даёт замену.', 'Как партнёр вы и команда становитесь сооснователями решения.'],
    rule='<b>Самая сильная мотивация — собственность.</b> Тот, у кого есть доля в решении, хочет, чтобы оно действительно работало, '
         'а не просто чтобы проект закрыли счётом.',
    a_eyebrow='Как мы работаем', a_h2='Сначала понять, потом строить — этап за этапом',
    a_lead='После каждого шага вы решаете заново: продолжить, скорректировать или остановиться.',
    steps=[('бесплатно', 'Разговор', '30 минут. Разбираемся в проблеме и честно говорим, можем ли помочь.'),
           ('около 2 недель', 'Диагностика', 'Фиксированная цена. План решения, этапы с критериями приёмки, цена и срок.'),
           ('фикс. цена за этап', 'Первая версия', 'Команда строит первое рабочее решение для вашей компании. Каждую пятницу — видимый результат.'),
           ('постоянно', 'Эксплуатация', 'Та же команда сопровождает и развивает решение — за ежемесячную плату.')],
    g_eyebrow='Два пути',
    v_eyebrow='Видение', v_h2='Сначала лучшее ПО для вашей компании. Потом — для всей отрасли.',
    v_lead='Компании одной отрасли конкурируют в своём деле, а не в софте. Так появился DATEV: немецкие налоговые консультанты вместе '
           'построили своё ПО и до сих пор владеют им как кооперативом. Кто строит первым, задаёт стандарт. Каждый шаг опирается на '
           'предыдущий, ни один не обязателен.',
    vsteps=[('Диагностика', 'две недели, фиксированная цена'), ('Своё ПО', 'построено для вашей компании, проверено в работе'),
            ('Стартап', 'вы и команда основываете его вместе — под своим именем'),
            ('Клиенты отрасли', 'решением пользуются другие компании, данные строго раздельны'),
            ('Кооператив', 'отрасль становится совладельцем ПО')],
    o_h3='Когда подключается отрасль',
    owners=[('Компании отрасли', 'покупают паи кооператива: право голоса и более дешёвые лицензии'),
            ('Кооператив', 'становится основным владельцем стартапа — ПО принадлежит отрасли, а не корпорации'),
            ('Вы как основатель', 'сохраняете долю основателя, бесплатное использование и место в наблюдательном совете'),
            ('Команда', 'сохраняет свои доли и продолжает развивать ПО')],
    v_rule='<b>Кто думает обо всех, получает лучшее.</b> Первый заказчик задаёт стандарт своей отрасли — и получает решение, '
           'построенное именно под него.',
    p_eyebrow='Подходит ли это вам?', p_h2='Больше всего выигрывают компании, к которым относятся два из этих пунктов',
    p_list=['Отраслевой софт не подходит под ваши процессы, слишком дорогой или негибкий.',
            'Важная работа всё ещё идёт через Excel, почту или бумагу.',
            'Вы думали о собственном ПО, но пугал риск.',
            'Другие компании вашей отрасли бьются с той же проблемой.'],
    p_note='Остальные 20% бюджета — гарантия AMALOR: один договор, подбор и замена людей, метод, контроль качества, инструменты. '
           '<a href="{L}principles/">Модель подробно →</a>',
    k_eyebrow='Контакт', k_h2='Одного разговора достаточно, чтобы понять, подходит ли это',
    k_lead='Расскажите, что сегодня стоит вам времени или денег. 30 минут, бесплатно и ни к чему не обязывает. Ответим в течение '
           'рабочего дня — на русском, английском или немецком.',
    k_btn=['', 'WhatsApp', 'Позвонить', 'LinkedIn'], k_form='Или опишите задачу прямо здесь:'),
}


def client_page(lang, form, product_client, faq):
    t = T[lang]
    first = BOOKING.get(lang, '#anfrage')
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    steps = ''.join(f'<div><p class="when"><span class="num">{i + 1:02d}</span> {a}</p><h3>{b}</h3><p>{c}</p></div>'
                    for i, (a, b, c) in enumerate(t['steps']))
    vsteps = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in t['vsteps'])
    owners = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t['owners'])
    btns = []
    if lang in BOOKING:
        btns.append(f'<a class="btn" href="{BOOKING[lang]}">{t["k_btn"][0]}</a>')
    btns += [f'<a class="btn ghost" href="mailto:hello@amalor.ai">hello@amalor.ai</a>',
             f'<a class="btn ghost" href="{WA[lang]}" rel="noopener">{t["k_btn"][1]}</a>',
             f'<a class="btn ghost" href="tel:{PHONE}">{t["k_btn"][2]}</a>',
             f'<a class="btn ghost" href="{LINKEDIN}" rel="me noopener">{t["k_btn"][3]}</a>']
    product_client = product_client.split('<section id="danach">')[0].rstrip()  # "after the project" is step 4 now
    # the product table keeps its own heading; it gets the eyebrow of the page
    product_client = product_client.replace('<div class="head">', f'<div class="head">\n    <span class="who">{t["g_eyebrow"]}</span>', 1)
    return f'''<header class="hero small cl-hero">
  <div class="stack">
    <span class="who">{t['eyebrow']}</span>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    <div class="hb-cta"><a class="btn" href="{first}">{t['cta1']}</a><a class="btn ghost" href="#ablauf">{t['cta2']}</a></div>
    <p class="byline">{t['byline']}</p>
  </div>
</header>
<section id="warum">
  <div class="head">
    <span class="who">{t['w_eyebrow']}</span>
    <h2>{t['w_h2']}</h2>
    <p class="lead">{t['w_lead']}</p>
  </div>
  <div class="cards3 two">
    <div class="card"><p class="when">{t['c1s']}</p><h3>{t['c1']}</h3><ul class="ticks">{li(t['c1l'])}</ul></div>
    <div class="card us"><p class="when">{t['c2s']}</p><h3>{t['c2']}</h3><ul class="ticks">{li(t['c2l'])}</ul></div>
  </div>
  <p class="rule">{t['rule']}</p>
</section>
<section id="ablauf" class="dark">
  <div class="head">
    <span class="who">{t['a_eyebrow']}</span>
    <h2>{t['a_h2']}</h2>
    <p class="lead">{t['a_lead']}</p>
  </div>
  <div class="week steps4">{steps}</div>
</section>
{product_client}
<section id="vision" class="dark">
  <div class="head">
    <span class="who">{t['v_eyebrow']}</span>
    <h2>{t['v_h2']}</h2>
    <p class="lead">{t['v_lead']}</p>
  </div>
  <ol class="flow">{vsteps}</ol>
  <h3 class="o-h3">{t['o_h3']}</h3>
  <div class="owners">{owners}</div>
  <p class="rule">{t['v_rule']}</p>
</section>
<section id="passt">
  <div class="head">
    <span class="who">{t['p_eyebrow']}</span>
    <h2>{t['p_h2']}</h2>
  </div>
  <ul class="ticks fit2">{li(t['p_list'])}</ul>
  <p class="when" style="margin-top:20px">{t['p_note']}</p>
</section>
<section id="anfrage" class="dark">
  <div class="head">
    <span class="who">{t['k_eyebrow']}</span>
    <h2>{t['k_h2']}</h2>
    <p class="lead">{t['k_lead']}</p>
  </div>
  <div class="hb-cta">{''.join(btns)}</div>
  <p class="k-form">{t['k_form']}</p>
  {form}
</section>
{faq}'''


# ---------- words that go everywhere: no "circle", no location ----------
TEXT_FIX = {
'de': [
    ('aus dem Kreis', 'aus dem Netzwerk'), ('Mitglied des Kreises', 'Mitglied des Netzwerks'),
    ('aus demselben Kreis', 'aus demselben Netzwerk'), ('an den Kreisen teilnehmen', 'an den Runden teilnehmen'),
    ('Suchkreis', 'Suchrunde'), ('zu den Kreisen', 'zu den Runden'), ('des nächsten Kreises', 'der nächsten Runde'),
    ('der große Kreis', 'die große Runde'), ('<h3>Kreis</h3>', '<h3>Runde</h3>'), ('Kreis der Teams', 'Runde der Teams'),
    (' Dubai und remote.', ''), ('In Dubai und remote weltweit.', 'Remote, wo immer Sie sind.'),
    ('neben Programmen aus Dubai und Impact-Investoren', 'neben Förderprogrammen und Impact-Investoren'),
    ('placeholder="Dubai"', 'placeholder="Leipzig"'),
],
'en': [
    ('from the circle', 'from the network'), ('a circle member', 'a network member'), ('member of the circle', 'member of the network'),
    ('from the same circle', 'from the same network'), ('invite me to circles', 'invite me to sessions'),
    ('join the circles', 'join the sessions'), ('Search circle', 'Search session'), ('the next circle', 'the next session'),
    ('<h3>Circle</h3>', '<h3>Check-in</h3>'), ('Circle of teams', 'Cross-team session'), ('the big circle', 'the big gathering'),
    (' Dubai and remote.', ''), ('In Dubai and remotely worldwide.', 'Remotely, wherever you are.'),
    ('alongside Dubai programmes and impact investors', 'alongside public programmes and impact investors'),
    ('placeholder="Dubai"', 'placeholder="London"'),
],
'ru': [
    ('из круга', 'из сообщества'), ('из того же круга', 'из того же сообщества'), ('<h3>Круг</h3>', '<h3>Планёрка</h3>'),
    ('большой круг', 'общая встреча'), ('Круг команд', 'Встреча команд'), ('Круг поиска', 'Поисковая встреча'),
    ('ближайшего круга', 'ближайшей встречи'), ('участвовать в кругах', 'участвовать во встречах'),
    ('приглашений на круги', 'приглашений на встречи'), ('участника круга', 'участника сообщества'),
    ('участник круга', 'участник сообщества'),
    (' Дубай и удалённо.', ''), ('В Дубае и удалённо по всему миру.', 'Удалённо, где бы вы ни находились.'),
    ('рядом с программами Дубая и impact-инвесторами', 'рядом с программами поддержки и impact-инвесторами'),
],
}


def fix_text(lang, page_html):
    for a, b in TEXT_FIX[lang]:
        page_html = page_html.replace(a, b)
    return page_html

# ---------- the manifesto exists in every language now (2026-11-19) ----------
for _l, _m in {'ru': 'Манифест', 'en': 'Manifesto', 'de': 'Manifest'}.items():
    CIRCLES_TXT[_l]['man'] = _m
