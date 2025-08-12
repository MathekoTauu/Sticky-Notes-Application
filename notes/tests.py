from django.test import TestCase
from .models import Note
from django.urls import reverse

class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Test Note", content="This is a test.")

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test.")