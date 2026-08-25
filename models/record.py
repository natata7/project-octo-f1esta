"""Record — a single contact entry in the AddressBook."""

from datetime import datetime

from models.fields import Address, Birthday, Email, Name, Phone

class Record:
    def __init__(self, name: Name, phone: Phone, email: Email):
        self.name = name
        self.phone = phone
        self.email = email

    def add_phone(self, phone: Phone):
        pass

    def remove_phone(self, phone: Phone):
        pass

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        pass

    def find_phone(self, phone: Phone):
        pass

    def set_email(self, email: Email):
        pass

    def set_address(self, address: Address):
        pass

    def add_birthday(self, birthday: Birthday):
        pass

    def days_to_birthday(self):
        pass