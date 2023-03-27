import numpy as np

# ----- Quantities that are given ------- #

# -- Input-output matrix
A = np.array([[186/450, 12/450, 9/450],
              [54/21, 6/21, 6/21], 
              [30/60, 3/60, 15/60]])

# -- Labour input vector
l = np.array([18/450, 12/21, 30/60])

# -- Real wage bundle
b = np.array([2, 0, 1/6])

# -- Net output
y = np.array([180, 0, 30])

# Check the dimensions of vectors and matrix
# If number of columns of A is not equal
# to the length of the other three vectors
# do not proceed. Check data.
print(A.shape)
print(l.shape)
print(b.shape)
print(y.shape)


# --------- Gross Output --------- #
# Create identity matrix
n = A.shape[1]
I = np.identity(n)

# The "inv" function gives the inverse, 
# and @ is used for matrix multiplication
# The result will be displayed on screen
Q = np.linalg.inv(I - A) @ y
print(Q)


# --------- Value System --------- #

# Vector of values
lambda_vec = l @ np.linalg.inv(I - A)
print(lambda_vec)

# Value embodied in the net product ...
print(lambda_vec @ y)

# Is equal to the total labour to produce gross output
print(l @ Q)

# Value of real wage bundle (value of labour power)
vrb = lambda_vec @ b
print(vrb)

# Rate of exploitation
e = (1/vrb) - 1
print(e)


# --------- Price System: 1 --------- #
# Rate of profit calculations

# Maximum eigenvalue of A
jj_A = np.linalg.eigvals(A)
lambda_mA = max(jj_A)
print(lambda_mA)

# Maximal rate of profit
R = (1/lambda_mA) - 1
print(R)

# Augmented input matrix
M = A + np.outer(b, l)

# Maximum eigenvalue of M
jj_M = np.linalg.eigvals(M)
lambda_mM = max(jj_M)
print(lambda_mM)

# Uniform rate of profit
r_e = (1/lambda_mM) - 1
print(r_e)


# --------- Price System: 2 --------- #
# Relative price calculations

# M1 matrix
M1 = I - (1/lambda_mM) * M

# Pre-multiply M1 with a price vector
# Choose any two equations
# Solve for relative prices
# Here we solve in terms of p3
A1 = M1[0:2, 0:2]
b1 = M1[2, 0:2]
p12 = np.linalg.solve(A1.T, b1)

# Relative price vector in terms of p3
p = np.concatenate((-p12, [1]))
print(p)


# --------- Price System: 3 --------- #
# Using numeraire to close system

# Numeraire = third commodity, i.e. p3=1
p = np.concatenate((-p12, [1]))
print(p)

# Numeraire = nominal wage rate
# Equation capturing this numeraire:
# 2 * p_1 + 0.167 * p_3 = 1
# To solve for prices, we will
# replace one equation with the
# numeraire equation.

# Trans
