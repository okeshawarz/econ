using LinearAlgebra, Statistics, Plots, LaTeXStrings, Latexify 
# Technology Matrix
A = [186/450 54/21 30/60;
     12/450 6/21 3/60;
     9/450 6/21 15/60]


# Labor input Vector
l = [18/450, 12/21, 30/60]

# Real Wage Bundle
b = [2, 0, 1/6]

# Net output
y = [180, 0, 30]

#latexify(round.(A; digits = 3)) |> render

# Check that dimensions are correct
size(A)[1] == length(l) & length(b) & length(y)

#### Gross Output Vector
x = inv(I - A) * y 
λ = l' * inv(I - A)
w = λ * b

eigmax = maximum(eigvals(A))
R_max = (1/(eigmax)) - 1

# Check: Value embodied in the net product is equal to the 
# total labor required to produce the gross output
λ * y == l' * x

# Value of the real wage bundle
V_lp = λ * b

# Rate of Exploitation
e = (1 - V_lp) / 1

# Average rate of profit given non-zero wage bundle
M = A + (b * l')
eigmax_m = maximum(eigvals(M))
r_avg = (1/(eigmax_m) - 1) # Nice, bro, nice

#### Relative Prices
# Calculate the prices of production such that 
# the uniform rate of profit is 0.185 in all industries
z = zeros(1,3)

M_p = (I - (1/eigmax_m) * M)

# Since M_p is linearly dependent, we can  only solve for relative prices,
# i.e setting one commodity to be the numeraire, i.e. obtaining the price vector
# in terms of p_3

# Choose first 2 equations to solve for 3rd
A1 = M_p[1:2, 1:2] #Matrix containing [M11 M12]
                   #                  [M21 M22]
b1 = M_p[3, 1:2]   #Vector containing [M31 M32]
p_12 = A1'\b1
p = push!(-p_12, 1) # The vector of prices given p_3 = 1

# Closing the  system with a numeraire

# Let the numeraire equal the nominal wage rate
M2 = M_p'

# Nominal wage coefficient
w_coeff = Base.vect(2, 0, 1/6)
M3 = vcat(M2[1:2, 1:3], w_coeff')

# RHS vector to solve Ax = b
b_n = Base.vect(0, 0, 1)
p_nwage = M3\b_n
p, p_nwage

#### Closing the system with invariance principles

# Invariance princpile 1: net output expressed in prices (y) is equivalent 
# to net output in values (Λ)

# set y = Λ to obtain 6p_1 + p_3 = 2:
inv1 = [6 0 1]

# Use inv1 as the third equation in augmented matrix (instead of 
# the nominal wage as before)
M4 = vcat(M2[1:2, 1:3], inv1)
binv1 = [0 0 2] 

p_inv1 = M4\binv1'

