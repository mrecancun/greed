from game.casting.actor import Actor

class Score (Actor):

    def __init__(self):
        """Constructs a new actor"""
        self._score = 0
        super (). __init__ ()

    def subtract (self):
        self._score -= 1

    def add (self):
        self._score += 1

    def get_score (self):
        return self._score 

        
