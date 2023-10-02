import random

class Player:
    def __init__(self):
        self.position = 0

    #No se si esto podria funcionar o habria que separar a los players clases distintas y cada uno con sus propiedades
    def setPositionP1(self):
        self.position = random.randint(0, 5)
    
    def setPositionP2(self):
        self.position = random.randint(10, 15)