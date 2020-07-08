# Create your Game class logic in here.
import random
from phrase import Phrase

class Game():

    def __init__(self, phrases):
        self.phrase = Phrase(phrases[randint(len(phrases))])
        self.won = False
        self.lives = 5
        self.letters_guessed = ''

    def update_letters_guessed(self, guess):
        self.letters_guessed.append(guess)

    def get_guess(self):
        valid_guess = False
        while not valid_guess:
            try:
                guessed_char = input('Enter a letter (a-z): ')
                if len(guessed_char) > 1:
                    raise ValueError('Too many characters entered - please enter only one letter')
                if re.search(guessed_char, [^a-z]):
                    raise ValueError('Invalid character entered - please enter a letter (a-z) ')
                if guessed_char in self.letters_guessed:
                    raise ValueError("You've already guessed this letter, try again ")
            except ValueError:
                continue
            valid_guess = True
        return guessed_char.lower()

    def update_lives(self, good_guess):
        if not good_guess:
            self.lives -= 1

    def play_game(self):
        print('Welcome to Phrase Hunter !')
        print('guess a letter in the phrase')
        print('5 guesses to get the phrase')
        print('Your phrase is: ',end='')
        self.phrase.display_phrase()
        while not self.won and self.lives > 0:
            guessed_char = get_guess()
            update_letters_guessed(guessed_char)
            good_guess = self.phrase.check_guess(guessed_char)
            if good_guess:
                self.won = self.phrase.check_if_won()
            else:
                update_lives()
        if self.won:
            print("Magnificent job, you got it !! ")
        else:
            print("Sorry you didn't get it this time.")
            print("Complete phrase was: " + self.phrase)




