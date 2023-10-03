import pygame

from classes.Enviroment import Enviroment
from classes.Obstacle import Obstacle
from classes.Player import Player
from classes.Proyectil import Proyectil


class GUI():
    def __init__(self, enviroment: Enviroment, width = 500, height = 500, assets_path = './assets', background_floor = 88) -> None:
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tick = 60

        self.width = width
        self.height = height
        self.background_floor = background_floor

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 72)

        self.enviroment = enviroment

        loaded_backgound = pygame.image.load(f'{assets_path}/background.jpg')
        self.background = pygame.transform.scale(loaded_backgound, (width, height))


    def normalize_y_position_to_floor(self, y_position: int) -> int:
        return self.height - y_position - self.background_floor


    def draw_background(self) -> None:
        self.screen.blit(self.background, (0, 0))


    def draw_obstacle(self, obstacle: Obstacle) -> None:
        rect = pygame.Rect(
            obstacle.position[0], 
            self.normalize_y_position_to_floor(obstacle.position[1]) - obstacle.height, 
            obstacle.width, 
            obstacle.height
        )

        pygame.draw.rect(
            self.screen, 
            obstacle.color, 
            rect
        )


    def draw_player(self, player: Player) -> None:
        rect = pygame.Rect(
            player.player_position[0], 
            self.normalize_y_position_to_floor(player.player_position[1]) - player.height, 
            player.width, 
            player.height
        )

        pygame.draw.rect(
            self.screen, 
            player.color, 
            rect
        )


    def draw_players(self) -> None:
        for player in self.enviroment.players:
            self.draw_player(player)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def run_game(self) -> None:
        while self.running:
            self.clock.tick(self.tick)
            self.check_events()

            self.draw_background()
            self.draw_players()
            self.draw_obstacle(self.enviroment.obstacle)

            pygame.display.update()



    