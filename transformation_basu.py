from ctypes import sizeof
import scipy.linalg as la
import numpy as np

# Technology matrix
A = np.array(
        [[186/450, 54/21, 30/60],
         [12/450,  6/21 ,  3/60],
         [9/450,   6/21 , 15/60]])

# Labor input vector
l = np.array([18/450, 12/21, 30/60])

# Real Wage Bundle
b = np.array([2, 0, 1/6])

# Net Output:
y = np.array([180, 0, 30])

# Check dimensions:
len(A) == len(l) & len(b) & len(y) 

#### Gross Output Vector
x = la.inv(np.eye(3) - A) @ y
lam = np.transpose(l) @ la.inv(np.eye(3) - A) 
w = lam @ b

eigmax = max(la.eigvals(A))
R_max = 1/(eigmax) - 1

# Check: Value embodied in the net product is equal to the total labor
# required to produce the gross output.



