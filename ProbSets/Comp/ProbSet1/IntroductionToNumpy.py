#Introduction to Numpy

import numpy as np

# Problem 1
# Define matrices
A = np.array([ [3, -1, 4], [1, 5, -9] ])
B = np.array( [ [2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3] ])

# Define function to multiply matrices

def ex1func(a, b):
    '''
    This function takes as inputs two matrices, multiplies them,
    and yields their product as output.
    '''
    prod = (a @ b)
    return prod

# Execute Function
print(ex1func(A, B))

'''
--------------------------------------------------------------
'''
# Exercise 2
# Define function (this time I make the matrix inside the Function)

def ex2func():
    '''
    First, I define the matrix A. Then, I will define B such that
    B = -A^3 +9A -15A. Finally, I output B
    '''
    A = np.array( [ [3, 1, 4], [1, 5, 9], [-5, 3, 1] ] )
    B = (-1) * (A @ A @ A) + (9) * (A @ A) + (-15) * (A)
    return B

print(ex2func())

'''
---------------------------------------------------------------
'''

# Exercise 3

# Define matrices
A = np.ones((7, 7))
A = np.triu(A)

B = np.ones((7,7)) * (-1)
B = B + (6 * A)
Diag6 = np.diag( [6] * 7 )
B = B - Diag6

# Multiply
Prod =(A @ B @ A)
Prod = Prod.astype(np.int64)

print(Prod)

'''
-----------------------------------------------------
'''

# Exercise 4

# Define the Function.


def ex4func(A):
    '''
    This function will take a matrix A as an input. I'll use
    the mask (y < 0) to change all the negative entries of the
    matrix A to 0, and then I'll output the changed matrix A.
    '''

    mask = A < 0
    A[mask] = 0
    return A

# Test

A = np.array( [ [1, -1], [-1, 1] ] )
B = ex4func(A)
print(B)

#It works!

'''
--------------------------------------------------
'''

# Exercise 5


def ex5func():
    '''
    This function defines A, B, and C, and then stacks them into the
    matrix specified in exercise 5. I create some 0 matrices, identity
    matrices, and the transpose of A in the process, and I output a matrix
    called final.
    '''
    # Define A, B, and C.
    A = np.array( [ [0, 2, 4], [1, 3, 5] ] )

    B = np.full( (3, 3), 3 )
    B = np.tril(B)

    C = np.diag( [-2] * 3)

    # Define my identity, transpose and zero matrices

    z3by3 = np.zeros( (3, 3) )
    z2by2 = np.zeros( (2, 2) )
    z3by2 = np.zeros( (3, 2) )
    z2by3 = np.zeros( (2, 3) )
    id3 = np.eye(3)
    Atrans = A.T

    # Create 3 block rows:
    blkrow1 = np.hstack((z3by3, Atrans, id3))
    blkrow2 = np.hstack((A, z2by2, z2by3))
    blkrow3 = np.hstack((B, z3by2, C))

    # Stack the vlock rows on top of each other to make the final matrix
    final = np.vstack((blkrow1, blkrow2, blkrow3))

    # Return the final matrix
    return final

print(ex5func())
'''
-------------------------------------------------------
'''

# Exercise 6
# Define the Function

def ex6func(A):
    '''
    The purpose of this function is to turn A into a "row stochastic"
    matrix. I want to divide each row element by the row sum, and I do
    this with array broadcasting.
    '''
    Rowsum = A.sum(axis=1)
    Rowsum = Rowsum.reshape((-1, 1))
    print(Rowsum)
    Final = A / Rowsum

    return Final

#Test
A = np.array( [ [1, 3], [2, 7] ])
print(ex6func(A))

'''
--------------------------------------------------------------------------------
'''
#Exerise 7

grid = np.load("grid.npy")
'''
The strategy is to use matrix slicing to create 4 matrices which correspond to

'''
horizontal = (grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
hmax= np.max(horizontal)

vertical = (grid[:-3,:] * grid[1:-2,:] * grid[2:-1,:] * grid[3:,:])
vmax = np.max(vertical)

diag1 = (grid[:-3,:-3] * grid[1:-2,1:-2] * grid[2:-1,2:-1] * grid[3:,3:])
diag1max = np.max(diag1)

diag2 = (grid[3:,:-3] * grid[2:-1,1:-2] * grid[1:-2,2:-1] * grid[:-3,3:])
diag2max = np.max(diag2)


allmaxes=[hmax, vmax, diag1max, diag2max]
winner=max(allmaxes)
print("The winner is: ", winner)
