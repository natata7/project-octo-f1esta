"""AddressBook — collection of Records, keyed by name."""

from collections import UserDict
from assistant.models.record import Record


class AddressBook(UserDict):
    """A collection of Records, keyed by name."""

    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record: Record):
        if record.name.value in self.data:
            raise ValueError(f"Contact '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(name)

    def search(self, query: str) -> list[Record]:
        q = query.lower()
        results = []
        for record in self.data.values():
            if q in record.name.value.lower():
                results.append(record)
                continue
            if any(q in phone.value for phone in record.phones):
                results.append(record)
                continue
            if record.email and q in record.email.value.lower():
                results.append(record)
                continue
            if record.address and q in record.address.value.lower():
                results.append(record)
                continue
        return results