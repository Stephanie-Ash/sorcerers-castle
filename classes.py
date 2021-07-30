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
    int_txt = ('The Evil Sourcerer has poisoned the Tree of Life '
               'and the forest is dying.\n'
               'He has locked the antidote in his castle."')
    choice_txt = '"Will you embark on a quest to retrieve it for us?"'
    options = ['yes', 'no']
    opt_txt = 'Do you help?'
    exits = [{'type': 'item', 'route': create_item1()},
             {'type': 'story', 'route': create_intro_no()}]
    exit_txt = []
    exit_txt.append('\n"Thank you, I know you will save our forest."')
    exit_txt.append('\n"No?! What a big coward you are!"')

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
    exits = [{'type': 'item', 'route': create_item1()},
             {'type': 'game over', 'route': 'game_over'}]
    exit_txt = []
    exit_txt.append('\n"Thank you, I know you will save our forest."')
    exit_txt.append('\nThe elven woman runs off in a huff.')

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
    exits = [{'type': 'puzzle', 'route': 'puzzle2'},
             {'type': 'puzzle', 'route': 'puzzle3'}]
    exit_txt = []
    exit_txt.append('\nYou open the door to the left.')
    exit_txt.append('\nYou open the door to the right.')

    hall = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return hall


def create_dungeon():
    """
    Create the dungeon Branches object
    """
    int_txt = ('You land with a bump in a cold dark dungeon.\n'
               'You see that there is a door set high in the wall '
               'accross from you.\n'
               'You search around for something to help you climb.')
    choice_txt = 'You find a metal hook on a rope and an old wooden ladder.'
    options = ['rope', 'ladder']
    opt_txt = 'Which item do you use?'
    exits = [{'type': 'story', 'route': create_c1()},
             {'type': 'game over', 'route': 'game_over'}]
    exit_txt = []
    exit_txt.append('\nYou grab the rope, swing it around your head '
                    'and throw it towards the door.\n'
                    'The hook connects and gets lodged.\n'
                    'You climb the rope and go through the door.')
    exit_txt.append('\nYou prop the ladder against the wall '
                    'and start climbing.\nYou are almost at the top '
                    'when the steps break and you fall.')

    dungeon = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return dungeon


# A route, followed if Puzzle2 is passed.
def create_a1():
    """
    Create the a1 Branches object.
    """
    int_txt = ('You find yourself in a...jungle!\n'
               'The trees are tightly packed together and wild looking,\n'
               'with many strong vines hanging from them.\n'
               'There is a quickly flowing river running through the trees.\n'
               'You spy a boat tied at the edge of the river.')
    choice_txt = ('Do you:\n'
                  'a. Swing through the trees using the vines\n'
                  'b. Try your luck with the boat')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = [{'type': 'story', 'route': create_a2()},
             {'type': 'story', 'route': create_a3()}]
    exit_txt = []
    exit_txt.append('\nYou climb onto the nearest sturdy looking vine '
                    'and start swinging.')
    exit_txt.append('\nYou climb into the boat and speed down the river.')

    a1 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return a1


def create_a2():
    """
    Create the a2 Branches object
    """
    int_txt = ('You are making great progress until you suddenly swing '
               'into a clearing.\nYou drop to the floor.\n'
               'You spy a jaguar loitering in the centre of the clearing.')
    choice_txt = ('Do you:\n'
                  'a. Create a distraction\n'
                  'b. Try to sneak past the jaguar')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = [{'type': 'story', 'route': create_sprite()},
             {'type': 'game over', 'route': 'game_over'}]
    exit_txt = []
    exit_txt.append('\nYou throw a branch into the distant trees.\n'
                    'The jaguar takes off after it and you run.\n'
                    'You finally stop next to a pool of water.\n'
                    'There is a door ahead.')
    exit_txt.append('\nYou continue quietly.\n'
                    'Just as you make it past the jaguar "snap" you stand '
                    'on a branch.\nThe jaguar grabs you.')

    a2 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return a2


def create_a3():
    """
    Create the a3 Branches object
    """
    int_txt = ('Your journey gets rougher as you travel through rapids.\n'
               'You see a steep drop, almost waterfall ahead.\n'
               'There is a rock coming up on your left.')
    choice_txt = ('Do you:\n'
                  'a. Abandon the boat for the rock\n'
                  'b. Stay in the boat and hold on tight')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = [{'type': 'game over', 'route': 'game_over'},
             {'type': 'story', 'route': create_sprite()}]
    exit_txt = []
    exit_txt.append('\nYou jump onto the rock but it is too slippery.\n'
                    'You fall into the water and are dragged under.')
    exit_txt.append('\nYou duck down and grab tight to the edge of the boat.\n'
                    'It rushes down the steep rapid but miraculously stays '
                    'upright and intact.\nIt beaches at the edge of a deep '
                    'pool.\nYou get out, there is a door ahead.')

    a3 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return a3


