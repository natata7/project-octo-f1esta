"""Validation helpers and custom exceptions.

Every field class in ``models.fields`` should call the matching
``validate_*`` function from here and raise ``ValidationError`` on
failure. Keeping validation centralized here (instead of scattered
regexes) makes it easy to unit test and to reuse from both the
address book and any future import/export feature.
"""

class ValidationError(Exception):
    """Raised when user input fails validation."""

    pass

def validate_phone():
    pass

def validate_email():
    pass

def validate_birthday():
    pass