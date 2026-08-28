"""Record — a single contact entry in the AddressBook."""

from assistant.models.fields import Name, Phone, Email, Address, Birthday


class Record:
    def __init__(self, name, address=None, email=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None

    def add_phone(self, phone_number):
        if self.find_phone(phone_number):
            raise ValueError("Phone already exists.")
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
            return True
        return False

    def edit_phone(self, old_phone_number, new_phone_number):
        new_phone = Phone(new_phone_number)
        phone_to_edit = self.find_phone(old_phone_number)
        if phone_to_edit:
            phone_to_edit.value = new_phone.value
        else:
            raise ValueError(f"Phone number {old_phone_number} not found.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday_string):
        self.birthday = Birthday(birthday_string)

    def set_email(self, email_string):
        self.email = Email(email_string)

    def set_address(self, address_string):
        self.address = Address(address_string)

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones) if self.phones else "None"
        bday_str = f", birthday: {self.birthday}" if self.birthday else ""
        email_str = f", email: {self.email}" if self.email else ""
        addr_str = f", address: {self.address}" if self.address else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{email_str}{addr_str}{bday_str}"