'''Random is used to randomly place ships in gameboard and sys is used
to exit the game upon users request  '''
import random
import sys


def create_random_ship():
    '''
    Creates a random position within the board to place the target
    '''
    return random.randint(0, 5), random.randint(0, 5)


print("Welcome to Battleships!")

player = input('Please Enter Your Name: ')
while not player.isalpha():
    print('Invalid Entry, Try Again: ')
    player = input('Please Enter Your Name: ')

print(f"""\n{player}, you have 15 missles and there are 3 ships on the map.
In order to hit them, you have
to enter specific numbers for that location.\n
Example: For the first row and first column.
You have to write 1 and 1.
\nGOODLUCK!\n""")


def play_game():
    '''
    Guesses and checks with data validation. This function is the code for the
    gameplay.
    '''
    print("Let's Begin\n")
    game_board = [["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"],
                  ["O", "O", "O", "O", "O"]]

    for i in game_board:
        print(*i)

    ship1 = create_random_ship()
    ship2 = create_random_ship()
    ship3 = create_random_ship()
    ships_left = 3
    ammo = 15

    while ammo:
        try:
            row = int(input("Row: "))
            column = int(input("Col: "))
        except ValueError:
            print(f"{player}, only enter numbers between 1-5!")
            continue

        if row not in range(1, 6) or column not in range(1, 6):
            print(f"{player}, the numbers must be between 1-5!")
            continue

        row = row - 1
        column = column - 1

        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print(f"{player}, you have already tried that spot.")
            continue
        elif (row, column) == ship1 or (row, column) == ship2:
            print((f"STRIKE! You still have {ammo} missles remaining!"))
            print(f"Ships left: {ships_left}")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                for i in game_board:
                    print(*i)
                print('Game Over!')
                print(f"CONGRATS {player}! You WON with {ammo} missles left")
                play_again()
        elif (row, column) == ship3:
            print(f"STRIKE! You still have {ammo} missles remaining!")
            print(f"Ships left: {ships_left}")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                for i in game_board:
                    print(*i)
            print('Game Over!')
            print(f"Ships left: {ships_left}")
            print(f"CONGRATS {player}! You WON with {ammo} missles left")
            play_again()
        else:
            ammo -= 1
            print(f"Oh No! Missed! You have {ammo} missles remaining")
            print(f"Ships left: {ships_left}")
            game_board[row][column] = "-"

        for i in game_board:
            print(*i)

    play_again()


def play_again():
    '''
    Start a new game or exit the program
    '''
    another_game = input("Play Again? <y>es or <n>o?: ").lower()
    if another_game == "y":
        play_game()
    elif another_game == 'n':
        print(f'Thanks for playing {player}')
        sys.exit()
    elif another_game != 'y' or 'n':
        print('Enter "y/Y" for yes or "n/N" for no')
        play_again()


if __name__ == "__main__":
    play_game()
