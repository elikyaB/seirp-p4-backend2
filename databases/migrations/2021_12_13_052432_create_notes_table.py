"""CreateNotesTable Migration."""

from masoniteorm.migrations import Migration


class CreateNotesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("notes") as table:
            table.increments("id")
            table.string("title")
            table.string("body")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("notes")
