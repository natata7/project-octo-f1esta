"""Command handlers.

Each handler has the signature (args: list[str], book: AddressBook,
notes: NotesBook) -> str and is wrapped with @input_error.
"""

from assistant.address_book.address_book import AddressBook
from assistant.models.record import Record
from assistant.notes.notes_book import NotesBook
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
def add_birthday(args, book: AddressBook, notes: NotesBook):
    pass


@input_error
def show_birthday(args, book: AddressBook, notes: NotesBook):
    pass


@input_error
def birthdays(args, book: AddressBook, notes: NotesBook):
    pass


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
    if not args:
        raise ValueError("Enter note ID.")
    note_id = args[0]
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



def show_help(args, book: AddressBook, notes: NotesBook) -> str:
    return """
            Available commands:

            General:
            hello
                Show greeting.

            help
                Show this help message.

            close / exit
                Save data and exit the assistant.

            Contacts:
            add-contact
                Add a new contact.

            change-contact
                Edit an existing contact.

            phone <name>
                Show contact information by name.

            all-contacts
                Show all contacts.

            search-contacts <query>
                Search contacts.

            delete-contact <name>
                Delete a contact.

            Birthdays:
            add-birthday
                Add a birthday to a contact.

            show-birthday <name>
                Show contact birthday.

            birthdays
                Show upcoming birthdays.

            Notes:
            add-note
                Add a new note.

            all-notes
                Show all notes.

            find-notes <query>
                Search notes.

            edit-note
                Edit an existing note.

            delete-note <id>
                Delete a note.

            Tags:
            add-tag
                Add a tag to a note.

            find-notes-by-tag <tag>
                Find notes by tag.

            sort-notes
                Sort notes by tags.
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