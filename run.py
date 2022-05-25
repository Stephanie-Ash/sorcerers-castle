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
        time.sleep(0.018)


def start_game():
    """
    Start the game. Print the game title
    and introductory text.
    """
    text = ("********************************************************\n"
            "*                The Sorcerer's Castle                *\n"
            "*            _   _   _            _   _   _            *\n"
            "*           | |_| |_| |          | |_| |_| |           *\n"
            "*           |         |__________|         |           *\n"
            "*           |                              |           *\n"
            "*           |           ________           |           *\n"
            "*           |          |        |          |           *\n"
            "*           |          |        |          |           *\n"
            "*           |          |        |          |           *\n"
            "*           |          |________|          |           *\n"
            "*           |______________________________|           *\n"
            "*                                                      *\n"
            "* Type responses using the keyboard then press return  *\n"
            "********************************************************\n\n")

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

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

    printing('"Thank stars I have found someone."\n')

    while True:
        name = input('"What is your name?":\n')
        if name == '':
            print('No name provided, please enter a name.\n')
        else:
            break

    PLAYER['name'] = name
    printing('\n\n')
    printing(f'"{PLAYER["name"]} the forest of High Elms needs your help.\n')

    describe_location(classes.create_intro())


def describe_location(branch):
    """
    Provide an initial description of the area and
    give a description of the choices the player will have to make,
    before calling the selection functions.
    Will run for all standard story or item Branches.
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
                           f'({branch.options[0]}/{branch.options[1]}):\n')
        else:
            choice = input(f'{branch.opt_txt} '
                           f'({branch.options[0]}/{branch.options[1]}/'
                           f'{branch.options[2]}):\n')
        if validate_choice(choice, branch):
            break

    if len(branch.exit_txt) == 1:
        PLAYER['inventory'].append(choice.lower())
        exit = branch.exits[0]
        printing(f'\n\nYou take the {choice.lower()} '
                 'and place it in your bag.\n')
        printing('Your bag now contains the following: ')
        print(*PLAYER['inventory'], sep=", ")
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
    Check the user input from the make_selection function.
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
    elif exit['route'] == 'end_room':
        end_room()
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
    printing(classes.PuzzleStrings.puzz_one1)

    anagram = 'MOONSTARER'

    while True:
        answer = input('Rearrange the letters to form a single word:\n')
        if answer == '':
            print('No answer provided, please enter an answer.\n')
        elif not all(char in anagram for char in answer.upper()):
            print('\nYou must use the letters provided.\n')
        elif len(answer) != 10:
            print('\nYour answer must be 10 letters in length.\n')
        else:
            break

    if answer.upper() == 'ASTRONOMER':
        printing(classes.PuzzleStrings.puzz_one2)
        describe_location(classes.create_hall())
    else:
        printing(classes.PuzzleStrings.puzz_one3)
        game_over()


def puzzle_two():
    """
    Ask the player a word puzzle and validate their input.
    Choose route  based on whether the answer is correct.
    """
    printing(classes.PuzzleStrings.puzz_two1)

    while True:
        answer = input('Enter your answer:\n')
        if answer == '':
            print('No answer provided, please enter an answer.\n')
        elif not answer.isalpha():
            print('\nYour answer must only include letters.\n')
        elif len(answer) != 8:
            print('\nYour answer must be 8 letters in length.\n')
        else:
            break

    if answer.upper() == 'INDUSTRY':
        printing(classes.PuzzleStrings.puzz_two2)
        describe_location(classes.create_a1())
    else:
        printing(classes.PuzzleStrings.puzz_two3)
        describe_location(classes.create_dungeon())


def puzzle_three():
    """
    Ask the player a number puzzle and validate their answer.
    Choose a route based on whether the answer is correct.
    """
    printing(classes.PuzzleStrings.puzz_three1)

    while True:
        answer = input('Enter your answer:\n')

        if validate_answer(answer):
            break

    if int(answer) == 24:
        printing(classes.PuzzleStrings.puzz_three2)
        describe_location(classes.create_b1())
    else:
        printing(classes.PuzzleStrings.puzz_three3)
        describe_location(classes.create_dungeon())


def puzzle_four():
    """
    Ask the player a final number puzzle.
    Validate their input.
    If correct continue to the final item select, else game over.
    """
    printing(classes.PuzzleStrings.puzz_four1)

    while True:
        answer = input('Enter your answer:\n')

        if validate_answer(answer):
            break

    if int(answer) == 8:
        describe_location(classes.create_item3())
    else:
        printing(classes.PuzzleStrings.puzz_four2)
        game_over()


def validate_answer(answer):
    try:
        int(answer)
    except ValueError:
        print('\nYou must enter a number\n')
        return False

    return True


def end_room():
    """
    Final destination. Decide whether the player wins or loses
    based on if the correct items are in the inventory of the
    PLAYER dictionary.
    """
    printing(classes.EndRoomStrings.end_room1)

    if 'sledgehammer' not in PLAYER['inventory']:
        printing(classes.EndRoomStrings.end_room2)
        game_over()
    else:
        printing(classes.EndRoomStrings.end_room3)
        printing(classes.EndRoomStrings.end_room4)
        if 'axe' not in PLAYER['inventory']:
            printing(classes.EndRoomStrings.end_room5)
            game_over()
        else:
            printing(classes.EndRoomStrings.end_room6)
            printing(classes.EndRoomStrings.end_room7)
            if 'waterskin' not in PLAYER['inventory']:
                printing(classes.EndRoomStrings.end_room8)
                game_over()
            else:
                printing(classes.EndRoomStrings.end_room9)
                printing(f'Congratulations {PLAYER["name"]}! '
                         'You have saved the forest.\n\n')
                win_game()


def win_game():
    """
    Print a message when the player wins
    """
    text = ("*********************************************************\n"
            "*                      ,@@@@@@@,                        *\n"
            "*              ,,,.   ,@@@@@@/@@,  .oo8888o.            *\n"
            "*           ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o           *\n"
            "*          ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'          *\n"
            "*          %&&%&%&/%&&%@@\@@/ /@@@88888\88888'          *\n"
            "*          %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'           *\n"
            "*          `&%\ ` /%&'    | |        \ '|8'             *\n"
            "*              | |        | |         | |               *\n"
            "*              | |        | |         | |               *\n"
            "*         jgs /   \      /   \       /   \              *\n"
            "*                                                       *\n"
            "*********************************************************\n")

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)


def game_over():
    """
    Print a game over message when the player chooses the
    wrong option.
    """
    text = ("*********************************************************\n"
            "*   _____                         ____                  *\n"
            "*  / ____|                       / __ \                 *\n"
            "* | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __  *\n"
            "* | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| *\n"
            "* | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |    *\n"
            "*  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|    *\n"
            "*                                                       *\n"
            "*********************************************************\n\n")

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

    print("To play again click 'Play Game'.")


start_game()
