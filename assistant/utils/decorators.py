"""Decorators shared across CLI command handlers.

Acceptance criterion #10 ("програма коректно обробляє некоректне
введення без закриття") is handled centrally here — every command
handler in cli/commands.py should be wrapped with @input_error
instead of each handler having its own try/except.
"""

from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Enter the argument for the command."
    return inner