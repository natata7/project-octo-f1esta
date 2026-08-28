"""NotesBook — collection of Notes, keyed by note id."""

from assistant.models.note import Note
from assistant.utils.colors import RESET, YELLOW


class NotesBook:
    def __init__(self):
        self.data: dict[str, Note] = {}

    def _generate_id(self) -> str:
        existing = [int(k) for k in self.data if k.isdigit()]
        return str(max(existing, default=0) + 1)

    def add_note(self, text: str, tags: list[str] | None = None) -> Note:
        note = Note(text, tags, id=self._generate_id())
        self.data[note.id] = note
        return note

    def get(self, note_id: str) -> Note:
        if note_id not in self.data:
            raise KeyError(note_id)
        return self.data[note_id]

    def delete(self, note_id: str) -> None:
        if note_id not in self.data:
            raise KeyError(note_id)
        del self.data[note_id]

    def edit(self, note_id: str, new_text: str) -> Note:
        note = self.get(note_id)
        note.text = new_text
        return note

    def add_tag(self, note_id: str, tags: list[str]) -> Note:
        note = self.get(note_id)
        for tag in tags:
            note.add_tag(tag)
        return note

    def search(self, query: str) -> list[Note]:
        q = query.lower()
        return [
            note
            for note in self.data.values()
            if q in note.text.lower() or any(q in tag for tag in note.tags)
        ]

    def search_by_tag(self, tag: str) -> list[Note]:
        tag = tag.strip().lower().lstrip("#")
        return [note for note in self.data.values() if tag in note.tags]

    def sort_by_tag(self) -> list[Note]:
        """Notes with tags first (sorted alphabetically by their tags),
        untagged notes last."""
        return sorted(
            self.data.values(),
            key=lambda note: (not note.tags, sorted(note.tags), int(note.id or 0)),
        )

    def __str__(self):
        if not self.data:
            return f"{YELLOW}No notes yet.{RESET}"
        return "\n".join(str(note) for note in self.data.values())
