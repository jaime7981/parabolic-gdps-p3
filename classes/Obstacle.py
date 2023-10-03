
class Obstacle():
    def __init__(self, width, height, position  = [0, 0], obstacle_color = 'black') -> None:
        self.width = width
        self.height = height

        self.position = position

        self.color = obstacle_color


    def set_position(self, position) -> None:
        self.position = position


    def __str__(self) -> str:
        return f'position: {self.position}, width: {self.width}, height: {self.height}'
