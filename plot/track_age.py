import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
exponent = -1.5
const_exp = 0.77686983985157021
x = np.array(range(0, 60))
y = (1.0 - np.exp(exponent * x / 60)) / const_exp

# Create the plot
plt.plot(x, y)

# Show the plot
plt.show()
