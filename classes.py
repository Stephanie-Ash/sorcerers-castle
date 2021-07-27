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
