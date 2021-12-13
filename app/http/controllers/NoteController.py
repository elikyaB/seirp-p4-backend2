""" A NoteController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Note import Note


class NoteController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Note.find(id)

    def index(self):
        return Note.all()

    def create(self):
        title = self.request.input("title")
        body = self.request.input("body")
        note = Note.create({"title": title, "body": body})
        return note

    def update(self):
        title = self.request.input("title")
        body = self.request.input("body")
        id = self.request.param("id")
        Note.where("id", id).update({"title": title, "body": body})
        return Note.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        note = Note.where("id", id).get()
        Note.where("id", id).delete()
        return note