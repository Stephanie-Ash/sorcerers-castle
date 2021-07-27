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
