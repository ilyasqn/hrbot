# HRbot

HRbot — это Telegram-бот, созданный для публикации вакансий, ивентов и другой информации в HR-сообществе. Бот разработан с использованием **aiogram 3**, реализует пошаговое заполнение формы вакансии и отправляет данные в Telegram-канал и на backend IT-nomads.

---

## 🚀 Функции

- Публикация вакансий через Telegram
- Пошаговая форма сбора информации:
  - Должность
  - Компания
  - Локация
  - Зарплата (от / до)
  - Опыт работы
  - Формат работы (удалённо / офис / гибрид)
  - Уровень (Junior / Middle / Senior)
  - Описание вакансии
- Проверка правильности ввода числовых значений (зарплата, опыт)
- Отправка информации в Telegram-канал и на backend (с Pydantic-валидацией)
- Работа как в личных чатах, так и в группах (с фильтрацией)

---

## 🛠 Технологии

- Python 3.12
- aiogram 3.20
- Pydantic 2.11.6
- Aiohttp 3.11.8

## 📋 Структура проекта
```angular2html
HRbot/
├── docker-compose.yml
├── Dockerfile
├── logs/
│   └── hrbot.log
├── main.py
├── README.md
├── requirements.txt
└── src/
    ├── configs/
    │   ├── backend.py
    │   └── bot.py
    ├── handlers/
    │   ├── handler.py
    │   ├── event/
    │   └── vacancy/
    │       ├── form.py
    │       ├── handler.py
    │       └── init.py
    ├── keyboards/
    │   ├── base.py
    │   ├── main.py
    │   └── vacancy/
    │       ├── kb.py
    │       └── init.py
    ├── services/
    │   ├── formatter.py
    │   └── sender.py
    ├── states/
    │   ├── event.py
    │   └── vacancy.py
    └── utils/
        └── logger.py
```

## Как запустить проект?

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/ilyasqn/hrbot
2. Следуй корневому пути проекта:
   ```bash
   cd hrbot
3. Запуск:
   ```bash
   docker-compose up --build
