using LinearAlgebra, Statistics, Plots, LaTeXStrings, Latexify 
# Technology Matrix
A = [186/450 54/21 30/60;
     12/450 6/21 3/60;
     9/450 6/21 15/60]

latexify(round.(A; digits = 3)) |> render

# Labor input Vector
l = [18/450, 12/21, 30/60]
latexify(l)

# Real Wage Bundle
b = [2, 0, 1/6]
latexify(b)

# Net output
y = [180, 0, 30]

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
