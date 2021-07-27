import inspect


# Classes containing text and player options
# for most of the story

class Branches:
    """
    Creates an instance of Branches.
    Will contain the story text on entrance and exit of the branch,
    player options, and next branches in the story
    for standard player choice points.
    """
    def __init__(self, int_txt, choice_txt, options, opt_txt, exits, exit_txt):
        self.int_txt = int_txt
        self.choice_txt = choice_txt
        self.options = options
        self.opt_txt = opt_txt
        self.exits = exits
        self.exit_txt = exit_txt


def create_intro():
    """
    Create the intro Branches object
    """
    int_txt = inspect.cleandoc("""
    ""The Forest of High Elms needs your help.
    The Evil Sourcerer has poisoned the Tree of Life and the forest is dying.
    He has locked the antidote in his castle"" """)
    choice_txt = '"Will you embark on a quest to retrieve it for us?"'
    options = ['yes', 'no']
    opt_txt = 'Do you help?'
    exits = ['ITEM_ONE', 'INTRO_NO']
    exit_txt = []
    exit_txt.append('"Thank you, I know you will save our forest."')
    exit_txt.append('"No?! What a big coward you are!"')

    intro = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return intro


def create_intro_no():
    """
    Create the intro_no Branches object
    """
    int_txt = '"The tree of life will not last much longer."'
    choice_txt = '"Please change your mind, the forest is counting on you!"'
    options = ['yes', 'no']
    opt_txt = 'Do you help?'
    exits = ['ITEM_ONE', 'game_over']
    exit_txt = []
    exit_txt.append('"Thank you, I know you will save our forest."')
    exit_txt.append('The elven woman runs off in a huff.')

    intro_no = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return intro_no


def create_hall():
    """
    Create the hall Branches object
    """
    int_txt = 'You walk into a dark hallway.'
    choice_txt = 'There are two doors, one to the left and one to the right.'
    options = ['left', 'right']
    opt_txt = 'Which door do you choose?'
    exits = ['PUZZLE2', 'PUZZLE3']
    exit_txt = []
    exit_txt.append('You open the door to the left.')
    exit_txt.append('You open the door to the right.')

    hall = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return hall


def create_dungeon():
    """
    Create the dungeon Branches object
    """
    int_txt = inspect.cleandoc("""
    You land with a bump in a cold dark dungeon.
    You see that there is a door set high in the wall in accross from you.
    You search around for something to help you climb.""")
    choice_txt = 'You find a metal hook on a rope and an old wooden ladder.'
    options = ['rope', 'ladder']
    opt_txt = 'Which item do you use?'
    exits = ['A1', 'game_over']
    exit_txt = []
    exit_txt.append('You grab the rope, swing it around your head '
                    'and throw it towards the door.\n'
                    'The hook connects and gets lodged.\n'
                    'You climb the rope and go through the door.\n')
    exit_txt.append('You prop the ladder against the wall '
                    'and start climbing.\nYou are almost at the top '
                    'when the steps break and you fall.')

    dungeon = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return dungeon
