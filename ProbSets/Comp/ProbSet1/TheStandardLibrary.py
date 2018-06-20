#The Standard Library

#Exercise 1

# Define function using Lamda shortcut
f = lambda L: [min(L), max(L), sum(L)/len(L)]

# Test
L = [1, 2, 3, 4, 5]
print(f(L))

# Great!

'''
----------------------------------------------
'''

# Exercise 2
# int
orig = 5
newname = orig
newname = newname+1
newname == orig
# False -> Immutable

# str
orig = "Hello World"
newname = orig
newname = newname + "Extra"
newname == orig
# False -> Immutable

# list
orig = [1, 2, 3]
newname = orig
newname[1] = 1000
newname == orig
# True ->  Mutable

# Tuple
orig = (1, 2, 3)
newname = orig
newname += (1,)
newname == orig
# False -> immutable

# set
orig = {1, 2, 3, 4, 5}
newname = orig
newname.add("New Thing")
newname == orig
newname==orig
# True -> Mutable

print("Integers, Strings, and Tuples are immutable, while Lists and Sets are mutable.")

'''
-------------------------------------------------------------------
'''
# Exercise 3
import calculator as cr

def pythag(a, b):
    '''
    This function uses the functions I just defined in the calculator module to
    find the length of the hypotenuse of a triangle with legs a, b
    '''
    asq = cr.prodfunc(a, a)
    bsq = cr.prodfunc(b, b)
    csq = cr.sumfunc(asq, bsq)
    c = cr.sqrt(csq)
    return c

print(pythag(3,4))

# Output is 5 - good!
'''
-----------------------------------------------------------------
'''
# Exercise 4
import itertools as it

# Define function
def powerset(A):
    '''
    This function takes the power set of a set A. First, I find the length
    of the set. Then, I find the combinations of the set with all the possible
    sizes from 1 up to the length of the set in a for loop. I concaten'
    ate all
    these combinations together, which should create the power set of A (called
    "final").
    '''

    length = len(A)
    ''' I put in the empty set manually since I don't know how to do it with
    functions. '''
    final = [{}]

    ''' Here's the loop creating the power set:'''

    for x in range(0, length):
        combos = list(it.combinations(A, x+1))
        final = final + combos

    return final

# Test
A = {"one", "two", "three", "four", "five"}
pA = powerset(A)
print(len(pA))
print(pA)

# It works!

'''
-------------------------------------------------------------------------------
'''
