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
        self.font = pygame.font.SysFont('Arial', 10)

        self.enviroment = enviroment

        loaded_backgound = pygame.image.load(f'{assets_path}/background.jpg')
        self.background = pygame.transform.scale(loaded_backgound, (width, height))


    def normalize_y_position_to_floor(self, y_position: int) -> int:
        return self.height - y_position - self.background_floor


    def draw_background(self) -> None:
        self.screen.blit(self.background, (0, 0))


    def draw_obstacle(self, obstacle: Obstacle) -> None:
        if obstacle is None:
            return
        
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
            self.draw_player_health(player)


    def draw_player_health(self, player: Player) -> None:
        player_center = player.player_center()
        player_center = (
            player_center[0], 
            self.normalize_y_position_to_floor(player_center[1])
        )

        player_center = (
            player_center[0] - player.width * 5 // 2, 
            player_center[1] - player.height
        )

        pygame.draw.rect(
            self.screen, 
            'black', 
            pygame.Rect(
                player_center[0], 
                player_center[1], 
                100, 
                5
            )
        )

        pygame.draw.rect(
            self.screen,
            'red',
            pygame.Rect(
                player_center[0], 
                player_center[1], 
                player.health, 
                3
            )
        )


    def draw_mouse_position(self) -> None:
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, (0, 10, 155), (x, y), 5)


    def get_player_and_mouse_positions(self) -> tuple:
        actual_player = self.enviroment.actual_payer
        player_center = actual_player.player_center()
        player_center = (
            player_center[0], 
            self.normalize_y_position_to_floor(player_center[1])
        )

        x, y = pygame.mouse.get_pos()

        return [player_center, (x, y)]


    def draw_mouse_line_from_player(self) -> None:
        player_center, mouse_position = self.get_player_and_mouse_positions()

        pygame.draw.line(
            self.screen, 
            (0, 0, 0), 
            player_center, 
            mouse_position
        )


    def normalize_angle_label_value(self, angle: int) -> int:
        angle = abs(angle)

        if angle > 90:
            angle = 180 - angle

        return angle 


    def draw_mouse_shooting_labels(self) -> None:
        player_center, mouse_position = self.get_player_and_mouse_positions()

        velocity = self.enviroment.physics.get_distance_from_two_points(player_center, mouse_position)
        angle = self.enviroment.physics.get_angle_from_two_points(player_center, mouse_position)
        angle = self.normalize_angle_label_value(angle)

        label_1_surface = self.font.render(f'velocity: {velocity}', True, 'black')
        label_2_surface = self.font.render(f'angle: {angle}', True, 'black')
        self.screen.blit(label_1_surface, (mouse_position[0] + 15, mouse_position[1] + 15))
        self.screen.blit(label_2_surface, (mouse_position[0] + 15, mouse_position[1] + 25))


    def draw_proyectile_trajectory(self) -> None:
        player_center, mouse_position = self.get_player_and_mouse_positions()

        velocity = self.enviroment.physics.get_distance_from_two_points(player_center, mouse_position)
        angle = self.enviroment.physics.get_angle_from_two_points(player_center, mouse_position)

        proyectile = self.enviroment.create_proyecile(
            angle, 
            velocity,
            player_center
        )

        for time in range(-10, 50):
            position = proyectile.calculate_position(time / 3)

            pygame.draw.circle(self.screen, 'red', position, 1)


    def draw_proyectiles(self) -> None:
        for proyectile in self.enviroment.proyectiles:
            proyectile_position = proyectile.calculate_position_on_proyectile_time()
            proyectile.add_time()

            pygame.draw.circle(self.screen, (10, 200, 100), proyectile_position, 5)


    def shoot_projectile(self):
        player_center, mouse_position = self.get_player_and_mouse_positions()

        velocity = self.enviroment.physics.get_distance_from_two_points(player_center, mouse_position)
        angle = self.enviroment.physics.get_angle_from_two_points(player_center, mouse_position)

        self.enviroment.shoot(angle, velocity, player_center)
    

    def draw_mouse(self):
        self.draw_mouse_line_from_player()
        self.draw_mouse_position()
        self.draw_mouse_shooting_labels()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    print(f"Left click at position: ({x}, {y})")
                    self.enviroment.change_turn()
                    self.shoot_projectile()


    def run_game(self) -> None:
        while self.running:
            self.clock.tick(self.tick)
            self.check_events()

            self.draw_background()
            self.draw_players()
            self.draw_obstacle(self.enviroment.obstacle)
            self.draw_mouse()
            self.draw_proyectile_trajectory()
            self.draw_proyectiles()

            pygame.display.update()



    