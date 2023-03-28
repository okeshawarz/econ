using LinearAlgebra, Roots, Plots

# nxn IO matrix
A = [186/450 54/21 30/60
     12/450 6/21 3/60
     9/450 6/21 15/60]

# 1xn direct labor input vector
l = [18/450 12/21 30/60]

# nominal wage rate
w = 1

# value of labor-power
v = (1/3)

# nx1 net output vector
y = [180; 0; 30;;]

# Gross output
Q = (I-A)\y

# Maximum  eigenvalue of A
λ_mA = eigmax(A)

# Maximal rate of profit
R = (1/λ_mA) - 1

# WORKS FINE UP UNTIL HERE

# univariate function of r:
# (This generates a 1x1 matrix so just take the first element)

f(r2) = ((1+r2)*w*l*inv(I-(1+r2)A)*(I-A)Q - (w*l*Q/v))[1]

r = find_zeros(f, (0, R-0.01))[1]

#GREAT SUCCESSSSSSSSSSSSSSSS

# Vector of prices of production
p = (1+r)*w*l*(inv(I-(1+r)A))

# Vector of values
Λ = l*inv(I-A)

# MEV/MELT
melt = (p*y)/(Λ*y)