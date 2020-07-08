from phrasehunter.character import Character

# Create your Phrase class logic here.
class Phrase():

    # handle the creation of phrases.
    def __init__(self, phrase):
        self.phrase = [Character(char) for char in phrase]
        self.phrasestr = phrase
        self.guessed = False

    def display_phrase(self):
        for char in self.phrase:
            print_char = char.display_char()
            print(print_char, end=' ')
        print('\n')

    def check_guess(self, guess):
        good_guess = False
        for char in self.phrase:
            if not char.guessed:
                char.set_guess(guess)
                if char.guessed:
                    good_guess = True
        return good_guess

    def check_if_won(self):
        for char in self.phrase:
            if not char.guessed:
                return False
        return True



