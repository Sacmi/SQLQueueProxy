# SQLQueueProxy

SQLQueueProxy - это система управления потоком SQL-запросов от распределенных клиентов к базе данных. Проект реализует механизм буферизации и координированной обработки запросов с последующей маршрутизацией результатов обратно клиентам.

## Функциональность

- Прием SQL-запросов от множества клиентов
- Буферизация запросов в очереди
- Координированная передача запросов к СУБД PostgreSQL
- Маршрутизация результатов обратно клиентам
- Поддержка распределенной работы

## Требования

- Python 3.8+
- PostgreSQL
- Docker (опционально)

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/sacmi/sqlqueueproxy
cd sqlqueueproxy
```

2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
# или
.\venv\Scripts\activate  # для Windows

pip install -r requirements.txt
```

## Запуск PostgreSQL в Docker

1. Запустите контейнер с PostgreSQL:
```bash
docker run --name postgres-queue \
    -e POSTGRES_PASSWORD=pass \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=postgres \
    -p 5432:5432 \
    -d postgres:15
```

2. Проверьте, что контейнер запущен:
```bash
docker ps
```

3. Для остановки базы данных:
```bash
docker stop postgres-queue
```

4. Для повторного запуска:
```bash
docker start postgres-queue
```

## Запуск приложения

1. Запустите сервер очереди:
```bash
python server.py
```

2. В отдельном терминале запустите клиент для тестирования:
```bash
python client.py
```

## Структура проекта

```
sqlqueueproxy/
│
├── server.py          # Сервер очереди
├── client.py          # Тестовый клиент
├── init_db.sql        # SQL скрипт инициализации БД
├── requirements.txt   # Зависимости проекта
├── .gitignore         # Исключения для Git
└── README.md          # Документация
```

## Конфигурация

Основные параметры настраиваются в начале файлов server.py и client.py:

```python
# Параметры базы данных
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "pass"

# Параметры сервера
HOST = '127.0.0.1'
PORT = 65432
```

## Тестирование

Для проверки работы системы можно запустить несколько экземпляров клиента, каждый в отдельном терминале:

```bash
python client.py
```