# B route, followed if Puzzle3 is passed.
def create_b1():
    """
    Create the b1 Branches object
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
    exits = [{'type': 'story', 'route': create_b2()},
             {'type': 'story', 'route': create_b3()},
             {'type': 'story', 'route': create_b4()}]
    exit_txt = []
    exit_txt.append('\nYou take off towards the village.')
    exit_txt.append('\nYou take off towards the oasis.')
    exit_txt.append('\nYou continue through the desert.')

    b1 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return b1


def create_b2():
    """
    Create the b2 Branches object
    """
    int_txt = ('You walk into the village and wander past the huts.\n'
               'You open the door to one and notice a group '
               'of sand monsters.\n'
               'You try to shut the door but it is too late, they have '
               'seen you.')
    choice_txt = ('Do you:\n'
                  'a. Run away\n'
                  'b. Stay and fight')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = [{'type': 'retrace', 'route': 'b1'},
             {'type': 'game over', 'route': 'game_over'}]
    exit_txt = []
    exit_txt.append('\nYou turn and run away as fast as you can.\n'
                    'At first you hear them chasing but soon lose them.\n'
                    'You stop to catch your breath and find yourself '
                    'on top of the same dune as before.\n\n'
                    'Do you:\n'
                    'a. Head towards the village\n'
                    'b. Head towards the oasis\n'
                    'c. Continue through the desert')
    exit_txt.append('\nYou grab a club by the door and run into the group.\n'
                    'You fight valiantly but they are too strong.\n'
                    'They knock you to the floor and attack.')

    b2 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return b2


def create_b3():
    """
    Create the b3 Branches object
    """
    int_txt = ('You stroll into the oasis, it is so much cooler here.\n'
               'There is a large pool in the middle.\n'
               'There is a rope bridge from one side to the other.\n'
               'There are also lily pads all the way across.')
    choice_txt = ('Do you:\n'
                  'a. Take the bridge\n'
                  'b. Jump across the lily pads')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = [{'type': 'story', 'route': create_sprite()},
             {'type': 'game over', 'route': 'game_over'}]
    exit_txt = []
    exit_txt.append('\nYou head across the bridge.\n'
                    'As you are crossing it creaks and begins to snap.\n'
                    'You run across and jump onto the other side.\n'
                    'There is a door ahead.')
    exit_txt.append('\nYou make your way steadily across the lily pads.\n'
                    'Suddenly one sinks under your weight.\n'
                    'You fall in and are dragged under.')

    b3 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return b3


def create_b4():
    """
    Create the b4 Branches object
    """
    int_txt = ('You keep walking, you are getting hotter and hotter.\n'
               'You will not make it much further.\n'
               'At the top of the next dune you stumble across a camel.\n'
               'By the camel there is a thin flat board.')
    choice_txt = ('Do you:\n'
                  'a. Sandboard over the dunes\n'
                  'b. Ride the camel')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = [{'type': 'game over', 'route': 'game_over'},
             {'type': 'story', 'route': create_sprite()}]
    exit_txt = []
    exit_txt.append('\nYou grab the board and slide down the dune.\n'
                    'When you get to the bottom the board is useless.\n'
                    'You start up the next dune carrying the board.\n'
                    'You collapse with heat exhaustion.')
    exit_txt.append('\nYou grab the neck of the camel and it takes off '
                    'before you can climb on.\n'
                    'You hold on tight while it keeps running.\n'
                    'Eventually It comes to a halt at the edge of the oasis.\n'
                    'You see a door ahead.')

    b4 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return b4


# C route, followed if player escapes the dungeon.
def create_c1():
    """
    Create the c1 Branches object
    """
    int_txt = ('You walk into a dark, stinky sewer, yuk!\n'
               'You continue forward until you see three tunnels ahead.')
    choice_txt = ('There is light coming from the first,\n'
                  'the sound of rushing water from the second and\n'
                  'the squeaking sound of rats from the third.')
    options = ['1', '2', '3']
    opt_txt = 'Which tunnel do you choose?'
    exits = [{'type': 'game over', 'route': 'game_over'},
             {'type': 'story', 'route': create_c2()},
             {'type': 'story', 'route': create_c3()}]
    exit_txt = []
    exit_txt.append('\nYou wander down the first tunnel towards the light.\n'
                    'But it is not light it is fire!\n'
                    'It speeds towards you and engulfs you.')
    exit_txt.append('\nYou take the middle tunnel towards the sound of water.')
    exit_txt.append('\nYou take the third tunnel.')

    c1 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return c1


def create_c2():
    """
    Create the c2 Branches object
    """
    int_txt = ('More water and sewage comes into the tunnel from the sides.\n'
               'It has reached your waist and is still rising.')
    choice_txt = ('Do you:\n'
                  'a. Continue forward\n'
                  'b. Turn back the way you came')
    options = ['a', 'b']
    opt_txt = 'Make your choice'
    exits = [{'type': 'game over', 'route': 'game_over'},
             {'type': 'retrace', 'route': 'c1'}]
    exit_txt = []
    exit_txt.append('\nYou let the water take you and float down the tunnel.\n'
                    'At the end there is a grate blocking your path.\n'
                    'There is no way through, the water keeps rising.\n')
    exit_txt.append('\nThe turn back the way you came, fighting the water.\n'
                    'You arrive back at the entrance of the tunnel.\n'
                    'You turn and look again at the three tunnels')

    c2 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return c2


def create_c3():
    """
    Create the c3 Branches object
    """
    int_txt = ('The sound of rats gets louder the further you go.\n'
               'You feel them running past your feet.\n'
               'You arrive at another tunnel branch.')
    choice_txt = ('There is a breeze coming from the tunnel on the left.\n'
                  'A river of rats runs down the one on the right.')
    options = ['left', 'right']
    opt_txt = 'Which tunnel do you choose'
    exits = [{'type': 'game over', 'route': 'game over'},
             {'type': 'story', 'route': create_sprite()}]
    exit_txt = []
    exit_txt.append('\nYou take the left and walk towards the breeze.\n'
                    'Suddenly the floor drops away from you and you fall.')
    exit_txt.append('\nYou take the right and get carried along by the rats.\n'
                    'You arrive in a wider cavern. There is a door ahead.')

    c3 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return c3


def create_sprite():
    """
    Create the sprite Branches object.
    Reached if the player makes it through the A, B or C routes
    """
    int_txt = ('Before you can reach the door a sprite appears.\n'
               '"Oh you must be the person sent to save the forest.\n'
               'I should not be here but I wanted to see the castle"')
    choice_txt = ('"Unfortunately I have dropped my magic beads.\n'
                  'I cannot escape without them.\n'
                  'Will you help me collect them?"')
    options = ['yes', 'no']
    opt_txt = 'Do you help?'
    exits = [{'type': 'item', 'route': create_item2()},
             {'type': 'puzzle', 'route': 'puzzle4'}]
    exit_txt = []
    exit_txt.append('\nYou collect up all the beads and hand them over.')
    exit_txt.append('\n"Fine suit yourself!"\n'
                    'You walk through the door.')

    sprite = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return sprite


# Item pick up Branches
def create_item1():
    """
    Create the item1 Branches object
    """
    int_txt = ('"Be careful on your quest, the castle is full of traps.\n'
               'I hear that the sourcerer can even manipulate fire."')
    choice_txt = ('"Here take an item to help you on your quest."')
    options = ['candle', 'waterskin', 'food']
    opt_txt = 'Which item do you take?'
    exits = [{'type': 'puzzle', 'route': 'puzzle1'}]
    exit_txt = []
    exit_txt.append('You make your way towards the castle.')

    item1 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return item1


def create_item2():
    """
    Create the item2 Branches object
    """
    int_txt = ('"Thank you, I can now escape the castle.\n'
               'Your journey from here is treacherous.\n'
               'There will be many walls to knock down."')
    choice_txt = ('"Here take an item to help you."')
    options = ['sledgehammer', 'rope', 'feather']
    opt_txt = 'Which item do you take?'
    exits = [{'type': 'puzzle', 'route': 'puzzle4'}]
    exit_txt = []
    exit_txt.append('You walk through the door.')

    item2 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return item2


def create_item3():
    """
    Create the item3 Branches object
    """
    int_txt = ('\n\nThe force field disappears and you step through.\n'
               'You see some items on the floor.')
    choice_txt = ('You decide to take one with you.')
    options = ['knife', 'axe', 'fan']
    opt_txt = 'Which item do you take?'
    exits = [{'type': 'story', 'route': 'end_room'}]
    exit_txt = []
    exit_txt.append('You ascend the stairs.')

    item3 = Branches(int_txt, choice_txt, options, opt_txt, exits, exit_txt)
    return item3
