import sympy as sp

# Define the variable
t = sp.symbols('t')

# Define the integrand (t + 3t^2)
integrand = t + 3*t**2

# Compute the integral
work = sp.integrate(integrand, (t, 0, 1))

# Display the result
print("The work done by the force field is:", work)
