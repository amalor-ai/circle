"""Content for the pages that are new in the multi-page site (ru / en)."""

NAV = {
    'ru': [('clients/', 'Заказчикам'), ('members/', 'Участникам'), ('team/', 'Как работает команда'),
           ('guides/', 'Проводникам'), ('investors/', 'Инвесторам'), ('principles/', 'Принципы'), ('book/', 'Книга')],
    'en': [('clients/', 'Clients'), ('members/', 'Members'), ('team/', 'How a team works'),
           ('guides/', 'Referrers'), ('investors/', 'Investors'), ('principles/', 'Principles'), ('book/', 'Book')],
}

TITLE = {'ru': 'Команда последнего поколения', 'en': 'Last Generation Team'}

PAGE_TITLES = {
    'ru': {'index': 'Команда последнего поколения', 'clients': 'Заказчикам — Команда последнего поколения',
           'members': 'Участникам — Команда последнего поколения', 'team': 'Как работает команда — Команда последнего поколения',
           'guides': 'Проводникам — Команда последнего поколения', 'principles': 'Принципы — Команда последнего поколения',
           'investors': 'Инвесторам — Команда последнего поколения', 'book': 'Книга — Команда последнего поколения'},
    'en': {'index': 'Last Generation Team', 'clients': 'Clients — Last Generation Team',
           'members': 'Members — Last Generation Team', 'team': 'How a team works — Last Generation Team',
           'guides': 'Referrers — Last Generation Team', 'principles': 'Principles — Last Generation Team',
           'investors': 'Investors — Last Generation Team', 'book': 'Book — Last Generation Team'},
}

DESC = {
    'ru': {'clients': 'Слаженная работа по этапам до результата: небольшая команда специалистов, диагностика по фиксированной цене, оплата по этапам. Дубай и удалённо.',
           'members': 'Работа в команде, а не в одиночку: задачи со смыслом, доход по вкладу, путь от участника до наставника.',
           'team': 'Ритм недели и шестинедельного цикла, договор команды и то, как процесс улучшает сам себя.',
           'guides': 'Познакомьте нас с заказчиком и получите 10% от первого проекта.',
           'principles': 'На чём держится команда, какие задачи мы берём и как делятся деньги.',
           'investors': 'Путь инвестора: сначала участие, деньги — после доказательств.',
           'book': 'Книга «Команда последнего поколения. Как связка тростника» — скоро.'},
    'en': {'clients': 'Coordinated work, stage by stage, to the result: a small team of specialists, a fixed-price diagnostic, payment per stage. Dubai and remote.',
           'members': 'Work in a team, not alone: meaningful projects, income by contribution, a path from member to mentor.',
           'team': 'The weekly rhythm, the six-week cycle, the team agreement and how the process improves itself.',
           'guides': 'Introduce us to a client and receive 10% of the first project.',
           'principles': 'What holds the team together, which tasks we take on and how the money is shared.',
           'investors': 'The investor path: participation first, money after proof.',
           'book': 'The book “Last Generation Team. Like a bundle of reeds” — coming soon.'},
}

HOME_MORE = {
'ru': '''<section>
  <div class="head"><h2>Как это устроено</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Задача</h3><p class="when">Заказчик приносит задачу или её находит участник круга. Проверяем её ситом.</p></div></li>
    <li><span class="num">2</span><div><h3>Команда</h3><p class="when">Под задачу собираем небольшую команду из людей, проверенных делом.</p></div></li>
    <li><span class="num">3</span><div><h3>Работа по этапам</h3><p class="when">Каждый этап заказчик видит и принимает. За результат отвечает вся команда.</p></div></li>
    <li><span class="num">4</span><div><h3>Рост</h3><p class="when">Сильные решения могут вырасти в продукт, а команда — стать его совладельцами.</p></div></li>
  </ol>
  <p class="more"><a href="{L}team/">Как работает команда →</a> · <a href="{L}principles/">Принципы →</a></p>
</section>''',
'en': '''<section>
  <div class="head"><h2>How it works</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Task</h3><p class="when">A client brings a task, or a circle member finds one. We run it through our filter.</p></div></li>
    <li><span class="num">2</span><div><h3>Team</h3><p class="when">We form a small team of people who have proven themselves in practice.</p></div></li>
    <li><span class="num">3</span><div><h3>Staged delivery</h3><p class="when">The client sees and accepts every stage. The whole team is accountable.</p></div></li>
    <li><span class="num">4</span><div><h3>Growth</h3><p class="when">Strong solutions can grow into a product, and the team can become its co-owners.</p></div></li>
  </ol>
  <p class="more"><a href="{L}team/">How a team works →</a> · <a href="{L}principles/">Principles →</a></p>
</section>'''}

