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
    Guesses and checks with data validation
    '''


if __name__ == "__main__":
    play_game()
