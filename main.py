from classes.Enviroment import Enviroment
from classes.Player import Player
from classes.enums import Difficulty
from classes.GUI import GUI

def validate_input(input):
    if input == '0' or input == '1' or input == '2' or input == '3':
        return True
    else:
        return False
    
def initial_setup() -> (Difficulty, Difficulty):
    
    while True:
        print("\nNone -> 0\nEasy -> 1\nMedium -> 2\nHard -> 3\n")
        obstacle_diff = input('Enter obstacle difficulty [0-3]: ')
        wind_diff = input('Enter wind difficulty [0-3]: ')
        
        # obstacle_diff = '1'
        # wind_diff = '1'

        if validate_input(obstacle_diff) and validate_input(wind_diff):
            obstacle_diff = int(obstacle_diff)
            wind_diff = int(wind_diff)
            return (Difficulty(obstacle_diff), Difficulty(wind_diff))
        
        else:
            print('Invalid input!\n')
            continue

def main():
    player_1 = Player(player_name = 'player_1')
    player_2 = Player(player_name = 'player_2')
    
    obstacle_diff, wind_diff = initial_setup()

    game = Enviroment(obstacle_diff = obstacle_diff, wind_diff = wind_diff)

    game.add_player(player_1)
    game.add_player(player_2)

    game.start_game()

    print(game)

    gui = GUI(game)
    gui.run_game()


if __name__ == '__main__':
    main()
