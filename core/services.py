# Business logic (kept separate for unit testing and modularity)
from .models import Note

def create_note(title: str, body: str) -> Note:
    return Note.objects.create(title=title, body=body)

def latest_notes(limit: int = 5):
    return list(Note.objects.order_by("-created_at")[:limit])
