# Import your Game class
from ./phrasehunter/game.py import Game

# Create your Dunder Main statement.
if __name__ == "__main__":
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
    game = Game()
    game.start()