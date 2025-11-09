import numpy as np

rng = np.random.default_rng(seed=1701)

x = rng.integers(12, size=(3,4))
print(x, "\n")

#to more advantage operations, the fancy indexing can be combined with others indexing schemes already saw.
# we can combine the simple indexing with fancy indexing
x_1 = x[2, [2, 0, 1]]
print(x_1, "\n")

#fancy indexing with slicing
x_2 = x[:, [2, 0, 1]]
print(x_2, "\n")

#fancy indexing with mask
row = np.array([0, 1, 2])
mask = np.array([True, False, True, False])
x_3 = x[row[:, np.newaxis], mask]

print(x_3)