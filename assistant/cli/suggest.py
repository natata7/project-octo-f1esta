"""guess the intended command from a typo/near-miss."""

import difflib
from collections.abc import Iterable


def suggest_command(user_input: str, commands: Iterable[str]) -> str | None:

    if not user_input:
        return None

    matches = difflib.get_close_matches(
        user_input.lower(), list(commands), n=1, cutoff=0.5
    )
    if matches:
        return matches[0]

    for command in commands:
        if command.startswith(user_input.lower()) or user_input.lower() in command:
            return command
    return None
