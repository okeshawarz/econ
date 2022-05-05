#%% [markdown]

# $$ \dot x = 2x -y $$
# $$ \dot y = x - y $$



# %%
import sympy
import numpy as np
import matplotlib.pyplot as plt
from sympy.plotting import plot as symplot

%matplotlib inline

# symbols
x, y = sympy.symbols('x, y')

# equations of motion
xdot = 2*x - y
ydot = x - y

print(xdot, ydot)
# %%

# Set equations equal to 0
x_ss = sympy.Eq(xdot, 0)
y_ss = sympy.Eq(ydot, 0)

# solve for steady state
x_eq = sympy.solve(x_ss, x)
y_eq = sympy.solve(y_ss, y)

x_eq, y_eq

# %%
# Lambdify the functions to solve numerically. Change to numpy
x_num = sympy.lambdify([x, y], xdot, "numpy")
y_num = sympy.lambdify([x, y], ydot, "numpy")
x_num, y_num

# %%

def sol1(xy, t):
    x, y = xy
    dxdt = x_num(x, y)
    dydt = y_num(x, y)
    return np.array([dxdt, dydt])

fig1 = plt.figure(figsize=(8,6)) # Begin a figure with the given dimensions
ax1 = fig1.add_subplot(1,1,1) # Add a subplot for the nullclines

# Create a grid of 20x20 from -10 to 10
x1 = np.linspace(-10, 10, 20)
y1 = np.linspace(-10, 10, 20)

# for xdot = 0 (y = 2x). ax plot format is [x1, x2], [y1, y2]
ax1.plot([-5,5],[-10,10], 'b', lw=2, label = 'x nullcline')

# for ydot = 0 (y=x)
ax1.plot([-10, 10], [-10, 10], 'b', lw = 2, label = 'y nullcline')


x1, y1 = np.meshgrid(x1, y1)
t = 0
u, v = np.zeros(x1.shape), np.zeros(y1.shape)
ni, nj = x1.shape
for i in range(ni):
    for j in range(nj):
        x=x1[i, j]
        y=y1[i,j]
        yprime = sol1([x, y], t)
        u[i,j] = yprime[0]
        v[i, j] = yprime[1]
#Q = plt.quiver(x1, y1, u, v, color = 'r')
V = plt.streamplot(x1, y1, u, v, color='r')

## Success!!

# %% [markdown]

# #Problem 2
# $$ \dot x = -x + y $$
# $$ \dot y = -x - y $$

#%%

%reset

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x, y = sp.symbols('x y')

# Equations of motion
xdot = - x + y
ydot = - x - y

# %%

# Set equal to 0 to find steady state
x_ss = sp.Eq(xdot, 0)
y_ss = sp.Eq(ydot, 0)

# %%
# Solve for equilibrium levels of x and y
x_eq = sp.solve(x_ss, x)
y_eq = sp.solve(y_ss, y)
x_eq, y_eq

# %%
x_num = sp.lambdify([x, y], xdot, "numpy")
y_num = sp.lambdify([x, y], ydot, "numpy")
x_num, y_num

# %%

def sol1(xy, t):
    x, y = xy
    dxdt = x_num(x, y)
    dydt = y_num(x, y)
    return np.array([dxdt, dydt])

fig1 = plt.figure(figsize=(8,6)) # Begin a figure with the given dimensions
ax1 = fig1.add_subplot(1,1,1) # Add a subplot for the nullclines

# Create a grid of 20x20 from -10 to 10
x1 = np.linspace(-10, 10, 20)
y1 = np.linspace(-10, 10, 20)

# for xdot = 0 (y=x)
ax1.plot([-10,10],[-10,10], 'b', lw=2, label = 'x nullcline')

# for ydot = 0 (y=-x)
ax1.plot([-10, 10], [10, -10], 'b', lw = 2, label = 'y nullcline')


x1, y1 = np.meshgrid(x1, y1)
t = 0
u, v = np.zeros(x1.shape), np.zeros(y1.shape)
ni, nj = x1.shape
for i in range(ni):
    for j in range(nj):
        x=x1[i, j]
        y=y1[i,j]
        yprime = sol1([x, y], t)
        u[i,j] = yprime[0]
        v[i, j] = yprime[1]
