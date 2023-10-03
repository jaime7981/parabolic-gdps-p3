from classes.enums import Difficulty
from random import randint
import math

class Physics():
    def __init__(self, difficulty: Difficulty = Difficulty.easy) -> None:
        self.gravity = 9.8
        self.magnitud = self.set_wind_magnitud(difficulty)

        if self.magnitud == None:
            self.set_wind_magnitud(difficulty)


    def set_wind_magnitud(self, difficulty: Difficulty = Difficulty.none):
        if difficulty == Difficulty.none:
            self.magnitud = 0

        elif difficulty == Difficulty.easy:
            self.magnitud = randint(1, 5)

        elif difficulty == Difficulty.medium:
            self.magnitud = randint(5, 10)

        elif difficulty == Difficulty.hard:
            self.magnitud = randint(10, 20)

        else:
            self.magnitud = 0
            print('error, difficulty not found')


    def get_angle_from_two_points(self, point_a: tuple, point_b: tuple) -> int:
        x1, y1 = point_a
        x2, y2 = point_b

        return int(math.degrees(math.atan2(y2 - y1, x2 - x1)))


    def get_distance_from_two_points(self, point_a: tuple, point_b: tuple) -> int:
        x1, y1 = point_a
        x2, y2 = point_b

        return int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))


    def calculate_force_x(self, angle: int, velocity: int) -> int:
        # make angle from 0 to 180
        angle = math.radians(angle)
        return int(math.cos(angle) * velocity)
    

    def calculate_force_y(self, angle: int, velocity: int) -> int:
        angle = math.radians(angle)
        return int(math.sin(angle) * velocity)


    #x(t) = ½ axt2 + v0xt + x0, retorna la posicion del proyectil en X para despues graficar
    def calculate_position_x(self, time: int, velocity: int, angle: int, initial_position_x:int = 0):
        force_x = self.calculate_force_x(angle, velocity)
        position_x = 1/2 * ((self.magnitud) * time**2) + (force_x * time) + initial_position_x
        return position_x
    

    #y(t) = -½ gt2 + v0yt + y0, retorna la posicion del proyectil en Y para despues graficar
    def calculate_position_y(self, time: int, velocity: int, angle: int, initial_position_y:int = 0):
        force_y = self.calculate_force_y(angle, velocity)
        position_y = 1/2 * (self.gravity * time**2) + (force_y * time) + initial_position_y
        return position_y