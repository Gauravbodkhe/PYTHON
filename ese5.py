# Make sure matplotlib is installed first:
# You can install it with: pip install matplotlib

#Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt 
import numpy as np


# Define the coordinates
x = [1, 8]
y = [3, 10]

# Plotting the line
plt.plot(x, y, color='blue', marker='o')  # Line from (1, 3) to (8, 10)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Show the plot
plt.show()
