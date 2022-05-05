#%% [markdown]

# # Solve the Consumer Problem
# Consider the following consumer problem:

# $V(p_1, p_2, I) = max_{x_1, x_2} x_1^{a} x_2^{1-a}$ 
# subject to the standard budget constraint

# Solution

# %%

# Paramter selection
alpha = .25
I = 10
p1 = 1
p2 = 2

# Objective function
def objectiveFunction(x1, alpha, I, p1, p2):
    # Transform budget constraint into equality
    x2 = (I - p1*x1)/p2
    # Define utility function
    utility = x1**alpha * x2**(1-alpha)
    return utility

from scipy import optimize

# Since parameters are defined, we create a function that only takes x1
obj = lambda x1: -objectiveFunction(x1, alpha, I, p1, p2)

solution = optimize.minimize_scalar(obj, bounds = (0,I/p1))

x1 = solution.x
x2 = (I-x1*p1)/p2

print(x1, x2)


# %%

# AS AD Model
# Choose Parameters
a = 0.4 
gamma = 0.1
phi = 0.9
delta = 0.8
omega = 0.15
sigma_x = 1
sigma_c = 0.2
T = 100

# synthetic parameters
b = (1 + a * phi * gamma) / (1 + a * gamma)
beta = 1 / (1 + a * gamma) 

# Model functions
def outputGap(y_hat_lag, z, z_lag, s, s_lag):
    y_hat = b * y_hat_lag + beta * (z - z_lag) - a * beta * s + a * beta * phi * s_lag
    return y_hat

def inflationGap(pi_lag, z, z_lag, s, s_lag):
    pi_hat = b * pi_lag + beta * gamma * z - beta * phi * gamma * z_lag + beta * s - beta * phi * s_lag
    return pi_hat

# z is an AR(1) demand shock
def demandShock(z_lag, x):
    z_hat = delta*z_lag + x
    return z_hat

#s is an AR(1) supply shock
def supplyShock(s_lag, c):
    s_hat = omega*s_lag + c
    return s_hat
# %%
import numpy as np

np.random.seed(200149)

# Generate stochastic parameter with mean 0, scale sigma_x, and T=100 entries
x = np.random.normal(loc=0, scale=sigma_x, size=T) 
c = np.random.normal(loc = 0, scale = sigma_c, size = T)

# Generate arrays for z, c, pihat and yhat with length T=100
z = np.zeros(T)
s = np.zeros(T)
y_hat = np.zeros(T)
pi_hat = np.zeros(T)

# %%

#Run simulation

for t in range(1, T):

    # Update z and s. This operation will take set element t in the arrays for z
    # and s and equate them to the output of the functions defined above at t-1
    # and t.

    # demandShock takes z_lag and x as an argument:
    z[t] = demandShock(z[t-1], x[t])
    #supplyShock takes s_lag and c:
    s[t] = supplyShock(s[t-1], c[t])

    # Using the updated values for the random shocks, we compute the equations
    # of motion
    y_hat[t] = outputGap(y_hat[t-1], z[t], z[t-1], s[t], s[t-1])
    pi_hat[t] = inflationGap(pi_hat[t-1], z[t], z[t-1], s[t], s[t-1])



# %%
# Plot
import matplotlib.pyplot as plt
%matplotlib inline

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(y_hat, label = '$\\hat{y}$')
ax.plot(pi_hat, label = '$\\hat{pi}$')

# %%
