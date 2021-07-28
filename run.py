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
    and introductory text.
    """
    printing("*****************************************\n")
    printing("*         The Sorcerer's Castle         *\n")
    printing("*****************************************\n\n")

    printing('"Zzzz"\n'
             'You are sleeping peacefully under a tree when you are\n'
             'rudely awakened by a woman stumbling over you.\n'
             'She has the pointy ears of an elf and wears a green cloak.\n'
             'Upon seeing you she sighs in relief.\n\n')

    create_player()


def create_player():
    """
    Request a name from the player and add it to
    the player dictionary. While loop will ensure a name is given.
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
    printing('\n\n')
    printing(f'"{PLAYER["name"]} the forest of high elms needs your help.\n')

    describe_location(classes.create_intro())


def describe_location(branch):
    """
    Provide an initial description of the area and
    give a description of the choices the player will have to make,
    before calling the selection functions.
    Will run for all standard story Branches.
    """
    printing(f'{branch.int_txt}\n\n')
    printing(f'{branch.choice_txt}\n\n')

    if len(branch.options) == 2:
        make_selection_two(branch)
    else:
        make_selection_three(branch)


def make_selection_two(branch):
    """
    Ask the player to make a choice via the teminal using the 'options'
    Branches instance attribute.
    The While loop will request input until a valid choice is made.
    """

    while True:
        choice = input(f'{branch.opt_txt} '
                       f'({branch.options[0]}/{branch.options[1]})\n')
        if validate_choice(choice, branch):
            break

    for i, j, k in zip(branch.options, branch.exits, branch.exit_txt):
        if choice.lower() == i:
            exit = j
            exit_text = k
            printing(f'\n{exit_text}\n\n')

    choose_destination(exit)


def validate_choice(selection, branch):
    """
    Check the user input from the make_selection functions.
    Print error messages if not valid.
    """
    user_choice = selection.lower()
    if user_choice == "":
        print('You must enter an option to continue.\n')
        return False
    elif user_choice not in branch.options:
        print(f'\n{user_choice} is not one of the options. Try again.\n')
        return False
    else:
        return True


start_game()
