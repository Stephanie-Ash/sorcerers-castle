# Classes containing text and player options
# for most of the story.

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


# A route, followed if Puzzle2 is passed.
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
                  'a. Create a distraction\n'
                  'b. Try to sneak past the jaguar')
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
                  'a. Abandon the boat for the rock\n'
                  'b. Stay in the boat and hold on tight')
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


# B route, followed if Puzzle3 is passed.
def create_B1():
    """
    Create the B1 Branches object
    """
    int_txt = ('You emerge into...a desert!\n'
               'Sandy dunes stretch for miles in every direction.\n'
               'You start walking. It is really hot and you quickly tire.\n'
               'As you ascend a dune you see a village of huts ahead.\n'
               'In the other direction is a green oasis.')
    choice_txt = ('Do you:\n'
                  'a. Head towards the village\n'
                  'b. Head towards the oasis\n'
                  'c. Continue through the desert')
    options = ['a', 'b', 'c']
    opt_txt = 'Make your choice'
    exits = ['B2', 'B3', 'B4']
    exit_txt = []
    exit_txt.append('You take off towards the village.')
    exit_txt.append('You take off towards the oasis.')
    exit_txt.append('You continue through the desert.')

    B1 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return B1


def create_B2():
    """
    Create the B2 Branches object
    """
    int_txt = ('You walk into the village and wander past the huts.\n'
               'You decide to check inside one.\n'
               'As you open the door you notice a group of sand monsters.\n'
               'You try to shut the door but it is too late, they have '
               'seen you.')
    choice_txt = ('Do you:\n'
                  'a. Run away\n'
                  'b. Stay and fight\n')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = ['B1_return', 'game_over']
    exit_txt = []
    exit_txt.append('You turn and run away as fast as you can.\n'
                    'At first you hear them chasing but soon lose them.\n'
                    'You stop to catch your breath and find yourself '
                    'on top of the same dune as before.')
    exit_txt.append('You grab a club by the door and run into the group.\n'
                    'You fight valiantly but they are too strong.\n'
                    'They knock you to the floor and attack.')

    B2 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return B2


def create_B3():
    """
    Create the B3 Branches object
    """
    int_txt = ('You stroll into the oasis, it is so much cooler here.\n'
               'There is a large pool in the middle.\n'
               'It looks like you must cross it to get to the other side.\n'
               'There is a rope bridge from one side to the other.\n'
               'There are also lily pads all the way across.')
    choice_txt = ('Do you:\n'
                  'a. Take the bridge\n'
                  'b. Jump across the lily pads\n')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = ['SPRITE', 'game_over']
    exit_txt = []
    exit_txt.append('You head across the bridge.\n'
                    'As you are crossing it creaks and begins to snap.\n'
                    'You run across and jump onto the other side.\n'
                    'There is a door ahead.')
    exit_txt.append('You make your way steadily across the lily pads.\n'
                    'Suddenly one sinks under your weight.\n'
                    'You fall in and are dragged under.')

    B3 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return B3


def create_B4():
    """
    Create the B4 Branches object
    """
    int_txt = ('You keep walking, you are getting hotter and hotter.\n'
               'You will not make it much further.\n'
               'At the top of the next dune you stumble across a camel.\n'
               'It does not look friendly, it hisses and spits at you.\n'
               'By the camel there is a thin flat board.')
    choice_txt = ('Do you:\n'
                  'a. Sandboard over the dunes\n'
                  'b. Ride the camel\n')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = ['game_over', 'SPRITE']
    exit_txt = []
    exit_txt.append('You grab the board and have fun sliding down the dune.\n'
                    'When you get to the bottom the board is useless.\n'
                    'You start up the next dune carrying the board.\n'
                    'You collapse with heat exhaustion.')
    exit_txt.append('You grab the neck of the camel and it takes off '
                    'before you can climb on.\n'
                    'You cling on and swing yourself over its back.\n'
                    'You hold on while it keeps running.\n'
                    'Eventually It comes to a halt at the edge of the oasis.\n'
                    'You see a door ahead.')

    B4 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return B4
