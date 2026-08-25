"""NotesBook — collection of Notes, keyed by note id."""

from assistant.models.note import Note


class NotesBook:
    def __init__(self):
        self.data: dict[str, Note] = {}

    def add_note(self, text: str, tags: list[str] | None = None):
        pass

    def find(self, note_id: str) -> Note | None:
        return self.data.get(note_id)

    def delete(self, note_id: str) -> None:
        if note_id in self.data:
            del self.data[note_id]
        else:
            raise KeyError(note_id)

    def search(self, query: str):
        pass

    def search_by_tag(self, tag: str):
        pass

    def sort_by_tag(self):
        pass

    def __str__(self):
        if not self.data:
            return "No notes yet."
        return "\n".join(str(n) for n in self.data.values())
