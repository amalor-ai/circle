"""Content for the pages that are new in the multi-page site (ru / en)."""

NAV = {
    'ru': [('clients/', 'Заказчикам'), ('members/', 'Участникам'), ('team/', 'Как работает команда'),
           ('guides/', 'Проводникам'), ('principles/', 'Принципы'), ('book/', 'Книга')],
    'en': [('clients/', 'Clients'), ('members/', 'Members'), ('team/', 'How a team works'),
           ('guides/', 'Referrers'), ('principles/', 'Principles'), ('book/', 'Book')],
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
  <img src="{R}assets/book-cover-ru.jpg" width="659" height="988" alt="Cover of the book “Last Generation Team. Like a bundle of reeds” (Russian edition)">
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
