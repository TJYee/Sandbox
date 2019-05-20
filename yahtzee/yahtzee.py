import random


class Die(object):
    """
    A class used to represent a Die

    ...

    Attributes
    ----------
        __value : int
            The current value of the Die (default is None)
        side_min_value : int
            The lowest side value (default is 1)
        side_count : int
            The number of sides on the Die (default is 6)
        side_increment : int
            The incremental side value between sides (default is 1)

    Methods
    -------
    roll()
        Rolls the Die to get a new random value of the Die
    check_value()
        Returns current value of Die
    """

    __value = None

    def __init__(self, side_min_value=1, side_count=6, side_increment=1):
        """
        Parameters
        ----------
        side_min_value : int, optional
            The lowest side value (default is 1)
        side_count : int, optional
            The number of sides on the Die (default is 6)
        side_increment : int, optional
            The incremental side value between sides (default is 1)
        """
        print("Called Die constructor")
        self.side_min_value = side_min_value
        self.side_count = side_count
        self.side_increment = side_increment

    def roll(self):
        """Rolls the Die to get a new random value of the Die"""
        self.__value = random.randint(
            self.side_min_value, self.side_count) * self.side_increment

    def check_value(self):
        """Returns current value of Die"""
        return self.__value


# Test Code
# die1 = Die(side_min_value=0, side_count=10, side_increment=10)
# print("Minimum side is: " + str(die1.side_min_value))
# print("Side count is: " + str(die1.side_count))
# print("Value is: " + str(die1.check_value()))
# die1.roll()
# print("Value is: " + str(die1.check_value()))
# die1.roll()
# print("Value is: " + str(die1.check_value()))

game_play = True
print("Beginning of Game Loop")
while(game_play):
    print("Start of Game")
    print("End of Game")
    user_input = input("Would you like to continue to play? ")
    while(not(user_input in ["yes", "no"])):
        print("I do not understand that response.")
        user_input = input("Would you like to continue to play? ")
    if(user_input == "no"):
        game_play = False

print("End of Game Loop.")
