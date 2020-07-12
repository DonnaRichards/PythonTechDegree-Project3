import csv
import sys
from phrasehunter.game import Game

"""
PhraseHunter game

The code chooses a random phrase and displays each letter of the phrase as underscore character placeholders, _.

Each time the player guesses a letter, the program compares the letter the player has chosen with the random phrase. 
If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.

A player continues to select letters until they guess the phrase (and win), or make five incorrect guesses (and lose).

If the player completes the phrase before they run out of guesses, a winning screen appears. 
If the player guesses incorrectly five times, a losing screen appears.

Game is using quotes about cats, from https://www.shutterfly.com/ideas/cat-quotes/
"""


def load_phrases():
    """
    Load quotes to be used for the game from file phrasehunter.csv
    each quote is stored in tuple containing quote + author
    :return: phraselist
    :rtype: list of tuples
    """
    phraselist = []
    try:
        with open('./phrasehunter/phraselist.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='|')
            for row in reader:
                phraselist.append((row['Phrase'], row['Author']))
    except FileNotFoundError:
        print('phraselist.csv file not found, terminating program')
        sys.exit(1)
    return phraselist


if __name__ == "__main__":
    phraselist = load_phrases()
    play_again = 'y'
    while play_again.lower() == 'y':
        game = Game(phraselist)
        game.play_game()
        play_again = input('Do you want to play again ? (y/n) ')
        del game
    print('Thank you for playing the game !  Enjoy the rest of your day')
