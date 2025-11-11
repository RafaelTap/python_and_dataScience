import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=1701)

x = rng.normal(size=100)
print(x, "\n")

#create a handmade histogram
bins = np.linspace(-5, 5, 20)

#fast way with one line to plot a histogram, matplotlib provides the routine plt.hist

plt.hist(x, bins, histtype='step')
plt.show()