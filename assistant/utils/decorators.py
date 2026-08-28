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

from assistant.utils.colors import BOLD, RED, RESET
from assistant.utils.validators import ValidationError


def input_error(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)

        except ValidationError as error:
            return f"{BOLD}{RED}Error:{RESET} {error}"

        except ValueError as error:
            message = str(error) or "invalid or missing arguments for this command."
            return f"{BOLD}{RED}Error:{RESET} {message}"

        except TypeError:
            return f"{BOLD}{RED}Error:{RESET} Invalid input. Please provide the correct arguments."

        except KeyError as error:
            key = error.args[0] if error.args else None

            if key:
                return f"{BOLD}{RED}Error:{RESET} '{key}' not found."

            return f"{BOLD}{RED}Error:{RESET} Item not found."

        except IndexError:
            return f"{BOLD}{RED}Error:{RESET} Not enough arguments."

    return wrapper
