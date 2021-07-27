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
    int_txt = ('"The Forest of High Elms needs your help.\n'
               'The Evil Sourcerer has poisoned the Tree of Life '
               'and the forest is dying.\n'
               'He has locked the antidote in his castle."')
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
    int_txt = ('You land with a bump in a cold dark dungeon.\n'
               'As your eyes adjust you see that there is a door '
               'set high in the wall in accross from you.\n'
               'You search around for something to help you climb.')
    choice_txt = 'You find a metal hook on a rope and an old wooden ladder.'
    options = ['rope', 'ladder']
    opt_txt = 'Which item do you use?'
    exits = ['C1', 'game_over']
    exit_txt = []
    exit_txt.append('You grab the rope, swing it around your head '
                    'and throw it towards the door.\n'
                    'The hook connects and gets lodged.\n'
                    'You climb the rope and go through the door.')
    exit_txt.append('You prop the ladder against the wall '
                    'and start climbing.\nYou are almost at the top '
                    'when the steps break and you fall.')

    dungeon = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return dungeon


# A route followed if Puzzle2 is passed.
def create_A1():
    """
    Create the A1 Branches object.
    """
    int_txt = ('You find yourself in a...jungle!\n'
               'The trees are tightly packed together and wild looking,\n'
               'with many strong looking vines hanging from them.\n'
               'There is a quickly flowing river running through the trees.\n'
               'You spy a boat tied at the edge of the river')
    choice_txt = ('Do you:\n'
                  'a. Swing through the trees using the vines?\n'
                  'b. Try your luck with the boat?')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = ['A2', 'A3']
    exit_txt = []
    exit_txt.append('You climb onto the nearest sturdy looking vine '
                    'and start swinging.')
    exit_txt.append('You climb into the boat and speed down the river.')

    A1 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return A1


def create_A2():
    """
    Create the A2 Branches object
    """
    int_txt = ('You are making great progress until you suddenly swing '
               'into a clearing.\nwithout the next vine to grab onto '
               'you swing back into a tree and drop to the floor.\n'
               'Just as you are about to walk across the clearing you '
               'spy a jaguar loitering on the edge')
    choice_txt = ('Do you:\n'
                  'a. Create a distraction?\n'
                  'b. Try to sneak past the jaguar?')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = ['SPRITE', 'game_over']
    exit_txt = []
    exit_txt.append('You throw a branch into the distant trees.\n'
                    'The jaguar takes off after it and you run.\n'
                    'All of a sudden you come to a steep hill.\n'
                    'You tumble down and land next to a pool of water.\n'
                    'There is a door ahead.')
    exit_txt.append('You continue quietly.\n'
                    'Just as you make it past the jaguar "snap" you stand '
                    'on a branch.\nThe jaguar grabs you.')

    A2 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return A2


def create_A3():
    """
    Create the A3 Branches object
    """
    int_txt = ('Your journey gets rougher as you travel through rapids.\n'
               'You see a steep drop, almost waterfall ahead.\n'
               'There is a rock coming up on your left.')
    choice_txt = ('Do you:\n'
                  'a. Abandon the boat for the rock?\n'
                  'b. Stay in the boat and hold on tight?')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = ['game_over', 'SPRITE']
    exit_txt = []
    exit_txt.append('You jump onto the rock but it is too slippery\n'
                    'You fall into the water and are dragged under.')
    exit_txt.append('You duck down and grab tight to the edge of the boat.\n'
                    'It rushes down the steep rapid but miraculously stays '
                    'upright and intact.\nIt beaches at the edge of a deep '
                    'pool.\nYou get out, there is a door ahead.')

    A3 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return A3