LADDER = {
'ru': '''<section>
  <div class="head">
    <h2>Приходят за деньгами. Остаются за командой</h2>
    <p class="lead">Мотивация растёт вместе с человеком: от заработка и опыта — к признанию и желанию отдавать.</p>
  </div>
  <ol class="ladder">
    <li><span class="num">1</span><div><h3>Участник</h3><p class="when">мотив: деньги и опыт</p></div></li>
    <li><span class="num">2</span><div><h3>Член команды</h3><p class="when">мотив: доля и признание заказчика</p></div></li>
    <li><span class="num">3</span><div><h3>Ядро</h3><p class="when">мотив: признание за вклад в общее</p></div></li>
    <li><span class="num">4</span><div><h3>Наставник</h3><p class="when">мотив: отдача и рост других</p></div></li>
  </ol>
  <p class="rule"><b>Основа на каждом уровне:</b> справедливая оплата и доля по вкладу.</p>
</section>''',
'en': '''<section>
  <div class="head">
    <h2>People come for the money. They stay for the team</h2>
    <p class="lead">Motivation grows with the person: from income and experience to recognition and the wish to give back.</p>
  </div>
  <ol class="ladder">
    <li><span class="num">1</span><div><h3>Member</h3><p class="when">motive: income and experience</p></div></li>
    <li><span class="num">2</span><div><h3>Team member</h3><p class="when">motive: a share and client recognition</p></div></li>
    <li><span class="num">3</span><div><h3>Core</h3><p class="when">motive: recognition for contributing to the whole</p></div></li>
    <li><span class="num">4</span><div><h3>Mentor</h3><p class="when">motive: giving back and helping others grow</p></div></li>
  </ol>
  <p class="rule"><b>The base at every level:</b> fair pay and a share by contribution.</p>
</section>'''}

