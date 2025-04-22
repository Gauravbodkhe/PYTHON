import numpy as np
from scipy.integrate import quad

# Function to integrate for a fixed x and y
def integrand(z, x, y):
    return 1  # We are integrating the function 1, to get volume

# Limits for y given x
def limits_y(x):
    return -np.sqrt(4 - x**2), np.sqrt(4 - x**2)

# Limits for z given x and y
def limits_z(x, y):
    return -np.sqrt(4 - x**2 - y**2), np.sqrt(4 - x**2 - y**2)

# Perform the integration in steps
def volume_of_sphere():
    volume, _ = quad(lambda x: quad(lambda y: quad(lambda z, x=x, y=y: integrand(z, x, y),*limits_z(x, y))[0],*limits_y(x))[0], -2, 2)
    return volume
z
# Calculate the volume
vol = volume_of_sphere()

# Display the result
print(f"The volume of the sphere is: {vol}")
