"""Validation helpers and custom exceptions.

Every field class in ``models.fields`` should call the matching
``validate_*`` function from here and raise ``ValidationError`` on
failure. Keeping validation centralized here (instead of scattered
regexes) makes it easy to unit test and to reuse from both the
address book and any future import/export feature.
"""
import re
from datetime import datetime











def validate_phone(phone: str) -> str:
    normalized_phone = re.sub(r"[\s()-]", "", phone)

    if not re.fullmatch(r"\+?\d{10,15}", normalized_phone):
        raise ValidationError(
            "Phone number must contain 10-15 digits and may start with '+'."
        )

    return normalized_phone

def validate_email(email: str) -> str:
    pattern = r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern, email):
        raise ValidationError("Invalid email format.")

    return email

def validate_birthday(birthday: str) -> str:
    try:
        datetime.strptime(birthday, "%d.%m.%Y")
    except ValueError:
        raise ValidationError(
            "Invalid birthday. Use format DD.MM.YYYY."
        )

    return birthday