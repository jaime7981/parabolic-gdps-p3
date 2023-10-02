from classes.Enviroment import Enviroment
from classes.Player import Player

def main():
    player_1 = Player(player_name = 'player_1')
    player_2 = Player(player_name = 'player_2')

    game = Enviroment()

    game.add_player(player_1)
    game.add_player(player_2)

    game.start_game()

    print(game)

if __name__ == '__main__':
    main()