TEAM = {
'ru': '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">Как работает команда</p>
    <h1>Ритм, который держит людей вместе</h1>
    <p class="lead">Около трёх часов встреч в неделю — совместимо с основной работой. Каждая встреча начинается с цели и заканчивается решением.</p>
  </div>
</header>
<section>
  <div class="head"><h2>Неделя</h2></div>
  <div class="week">
    <div><p class="when">Пн · 30 минут</p><h3>Круг</h3><p>Цель одной фразой. Все говорят по очереди, около минуты, без споров. Каждый называет главную задачу и где нужна помощь.</p></div>
    <div><p class="when">Вт–Чт · без встреч</p><h3>Работа и выходы к клиентам</h3><p>Короткий отчёт в чате: что сделал, где застрял. Застрявшему помогают — и это видно всем.</p></div>
    <div><p class="when">Пт · 45 минут</p><h3>Демо и раунд признания</h3><p>Что узнали у клиентов, что сделали. Каждый называет ценное, что сделал кто-то другой.</p></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>Цикл — 6 недель работы и пауза</h2>
    <p class="lead">В конце цикла команда решает: продолжаем, меняем курс или расходимся.</p>
  </div>
  <div class="cycle" aria-label="Шесть недель работы, затем большая ретроспектива и пауза">
    <span>Нед. 1</span><span>Нед. 2</span><span>Нед. 3</span><span>Нед. 4</span><span>Нед. 5</span><span>Нед. 6</span><span class="retro">Ретро · 90 мин</span><span class="pause">Пауза 1–2 нед.</span>
  </div>
  <div class="cols" style="margin-top:20px">
    <div><h3>Большая ретро</h3>
      <ul class="ticks"><li>Чему я научился у каждого</li><li>Моя ошибка и что я с ней сделаю</li><li>Где тянул на себя, где отдавал</li><li>Одно изменение процесса</li></ul></div>
    <div><h3>Раз в квартал — большой круг</h3>
      <ul class="ticks"><li>Роли и Team Lead подтверждаются по согласию — по сделанному, а не по симпатии</li><li>Признание за помощь другим — главный повод для почёта</li><li>Взнос в общий фонд, который запускает новые команды</li></ul></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>Договор команды</h2>
    <p class="lead">Подписывается в первый день и перечитывается на каждой большой ретро.</p>
  </div>
  <ol class="contract">
    <li>Отвечаем за результат вместе: застрял один — это задача всех.</li>
    <li>О товарищах говорим ценное. О своих ошибках каждый говорит сам.</li>
    <li>На встрече присутствуем полностью: без телефонов и параллельной работы.</li>
    <li>Решаем по согласию: решение проходит, если нет обоснованных возражений.</li>
    <li>В споре сначала пересказываем позицию другого так, чтобы он согласился.</li>
    <li>Помощь другим видна и ценится выше личных достижений.</li>
    <li>Сигнал «мне тяжело» — нормальный и безопасный. Двое подхватят задачи.</li>
    <li>Роли, включая Team Lead, команда подтверждает раз в квартал.</li>
  </ol>
</section>
<section>
  <div class="head"><h2>Процесс улучшает сам себя</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Ретро команды</h3><p class="when">обязана дать одно изменение</p></div></li>
    <li><span class="num">2</span><div><h3>Проверка циклом</h3><p class="when">стало лучше по показателям здоровья команды?</p></div></li>
    <li><span class="num">3</span><div><h3>Круг команд</h3><p class="when">раз в месяц: что сработало у других</p></div></li>
    <li><span class="num">4</span><div><h3>Общий плейбук</h3><p class="when">новая версия для всех команд</p></div></li>
  </ol>
  <div class="metrics">
    <div><b>Скорость обучения</b><span>сколько гипотез проверено у клиентов за неделю</span></div>
    <div><b>Надёжность</b><span>доля выполненных обещаний</span></div>
    <div><b>Безопасность</b><span>короткий опрос раз в цикл</span></div>
    <div><b>Равенство голоса</b><span>насколько равномерно говорят на встречах</span></div>
  </div>
</section>''',
'en': '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">How a team works</p>
    <h1>A rhythm that keeps people together</h1>
    <p class="lead">About three hours of meetings a week — compatible with a main job. Every meeting starts with a goal and ends with a decision.</p>
  </div>
</header>
<section>
  <div class="head"><h2>The week</h2></div>
  <div class="week">
    <div><p class="when">Mon · 30 minutes</p><h3>Circle</h3><p>The goal in one sentence. Everyone speaks in turn for about a minute, no debate. Each person names their main task and where they need help.</p></div>
    <div><p class="when">Tue–Thu · no meetings</p><h3>Work and client visits</h3><p>A short update in chat: what I did, where I am stuck. Whoever is stuck gets help — and everyone sees it.</p></div>
    <div><p class="when">Fri · 45 minutes</p><h3>Demo and recognition round</h3><p>What we learned from clients and what we built. Everyone names something valuable another person did.</p></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>The cycle — 6 weeks of work and a pause</h2>
    <p class="lead">At the end of each cycle the team decides: continue, change course or part ways.</p>
  </div>
  <div class="cycle" aria-label="Six weeks of work, then a big retrospective and a pause">
    <span>Wk 1</span><span>Wk 2</span><span>Wk 3</span><span>Wk 4</span><span>Wk 5</span><span>Wk 6</span><span class="retro">Retro · 90 min</span><span class="pause">Pause 1–2 wks</span>
  </div>
  <div class="cols" style="margin-top:20px">
    <div><h3>The big retrospective</h3>
      <ul class="ticks"><li>What I learned from each person</li><li>My mistake and what I will do about it</li><li>Where I took, where I gave</li><li>One change to the process</li></ul></div>
    <div><h3>Once a quarter — the big circle</h3>
      <ul class="ticks"><li>Roles and the Team Lead are confirmed by consent — by what was done, not by sympathy</li><li>Recognition for helping others is the main reason for honour</li><li>A contribution to the common fund that launches new teams</li></ul></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>The team agreement</h2>
    <p class="lead">Signed on day one and re-read at every big retrospective.</p>
  </div>
  <ol class="contract">
    <li>We own the result together: if one is stuck, it is everyone’s task.</li>
    <li>About teammates we speak of what is valuable. About our own mistakes each speaks for themselves.</li>
    <li>At meetings we are fully present: no phones, no parallel work.</li>
    <li>We decide by consent: a decision passes if there are no reasoned objections.</li>
    <li>In a disagreement we first restate the other’s position until they agree.</li>
    <li>Helping others is visible and valued above personal achievements.</li>
    <li>Saying “this is hard for me” is normal and safe. Two people will pick up the tasks.</li>
    <li>Roles, including the Team Lead, are confirmed by the team every quarter.</li>
  </ol>
</section>
<section>
  <div class="head"><h2>The process improves itself</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Team retro</h3><p class="when">must produce one change</p></div></li>
    <li><span class="num">2</span><div><h3>Checked by the cycle</h3><p class="when">did the team’s health indicators improve?</p></div></li>
    <li><span class="num">3</span><div><h3>Circle of teams</h3><p class="when">monthly: what worked for others</p></div></li>
    <li><span class="num">4</span><div><h3>Shared playbook</h3><p class="when">a new version for all teams</p></div></li>
  </ol>
  <div class="metrics">
    <div><b>Learning speed</b><span>hypotheses tested with clients per week</span></div>
    <div><b>Reliability</b><span>share of promises kept</span></div>
    <div><b>Safety</b><span>a short survey once per cycle</span></div>
    <div><b>Equal voice</b><span>how evenly people speak in meetings</span></div>
  </div>
</section>'''}

