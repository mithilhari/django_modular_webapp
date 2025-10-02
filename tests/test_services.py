import pytest
from core.services import create_note, latest_notes
from core.models import Note

@pytest.mark.django_db
def test_create_and_list_notes():
    create_note("Hello", "World")
    notes = latest_notes(limit=10)
    assert len(notes) == 1
    assert isinstance(notes[0], Note)
