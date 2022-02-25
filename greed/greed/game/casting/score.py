from game.casting.actor import Actor

class Score (Actor):

    def __init__(self):
        """Constructs a new actor"""
        self._score = 0
        """Inherits __init__ from the Actor class"""
        super (). __init__ ()

    def subtract (self):
        """Substracts the score by 1"""
        self._score -= 1

    def add (self):
        """Adds the score by 1"""
        self._score += 1

    def get_score (self):
        """Returns the score as its current value"""
        return self._score 

        

