# Create your Game class logic in here.
import random
import re

class Game():
    '''
 |  Class representing a company employee.
 |  
 |  Attributes
 |   ----------
 |   name : str 
 |       Employee's name        
 |   email : str, default None
 |       Employee's email
 |   salary : float, default None
 |       Employee's salary
 |   rank : int, default 5
 |       The rank of the employee in the company hierarchy (1 -- CEO, 2 -- direct reports of CEO, 3 -- direct reports of direct reports of CEO etc). Cannot be None if the employee is current.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, email=None, salary=None, rank=5)
 |      Create an Employee object
 |  
 |  give_raise(self, amount)
 |      Raise employee's salary by a certain `amount`. Can only be used with current employees.
 |      
 |      Example usage:
 |        # emp is an Employee object
 |        emp.give_raise(1000)
 |  
 |  promote(self)
 |      Promote an employee to the next level of the company hierarchy. Decreases the rank of the employee by 1. Can only be used on current employeed who are not at the top of the hierarchy.
 |      
 |      Example usage:
 |          # emp is an Employee object
 |          emp.promote()
 |  
 |  terminate(self)
 |      Terminate the employee. Sets salary and rank to None..
 |      
 |      Example usage:
 |         # emp is an Employee object
 |         emp.terminate()
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
    '''

    # methods for starting the game, handling interactions, getting a random phrase, 
    # checking for a win/loss state, and removing "lives" or turns from the player.
    def __init__(self, phrases):
        self.phrase = Phrase(phrases[randint(len(phrases))])
        self.won = False
        self.num_guesses = 0

    def get_guess(self):
        valid_guess = False
        while not valid_guess:
            try:
                user_guess = input('Enter a letter (a-z): ')
                if len(user_guess) > 1:
                    raise ValueError('Too many characters entered - please enter only one letter')
                if re.search(user_guess, [^a-z]):
                    raise ValueError('Invalid character entered - please enter a letter (a-z) ')
            except ValueError:
                continue
            valid_guess = True
        return user_guess


    def start(self):
        print('Welcome to Phrase Hunter !')
        print('guess a letter in the phrase')
        print('5 guesses to get the phrase')
        print('Your phrase is: ',end='')
        self.phrase.display_phrase()
        while not self.won and self.num_guesses < 6:
            guess = get_guess()
            good_guess = phrase.check_guess(guess)




