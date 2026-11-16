# Команда последнего поколения

Сайт набора: заказчики, исполнители, проводники. Статическая страница на GitHub Pages.

- `index.html` — вся страница (стили и скрипт внутри).
- Формы отправляются в HubSpot (Forms API v3, портал 149651742). ID форм задаются в `CONFIG` внизу `index.html`; пустой ID = режим превью.
- Публикация: GitHub Pages «Deploy from a branch», ветка `main`, папка `/` (root). Любой push в `main` публикуется сам.

## Сборка
- Исходники: `src/krug.html` (русский), `src/tr_en.py` делает из него `src/krug_en.html` (английский).
- `python3 src/build.py` собирает `index.html`, `en/index.html`, `robots.txt`, `sitemap.xml`, `llms.txt` (разметка schema.org, FAQ, hreflang).
- Адрес сайта задаётся в `BASE` в `src/build.py` — сменить на `https://team.amalor.ai` после настройки DNS.
