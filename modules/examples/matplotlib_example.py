"""
This file contains a quick demonstration of matplotlib, a python plotting library.

For more examples, check this out: 
https://matplotlib.org/stable/gallery/index.html 
"""

import numpy as np
import matplotlib.pyplot as plt

# Use numpy to generate 3 random arrays.
# The "normal" function takes a mean, standard deviation, and number of points to generate
# a normally distributed array of data.
seed = 1
x = np.random.default_rng(seed).normal(0, 0.3, 100)
y = np.random.default_rng(seed+1).normal(0, 0.5, 100)
z = np.random.default_rng(seed+2).normal(0, 0.1, 100)

# Create a new matplotlib figure with one row and 3 columns.
fig, ax = plt.subplots(1,3, sharey=True)

ax[0].scatter(x, y)
ax[0].grid(True)
ax[0].axis('equal')
ax[0].set_title('Y vs. X')

ax[1].scatter(x, z)
ax[1].grid(True)
ax[1].axis('equal')
ax[1].set_title('Z vs. X')

ax[2].scatter(y, z)
ax[2].grid(True)
ax[2].axis('equal')
ax[2].set_title('Z vs. Y')

# Save the figure to a file. 
fig.savefig("figure_example.png")

