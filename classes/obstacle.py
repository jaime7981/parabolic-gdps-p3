
class Obstacle():
    def __init__(self, width, height, position  = (0, 0)) -> None:
        self.width = width
        self.height = height

        self.position = position


    def set_position(self, position) -> None:
        self.position = position
