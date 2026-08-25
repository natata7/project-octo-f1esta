"""AddressBook — collection of Records, keyed by name."""


class AddressBook():
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

    def remove_record(self, name):
        pass

    def get_record(self, name):
        pass

    def list_records(self):
        pass

    def search(self, query):
        pass