INVESTORS = {
'ru': '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">Инвесторам</p>
    <h1>Сначала участие. Деньги — после доказательств</h1>
    <p class="lead">Мы не просим вкладывать в идею. Мы зовём войти рано — и вложить, когда пилот покажет результат. Мы находим задачу, за которую заказчик готов платить, собираем под неё команду из людей, проверенных делом, и показываем инвестору не питч, а паспорт команды с первым клиентом.</p>
  </div>
</header>
<section>
  <div class="head"><h2>Путь инвестора</h2></div>
  <ol class="ladder">
    <li><span class="num">0</span><div><h3>Наставник и жюри</h3><p class="when">сейчас, до пилота</p><p>Ведёте команду, судите демо-день, даёте мягкое обещание «если будет X — вложу Y». Получаете самый ранний взгляд на команды — без денег и без риска.</p></div></li>
    <li><span class="num">1</span><div><h3>Клуб ангелов</h3><p class="when">после пилота</p><p>Небольшой чек вместе с 5–10 ангелами. Право первого взгляда и соинвестирования в каждую команду.</p></div></li>
    <li><span class="num">2</span><div><h3>Фонд и партнёры</h3><p class="when">масштаб</p><p>Участие в фонде рядом с программами Дубая и impact-инвесторами. Портфель команд с доказанной совместной работой и реальными клиентами.</p></div></li>
  </ol>
</section>
<section>
  <div class="head"><h2>Что получает инвестор</h2></div>
  <ul class="prin plain">
    <li><b>Поток проверенных команд</b><span>Команды приходят с паспортом и первым клиентом — не нужно искать сделки.</span></li>
    <li><b>Сниженный риск</b><span>Команда уже работала вместе, спрос подтверждён заказчиком — два главных риска закрыты до чека.</span></li>
    <li><b>Данные</b><span>С каждым циклом видно, какие сигналы предсказывают сильную команду.</span></li>
  </ul>
</section>
<section>
  <div class="head"><h2>Паспорт команды</h2><p class="lead">Пример того, что видит инвестор.</p></div>
  <div class="passport">
    <div><span>Заказчик</span><b>письмо о намерениях ✓</b></div>
    <div><span>Совместные циклы</span><b>2 из 2 пройдены</b></div>
    <div><span>Team Lead</span><b>подтверждён командой</b></div>
    <div><span>Разговоры с клиентами</span><b>[число]</b></div>
    <div><span>Надёжность</span><b>доля выполненных обещаний</b></div>
    <div><span>Вклад</span><b>продукт · технологии · продажи</b></div>
  </div>
  <p class="more">Хотите стать одним из первых наставников? Напишите: <b>hello@amalor.ai</b></p>
</section>''',
'en': '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">Investors</p>
    <h1>Participation first. Money after proof</h1>
    <p class="lead">We do not ask you to invest in an idea. We invite you in early — and to invest once a pilot shows results. We find a problem a client will pay to solve, form a team of people proven in practice and show the investor not a pitch but a team passport with a first client.</p>
  </div>
</header>
<section>
  <div class="head"><h2>The investor path</h2></div>
  <ol class="ladder">
    <li><span class="num">0</span><div><h3>Mentor and jury</h3><p class="when">now, before the pilot</p><p>Guide a team, judge the demo day, give a soft commitment: “if X happens, I will invest Y”. You get the earliest look at teams — no money, no risk.</p></div></li>
    <li><span class="num">1</span><div><h3>Angel club</h3><p class="when">after the pilot</p><p>A small ticket together with 5–10 angels. First look and co-investment rights in every team.</p></div></li>
    <li><span class="num">2</span><div><h3>Fund and partners</h3><p class="when">at scale</p><p>A stake in a fund alongside Dubai programmes and impact investors. A portfolio of teams with proven collaboration and real clients.</p></div></li>
  </ol>
</section>
<section>
  <div class="head"><h2>What the investor gets</h2></div>
  <ul class="prin plain">
    <li><b>A flow of proven teams</b><span>Teams arrive with a passport and a first client — no deal hunting.</span></li>
    <li><b>Lower risk</b><span>The team has already worked together and demand is confirmed by a client — the two biggest risks are closed before the ticket.</span></li>
    <li><b>Data</b><span>Every cycle shows which signals predict a strong team.</span></li>
  </ul>
</section>
<section>
  <div class="head"><h2>Team passport</h2><p class="lead">An example of what an investor sees.</p></div>
  <div class="passport">
    <div><span>Client</span><b>letter of intent ✓</b></div>
    <div><span>Joint cycles</span><b>2 of 2 completed</b></div>
    <div><span>Team Lead</span><b>confirmed by the team</b></div>
    <div><span>Client conversations</span><b>[number]</b></div>
    <div><span>Reliability</span><b>share of promises kept</b></div>
    <div><span>Contribution</span><b>product · technology · sales</b></div>
  </div>
  <p class="more">Want to be one of the first mentors? Write to <b>hello@amalor.ai</b></p>
</section>'''}

