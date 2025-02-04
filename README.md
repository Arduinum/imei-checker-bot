# imei-checker-bot
imei-checker-bot - бот для проверки imei телефона.

ТЗ Телеграм бот IMEI

1. Общее описание
Необходимо разработать бэкенд-систему для проверки IMEI устройств, которая будет интегрирована с Telegram-ботом и предоставлять API для внешних запросов. В рамках тестового задания необходимо реализовать базовую работу с одним сервисом.
2. Функционал
2.1 Доступ
Белый список пользователей для Telegram:
Реализовать белый список для доступа к функционалу бота.

Авторизация через API:
Реализовать авторизацию по токену для доступа к API.

2.2 Telegram-бот
- Пользователь отправляет боту IMEI.

Бот должен:
- Проверить IMEI на валидность.
- Отправить в ответ информацию о IMEI.

2.3 Запросы API (пример)
Запрос на получение информации:
Метод: POST /api/check-imei
Параметры запроса:
imei (строка, обязательный) — IMEI устройства.
token (строка, обязательный) — токен авторизации.

Ответ:
JSON с информацией о IMEI.

3. Список сервисов
В рамках тестового задания достаточно реализовать тестовую работу с сервисом:
https://imeicheck.net/

Токен API Sandbox: e4oEaZY1Kom5OXzybETkMlwjOCy3i8GSCGTHzWrhd4dc563b
Документация: https://imeicheck.net/promo-api

<details>
  <summary>
    <strong>
      Стек
    </strong>
  </summary>
  
- Python 3.12.0;
- PostgreSQL;
- Docker-compose;
</details>

<details>
  <summary>
    <strong>
      Как оформлять ветки и коммиты
    </strong>
  </summary>

Пример ветки `name_task`

- **name_task** (название задачи)

Пример коммита `refactor: renaming a variable`

- **feat:** (новая функционал кода, БЕЗ учёта функционала для сборок);
- **devops:** (функционал для сборки, - добавление, удаление и исправление);
- **fix:** (исправление ошибок функционального кода);
- **docs:** (изменения в документации);
- **style:** (форматирование, отсутствующие точки с запятой и т.п., без изменения производственного кода);
- **refactor:** (рефакторинг производственного кода, например, переименование переменной);
- **test:** (добавление недостающих тестов, рефакторинг тестов; без изменения производственного кода);
- **chore:** (обновление рутинных задач и т. д.; без изменения производственного кода).

Оформление основано на https://www.conventionalcommits.org/en/v1.0.0/
</details>

<details>
  <summary>
    <strong>
      Пример запуска проекта (Debian, Ubuntu) для разработчиков
    </strong>
  </summary>

- **Заполните .env**: по образцу документа `.env.example`;
- **Запустите проект**: `docker compose -f docker-compose.yml --env-file .env up -d`.
</details>
