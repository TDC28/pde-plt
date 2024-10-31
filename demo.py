# This is a PDE (wave equation) demo, used as a starter to this project.

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["animation.embed_limit"] = 2**128


def tridiag(a: float, b: float, c: float, n: int):
    """
    Creates a tridiagonal matrix with values a, b, c
    """
    a_list = [a] * (n - 1)
    b_list = [b] * n
    c_list = [c] * (n - 1)

    return np.diag(a_list, -1) + np.diag(b_list) + np.diag(c_list, 1)


x = np.linspace(0, 1, 40)
dx = x[1] - x[0]

dt = 0.05
tMax = 15
t = np.linspace(0, tMax, int(tMax / dt))

c = 0.01
r = c * dt / dx
n = len(x)

# Boundary conditions
fLeft = lambda t: 0
fRight = lambda t: 0

# Initial conditions
fPosInitial = lambda x: np.exp(-200 * (x - 0.5) ** 2)
fVelInitial = lambda x: 0

# Computing solution
A = tridiag(r**2, 2 * (1 - r**2), r**2, n)

u = np.zeros((len(t), n))
u[0] = fPosInitial(x)
u[0][0] = fLeft(0)
u[0][-1] = fRight(0)

u[1] = 0.5 * (A @ u[0]) + dt * fVelInitial(x)
u[1][0] = fLeft(dt)
u[1][-1] = fRight(dt)


for i in range(1, len(t) - 1):
    u[i + 1] = A @ u[i] - u[i - 1]
    u[i + 1][0] = fLeft(t[i])
    u[i + 1][-1] = fRight(t[i])

# Plotting
fig, ax = plt.subplots()

line = ax.plot(x, u[0])[0]
ax.set(xlim=[0, 1], ylim=[-2, 2])


def update(frame):
    y_data = u[frame]
    line.set_xdata(x)
    line.set_ydata(y_data)
    return line


ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=15)
plt.show()
