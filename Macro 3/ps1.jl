using Symbolics, DifferentialEquations, Plots, Latexify
import SymPy

### a

@variables t x y
D = Differential(t)
eqs = [0 ~ 2x - y,
       0 ~ x - y]

sol = Symbolics.solve_for(eqs, [x, y])
latexify(sol)  |> render