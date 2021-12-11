from matplotlib import pyplot as plt
import numpy as np
from scipy import constants

x = np.linspace(0.1, 1, 1000)

# Maxwell Boltzman distribution
T = 10000.0
k = constants.k
kev = k/constants.e
ymb = np.exp(-x/(kev*T))
ybe = 1.0/(np.exp(x/(kev*T))-1.0)
yfd = 1.0/(np.exp(x/(kev*T))+1.0)
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, ymb, label= "MB distribution")  # Plot some data on the axes.
ax.plot(x, ybe, label= "BE distribution")
ax.plot(x, yfd, label= "FD distribution")
# Plot more data on the axes...
ax.set_xlabel("Energy")  # Add an x-label to the axes.
ax.set_ylabel("Distribution")  # Add a y-label to the axes.
ax.set_title("Comparision of distribution functions")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()