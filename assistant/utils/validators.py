"""Validation helpers and custom exceptions.

Every field class in ``models.fields`` should call the matching
``validate_*`` function from here and raise ``ValidationError`` on
failure. Keeping validation centralized here (instead of scattered
regexes) makes it easy to unit test and to reuse from both the
address book and any future import/export feature.
"""

import re
from datetime import datetime


class ValidationError(Exception):
    """Raised when user input fails validation."""

    pass


def validate_phone(phone: str) -> str:
    normalized_phone = re.sub(r"\D", "", phone)

    if normalized_phone.startswith("380") and len(normalized_phone) == 12:
        return f"+{normalized_phone}"

    if normalized_phone.startswith("0") and len(normalized_phone) == 10:
        return f"+38{normalized_phone}"

    raise ValidationError(
        "Invalid phone number. Use format +380XXXXXXXXX or 0XXXXXXXXX."
    )


def validate_email(email: str) -> str:
    pattern = r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern, email):
        raise ValidationError("Invalid email format.")

    return email


def validate_birthday(birthday: str) -> str:
    try:
        datetime.strptime(birthday, "%d.%m.%Y")
    except ValueError:
        raise ValidationError("Invalid birthday. Use format DD.MM.YYYY.")

    return birthday