BOOK = {
'ru': '''<section class="book">
  <img src="{R}assets/book-cover-ru.jpg" width="659" height="988" alt="Обложка книги «Команда последнего поколения. Как связка тростника»">
  <div class="stack">
    <p class="eyebrow">Книга · скоро</p>
    <h1>Команда последнего поколения</h1>
    <p class="sub">Как связка тростника</p>
    <p class="lead">Как вместе получить больше, чем в одиночку, — и делать то, что нужно миру. Книга о том, как небольшая команда выбирает задачи, самоорганизуется и растёт — от первого заказа до сети команд.</p>
    <p class="when">Книга готовится к выходу. Оставьте анкету участника — пришлём, когда выйдет.</p>
    <div><a class="btn" href="{L}members/#join">Записаться</a></div>
  </div>
</section>''',
'en': '''<section class="book">
  <img src="{R}assets/book-cover-en.jpg" width="659" height="988" alt="Cover of the book “Last Generation Team. Like a bundle of reeds”">
  <div class="stack">
    <p class="eyebrow">Book · coming soon</p>
    <h1>Last Generation Team</h1>
    <p class="sub">Like a bundle of reeds</p>
    <p class="lead">How to achieve more together than alone — and do what the world needs. A book about how a small team chooses its tasks, organises itself and grows — from the first order to a network of teams.</p>
    <p class="when">The book is in preparation, Russian edition first. Sign up as a member and we will let you know when it is out.</p>
    <div><a class="btn" href="{L}members/#join">Sign up</a></div>
  </div>
</section>'''}

