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
from assistant.utils.colors import BOLD, CYAN, GREEN, RESET, YELLOW

@input_error
def add_contact():
    """Add a new contact to the address book."""
    pass  # Implementation goes here

@input_error
def change_contact(args, book: AddressBook, notes: NotesBook):
    pass


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
def add_note(args, book: AddressBook, notes: NotesBook) -> str:
    text = " ".join(args)
    note = notes.add_note(text)
    return str(note)


def show_notes(args, book: AddressBook, notes: NotesBook) -> str:
    return str(notes)


@input_error
def find_notes(args, book: AddressBook, notes: NotesBook) -> str:
    query = " ".join(args)
    return str(notes.find(query))


@input_error
def edit_note(args, book: AddressBook, notes: NotesBook) -> str:

    note_id = args[0]

    new_text = " ".join(args[1:])

    return str(notes.edit(note_id, new_text))


@input_error
def delete_note(args, book: AddressBook, notes: NotesBook) -> str:
    note_id = args[0]
    if note_id not in notes.data:
        return "Note not found."
    notes.delete(note_id)
    return "Note deleted."


# --- notes: bonus tags ------------------------------------------------------

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



def show_help(args, book: AddressBook, notes: NotesBook) -> str:
    return f"""
{BOLD}{CYAN}Available commands:{RESET}

{BOLD}{YELLOW}General:{RESET}

  {GREEN}hello{RESET} --> Show greeting

  {GREEN}help{RESET} --> Show this help message

  {GREEN}close / exit{RESET} --> Save data and exit the assistant

{BOLD}{YELLOW}Contacts:{RESET}

  {GREEN}add-contact{RESET} --> Add a new contact

  {GREEN}change-contact{RESET} --> Edit an existing contact

  {GREEN}phone <name>{RESET} --> Show contact information by name

  {GREEN}all-contacts{RESET} --> Show all contacts

  {GREEN}search-contacts <query>{RESET} --> Search contacts

  {GREEN}delete-contact <name>{RESET} --> Delete a contact

{BOLD}{YELLOW}Birthdays:{RESET}

  {GREEN}add-birthday{RESET} --> Add a birthday to a contact

  {GREEN}show-birthday <name>{RESET} --> Show contact birthday

  {GREEN}birthdays{RESET} --> Show upcoming birthdays

{BOLD}{YELLOW}Notes:{RESET}

  {GREEN}add-note{RESET} --> Add a new note

  {GREEN}all-notes{RESET} --> Show all notes

  {GREEN}find-notes <query>{RESET} --> Search notes

  {GREEN}edit-note{RESET} --> Edit an existing note

  {GREEN}delete-note <id>{RESET} --> Delete a note

{BOLD}{YELLOW}Tags:{RESET}

  {GREEN}add-tag{RESET} --> Add a tag to a note

  {GREEN}find-notes-by-tag <tag>{RESET} --> Find notes by tag

  {GREEN}sort-notes{RESET} --> Sort notes by tags
  
""".strip()



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