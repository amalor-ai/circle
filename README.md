# Команда последнего поколения

Сайт набора: заказчики, исполнители, проводники. Статический сайт на Azure Static Web Apps: https://team.amalor.ai

- `index.html` — вся страница (стили и скрипт внутри).
- Формы отправляются в HubSpot (Forms API v3, портал 149651742). ID форм задаются в `CONFIG` внизу `index.html`; пустой ID = режим превью.
- Публикация: любой push в `main` → GitHub Action `.github/workflows/deploy.yml` → Azure Static Web App `swa-amalor-team` (ресурсная группа `rg-amalor-web`, тенант amalor.ai). Публикуются только собранные страницы, без `src/` и `infra/`.
- Инфраструктура как код: `infra/main.bicep`; первичная настройка — `infra/setup-azure.ps1` (создаёт приложение, кладёт токен в GitHub secret, затем привязывает домен). DNS-запись `team` — в репозитории amalor-website, `infra/dns.bicep`.
- Старый адрес amalor-ai.github.io/circle после переезда отдаёт переадресацию на team.amalor.ai.

## Сборка
- Страницы: главная, Заказчикам, Участникам, Как работает команда, Проводникам, Принципы, Книга, Инвесторам (в меню). Всё на русском, английском (`/en/`) и немецком (`/de/`).
- Исходники: `src/krug.html` (дизайн и общие блоки, русский), `src/tr_en.py` → `src/krug_en.html` (английский), `src/tr_de.py` → `src/krug_de.html` (немецкий, из английского), `src/content_extra.py` + `src/content_de.py` (новые страницы).
- Сборка: `python3 src/tr_en.py && python3 src/tr_de.py && python3 src/build.py` — пишет все `index.html`, `robots.txt`, `sitemap.xml`, `llms.txt`.
- Немецкие формы и тексты страницы «Für Fachleute» — `src/forms_de.py` (применяется после `polish_de`). Новые поля должны быть свойствами контакта и полями формы в HubSpot: `python3 infra/hubspot_forms.py` (dry run), затем `--apply`; нужен токен в `HUBSPOT_TOKEN`.
- Адрес сайта — `BASE` в `src/build.py`; сменить на `https://team.amalor.ai` после настройки DNS.

## Манифест
`python3 src/manifest.py` — собирает страницу manifest/ и PDF assets/manifest-ru.pdf (нужен Playwright). Шрифт Manrope лежит в assets/fonts.
