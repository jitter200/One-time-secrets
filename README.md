# One-time-secrets

Сервис для безопасного одноразового хранения и получения секретов.

## Возможности

- Создание, получение и удаление секретов.
- Секрет выдается только один раз.
- Секрет хранится зашифрованным.
- Кеширование на 5 минут.
- Логирование действий в PostgreSQL.
- Контейнеризация с помощью Docker.

## Запуск

```bash
docker-compose up --build
```

API будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

## Эндпоинты

- `POST /secret` — создать секрет.
- `GET /secret/{secret_key}` — получить секрет.
- `DELETE /secret/{secret_key}` — удалить секрет (если задан passphrase).

## Переменные окружения

Все переменные указаны в файле `.env`.
