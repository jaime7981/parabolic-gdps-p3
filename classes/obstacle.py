import random

class Obstacle:
    def __init__(self):
        self.difficulty = ""
        self.size = 0
        self.position = 0

    def setDifficulty(self, difficulty):
        if difficulty == "none":
            self.difficulty = "none"
            self.size = random.randint(0, 0.25)
        if difficulty == "easy":
            self.difficulty = "easy"
            self.size = random.randint(0.26, 0.5)
        if difficulty == "medium":
            self.difficulty = "medium"
            self.size = random.randint(0.51, 1)
        if difficulty == "hard":
            self.difficulty = "hard"
            self.size = random.randint(1.1, 1.5)

    