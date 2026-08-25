# Personal Assistant

CLI-помічник для ведення адресної книги контактів та нотаток.

## Системні вимоги

- Python 3.10+

## Встановлення

```bash
git clone https://github.com/natata7/project-octo-f1esta.git
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск

```bash
python -m main
```

## Загальна структура

```

main.py                 # точка входу
cli/
├── parser.py           # розбір введеного рядка на команду, аргументи
├── commands.py         # обробники команд
└── suggest.py          # бонус: підказка команди при помилці введення
models/
├── fields.py           # Field, Name, Phone, Email, Address, Birthday
├── record.py           # Record (один контакт)
└── note.py             # Note (одна нотатка + теги)
address_book/
└── address_book.py     # AddressBook(UserDict) — CRUD, пошук, дні народження
notes/
└── notes_book.py       # NotesBook — CRUD, пошук, теги
storage/
└── storage.py          # збереження/завантаження через pickle
utils/
├── validators.py       # regex-валідація телефону/email/дати
└── decorators.py       # @input_error — централізована обробка помилок вводу
```
