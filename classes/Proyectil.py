from classes.Physics import Physics
from classes.Player import Player

class Proyectil:
    def __init__(self, angle, velocity, physics: Physics = Physics(), start_position: tuple = (0, 0), shooting_player: Player = None, damage: int = 10) -> None:
        self.physics = physics

        self.angle = angle
        self.velocity = velocity
        self.initial_position = start_position
        self.position = start_position

        self.time = 0

        self.radius = 5
        self.color = (10, 200, 100)
        self.damage = damage
        self.wheight = self.radius // 2

        self.shooting_player = shooting_player

    
    def set_angle(self, angle: int):
        self.angle = angle

    
    def set_velocity(self, velocity: int):
        self.velocity = velocity


    def reset_time(self):
        self.time = 0


    def add_time(self):
        self.time += 0.1
        self.damage = int(abs(self.physics.calculate_damage(self.time, self.velocity, self.angle) ** (1/self.wheight)))


    def calculate_position_on_proyectile_time(self):
        return self.calculate_position(self.time)


    def calculate_position(self, time: int):
        x = self.physics.calculate_position_x(time, self.velocity, self.angle, self.initial_position[0])
        y = self.physics.calculate_position_y(time, self.velocity, self.angle, self.initial_position[1])

        return (x, y)