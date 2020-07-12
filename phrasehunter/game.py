# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import re
import random


class Game:
    '''
    Play one Game of Phrase Hunter
    '''
    def __init__(self, phrases):
        '''
        :param phrases: list of phrases which can be used for the game
        :type phrases: list of tuples (each tuple contains phrase and author)
        Attributes:
            phrase = one quote (selected randomly from the list of quotes passed in)
            won = flag to indicate whether game won or not, True or False
            lives = count of number of lives a player has left.  Starts at 5, reduces by 1 for
                each incorrect guess
            letters_guessed = a list which keeps track of which letters the player has guessed
        '''
        self.phrase = Phrase(phrases[random.randint(0, len(phrases) - 1)])
        self.won = False
        self.lives = 5
        self.letters_guessed = []

    def get_guess(self):
        """
        Control the process of getting a guess from the player
        Keep asking for guess until it is valid (i.e. a single letter a-z, case insensitive)
        :return: the guessed letter
        :rtype: str
        :raises: ValueError - if user input invalid (i.e. not a single letter)
        """
        guessed_char = ''
        valid_guess = False
        while not valid_guess:
            try:
                guessed_char = input('Enter a letter (a-z): ')
                if len(guessed_char) > 1:
                    raise ValueError('Too many characters entered - please enter only one letter')
                if len(guessed_char) < 1:
                    raise ValueError('Nothing entered - please enter a letter')
                if re.search(r'[^A-Za-z]', guessed_char):
                    raise ValueError('Invalid character entered - please enter a letter (a-z) ')
                if guessed_char.lower() in self.letters_guessed:
                    raise ValueError("You've already guessed this letter, try again ")
            except ValueError as err:
                print(err)
                continue
            valid_guess = True
        return guessed_char

    def play_game(self):
        """
        Control the game play
        Loop asking player to guess a letter and displaying the updated phrase
        (guessed letters becoming visible) until either the phrase has been guessed
        or player is out of lives
        """
        print('Welcome to Phrase Hunter !')
        print('guess a letter in the phrase')
        print('5 guesses to get the phrase')
        while not self.won and self.lives > 0:
            print(f'You have {self.lives} guesses left')
            print('Current phrase is: ', end='')
            self.phrase.display_phrase()
            guessed_char = self.get_guess()
            self.letters_guessed.append(guessed_char)
            good_guess = self.phrase.check_guess(guessed_char)
            if good_guess:
                print('Good guess')
                self.won = self.phrase.check_if_won()
            else:
                print('Sorry this letter not in phrase')
                self.lives -= 1
        if self.won:
            print("********************************")
            print(" Magnificent job, you got it !! ")
            print("********************************")
        else:
            print("Sorry you didn't get it this time.")
        print("Complete quote:\n\n " + self.phrase.show_full_quoted_phrase() + "\n")
