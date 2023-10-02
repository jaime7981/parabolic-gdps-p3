from classes.Obstacle import Obstacle
from classes.enums import Difficulty

from random import randint

GRAVITY = 9.8
PLAYER_HEIGHT = 10 ## in pixels
PLAYER_WIDTH = 5 ## in pixels

class Game():
    def __init__(self, width_limits = (0,500), height_limits = (0, 500), obstacle_diff = Difficulty.easy, wind_diff = Difficulty.easy) -> None:
        self.players = []

        self.width_limits = width_limits
        self.height_limits = height_limits

        self.obstacle_diff = obstacle_diff
        self.wind_diff = wind_diff

        self.obstacle = self.create_obstacle()


    def add_player(self, player) -> bool:
        if len(self.players) <= 2:
            self.players.append(player)
            return True
        else:
            print('Max players reached!')
            return False
        

    def create_obstacle(self) -> None:
        if self.obstacle_diff == Difficulty.easy:
            width, height = (randint(PLAYER_WIDTH // 2, PLAYER_WIDTH), randint(PLAYER_HEIGHT // 2, PLAYER_HEIGHT))
            print('Easy obstacle created!')
            return Obstacle(width, height)
        
        elif self.obstacle_diff == Difficulty.medium:
            width, height = (randint(PLAYER_WIDTH, PLAYER_WIDTH * 2), randint(PLAYER_HEIGHT, PLAYER_HEIGHT * 2))
            print('Medium obstacle created!')
            return Obstacle(width, height)
        
        elif self.obstacle_diff == Difficulty.hard:
            width, height = (randint(PLAYER_WIDTH * 2, PLAYER_WIDTH * 3), randint(PLAYER_HEIGHT * 2, PLAYER_HEIGHT * 3))
            print('Hard obstacle created!')
            return Obstacle(width, height)
        
        elif self.obstacle_diff == Difficulty.none:
            print('No obstacle created!')
            return None
        

    def setup_positions(self) -> bool:
        if len(self.players) == 2:
            self.players[0].set_position(
                (
                    randint(self.width_limits[0], self.width_limits[1] // 4), 
                    0
                )
            )

            self.players[1].set_position(
                (
                    randint(3 * self.width_limits[1] // 4, self.width_limits[1]), 
                    0
                )
            )
        else:
            print('Not enough players to setup positions!')
            raise Exception('Not enough players to setup positions!')
        
        if self.obstacle != None:
            self.obstacle.set_position(
                (
                    randint(self.width_limits[1] // 4, 3 * self.width_limits[1] // 4), 
                    0
                )
            )

        return True
        

    def start_game(self) -> None:
        self.setup_positions()

        print('Game started!')
        print('Players: ', self.players)
        print('Obstacle: ', self.obstacle)
        print('Wind: ', self.wind_diff)
        print('Gravity: ', GRAVITY)
        print('Width limits: ', self.width_limits)
        print('Height limits: ', self.height_limits)


    def __str__(self) -> str:
        return f'Game: {self.players}, {self.obstacle}, {self.wind_diff}, {GRAVITY}, {self.width_limits}, {self.height_limits}'