#UnitTesting

#Exercise 1/2

'''
The issue with the original function was that for numbers like 4 and 6, the
range for i was (2,2), which gives nothing to test, so the function was just
spitting out "n." Indeed, the function will fail for any perfect square! So to
fix this, I changed the upper bound from n**.5 to n**.5+1.
'''

def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1:
        return 1
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return i
    return n

'''
-------------------------------------------------------------------------------
'''

# Exercise 2
def month_length(month, leap_year=False):
    """Return the number of days in the given month."""
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July", "August", "October", "December"}:
        return 31
    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None

'''
-------------------------------------------------------------------------------
'''

# Exercise 3
def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")

'''
-------------------------------------------------------------------------------
'''
# Exercise 4

class Fraction(object):
    """Reduced fraction class with integer numerator and denominator."""
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        elif type(numerator) is not int or type(denominator) is not int:
            raise TypeError("numerator and denominator must be integers")
        def gcd(a,b):
            while b != 0:
                a, b = b, a % b
            return a
        common_factor = gcd(numerator, denominator)
        self.numer = numerator // common_factor
        self.denom = denominator // common_factor
    def __str__(self):
        if self.denom != 1:
            return "{} / {}".format(self.numer, self.denom)
        else:
            return str(self.numer)
    def __float__(self):
        return self.numer / self.denom
    def __eq__(self, other):
        if type(other) is Fraction:
            return self.numer==other.numer and self.denom==other.denom
        else:
            return float(self) == other
    def __add__(self, other):
        return Fraction(self.numer*other.denom + self.denom*other.numer, self.denom*other.denom)
    def __sub__(self, other):
        return Fraction(self.numer*other.denom - self.denom*other.numer, self.denom*other.denom)
    def __mul__(self, other):
        return Fraction(self.numer*other.numer, self.denom*other.denom)
    def __truediv__(self, other):
        if self.denom*other.numer == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return Fraction(self.numer*other.denom, self.denom*other.numer)

'''
I found an error when testing the addition and subtraction for the class
and fixed the method in the code. The rest of the changes to the unit tests are
noticable in the file.
'''

'''
-------------------------------------------------------------------------------
'''

# Exercise 5

'''
The unit tests cannot be implemented until we have the function ready, but they
would look something like this:

test_count_sets():
    assert ut.count_sets(["1022", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"]) == 6
    pt.raises(ValueError, ut.count_sets, hand = ["1022"]
    pt.raises(ValueError, ut.count_sets, hand = ["1022", "1022", "1022", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"])
    pt.raises(ValueError, ut.count_sets, hand = ["10220112", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"])
    pt.raises(ValueError, ut.count_sets, hand = ["5784", "1122", "0100", "2021", "0010", "2201", "2111", "0020", "1102", "0210", "2110", "1020"])

test_is_set():
    assert ut.is_set("0000", "1111", "2222") == True
    assert ut.is_set("0000", "1000", "0111") == False
'''

'''
-------------------------------------------------------------------------------
'''

# Exercise 6:
import itertools as it
import numpy as np

def is_set(a, b, c):
    '''
    This function takes three string arguments (set cards) and tells me whether
    it is a set or not. It returns True if there is a set, and False if there is
    not a set. It will be implemented in the larger count_sets, so it will not
    raise errors.

    Rebekah had the idea to make a set of the digits of each number. Then, we
    can check to see if the cardinality of the set is 1 or 3. If so, then either
    all the digits are the same or they're all different. If all these sets have
    cardinality 1 or 3, then the cards are in a set! Otherwise, no.
    '''
    digit1set = {a[0], b[0], c[0]}
    digit2set = {a[1], b[1], c[1]}
    digit3set = {a[2], b[2], c[2]}
    digit4set = {a[3], b[3], c[3]}

    digit1good = (len(digit1set) == 1 or len(digit1set) == 3)
    digit2good = (len(digit2set) == 1 or len(digit2set) == 3)
    digit3good = (len(digit3set) == 1 or len(digit3set) == 3)
    digit4good = (len(digit4set) == 1 or len(digit4set) == 3)

    winner = (digit1good == True and digit2good == True and digit3good == True and digit4good == True)

    return winner


def count_sets(cards):
    '''
    This function will take an argument cards which should be a valid hand of 12
    "Set cards," and spit out the number of sets in the hand. The function will
    raise an error if the argument is not a valid set hand, i.e., any of the
    following fails:
        > There are not exactly 12 cards
        > the cards are not unique
        > One or more cards does not have exactly 4 digits.
        > One or more cards has a character other than 0, 1, or 2
    '''
    # Start score counter
    score = 0
    # get all combinations of Three
    threesets = list(it.combinations(cards, 3))
    #pull arguments from the individual triples
    for triple in threesets:
        arg1 = str(triple[0])
        arg2 = str(triple[1])
        arg3 = str(triple[2])
    #Use counter to track how many hands are sets
        if is_set(arg1, arg2, arg3) == True:
            score = score+1
    #errors
    #There are not exactly 12 cards
    if len(cards) != 12:
        raise ValueError("The hand must have exactly 12 cards")
    #The cards are not unique
    if len(cards) == 12 and len(set(cards)) != 12:
        raise ValueError("The cards are not unique")
    #One or more cards does not have exactly four digits
    for i in range(0, len(cards)):
        if len(cards[i]) != 4:
            raise ValueError("One of the cards is not of length 4")
    #One or more cards has a character other than 0, 1, or 2
    for card in cards:
        print(card)
        for i in range(0, 4):
            if (card[i] == '0' or card[i] == '1' or card[i] == '2'):
                pass
            else:
                raise ValueError("One of the cards has a value which is not 0, 1, or 2")
    return score

    '''
    When I finished this, I actually had 100 percent coverage and I didn't have
    to add any unit tests!
    '''
