"""Record — a single contact entry in the AddressBook."""

from assistant.models.fields import Address, Birthday, Email, Name, Phone
from assistant.utils.colors import BOLD, CYAN, RESET
from assistant.utils.validators import ValidationError, validate_phone


class Record:
    def __init__(self, name: str, address: str | None = None, email: str | None = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None

    def add_phone(self, phone_number: str):
        if self.find_phone(phone_number):
            raise ValueError("Phone already exists.")
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number: Phone) -> bool:
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
            return True
        return False

    def edit_phone(self, old_phone_number: Phone, new_phone_number: str):
        new_phone = Phone(new_phone_number)
        phone_to_edit = self.find_phone(old_phone_number)
        if phone_to_edit:
            phone_to_edit.value = new_phone.value
        else:
            raise ValueError(f"Phone number {old_phone_number} not found.")

    def find_phone(self, phone_number):
        try:
            target = validate_phone(phone_number)
        except ValidationError:
            target = phone_number
        for phone in self.phones:
            if phone.value == target:
                return phone
        return None

    def add_birthday(self, birthday_string: str):
        self.birthday = Birthday(birthday_string)

    def set_email(self, email_string: str):
        self.email = Email(email_string)

    def set_address(self, address_string: str):
        self.address = Address(address_string)

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones) if self.phones else "None"
        bday_str = f", birthday: {self.birthday}" if self.birthday else ""
        email_str = f", email: {self.email}" if self.email else ""
        addr_str = f", address: {self.address}" if self.address else ""
        return (
            f"Contact name: {BOLD}{CYAN}{self.name.value}{RESET}, "
            f"phones: {phones_str}{email_str}{addr_str}{bday_str}"
        )
