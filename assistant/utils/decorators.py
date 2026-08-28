# assistant/utils/decorators.py

"""Decorators shared across CLI command handlers.

Acceptance criterion #10 ("програма коректно обробляє некоректне
введення без закриття") is handled centrally here — every command
handler in cli/commands.py should be wrapped with @input_error
instead of each handler having its own try/except.
"""

from collections.abc import Callable
from functools import wraps
from typing import Any

from assistant.utils.validators import ValidationError


def input_error(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)

        except ValidationError as error:
            return f"Error: {error}"

        except ValueError:
            return "Error: invalid or missing arguments for this command."

        except KeyError as error:
            key = error.args[0] if error.args else None

            if key:
                return f"Error: '{key}' not found."

            return "Error: Item not found."

        except IndexError:
            return "Error: Not enough arguments."

    return wrapper
