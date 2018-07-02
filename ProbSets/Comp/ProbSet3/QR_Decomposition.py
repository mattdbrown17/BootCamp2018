#QR_Decomposition

#Apply Gram-Schmidt algorithm
import numpy as np
from scipy import linalg

A = np.random.rand(5, 5)
#Store dimensions of A
dimA = (A.shape)
# Create copy of A and nxn matrix of zeros
Q = A
print(Q, Q.T)

R = np.zeros((dimA[1], dimA[1]))
for i in range(dimA[1]):
    R[i,i] = (linalg.norm(Q[:,i]))
    #Normalize the column of Q
    Q[:,i] = Q[:,i]/linalg.norm(Q[:,i])
    for j in range(i+1, dimA[1]):
        #Orthogonalize other columns of Q wrt ith column
        R[i,j] = np.vdot(Q[:,j], Q[:,i])
        Q[:,j] = Q[:,j] - (R[i,j] * Q[:,i])

print("Here is Q", Q, "Here is R", R, "Here is QR-A", np.matmul(Q,R)-A)
print(np.vdot(Q[:,0], Q[:,3]))
#THIS IS WRONG