EXTRA_CSS = '''
/* multi-page additions */
.menu{display:flex;flex-wrap:wrap;gap:4px 16px;padding-block:0 14px}
.menu a{color:#C9E4E2;text-decoration:none;font-size:14px;font-weight:500;padding:4px 0;border-bottom:2px solid transparent}
.menu a:hover,.menu a[aria-current]{color:#FFFFFF;border-bottom-color:#E2BF74}
.brandbar{flex-wrap:wrap}
.brandbar .menu{flex-basis:100%}
.hero.small{padding-block:48px 24px}
.hero.small h1{font-size:clamp(30px,5vw,46px)}
.more{margin-top:20px;font-weight:600}
.ladder{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:12px}
.ladder li{display:grid;grid-template-columns:40px 1fr;gap:14px;padding:16px;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
.ladder li:nth-child(2){margin-left:24px}.ladder li:nth-child(3){margin-left:48px}.ladder li:nth-child(4){margin-left:72px}
@media (max-width:560px){.ladder li{margin-left:0!important}}
.ladder p:not(.when){margin-top:6px;color:var(--muted);font-size:15px}
.rule{margin-top:16px;border-left:3px solid var(--gold);padding:10px 14px;background:var(--gold-soft);border-radius:0 8px 8px 0;font-size:15px}
.week{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.week>div{padding:16px;border:1px solid var(--line);border-radius:12px;background:var(--surface)}
.week h3{margin:4px 0 6px}.week p:not(.when){color:var(--muted);font-size:15px}
.cycle{display:flex;flex-wrap:wrap;gap:6px}
.cycle span{flex:1 1 80px;text-align:center;padding:10px 6px;border-radius:8px;background:var(--teal-soft);color:var(--brand);font-size:14px;font-weight:600}
.cycle .retro{flex-basis:130px;background:var(--gold-soft);color:var(--gold)}
.cycle .pause{flex-basis:130px;background:transparent;border:1px dashed var(--line);color:var(--muted)}
.contract{margin:8px 0 0;padding-left:22px;display:grid;gap:10px}
.contract li::marker{color:var(--gold);font-weight:700}
.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin-top:20px}
.metrics div{display:flex;flex-direction:column;padding:12px;border-radius:10px;background:var(--gold-soft)}
.metrics span{font-size:14px;color:var(--muted)}
.prin.plain li{background:var(--surface)}
.passport{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;padding:18px;border:1px solid var(--line);border-radius:14px;background:var(--surface)}
.passport div{display:flex;flex-direction:column}
.passport span{font-size:13px;color:var(--muted)}
.book{display:grid;grid-template-columns:minmax(0,300px) 1fr;gap:36px;align-items:center;border-top:0}
.book img{width:100%;height:auto;border-radius:6px;box-shadow:0 18px 40px rgba(8,60,58,.25)}
@media (max-width:640px){.book{grid-template-columns:1fr}.book img{max-width:260px}}
footer .menu{padding:0}
footer .fl{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:flex-start}
'''

