"""Entry point: `python -m assistant.main` or the `assistant` console script."""

from assistant.storage.storage import save_data, load_data

WELCOME = """
==============================================
  Personal Assistant — Address Book & Notes
==============================================
Type 'help' to see available commands.
Type 'close' or 'exit' to quit and save.
"""


def main() -> None:
    print(WELCOME)


if __name__ == "__main__":
    main()
