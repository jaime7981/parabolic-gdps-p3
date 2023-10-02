import random

class Wind:
    def __init__(self):
        self.magnitud = 0
        self.gravity = 9.8
        
    def setMagnitud(self, difficulty):
        if difficulty == "none":
            self.magnitud = 0
        if difficulty == "easy":
            self.magnitud = random.randint(0.1, 0.5)
        if difficulty == "medium":
            self.magnitud = random.randint(0.51, 1)
        if difficulty == "hard":
            self.magnitud == random.randint(1, 2)