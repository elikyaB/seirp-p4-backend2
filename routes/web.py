"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup
ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "NoteController@index").name("index"),
        Get("/@id", "NoteController@show").name("show"),
        Post('/', "NoteController@create").name("create"),
        Put('/@id', "NoteController@update").name("update"),
        Delete('/@id', "NoteController@destroy").name("destroy")
    ], prefix="/notes", name="notes")
]
