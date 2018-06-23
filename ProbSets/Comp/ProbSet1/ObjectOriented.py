#ObjectOriented

#Exercise 1

''' I'll construct the backpack class: '''
class Backpack:
    """A Backpack object class. Has a name, a color, a maximum size,
    and a list of contents.
    Attributes:
    name (str): the name of the backpack's owner.
    contents (list): the contents of the backpack.
    color (str): Color of the Backpack
    max_size (int): The max capacity of the backpack
    """
    def __init__(self, name, color, max_size=5): # The constructor.
        """Set the name and initialize an empty list of contents.
        Parameters:
        name (str): the name of the backpack's owner.
        color (str): Color of the Backpack
        max_size (int): The max capacity of the backpack
        """
        self.name = name # Initialize some attributes.
        self.contents = []
        self.color = color
        self.max_size = max_size

    def put(self, item):
        """Add 'item' to the backpack's list of contents."""
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)

    def dump(self):
        """Empties the contents of the backpack"""
        self.contents = []

    def __eq__(self, other):
        return (self.contents == other.contents and self.name == \
                other.name and len(self.color) == len(other.color))

    def __str__(self):
        return(f"""
               Owner = \t {self.name} \n
               Color = \t {self.color} \n
               Size = \t {len(self.contents)} \n
               Max Size = \t {self.max_size} \n
               Contents = \t {self.contents} """)


''' Testing the backpack: '''
def test_backpack():
    '''
    Note that "No Room" is not an error!
    '''
    testpack = Backpack("Matt", "red")
    if testpack.name != "Matt":
        print("Backpack.name assigned incorrectly")
    if testpack.color != "red":
        print("Color assigned incorrectly")
    if testpack.max_size != 5:
        print("max_size assigned incorrectly")
    for item in ["pencil", "pen", "paper"]:
        testpack.put(item)
    if testpack.contents != ["pencil", "pen", "paper"]:
        print("Issue with either put or contents")
    testpack.take("pencil")
    if testpack.contents != ["pen", "paper"]:
        print("issue with take")
    testpack.dump()
    if testpack.contents != []:
        print("Issue with dump")
    smallpack = Backpack("Matt", "red", max_size=1)
    for item in ["pencil", "pen", "paper"]:
        smallpack.put(item)
    if smallpack.contents == ["pencil", "pen", "paper"]:
        print("I'm allowed to put too many things in the pack")

test_backpack()

'''
------------------------------------------------------------------------
'''

# Exercise 2

import time

''' I construct a new subclass of backpacks. '''
class Jetpack(Backpack):
    '''
    A Jetpack object class. Inherits from the Backpack object class
    A jetpack is smaller than a backpack and can fly using fuel.

    Attributes:
    name (str): the name of the knapsack's owner.
    color (str): the color of the knapsack.
    max_size (int): the maximum number of items that can fit inside.
    contents (list): the contents of the backpack.
    fuel (int): The amount of fuel in the jetpack.

    '''

    def __init__(self, name, color, max_size=2, fuel=10):
        '''
        Use the backpack constructor to initialize the name, color, and
        max_size attributes. A jetpack only holds 2 items by default
        (There is less room for other items with a large fuel tank!)

        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        fuel (int): The amount of fuel in the jetpack.
        '''
        Backpack.__init__(self, name, color, max_size)
        Backpack.fuel = fuel

    def fly(self, burn): #Define a new method just for jetpacks.
        '''
        The jetpack flies for as many seconds as fuel is burned. The
        fuel which is burned is subtracted from the fuel supply. If you
        put in an invalid amount of fuel to burn the function spits out
        an error.
        '''
        if burn > self.fuel:
            print("Not enough fuel!")
        else:
            print("You're flying! For ")
            for  i in range(0, burn):
                print(i+1, " seconds")
                time.sleep(1)
            print("You've burned ",  burn ," of your fuel. \
                    Time to land.")
            print(self.fuel, " is your current fuel supply")
            self.fuel = self.fuel - burn

    def dump(self): #Override the .dump (method)
        self.contents = []
        self.fuel = 0


