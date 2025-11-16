import numpy as np

# some time qe don't have interest in sort full array, but in deserve found the
# lowest values of array. The result is a new array with the lowest values in the left
# of partition and the others values in the right.

x = np.array([0,3,5,7,5,8,6,7])
print(x, '\n')

ptt_x = np.partition(x, 3)
print(ptt_x, '\n')

# partition in multidimensional array

rng = np.random.default_rng(seed= 45)

x1 = rng.integers(1, 10, size= (4,6))
print(x1, '\n')

ptt_x1 = np.partition(x1, 2,  axis= 1)
print(ptt_x1)