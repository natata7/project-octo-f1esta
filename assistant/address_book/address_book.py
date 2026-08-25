"""AddressBook — collection of Records, keyed by name."""

from collections import UserDict
from assistant.models.record import Record

class AddressBook(UserDict):
    """A collection of Records, keyed by name.

    This class is a subclass of UserDict, which means it behaves like a
    dictionary. Each key is a contact's name (string), and each value is
    a Record object containing the contact's details.
    """

    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        pass

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(name)

    def search(self, query):
        pass