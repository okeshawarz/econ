using Symbolics, DifferentialEquations, Plots, Latexify
import SymPy as sp

x, y, z = sp.@vars x y z
xdot = 2 * x - y
ydot = x - y

x_ss = sp.Eq(xdot, 0)
y_ss = sp.Eq(ydot, 0)
x_eq = sp.solve(x_ss, x)
y_eq = sp.solve(y_ss, y)

#Alternate: 

rhs = [2x - y,
       x - y]

fps = sp.solve(rhs, [x, y])

# Jacobian
J = rhs.jacobian([x, y])

