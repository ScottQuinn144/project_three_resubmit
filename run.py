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
