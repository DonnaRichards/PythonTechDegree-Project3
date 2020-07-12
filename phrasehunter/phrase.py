from phrasehunter.character import Character


class Phrase:
    """
    Controls creation and formatting of one phrase for the game
    """
    # Class global constant - an approx maximum number of phrase characters
    #                           to print on one line
    PRINT_LEN = 60

    def __init__(self, phrase):
        '''
        :param phrase:
        :type phrase:
                Attributes:
            phrasestr (str): the phrase, in string format
            phrase (list of Character): the phrase as a list of Characters
            author (str): the author of the quote
        '''
        self.phrasestr = self.format_phrase(phrase[0])
        self.phrase = [Character(char) for char in self.phrasestr]
        self.author = phrase[1]


    def format_phrase(self, phrase):
        '''
        Some of the phrases (quotes) are longer that what will display normally on one line.
        this function is an initial formatting of phrases which are longer than a
        defined value (class global constant) to insert some newline (\n) characters
        so they will display on multiple lines - hence more readable.
        Takes a pretty simplistic approach - loops through the characters in the phrase
        keeping count.  For each space character after the count hits the defined limit,
        replace with a newline \n
        :param: phrase = string version of phrase
        :return:  modified string with newlines inserted
        :rtype: str
        '''
        count = 0
        phrasel = list(phrase)
        for index, char in enumerate(phrasel):
            if char == ' ' and count > self.PRINT_LEN:
                phrasel[index] = '\n'
                count = 0
            count += 1
        return ''.join(phrasel)

    def display_phrase(self):
        '''
        Display phrase during game.  Guessed characters are revealed but characters not
        guessed yet display as an underscore _
        :return: None
        :rtype: None
        '''
        print('\n')
        for char in self.phrase:
            print_char = char.display_char()
            print(print_char, end=' ')
        print('\n')

    def show_full_quoted_phrase(self):
        """
        Displays full (no characters hidden) quote, with author at end of game.
        :return: A string consisting of string representation of quote + the author.
                    Newline between end of quote and author.
        :rtype: str
        """
        return '"' + self.phrasestr + '"\n - ' + self.author

    def check_guess(self, guess):
        """
        Check player's guess.   Compare guessed character to the characters in the
        phrase, pass to Character class to update phrase character guessed value.
        :param guess: guessed character
        :type guess: str
        :return: good_guess: True or False - Was character in phrase or not
        :rtype: bool
        """
        good_guess = False
        for char in self.phrase:
            if not char.guessed:
                char.set_guessed(guess)
                if char.guessed:
                    good_guess = True
        return good_guess

    def check_if_won(self):
        """
        Check if player has won the game !
        If all characters in the phrase are guessed, then it is a yes.
        :return: True or False, won game or not
        :rtype: bool
        """
        for char in self.phrase:
            if not char.guessed:
                return False
        return True
