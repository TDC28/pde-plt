# This is a PDE (wave equation) demo, used as a starter to this project.

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["animation.embed_limit"] = 2**128


def tridiag(a: int, b: int, c: int, n: int):
    """
    Creates a tridiagonal matrix with values a, b, c
    """
    a_list = [a] * (n - 1)
    b_list = [b] * n
    c_list = [c] * (n - 1)

    return np.diag(a_list, -1) + np.diag(b_list) + np.diag(c_list, 1)


x = np.linspace(0, 1, 100)
n = len(x)
dt = 0.2
dx = x[1] - x[0]
tMax = 150
c = 0.02
r = c * dt / dx

# Boundary conditions
fLeft = lambda t: 0
fRight = lambda t: 0

# Initial conditions
fPosInitial = lambda x: np.exp(-200 * (x - 0.5) ** 2)
fVelInitial = lambda x: 0

# Computing solution
A = tridiag(r**2, 2 * (1 - r**2), r**2, n)
u = fPosInitial(x)
u[0] = fLeft(0)
u[-1] = fRight(0)
u = np.array([u])

t = np.linspace(0, tMax, int(tMax / dt))

for i in range(len(t)):
    if i == 0:
        u = np.append(u, np.array([0.5 * (A @ u[0]) + dt * fVelInitial(x)]), axis=0)

    else:
        u = np.append(u, np.array([A @ u[i] - u[i - 1]]), axis=0)

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
