import sympy as sp

# Define the variable t
t = sp.symbols('t')

# Define the integrand (i * exp(3i*t))
integrand = sp.I * sp.exp(3 * sp.I * t)

# Compute the integral from 0 to 2*pi
integral_result = sp.integrate(integrand, (t, 0, 2 * sp.pi))

# Display the result
print("The value of the line integral is:", integral_result)
