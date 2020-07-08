import re

# Create your Character class logic in here.
class Character():


    # help a Phrase determine how an individual character should display itself.

    def __init__(self, char):
        self.char = char
        if re.search(char, [a-z]):
            self.guessed = False
        else
            self.guessed = True

    def set_guess(self, char):
        if char.lower() == self.char.lower():
            self.guessed = True

    def __str__(self):
        if self.guessed:
            return self.char
        else
            return '_'

    def show_char(self):
        return self.char