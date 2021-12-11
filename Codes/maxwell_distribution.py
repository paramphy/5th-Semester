from matplotlib import pyplot as plt
import numpy as np
from scipy import constants

x = np.linspace(0, 10, 10000)

# Maxwell Boltzman distribution
T = 10000.0
k = constants.k
kev = k/constants.e
y = np.exp(-x/(kev*T))
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y, label= str(T) + 'K')  # Plot some data on the axes.
# Plot more data on the axes...
ax.set_xlabel("Energy")  # Add an x-label to the axes.
ax.set_ylabel("Distribution")  # Add a y-label to the axes.
ax.set_title("Maxwell - Boltzman Distribution function")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()

