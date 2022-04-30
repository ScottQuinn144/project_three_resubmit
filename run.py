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


def play_again():
    '''
    Start a new game or exit the program
    '''


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
        elif (row, column) == ship1 or ship2 or ship3:
            print((f"STRIKE! You still have {ammo} missles remaining!"))
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print('Game Over!')
                print(f"CONGRATS {player}! You WON with {ammo} missles left")
                play_again()

        for i in game_board:
            print(*i)


if __name__ == "__main__":
    play_game()
