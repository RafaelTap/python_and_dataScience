import numpy as np

#np.all and np.any, can be used in any axis.

rng = np.random.default_rng(seed= 1701)

x = rng.integers(10, size=(3, 4))
print(np.all(x<8, axis= 1))