# ---- product path: a client's task can become a product with co-owners ----
PRODUCT_HOME = {
'ru': '''<section id="product">
  <div class="head">
    <h2>От задачи — к продукту</h2>
    <p class="lead">Иногда задача одной компании — это задача целой отрасли. Тогда решение становится продуктом, а у продукта появляются совладельцы: команда, которая его создала, и заказчик, который его вырастил.</p>
  </div>
  <ol class="flow">
    <li><b>Задача</b><span>одного заказчика</span></li>
    <li><b>Решение</b><span>по этапам, с приёмкой</span></li>
    <li><b>Нужно многим</b><span>проверяем у других компаний</span></li>
    <li><b>Продукт</b><span>лицензии для отрасли</span></li>
  </ol>
  <div class="owners">
    <div><b>Команда</b><span>доли по вкладу</span></div>
    <div><b>Заказчик-партнёр</b><span>доля и бесплатная лицензия для себя</span></div>
    <div><b>Организатор</b><span>доля за сборку и запуск</span></div>
    <div><b>Инвесторы</b><span>входят, когда продукт доказал спрос</span></div>
  </div>
  <p class="more"><a href="{L}clients/#product-client">Для заказчиков →</a> · <a href="{L}investors/">Для инвесторов →</a></p>
</section>''',
'en': '''<section id="product">
  <div class="head">
    <h2>From a task to a product</h2>
    <p class="lead">Sometimes one company’s problem is a whole industry’s problem. Then the solution becomes a product — and the product gets co-owners: the team that built it and the client who helped it grow.</p>
  </div>
  <ol class="flow">
    <li><b>Task</b><span>of one client</span></li>
    <li><b>Solution</b><span>in stages, with acceptance</span></li>
    <li><b>Needed by many</b><span>validated with other companies</span></li>
    <li><b>Product</b><span>licences for the industry</span></li>
  </ol>
  <div class="owners">
    <div><b>Team</b><span>shares by contribution</span></div>
    <div><b>Partner client</b><span>a share and a free licence for its own use</span></div>
    <div><b>Organiser</b><span>a share for assembling and launching</span></div>
    <div><b>Investors</b><span>join once the product has proven demand</span></div>
  </div>
  <p class="more"><a href="{L}clients/#product-client">For clients →</a> · <a href="{L}investors/">For investors →</a></p>
</section>'''}

PRODUCT_CLIENT = {
'ru': '''<section id="product-client">
  <div class="head">
    <h2>Ваш кейс может стать продуктом</h2>
    <p class="lead">Вы решаете свою задачу — и можете зарабатывать на том, что она нужна другим. Если после решения видно, что та же боль есть у других компаний, вы выбираете, как дальше.</p>
  </div>
  <div class="tbl"><table>
    <thead><tr><th></th><th>Обычный заказ</th><th class="us">Заказчик-партнёр</th></tr></thead>
    <tbody>
      <tr><td>Что получаете</td><td>готовое решение для своей компании</td><td class="us">решение для себя и долю в продукте для других</td></tr>
      <tr><td>Права</td><td>решение ваше, используете как хотите</td><td class="us">бессрочная бесплатная лицензия для своей компании и доля от лицензий для других</td></tr>
      <tr><td>Что вкладываете</td><td>оплату этапов</td><td class="us">оплату этапов, знание отрасли, участие в доработке и рекомендации как первый клиент</td></tr>
      <tr><td>Риск</td><td>—</td><td class="us">если продукт не вырастет, у вас всё равно остаётся работающее решение</td></tr>
    </tbody>
  </table></div>
  <p class="when" style="margin-top:12px">Размер доли зависит от вклада и записывается в договоре до начала работы над продуктом.</p>
</section>''',
'en': '''<section id="product-client">
  <div class="head">
    <h2>Your case can become a product</h2>
    <p class="lead">You solve your own problem — and can earn from the fact that others need it too. If, once it is solved, other companies clearly have the same pain, you choose what happens next.</p>
  </div>
  <div class="tbl"><table>
    <thead><tr><th></th><th>Standard order</th><th class="us">Partner client</th></tr></thead>
    <tbody>
      <tr><td>What you get</td><td>a working solution for your company</td><td class="us">a solution for yourself and a share in the product for others</td></tr>
      <tr><td>Rights</td><td>the solution is yours to use as you wish</td><td class="us">a perpetual free licence for your company and a share of licence revenue from others</td></tr>
      <tr><td>What you contribute</td><td>payment per stage</td><td class="us">payment per stage, industry knowledge, help refining it, and references as the first client</td></tr>
      <tr><td>Risk</td><td>—</td><td class="us">if the product does not grow, you still keep a working solution</td></tr>
    </tbody>
  </table></div>
  <p class="when" style="margin-top:12px">The size of the share depends on contribution and is written into the contract before work on the product starts.</p>
</section>'''}

