"""Persistence layer.

Save the application data in "assistant/data/data.pkl" directory.
"""

import pickle
from pathlib import Path
from assistant.address_book.address_book import AddressBook
from assistant.notes.notes_book import NotesBook

DATA_DIR = Path.cwd() / "assistant/data"
DATA_FILE = DATA_DIR / "data.pkl"


def save_data(book: AddressBook, notes: NotesBook, path: Path = DATA_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        pickle.dump({"book": book, "notes": notes}, f)


def load_data(path: Path = DATA_FILE) -> tuple[AddressBook, NotesBook]:
    if not path.exists():
        return AddressBook(), NotesBook()
    try:
        with open(path, "rb") as f:
            state = pickle.load(f)
        return state.get("book", AddressBook()), state.get("notes", NotesBook())
    except (pickle.PickleError, EOFError, AttributeError, FileNotFoundError):
        return AddressBook(), NotesBook()
