import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# Model Simulation Function
# ==========================================================

def simulate(h, N, x0, y0, alpha=0.0, sigma=0.0, seed=None):
    """
    Simulates the predator-prey system using Euler / Euler-Maruyama.

    Parameters:
        h      : time step
        N      : number of steps
        x0,y0  : initial conditions
        alpha  : damping parameter
        sigma  : noise intensity
        seed   : random seed
    """

    if seed is not None:
        np.random.seed(seed)

    x = np.zeros(N)
    y = np.zeros(N)

    x[0] = x0
    y[0] = y0

    sqrt_h = np.sqrt(h)

    for n in range(N - 1):

        # deterministic part
        dx = x[n] * (2 - y[n]) - alpha * (x[n] ** 2)
        dy = y[n] * (x[n] - 1)

        # update (Euler or Euler-Maruyama)
        x[n + 1] = x[n] + h * dx + sigma * x[n] * sqrt_h * np.random.randn()
        y[n + 1] = y[n] + h * dy + sigma * y[n] * sqrt_h * np.random.randn()

    return x, y


# ==========================================================
# Parameters
# ==========================================================

h = 0.001
N = 20000
x0, y0 = 1.5, 1.0

alpha = 0.1      # damping
sigma = 0.05     # noise intensity


# ==========================================================
# Case 1: Conservative (no damping, no noise)
# ==========================================================

x1, y1 = simulate(h, N, x0, y0, alpha=0.0, sigma=0.0, seed=1)

# ==========================================================
# Case 2: Damped (no noise)
# ==========================================================

x2, y2 = simulate(h, N, x0, y0, alpha=alpha, sigma=0.0, seed=2)

# ==========================================================
# Case 3: Damped + Noise
# ==========================================================

x3, y3 = simulate(h, N, x0, y0, alpha=alpha, sigma=sigma, seed=3)


# ==========================================================
# Plot 1: Phase Plane Comparison
# ==========================================================

plt.figure()
plt.plot(x1, y1, label="Conservative")
plt.plot(x2, y2, label="Damped")
plt.plot(x3, y3, label="Damped + Noise")

plt.axvline(1)
plt.axhline(2)
plt.scatter([1], [2])

plt.xlabel("Prey (x)")
plt.ylabel("Predator (y)")
plt.title("Phase Plane Comparison")
plt.legend()
plt.show()


# ==========================================================
# Plot 2: Distance to Equilibrium
# ==========================================================

r1 = np.sqrt((x1 - 1)**2 + (y1 - 2)**2)
r2 = np.sqrt((x2 - 1)**2 + (y2 - 2)**2)
r3 = np.sqrt((x3 - 1)**2 + (y3 - 2)**2)

plt.figure()
plt.plot(r1, label="Conservative")
plt.plot(r2, label="Damped")
plt.plot(r3, label="Damped + Noise")

plt.xlabel("Time Step")
plt.ylabel("Distance to Equilibrium")
plt.title("Distance to (1,2)")
plt.legend()
plt.show()
