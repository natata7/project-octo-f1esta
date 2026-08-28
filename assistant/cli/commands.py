"""Command handlers.

Each handler has the signature (args: list[str], book: AddressBook,
notes: NotesBook) -> str and is wrapped with @input_error.
"""

from assistant.address_book.address_book import AddressBook
from assistant.models.record import Record
from assistant.notes.notes_book import NotesBook
from assistant.utils.colors import BOLD, CYAN, GREEN, RESET, YELLOW
from assistant.utils.decorators import input_error


@input_error
def add_contact(args, book: AddressBook, notes: NotesBook) -> str:
    if len(args) < 1:
        raise ValueError("Give me name and phone please.")
    name = args[0]
    phone = args[1] if len(args) > 1 else None

    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        msg = "Contact added."
    else:
        msg = "Contact updated."

    if phone:
        record.add_phone(phone)
    return msg


@input_error
def change_contact(args, book: AddressBook, notes: NotesBook) -> str:
    if len(args) < 3:
        raise ValueError("Give me name, old phone and new phone please.")
    name, old_phone, new_phone = args[0], args[1], args[2]

    record = book.find(name)
    if record is None:
        raise KeyError(name)

    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook, notes: NotesBook) -> str:
    if not args:
        raise ValueError("Enter user name.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError(name)
    return str(record)


def show_all(args, book: AddressBook, notes: NotesBook) -> str:
    return str(book)


@input_error
def add_birthday(args, book: AddressBook, notes: NotesBook) -> str:
    if len(args) < 2:
        raise ValueError("Give me name and birthday (DD.MM.YYYY) please.")
    name, bday = args[0], args[1]
    record = book.find(name)
    if not record:
        raise KeyError(name)
    record.add_birthday(bday)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook, notes: NotesBook) -> str:
    if not args:
        raise ValueError("Enter contact name.")
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError(name)
    if not record.birthday:
        return f"{name} doesn't have a birthday specified."
    return f"{name}'s birthday: {record.birthday}"


@input_error
def birthdays(args, book: AddressBook, notes: NotesBook) -> str:
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays for the next week."
    return "\n".join(f"{item['name']}: {item['congratulation_date']}" for item in upcoming)


@input_error
def search_contacts(args, book: AddressBook, notes: NotesBook) -> str:
    """Search contacts by query string."""
    if not args:
        raise ValueError("Enter search query.")
    query = args[0]
    results = book.search(query)
    if not results:
        return "No contacts found."
    return "\n".join(str(record) for record in results)


@input_error
def delete_contact(args, book: AddressBook, notes: NotesBook) -> str:
    if not args:
        raise ValueError("Enter user name.")
    name = args[0]
    book.delete(name)
    return "Contact deleted."


@input_error
def add_note(args, book: AddressBook, notes: NotesBook):
    text = " ".join(args).strip()
    if not text:
        raise ValueError("Enter note text.")
    note = notes.add_note(text)
    return f"Note added with ID: {note.id}"


def show_notes(args, book: AddressBook, notes: NotesBook) -> str:
    return str(notes)


@input_error
def find_notes(args, book: AddressBook, notes: NotesBook):
    if not args:
        raise ValueError("Enter search query.")
    query = " ".join(args)
    results = notes.search(query)
    if not results:
        return "No notes found."
    return "\n".join(str(note) for note in results)


@input_error
def edit_note(args, book: AddressBook, notes: NotesBook):
    if len(args) < 2:
        raise ValueError("Give me note ID and new text please.")
    note_id, new_text = args[0], " ".join(args[1:])
    notes.edit(note_id, new_text)
    return "Note updated."


@input_error
def delete_note(args, book: AddressBook, notes: NotesBook):
    if not args:
        raise ValueError("Enter note ID.")
    note_id = args[0]
    notes.delete(note_id)
    return "Note deleted."


@input_error
def add_tag(args, book: AddressBook, notes: NotesBook):
    if len(args) < 2:
        raise ValueError("Give me note ID and at least one tag please.")
    note_id, tags = args[0], args[1:]
    note = notes.add_tag(note_id, tags)
    return f"Tag(s) added. {note}"


@input_error
def find_notes_by_tag(args, book: AddressBook, notes: NotesBook):
    if not args:
        raise ValueError("Enter a tag.")
    results = notes.search_by_tag(args[0])
    if not results:
        return "No notes found."
    return "\n".join(str(note) for note in results)


def sort_notes_by_tag(args, book: AddressBook, notes: NotesBook):
    if not notes.data:
        return "No notes yet."
    return "\n".join(str(note) for note in notes.sort_by_tag())


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

  {GREEN}add-note <text>{RESET} --> Add a new note

  {GREEN}all-notes{RESET} --> Show all notes

  {GREEN}find-notes <query>{RESET} --> Search notes by text or tag

  {GREEN}edit-note <id> <text>{RESET} --> Edit an existing note

  {GREEN}delete-note <id>{RESET} --> Delete a note

{BOLD}{YELLOW}Tags:{RESET}

  {GREEN}add-tag <id> <tag> [tag ...]{RESET} --> Add tag(s) to a note

  {GREEN}find-notes-by-tag <tag>{RESET} --> Find notes by tag

  {GREEN}sort-notes{RESET} --> Show notes sorted by tags
  
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