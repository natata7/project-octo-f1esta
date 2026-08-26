"""Command handlers.

Each handler has the signature (args: list[str], book: AddressBook,
notes: NotesBook) -> str and is wrapped with @input_error.

Wire a new command by (1) writing the handler below and
(2) registering it in COMMANDS at the bottom of this file — main.py
dispatches purely from that table, it never hardcodes command names.
"""

from assistant.models.record import Record
from assistant.address_book.address_book import AddressBook
from assistant.utils.decorators import input_error


@input_error
def add_contact_cmd(args, book: AddressBook):
    name, phone = args[0], args[1] if len(args) > 1 else None
    record = book.get(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        msg = "Contact created."
    else:
        msg = "Contact updated."
    if phone:
        record.add_phone(phone)
    return msg


@input_error
def delete_contact_cmd(args, book: AddressBook):
    name = args[0]
    if book.delete(name):
        return f"Contact '{name}' deleted."
    return "Contact not found."


@input_error
def edit_phone_cmd(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.data.get(name)
    if not record:
        raise KeyError
    record.edit_phone(old_phone, new_phone)
    return "Phone updated successfully."


@input_error
def search_cmd(args, book: AddressBook):
    query = args[0]
    results = book.search(query)
    if not results:
        return "No contacts matching query found."
    return "\n".join(str(rec) for rec in results)


@input_error
def birthdays_cmd(args, book: AddressBook):
    days = int(args[0]) if args else 7
    upcoming = book.get_upcoming_birthdays(days_ahead=days)
    if not upcoming:
        return f"No upcoming birthdays for the next {days} days."
    return "\n".join(f"{user['name']}: {user['congratulation_date']}" for user in upcoming)