from classes.game import Game
from classes.player import Player

def main():
    player_1 = Player(player_name = 'player_1')
    player_2 = Player(player_name = 'player_2')

    game = Game()

    game.add_player(player_1)
    game.add_player(player_2)

    game.start_game()

    print(game)

if __name__ == '__main__':
    main()
