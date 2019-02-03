import random
"""
Die Class
"""
class Die():
    """
    Constructor
    """
    def __init__(self, position):
        print("Called Die constructor")
        self.position = position

    
die1 = Die(1)

print(die1.position)
