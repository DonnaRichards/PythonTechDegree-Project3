# Create your Game class logic in here.
from phrasehunter.phrase import Phrase
import re
import random

class Game():

    def __init__(self, phrases):
        self.phrase = Phrase(phrases[random.randint(0, len(phrases)-1)])
        self.won = False
        self.lives = 5
        self.letters_guessed = []

    def update_letters_guessed(self, guess):
        self.letters_guessed.append(guess)

    def get_guess(self):
        valid_guess = False
        while not valid_guess:
            try:
                guessed_char = input('Enter a letter (a-z): ')
                if len(guessed_char) > 1:
                    raise ValueError('Too many characters entered - please enter only one letter')
                if len(guessed_char) < 1:
                    raise ValueError('Nothing entered - please enter a letter')
                if re.search(r'[^a-z]', guessed_char.lower()):
                    raise ValueError('Invalid character entered - please enter a letter (a-z) ')
                if guessed_char.lower() in self.letters_guessed:
                    raise ValueError("You've already guessed this letter, try again ")
            except ValueError as err:
                print(err)
                continue
            valid_guess = True
        return guessed_char.lower()

    def update_lives(self):
        self.lives -= 1

    def play_game(self):
        print('Welcome to Phrase Hunter !')
        print('guess a letter in the phrase')
        print('5 guesses to get the phrase')
        while not self.won and self.lives > 0:
            print(f'You have {self.lives} guesses left')
            print('Current phrase is: ', end='')
            self.phrase.display_phrase()
            guessed_char = self.get_guess()
            print('play_game - guessed char = ' + guessed_char)
            self.update_letters_guessed(guessed_char)
            good_guess = self.phrase.check_guess(guessed_char)
            if good_guess:
                print('Good guess')
                self.won = self.phrase.check_if_won()
            else:
                print('Sorry this letter not in phrase')
                self.update_lives()
        if self.won:
            print("Magnificent job, you got it !! ")
        else:
            print("Sorry you didn't get it this time.")
        print("Complete phrase: " + self.phrase.phrasestr)




