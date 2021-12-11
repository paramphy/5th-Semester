from matplotlib import pyplot as plt
import numpy as np
from scipy import constants

x = np.linspace(0, 10, 10000)

# Maxwell Boltzman distribution
k = constants.k
kev = k/constants.e
fig, ax = plt.subplots()  # Create a figure and an axes.
for T in range(0,10000,1000):
    y = 1.0/(np.exp((x-5)/(kev*T))+1)
    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    ax.plot(x, y, label= str(T) + 'K')  # Plot some data on the axes.
# Plot more data on the axes...
ax.set_xlabel("Energy")  # Add an x-label to the axes.
ax.set_ylabel("Distribution")  # Add a y-label to the axes.
ax.set_title("Farmi - Dirac Distribution function")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()