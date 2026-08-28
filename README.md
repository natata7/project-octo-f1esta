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

## Зберігання даних

Усі дані (контакти й нотатки) зберігаються у домашній папці користувача:
`~/.personal-assistant/data.pkl` або C:\Users\. Тому помічник можна запускати з будь-якої директорії й перезапускати без втрати даних.

## Команди

### Загальні

- `hello` - привітання
- `help` - список команд
- `close` / `exit` - зберегти дані та вийти

### Контакти

- `add-contact <name> [phone]` - додати контакт (або телефон до наявного)
- `change-contact <name> <old-phone> <new-phone>` - замінити номер телефону
- `remove-phone <name> <phone>` - видалити номер телефону
- `add-email <name> <email>` - задати email
- `add-address <name> <address>` - задати адресу
- `phone <name>` - показати картку контакту
- `all-contacts` - показати всі контакти
- `search-contacts <query>` - пошук за іменем/телефоном/email/адресою
- `delete-contact <name>` - видалити контакт

### Дні народження

- `add-birthday <name> <DD.MM.YYYY>` - додати дату народження
- `show-birthday <name>` - показати дату народження
- `birthdays [days]` - дні народження на N днів наперед (за замовчуванням 7)

### Нотатки

- `add-note <text>` - додати нотатку, повертає її ID 
- `all-notes` - показати всі нотатки
- `find-notes <query>` - пошук за текстом або тегом
- `edit-note <id> <text>` - змінити текст нотатки за її ID
- `delete-note <id>` - видалити нотатку за її ID

### Теги

- `add-tag <id> <tag>` - додати теги до нотатки
- `find-notes-by-tag <tag>` - знайти нотатки за тегом
- `sort-notes` - показати нотатки, відсортовані за тегами

Якщо команду введено з помилкою, помічник пропонує найближчу за назвою.

## Загальна структура

```
pyproject.toml           # метадані пакета, залежності, точка входу `assistant`
assistant/
├── main.py               # точка входу (main()), консольний скрипт `assistant`
├── cli/
│   ├── parser.py         # розбір введеного рядка на команду, аргументи
│   ├── commands.py       # обробники команд
│   └── suggest.py        # підказка найближчої команди при помилці введення
├── models/
│   ├── fields.py         # Field, Name, Phone, Email, Address, Birthday
│   ├── record.py         # Record (один контакт)
│   └── note.py           # Note (одна нотатка + теги)
├── address_book/
│   └── address_book.py   # AddressBook(UserDict) — CRUD, пошук, дні народження
├── notes/
│   └── notes_book.py     # NotesBook — CRUD, пошук та сортування за тегами
├── storage/
│   └── storage.py        # збереження/завантаження через pickle у директорії ~/.personal-assistant
└── utils/
    ├── validators.py     # валідація імені/телефону/email/дати
    ├── colors.py         # кольори
    └── decorators.py     # @input_error — централізована обробка помилок вводу
```

В проєкті використується стандарт кодування [PEP 8](https://peps.python.org/pep-0008/). Під час розробки використовуйте команди:

```
ruff check                # перевірити весь код проєкту
ruff check path/to/code/  # перевірити певну папку
ruff format               # автоформатувати весь код проєкту
ruff format path/to/code/ # автоформатувати певну папку
```
