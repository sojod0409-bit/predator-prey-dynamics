# Predator–Prey Dynamics  
## From Conservative Oscillations to Noisy Stable Systems

This project studies the transition from conservative oscillations to damped and stochastic dynamics in a predator–prey system.

---

## Mathematical Model

We analyze the system:

x' = x(2 - y) - α x²  
y' = y(x - 1)

We compute:

- Equilibrium points  
- Jacobian matrix  
- Eigenvalues  
- Stability conditions  

---

## Numerical Experiments

We compare three cases:

1. Conservative system (no damping, no noise)  
2. Damped system  
3. Damped + stochastic noise  

We analyze:

- Phase plane trajectories  
- Distance to equilibrium  
- Effect of numerical methods  

---

## Goal

To understand how damping and stochastic perturbations modify the qualitative behavior of nonlinear dynamical systems.
## Results

### Phase Plane
![Phase Plane](phase_plane.png)

### Distance to Equilibrium
![Distance](distance_plot.png)
---

## Mathematical Stability Analysis

For the damped system:

x' = x(2 - y) - αx²  
y' = y(x - 1)

The interior equilibrium is:

(1, 2 - α)

The Jacobian matrix evaluated at the equilibrium gives:

Trace = -α  
Determinant = 2 - α  

For 0 < α < 2:

- Trace < 0  
- Determinant > 0  

This implies local asymptotic stability.

For α = 0.1, the discriminant is negative, leading to complex eigenvalues with negative real part.  
Therefore, the equilibrium is a **stable spiral (spiral sink)**.

This explains the numerical observations.
