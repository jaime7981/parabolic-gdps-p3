
class Player():
    def __init__(self, position = (0, 0), player_name = 'default_player') -> None:
        self.player_name = player_name
        self.player_position = position

    
    def set_position(self, position) -> None:
        self.player_position = position


    def __str__(self) -> str:
        return self.player_name
    

    def __repr__(self) -> str:
        return f'name: {self.player_name}, position: {self.player_position}'