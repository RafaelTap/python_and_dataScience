import numpy as np

rng = np.random.default_rng(seed= 1701)

x = rng.integers(10, size= (3,4))
print(x)

print(x < 6)

