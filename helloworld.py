import matplotlib.pyplot as plt
import numpy as np

# define a linear function
 
def f(x):
    return x

def g(x):
    return np.cos(x)

def h(x):
    return np.sin(x/2)

burntime = 10
maxThrust = 2000

x = np.linspace(0, burntime, 1000)

y1 = f(x)
y2 = g(x)
y3 = h(x)


fig, ax = plt.subplots()

ax.plot(x, y1)
ax.set_xlim(0, burntime)
ax.set_ylim(0,20)

ax.plot(x, y2)
ax.set_xlim(0, burntime)
ax.set_ylim(0,20)

ax.plot(x, y3)
ax.set_xlim(0, burntime)
ax.set_ylim(0,20)

plt.show()

# calculate line integral


