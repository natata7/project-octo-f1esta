"""Entry point: `python -m assistant.main` or the `assistant` console script."""

from assistant.cli.commands import COMMANDS
from assistant.cli.parser import parse_input
from assistant.cli.suggest import suggest_command
from assistant.storage.storage import load_data, save_data

EXIT_COMMANDS = {"close", "exit"}

WELCOME = """
==============================================
  Personal Assistant — Address Book & Notes
==============================================
Type 'help' to see available commands.
Type 'close' or 'exit' to quit and save.
"""


def main() -> None:
    book, notes = load_data()
    print(WELCOME)

    while True:
        try:
            user_input = input("assistant> ")
        except (EOFError, KeyboardInterrupt):
            break

        command, args = parse_input(user_input)
        if not command:
            continue

        if command in EXIT_COMMANDS:
            print("Good bye!")
            break

        handler = COMMANDS.get(command)
        if handler is None:
          print("Unknown command. Type 'help' to see available commands.")
          continue

        print(handler(args, book, notes))


if __name__ == "__main__":
    main()
