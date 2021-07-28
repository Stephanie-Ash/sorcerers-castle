import classes
import time
import sys


# Code Credit:
# https://stackoverflow.com/questions/4627033/printing-a-string-with-a-little-delay-between-the-chars
# Function based on https://github.com/roomacarthur/escape-the-cave
# by Ruairidh MacArthur
def printing(text):
    """
    Function to control the speed of the print statements
    for more dynamic story telling.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


def start_game():
    """
    Start the game. Print the game title
    and introductory text
    """
    printing("*****************************************\n")
    printing("*         The Sorcerer's Castle         *\n")
    printing("*****************************************\n\n")

    printing('"Zzzz"\n'
             'You are sleeping peacefully under a tree when you are\n'
             'rudely awaken by a woman stumbling over you.\n'
             'She has the pointy ears of an elf and wears a green cloak.\n'
             'Upon seeing you she sighs in relief.\n\n')

    create_player()


def create_player():
    """
    Request a name from the player and add it to
    the player dictionary.
    """
    global PLAYER
    PLAYER = {'name': '', 'Inventory': []}

    printing('"Thank stars I have found someone"\n')

    while True:
        name = input('"What is your name?"\n')
        if name == '':
            print('No name provided, please enter a name.\n')
        else:
            break

    PLAYER['name'] = name


start_game()
print(PLAYER)
