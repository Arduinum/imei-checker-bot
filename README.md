# imei-checker-bot
imei-checker-bot - бот для проверки imei телефона.

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