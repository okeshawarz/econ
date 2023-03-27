using LinearAlgebra, Statistics, Plots, Latexify
# This code replicates the example discussed in 
# 7.A.4 of Basu(2021).

#### Quantities that are taken as given
# A = input-output matrix
# l = labour-input vector
# w = nominal wage rate
# v = value of labor power
# Q = gross output vector

A = [186/450 54/21 30/60;
     12/450 6/21 3/60;
     9/450 6/21 15/60]

l = [18/450 12/21 30/60]

w = 1

v = 0.515

y = [180 
     0 
     30]

# Compute Gross Output
x = (I-A)\y

# Maximum Eigenvalue of A
λ_mA = eigmax(A)

# Maximal rate of profit
R = (1/λ_mA) - 1

# Define Univariate function of the rate of profit

f(r2) = (1 + r2)w*l*inv((I - (1+r2)A))*(I - A)*x - (w*l*x/v)
h(r2) = (1 + r2)w*l*((I-1+r2)\(I-A)*x) - (w*l*x/v)

# Doesn't work, but it should. Alternate way:
function g(r2)
    D2 = (I-A)*x
    l2 = l
    A2 = A
    L2 = (l*x)/v
    C2 = (I-(1+r2)*A2)
    E2 = C2\D2
    B2 = (1+r2)*l2*E2
    i2 = B2-L2
    return(i2)
end

using Roots
r = find_zero(g, (0, R-0.1))

#WARNING: Value for r given here different than in text. 
#Python gives the same value-- maybe difference in root finding algorithm?

# Solve for prices of production
p = (1+r)*w*l*(inv(I-(1+r)*A))

# Vector of values
Λ = l*inv(I-A)

# MEV
mev = (p*y')/(Λ*y')