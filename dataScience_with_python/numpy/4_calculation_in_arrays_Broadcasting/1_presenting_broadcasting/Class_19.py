import numpy as np

# in this exemple the broadcasting happens in both arrays to become compatible with the same shape

a = np.arange(3)
b = np.arange(3) [:, np.newaxis]

print(a, "\n", b)

# the result is a two-dimensional array
sum_ = a + b
print(sum_)