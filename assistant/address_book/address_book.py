"""AddressBook — collection of Records, keyed by name."""

from collections import UserDict
from datetime import datetime, timedelta

from assistant.models.record import Record


def _on_year(day, year):
    """безпечний перенос 29 лютого на 28 лютого."""
    try:
        return day.replace(year=year)
    except ValueError:
        return day.replace(year=year, day=28)


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

    def __str__(self) -> str:
        if not self.data:
            return "Address book is empty."
        return "\n".join(str(record) for record in self.data.values())

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False

    def search(self, query: str) -> list[Record]:
        q = query.lower()
        results = []
        for record in self.data.values():
            name_match = q in record.name.value.lower()
            phone_match = any(q in p.value for p in record.phones)
            email_match = record.email and q in record.email.value.lower()
            address_match = record.address and q in record.address.value.lower()

            if name_match or phone_match or email_match or address_match:
                results.append(record)
        return results

    def get_upcoming_birthdays(self, days_ahead: int = 7) -> list[dict[str, str]]:
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            bday = record.birthday.value
            bday_this_year = _on_year(bday, today.year)

            if bday_this_year < today:
                bday_this_year = _on_year(bday, today.year + 1)

            days_until_bday = (bday_this_year - today).days
            if 0 <= days_until_bday <= days_ahead:
                congratulation_date = bday_this_year

                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                    }
                )

        return upcoming_birthdays
