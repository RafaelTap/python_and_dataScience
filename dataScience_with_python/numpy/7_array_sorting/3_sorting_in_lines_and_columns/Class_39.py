import numpy as np

rng = np.random.default_rng(seed=45)

x = rng.integers(0, 10, size=(4, 6))
print(x, '\n')

sorted_x = np.sort(x, axis=0) #sort columns
print(sorted_x, '\n')

sorted_x2 = np.sort(x, axis=1)
print(sorted_x2)

# this sort used like this, treat each line and each column like a independent array and
# any relationship between the values of lines or values of column will be lost.
