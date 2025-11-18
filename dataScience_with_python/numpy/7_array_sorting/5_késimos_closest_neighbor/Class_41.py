import numpy as np
import matplotlib.pyplot as plt

# let's see how use the function argsort() in multiples axes to found the closest neighbor
# at a certain point in a set.
rng = np.random.default_rng(seed=42)

x = rng.random((10,2))
print(x)

# how the points are distributed
plt.style.use('seaborn-v0_8-whitegrid')
plt.scatter(x[:,0], x[:,1], s=100)
plt.show()


