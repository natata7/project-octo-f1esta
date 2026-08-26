"""Command handlers.

Each handler has the signature (args: list[str], book: AddressBook,
notes: NotesBook) -> str and is wrapped with @input_error.

Wire a new command by (1) writing the handler below and
(2) registering it in COMMANDS at the bottom of this file — main.py
dispatches purely from that table, it never hardcodes command names.
"""

from assistant.address_book.address_book import AddressBook
from assistant.models.record import Record
from assistant.notes.notes_book import NotesBook
from assistant.utils.decorators import input_error

@input_error
def add_contact(args, book: AddressBook, notes: NotesBook) -> str:
    """Add a new contact to the address book."""
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook, notes: NotesBook) -> str:
    """Change an existing phone number for a contact."""
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."

@input_error
def show_phone(args, book: AddressBook, notes: NotesBook) -> str:
    (name,) = args
    record = book.find(name)
    if record is None:
        raise KeyError(name)
    return str(record)

def show_all(args, book: AddressBook, notes: NotesBook) -> str:
    return str(book)

@input_error
def add_birthday(args, book: AddressBook, notes: NotesBook):
    pass

@input_error
def show_birthday(args, book: AddressBook, notes: NotesBook):
    pass

@input_error
def birthdays(args, book: AddressBook, notes: NotesBook):
    pass

@input_error
def search_contacts(args, book: AddressBook, notes: NotesBook):
    pass

@input_error
def delete_contact(args, book: AddressBook, notes: NotesBook) -> str:
    (name,) = args
    book.delete(name)
    return "Contact deleted."

@input_error
def add_note(args, book: AddressBook, notes: NotesBook):
    pass

def show_notes(args, book: AddressBook, notes: NotesBook) -> str:
    return str(notes)

@input_error
def find_notes(args, book: AddressBook, notes: NotesBook):
    pass

@input_error
def edit_note(args, book: AddressBook, notes: NotesBook):
    pass

@input_error
def delete_note(args, book: AddressBook, notes: NotesBook):
    (note_id,) = args
    notes.delete(note_id)
    return "Note deleted."

@input_error
def add_tag(args, book: AddressBook, notes: NotesBook):
    pass

@input_error
def find_notes_by_tag(args, book: AddressBook, notes: NotesBook):
    pass

def sort_notes_by_tag(args, book: AddressBook, notes: NotesBook):
    pass

def say_hello(args, book: AddressBook, notes: NotesBook) -> str:
    return "How can I help you?"

def show_help(args, book: AddressBook, notes: NotesBook):
    pass

COMMANDS = {
    "hello": say_hello,
    "help": show_help,
    "add-contact": add_contact,
    "change-contact": change_contact,
    "phone": show_phone,
    "all-contacts": show_all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
    "search-contacts": search_contacts,
    "delete-contact": delete_contact,
    "add-note": add_note,
    "all-notes": show_notes,
    "find-notes": find_notes,
    "edit-note": edit_note,
    "delete-note": delete_note,
    "add-tag": add_tag,
    "find-notes-by-tag": find_notes_by_tag,
    "sort-notes": sort_notes_by_tag,
}