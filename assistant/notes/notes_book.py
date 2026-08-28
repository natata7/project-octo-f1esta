"""NotesBook — collection of Notes, keyed by note id."""

from assistant.models.note import Note


class NotesBook:
    def __init__(self):
        self.data: dict[str, Note] = {}

    def add_note(self, text: str, tags: list[str] | None = None):
        note = Note(text, tags)
        self.data[note.id] = note
        return note

    def find(self, query: str):
        result = NotesBook.search(query)

        if result:
            return result
        else:
            return "No matches."

    def delete(self, note_id: str) -> None:
        if note_id in self.data:
            del self.data[note_id]
        else:
            print("Note not found.")
            
    def edit(self, note_id: str, new_text: str):
        if note_id in self.data:
            self.data[note_id].text = new_text
            return self.data[note_id]
        else:
            return "Note not found."

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
