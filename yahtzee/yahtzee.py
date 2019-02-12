import random


class Die():
    '''
    The Die object contains information and actions of a singal Die


    Args:
        side_start (int): The side_start is used for stating the lowest side value of the Die
        max_side (int): The max_side is used for stating how many sides are on the Die
        position (int): The position is used for keeping track of the Die


    Attributes:
        side_start (int): This is where we store side_start
        max_side (int): This is where we store max_side
        position (int): This is where we store position
    '''

    def __init__(self, side_start, max_side, position):
        print("Called Die constructor")
        self.side_start = side_start
        self.max_side = max_side
        self.position = position


die1 = Die(1, 6, 1)

print(die1.side_start)
print(die1.max_side)
print(die1.position)
