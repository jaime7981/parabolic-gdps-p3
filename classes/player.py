import random

class Player:
    def __init__(self, position = (0, 0), player_name = 'default_player') -> None:
        self.player_name = player_name
        self.player_position = position
        self.position = 0

    def __str__(self) -> str:
        return self.player_name
    

    def __repr__(self) -> str:
        return self.player_name    
    
    #No se si esto podria funcionar o habria que separar a los players clases distintas y cada uno con sus propiedades
    def setPositionP1(self):
        self.position = random.randint(0, 5)
    
    def setPositionP2(self):
        self.position = random.randint(10, 15)