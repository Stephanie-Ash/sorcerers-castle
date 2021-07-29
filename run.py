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
    PLAYER = {'name': '', 'inventory': []}

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

    make_selection(branch)


def make_selection(branch):
    """
    Ask the player to make a choice via the teminal using the 'options'
    Branches instance attribute.
    The While loop will request input until a valid choice is made.
    """
    while True:
        if len(branch.options) == 2:
            choice = input(f'{branch.opt_txt} '
                           f'({branch.options[0]}/{branch.options[1]})\n')
        else:
            choice = input(f'{branch.opt_txt} '
                           f'({branch.options[0]}/{branch.options[1]}/'
                           f'{branch.options[2]})\n')
        if validate_choice(choice, branch):
            break

    if len(branch.exit_txt) == 1:
        PLAYER['inventory'].append(choice.lower())
        exit = branch.exits[0]
        printing(f'\n\nYou take the {choice.lower()} '
                 'and place it in your bag.\n')
        printing(f'{branch.exit_txt[0]}\n\n')
    else:
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


def choose_destination(exit):
    """
    Choose the appropriate function based on the player's choice and
    so decide the route of the story.
    """
    if exit['type'] == 'game over':
        game_over()
    elif exit['route'] == 'puzzle1':
        puzzle_one()
    elif exit['route'] == 'puzzle2':
        puzzle_two()
    elif exit['route'] == 'puzzle3':
        puzzle_three()
    elif exit['route'] == 'puzzle4':
        puzzle_four()
    elif exit['type'] == 'retrace' and exit['route'] == 'b1':
        make_selection(classes.create_b1())
    elif exit['type'] == 'retrace' and exit['route'] == 'c1':
        make_selection(classes.create_c1())
    else:
        describe_location(exit['route'])


def puzzle_one():
    """
    Function to ask the player an anagram puzzle and validate input.
    If the player passes they will continue in the story.
    Otherwise it will be game over.
    """
    printing('You arrive at the castle.\n'
             'It has massive stone walls but no windows.\n'
             'There is a large wooden door in the centre of the wall.\n'
             'You try to push it open but it will not budge.\n'
             'In the centre there are a series of letters.\n'
             'The letters can be moved.\n\n'
             'They Spell out: MOON STARER\n\n')

    anagram = 'MOONSTARER'

    while True:
        answer = input('Rearrange the letters to form a single word:\n')
        if answer == '':
            print('No answer provided, please enter an answer.\n')
        elif not all(char in answer.upper() for char in anagram):
            print('\nYou must use the letters provided.\n')
        elif len(answer) != 10:
            print('\nYou must use the letters provided.\n')
        else:
            break

    if answer.upper() == 'ASTRONOMER':
        printing('You rearrange the letters and the door swings open.\n')
        describe_location(classes.create_hall())
    else:
        printing('You rearrange the letters.\n'
                 'Suddenly you hear a rush of water.\n'
                 'A raging torrent comes and washes you away.')
        game_over()


def puzzle_three():
    """
    Ask the player a number puzzle and validate their answer.
    Choose a route based on whether the answer is correct.
    """
    printing('You walk into a low ceilinged room with many windows.\n'
             'The door behind you shuts and locks.\n'
             'You look out of the windows and see you are very high up.\n'
             'How did that happen?!\n'
             'There is a trapdoor on the floor with a sign in the centre.\n'
             'It looks like a puzzle. There is a key pad next to it.\n\n'
             'The puzzle reads:\n'
             'if tree = 48 and branch = 46 what does leaf equal?\n\n')

    while True:
        answer = input('Input your answer:\n')
        try:
            int(answer)
            break
        except ValueError:
            print('\nYou must enter a number\n')

    if int(answer) == 24:
        printing('The trapdoor makes a clunking sound.\n'
                 'It opens to reveal a flight of stairs which you descend.\n')
        describe_location(classes.create_b1())
    else:
        printing('The trapdoor makes a clunking noise.\n'
                 'Suddenly the whole floor of the room disappears.\n'
                 'You fall for what seems like ages.\n')
        describe_location(classes.create_dungeon())


def puzzle_two():
    print('puzzle2')


def puzzle_four():
    print('puzzle4')


def game_over():
    print('game over')


start_game()
