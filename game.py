

class Game():
    def __init__(self, difficulty) -> None:
        
        self.difficulty = difficulty


    def getDifficulty(self):
        return self.difficulty

    def setDifficulty(self, difficult):
        self.difficulty = difficult