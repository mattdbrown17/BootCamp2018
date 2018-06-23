"""
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
"""
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

# Exercise 5

# Prompt user for name (Argv1), time in seconds (argv2)

import sys

if len(sys.argv) == 3:
    print("Hello,", sys.argv[1], "You've requested to play Shut the Box with a time limit of", sys.argv[2], " seconds. Here we go!")
else:
    print("Three total command line arguments are required")
    print("System Arguments:", sys.argv)

#import packages

import time
import numpy as np
import random
from itertools import combinations

'''
I start by creating many objects which will be useful in the game.

The box will be a 2x9 array with the values one through nine on the top row and
truth values 1 and 0 on the bottom. 1 corresponds to "closed", 0 to "open." The
game starts with all elements having value 0, the goal is to get them all to 1.
'''

box = np.zeros((2, 9), dtype=int)
for i in range (0, 9):
    box[0, i] = i+1

''' numbers will help me with the dice roll. '''
numbers = [1, 2, 3, 4, 5, 6]

''' Define time limit using system argument '''
timelimit = float(sys.argv[2])

'''Define things related to win condition'''
gameover = 0
win = 0

''' Define function for parsing player input. '''

def parse_input(player_input, remaining):
    """Convert a string of numbers into a list of unique integers, if possible.
    Then check that each of those integers is an entry in the other list.

    Parameters:
        player_input (str): A string of integers, separated by spaces.
            The player's choices for which numbers to remove.
        remaining (list): The list of the numbers that still need to be
            removed before the box can be shut.

    Returns:
        A list of the integers if the input was valid.
        An empty list if the input was invalid.
    """
    try:
        choices = [int(i) for i in player_input.split()]
        if len(set(choices)) != len(choices):
            raise ValueError
        if any([number not in remaining for number in choices]):
            raise ValueError
        return choices
    except ValueError:
        return []

''' Define function for checking if roll causes game to end '''

def isvalid(roll, remaining):
    '''
    Check to see whether or not a roll is valid. That is, check if there
    exists a combination of the entries of 'remaining' that sum up to
    'roll'.

    Parameters:
        roll (int): The value of a dice roll, between 2 and 12
                    (inclusive).
        remaining (list): The list of the numbers that still need to be
                          removed before the box can be shut.

    Returns:
        True if the roll is valid.
        False if the roll is invalid.
    '''
    if roll not in range(2, 13):
        return False
    for i in range(1, len(remaining) + 1):
        if any([sum(combo) == roll for combo in combinations(remaining, i)]):
            return True
    return False

''' Define function for seeing if the choices the player gives are valid.'''
'''
def isinremaing(clean_input, remaining)

'''

''' We're about to start the game, so I'll also take the start time here. '''
starttime = time.time()

'''
*****************************************************************************
'''

'''
Now I'll start playing the turns. At the beginning of each turn, several things
happen:
1) Dice are rolled
2) Check for a win/loss condition.
3) Current box is displayed
4) Dice roll is displayed
5) Seconds left are displayed
Then, I prompt the player for his move.
After the prompt, I parse the move and the box is modified accordingly

The while loop runs until the gameover counter turns to 1. Then, I display
an appropriate message depending on the win counter.
'''

while gameover==0:
    #Roll the dice
    roll = random.choice(numbers) + random.choice(numbers)
    # Determine how much time is left.
    currenttime = time.time()
    timeleft = (timelimit - (currenttime - starttime))
    #Determine which numbers are left in the box.
    remaining = []
    for i in range(0, 9):
        if box[1, i]==0:
            remaining = remaining + [box[0, i]]
    #Display the state of the game
    print("Remaining numbers: ", remaining)
    print("You Rolled:", roll)
    print("You have", round(timeleft), "Seconds left.")
    # If all the numbers are "shut,"" the game is over and I've won.
    if np.sum(box[1, :])==9:
        print("Well done. You Win!")
        win=1
        break
    #If the roll makes the player lose, end the game
    if isvalid(roll, remaining) == False:
        print("You're out of possible moves. You lose. Try harder next time!")
        break
    # If player is out of time, end the game.
    if timeleft<0:
        print("Gotta be quicker than that. Time's up! You lose.")
        break
    if timeleft < timelimit/4:
        print("Better hurry up!")

    '''
    It is time for the player's move. I do the whole thing inside a while loop,
    and I change the counter moveworked once the player puts in a valid move and
    I modify the box. If he doesn't do a valid move, I give an error message and
    spit him back to the beginning.
    '''
    moveworked = 0
    while moveworked == 0:
        #Prompt the player for his move.
        player_input = input("Numbers to eliminate:")
        # Parse input/check if input is valid.
        clean_input = parse_input(player_input, remaining)
        print(clean_input)
        # If the move is not of the valid form, then send the user back.
        if clean_input == []:
            print("Invalid move. Try again!")
        # If not, carry on.
        else:
            # If the move is valid, check if the sum of the input is equal to roll.
            if np.sum(clean_input)==roll:
                #Carry on
                for i in range(1, 10):
                    if i in clean_input:
                        box[1, i-1] = 1
                        moveworked = 1
            else:
                # Send the user back if sum of input is not equal to roll
                print("Invalid move - check your addition :)")