PRODUCT_MEMBER = {
'ru': '<p class="more"><a href="{L}#product">Как проект вырастает в продукт с совладельцами →</a></p>',
'en': '<p class="more"><a href="{L}#product">How a project grows into a product with co-owners →</a></p>'}

PIPELINE = {
'ru': '''<section>
  <div class="head">
    <h2>Сначала спрос. Потом люди. Деньги — последними</h2>
    <p class="lead">Первый пилот впереди. Сейчас мы зовём наставников, которые хотят увидеть команды с самого начала.</p>
  </div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Поиск спроса</h3><p class="when">задачи от заказчиков и участников, тендеры, жалобы клиентов, новые правила</p></div></li>
    <li><span class="num">2</span><div><h3>Проверка спроса</h3><p class="when">10–20 разговоров и заказчик, готовый платить за пилот</p></div></li>
    <li><span class="num">3</span><div><h3>Пробная работа</h3><p class="when">1–2 недели в смешанных парах на реальной задаче</p></div></li>
    <li><span class="num">4</span><div><h3>Сборка команды</h3><p class="when">3–5 человек, доли по вкладу, договор команды, Team Lead по согласию</p></div></li>
    <li><span class="num">5</span><div><h3>Решение с заказчиком</h3><p class="when">первые пользователи и первые деньги — до раунда</p></div></li>
    <li><span class="num">6</span><div><h3>Паспорт команды</h3><p class="when">история совместной работы, роли, разговоры с клиентами, показатели</p></div></li>
    <li><span class="num">7</span><div><h3>Демо инвесторам</h3><p class="when">команда, которая уже доказала, что работает, и заказчик-партнёр рядом</p></div></li>
  </ol>
  <p class="rule"><b>Нет заказчика — команду не собираем.</b> Не сработались — пересобираем из того же круга.</p>
</section>''',
'en': '''<section>
  <div class="head">
    <h2>Demand first. Then people. Money last</h2>
    <p class="lead">The first pilot is ahead. Right now we invite mentors who want to see the teams from the very beginning.</p>
  </div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Finding demand</h3><p class="when">tasks from clients and members, tenders, customer complaints, new regulations</p></div></li>
    <li><span class="num">2</span><div><h3>Validating demand</h3><p class="when">10–20 conversations and a client ready to pay for a pilot</p></div></li>
    <li><span class="num">3</span><div><h3>Trial work</h3><p class="when">1–2 weeks in mixed pairs on a real task</p></div></li>
    <li><span class="num">4</span><div><h3>Forming the team</h3><p class="when">3–5 people, shares by contribution, a team agreement, a Team Lead by consent</p></div></li>
    <li><span class="num">5</span><div><h3>Solution with the client</h3><p class="when">first users and first revenue — before any round</p></div></li>
    <li><span class="num">6</span><div><h3>Team passport</h3><p class="when">history of working together, roles, client conversations, indicators</p></div></li>
    <li><span class="num">7</span><div><h3>Investor demo</h3><p class="when">a team that has already proven it works, with a partner client alongside</p></div></li>
  </ol>
  <p class="rule"><b>No client — no team.</b> If people do not click, we regroup from the same circle.</p>
</section>'''}

EXTRA_CSS += '''
.flow{list-style:none;margin:8px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;counter-reset:f}
.flow li{position:relative;padding:14px;border-radius:12px;background:var(--teal-soft);display:flex;flex-direction:column;gap:2px}
.flow li:last-child{background:var(--gold-soft)}
.flow b{font-family:var(--display)}.flow span{font-size:14px;color:var(--muted)}
.owners{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin-top:14px}
.owners div{padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--surface);display:flex;flex-direction:column}
.owners span{font-size:14px;color:var(--muted)}
.tbl{overflow-x:auto}
table{border-collapse:collapse;width:100%;min-width:520px;font-size:15px}
th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}
thead th{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:600}
td:first-child{color:var(--muted)}
td.us,th.us{background:var(--gold-soft)}
th.us{color:var(--gold)}
'''