'''
------------------------------------------------------------------------
'''

# Exercise 3

#I modified the code in exercise 1 acccordingly.

'''
------------------------------------------------------------------------
'''

#Exercise 4

class ComplexNumber:
    """A complex number object class. Has a real part and an imaginary
    part.
    Attributes:
    real (float): the real part of the complex number
    imag (float): the imaginary part of the complex number.
    """

    def __init__(self, real, imag):
        """
        Parameters:
        real (float): the real part of the complex number
        imag (float): the imaginary part of the complex number.
        """
        self.real = real
        self.imag = imag

    def conjugate(self):
        """ Returns the complex conjugate. """
        return ComplexNumber(self.real, -self.imag)

    def __str__(self):
        ''' Returns a string representation of the complex number'''
        return(f"{self.real} + {self.imag}j")

    def __abs__(self):
        ''' Returns the absolute value of the complex number'''
        return((self.real**2 + self.imag**2)**.5)

    def __eq__(self, other):
        ''' Defines an equivalence relation '''
        return(self.real == other.real and self.imag == other.imag)

    def __add__(self, other):
        ''' Defines addition '''
        return(ComplexNumber(self.real + other.real, self.imag + other.
        imag))

    def __sub__(self, other):
        ''' Defines Subtraction '''
        return(ComplexNumber(self.real - other.real, self.imag - other.
        imag))

    def __mul__(self, other):
        ''' Defines Multiplication '''
        return(ComplexNumber(self.real * other.real - self.imag *
        other.imag, self.real * other.imag + other.real * self.imag))

    def __truediv__(self, other):
        ''' Defines Division '''
        if other == ComplexNumber(0, 0):
            print("ERROR: Cannot divide by zero")
        else:
            return(ComplexNumber((self.real * other.real + self.imag *
            other.imag) / (abs(other) ** 2), (self.imag * other.real -
            self.real * other.imag) / (abs(other) ** 2)))

def test_ComplexNumber(a, b):
    '''
    Defines a test for my ComplexNumber class by comparing it to
    Python's. I take an input and turn it into python's (py_cnum) and my
    (my_cnum) versions of a complex number to compare them against each
    other.
    '''
    py_cnum, my_cnum = complex(a, b), ComplexNumber(a, b)

    if my_cnum.real != a or my_cnum.imag != b:
        print("__init__ is broken")

    if py_cnum.conjugate().imag != my_cnum.conjugate().imag:
        print("conjugate() failed for,",  py_cnum)

    if str(py_cnum) != str(my_cnum):
        print("__str__() failed for", py_cnum)

    if abs(py_cnum) != abs(my_cnum):
        print("__abs__() failed for", py_cnum)

    ''' Define 2 more complex numbers for the binary operators '''
    py_55 = complex(5, 5)
    my_55 = ComplexNumber(5, 5)

    if (py_cnum + py_55).real != (my_cnum + my_55).real and \
    (py_cnum + py_55).imag != (my_cnum + my_55).imag:
        print("__add__() failed for", py_cnum)

    if (py_cnum - py_55).real != (my_cnum - my_55).real and \
    (py_cnum - py_55).imag != (my_cnum - my_55).imag:
        print("__sub__() failed for", py_cnum)

    if (py_cnum * py_55).real != (my_cnum * my_55).real and \
    (py_cnum * py_55).imag != (my_cnum * my_55).imag:
        print("__mul__() failed for", py_cnum)
        print(py_cnum * py_55, my_cnum * my_55)

    if (py_cnum / py_55).real != (my_cnum / my_55).real and \
    (py_cnum / py_55).imag != (my_cnum / my_55).imag:
        print("__truediv__() failed for", py_cnum)
        print(py_cnum / py_55, my_cnum / my_55)

test_ComplexNumber(2, 4)
''' The __str__ function fails - but that's a question of formatting rather
than of content. '''
