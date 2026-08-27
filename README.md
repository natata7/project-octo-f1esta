# Personal Assistant

CLI-помічник для ведення адресної книги контактів та нотаток.

## Системні вимоги

- Python 3.10+

## Встановлення

```bash
git clone https://github.com/natata7/project-octo-f1esta.git
cd project-octo-f1esta
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

## Запуск

```bash
assistant
```

Або без встановлення пакета, з кореня репозиторію:

```bash
python -m assistant.main
```

## Загальна структура

```

pyproject.toml           # метадані пакета, залежності, точка входу `assistant`
assistant/
├── main.py               # точка входу (main()), консольний скрипт `assistant`
├── cli/
│   ├── parser.py         # розбір введеного рядка на команду, аргументи
│   ├── commands.py       # обробники команд
│   └── suggest.py        # бонус: підказка команди при помилці введення
├── data/
│   ├── data.py           # службовий файл для зберігання даних додатку, створюється після першого запуску
├── models/
│   ├── fields.py         # Field, Name, Phone, Email, Address, Birthday
│   ├── record.py         # Record (один контакт)
│   └── note.py           # Note (одна нотатка + теги)
├── address_book/
│   └── address_book.py   # AddressBook(UserDict) — CRUD, пошук, дні народження
├── notes/
│   └── notes_book.py     # NotesBook — CRUD, пошук, теги
├── storage/
│   └── storage.py        # збереження/завантаження через pickle
└── utils/
    ├── validators.py     # regex-валідація телефону/email/дати
    └── decorators.py     # @input_error — централізована обробка помилок вводу
```

В проєкті використується стандарт кодування [PEP 8](https://peps.python.org/pep-0008/). Під час розробки використовуйте команди:

```
ruff check                # перевірити весь код проєкту
ruff check path/to/code/  # перевірити певну папку
ruff format               # автоформатувати весь код проєкту
ruff format path/to/code/ # автоформатувати певну папку
```
