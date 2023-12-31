from classes.Obstacle import Obstacle
from classes.Proyectil import Proyectil
from classes.Physics import Physics
from classes.enums import Difficulty

from random import randint

PLAYER_HEIGHT = 40 ## in pixels
PLAYER_WIDTH = 20 ## in pixels

class Enviroment():
    def __init__(self, width_limits = (0,500), height_limits = (0, 500), obstacle_diff = Difficulty.easy, wind_diff = Difficulty.easy) -> None:
        self.players = []
        self.actual_payer = None
        self.turns = 0

        self.proyectiles = []

        self.width_limits = width_limits
        self.height_limits = height_limits

        self.obstacle_diff = obstacle_diff
        self.wind_diff = wind_diff

        self.physics = Physics(self.wind_diff)

        self.obstacle = self.create_obstacle()


    def add_player(self, player) -> bool:
        if len(self.players) <= 2:
            player.set_dimensions(PLAYER_WIDTH, PLAYER_HEIGHT)
            self.players.append(player)
            return True
        else:
            print('Max players reached!')
            return False
        

    def change_turn(self) -> None:
        self.turns += 1
        self.actual_payer = self.players[self.turns % len(self.players)]
        
        return self.actual_payer
        

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
    

    def create_proyecile(self, angle, velocity, player_center) -> None:
        proyectile = Proyectil(
            angle, 
            velocity, 
            self.physics, 
            player_center,
            self.actual_payer
        )

        return proyectile
    

    def shoot(self, angle, velocity, player_center) -> None:
        proyectile = self.create_proyecile(angle, velocity, player_center)

        self.proyectiles.append(proyectile)

        return proyectile

    def move_proyectiles(self) -> None:
        for proyectile in self.proyectiles:
            proyectile.add_time()
            proyectile.position = proyectile.calculate_position(proyectile.time)

            if proyectile.time > 100:
                self.proyectiles.remove(proyectile)

    
    def check_proyectiles_collisions(self, normalize_position) -> None:
        for proyectile in self.proyectiles:
            proyectile_position = proyectile.calculate_position_on_proyectile_time()

            if self.obstacle_diff != Difficulty.none:
                if self.physics.is_circle_inside_rectangle(
                        proyectile_position,
                        proyectile.radius,
                        self.obstacle.width,
                        self.obstacle.height,
                        (
                            self.obstacle.position[0],
                            normalize_position(self.obstacle.position[1] + self.obstacle.height)
                        )
                    ):
                    self.proyectiles.remove(proyectile)
                    print('Obstacle hit!')

            for player in self.players:
                if self.physics.is_circle_inside_rectangle(
                        proyectile_position, 
                        proyectile.radius, 
                        player.width, 
                        player.height, 
                        (
                            player.player_position[0],
                            normalize_position(player.player_position[1] + player.height)
                        )
                    ) and player != proyectile.shooting_player:
                    player.substrac_health(proyectile.damage)
                    print(f'Player hit! {proyectile.damage} damage!')
                    self.proyectiles.remove(proyectile)
        

    def start_game(self) -> None:
        self.setup_positions()
        self.actual_payer = self.players[0]

        print('Game started!')
        print('Players: ', self.players)
        print('Obstacle: ', self.obstacle)
        print('Wind: ', self.wind_diff)
        print('Width limits: ', self.width_limits)
        print('Height limits: ', self.height_limits)


    def check_game_end(self) -> bool:
        for player in self.players:
            if player.health <= 0:
                return (
                    True, 
                    {
                        'looser' : player,
                        'winner' : self.get_winner()
                    }
                )
        
        return (False, None)
    

    def get_winner(self) -> None:
        for player in self.players:
            if player.health > 0:
                return player


    def __str__(self) -> str:
        return f'Game: {self.players}, {self.obstacle}, {self.wind_diff}, {self.width_limits}, {self.height_limits}'