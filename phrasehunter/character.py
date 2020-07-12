import re


class Character:
    """
    Representation of a single character in the phrase
    """

    def __init__(self, char):
        '''
        :param char: One character in the phrase
        :type char: str
        Attributes:
            original_char (str): The character (non hidden), from param char
            guessed (bool): True or False - has the character been guessed or not
        '''
        self.original_char = char
        if re.search(r'[A-Za-z]', char):
            self.guessed = False
        else:
            self.guessed = True

    def set_guessed(self, char):
        """
        For a single character in phrase, update the guessed attribute
        Check if character player has guessed matches this character
        if so guessed is updated to True
        :param char: character player has guessed
        :type char: str
        """
        if char.lower() == self.original_char.lower():
            self.guessed = True

    def display_char(self):
        """
        Character display - if player has guessed this character show normally.
        If not, display as underscore '_'
        :return: character itself or _
        :rtype: str
        """
        if self.guessed:
            return self.original_char
        else:
            return '_'
