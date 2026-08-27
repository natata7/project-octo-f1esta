# assistant/utils/decorators.py

"""Decorators shared across CLI command handlers.

Acceptance criterion #10 ("програма коректно обробляє некоректне
введення без закриття") is handled centrally here — every command
handler in cli/commands.py should be wrapped with @input_error
instead of each handler having its own try/except.
"""

from functools import wraps
from typing import Any, Callable

from assistant.utils.validators import ValidationError


def input_error(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)

        except ValidationError as error:
            return f"Error: {error}"

        except ValueError as error:
            return f"Error: {error}"

        except KeyError as error:
            message = error.args[0] if error.args else "Item not found."
            return f"Error: {message}"

        except IndexError:
            return "Error: Not enough arguments."

    return wrapper