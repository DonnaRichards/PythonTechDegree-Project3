import re

# Create your Character class logic in here.
class Character():
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

    # help a Phrase determine how an individual character should display itself.

    def __init__(self, char):
        self.char = char
        if re.search(char, [a-z]):
            self.guessed = False
        else
            self.guessed = True

    def guess(self, char):
        if char.lower() == self.char.lower():
            self.guessed = True

    def __str__(self):
        if self.guessed:
            return self.char
        else
            return '_'

