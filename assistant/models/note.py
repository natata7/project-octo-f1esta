"""Note — a text note with optional tags."""


class Note:
    def __init__(self, text: str, tags: list[str] | None = None, id: str | None = None):
        self.id = id
        self.text = text
        self.tags: list[str] = []
        for tag in tags or []:
            self.add_tag(tag)

    def add_tag(self, tag: str) -> bool:
        """Add a normalized tag. Returns True if it was actually added."""
        tag = tag.strip().lower().lstrip("#")
        if not tag:
            raise ValueError("Tag cannot be empty.")
        if tag in self.tags:
            return False
        self.tags.append(tag)
        return True

    def __str__(self):
        tags = f"  [#{', #'.join(self.tags)}]" if self.tags else ""
        return f"[{self.id}] {self.text}{tags}"
