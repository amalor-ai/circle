# Команда последнего поколения

Сайт набора: заказчики, исполнители, проводники. Статическая страница на GitHub Pages.

- `index.html` — вся страница (стили и скрипт внутри).
- Формы отправляются в HubSpot (Forms API v3, портал 149651742). ID форм задаются в `CONFIG` внизу `index.html`; пустой ID = режим превью.
- Публикация: GitHub Pages «Deploy from a branch», ветка `main`, папка `/` (root). Любой push в `main` публикуется сам.

## Сборка
- Страницы: главная, Заказчикам, Участникам, Как работает команда, Проводникам, Принципы, Книга; «Инвесторам» — только по ссылке (noindex, нет в меню и в sitemap). Всё на русском, английском (`/en/`) и немецком (`/de/`).
- Исходники: `src/krug.html` (дизайн и общие блоки, русский), `src/tr_en.py` → `src/krug_en.html` (английский), `src/tr_de.py` → `src/krug_de.html` (немецкий, из английского), `src/content_extra.py` + `src/content_de.py` (новые страницы).
- Сборка: `python3 src/tr_en.py && python3 src/tr_de.py && python3 src/build.py` — пишет все `index.html`, `robots.txt`, `sitemap.xml`, `llms.txt`.
- Адрес сайта — `BASE` в `src/build.py`; сменить на `https://team.amalor.ai` после настройки DNS.
