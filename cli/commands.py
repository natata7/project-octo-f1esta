"""Command handlers.

Each handler has the signature (args: list[str], book: AddressBook,
notes: NotesBook) -> str and is wrapped with @input_error.

Wire a new command by (1) writing the handler below and
(2) registering it in COMMANDS at the bottom of this file — main.py
dispatches purely from that table, it never hardcodes command names.
"""

from utils.decorators import input_error


@input_error
def add_contact():
    """Add a new contact to the address book."""
    pass  # Implementation goes here