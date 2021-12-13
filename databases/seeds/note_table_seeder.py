"""NoteTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Note import Note


class NoteTableSeeder(Seeder):
    def run(self):
        Note.create({"title": "Hello", "body": "world"})
