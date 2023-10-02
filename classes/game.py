from enums import Difficulty

GRAVITY = 9.8

class Game():
    def __init__(self, obstacle = Difficulty.easy, wind = Difficulty.easy) -> None:
        self.players = []

        self.obstacle = obstacle
        self.wind = wind


    def add_player(self, player) -> bool:
        if len(self.players) <= 2:
            self.players.append(player)
            return True
        else:
            print('Max players reached!')
            return False