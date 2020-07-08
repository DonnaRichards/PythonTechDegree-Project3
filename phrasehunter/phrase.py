from ./character import Character

# Create your Phrase class logic here.
class Phrase():
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

    # handle the creation of phrases.
    def __init__(self, phrase):
        self.phrase = [Character(char) for char in phrase]
        self.guessed = False

    def __str__(self):
        for char in phrase:
            print(char.show_char(), end='')

    def display_phrase(self):
        for char in self.phrase:
            print(char, end=' ')
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



