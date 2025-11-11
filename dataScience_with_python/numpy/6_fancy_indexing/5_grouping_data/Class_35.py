import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=1701)

x = rng.normal(size=100)
print(x, "\n")

#create a handmade histogram
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

#finds appropriate track to each x
i = np.searchsorted(bins, x)

#add 1 to each of these categories
np.add.at(counts, i, 1)

plt.plot(bins, counts, drawstyle='steps')
plt.show()
