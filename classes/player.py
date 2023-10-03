
class Player:
    def __init__(self, width = 20, height = 40, position = (0, 0), player_color = 'blue', health = 100, player_name = 'default_player') -> None:
        self.player_name = player_name

        self.width = width
        self.height = height

        self.player_position = position

        self.color = player_color

        self.health = health

    
    def set_position(self, position) -> None:
        self.player_position = position


    def set_width(self, width) -> None:
        self.width = width


    def set_height(self, height) -> None:
        self.height = height


    def set_dimensions(self, width, height) -> None:
        self.set_width(width)
        self.set_height(height)


    def set_health(self, health) -> None:
        self.health = health


    def substrac_health(self, damage) -> None:
        self.health -= damage


    def player_center(self) -> tuple:
        return (self.player_position[0] + self.width // 2, self.player_position[1] + self.height // 2)


    def __str__(self) -> str:
        return self.player_name
    

    def __repr__(self) -> str:
        return f'name: {self.player_name}, position: {self.player_position}'
