import numpy as np

x = np.array([range(10)])
print(x, "\n")

x_sum = np.sum(x)
print(x_sum, "\n")

rng = np.random.default_rng()
y = rng.random(100)
print(y, "\n")

# use np.sum() is faster than sum() - check with ipython
# np.sum() can work with multidimensional arrays
# np.sum(x, 1) works along the axis with value 1, sum(x, 1)
# begging the sum in 1.
y_sum = np.sum(y)

print(y_sum)
