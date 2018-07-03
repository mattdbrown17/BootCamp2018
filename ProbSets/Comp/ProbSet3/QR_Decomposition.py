#QR_Decomposition

import numpy as np
from scipy import linalg

A = np.random.randn(3, 8)

def QR(A):
    '''
    Function accepts arrays of floating-point objects and outputs the
    QR decomposition, using the modified gram-schmidt algorithm.
    '''
    #Store dimensions of A
    dimA = (A.shape)
    # Create copy of A and nxn matrix of zeros
    Q = A.copy()
    R = np.zeros((dimA[1], dimA[1]))
    #Modified QR algorithm
    for i in range(dimA[1]):
        R[i,i] = (linalg.norm(Q[:,i]))
        #Normalize the column of Q
        Q[:,i] = Q[:,i]/linalg.norm(Q[:, i])
        for j in range(i+1, dimA[1]):
            #Orthogonalize other columns of Q wrt ith column
            R[i,j] = (Q[:,j].T @ Q[:,i])
            Q[:,j] = Q[:,j] - (R[i,j] * Q[:,i])
    return Q, R

#Come back here to check/define it in a function.

'''
------------------------------------------------------------------------
'''

# Exercise 2
f = lambda A: np.prod(np.diag(QR(A)[1]))
'''
------------------------------------------------------------------------
'''

#Exercise 3
def solvelinsys(A, b):
    '''
    Accepts matrix A, vector b, solves linear system Ax = b via QR
    decomposition.
    '''
    Q, R = QR(A)[0], QR(A)[1]
    y = Q.T @ b
    d = R.shape[1]
    #Backsolve
    x = np.zeros(d)
    for i in range(d):
        x[d-1-i] = y[d-1-i]
        for j in range (d-1-i, d-1):
            x[d-1-i] = x[d-1-i] - R[d-1-i,j+1]*x[j+1]
        x[d-1-i] = x[d-1-i]/R[d-1-i, d-1-i]
    return x

#Test case
A = np.array([[2, 1, 2, 0], [1, 3, 5, 0], [0, 2, 3, 2], [1, 0, 1, 1]], dtype=float)
b = np.array([3, 4, 2, 1], dtype = float)

print("Ex3 Check (should be near 0):", A @ solvelinsys(A, b) - b)

'''
------------------------------------------------------------------------
'''

#Exercise 4

def Householder(A):
    m, n = A.shape[0], A.shape[1]
    R = A.copy()
    Q = np.identity(m)
    for k in range(0, n):
        u = R[k:, k].copy()
        sign = lambda x: 1 if x>=0 else -1
        u[0] = u[0] + sign(u[0]) * linalg.norm(u)
        u = u / linalg.norm(u)
        R[k:, k:] = R[k:, k:] - 2 * np.outer(u,np.dot(u.T, R[k:,k:]))
        Q[k:, :] = Q[k:, :] - 2 * np.outer(u, np.dot(u.T, Q[k:,:]))
    return Q.T, R

'''
------------------------------------------------------------------------
'''

#Exercise 5

def Hessenberg(A):
        m, n = A.shape[0], A.shape[1]
        H = A.copy()
        Q = np.identity(m)
        for k in range(0, n-2):
            u = H[k+1:,k].copy()
            sign = lambda x: 1 if x>=0 else -1
            u[0] = u[0] + sign(u[0]) * linalg.norm(u)
            u = u / linalg.norm(u)
            H[k+1:,k:] = H[k+1:,k:] - 2 * np.outer(u, (u.T @ H[k+1:,k:]))
            H[:,k+1:] = H[:, k+1:] - 2 * np.outer((H[:,k+1:] @ u), u.T)
            Q[k+1:,:] = Q[k+1:,:] - 2 * np.outer(u, (u.T @ Q[k+1:, :]))
        return H, Q.T

A = np.random.random((8,8))
print(Hessenberg(A)[0])
print(linalg.hessenberg(A))