#Q = plt.quiver(x1, y1, u, v, color = 'r')
V = plt.streamplot(x1, y1, u, v, color='r')

%reset
# %% [markdown]

# # Problem 3
# $$ \dot x =  exp x - y $$
# $$ \dot y = - x - y + 1 $$
#

# %%
import sympy
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

x, y = sympy.symbols('x y')
xdot = sympy.exp(x) - y
ydot = - x - y + 1

# Find zeros
x_ss = sympy.Eq(xdot, 0)
y_ss = sympy.Eq(ydot, 0)
x_ss, y_ss

# %%

x_eq = sympy.solve(x_ss, x)
y_eq = sympy.solve(y_ss, y)
x_eq, y_eq


# %%
x_num = sympy.lambdify([x, y], xdot, np)
y_num = sympy.lambdify([x, y], ydot, np)

# %%
def sol1(xy, t):
    x, y = xy
    dxdt = x_num(x, y)
    dydt = y_num(x, y)
    return np.array([dxdt, dydt])

# %%
fig1 = plt.figure(figsize=(8,6)) # Begin a figure with the given dimensions
ax1 = fig1.add_subplot(1,1,1) # Add a subplot for the nullclines

# Create a grid of 20x20 from -10 to 10
x1 = np.linspace(-10, 2.5, 20)
y1 = np.linspace(-10, 10, 20)

# for xdot = 0
ax1.plot(x1, np.exp(x1))

# for ydot = 0
#ax1.plot(x, 1-x, 'b', lw = 2, label = 'y nullcline')
ax1.plot(x1, 1-x1)


x1, y1 = np.meshgrid(x1, y1)
t = 0
u, v = np.zeros(x1.shape), np.zeros(y1.shape)
ni, nj = x1.shape
for i in range(ni):
    for j in range(nj):
        x=x1[i, j]
        y=y1[i,j]
        yprime = sol1([x, y], t)
        u[i,j] = yprime[0]
        v[i, j] = yprime[1]
#Q = plt.quiver(x1, y1, u, v, color = 'r')
V = plt.streamplot(x1, y1, u, v, color='r')

%reset

# %% [markdown]

# # Problem 4
# $$ \dot x = x - y $$
# $$ \dot y = dx - 0.5y $$


# %%
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

x, y = sp.symbols('x y')
xdot = x - y
ydot = 2 * x - 0.5 * y

x_eq = sp.solve(xdot, x)
y_eq = sp.solve(ydot, y)

# %%
x_num = sp.lambdify([x, y], xdot, "numpy")
y_num = sp.lambdify([x, y], ydot, "numpy")
x_num, y_num

# %%

def sol1(xy, t):
    x, y = xy
    dxdt = x_num(x, y)
    dydt = y_num(x, y)
    return np.array([dxdt, dydt])

fig1 = plt.figure(figsize=(8,6)) # Begin a figure with the given dimensions
ax1 = fig1.add_subplot(1,1,1) # Add a subplot for the nullclines

# Create a grid of 20x20 from -10 to 10
x1 = np.linspace(-10, 10, 20)
y1 = np.linspace(-10, 10, 20)

# for xdot = 0 (y=x)
ax1.plot(x1, x1, 'b', lw=2, label = 'x nullcline')

# for ydot = 0 (y=-x)
ax1.plot(y1, 0.25 * y1, 'b', lw = 2, label = 'y nullcline')


x1, y1 = np.meshgrid(x1, y1)
t = 0
u, v = np.zeros(x1.shape), np.zeros(y1.shape)
ni, nj = x1.shape
for i in range(ni):
    for j in range(nj):
        x=x1[i, j]
        y=y1[i,j]
        yprime = sol1([x, y], t)
        u[i,j] = yprime[0]
        v[i, j] = yprime[1]
#Q = plt.quiver(x1, y1, u, v, color = 'r')
V = plt.streamplot(x1, y1, u, v, color='r')


# %%
