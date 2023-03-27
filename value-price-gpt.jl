# This code can be used to replicate the examples
# discussed in Chapter 7 of THE LOGIC OF CAPITAL
# This code is also printed in the appendix to
# Chapter 7 in the book

# ------------------------------------------------ #
# ------------ Standard Interpretation ----------- #

# ----- Quantities that are given ------- #

# -- Input-output matrix
A = [186/450 12/450 9/450;
     54/21 6/21 6/21;
     30/60 3/60 15/60]

# -- Labour input vector
l = [18/450, 12/21, 30/60]

# -- Real wage bundle
b = [2, 0, 1/6]

# -- Net output
y = [180, 0, 30]

# Check the dimensions of vectors and matrix
# If number of columns of A is not equal
# to the length of the other three vectors
# do not proceed. Check data.
@show size(A)
@show length(l)
@show length(b)
@show length(y)


# --------- Gross Output --------- #
# Create identity matrix
n = size(A, 2)
I = Matrix{Float64}(I, n, n)

# The "\" operator gives the inverse,
# and * is used for matrix multiplication
# The result will be displayed on screen
Q = (I - A) \ y
@show Q

# --------- Value System --------- #

# Vector of values
λ = l' * (I - A) \ [1; 1; 1]

# Value embodied in the net product ...
@show λ' * y

# Is equal to the total labour to produce gross output
@show l' * Q

# Value of real wage bundle (value of labour power)
vrb = λ' * b
@show vrb

# Rate of exploitation
e = 1 / vrb - 1
@show e


# --------- Price System: 1 --------- #
# Rate of profit calculations

# Maximum eigenvalue of A
λ_mA = maximum(eigen(A).values)

# Maximal rate of profit
R = 1 / λ_mA - 1
@show R

# Augmented input matrix
M = A + b * l'

# Maximum eigenvalue of M
λ_mM = maximum(eigen(M).values)

# Uniform rate of profit
r_e = 1 / λ_mM - 1
@show r_e


# --------- Price System: 2 --------- #
# Relative price calculations

# M1 matrix
M1 = I - (1 / λ_mM) * M

# Pre-multiply M1 with a price vector
# Choose any two equations
# Solve for relative prices
# Here we solve in terms of p3
A1 = M1[1:2, 1:2]
b1 = M1[3, 1:2]
p12 = A1 \ b1

# Relative price vector in terms of p3
p = [-p12; 1]
@show p

# --------- Price System: 3 --------- #
# Using numeraire to close system

# Numeraire = third commodity, i.e. p3=1
p = [-p12; 1]
@show p

# Numeraire = nominal wage rate
# Equation capturing this numeraire:
# 2 * p_1 + 0.167 * p_3 = 1
# To solve for prices, we will
# replace one equation with the
# numeraire equation.

# Transpose of M1
M2 = M1
