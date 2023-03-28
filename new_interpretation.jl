using LinearAlgebra, Roots, Plots

A = [186/450 54/21 30/60
     12/450 6/21 3/60
     9/450 6/21 15/60]
l = [18/450 12/21 30/60]
w = 1
v = (1/3)
y = [180; 0; 30;;]
Q = (I-A)\y
λ_mA = eigmax(A)
R = (1/λ_mA) - 1
f(r2) = ((1+r2)*w*l*inv(I-(1+r2)A)*(I-A)Q - (w*l*Q/v))[1]
r = find_zeros(f, (0, R-0.01))[1]
p = (1+r)*w*l*(inv(I-(1+r)A))

# Vector of values
Λ = l*inv(I-A)

# MEV/MELT
melt = (p*y)/(Λ*y)