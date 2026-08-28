"""AddressBook — collection of Records, keyed by name."""

from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

    def search(self, query):
        query = query.lower()
        results = []
        for record in self.data.values():
            name_match = query in record.name.value.lower()
            phone_match = any(query in p.value for p in record.phones)
            email_match = record.email and query in record.email.value.lower()
            address_match = record.address and query in record.address.value.lower()

            if name_match or phone_match or email_match or address_match:
                results.append(record)
        return results

    def get_upcoming_birthdays(self, days_ahead=7):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            bday = record.birthday.value
            bday_this_year = bday.replace(year=today.year)

            if bday_this_year < today:
                bday_this_year = bday_this_year.replace(year=today.year + 1)

            days_until_bday = (bday_this_year - today).days
            if 0 <= days_until_bday <= days_ahead:
                congratulation_date = bday_this_year

                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays