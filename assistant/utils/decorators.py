"""Decorators shared across CLI command handlers.

Acceptance criterion #10 ("програма коректно обробляє некоректне
введення без закриття") is handled centrally here — every command
handler in cli/commands.py should be wrapped with @input_error
instead of each handler having its own try/except.
"""

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Enter required arguments."
        except KeyError:
            return "Contact not found."
    return inner