# PDE u_tt + f(t, x) * u_t + g(t, x) * u_xx + h(t, x) * u_x = k(t, x)

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["animation.embed_limit"] = 2**128


# Define functions f, g, h, k
f = lambda t, x: 0
g = lambda t, x: -0.01
h = lambda t, x: 0
k = lambda t, x: 0

x = np.linspace(0, 1, 40)
dx = x[1] - x[0]

dt = 0.05
tMax = 15
t = np.linspace(0, tMax, int(tMax / dt))

m = len(t)
n = len(x)

# Boundary conditions
fLeft = lambda t: 0
fRight = lambda t: 0

# Initial conditions
fPosInitial = lambda x: np.exp(-200 * (x - 0.5) ** 2)
fVelInitial = lambda x: 0

# Computing numerical solution
u = np.zeros((m, n))
u[0] = fPosInitial(x)
u[0][0] = fLeft(0)
u[0][-1] = fRight(0)

u[1][0] = fLeft(t[1])
u[1][-1] = fRight(t[1])

for j in range(1, n - 1):
    d2udt2 = (
        k(dt, x[j])
        - f(dt, x[j]) * fVelInitial(x[j])
        - g(dt, x[j]) * (u[0][j - 1] - 2 * u[0][j] + u[0][j + 1]) / dx**2
        - h(dt, x[j]) * (-u[0][j - 1] + u[0][j]) / dx
    )
    u[1][j] = u[0][j] + dt * fVelInitial(x[j]) + dt**2 / 2 * d2udt2

# Useful function to simplify math
r = lambda t, x: dt * dx**2 * f(t, x) + dx**2

for i in range(1, m - 1):
    u[i + 1][0] = fLeft(t[i])
    u[i + 1][-1] = fRight(t[i])

    for j in range(1, n - 1):
        # These coefficients can be derived using discrete derivatives
        coefs = []
        coefs.append(-(dt**2) * g(t[i], x[j]) / r(t[i], x[j]))
        coefs.append(
            dt**2 * dx * h(t[i], x[j]) / r(t[i], x[j])
            + 2 * dt**2 * g(t[i], x[j]) / r(t[i], x[j])
            + dt * dx**2 * f(t[i], x[j]) / r(t[i], x[j])
            + 2 * dx**2 / r(t[i], x[j])
        )
        coefs.append(
            -(dt**2) * dx * h(t[i], x[j]) / r(t[i], x[j])
            - dt**2 * g(t[i], x[j]) / r(t[i], x[j])
        )
        coefs.append(-(dx**2) / r(t[i], x[j]))
        coefs.append(dt**2 * dx**2 / r(t[i], x[j]))

        u[i + 1][j] = (
            coefs[0] * u[i][j - 1]
            + coefs[1] * u[i][j]
            + coefs[2] * u[i][j + 1]
            + coefs[3] * u[i - 1][j]
            + coefs[4] * k(t[i], x[j])
        )


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
