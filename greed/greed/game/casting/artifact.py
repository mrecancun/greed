from game.casting.actor import Actor
from game.shared.point import Point

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact (Actor):
    def __init__(self):
        """Constructs a new artifact."""
        self._message = ""
        self._velocity = Point(0,1)

        super (). __init__ ()

    def set_message(self, message):
        """Sets the actor's message".
        
        Args:
            color (Color): The given color.
        """
        self._message = message

    def get_message(self):
        """Gets the actor's  message.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._message