import numpy as np

rng = np.random.default_rng(seed=1701)

x = rng.integers(10, size=(3,4))
print(x,"\n")

#boolean array with values true and false
print(x < 5, "\n")

#selecting the values from array, masking.
#return an unidimensional array with all values lower than 5.
print(x[x < 5])