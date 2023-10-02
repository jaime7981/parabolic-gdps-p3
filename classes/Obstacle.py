from .Player import Player
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
        
    def setPosition(self, player1: Player, player2: Player):
        if player1.position > player2.position:
            self.position = (player1.position - player2.position)/2
        if player2.position > player1.position:
            self.position = (player2.position - player1.position)/2

    