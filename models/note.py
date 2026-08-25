"""Note — a text note with optional tags (tags are the bonus-part feature)."""

class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content