import numpy as np

#reproduction seed
#genarating radom numbers with a seed to guarantee that the same
#random arrays will be created in each execution.

rng = np.random.default_rng(seed=1701)

x1 = rng.integers(10, size=8) #one-dimensional array
x2 = rng.integers(10, size=(4,7)) #two-dimensional array
x3 = rng.integers(10, size=(4,5,6)) #three-dimensional array
x4 = rng.integers(10, size =(4,5,6,7)) #four-dimensional array

print("one-dimensional \n", x1, "\n")
print("shape: ", x1.shape,"\n")

print("two-dimensional\n", x2, "\n")
print("shape: ", x2.shape, "\n")

print("three-dimensional\n", x3, "\n")
print("shape: ", x3.shape)

print("array four-dimension\n", x4, "\n")
print("shape: ", x4.shape)

